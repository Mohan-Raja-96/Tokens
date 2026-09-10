from openai import OpenAI
import tiktoken
import os

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

prompt = "Tell me a story about a puppy who learns to fly."

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

tokens = encoding.encode(prompt)

print("🔢 Number of tokens:", len(tokens))
print("🧩 Tokens:", tokens[:10])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

print("\n🤖 Chatbot says:")
print(response.choices[0].message.content)
