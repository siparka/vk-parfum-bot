from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 40)
print("VK_TOKEN =", os.getenv("VK_TOKEN"))
print("CHAT_ID =", os.getenv("CHAT_ID"))
print("=" * 40)

VK_TOKEN = os.getenv("VK_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
