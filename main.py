import json
import telegram

Lire les infos dans config.json,
with open("config.json", "r") as f:
    config = json.load(f)

bot = telegram.Bot(token=config["token"])
bot.send_message(chat_id=config["chat_id"], text="Le bot fonctionne ✅")
