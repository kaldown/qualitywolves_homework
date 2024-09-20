import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from schemas.ticker import TickerResult


def send_email(sender_email, receiver_email, subject, body: list[TickerResult], smtp_server, port, login, password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText('\n'.join(str(ticker) for ticker in body), 'plain'))

    with smtplib.SMTP(smtp_server, port) as server:
        try:
            server.starttls()
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        except Exception as e:
            print(e)
        finally:
            server.quit()
