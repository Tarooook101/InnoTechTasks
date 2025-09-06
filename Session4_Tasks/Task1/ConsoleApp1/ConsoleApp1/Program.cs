using ConsoleApp1;
using System.Management;
using System.Text;

namespace ConsoleApp1;
public class Program
{
    private static readonly string LogDirectory = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Logs");
    private static CancellationTokenSource _cancellationTokenSource = new();
    private static bool _isRunning = true;

    public static async Task Main(string[] args)
    {
        Console.WriteLine("System Monitor Service Starting...");
        Console.WriteLine("Press Ctrl+C to stop the service");

        // Handle Ctrl+C gracefully
        Console.CancelKeyPress += (sender, e) =>
        {
            e.Cancel = true;
            _isRunning = false;
            _cancellationTokenSource.Cancel();
            Console.WriteLine("\nShutdown signal received. Stopping service...");
        };

        // Create logs directory if it doesn't exist
        Directory.CreateDirectory(LogDirectory);

        try
        {
            await RunServiceAsync(_cancellationTokenSource.Token);
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("Service stopped gracefully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Service error: {ex.Message}");
            WriteErrorLog($"Service error: {ex}");
        }

        Console.WriteLine("Service has stopped.");
    }

    private static async Task RunServiceAsync(CancellationToken cancellationToken)
    {
        while (_isRunning && !cancellationToken.IsCancellationRequested)
        {
            try
            {
                var systemInfo = GatherSystemInformation();
                WriteSystemLog(systemInfo);
                Console.WriteLine($"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] System information logged successfully");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error gathering system information: {ex.Message}");
                WriteErrorLog($"Error gathering system information: {ex}");
            }

            // Wait for 1 minute or until cancellation
            try
            {
                await Task.Delay(TimeSpan.FromMinutes(1), cancellationToken);
            }
            catch (OperationCanceledException)
            {
                break;
            }
        }
    }

    private static SystemInformation GatherSystemInformation()
    {
        var systemInfo = new SystemInformation
        {
            Timestamp = DateTime.Now,
            CPUTemperature = GetCPUTemperature(),
            OSInfo = GetOperatingSystemInfo(),
            TotalRAMSize = GetTotalRAMSize(),
            HardDiskSerialNumber = GetHardDiskSerialNumber(),
            NumberOfCPUCores = Environment.ProcessorCount
        };

        return systemInfo;
    }

    private static string GetCPUTemperature()
    {
        try
        {
            // Try to get CPU temperature from WMI
            using var searcher = new ManagementObjectSearcher(@"root\WMI", "SELECT * FROM MSAcpi_ThermalZoneTemperature");
            using var collection = searcher.Get();

            var temperatures = new StringBuilder();
            foreach (ManagementObject obj in collection)
            {
                var tempKelvin = Convert.ToDouble(obj["CurrentTemperature"]);
                var tempCelsius = (tempKelvin / 10.0) - 273.15;
                temperatures.AppendLine($"Zone: {tempCelsius:F1}°C");
            }

            if (temperatures.Length > 0)
                return temperatures.ToString().TrimEnd();

            // Alternative method using OpenHardwareMonitorLib namespace (if available)
            // This would require additional NuGet packages
            return "Temperature sensor not accessible";
        }
        catch (Exception ex)
        {
            return $"Temperature unavailable: {ex.Message}";
        }
    }

    private static string GetOperatingSystemInfo()
    {
        try
        {
            using var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");
            using var collection = searcher.Get();

            foreach (ManagementObject obj in collection)
            {
                var osInfo = new StringBuilder();
                osInfo.AppendLine($"OS: {obj["Caption"]}");
                osInfo.AppendLine($"Version: {obj["Version"]}");
                osInfo.AppendLine($"Architecture: {obj["OSArchitecture"]}");
                osInfo.AppendLine($"Build Number: {obj["BuildNumber"]}");
                osInfo.AppendLine($"Install Date: {ManagementDateTimeConverter.ToDateTime(obj["InstallDate"].ToString())}");
                osInfo.AppendLine($"Last Boot: {ManagementDateTimeConverter.ToDateTime(obj["LastBootUpTime"].ToString())}");

                return osInfo.ToString().TrimEnd();
            }
        }
        catch (Exception ex)
        {
            return $"OS Info unavailable: {ex.Message}";
        }

        return "OS Info unavailable";
    }

