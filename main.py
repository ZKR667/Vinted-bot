import os
import requests
import time
import telegram

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MARGE_MIN = float(os.getenv("MARGE_MIN", "0.35"))

bot = telegram.Bot(token=TOKEN)

def chercher_bons_plans():
    url = "https://api.vinted.com/items?search_text=chaussures"
    try:
        response = requests.get(url)
        data = response.json()
        for item in data.get("items", []):
            prix = float(item.get("price", 0))
            prix_achat = float(item.get("purchase_price", 1))  # éviter division par 0
            marge = (prix - prix_achat) / prix_achat
            if marge >= MARGE_MIN:
                msg = f"Bon plan: {item.get('title', 'Inconnu')} à {prix}€ (marge {marge*100:.1f}%)"
                bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print("Erreur:", e)

if name == "main":
    while True:
        chercher_bons_plans()
        time.sleep(3600
