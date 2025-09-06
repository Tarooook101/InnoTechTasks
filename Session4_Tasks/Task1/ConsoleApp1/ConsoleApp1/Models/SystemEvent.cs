
using System.Text.Json;
using System.Text.Json.Serialization;

namespace ConsoleApp1.Models;

public class SystemEvent
{
    [JsonPropertyName("timestamp")]
    public DateTime Timestamp { get; set; }

    [JsonPropertyName("cpu_temperature_celsius")]
    public string CpuTemperatureCelsius { get; set; } = "N/A";

    [JsonPropertyName("os_name")]
    public string OsName { get; set; } = string.Empty;

    [JsonPropertyName("os_version")]
    public string OsVersion { get; set; } = string.Empty;

    [JsonPropertyName("machine_name")]
    public string MachineName { get; set; } = string.Empty;

    [JsonPropertyName("uptime_hours")]
    public double UptimeHours { get; set; }

    [JsonPropertyName("total_memory_gb")]
    public double TotalMemoryGb { get; set; }

    [JsonPropertyName("available_memory_gb")]
    public double AvailableMemoryGb { get; set; }

    [JsonPropertyName("disk_serial_number")]
    public string DiskSerialNumber { get; set; } = "N/A";

    [JsonPropertyName("cpu_cores")]
    public int CpuCores { get; set; }

    [JsonPropertyName("cpu_usage_percent")]
    public double CpuUsagePercent { get; set; }

    [JsonPropertyName("process_count")]
    public int ProcessCount { get; set; }

    public string ToJsonString()
    {
        var options = new JsonSerializerOptions
        {
            WriteIndented = false,
            PropertyNamingPolicy = JsonNamingPolicy.SnakeCaseLower
        };
        return JsonSerializer.Serialize(this, options);
    }

    public string ToHumanReadableString()
    {
        return $"{Timestamp:yyyy-MM-dd HH:mm:ss} | " +
               $"CPU Temp: {CpuTemperatureCelsius}°C | " +
               $"OS: {OsName} {OsVersion} | " +
               $"Machine: {MachineName} | " +
               $"Uptime: {UptimeHours:F1}h | " +
               $"RAM: {AvailableMemoryGb:F1}/{TotalMemoryGb:F1}GB | " +
               $"Disk SN: {DiskSerialNumber} | " +
               $"CPU Cores: {CpuCores} | " +
               $"CPU Usage: {CpuUsagePercent:F1}% | " +
               $"Processes: {ProcessCount}";
    }
}