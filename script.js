function sendMessage() {
    // Get the input message value
    const messageInput = document.getElementById('messageInput');
    const messageText = messageInput.value.trim();
    
    // If the message is not empty, send it
    if (messageText) {
        // Create a new message element
        const newMessage = document.createElement('div');
        newMessage.classList.add('message', 'outgoing');
        newMessage.innerHTML = `<strong>You:</strong> ${messageText}`;
        
        // Append the new message to the chat window (at the top)
        const messagesContainer = document.getElementById('messages');
        messagesContainer.insertBefore(newMessage, messagesContainer.firstChild);
        
        // Clear the input field
        messageInput.value = '';
    }
}
