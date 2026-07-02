from dotenv import load_dotenv
import os

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
