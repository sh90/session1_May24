import ollama
import pandas as pd

data = pd.read_csv("sample_tweets_sentiment.csv")
model = "gemma3:1b"  # Example AI models from Ollama llama2
list_of_tweets = data["tweet"].tolist()
for tweet in list_of_tweets:
        print(type(tweet))
        response = ollama.generate(model=model, prompt=f"Can you analyze the sentiment the given tweet \n: {tweet}")
        print(response.response)
