from openai import OpenAI
import data_info
import pandas as pd

client = OpenAI(api_key=data_info.open_ai_key)

# Pandas is used to read csv,  excel files
data = pd.read_csv("sample_tweets_sentiment.csv")

results = []
list_of_tweets = data["tweet"].tolist()
for tweet in list_of_tweets:
        print(tweet)
        response = client.responses.create(
            model="gpt-4o-mini",
            input= f"Can you analyze the sentiment the given tweet by assigning a score b/w 1 to 5. where 1 means very negative and 5 means very positive "
                                                       f"\n: {tweet}"
        )
        print(response.output_text)
        results.append(response.output_text)

result_csv = pd.DataFrame(results)
result_csv.to_csv("sample_tweets_sentiment_result.csv")
