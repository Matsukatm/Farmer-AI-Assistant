from twilio.twiml.messaging_response import MessagingResponse
from core.message_processor import process_farmer_message

def handle_whatsapp_message(request):
    """Handle incoming WhatsApp messages"""
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From')
    
    # Handle greeting messages
    if incoming_msg.lower() in ['hi', 'hello', 'habari', 'mambo']:
        response_text = "Habari! 🌱 I'm your farming assistant. Ask me about:\n• Pest control (mdudu)\n• Planting advice (panda)\n• Weather (hali ya hewa)\n• Market prices (bei)"
    else:
        # Process the message with auto language detection
        response_text = process_farmer_message(incoming_msg, 'auto')
    
    # Create Twilio response
    resp = MessagingResponse()
    resp.message(response_text)
    
    return str(resp)

def send_whatsapp_message(to_number, message):
    """Send outbound WhatsApp message (for notifications)"""
    from twilio.rest import Client
    from config import Config
    
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
    
    try:
        message = client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',  # Twilio sandbox number
            to=f'whatsapp:{to_number}'
        )
        return message.sid
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return None
