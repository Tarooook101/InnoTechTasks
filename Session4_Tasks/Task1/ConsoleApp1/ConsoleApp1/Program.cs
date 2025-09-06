using ConsoleApp1.Services;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

namespace ConsoleApp1;

public class Program
{
    private static EventLoggerService? _eventLoggerService;
    private static ILogger<Program>? _logger;

    public static async Task Main(string[] args)
    {
        Console.WriteLine("System Event Logger Starting...");

        try
        {
            // Setup configuration
            var configuration = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .AddCommandLine(args)
                .AddEnvironmentVariables()
                .Build();

            // Setup dependency injection
            var services = new ServiceCollection()
                .AddSingleton<IConfiguration>(configuration)
                .AddLogging(builder =>
                {
                    builder.AddConfiguration(configuration.GetSection("Logging"));
                    builder.AddConsole();
                })
                .AddSingleton<SystemInfoService>()
                .AddSingleton<EventLoggerService>()
                .BuildServiceProvider();

            _logger = services.GetRequiredService<ILogger<Program>>();
            _eventLoggerService = services.GetRequiredService<EventLoggerService>();

            _logger.LogInformation("System Event Logger started successfully");

            // Setup console cancellation handling
            Console.CancelKeyPress += OnCancelKeyPress;

            // Setup graceful shutdown for Windows Service
            AppDomain.CurrentDomain.ProcessExit += OnProcessExit;

            // Keep the application running
            var cancellationTokenSource = new CancellationTokenSource();

            // Wait indefinitely until cancellation is requested
            try
            {
                await Task.Delay(Timeout.Infinite, cancellationTokenSource.Token);
            }
            catch (OperationCanceledException)
            {
                _logger.LogInformation("Application shutdown requested");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Fatal error: {ex.Message}");
            _logger?.LogCritical(ex, "Fatal error occurred during startup");
            Environment.Exit(1);
        }
        finally
        {
            await Cleanup();
        }
    }

    private static void OnCancelKeyPress(object? sender, ConsoleCancelEventArgs e)
    {
        e.Cancel = true; // Prevent immediate termination
        _logger?.LogInformation("Shutdown signal received (Ctrl+C)");
        Task.Run(async () => await Cleanup());
    }

    private static async void OnProcessExit(object? sender, EventArgs e)
    {
        _logger?.LogInformation("Process exit event received");
        await Cleanup();
    }

    private static async Task Cleanup()
    {
        try
        {
            _logger?.LogInformation("Shutting down System Event Logger...");

            _eventLoggerService?.Dispose();

            // Give some time for final operations
            await Task.Delay(1000);

            _logger?.LogInformation("System Event Logger stopped");
        }
        catch (Exception ex)
        {
            _logger?.LogError(ex, "Error during cleanup");
        }
        finally
        {
            Environment.Exit(0);
        }
    }
}