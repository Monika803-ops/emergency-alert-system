from flask import Flask, render_template
import threading
from model.vision_model import start_vision_detection
from audio_listener import start_audio_detection
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=start_vision_detection, daemon=True).start()
    threading.Thread(target=start_audio_detection, daemon=True).start()
    app.run(debug=True)


# audio_listener.py

import speech_recognition as sr
from emergency_alert import send_emergency_alert
from groq_integration import run_groq_audio_model

def start_audio_detection():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("[INFO] Listening for emergency keywords using Groq AI...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("[INFO] Waiting for voice...")
                audio = recognizer.listen(source, timeout=5)
                result = run_groq_audio_model(audio)
                if result.get("emergency_detected"):
                    print("[ALERT] Emergency keyword detected by Groq!")
                    send_emergency_alert()
            except sr.WaitTimeoutError:
                print("[INFO] Timeout - No voice detected.")
            except Exception as e:
                print(f"[ERROR] {e}")


# model/vision_model.py

from emergency_alert import send_emergency_alert
from groq_integration import run_groq_vision_model

def start_vision_detection():
    while True:
        frame = get_camera_frame()  # Replace with actual camera input logic
        result = run_groq_vision_model(frame)
        if result.get("is_threat"):
            print("[GROQ VISION] Threat detected!")
            send_emergency_alert()

def get_camera_frame():
    return None  # Replace with actual camera frame logic


# emergency_alert.py

import os
from twilio.rest import Client
load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP_NUMBER = os.getenv('FROM_WHATSAPP_NUMBER')
TO_WHATSAPP_NUMBER = os.getenv('TO_WHATSAPP_NUMBER')

def send_emergency_alert():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Emergency! Monika needs help. Please contact her immediately.",
        from_=FROM_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )
    print("[ALERT SENT] Emergency WhatsApp alert sent. SID:", message.sid)


# groq_integration.py

def run_groq_audio_model(audio):
    text = "help"  # Simulated transcribed text
    if "help" in text or "save me" in text or "danger" in text:
        return {"emergency_detected": True}
    return {"emergency_detected": False}

def run_groq_vision_model(frame):
    return {"is_threat": False}  # Change to True for test
