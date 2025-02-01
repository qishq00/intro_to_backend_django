from django.urls import path
from .views import movie_list  # Импортируем представление

urlpatterns = [
    path('movies/', movie_list),  # Добавляем маршрут для списка фильмов
]
