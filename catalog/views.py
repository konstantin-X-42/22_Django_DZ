from django.shortcuts import render

def home_view(request):
    """Контроллер главной страницы"""
    return render(request, 'catalog/21-2_home1.html')

def categories_view(request):
    """Контроллер для страницы категорий"""
    return render(request, 'catalog/21-2_home2.html')

def orders_view(request):
    """Контроллер для страницы заказов"""
    return render(request, 'catalog/21-2_home3.html')

def contacts_view(request):
    """Контроллер страницы контактов"""
    return render(request, 'catalog/21-2_home4.html')
