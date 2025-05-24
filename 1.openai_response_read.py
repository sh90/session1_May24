# pip install openai
from openai import OpenAI
import data_info


task = """Write a 50 word summary on ethics in AI."""

# Call openai
client = OpenAI(api_key=data_info.open_ai_key)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": task},
    ]
)

# Read the response
print(completion.response)
print(completion.choices[0].message.content)
