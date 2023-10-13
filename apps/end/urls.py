# Импорты
from django.urls import path
from apps.mp3.views import MailFormView, done, error

# Определяем переменную urlpatterns - список URL-маршрутов для Django-приложения
urlpatterns = [
    # URL-маршрут для главной страницы
    path('', MailFormView.as_view(), name="index"),

    # URL-маршрут для страницы "done"
    path('done/', done, name="done"),

    # URL-маршрут для страницы "error"
    path('error/', error, name="error")
]
