import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

os.chdir(os.path.dirname(os.path.realpath(__file__)))

load_dotenv()
#News API
NEWS_API_KEY=os.getenv("NEWS_API")

#Open AI API
OPEN_AI_KEY=os.getenv("OPEN_AI")
ORGANIZATION_ID=os.getenv("ORGANIZATION_ID")

client=OpenAI(
    api_key=OPEN_AI_KEY,
    organization=ORGANIZATION_ID
)

#Spotify API
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv('CLIENT_SECRET')




def get_news():
    country="at"

    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"

    result = requests.get(url,timeout=5)
    return result.json()

def url_encode(text):
    import urllib
    return urllib.parse.quote_plus(text)

def get_accessToken():
    url = "https://accounts.spotify.com/api/token"
    header = {"grant_type":"client_credentials"}
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    response = requests.post(url, data=header, auth=auth,timeout=5)

    return response.json()["access_token"]


def get_songs(access_Token,search):
    url = " https://api.spotify.com/v1"
    headers= {"Authorization":f"Bearer {access_Token}"}

    
    search = f"/search?q={search}&type=track&market=AT&limit=1"


    full_url=f"{url}{search}"

    response=requests.get(full_url,headers=headers,timeout=5)
    return  response.json()


data = get_news()

for i in range(5):
    link=(data["articles"][i]["url"])
    title=(data["articles"][i]["title"])

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Summarize the following News Article in 2-3 Words:{link}"}
        ]
        )
    summary=completion.choices[0].message.content
    tracks = get_songs(get_accessToken(),summary)
    song_sample=tracks["tracks"]["items"][0]["preview_url"]
    song_name=tracks["tracks"]["items"][0]["name"]
    
    
    print(f"Based on the following News Article:{title}\nWith these Keywords: {summary}\nI have found this Track:{song_name}\n{song_sample}\n")

    print("-" * 50)