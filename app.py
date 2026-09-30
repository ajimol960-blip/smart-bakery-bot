import streamlit as st
from libs.menu_loader import load_menu
from libs.llm_utils import send_message_to_llm,start_session
from libs.menu_loader import load_menu

#menu
CAKE_MENU = load_menu()
#UI
st.title("🎂Home Bakery Ai Assistant🎂")
st.markdown("Serving Dubai & Sharjah | Homemade Cakes | Payment On Delivery")

if "messages" not in st.session_state:
     start_session()
     welcome_message = (
          "Hi There Welcome to Habeebe Cakes\n\n"
          "Here is our menu:\n" + CAKE_MENU + "\n\n"
          "Would you like to place an order today?"         
     )
     st.session_state.messages = [{
          "role":"ai",
          "content": welcome_message
     }]
user_input = st.chat_input("Enter Your Message...")

if user_input:
    st.session_state.messages.append({
         "role":"user",
          "content": user_input
    })     
    llm_resp = send_message_to_llm(user_input)  
    #storing llm to chat history
    st.session_state.messages.append({
               "role":"ai",
                "content": llm_resp
          })                     

#     with st.chat_message("user"):
#          st.markdown(user_input)

for msg in st.session_state.messages:
     with st.chat_message(msg["role"]):
          st.markdown(msg["content"])          


