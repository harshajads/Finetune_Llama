import openai
import os

# Replace with your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

try:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello in one sentence."}
        ],
        max_tokens=20  # small response
    )

    # Print the assistant's reply
    print("✅ API key works! Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ API key failed:", e)
