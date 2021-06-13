from django.shortcuts import render
import requests

def home(request):
    # Render the HTML template home.html
    # response = requests.post('http://127.0.0.1:8000/api/employees/', json={"one": 1})
    response = requests.get('http://127.0.0.1:8000/api/employees/')
    print(response.json()) # This should contain the returned data
    context = response.json()
    return render(request, 'home.html', context)
