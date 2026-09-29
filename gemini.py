from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Gemini Chatbot Started!")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Gemini: Goodbye! 👋")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question
    )

    print("Gemini:", response.text)