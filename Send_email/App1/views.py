from django.core.mail import EmailMessage
from django.http import HttpResponse

def test_email(request):
    recipients = ['user1@example.com', 'user2@example.com', 'user3@example.com']
    for email_address in recipients:
        email = EmailMessage(
            subject='Тестовое письмо',
            body=f'Это тестовое сообщение для {email_address}, отправленное в консоль.',
            to=[email_address]
        )
        email.send()
    
    return HttpResponse("Письма отправлены!")
