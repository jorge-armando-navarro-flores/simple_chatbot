from openai_service import get_completion_from_messages
from db import context

def get_answer(messages):
    response = get_completion_from_messages(messages, temperature=1)
    return response

def get_context():
    return context
