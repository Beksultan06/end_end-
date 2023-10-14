from youtube_dl import YoutubeDL
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task


@shared_task()
def send_feedback_email_task(url, email):
    video_info = YoutubeDL().extract_info(url=url, download=False)
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best', 
        'keepvideo': False,  
        'outtmpl': f'media/{filename}',  
    }
    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    mail = EmailMessage(
        "Ваш файл готов.",
        "Это уведомление отправлено, потому что вы указали свой адрес электронной почты на нашем веб-сайте.",
        settings.EMAIL_HOST_USER,  
    )
    mail.attach_file(f'media/{filename}')
    mail.send()
