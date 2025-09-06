using Microsoft.AspNetCore.Mvc;
using StudentsAffairsWebAPI_MyCode.Models;
using System.Text.Json;

namespace StudentsAffairsWebAPI_MyCode.Controllers;

[Route("api/[controller]")]
[ApiController]
public class StudentsController : ControllerBase
{
    List<Student> students = new();
    Student student = new();
    const int maxStudentsCount = 15;
    const string filePath = "Students.json";

    public StudentsController()
    {
        FileInfo fileInfo = new FileInfo(filePath);
        if (fileInfo.Exists)
        {
            string? fileContent = System.IO.File.ReadAllText(filePath);
            students = JsonSerializer.Deserialize<List<Student>>(fileContent);
        }

        if (students is null || !students.Any())
        {
            FillStudents(maxStudentsCount);
            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);
        }
    }

    public void FillStudents(int desiredCount)
    {
        for (int i = 1; i <= desiredCount; i++)
        {
            Student student = new() { Id = i, Name = $"Student{i}", Age = i + 30, Mobile = $"012784512{i}" };
            students.Add(student);
        }
    }

    [HttpGet]
    public IEnumerable<Student> GetAll()
    {
        return students ?? new();
    }

    [HttpGet("{id}")]
    public IActionResult GetById([FromRoute] string id)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        try
        {
            Student? studentFromList = students.FirstOrDefault(e => e.Id.Equals(idParsed));
            return Ok(studentFromList);
        }
        catch (Exception exception)
        {
            return NotFound(exception.Message);
        }
    }

    [HttpPost]
    public IActionResult Post([FromBody] Student student)
    {
        if (student is null)
            return BadRequest("Student cannot be null");

        try
        {
            // Check if student with same ID already exists
            if (students.Any(s => s.Id == student.Id))
                return Conflict($"Student with ID {student.Id} already exists");

            students?.Add(student);

            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Created($"api/students/{student.Id}", student);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpPut]
    public IActionResult Update([FromBody] Student student)
    {
        if (student is null || string.IsNullOrEmpty(student.Name))
            return BadRequest("Student cannot be null and name cannot be empty");

        try
        {
            Student? studentFromList = students.FirstOrDefault(e => e.Name is not null && e.Name.Equals(student.Name));
            if (studentFromList is null)
                return NotFound($"Student with name '{student.Name}' not found");

            int toBeUpdatedStudentIndex = students.IndexOf(studentFromList);

            if (toBeUpdatedStudentIndex >= 0)
                students[toBeUpdatedStudentIndex] = student;
            else
                return NotFound($"Student with name '{student.Name}' not found");

            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(student);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpDelete("{id}")]
    public IActionResult Delete([FromRoute] string id)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        try
        {
            Student? toBeDeletedStudent = students.FirstOrDefault(e => e.Id.Equals(idParsed));

            if (toBeDeletedStudent is null)
                return NotFound($"Student with ID {idParsed} not found");

            students.Remove(toBeDeletedStudent);

            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(toBeDeletedStudent);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpDelete]
    public IActionResult Delete([FromBody] Student student)
    {
        if (student is null)
            return BadRequest("Student cannot be null");

        try
        {
            Student? studentFromList = students.FirstOrDefault(e => e.Name is not null && e.Name.Equals(student.Name));
            if (studentFromList is null)
                return NotFound($"Student with name '{student.Name}' not found");

            students.Remove(studentFromList);

            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(studentFromList);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpDelete("all")]
    public IActionResult DeleteAll()
    {
        try
        {
            int deletedCount = students.Count;

            if (deletedCount == 0)
                return Ok(new { message = "No students to delete", deletedCount = 0 });

            students.Clear();

            
            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(new
            {
                message = "All students deleted successfully",
                deletedCount = deletedCount
            });
        }
        catch (Exception exception)
        {
            return BadRequest(new
            {
                message = "Error occurred while deleting all students",
                error = exception.Message
            });
        }
    }

    // BONUS ENDPOINT: Delete All Students with Confirmation
    [HttpDelete("all/confirm")]
    public IActionResult DeleteAllWithConfirmation([FromQuery] bool confirm = false)
    {
        if (!confirm)
        {
            return BadRequest(new
            {
                message = "To delete all students, you must confirm by adding ?confirm=true to the URL",
                example = "DELETE /api/students/all/confirm?confirm=true"
            });
        }

        try
        {
            int deletedCount = students.Count;

            if (deletedCount == 0)
                return Ok(new { message = "No students to delete", deletedCount = 0 });

            students.Clear();


            string? fileContent = JsonSerializer.Serialize(students);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(new
            {
                message = "All students deleted successfully with confirmation",
                deletedCount = deletedCount,
                timestamp = DateTime.UtcNow
            });
        }
        catch (Exception exception)
        {
            return BadRequest(new
            {
                message = "Error occurred while deleting all students",
                error = exception.Message
            });
        }
    }
}