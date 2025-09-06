
namespace ConsoleApp2.Services;

public class ServiceResult
{
    public bool Success { get; set; }
    public string ErrorMessage { get; set; } = string.Empty;
    public int TeachersGenerated { get; set; }
    public int TotalTeachers { get; set; }
    public string FilePath { get; set; } = string.Empty;
}
