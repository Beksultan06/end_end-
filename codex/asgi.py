# Импортируем необходимые модули
import os
from django.core.asgi import get_asgi_application

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codex.settings')

# Получаем ASGI-приложение Django, которое будет обрабатывать асинхронные запросы и события
application = get_asgi_application()
