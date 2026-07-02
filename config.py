from dotenv import load_dotenv
import os

load_dotenv()

print("VK_TOKEN =", os.getenv("VK_TOKEN"))
print("CHAT_ID =", os.getenv("CHAT_ID"))

VK_TOKEN = os.getenv("VK_TOKEN")

chat = os.getenv("CHAT_ID")
if chat is None:
    raise ValueError("CHAT_ID не найден в переменных окружения!")

CHAT_ID = int(chat)
