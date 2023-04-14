import streamlit as st
from whatsapp import send_whatsapp_message

transaction_id = st.experimental_get_query_params()['id1'][0]
name = st.experimental_get_query_params()['id2'][0]
ph_no = st.experimental_get_query_params()['id3'][0]
from1 = st.experimental_get_query_params()['id4'][0]
to1 = st.experimental_get_query_params()['id5'][0]
date1 = st.experimental_get_query_params()['id6'][0]
selected_seats = st.experimental_get_query_params()['id7'][0]


def send_msg(user_id, from1, to1, date1, selected_seats, ph_no):
    message = f'''Get ready for a comfortable ride! Your bus booking has been confirmed. Sit back, relax, and enjoy the journey with us!

Dear {user_id},

We are happy to inform you that your bus booking has been confirmed for {date1} from {from1} to {to1}. Your seat number is {selected_seats}. Please arrive at the boarding point at least 30 minutes before departure.

Thank you for choosing our bus booking system. We wish you a safe and comfortable journey.

Best regards,
VRS Bus Booking System🌹'''
    send_whatsapp_message(message, ph_no)


st.write(transaction_id, name, ph_no, from1, to1, date1, selected_seats)
send_msg(name, from1, to1, date1, selected_seats, ph_no)
st.info(
    f'### Hi, {name} Your booking has been confirmed & the transaction id is {transaction_id}')