    private static string GetTotalRAMSize()
    {
        try
        {
            using var searcher = new ManagementObjectSearcher("SELECT TotalPhysicalMemory FROM Win32_ComputerSystem");
            using var collection = searcher.Get();

            foreach (ManagementObject obj in collection)
            {
                var totalMemoryBytes = Convert.ToUInt64(obj["TotalPhysicalMemory"]);
                var totalMemoryGB = totalMemoryBytes / (1024.0 * 1024.0 * 1024.0);
                return $"{totalMemoryGB:F2} GB ({totalMemoryBytes:N0} bytes)";
            }
        }
        catch (Exception ex)
        {
            return $"RAM Info unavailable: {ex.Message}";
        }

        return "RAM Info unavailable";
    }

    private static string GetHardDiskSerialNumber()
    {
        try
        {
            using var searcher = new ManagementObjectSearcher("SELECT SerialNumber, Model, Size FROM Win32_DiskDrive WHERE MediaType='Fixed hard disk media'");
            using var collection = searcher.Get();

            var diskInfo = new StringBuilder();
            foreach (ManagementObject obj in collection)
            {
                var serialNumber = obj["SerialNumber"]?.ToString()?.Trim() ?? "N/A";
                var model = obj["Model"]?.ToString() ?? "Unknown";
                var sizeBytes = Convert.ToUInt64(obj["Size"] ?? 0);
                var sizeGB = sizeBytes / (1024.0 * 1024.0 * 1024.0);

                diskInfo.AppendLine($"Disk: {model} | Serial: {serialNumber} | Size: {sizeGB:F1} GB");
            }

            return diskInfo.Length > 0 ? diskInfo.ToString().TrimEnd() : "No hard disks found";
        }
        catch (Exception ex)
        {
            return $"Disk Info unavailable: {ex.Message}";
        }
    }

    private static void WriteSystemLog(SystemInformation systemInfo)
    {
        var timestamp = systemInfo.Timestamp.ToString("yyyyMMdd_HHmmss");
        var fileName = $"SystemLog_{timestamp}.txt";
        var filePath = Path.Combine(LogDirectory, fileName);

        var logContent = new StringBuilder();
        logContent.AppendLine("=== SYSTEM MONITORING LOG ===");
        logContent.AppendLine($"Timestamp: {systemInfo.Timestamp:yyyy-MM-dd HH:mm:ss}");
        logContent.AppendLine($"Machine Name: {Environment.MachineName}");
        logContent.AppendLine($"User Domain: {Environment.UserDomainName}");
        logContent.AppendLine($"User Name: {Environment.UserName}");
        logContent.AppendLine();

        logContent.AppendLine("=== CPU INFORMATION ===");
        logContent.AppendLine($"Number of CPU Cores: {systemInfo.NumberOfCPUCores}");
        logContent.AppendLine($"CPU Temperature: {systemInfo.CPUTemperature}");
        logContent.AppendLine();

        logContent.AppendLine("=== MEMORY INFORMATION ===");
        logContent.AppendLine($"Total RAM Size: {systemInfo.TotalRAMSize}");
        logContent.AppendLine();

        logContent.AppendLine("=== OPERATING SYSTEM ===");
        logContent.AppendLine(systemInfo.OSInfo);
        logContent.AppendLine();

        logContent.AppendLine("=== DISK INFORMATION ===");
        logContent.AppendLine(systemInfo.HardDiskSerialNumber);
        logContent.AppendLine();

        logContent.AppendLine("=== END LOG ===");

        File.WriteAllText(filePath, logContent.ToString(), Encoding.UTF8);
    }

    private static void WriteErrorLog(string error)
    {
        try
        {
            var timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
            var fileName = $"ErrorLog_{timestamp}.txt";
            var filePath = Path.Combine(LogDirectory, fileName);

            var errorContent = new StringBuilder();
            errorContent.AppendLine("=== ERROR LOG ===");
            errorContent.AppendLine($"Timestamp: {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
            errorContent.AppendLine($"Error: {error}");
            errorContent.AppendLine("=== END ERROR LOG ===");

            File.WriteAllText(filePath, errorContent.ToString(), Encoding.UTF8);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Failed to write error log: {ex.Message}");
        }
    }
}