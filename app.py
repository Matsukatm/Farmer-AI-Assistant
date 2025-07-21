from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import uuid
import os

from core.message_processor import process_farmer_message
from integrations.whatsapp_handler import handle_whatsapp_message
from config import Config

app = Flask(__name__, 
           template_folder='web/templates',
           static_folder='web/static')
app.secret_key = Config.SECRET_KEY

# Store chat sessions (use Redis/DB for production)
chat_sessions = {}

# Web Interface Routes
@app.route('/')
def index():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        chat_sessions[session['session_id']] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def web_chat():
    data = request.json
    message = data.get('message', '')
    language = data.get('language', 'en')
    session_id = session.get('session_id')
    
    # Process the farmer's message
    response = process_farmer_message(message, language)
    
    # Store chat history
    if session_id not in chat_sessions:
        chat_sessions[session_id] = []
    
    chat_sessions[session_id].append({
        'user': message,
        'bot': response,
        'timestamp': datetime.now().isoformat()
    })
    
    return jsonify({'response': response})

# WhatsApp Webhook
@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    return handle_whatsapp_message(request)

@app.route('/history')
def get_history():
    session_id = session.get('session_id')
    return jsonify(chat_sessions.get(session_id, []))

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)