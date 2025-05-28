import requests
import time
import json
import telegram

Charger la config,
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["telegram_token"]
CHAT_ID = config["chat_id"]
MARGE_MIN = config.get("marge_min", 0.35)

bot = telegram.Bot(token=TOKEN)

def chercher_bons_plans():
    # Exemple simple: recherche fictive Vinted (à adapter)
    url = "https://api.vinted.com/items?search_text=chaussures"
    try:
        response = requests.get(url)
        data = response.json()
        for item in data["items"]:
            prix = float(item["price"])
            prix_achat = float(item["purchase_price"])
            marge = (prix - prix_achat) / prix_achat
            if marge >= MARGE_MIN:
                msg = f"Bon plan: {item['title']} à {prix}€ (marge {marge*100:.1f}%)"
                bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print("Erreur:", e)

if name == "main":
    while True:
        chercher_bons_plans()
        time.sleep(3600)
