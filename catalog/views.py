from django.shortcuts import render

def home(request):
    """Контроллер связывает внутреннюю логику сервера с визуальной HTML-страницей, которую видит пользователь в браузере"""
    return render(request, 'home.html')

