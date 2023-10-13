# Импорты
from django.apps import AppConfig

# Определяем кастомный класс AppConfig для приложения "mp3"
class MP3Config(AppConfig):
    # Настраиваем поле по умолчанию для автогенерируемых первичных ключей в моделях приложения
    default_auto_field = 'django.db.models.BigAutoField'

    # Указываем имя приложения
    name = 'apps.end'
