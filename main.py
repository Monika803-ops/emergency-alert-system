from flask import Flask, render_template
import threading
from audio_listener import start_audio_detection
from vision_model2 import start_vision_detection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=start_audio_detection).start()
    threading.Thread(target=start_vision_detection).start()
    app.run(debug=True)