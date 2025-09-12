
namespace BlazorComponentProject.Components;

public partial class DropDownComponent
{
    [Parameter] public string ButtonText { get; set; } = "Dropdown";
    [Parameter] public string ButtonClass { get; set; } = "btn-secondary";
    [Parameter] public List<DropDownItem>? Items { get; set; }
    [Parameter] public RenderFragment? ChildContent { get; set; }
    [Parameter] public EventCallback<DropDownItem> OnItemSelected { get; set; }

    private async Task OnItemClick(DropDownItem item)
    {
        if (OnItemSelected.HasDelegate)
        {
            await OnItemSelected.InvokeAsync(item);
        }
    }

    public class DropDownItem
    {
        public string Text { get; set; } = string.Empty;
        public string Url { get; set; } = string.Empty;
        public object? Data { get; set; }
    }
}