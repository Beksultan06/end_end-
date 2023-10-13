# Импортируем необходимые модули
import os
from celery import Celery

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codex.settings")

# Создаем объект Celery
app = Celery("codex")

# Конфигурируем настройки Celery из объекта settings Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически обнаруживаем и регистрируем задачи из приложений Django
app.autodiscover_tasks()
