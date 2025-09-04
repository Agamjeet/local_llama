from ollama import chat
from ollama import ChatResponse

def chat(model='llama3.2:latest', messages=None, images=None):
    """
    Chat with Llama model
    
    Args:
        model (str): Model name to use
        messages (list): List of message dictionaries with 'role' and 'content'
        images (list): Optional list of image data for vision models
    
    Returns:
        ChatResponse: Response from the model
    """
    if messages is None:
        messages = []
    
    # Prepare the message structure
    chat_messages = []
    for message in messages:
        msg = {
            'role': message['role'],
            'content': message['content']
        }
        if images and 'images' in message:
            msg['images'] = message['images']
        elif images:
            msg['images'] = images
        chat_messages.append(msg)
    
    # Make the API call
    response = chat(model=model, messages=chat_messages)
    return response

# Example usage (commented out for production)
# response = chat(model='llama3.2:latest', messages=[
#     {
#         'role': 'user',
#         'content': 'Why is the sky blue?',
#     },
# ])
# print(response.message.content)
