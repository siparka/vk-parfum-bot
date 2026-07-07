from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from config import VK_TOKEN, CHAT_ID

bot = Bot(VK_TOKEN)

# ========== ВОПРОСЫ ==========
QUESTIONS = {
    "q1": {
        "text": (
            "❓ Вопрос 1/8\n\n"
            "Расскажите, кто вы?\n\n"
            "1️⃣ Хочу начать свой бизнес с нуля\n"
            "2️⃣ Уже есть опыт в продажах\n"
            "3️⃣ Занимаюсь парфюмерией/косметикой\n"
            "4️⃣ Блогер / инфлюенсер\n"
            "5️⃣ У меня есть розничный магазин\n"
            "6️⃣ Просто изучаю возможности"
        ),
        "options": [
            "1️⃣ Хочу начать с нуля",
            "2️⃣ Есть опыт в продажах",
            "3️⃣ Занимаюсь парфюмерией",
            "4️⃣ Блогер / инфлюенсер",
            "5️⃣ Есть розничный магазин",
            "6️⃣ Изучаю возможности",
        ],
    },
    "q2": {
        "text": (
            "❓ Вопрос 2/8\n\n"
            "Какой у вас сейчас основной источник дохода?\n\n"
            "1️⃣ Работа по найму\n"
            "2️⃣ Свой бизнес\n"
            "3️⃣ Фриланс / самозанятость\n"
            "4️⃣ Инвестиции / пассивный доход\n"
            "5️⃣ Временно без работы / ищу варианты"
        ),
        "options": [
            "1️⃣ Работа по найму",
            "2️⃣ Свой бизнес",
            "3️⃣ Фриланс / самозанятость",
            "4️⃣ Инвестиции",
            "5️⃣ Временно без работы",
        ],
    },
    "q3": {
        "text": (
            "❓ Вопрос 3/8\n\n"
            "Что для вас самое важное в новом деле?\n\n"
            "1️⃣ Высокий доход\n"
            "2️⃣ Свободный график\n"
            "3️⃣ Работа из дома\n"
            "4️⃣ Возможность расти\n"
            "5️⃣ Работать с красивым продуктом"
        ),
        "options": [
            "1️⃣ Высокий доход",
            "2️⃣ Свободный график",
            "3️⃣ Работа из дома",
            "4️⃣ Возможность расти",
            "5️⃣ Красивый продукт",
        ],
    },
    "q4": {
        "text": (
            "❓ Вопрос 4/8\n\n"
            "Какой бюджет вы готовы вложить в старт?\n\n"
            "1️⃣ До 7 500 ₽\n"
            "2️⃣ 30 000 ₽\n"
            "3️⃣ 250 000 ₽\n"
            "4️⃣ Пока не знаю, мне надо подумать\n\n"
            "💡 Средний старт партнёра — 50 000 ₽, окупаемость 2-3 месяца."
        ),
        "options": [
            "1️⃣ До 7 500 ₽",
            "2️⃣ 30 000 ₽",
            "3️⃣ 250 000 ₽",
            "4️⃣ Пока не знаю, мне надо подумать",
        ],
    },
    "q5": {
        "text": (
            "❓ Вопрос 5/8\n\n"
            "Есть ли у вас своя аудитория или каналы коммуникации?\n\n"
            "1️⃣ Да, веду блог / канал / YouTube\n"
            "2️⃣ Да, есть чаты и группы\n"
            "3️⃣ Да, есть клиентская база\n"
            "4️⃣ Нет, начну с нуля\n"
            "5️⃣ Планирую создать"
        ),
        "options": [
            "1️⃣ Есть блог/канал",
            "2️⃣ Есть чаты/группы",
            "3️⃣ Есть клиентская база",
            "4️⃣ Нет, начну с нуля",
            "5️⃣ Планирую создать",
        ],
    },
    "q6": {
        "text": (
            "❓ Вопрос 6/8\n\n"
            "Сколько времени в день вы готовы уделять бизнесу?\n\n"
            "1️⃣ До 2 часов (хобби)\n"
            "2️⃣ 2-4 часа (полдня)\n"
            "3️⃣ 4-6 часов (активный рост)\n"
            "4️⃣ Полный рабочий день\n"
            "5️⃣ Всё свободное время (горю желанием!)"
        ),
        "options": [
            "1️⃣ До 2 часов",
            "2️⃣ 2-4 часа",
            "3️⃣ 4-6 часов",
            "4️⃣ Полный рабочий день",
            "5️⃣ Всё свободное время",
        ],
    },
    "q7": {
        "text": (
            "❓ Вопрос 7/8\n\n"
            "Что вас больше всего останавливает от старта?\n\n"
            "1️⃣ Страх, что не получится\n"
            "2️⃣ Не хватает опыта в продажах\n"
            "3️⃣ Боюсь вкладывать деньги без гарантий\n"
            "4️⃣ Не знаю, как найти клиентов\n"
            "5️⃣ Ничего не останавливает — хочу начать!\n\n"
            "💡 80% наших партнёров начинали с нуля."
        ),
        "options": [
            "1️⃣ Страх неудачи",
            "2️⃣ Нет опыта в продажах",
            "3️⃣ Боюсь вкладывать деньги",
            "4️⃣ Не знаю как найти клиентов",
            "5️⃣ Ничего не останавливает",
        ],
    },
    "q8": {
        "text": (
            "❓ Вопрос 8/8\n\n"
            "Какой доход вы хотели бы выйти через 3-6 месяцев?\n\n"
            "1️⃣ 50 000 - 100 000 ₽/мес\n"
            "2️⃣ 100 000 - 200 000 ₽/мес\n"
            "3️⃣ 200 000 - 500 000 ₽/мес\n"
            "4️⃣ Более 500 000 ₽/мес\n"
            "5️⃣ Пока не загадываю\n\n"
            "💎 Топ-партнёры зарабатывают от 300 000 ₽/мес."
        ),
        "options": [
            "1️⃣ 50-100 тыс. ₽",
            "2️⃣ 100-200 тыс. ₽",
            "3️⃣ 200-500 тыс. ₽",
            "4️⃣ Более 500 тыс. ₽",
            "5️⃣ Пока не загадываю",
        ],
    },
}

