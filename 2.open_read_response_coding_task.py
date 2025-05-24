from openai import OpenAI
import data_info
client = OpenAI(api_key=data_info.open_ai_key)

task = ["Generate code in python to call chatgpt"]
response = client.responses.create(
    model="gpt-4o-mini",
    input=task[0]
)

print(response.output_text)
