from django.urls import path
from apps.end.views import MailFormView, done, error

urlpatterns = [
    path('', MailFormView.as_view(), name="index"),
    path('done/', done, name="done"),
    path('error/', error, name="error")
]
