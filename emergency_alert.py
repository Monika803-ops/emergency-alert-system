from twilio.rest import Client
import geocoder
import os
from dotenv import load_dotenv

# Twilio credentials
load_dotenv()

print("Twilio SID:",os.getenv("TWILIO_ACCOUNT_SID"))
print("Twilio Auth Token:",os.getenv("TWILIO_AUTH_TOKEN"))
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP_NUMBER = os.getenv('FROM_WHATSAPP_NUMBER')
TO_WHATSAPP_NUMBER = os.getenv('TO_WHATSAPP_NUMBER')  # Verified number

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return f"{g.city}, {g.state}, {g.country} - {g.latlng}"
    else:
        return "Location not available"

def send_emergency_alert():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    location = get_location()
    message_body = (
        "Emergency! Monika needs help. Please contact her immediately.\n"
        f"Location: {location}"
    )

    message = client.messages.create(
        body=message_body,
        from_=FROM_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )

    print("[ALERT SENT] Emergency WhatsApp alert sent.")
    print("[LOCATION] Included in message:", location)
    print("[SID]", message.sid)