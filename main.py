from vkbottle.bot import Bot, Message
import os

print("=== ENV KEYS ===")
print(sorted(os.environ.keys()))
print("================")
from config import VK_TOKEN, CHAT_ID

bot = Bot(VK_TOKEN)

users = {}

@bot.on.message()
async def all_messages(message: Message):

    print("=" * 40)
    print("TEXT:", message.text)
    print("FROM:", message.from_id)
    print("=" * 40)

    if message.text.lower() in ["/start", "start", "начать"]:

        users[message.from_id] = {"step": "name"}

        await message.answer(
            "👋 Привет!\n\n"
            "1️⃣ Как вас зовут?"
        )

        return

    user = users[message.from_id]
    step = user["step"]

    # -------------------------
    # Имя
    # -------------------------

    if step == "name":

        user["name"] = message.text
        user["step"] = "city"

        await message.answer(
            "2️⃣ Из какого вы города?"
        )
        return

    # -------------------------
    # Город
    # -------------------------

    if step == "city":

        user["city"] = message.text
        user["step"] = "experience"

        await message.answer(
            "3️⃣ Есть ли у вас опыт в продажах?\n\n"
            "Ответьте:\n"
            "Да\n"
            "или\n"
            "Нет"
        )

        return

    # -------------------------
    # Опыт
    # -------------------------

    if step == "experience":

        user["experience"] = message.text
        user["step"] = "budget"

        await message.answer(
            "4️⃣ Какой бюджет готовы вложить?\n\n"
            "Напишите один из вариантов:\n\n"
            "До 50 000 ₽\n"
            "50–150 тыс. ₽\n"
            "Более 150 тыс. ₽\n"
            "Пока не знаю"
        )

        return

    # -------------------------
    # Бюджет
    # -------------------------

    if step == "budget":

        user["budget"] = message.text
        user["step"] = "income"

        await message.answer(
            "5️⃣ Какой доход хотите получать?\n\n"
            "Напишите один из вариантов:\n\n"
            "До 100 тыс.\n"
            "100–200 тыс.\n"
            "Более 200 тыс."
        )

        return

    # -------------------------
    # Доход
    # -------------------------

    if step == "income":

        user["income"] = message.text
        user["step"] = "phone"

        await message.answer(
            "6️⃣ Напишите ваш номер телефона."
        )

        return

    # -------------------------
    # Телефон
    # -------------------------

    if step == "phone":

        user["phone"] = message.text

        text = (
            "🔥 НОВАЯ ЗАЯВКА\n\n"
            f"👤 Имя: {user['name']}\n"
            f"🏙 Город: {user['city']}\n"
            f"💼 Опыт: {user['experience']}\n"
            f"💰 Бюджет: {user['budget']}\n"
            f"🎯 Доход: {user['income']}\n"
            f"📞 Телефон: {user['phone']}\n\n"
            f"VK: https://vk.com/id{message.from_id}"
        )

        await bot.api.messages.send(
            peer_id=CHAT_ID,
            message=text,
            random_id=0
        )

        await message.answer(
            "✅ Спасибо!\n\n"
            "Егор свяжется с вами в ближайшее время."
        )

        users.pop(message.from_id, None)

        return


print("🤖 Бот запущен")

bot.run_forever()
