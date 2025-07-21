# 🌱 Farmer AI Assistant

An intelligent agricultural chatbot designed to help Kenyan farmers with farming advice, pest control, planting schedules, weather information, and market prices. Available through both web interface and WhatsApp.

## 🚀 Features

- **Multi-language Support**: English, Kiswahili, Kikuyu, and Luo
- **Agricultural Expertise**: Pest control, planting advice, weather info, market prices
- **Dual Interface**: Web chat and WhatsApp integration
- **Real-time Translation**: Automatic language detection and response translation
- **Chat History**: Session-based conversation tracking
- **Mobile Responsive**: Works on all devices

## 📁 Project Structure

```
farmer-ai-assistant/
├── app.py                  # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── README.md              # This file
├── core/                  # Core business logic
│   ├── __init__.py
│   ├── agri_knowledge.py  # Agricultural advice functions
│   ├── language_handler.py # Translation utilities
│   └── message_processor.py # Main message processing
├── integrations/          # External service integrations
│   ├── __init__.py
│   └── whatsapp_handler.py # WhatsApp/Twilio integration
├── web/                   # Web interface
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css  # Web styling
│   │   └── js/
│   │       └── script.js  # Frontend JavaScript
│   └── templates/
│       └── index.html     # Web interface template
└── utils/                 # Utility functions
    └── __init__.py
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- OpenAI API key
- Twilio account (for WhatsApp)
- Weather API key (optional)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd farmer-ai-assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   OPENAI_API_KEY=your-openai-api-key
   TWILIO_ACCOUNT_SID=your-twilio-sid
   TWILIO_AUTH_TOKEN=your-twilio-token
   WEATHER_API_KEY=your-weather-api-key
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Web Interface: `http://localhost:5000`
   - WhatsApp Webhook: `http://localhost:5000/whatsapp`

## 🌐 API Endpoints

### Web Interface
- `GET /` - Main chat interface
- `POST /chat` - Send message and get response
- `GET /history` - Get chat history
- `GET /health` - Health check

### WhatsApp Integration
- `POST /whatsapp` - Twilio webhook for WhatsApp messages

## 📱 WhatsApp Setup

1. **Create Twilio Account**
   - Sign up at [Twilio Console](https://console.twilio.com/)
   - Get Account SID and Auth Token

2. **Configure WhatsApp Sandbox**
   - Go to Twilio Console > Messaging > Try it out > Send a WhatsApp message
   - Follow setup instructions
   - Set webhook URL to: `https://your-domain.com/whatsapp`

3. **Test WhatsApp Integration**
   - Send "join <sandbox-keyword>" to your Twilio WhatsApp number
   - Start chatting with the bot

## 🤖 Usage Examples

### Web Interface
1. Open `http://localhost:5000`
2. Select your preferred language
3. Type farming questions like:
   - "What pests attack maize?"
   - "When should I plant beans?"
   - "What's the weather forecast?"

### WhatsApp
Send messages like:
- "Ni mdudu gani wanaoshambulia mahindi?" (Swahili)
- "When is the best time to plant tomatoes?"
- "Market prices for potatoes"

## 🧠 Agricultural Knowledge Base

The bot provides advice on:

- **Pest Control**: Identification, organic treatments, prevention
- **Planting Calendar**: Seasonal advice, crop recommendations
- **Weather Information**: Current conditions, farming suitability
- **Market Prices**: General pricing guidance
- **General Farming**: Sustainable practices, crop management

## 🌍 Supported Languages

- **English** (en)
- **Kiswahili** (sw)
- **Kikuyu** (ki)
- **Luo** (luo)

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask session secret | Yes |
| `OPENAI_API_KEY` | OpenAI API key for AI responses | Yes |
| `TWILIO_ACCOUNT_SID` | Twilio account identifier | For WhatsApp |
| `TWILIO_AUTH_TOKEN` | Twilio authentication token | For WhatsApp |
| `WEATHER_API_KEY` | OpenWeatherMap API key | Optional |

### Customization

- **Add new languages**: Update `config.py` and translation functions
- **Extend knowledge base**: Modify functions in `core/agri_knowledge.py`
- **Custom styling**: Edit `web/static/css/style.css`
- **Add new intents**: Update `classify_message_intent()` function

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

1. **Using Gunicorn**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Using Docker**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
   ```

3. **Cloud Platforms**
   - **Heroku**: Add `Procfile` with `web: gunicorn app:app`
   - **Railway**: Connect GitHub repo and deploy
   - **DigitalOcean**: Use App Platform with Python buildpack

## 🧪 Testing

### Manual Testing
1. Test web interface at `http://localhost:5000`
2. Test different languages and question types
3. Verify WhatsApp webhook with ngrok for local testing

### WhatsApp Local Testing
```bash
# Install ngrok
npm install -g ngrok

# Expose local server
ngrok http 5000

# Use ngrok URL as Twilio webhook
```
## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Contact: tommiespice@gmail.com

## 🙏 Acknowledgments

- OpenAI for GPT-3.5 Turbo API
- Twilio for WhatsApp Business API
- Google Translate for multi-language support
- Bootstrap for responsive UI components

## 📊 Roadmap

- [ ] Database integration for chat history
- [ ] Image recognition for pest identification
- [ ] SMS integration
- [ ] Farmer registration and profiles
- [ ] Crop calendar notifications
- [ ] Market price alerts
- [ ] Voice message support
- [ ] Offline mode capabilities
# Farmer-AI-Assistant
