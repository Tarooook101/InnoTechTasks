using Microsoft.AspNetCore.Mvc;
using StudentsAffairsWebAPI_MyCode.Models;
using System.Text.Json;

namespace StudentsAffairsWebAPI_MyCode.Controllers;

[ApiController]
[Route("api/[controller]")]
public class TeachersController : ControllerBase
{
    const int maxTeachersCount = 15;
    private List<Teacher>? teachers = new();
    Teacher teacher = new();
    const string filePath = @"Teachers.json";

    public TeachersController()
    {
        FileInfo fileInfo = new FileInfo(filePath);
        if (fileInfo.Exists)
        {
            string? fileContent = System.IO.File.ReadAllText(filePath);

            teachers = JsonSerializer.Deserialize<List<Teacher>>(fileContent);
        }

        if (teachers is null || !teachers.Any())
        {
            teachers = teacher.ReadTeachers(maxTeachersCount).ToList();
            string? fileContent = JsonSerializer.Serialize(teachers);
            System.IO.File.WriteAllText(filePath, fileContent);
        }
    }

    [HttpGet]
    public IEnumerable<Teacher> Get()
    {
        return teachers ?? new();
    }

    [HttpGet("{id}")]
    public IActionResult GetById([FromRoute] string id)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        try
        {
            Teacher? teacherFromList = teachers?.FirstOrDefault(t => t.Id.Equals(idParsed));

            if (teacherFromList is null)
                return NotFound($"Teacher with ID {idParsed} not found");

            return Ok(teacherFromList);
        }
        catch (Exception exception)
        {
            return NotFound(exception.Message);
        }
    }

    [HttpPost]
    public IActionResult Post([FromBody] Teacher teacher)
    {
        if (teacher is null)
            return BadRequest("Teacher cannot be null");

        try
        {

            if (teachers?.Any(t => t.Id == teacher.Id) == true)
                return Conflict($"Teacher with ID {teacher.Id} already exists");

            teachers?.Add(teacher);

            string? fileContent = JsonSerializer.Serialize(teachers);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Created($"api/teachers/{teacher.Id}", teacher);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpPut]
    public IActionResult Update([FromBody] Teacher teacher)
    {
        if (teacher is null || string.IsNullOrEmpty(teacher.Name))
            return BadRequest("Teacher cannot be null and name cannot be empty");

        try
        {
            Teacher? teacherFromList = teachers?.FirstOrDefault(t => t.Id == teacher.Id);

            if (teacherFromList is null)
                return NotFound($"Teacher with ID {teacher.Id} not found");

            int teacherIndex = teachers!.IndexOf(teacherFromList);

            if (teacherIndex >= 0)
            {
                teachers[teacherIndex] = teacher;
            }
            else
            {
                return NotFound($"Teacher with ID {teacher.Id} not found");
            }

            string? fileContent = JsonSerializer.Serialize(teachers);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(teacher);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpPut("{id}")]
    public IActionResult UpdateById([FromRoute] string id, [FromBody] Teacher teacher)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        if (teacher is null || string.IsNullOrEmpty(teacher.Name))
            return BadRequest("Teacher cannot be null and name cannot be empty");

        try
        {
            Teacher? teacherFromList = teachers?.FirstOrDefault(t => t.Id == idParsed);

            if (teacherFromList is null)
                return NotFound($"Teacher with ID {idParsed} not found");


            teacher.Id = idParsed;

            int teacherIndex = teachers!.IndexOf(teacherFromList);
            teachers[teacherIndex] = teacher;

            string? fileContent = JsonSerializer.Serialize(teachers);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(teacher);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpDelete("{id}")]
    public IActionResult DeleteById([FromRoute] string id)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        try
        {
            Teacher? teacherToDelete = teachers?.FirstOrDefault(t => t.Id == idParsed);

            if (teacherToDelete is null)
                return NotFound($"Teacher with ID {idParsed} not found");

            teachers?.Remove(teacherToDelete);

            string? fileContent = JsonSerializer.Serialize(teachers);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(teacherToDelete);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }

    [HttpDelete]
    public IActionResult Delete([FromBody] Teacher teacher)
    {
        if (teacher is null)
            return BadRequest("Teacher cannot be null");

        try
        {
            Teacher? teacherFromList = teachers?.FirstOrDefault(t => t.Id == teacher.Id);

            if (teacherFromList is null)
                return NotFound($"Teacher with ID {teacher.Id} not found");

            teachers?.Remove(teacherFromList);

            string? fileContent = JsonSerializer.Serialize(teachers);
            System.IO.File.WriteAllText(filePath, fileContent);

            return Ok(teacherFromList);
        }
        catch (Exception exception)
        {
            return BadRequest(exception.Message);
        }
    }
}
