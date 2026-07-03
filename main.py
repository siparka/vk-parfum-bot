from vkbottle.bot import Bot, Message
from config import VK_TOKEN, CHAT_ID

bot = Bot(VK_TOKEN)

users = {}


@bot.on.message(text=["/start", "start", "начать"])
async def start(message: Message):
    users[message.from_id] = {"step": "name"}

    await message.answer("👋 Привет!\n\n1️⃣ Как вас зовут?")


@bot.on.message()
async def handler(message: Message):

    if message.from_id not in users:
        await message.answer("Напишите /start")
        return

    user = users[message.from_id]

    step = user["step"]

    if step == "name":
        user["name"] = message.text
        user["step"] = "city"
        await message.answer("2️⃣ Из какого вы города?")
        return

    if step == "city":
        user["city"] = message.text
        user["step"] = "done"

        await bot.api.messages.send(
            peer_id=CHAT_ID,
            message=(
                "🔥 НОВАЯ ЗАЯВКА\n\n"
                f"👤 {user['name']}\n"
                f"🏙 {user['city']}\n"
            ),
            random_id=0
        )

        await message.answer("✅ Спасибо! Егор свяжется с вами в ближайшее время.")
        users.pop(message.from_id, None)
        return


print("🤖 Bot started")
bot.run_forever()
