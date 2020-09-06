import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = 'user@gmail.com'  # Введите ваш gmail
password = 'password'  # Пароль от gmail


def send_mail(subject_email='Hello World', body_email='Email Body',
              from_email='From Standalone coder <elvis66666@gmail.com>', to_emails=None,
              html_email=None):
    if isinstance(to_emails, str):
        to_emails = list(to_emails.split(","))

    assert isinstance(to_emails, list)

    # Формируем письмо
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)  # Приводим наш список эмейлов к строке, разделенных запятой
    msg['Subject'] = subject_email

    txt_part = MIMEText(body_email, 'plain')
    msg.attach(txt_part)

    # Если тело письма передается ввиде html
    if html_email is not None:
        html_part = MIMEText('<h1>Test html</h1>', 'html')
        msg.attach(html_part)

    # Настройки для подключения к серверу гугла
    google_host = 'smtp.gmail.com'
    google_host_port = '587'

    try:
        # используем smtplib для подключения к google
        server = smtplib.SMTP(host=google_host, port=google_host_port)  # Инициализиурем подключение
        server.ehlo()  # SMTP ehlo команда
        server.starttls()  # Устанавливает соединение с SMTP в TLS моде
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()
        return True
    except:
        return False

    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass
