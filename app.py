from openai_service import get_completion_from_messages
from db import Conversation

conversation = Conversation()

def get_answer(message):
    conversation.add_user_message(message)
    response = get_completion_from_messages(conversation.get_messages(), temperature=1)
    conversation.add_assistant_response(response)
    return response

def start_conversation():
    conversation.start()
