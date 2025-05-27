import requests
import time

TOKEN = "7537755812:AAHiATh4ry0BD7myVlwsr5qvP-ra87w3bug"
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
            text = message.get("text", "").lower()

            print(f"Received message: {text} from chat_id: {chat_id}")

            # Commands & replies
            if text == "/start":
                send_message(chat_id, "Welcome! How can I help you?")
            elif text == "/help":
                send_message(chat_id, "Available commands:\n/start\n/help\nhello\nhi\nwho are you\nhow are you")
            elif text == "hello":
                send_message(chat_id, "Hello! 👋")
            elif text == "hi":
                send_message(chat_id, "Hey there! 😊")
            elif text == "good morning":
                send_message(chat_id, "Good morning! Have a great day ☀️")
            elif text == "who are you":
                send_message(chat_id, "I’m your friendly chatbot! 🤖 Here to help.")
            elif text == "how are you":
                send_message(chat_id, "I'm doing great! Thanks for asking. 😊 How about you?")
            else:
                send_message(chat_id, "Sorry, I didn't understand that. Try /help to see what I can do.")

        time.sleep(1)

if __name__ == "__main__":
    main()
