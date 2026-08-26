import streamlit as st
import sqlite3
from database import create_table, insert_data

create_table()
st.title("Personal Information Form")
st.info("This form is created by Rupam as a fun activity and practice project as a student")
st.write("Please fill in your information below.")

with st.form("personal_form"):
 name=st.text_input("Name")
 age=st.number_input("Age",min_value=1,max_value=100,step=1)
 gender=st.selectbox("Gender",["Select Gender","Male","Female","Other"])
 village=st.text_input("Village")
 district=st.text_input("District")
 occupation=st.text_input("Occupation")
 address=st.text_area("Address")

 submit=st.form_submit_button("Submit Form")
 if submit:
   if name and village and district and occupation and address:
    st.success("Form Submitted Sucessfully!")
    insert_data(name, age, gender, village, district, occupation, address)
    st.write("### Submitted Information")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("Village:",village)
    st.write("District:",district)
    st.write("Occupaion:",occupation)
    st.write("Address:",address)
   else:
    st.error("please fill all the required fields")
