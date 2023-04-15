
from twilio.rest import Client


def send_whatsapp_message(message1, ph_no):
    account_sid = 'ACe70026797af84a122af1a38a866193ec'

    auth_token = '2e056ba765fc64980c2831186b0ffe67'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',  # This is your Sandbox number
        body=message1,
        # This is the number you want to send the message to
        to=f'whatsapp:+91{ph_no}'
    )

    print(message.sid)
