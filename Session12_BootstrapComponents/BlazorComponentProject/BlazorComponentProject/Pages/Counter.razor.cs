using BlazorComponentProject.Components;

namespace BlazorComponentProject.Pages;

public partial class Counter
{
    private int currentCount = 0;
    private int newCount = 0;
    private bool showAlert = false;
    private bool showToast = false;
    private bool showModal = false;

    // Component references
    private AlertComponent? alertComponent;
    private ToastComponent? toastComponent;
    private ModalComponent? modalComponent;

    // Dropdown items
    private List<DropDownComponent.DropDownItem> dropdownItems = new()
    {
        new() { Text = "Reset", Data = "reset" },
        new() { Text = "+10", Data = "add10" },
        new() { Text = "-5", Data = "subtract5" }
    };

    private void IncrementCount()
    {
        currentCount++;
        ShowSuccessAlert();
    }

    private async Task OnActionSelected(DropDownComponent.DropDownItem item)
    {
        switch (item.Data?.ToString())
        {
            case "reset":
                currentCount = 0;
                break;
            case "add10":
                currentCount += 10;
                break;
            case "subtract5":
                currentCount -= 5;
                break;
        }
        ShowSuccessAlert();
    }

    private void ShowSuccessAlert()
    {
        showAlert = true;
        StateHasChanged();
    }

    private void ShowToastNotification()
    {
        showToast = true;
        StateHasChanged();
    }

    private void ShowCounterModal()
    {
        newCount = currentCount; 
        showModal = true;
        StateHasChanged();
    }

    private void CancelModal()
    {
        showModal = false;
        StateHasChanged();
    }

    private void SetNewCount()
    {
        currentCount = newCount;
        showModal = false;
        ShowSuccessAlert();
        StateHasChanged();
    }
}