# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import streamlit_chat as message
import os
from dotenv import load_dotenv
import time

def init():
    st.set_page_config(
        page_title="My ChatGPT : Python Streamlit",
        page_icon="💻"
    )

    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY")=="":
        failureKeyMessage = st.warning("No OPENAI_API_KEY found in Configuration!!")
        time.sleep(2)
        failureKeyMessage.empty()
        exit(1)
    else:
        successKeyMessage = st.info("OPENAI_API_KEY has been set.")
        time.sleep(2)
        successKeyMessage.empty()




def main(name):

    init()

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    st.header("My ChatGPT : Python")

    with st.sidebar:
        user_input = st.text_input("Please enter your query :", key="user_inpuit")

    if user_input:
        message.message("Hello i am Assistant!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
