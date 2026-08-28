import streamlit as st
import sqlite3
from database import create_table, insert_data
import pandas as pd
create_table()
st.set_page_config(page_title="Personal Information Form",page_icon="🎀",layout="centered")
st.title("🎀Personal Information Form🎀")
st.info("This form is created by Rupam as a fun activity and practice project as a student")
st.write("Please fill in your information below.")

with st.form("personal_form"):
 name=st.text_input("👤Name")
 age=st.number_input("🎂Age",min_value=1,max_value=100,step=1)
 gender=st.selectbox("Gender",["Select Gender","Male","Female","Other"])
 color=st.text_input("🎨color")
 fav_food=st.text_input("🍕Fav_Food")
 fav_subject=st.text_input("📚Fav_Subject")
 hobby=st.text_area("🎮Hobby")

 submit=st.form_submit_button("✨ Submit Form ✨")
 if submit:
   if name and color and fav_food and fav_subject and hobby:
    st.success("🎉Form Submitted Sucessfully!")
    insert_data(name, age, gender, color, fav_food, fav_subject, hobby)
    st.write("### Submitted Information")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("color:",color)
    st.write("Fav_Food:",fav_food)
    st.write("Fav_subject:",fav_subject)
    st.write("Hobby:",hobby)
   else:
    st.error("⚠️please fill all the required fields")
   st.write("### All Submitted Data")

conn = sqlite3.connect("personal_info.db")

df = pd.read_sql_query("SELECT * FROM personal_info", conn)

st.dataframe(df)

conn.close() 
