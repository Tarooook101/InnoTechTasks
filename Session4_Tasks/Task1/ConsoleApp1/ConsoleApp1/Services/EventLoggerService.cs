using ConsoleApp1.Models;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace ConsoleApp1.Services;

public class EventLoggerService : IDisposable
{
    private readonly ILogger<EventLoggerService> _logger;
    private readonly SystemInfoService _systemInfoService;
    private readonly IConfiguration _configuration;
    private readonly Timer _timer;
    private readonly string _logDirectory;
    private readonly string _logFormat;
    private readonly string _fileNamingMode;

    public EventLoggerService(
        ILogger<EventLoggerService> logger,
        SystemInfoService systemInfoService,
        IConfiguration configuration)
    {
        _logger = logger;
        _systemInfoService = systemInfoService;
        _configuration = configuration;

        _logDirectory = _configuration["EventLogger:LogDirectory"] ?? "logs";
        _logFormat = _configuration["EventLogger:LogFormat"] ?? "json";
        _fileNamingMode = _configuration["EventLogger:FileNamingMode"] ?? "rolling";

        var intervalMinutes = _configuration.GetValue<int>("EventLogger:IntervalMinutes", 1);
        var interval = TimeSpan.FromMinutes(intervalMinutes);

        // Ensure log directory exists
        Directory.CreateDirectory(_logDirectory);

        _logger.LogInformation("Starting EventLoggerService with {Interval} minute intervals", intervalMinutes);

        // Start timer immediately and then repeat at intervals
        _timer = new Timer(LogSystemEvent, null, TimeSpan.Zero, interval);
    }

    private async void LogSystemEvent(object? state)
    {
        try
        {
            var systemEvent = await _systemInfoService.GetSystemEventAsync();
            await WriteEventToFileAsync(systemEvent);

            _logger.LogInformation("Logged system event at {Timestamp}", systemEvent.Timestamp);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error logging system event");
        }
    }

    private async Task WriteEventToFileAsync(SystemEvent systemEvent)
    {
        var fileName = GetLogFileName(systemEvent.Timestamp);
        var filePath = Path.Combine(_logDirectory, fileName);

        string logEntry = _logFormat.ToLower() switch
        {
            "human" => systemEvent.ToHumanReadableString(),
            _ => systemEvent.ToJsonString()
        };

        // Append newline
        logEntry += Environment.NewLine;

        try
        {
            await File.AppendAllTextAsync(filePath, logEntry);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to write to log file: {FilePath}", filePath);

            // Try to write to a fallback location
            var fallbackPath = Path.Combine(Path.GetTempPath(), "SystemEventLogger", fileName);
            Directory.CreateDirectory(Path.GetDirectoryName(fallbackPath)!);
            await File.AppendAllTextAsync(fallbackPath, logEntry);
            _logger.LogWarning("Written to fallback location: {FallbackPath}", fallbackPath);
        }
    }

    private string GetLogFileName(DateTime timestamp)
    {
        return _fileNamingMode.ToLower() switch
        {
            "timestamped" => $"events-{timestamp:yyyyMMdd-HHmmss}.log",
            _ => $"events-{timestamp:yyyyMMdd}.log" // rolling (daily)
        };
    }

    public void Dispose()
    {
        _timer?.Dispose();
        _systemInfoService?.Dispose();
    }
}