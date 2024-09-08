class Conversation:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "Eres una asistente que habla como Shakespeare.",
            },
        ]

    def get_messages(self):
        return self.messages

    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})

    
    def add_assistant_response(self, message):
        self.messages.append({"role": "assistant", "content": message})
