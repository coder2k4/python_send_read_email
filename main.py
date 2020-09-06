import sys

from send_mail import send_mail

if __name__ == '__main__':
    print(sys.argv)  # python main.py mailfrom@gmail.com mailto@mail.ru "String to list test"

    if len(sys.argv) > 1:
        fromE = sys.argv[1]  # elvis66666@gmail.com

    if len(sys.argv) > 2:
        toE = sys.argv[2]  # coder2k@mail.ru

    if len(sys.argv) > 3:
        bodyE = sys.argv[3] # "String to list test"

    # print(fromE, toE, bodyE)
    response = send_mail(from_email=fromE, to_emails=toE, body_email=bodyE)
    print(response)
