from osonbot import Bot
from google import genai

bot = Bot("BOT_TOKEN")

client = genai.Client(api_key="YOUR_API_KEY")

def gemini(msg):
    return client.models.generate_content(model="gemini-2.5-flash", contents=msg['text'], config=genai.types.GenerateContentConfig(
        system_instruction="You are Gemini powered by google. You answer the questions in uzbek language"
    )).text

bot.when("/start", "Salom {first_name}")
bot.when("*", gemini)

bot.run()
