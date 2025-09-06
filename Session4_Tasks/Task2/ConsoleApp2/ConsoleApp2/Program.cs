using ConsoleApp2.Services;

namespace ConsoleApp2;
class Program
{
    static async Task Main(string[] args)
    {
        try
        {
            Console.WriteLine("Teacher Management System");
            Console.WriteLine("=========================");

            var teacherService = new TeacherService();

            Console.WriteLine("Generating and saving 15 teacher records...");
            var result = await teacherService.GenerateAndSaveTeachersAsync();

            if (result.Success)
            {
                Console.WriteLine($"✓ Successfully processed {result.TeachersGenerated} teachers.");
                Console.WriteLine($"✓ Total teachers in system: {result.TotalTeachers}");
                Console.WriteLine($"✓ Data saved to: {result.FilePath}");
            }
            else
            {
                Console.WriteLine($"✗ Error: {result.ErrorMessage}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"✗ Unexpected error: {ex.Message}");
        }

        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();
    }
}