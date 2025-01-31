import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini AI with API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API key not found. Please set it in the .env file.")
else:
    genai.configure(api_key=api_key)

def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt[0], question])
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Function to retrieve query from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return []

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - name, Class, 
    marks \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM students ;
    \nExample 2 - Tell me all the students studying in in Class 10?,  
    the SQL command will be something like this SELECT * FROM students 
    where CLASS="Class 10"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Welcome to the lp school")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    if response:
        st.write(f"Generated SQL query: {response}")
        rows = read_sql_query(response, "students.db")
        st.subheader("The Response is")
        for row in rows:
            st.write(row)

