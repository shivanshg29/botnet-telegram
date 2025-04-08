
# 🤖 Botnet - AI Telegram Bot using Django + Gemini

**Botnet** is a Telegram bot powered by Django REST Framework and Google's Gemini AI. It handles intelligent conversation, command responses, and supports features like rate limiting, authentication, and messaging.

---

## 📁 Project Structure

```
botnet/
│
├── Bot/                          # Django app for Telegram Bot
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── Botnet/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── Botnet_README.txt
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/botnet.git
cd botnet
```

### 2. Create Virtual Environment and Install Requirements

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add the Following to `.env`

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
BOT_PASSWORD=your_password
```

> You can use `python-decouple` or set them directly in `settings.py`.

### 4. Set Webhook

Use this command to set the webhook (example for Railway/Render):

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" -d "url=https://<your-domain>/bot/"
```

---

## 💬 Telegram Bot Commands

```
✨ *Welcome! Here are your available commands:* ✨

🍽️  /mess — *View today's Mess Menu*
📚  /timetable — *Check today's Lecture/Lab Schedule*
💬  /chat <your message> — *Talk with Gemini AI*
```

Make sure to set `"parse_mode": "Markdown"` in the payload.

---

## 🔗 Telegram Bot Link

Click here to chat with the bot:  
👉 [https://t.me/WebNetFatherBot](https://t.me/WebNetFatherBot)

---

## 🛡️ Features

- Function-based views (DRF)
- Gemini AI integration
- Telegram bot API
- Rate limiting (10 req/min globally)

---

## 🛠️ To Run the Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🙋‍♂️ Contributions

PRs and issues are welcome! Feel free to fork the repo and enhance the bot with new features like:
- Persistent auth via database
- Logging with Sentry
- Chat history tracking
- Admin commands
