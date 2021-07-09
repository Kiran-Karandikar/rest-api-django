from django.shortcuts import render


# Create your views here.
def home_page(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "test.html")
