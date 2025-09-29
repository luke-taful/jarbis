from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
gemmaToken = str(os.getenv("GEMMA_TOKEN"))

system_prompt = "You are a virtual assistant, based off Jarvis from Iron man, but with an attitude. Your name is Jarbis. Interact casually and informatively with the users of the channel. Keep all responses to 50 words or less, and always be as brief as possible."
user_prompt = str(input())

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=gemmaToken
)

completion = client.chat.completions.create(
    model="google/gemma-3n-e4b-it",
    messages=[
        {"role": "user", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    temperature=1.5,
    top_p=0.7,
    frequency_penalty=1,
    max_tokens=100,
)

response = completion.choices[0].message.content
print(f"'{user_prompt}'")
print(f"Assistant: {response}")