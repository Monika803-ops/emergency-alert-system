import speech_recognition as sr
from emergency_alert import send_emergency_alert

def start_audio_detection():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("[INFO] Listening for emergency keywords like 'help', 'save me'...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("[INFO] Waiting for voice...")
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio).lower()
                print(f"[HEARD] {text}")

                if "help" in text or "save me" in text or "danger" in text:
                    print("[ALERT] Emergency keyword detected!")
                    send_emergency_alert()

            except sr.WaitTimeoutError:
                print("[INFO] Timeout - No voice detected.")
            except sr.UnknownValueError:
                print("[INFO] Could not understand the audio.")
            except Exception as e:
                print(f"[ERROR] {e}")