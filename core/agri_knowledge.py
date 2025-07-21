import openai
from datetime import datetime
import requests
import os
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def get_agricultural_advice(message):
    """Get comprehensive agricultural advice"""
    intent = classify_message_intent(message)
    
    if intent == 'pest_control':
        return get_pest_advice(message)
    elif intent == 'planting_advice':
        return get_planting_advice(message)
    elif intent == 'weather_info':
        return get_weather_info()
    elif intent == 'market_prices':
        return get_market_info(message)
    else:
        return get_general_farming_advice(message)

def classify_message_intent(message):
    """Classify the farmer's message intent"""
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['pest', 'insect', 'bug', 'disease', 'mdudu']):
        return 'pest_control'
    elif any(word in message_lower for word in ['plant', 'grow', 'when', 'season', 'panda']):
        return 'planting_advice'
    elif any(word in message_lower for word in ['weather', 'rain', 'mvua']):
        return 'weather_info'
    elif any(word in message_lower for word in ['price', 'market', 'sell', 'bei']):
        return 'market_prices'
    else:
        return 'general_advice'

def get_pest_advice(message):
    """Get pest control advice"""
    prompt = f"""
    You are an agricultural expert in Kenya. A farmer asks: "{message}"
    
    Provide practical pest control advice including:
    - Identification tips
    - Organic/affordable treatments
    - Prevention methods
    - Local solutions available in Kenya
    
    Keep response concise but helpful (max 200 words).
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except:
        return "For pest control, try neem oil spray or soap solution. Check leaves regularly and remove affected parts. Consult your local agricultural officer for specific treatments."

def get_planting_advice(message):
    """Get planting calendar advice"""
    current_month = datetime.now().month
    
    # Kenya planting seasons
    if current_month in [3, 4, 5]:  # Long rains
        season = "long rains season"
        crops = "maize, beans, potatoes, tomatoes"
        advice = "Good time for main crops. Ensure proper spacing and fertilizer application."
    elif current_month in [10, 11, 12]:  # Short rains
        season = "short rains season" 
        crops = "vegetables, legumes, quick-maturing varieties"
        advice = "Plant drought-resistant varieties. Consider irrigation backup."
    else:
        season = "dry season"
        crops = "irrigation crops only (kale, spinach, onions)"
        advice = "Focus on water-efficient crops and mulching."
    
    return f"Current {season}. Best crops: {crops}. {advice} Check local weather before planting."

def get_weather_info(location="Nairobi"):
    """Get weather forecast"""
    api_key = Config.WEATHER_API_KEY
    if not api_key:
        return "Weather service unavailable. Check local weather reports."
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp'] - 273.15  # Convert to Celsius
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        return f"Weather: {weather}, {temp:.1f}°C, Humidity: {humidity}%. Good for farming activities."
    except:
        return "Weather info unavailable. Check local weather reports before farming activities."

def get_market_info(message):
    """Get market price information"""
    return "Market prices vary by location. Check with your local market or agricultural cooperative for current prices. Consider value addition to increase profits."

def get_general_farming_advice(message):
    """Get general farming advice"""
    prompt = f"""
    You are an expert agricultural advisor for Kenyan farmers. 
    Farmer's question: "{message}"
    
    Provide practical, actionable advice considering:
    - Local Kenyan farming conditions
    - Affordable solutions for small-scale farmers
    - Seasonal considerations
    - Common crops: maize, beans, potatoes, tomatoes, kale
    - Sustainable farming practices
    
    Keep response concise but helpful (max 200 words).
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except:
        return "I'm having trouble processing your request. Please try asking about specific crops, pests, or farming practices. You can also contact your local agricultural extension officer."