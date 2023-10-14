from django.shortcuts import render
from django.views.generic.edit import FormView
from apps.end.forms import MailForm


class MailFormView(FormView):
    template_name = "index.html"
    form_class = MailForm
    success_url = "/done/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

def done(request):
    return render(request, 'done.html')

def error(request):
    return render(request, 'error.html')