# ========== ХРАНИЛИЩЕ ПОЛЬЗОВАТЕЛЕЙ ==========
users = {}  # { user_id: {"step": "...", "answers": {...}} }


# ========== КЛАВИАТУРЫ ==========
def make_keyboard(options):
    """Клавиатура с вариантами ответов (кнопки друг под другом)"""
    keyboard = Keyboard(one_time=False, inline=False)
    for opt in options:
        keyboard.add(Text(opt), color=KeyboardButtonColor.PRIMARY)
        keyboard.row()
    return keyboard.get_json()


def make_start_keyboard():
    """Клавиатура: Да / Просто смотрю"""
    keyboard = Keyboard(one_time=True, inline=False)
    keyboard.add(Text("✅ Да, хочу узнать"), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("❌ Просто смотрю"), color=KeyboardButtonColor.SECONDARY)
    return keyboard.get_json()


# ========== ОБРАБОТЧИКИ ==========

@bot.on.message(text=["/start", "start", "начать"])
async def start(message: Message):
    """Начало — приветствие и две кнопки"""
    users[message.from_id] = {"step": "start_choice", "answers": {}}
    await message.answer(
        "👋 Привет! Я помощник Егора, руководителя партнёрской сети ParfumBusiness.\n\n"
        "За 3 минуты отвечу на 8 вопросов и расскажу, подходит ли вам наш формат партнёрства.\n\n"
        "А главное — мы уже подготовили для вас:\n"
        "✅ Готовую модель запуска продаж\n"
        "✅ Обучение с нуля\n"
        "✅ Поддержку на старте\n\n"
        "🔽 Начнём?",
        keyboard=make_start_keyboard(),
    )


