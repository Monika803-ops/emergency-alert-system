

Safe Walk - Real-Time Emergency Detection

Project Title

Safe Walk: AI-powered safety solution for real-time emergency detection.


Problem Statement 1 :Wave AI magic with groq

Objective

The project aims to provide an AI-based safety solution that monitors emergency keywords through voice recognition and detects suspicious activity through camera vision. If any danger is detected, the system immediately sends an emergency alert to the user’s designated contact via WhatsApp. This solution helps individuals feel secure without having to touch their phone during a potential emergency situation.

Real-World Use Case:

Walking alone at night or in secluded areas.

Detecting situations where the person may be in danger.

Sending instant alerts to loved ones or guardians for quick action.


🧠 Team & Approach

Team Name:OneSoulWithRam

Monika N V 
Linkedin: https://www.linkedin.com/in/monika-n-v-950321256
Github:https://github.com/Monika803-ops/


My Approach:

Why you chose this problem:
 The personal safety of individuals is a growing concern, especially for women and vulnerable individuals walking alone. This project addresses that by combining real-time AI with an emergency alert system.

Key challenges you addressed:

Integrating voice recognition and vision detection models in real-time without compromising performance.

Handling ambient noise for accurate voice detection.

Implementing a secure WhatsApp messaging system using Twilio for instant alerts.


Any pivots or breakthroughs: While working with Groq models for AI, we encountered challenges with real-time processing, but through threading and efficient resource management, we successfully enabled parallel processing of voice and vision models.


🛠️ Tech Stack

Core Technologies Used:

Frontend: HTML, CSS, JavaScript (Flask for UI rendering)

Backend: Python, Flask, Groq API

Database: None (Real-time processing with Groq models)

APIs: Twilio API (WhatsApp for emergency alerts)

Hosting: Local development (For the demo version)

Technologies Used: Groq API for fast AI inference


✨ Key Features

✅ Real-time Voice Detection: Detects emergency keywords like "help," "save me," and "danger."

✅ Vision-Based Threat Detection: Identifies suspicious movements or individuals through camera vision.

✅ Emergency WhatsApp Alert: Sends instant messages to a designated contact on detecting an emergency.

✅ AI-Powered Security: Uses Groq AI models for efficient real-time processing of voice and vision data.


Demo & Deliverables

Demo Video Link:https://youtu.be/62a1ThjeXg0?si=xcD90ZIWz48t9Ovr

PPT Link:
https://in.docworkspace.com/d/sIF2C54jNAeeAusAG

✅ Tasks & Bonus Checklist



🧪 How to Run the Project

Requirements:

Python 3.x

Dependencies:

Flask

SpeechRecognition

OpenCV

Twilio

dotenv

threading


.env file setup for Twilio credentials (ACCOUNT_SID, AUTH_TOKEN)


Local Setup:

1. Clone the repo:

git clone https://github.com/your-team/safewalk


2. Navigate into the project folder:

cd safewalk


3. Install dependencies:

pip install -r requirements.txt


4. Set up the environment variables in a .env file:

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
FROM_WHATSAPP_NUMBER=your_twilio_whatsapp_number
TO_WHATSAPP_NUMBER=your_emergency_contact_number


5. Run the project:

python safe_walk_groq.py


6. Open your browser and navigate to http://127.0.0.1:5000/ to view the demo.



🧬 Future Scope

Voice & Vision Model Enhancement: Improve the AI models to detect a wider range of emergency scenarios.

Mobile App Integration: Extend the project to mobile platforms (iOS/Android) for seamless integration and on-the-go safety.

More Integration: Add support for other emergency alert systems, like email or SMS, for broader accessibility.


📎 Resources / Credits

APIs or datasets used: Groq API for AI inference, Twilio for WhatsApp messaging.

Open-source libraries:

SpeechRecognition for voice detection

OpenCV for vision detection

Flask for web framework


Acknowledgements: Special thanks to the Groq team for providing high-performance models for real-time AI processing.

Final Words

This project was an exciting journey of integrating AI with real-world applications for improving personal safety. We faced challenges in processing voice and vision data in parallel, but with careful planning and implementation, we were able to create a functioning prototype. The experience of working with real-time communication systems like Twilio was invaluable, and we look forward to improving Safe Walk further.


  


