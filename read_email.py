import email
import imaplib

host = 'imap.gmail.com'
username = 'user@gmail.com'  # Введите ваш gmail
password = 'password'  # Пароль от gmail


def read_email():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")  # выбираем письма во входящих
    _, search_data = mail.search(None, 'UNSEEN')  # Получает кортэж непрочитанных сообщений и разворачиваем его (SPREAD)

    # В данную переменную будет парсить данные по письмам
    email_data = {}
    my_messages = []

    # Разбиваем строку по пробелам
    for num in search_data[0].split():

        _, data = mail.fetch(num, '(RFC822)')  # Магическое число ^_^
        _, b = data[0]  # копаем до нужных нам данных
        email_msg = email.message_from_bytes(b)

        '''
            subject: =?utf-8?B?0JTQvtGB0YLRg9C/INC6INGD0YHRgtGA0L7QudGB0YLQstGDINGD?=
            =?utf-8?B?0YHQv9C10YjQvdC+INC+0YLQvtC30LLQsNC9?=
            to: elvis66666@gmail.com
            from: "Evernote" <no-reply@account.evernote.com>
            date: Sun, 06 Sep 2020 16:18:38 +0000
        '''
        for header in ['subject', 'to', 'from', 'date']:
            # print("{}: {}".format(header, email_msg[header]))
            email_data[header] = email_msg[header]

        # email_msg = email.message_from_string(b)
        for part in email_msg.walk():
            if part.get_content_type() == 'text/plain':  # текст
                body = part.get_payload(decode=True)
                # print(body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == 'text/html':  # html
                html_body = part.get_payload(decode=True)
                # print(html_body.decode())
                email_data['html_body'] = html_body.decode()

        my_messages.append(email_data)  # Собираем наши письма

    return my_messages


if __name__ == '__main__':
    my_inbox_emails = read_email()
    print(my_inbox_emails)
