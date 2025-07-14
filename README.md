## 🤖 Telegram Echo Bot

Bu oddiy Telegram bot foydalanuvchidan kelgan xabarni **o'ziga qaytaradi** (echo qiladi).
`python-telegram-bot` kutubxonasi yordamida ishlab chiqilgan.

---

### 📦 Talab qilinadigan kutubxonalar

* `python-telegram-bot==13.15`
* `python-dotenv`

---

### 🛠 O'rnatish

1. Repository-ni klon qiling:

```bash
git clone https://github.com/your-username/echo-bot.git
cd echo-bot
```

2. Virtual muhit yarating va aktivlashtiring:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Kutubxonalarni o'rnating:

```bash
pip install -r requirements.txt
```

`requirements.txt` fayli quyidagicha ko'rinishda bo'lishi kerak:

```txt
python-telegram-bot==13.15
python-dotenv
```

---

### 🔐 `.env` fayli

`.env` fayl yarating va bot tokeningizni quyidagicha joylang:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

---

### 🚀 Ishga tushurish

```bash
python main.py
```

---

### 📂 Fayl tuzilmasi

```bash
echo-bot/
├── main.py
├── .env
├── requirements.txt
└── README.md
```

