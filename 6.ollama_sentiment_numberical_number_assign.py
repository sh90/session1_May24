#pip install ollama
import ollama
import pandas as pd

# Pandas is used to read csv,  excel files
data = pd.read_csv("sample_tweets_sentiment.csv")
# data = pd.read_excel("sample_tweets_sentiment.xlsx")
model = "gemma3:1b"  # Example AI models from Ollama llama2
list_of_tweets = data["tweet"].tolist()
for tweet in list_of_tweets:
        print(tweet)
        print("===================")
        response = ollama.generate(model=model, prompt=f"Can you analyze the sentiment the given tweet by assigning a score b/w 1 to 5. where 1 means very negative and 5 means very positive "
                                                       f"\n: {tweet}")
        print(response.response)
