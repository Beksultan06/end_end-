# Импортируем необходимые модули
import os
from django.core.wsgi import get_wsgi_application

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codex.settings')

# Получаем WSGI-приложение Django, которое будет обрабатывать запросы
application = get_wsgi_application()
