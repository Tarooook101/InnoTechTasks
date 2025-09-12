using ConsoleApp2.Models;
using System.Text.Json;

namespace ConsoleApp2.Services;

public class TeacherService
{
    private const string FilePath = @"F:\teachers.json";
    private const int TeachersToGenerate = 15;

    private readonly string[] FirstNames = {
            "Ahmed", "Fatima", "Mohamed", "Aisha", "Omar", "Nour", "Youssef", "Mariam",
            "Hassan", "Sara", "Ali", "Layla", "Mahmoud", "Yasmin", "Khaled", "Dina",
            "Mostafa", "Rana", "Tarek", "Hala", "Amr", "Mona", "Sayed", "Reem",
            "Ibrahim", "Noha", "Karim", "Salma", "Waleed", "Aya"
        };

    private readonly string[] LastNames = {
            "Hassan", "Mohamed", "Ahmed", "Ali", "Ibrahim", "Mahmoud", "Omar", "Youssef",
            "Abdel Rahman", "Farouk", "Nasser", "Sabry", "Rashad", "Gaber", "Saleh",
            "Mansour", "Zaki", "Morsi", "Shahin", "Fathy"
        };

    private readonly Random _random = new Random();

    public async Task<ServiceResult> GenerateAndSaveTeachersAsync()
    {
        try
        {
            // Check if F: drive exists
            if (!Directory.Exists("F:\\"))
            {
                return new ServiceResult
                {
                    Success = false,
                    ErrorMessage = "F:\\ drive does not exist. Please ensure the drive is available or modify the file path."
                };
            }

            // Read existing teachers
            var existingTeachers = await ReadExistingTeachersAsync();
            int nextId = GetNextId(existingTeachers);

            // Generate new teachers
            var newTeachers = GenerateTeachers(nextId, TeachersToGenerate);

            // Combine existing and new teachers
            existingTeachers.AddRange(newTeachers);

            // Save to file
            await SaveTeachersAsync(existingTeachers);

            return new ServiceResult
            {
                Success = true,
                TeachersGenerated = TeachersToGenerate,
                TotalTeachers = existingTeachers.Count,
                FilePath = FilePath
            };
        }
        catch (UnauthorizedAccessException ex)
        {
            return new ServiceResult
            {
                Success = false,
                ErrorMessage = $"Access denied to file path: {ex.Message}"
            };
        }
        catch (DirectoryNotFoundException ex)
        {
            return new ServiceResult
            {
                Success = false,
                ErrorMessage = $"Directory not found: {ex.Message}"
            };
        }
        catch (IOException ex)
        {
            return new ServiceResult
            {
                Success = false,
                ErrorMessage = $"File I/O error: {ex.Message}"
            };
        }
        catch (JsonException ex)
        {
            return new ServiceResult
            {
                Success = false,
                ErrorMessage = $"JSON parsing error: {ex.Message}"
            };
        }
        catch (Exception ex)
        {
            return new ServiceResult
            {
                Success = false,
                ErrorMessage = $"Unexpected error: {ex.Message}"
            };
        }
    }

    private async Task<List<Teacher>> ReadExistingTeachersAsync()
    {
        if (!File.Exists(FilePath))
        {
            return new List<Teacher>();
        }

        var jsonContent = await File.ReadAllTextAsync(FilePath);

        if (string.IsNullOrWhiteSpace(jsonContent))
        {
            return new List<Teacher>();
        }

        var options = new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        };

        return JsonSerializer.Deserialize<List<Teacher>>(jsonContent, options) ?? new List<Teacher>();
    }

    private int GetNextId(List<Teacher> existingTeachers)
    {
        if (existingTeachers.Count == 0)
            return 1;

        int maxId = 0;
        foreach (var teacher in existingTeachers)
        {
            if (teacher.Id > maxId)
                maxId = teacher.Id;
        }

        return maxId + 1;
    }

    private List<Teacher> GenerateTeachers(int startingId, int count)
    {
        var teachers = new List<Teacher>();

        for (int i = 0; i < count; i++)
        {
            teachers.Add(new Teacher
            {
                Id = startingId + i,
                Name = GenerateRandomName(),
                Mobile = GenerateRandomMobile()
            });
        }

        return teachers;
    }

    private string GenerateRandomName()
    {
        var firstName = FirstNames[_random.Next(FirstNames.Length)];
        var lastName = LastNames[_random.Next(LastNames.Length)];
        return $"{firstName} {lastName}";
    }

    private string GenerateRandomMobile()
    {
        var prefixes = new[] { "010", "011", "012", "015" };
        var prefix = prefixes[_random.Next(prefixes.Length)];

        var number = "";
        for (int i = 0; i < 8; i++)
        {
            number += _random.Next(0, 10);
        }

        return prefix + number;
    }

    private async Task SaveTeachersAsync(List<Teacher> teachers)
    {
        var options = new JsonSerializerOptions
        {
            WriteIndented = true,
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase
        };

        var jsonContent = JsonSerializer.Serialize(teachers, options);
        await File.WriteAllTextAsync(FilePath, jsonContent);
    }
}