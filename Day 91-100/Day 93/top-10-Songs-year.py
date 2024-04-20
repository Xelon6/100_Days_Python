import os
import requests
import json
from requests.auth import HTTPBasicAuth
from  dotenv import load_dotenv
import urllib
from flask import Flask,request

#CONST
app=Flask(__name__,static_folder="static")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv()

CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


#Funktionen

def url_encode(text):
    return urllib.parse.quote_plus(text)

def get_accessToken():
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type":"client_credentials"}
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    response = requests.post(url, data=data, auth=auth,timeout=5)

    return response.json()["access_token"]


def get_songs(access_Token,year,artist):
    url = " https://api.spotify.com/v1"
    headers= {"Authorization":f"Bearer {access_Token}"}
    if len(artist) > 0:
        artist=url_encode(f"artist:{artist}")
        artist=f"{artist}+"
    else:
        artist=""
    
    year=url_encode(f"year:{year}")
    search = f"/search?q={artist}{year}&type=track&market=AT&limit=10"


    full_url=f"{url}{search}"

    response=requests.get(full_url,headers=headers,timeout=5)
    return  response.json()



def read_template(template):
    with open(f"template/{template}.html","r",encoding="UTF-8") as f:
        return f.read()


#Websites


@app.route("/",methods=["GET"])
def index():
    AccessToken=get_accessToken()
    page=read_template("index")
    try:
        artist=request.args.get('artist').lower()
        year=request.args.get('year').lower()
        tracks = get_songs(AccessToken,year,artist)
        
        for track in tracks["tracks"]["items"]:
            song_name=track["name"]
            url=track["preview_url"]
            artist_name=track["artists"][0]["name"]
            release_date=track["album"]["release_date"]
            page +=f"""<div class="songs">
            <h2>Song Title: {song_name}</h2>
            <h3>Artist: {artist_name}</h3>
            <p>Release Date: {release_date}</p>
            <audio controls>
                <source src="{url}" type="audio/mpeg">
            </audio>
            <br>
            </div>
            
            """
    except Exception as e:
        print(e)


    
    return page

app.run("0.0.0.0",port=81)

