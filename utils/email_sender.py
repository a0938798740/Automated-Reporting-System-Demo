import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import logging
import config

class EmailSender:
    """
    Utility to send emails with attachments via SMTP.
    """
    @staticmethod
    def send_report(recipients, subject, body, attachment_path=None):
        msg = MIMEMultipart()
        msg['From'] = config.EMAIL_ACCOUNT
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg.attach(part)

        try:
            server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
            server.starttls()
            server.login(config.EMAIL_ACCOUNT, config.EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
            logging.info(f"Email sent to {recipients}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
