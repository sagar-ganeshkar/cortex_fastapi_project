import streamlit as st
import requests


# Backend API URL
API_URL = "http://127.0.0.1:8015/ai-chat"


# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Snowflake GenAI Assistant",
    layout="centered"
)


st.title("📊 Snowflake GenAI Assistant")
st.write("Ask questions about your Orders data")


# ----------------------------
# Input Box
# ----------------------------
question = st.text_area(
    "Enter your question:",
    placeholder="Why is furniture category making loss?"
)


# ----------------------------
# Button
# ----------------------------
if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question")

    else:

        with st.spinner("Thinking..."):

            payload = {
                "question": question
            }

            try:

                response = requests.post(API_URL, json=payload)

                if response.status_code == 200:

                    data = response.json()

                    st.success("Answer:")

                    st.write(data["answer"])

                else:

                    st.error("API Error")
                    st.text(response.text)

            except Exception as e:

                st.error(f"Connection failed: {e}")
