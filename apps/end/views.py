# Импорты
from django.shortcuts import render
from django.views.generic.edit import FormView
from apps.end.forms import MailForm


# Создаем класс представления для обработки формы.
class MailFormView(FormView):
    template_name = "index.html"
    form_class = MailForm
    success_url = "/done/"

    # Метод, который будет вызван при успешной валидации формы.
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

# Функция для отображения страницы "done.html" при успешной отправке формы.
def done(request):
    return render(request, 'done.html')

# Функция для отображения страницы "error.html" при возникновении ошибки.
def error(request):
    return render(request, 'error.html')
