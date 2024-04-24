import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

os.chdir(os.path.dirname(os.path.realpath(__file__)))

load_dotenv()

#Open AI Init
OPEN_AI_KEY=os.getenv("OPEN_AI")
ORGANIZATION_ID=os.getenv("ORGANIZATION_ID")
client=OpenAI(
    api_key=OPEN_AI_KEY,
    organization=ORGANIZATION_ID
)

#get wiki page
url = input("PLease Enter the link of the Wiki Article\n> ")

result=requests.get(url,timeout=5)

html=result.text


#get text from site with Beautiful Soup

soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup.find_all("p")
references = soup.find("ol", {"class": "references"}).find_all("li") if soup.find("ol", {"class": "references"}) else []

paragraph_text = [p.get_text() for p in paragraphs]

reference_text = [ref.get_text() for ref in references]

input_prompt = "Bitte fasse folgenden Wiki Artikel in 2-3 Paragraphen zusammen und zähle die Verweise am Ende Übersichtlich hinzu:\n\n"
for paragraph in paragraph_text:
    input_prompt += paragraph + "\n\n"

input_prompt += "Verweise:\n"
for reference in reference_text:
    input_prompt += reference + "\n"

# Requesting summary from OpenAI
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input_prompt}
    ]
)
summary = completion.choices[0].message.content

print(summary)