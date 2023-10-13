# Импорты
from youtube_dl import YoutubeDL
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task


# Создаем задачу Celery для отправки электронной почты
@shared_task()
def send_feedback_email_task(url, email):
    # Извлекаем информацию о видео с помощью youtube_dl
    video_info = YoutubeDL().extract_info(url=url, download=False)
    # Генерируем имя файла для сохранения на локальном сервере
    filename = f"{video_info['title']}.mp3"
    # Опции для youtube_dl
    options = {
        'format': 'bestaudio/best',  # Выбираем лучшее аудио качество
        'keepvideo': False,  # Не сохраняем видео, только аудио
        'outtmpl': f'media/{filename}',  # Путь для сохранения файла
    }
    # Загружаем аудио с указанной ссылки и применяем опции
    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    # Создаем объект EmailMessage для отправки уведомления
    mail = EmailMessage(
        "Ваш файл готов.",
        "Это уведомление отправлено, потому что вы указали свой адрес электронной почты на нашем веб-сайте.",
        settings.EMAIL_HOST_USER,  # Отправитель
        [email]  # Получатель(и)
    )
    # Прикрепляем скачанный файл к письму
    mail.attach_file(f'media/{filename}')
    # Отправляем письмо
    mail.send()
