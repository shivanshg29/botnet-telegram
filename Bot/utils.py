import google.generativeai as genai
import json
from datetime import datetime
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model=genai.GenerativeModel('gemini-2.0-flash')

def ask_gemini(prompt):
    response=model.generate_content(prompt)
    return response.text.strip()

def get_current_meal():
    hour = datetime.now().hour
    if 6 <= hour < 11:
        return "breakfast"
    elif 11 <= hour < 16:
        return "lunch"
    elif 18 <= hour < 23:
        return "dinner"
    else:
        return None 

def menu():
    with open("./mess_menu.json", "r") as file:
        menu_data = json.load(file)
    current_day = datetime.now().strftime("%A")
    current_meal = get_current_meal()

    if current_meal is None:
        print("It's not meal time now.")
    else:
        today_menu = next((day for day in menu_data if day["day"] == current_day), None)
        if today_menu:
            items = today_menu.get(current_meal, [])
            reply = f"{current_meal.capitalize()} items for {current_day}:\n" + "\n".join(f"- {item}" for item in items)
            return reply
        else:
            reply = f"No menu found for {current_day}."
            return reply
        
def get_today_timetable():
    with open("./timetable.json", "r") as file:
        timetable = json.load(file)
    today = datetime.now().strftime("%A")
    today_schedule = timetable.get(today, [])

    if not today_schedule:
        return f"No classes scheduled for {today}."

    reply = f"📅 Time Table for {today}:\n"
    for entry in today_schedule:
        reply += (
            f"⏰ {entry['time']} - {entry['subject']}\n"
            f"   📍 Location: {entry['location']}\n"
            f"   📘 Type: {entry['type']}\n\n"
        )

    return reply.strip()
