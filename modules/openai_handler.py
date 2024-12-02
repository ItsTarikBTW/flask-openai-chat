from openai import OpenAI
import os

class OpenAIHandler:
    def __init__(self):
        self.client = None
        self.conversation = []
        
    def initialize(self, api_key):
        self.client = OpenAI(api_key=api_key)
        
    def get_stream_response(self, message):
        if not self.client:
            raise Exception("OpenAI client not initialized")

        # Add user message to conversation
        self.conversation.append({"role": "user", "content": message})
            
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.conversation,  # Pass full conversation history
            stream=True
        )

        # Add empty assistant message placeholder
        self.conversation.append({"role": "assistant", "content": ""})
        last_msg_index = len(self.conversation) - 1

        # Create a new generator that updates conversation
        def stream_and_save():
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    # Update the last assistant message
                    self.conversation[last_msg_index]["content"] += content
                yield chunk

        return stream_and_save()