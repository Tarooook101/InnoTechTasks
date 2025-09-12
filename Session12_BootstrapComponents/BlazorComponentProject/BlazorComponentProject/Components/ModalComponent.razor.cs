namespace BlazorComponentProject.Components;

public partial class ModalComponent
{
    [Parameter] public string Title { get; set; } = string.Empty;
    [Parameter] public bool IsVisible { get; set; }
    [Parameter] public ModalSize Size { get; set; } = ModalSize.Default;
    [Parameter] public bool ShowCloseButton { get; set; } = true;
    [Parameter] public RenderFragment? BodyContent { get; set; }
    [Parameter] public RenderFragment? FooterContent { get; set; }
    [Parameter] public EventCallback OnHide { get; set; }
    [Parameter] public EventCallback OnShow { get; set; }

    private string SizeClass => Size switch
    {
        ModalSize.Small => "modal-sm",
        ModalSize.Large => "modal-lg",
        ModalSize.ExtraLarge => "modal-xl",
        _ => ""
    };

    protected override async Task OnParametersSetAsync()
    {
        if (IsVisible && OnShow.HasDelegate)
        {
            await OnShow.InvokeAsync();
        }
    }

    public async Task Hide()
    {
        IsVisible = false;
        if (OnHide.HasDelegate)
        {
            await OnHide.InvokeAsync();
        }
        StateHasChanged();
    }

    public void Show()
    {
        IsVisible = true;
        StateHasChanged();
    }
}