
namespace ConsoleApp1;

public class SystemInformation
{
    public DateTime Timestamp { get; set; }
    public string CPUTemperature { get; set; } = string.Empty;
    public string OSInfo { get; set; } = string.Empty;
    public string TotalRAMSize { get; set; } = string.Empty;
    public string HardDiskSerialNumber { get; set; } = string.Empty;
    public int NumberOfCPUCores { get; set; }
}
