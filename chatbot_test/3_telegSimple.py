import requests

TOKEN = "8068637667:AAGDD3L_TtUchpPbyhyRdqbFCfASwDRw8E0"
CHAT_ID = 5140261424  # ✅ Replace with your actual chat ID
MESSAGE = "🚀 Hello from your Python bot!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

response = requests.post(url, data=payload)
print("Status:", response.status_code)
print("Response:", response.json())
