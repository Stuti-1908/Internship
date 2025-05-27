import requests
import time

TOKEN = "8068637667:AAGDD3L_TtUchpPbyhyRdqbFCfASwDRw8E0"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=payload)
    print(f"Sent message '{text}' with status {response.status_code}")
    print("Response:", response.json())

def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def main():
    offset = None
    print("Bot started...")

    while True:
        updates = get_updates(offset)
        for update in updates.get("result", []):
            offset = update["update_id"] + 1  
            message = update.get("message")
            if not message:
                continue
            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            print(f"Received message: {text} from chat_id: {chat_id}")

            # Simple commands response
            if text.lower() == "/start":
                send_message(chat_id, "Welcome! How can I help you?")
            elif text.lower() == "hello":
                send_message(chat_id, "Hello! 👋")
            else:
                send_message(chat_id, "Sorry, I didn't understand that. Try /start or say Hello.")

        time.sleep(1)  # avoid flooding Telegram server

if __name__ == "__main__":
    main()
