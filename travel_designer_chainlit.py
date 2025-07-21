import google.generativeai as genai
import chainlit as cl

genai.configure(api_key="GEMINI_API_KEY")

class OpenAIWrapper:
    @staticmethod
    def chat(model, prompt):
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text

@cl.on_message
async def main(message: cl.Message):
    mood = message.content  # ✅ Extract the actual text typed by the user
    prompt = f"""
    Suggest 3 travel destinations for a person in {mood} mood.
    Pick the best one and give flight and hotel options.
    Finally, list top attractions and famous food in that destination.
    """
    response = OpenAIWrapper.chat("gemini-1.5-flash", prompt)
    await cl.Message(content=response).send()
