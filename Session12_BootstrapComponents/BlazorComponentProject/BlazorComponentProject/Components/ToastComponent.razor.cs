namespace BlazorComponentProject.Components;

public partial class ToastComponent
{
    [Parameter] public string Title { get; set; } = string.Empty;
    [Parameter] public string Message { get; set; } = string.Empty;
    [Parameter] public ToastType Type { get; set; } = ToastType.Info;
    [Parameter] public bool IsVisible { get; set; }
    [Parameter] public int AutoHideDelay { get; set; } = 5000;
    [Parameter] public string IconClass { get; set; } = string.Empty;
    [Parameter] public RenderFragment? ChildContent { get; set; }
    [Parameter] public EventCallback OnHide { get; set; }

    private string TimeStamp => DateTime.Now.ToString("HH:mm");
    private Timer? autoHideTimer;

    protected override void OnParametersSet()
    {
        if (IsVisible && AutoHideDelay > 0)
        {
            autoHideTimer?.Dispose();
            autoHideTimer = new Timer(async _ => await Hide(), null, AutoHideDelay, Timeout.Infinite);
        }
    }

    private async Task Hide()
    {
        IsVisible = false;
        autoHideTimer?.Dispose();
        await OnHide.InvokeAsync();
        StateHasChanged();
    }

    private string GetHeaderClass()
    {
        return Type switch
        {
            ToastType.Success => "bg-success text-white",
            ToastType.Error => "bg-danger text-white",
            ToastType.Warning => "bg-warning text-dark",
            _ => "bg-info text-white"
        };
    }

    private string GetBodyClass()
    {
        return string.IsNullOrEmpty(Title) ? Type switch
        {
            ToastType.Success => "text-bg-success",
            ToastType.Error => "text-bg-danger",
            ToastType.Warning => "text-bg-warning",
            _ => "text-bg-info"
        } : "";
    }


    public void Dispose()
    {
        autoHideTimer?.Dispose();
    }
}