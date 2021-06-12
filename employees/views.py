from django.shortcuts import render

def home(request):
    # Render the HTML template home.html
    return render(request, 'home.html')
