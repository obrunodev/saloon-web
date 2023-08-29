from django.shortcuts import render


def index(request):
    """
    Renders the landing page.
    """
    return render(request, 'scheduling/index.html')
