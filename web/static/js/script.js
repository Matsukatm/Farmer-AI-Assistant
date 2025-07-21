let isLoading = false;

function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    
    if (!message || isLoading) return;
    
    const language = document.getElementById('language').value;
    
    // Add user message to chat
    addMessage(message, 'user');
    input.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    isLoading = true;
    
    // Send to backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: message,
            language: language
        })
    })
    .then(response => response.json())
    .then(data => {
        hideTypingIndicator();
        addMessage(data.response, 'bot');
        isLoading = false;
    })
    .catch(error => {
        hideTypingIndicator();
        addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        isLoading = false;
        console.error('Error:', error);
    });
}

function addMessage(message, sender) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const content = sender === 'user' ? 
        `<div class="message-content">${escapeHtml(message)}</div>` :
        `<div class="message-content"><strong>🤖 Farm Assistant:</strong><br>${escapeHtml(message)}</div>`;
    
    messageDiv.innerHTML = content;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function showTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.id = 'typingIndicator';
    indicator.className = 'typing-indicator';
    indicator.innerHTML = '🤖 Farm Assistant is typing';
    document.getElementById('chatMessages').appendChild(indicator);
    indicator.style.display = 'block';
    document.getElementById('chatMessages').scrollTop = document.getElementById('chatMessages').scrollHeight;
}

function hideTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

function askQuestion(question) {
    document.getElementById('messageInput').value = question;
    sendMessage();
}

function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

// Load chat history on page load
window.onload = function() {
    fetch('/history')
        .then(response => response.json())
        .then(history => {
            history.forEach(chat => {
                addMessage(chat.user, 'user');
                addMessage(chat.bot, 'bot');
            });
        })
        .catch(error => {
            console.log('No previous chat history');
        });
    
    // Focus on input
    document.getElementById('messageInput').focus();
};

// Add some sample questions based on language
function updateQuickQuestions() {
    const language = document.getElementById('language').value;
    const questionsContainer = document.querySelector('.quick-questions');
    
    let questions = [];
    
    switch(language) {
        case 'sw':
            questions = [
                { text: 'Ni wadudu gani wanaoshambulia mahindi?', display: '🐛 Mdudu wa Mahindi' },
                { text: 'Ni wakati gani mzuri wa kupanda maharage?', display: '📅 Kupanda Maharage' },
                { text: 'Hali ya hewa itakuwaje?', display: '🌤️ Hali ya Hewa' },
                { text: 'Bei za nyanya sokoni?', display: '💰 Bei za Nyanya' }
            ];
            break;
        default:
            questions = [
                { text: 'What pests are common in maize?', display: '🐛 Pest Control' },
                { text: 'When should I plant beans?', display: '📅 Planting Calendar' },
                { text: 'What is the weather forecast?', display: '🌤️ Weather Info' },
                { text: 'Market prices for tomatoes', display: '💰 Market Prices' }
            ];
    }
    
    // Update buttons (simplified - you can enhance this)
    const buttons = questionsContainer.querySelectorAll('button');
    buttons.forEach((button, index) => {
        if (questions[index]) {
            button.onclick = () => askQuestion(questions[index].text);
            button.innerHTML = questions[index].display;
        }
    });
}

// Update questions when language changes
document.getElementById('language').addEventListener('change', updateQuickQuestions);