namespace BlazorComponentProject.Components;

public partial class AlertComponent
{
    [Parameter] public string Title { get; set; } = string.Empty;
    [Parameter] public string Message { get; set; } = string.Empty;
    [Parameter] public AlertType Type { get; set; } = AlertType.Info;
    [Parameter] public bool IsVisible { get; set; } = true;
    [Parameter] public bool IsDismissible { get; set; } = false;
    [Parameter] public string IconClass { get; set; } = string.Empty;
    [Parameter] public RenderFragment? ChildContent { get; set; }
    [Parameter] public EventCallback OnDismiss { get; set; }

    private string GetAlertClass()
    {
        return Type switch
        {
            AlertType.Primary => "alert-primary",
            AlertType.Secondary => "alert-secondary",
            AlertType.Success => "alert-success",
            AlertType.Danger => "alert-danger",
            AlertType.Warning => "alert-warning",
            AlertType.Info => "alert-info",
            AlertType.Light => "alert-light",
            AlertType.Dark => "alert-dark",
            _ => "alert-info"
        };
    }

    private async Task Hide()
    {
        IsVisible = false;
        if (OnDismiss.HasDelegate)
        {
            await OnDismiss.InvokeAsync();
        }
        StateHasChanged();
    }

    public void Show()
    {
        IsVisible = true;
        StateHasChanged();
    }
}