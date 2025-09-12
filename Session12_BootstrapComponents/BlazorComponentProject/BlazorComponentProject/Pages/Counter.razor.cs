namespace BlazorComponentProject.Pages;

public partial class Counter
{
    private int currentCount = 0;

    private void IncrementCount()
    {
        currentCount++;
    }

    private int newCount = 0;
    private bool showAlert = false;
    private bool showToast = false;
    private bool showModal = false;
}