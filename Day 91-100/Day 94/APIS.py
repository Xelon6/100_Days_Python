import os
import requests
from openai import OpenAI
from dotenv import load_dotenv


os.chdir(os.path.dirname(os.path.realpath(__file__)))

load_dotenv()

NEWS_API_KEY=os.getenv("NEWS_API")

OPEN_AI_KEY=os.getenv("OPEN_AI")
ORGANIZATION_ID=os.getenv("ORGANIZATION_ID")

client=OpenAI(
    api_key=OPEN_AI_KEY,
    organization=ORGANIZATION_ID
)


country="at"

url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"

result = requests.get(url,timeout=5)
data=result.json()


for i in range(5):
    url=(data["articles"][i]["url"])
    title=(data["articles"][i]["title"])

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Bitte fasse mir Folgenden News Artikel zusammen:{url}"}
        ]
        )
    summary=completion.choices[0].message.content
    
    print(url)
    print()
    print(title)
    print()
    print(summary)
    print()
    print("-" * 50)