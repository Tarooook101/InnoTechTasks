

using ConsoleApp1.Models;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Management;

namespace ConsoleApp1.Services;

public class SystemInfoService
{
    private readonly ILogger<SystemInfoService> _logger;
    private readonly PerformanceCounter? _cpuCounter;
    private readonly PerformanceCounter? _availableMemoryCounter;

    public SystemInfoService(ILogger<SystemInfoService> logger)
    {
        _logger = logger;

        try
        {
            _cpuCounter = new PerformanceCounter("Processor", "% Processor Time", "_Total");
            _availableMemoryCounter = new PerformanceCounter("Memory", "Available MBytes");

            // Initialize counters with first reading
            _cpuCounter.NextValue();
            _availableMemoryCounter.NextValue();
        }
        catch (Exception ex)
        {
            _logger.LogWarning("Failed to initialize performance counters: {Error}", ex.Message);
        }
    }

    public async Task<SystemEvent> GetSystemEventAsync()
    {
        var systemEvent = new SystemEvent
        {
            Timestamp = DateTime.UtcNow
        };

        try
        {
            // CPU Temperature
            systemEvent.CpuTemperatureCelsius = await GetCpuTemperatureAsync();

            // OS Information
            var (osName, osVersion) = GetOSInfo();
            systemEvent.OsName = osName;
            systemEvent.OsVersion = osVersion;

            // Machine Name
            systemEvent.MachineName = Environment.MachineName;

            // Uptime
            systemEvent.UptimeHours = GetUptimeHours();

            // Memory Information
            var (totalMemory, availableMemory) = GetMemoryInfo();
            systemEvent.TotalMemoryGb = totalMemory;
            systemEvent.AvailableMemoryGb = availableMemory;

            // Disk Serial Number
            systemEvent.DiskSerialNumber = await GetDiskSerialNumberAsync();

            // CPU Cores
            systemEvent.CpuCores = Environment.ProcessorCount;

            // CPU Usage
            systemEvent.CpuUsagePercent = GetCpuUsage();

            // Process Count
            systemEvent.ProcessCount = Process.GetProcesses().Length;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error gathering system information");
        }

        return systemEvent;
    }

    private async Task<string> GetCpuTemperatureAsync()
    {
        try
        {
            using var searcher = new ManagementObjectSearcher(
                @"root\WMI",
                "SELECT * FROM MSAcpi_ThermalZoneTemperature");

            var collection = await Task.Run(() => searcher.Get());

            foreach (ManagementObject obj in collection)
            {
                var temp = Convert.ToDouble(obj["CurrentTemperature"]);
                // Convert from tenths of Kelvin to Celsius
                var celsius = (temp / 10.0) - 273.15;
                return celsius.ToString("F1");
            }
        }
        catch (Exception ex)
        {
            _logger.LogDebug("WMI temperature reading failed: {Error}", ex.Message);
        }

        // Fallback: try OpenHardwareMonitor namespace
        try
        {
            using var searcher = new ManagementObjectSearcher(
                @"root\OpenHardwareMonitor",
                "SELECT * FROM Sensor WHERE SensorType='Temperature'");

            var collection = await Task.Run(() => searcher.Get());

            foreach (ManagementObject obj in collection)
            {
                var value = obj["Value"];
                if (value != null && obj["Name"]?.ToString()?.Contains("CPU") == true)
                {
                    return Convert.ToDouble(value).ToString("F1");
                }
            }
        }
        catch (Exception ex)
        {
            _logger.LogDebug("OpenHardwareMonitor temperature reading failed: {Error}", ex.Message);
        }

        return "N/A";
    }

    private (string osName, string osVersion) GetOSInfo()
    {
        try
        {
            using var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");
            foreach (ManagementObject obj in searcher.Get())
            {
                var name = obj["Caption"]?.ToString() ?? "Unknown OS";
                var version = obj["Version"]?.ToString() ?? "Unknown Version";
                return (name, version);
            }
        }
        catch (Exception ex)
        {
            _logger.LogWarning("Failed to get OS information: {Error}", ex.Message);
        }

        return (Environment.OSVersion.Platform.ToString(), Environment.OSVersion.Version.ToString());
    }

    private double GetUptimeHours()
    {
        try
        {
            var uptime = TimeSpan.FromMilliseconds(Environment.TickCount64);
            return uptime.TotalHours;
        }
        catch
        {
            return 0;
        }
    }

    private (double totalGb, double availableGb) GetMemoryInfo()
    {
        try
        {
            double totalMemoryGb = 0;
            using (var searcher = new ManagementObjectSearcher("SELECT TotalPhysicalMemory FROM Win32_ComputerSystem"))
            {
                foreach (ManagementObject obj in searcher.Get())
                {
                    var totalBytes = Convert.ToDouble(obj["TotalPhysicalMemory"]);
                    totalMemoryGb = totalBytes / (1024 * 1024 * 1024);
                    break;
                }
            }

            var availableMemoryGb = _availableMemoryCounter?.NextValue() / 1024.0 ?? 0;

            return (totalMemoryGb, availableMemoryGb);
        }
        catch (Exception ex)
        {
            _logger.LogWarning("Failed to get memory information: {Error}", ex.Message);
            return (0, 0);
        }
    }

    private async Task<string> GetDiskSerialNumberAsync()
    {
        try
        {
            using var searcher = new ManagementObjectSearcher(
                "SELECT SerialNumber FROM Win32_PhysicalMedia");

            var collection = await Task.Run(() => searcher.Get());

            foreach (ManagementObject obj in collection)
            {
                var serial = obj["SerialNumber"]?.ToString()?.Trim();
                if (!string.IsNullOrEmpty(serial))
                {
                    return serial;
                }
            }
        }
        catch (Exception ex)
        {
            _logger.LogDebug("Failed to get disk serial from Win32_PhysicalMedia: {Error}", ex.Message);
        }

        // Fallback to Win32_DiskDrive
        try
        {
            using var searcher = new ManagementObjectSearcher(
                "SELECT SerialNumber FROM Win32_DiskDrive WHERE MediaType='Fixed hard disk media'");

            var collection = await Task.Run(() => searcher.Get());

            foreach (ManagementObject obj in collection)
            {
                var serial = obj["SerialNumber"]?.ToString()?.Trim();
                if (!string.IsNullOrEmpty(serial))
                {
                    return serial;
                }
            }
        }
        catch (Exception ex)
        {
            _logger.LogWarning("Failed to get disk serial number: {Error}", ex.Message);
        }

        return "N/A";
    }

    private double GetCpuUsage()
    {
        try
        {
            return Math.Round(_cpuCounter?.NextValue() ?? 0, 1);
        }
        catch (Exception ex)
        {
            _logger.LogDebug("Failed to get CPU usage: {Error}", ex.Message);
            return 0;
        }
    }

    public void Dispose()
    {
        _cpuCounter?.Dispose();
        _availableMemoryCounter?.Dispose();
    }
}
