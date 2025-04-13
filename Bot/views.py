from .utils import ask_gemini,menu,get_today_timetable
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from rest_framework.decorators import api_view,permission_classes
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def telegram_webhook(request):
    data=request.data
    message = data.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    text = message.get('text')
    reply=""
    if chat_id and text=="/mess":
        reply=menu()
    elif chat_id and text=="/timetable":
        reply=get_today_timetable()
    elif chat_id and text.startswith("/chat"):
        user_message = text.replace("/chat", "", 1).strip()
        if user_message:
            try:
                reply = ask_gemini(user_message)
            except:
                return {"Error":"Gemini API Error"}
        else:
            reply = "Ask Something"
    else:
        reply = (
            "✨ *Welcome! Here are your available commands:* ✨\n\n"
            "🍽️  `/mess` — *View today's Mess Menu*\n"
            "📚  `/timetable` — *Check today's Lecture/Lab Schedule*\n"
            "💬  `/chat <your message>` — *Talk with Gemini AI*\n\n"
            "_Example_: `/chat What is Machine Learning?`"
        )


    telegram_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": reply,
    }
    try:
        response = requests.post(telegram_url, json=payload)
    except requests.exceptions.RequestException as err:
        print("Error in posting to Telegram:", err)


    return Response({"status": "ok"})