import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender = "vrushabhmanatkar13@gmail.com"
reaciver = "vrushabh7.m@gmail.com"
password = "ujjk qhyf mxfg yhav"

infobeans = "vrushabh.manatkar@infobeans.com"
infobeans_pass = "tfez ilgs yrgn gtkf"
infobeans_rec = "jaya.sisodia@infobeans.com"


class Setup_email:

    def __init__(self, Sender_email, Reciver_email, Subject, Body) -> None:
        self.Sender_email = Sender_email
        self.Reciver_email = Reciver_email
        self.Subject = Subject
        self.Body = Body

    def setup_message(self):
        messgae = MIMEMultipart()
        messgae["From"] = self.Sender_email
        messgae["To"] = self.Reciver_email

        messgae["Subject"] = self.Subject
        messgae.attach(MIMEText(self.Body, "plain"))
        self.messgae = messgae

    def send_email(self, password):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.Sender_email, password)
        server.send_message(self.messgae)
        server.quit()
