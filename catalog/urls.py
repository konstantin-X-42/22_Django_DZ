from django.urls import path
# Добавляем в импорт контроллеры
from catalog.views import home_view, categories_view, orders_view, contacts_view

# исключаем одноименные конфликты
app_name = 'catalog'

urlpatterns = [
    # маршрут для домашней страницы 1
    path('', home_view, name='21-2_home1'),

    # маршрут для Категорий страница 2
    path('categories/', categories_view, name='21-2_home2'),

    # маршрут для Заказов страница 3
    path('orders/', orders_view, name='21-2_home3'),

    # маршрут для страницы 4 контактов с закрывающим /
    path('contacts/', contacts_view, name='21-2_home4'),
]




# рабочий вариант

# from django.urls import path
# from catalog.views import home_view, contacts_view
#
# app_name = 'catalog'
#
# urlpatterns = [
#     # Маршрут для домашней страницы
#     path('', home_view, name='21-2_home1'),
#     # Маршрут для страницы контактов с закрывающим /
#     path('contacts/', contacts_view, name='21-2_home4'),
# ]






# мой изначально

# from django.urls import path
# from catalog.apps import CatalogConfig
# from catalog.views import home
#
# app_name = CatalogConfig.name
#
# urlpatterns = [
#     path('', home, name='home')
# ]
