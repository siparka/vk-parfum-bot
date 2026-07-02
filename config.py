import os

print("VK_TOKEN getenv:", os.getenv("VK_TOKEN"))
print("CHAT_ID getenv:", os.getenv("CHAT_ID"))

print("VK_TOKEN environ:", os.environ.get("VK_TOKEN"))
print("CHAT_ID environ:", os.environ.get("CHAT_ID"))

raise SystemExit
