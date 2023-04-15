import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

# from dotenv import load_dotenv  # pip install python-dotenv

PORT = 587
# Adjust server address, if you are not using @outlook
EMAIL_SERVER = "smtp-mail.outlook.com"

# Load the environment variables
current_dir = Path(__file__).resolve(
).parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
# load_dotenv(envars)

# Read environment variables
sender_email = 'vrsbusbookingsystem@outlook.com'
password_email = 'Vrsbusbooking123@'


def send_email(subject, receiver_email, name, city, to_city, seat_no):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("VRS Bus Booking Corp.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Dear {name},

Thank you for choosing our bus reservation system for your upcoming trip. We are happy to inform you that your reservation has been confirmed and your seat is secured.

Bus Details:
From: {city}
To: {to_city}
Seat Number: {seat_no}

We hope you enjoy your journey with us. Please arrive at the boarding point at least 30 minutes before the departure time.

In case of any further questions or concerns, please feel free to contact us.

Thank you,
VRS Bus Booking System
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Dear {name},</p>

<p>We are pleased to confirm your booking for the following bus journey:</p>


<p><strong>From:</strong> {city}</p>
<p><strong>To:</strong> {to_city}</p>

<p><strong>Seat number:</strong> {seat_no}</p>

<p>Please arrive at the bus station at least 15 minutes prior to departure. If you have any questions or concerns, please don't hesitate to contact us.</p>

<p>Thank you for choosing our bus booking system!</p>

<p>Best regards,</p>
<p>VRS BUS BOOKING SYSTEM</p>

      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


# if __name__ == "__main__":
#     send_email(
#         subject="Your bus reservation has been confirmed!",
#         name="Gowtham",
#         receiver_email="kavithagowtham205@gmail.com"
#     )
