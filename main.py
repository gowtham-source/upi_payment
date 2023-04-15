import streamlit as st
from mail import send_email

transaction_id = st.experimental_get_query_params()['id1'][0]
name = st.experimental_get_query_params()['id2'][0]
email = st.experimental_get_query_params()['id3'][0]
from1 = st.experimental_get_query_params()['id4'][0]
to1 = st.experimental_get_query_params()['id5'][0]
date1 = st.experimental_get_query_params()['id6'][0]
selected_seats = st.experimental_get_query_params()['id7'][0]


# st.write(transaction_id, name, email, from1, to1, date1, selected_seats)

send_email(
    subject="Your bus reservation has been confirmed!",
    name=name,
    receiver_email=email,
    city=from1,
    to_city=to1,
    seat_no=selected_seats
)

st.write("## Thank you for choosing our bus reservation system for your upcoming trip. We are happy to inform you that your reservation has been confirmed and your seat is secured.")
st.info("### Your ticket has been sent to your email address. Please check your email.")
