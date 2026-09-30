from google import genai
# import google.generativeai as genai
from libs.menu_loader import load_menu
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv()
#menu
menu_text = load_menu()


SYSTEM_INSTRUCTIONS = (
    f"You are a friendly assistant for a homemade cake business based in Dubai and Sharjah.Your Name is Habeebe Cakes\n"
    f"Here is the cake menu:\n{menu_text}\n\n"
    "Help the customer through the following steps:\n"
    "1. Greet the customer and show the menu.\n"
    "2. Ask what cake they want and confirm it exists in the menu.\n"
    "3. Ask for their delivery location (only Dubai or Sharjah).\n"
    "4. Ask for preferred delivery time.\n"
    "5. Ask for the occasion (e.g., birthday, festival, etc.).\n"
    "6. Ask if they need special decorations (name or other requests).\n"
    "7. Once all info is collected, generate a clear and cheerful order summary:\n"
    "   - Cake name\n   - Price (AED)\n   - Location\n   - Delivery time\n   - Occasion\n   - Decorations\n"
    "   - Total\n"
    "8. End by reminding them that payment is offline.\n"
    "Use emojis to make the experience friendly and fun!"
)
# setting up LLM
API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)
# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("gemini-3.5-flash-lite")
chat = None
def start_session():
    global chat
    chat = client.chats.create(
           model="gemini-3.5-flash-lite",
           config=types.GenerateContentConfig(
    # chat = model.start_chat()
    #    chat.send_message(SYSTEM_INSTRUCTIONS)
            system_instruction = SYSTEM_INSTRUCTIONS
          )
        )
 
print("LLM conf completed")  

def send_message_to_llm(message):
    resp = chat.send_message(message)
    text = resp.text
    return text