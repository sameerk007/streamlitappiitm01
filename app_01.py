import streamlit as st

with st.form(key="my_form"):
    num1 = st.text_input("Num1")
    num2 = st.text_input("Num2")
    submit_button = st.form_submit_button("Calculate")
if submit_button:
    st.write('The Sum of Num1 & Num2 is ',float(num1)+float(num2))