@bot.on.message(text="✅ Да, хочу узнать")
async def start_survey(message: Message):
    """Пользователь согласился — начинаем опрос с q1"""
    if message.from_id not in users:
        await message.answer("Напишите /start")
        return

    users[message.from_id] = {"step": "q1", "answers": {}}
    q = QUESTIONS["q1"]
    await message.answer(q["text"], keyboard=make_keyboard(q["options"]))


@bot.on.message(text="❌ Просто смотрю")
async def decline(message: Message):
    """Пользователь отказался — удаляем из памяти"""
    users.pop(message.from_id, None)
    await message.answer("Хорошо! Если передумаете — просто напишите /start")


# ========== ГЛАВНЫЙ ОБРАБОТЧИК (шаги q1–q8 и phone) ==========

@bot.on.message()
async def handle_all(message: Message):
    """
    Обрабатывает:
      - ответы на вопросы q1–q8
      - ввод номера телефона
      - игнорирует пользователей не в опросе
    """
    if message.from_id not in users:
        await message.answer("Напишите /start")
        return

    user = users[message.from_id]
    step = user["step"]

    # === ШАГ: выбор Да / Просто смотрю (пропускаем) ===
    if step == "start_choice":
        return

    # === ШАГ: ввод телефона ===
    if step == "phone":
        phone = message.text.strip()

        # Простейшая валидация: номер должен содержать цифры
        if not any(ch.isdigit() for ch in phone):
            await message.answer("Пожалуйста, введите номер телефона в формате +7XXXXXXXXXX")
            return

        answers = user["answers"]

        # Получаем имя из профиля ВК
        try:
            user_info = await bot.api.users.get(message.from_id)
            full_name = f"{user_info[0].first_name} {user_info[0].last_name}"
        except Exception:
            full_name = "Неизвестно"

        # Формируем отчёт
        report = (
            f"🔔 НОВЫЙ ЛИД!\n\n"
            f"📞 Телефон: {phone}\n\n"
            f"1️⃣ {answers.get('q1', '—')}\n"
            f"2️⃣ {answers.get('q2', '—')}\n"
            f"3️⃣ {answers.get('q3', '—')}\n"
            f"4️⃣ {answers.get('q4', '—')}\n"
            f"5️⃣ {answers.get('q5', '—')}\n"
            f"6️⃣ {answers.get('q6', '—')}\n"
            f"7️⃣ {answers.get('q7', '—')}\n"
            f"8️⃣ {answers.get('q8', '—')}\n\n"
            f"👤 {full_name}\n"
            f"🆔 vk.com/id{message.from_id}"
        )

        # Отправляем в чат
        await bot.api.messages.send(
            peer_id=CHAT_ID,
            message=report,
            random_id=0,
        )

        # Благодарим
        await message.answer(
            "✅ Спасибо! Егор свяжется с вами в ближайшее время.",
        )

        # Удаляем из памяти
        users.pop(message.from_id, None)
        return

    # === ШАГИ q1–q8 ===
    if step.startswith("q"):
        q_key = step
        q = QUESTIONS[q_key]
        q_number = int(step[1:])  # q1 → 1, q8 → 8

        # Проверка, что ответ — один из вариантов
        if message.text not in q["options"]:
            await message.answer("Пожалуйста, выберите ответ кнопкой 👇")
            return

        # Сохраняем ответ
        user["answers"][q_key] = message.text

        # Определяем следующий шаг
        if q_number < 8:
            next_key = f"q{q_number + 1}"
            user["step"] = next_key
            next_q = QUESTIONS[next_key]
            await message.answer(next_q["text"], keyboard=make_keyboard(next_q["options"]))
        else:
            # Все 8 вопросов пройдены — запрашиваем телефон
            user["step"] = "phone"

            # Клавиатура с подсказкой
            kb = Keyboard(one_time=True, inline=False)
            kb.add(Text("📱 Поделиться номером"), color=KeyboardButtonColor.POSITIVE)

            await message.answer(
                "📱 Супер! Остался последний шаг.\n\n"
                "Напишите ваш номер телефона в формате +7XXXXXXXXXX",
                keyboard=kb.get_json(),
            )


# ========== ЗАПУСК ==========
print("🤖 Bot started")
bot.run_forever()
