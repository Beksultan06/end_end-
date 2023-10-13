# Импорты
from django import forms
from apps.end.tasks import send_feedback_email_task


# Определяем класс MailForm, который будет представлять нашу форму
class MailForm(forms.Form):
    # Определяем поле для ввода URL
    url = forms.CharField(
        label="URL",
        widget=forms.Textarea(attrs={"rows": 1})
    )
    # Определяем поле для ввода адреса электронной почты
    email = forms.EmailField(label="Email Address")

    # Определяем метод send_email для отправки электронного письма
    def send_email(self):
        send_feedback_email_task.apply_async(
            args=[self.cleaned_data["url"], self.cleaned_data["email"]]
        )
