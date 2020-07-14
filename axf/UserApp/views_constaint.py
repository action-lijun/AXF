from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader


def send_email(email, name, token):
    subject = '啊哈'
    message = '白茶清欢无别事'

    index = loader.get_template('axf/user/register/active.html')



    context = {
        'name': name,
        'url': 'http://111.229.195.135:8000/axfuser/account/?token=' + str(token)
    }

    result = index.render(context=context)

    html_message = result

    from_email = 'li_jun_aha@163.com'
    recipient_list = [email]

    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)
