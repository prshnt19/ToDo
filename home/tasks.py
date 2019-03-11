# import logging
#
# from django.urls import reverse
# from django.core.mail import send_mail
# from django.contrib.auth import get_user_model
from ToDo.celery import app
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
# from dateutil import parser
# from django.utils.timezone import datetime
# from easy_pdf.views import PDFTemplateView
from .models import ToDo


@app.task
def send_email(id):
    todo = ToDo.objects.get(id=id)
    message = render_to_string('mail.html', {'todo': todo,
                                             'domain': '127.0.0.1:8000',
                                             'uid': urlsafe_base64_encode(force_bytes(todo.pk)).decode(),
                                             })

    mail_subject = 'Todo Task'
    email = EmailMessage(mail_subject, message, to=['prashant.rawat216@gmail.com'])
    email.send()
