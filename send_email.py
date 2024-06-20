import smtplib, ssl


def mail(query):

    host = "smtp.gmail.com"
    port = 465
    username = "russel.nlwork@gmail.com"
    password = "cntv szya yjjs pazq"
    receiver = "russel.workid@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, query)
