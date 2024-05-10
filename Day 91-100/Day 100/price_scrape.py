import requests
from bs4 import BeautifulSoup




url_billa="https://shop.billa.at/produkte/ja-natuerlich-kaisersemmel-00480904"
url_hofer="https://www.hofer.at/de/p.backbox-kaisersemmel.000000000000100932.html"


def get_billa_price(url):
    
    result=requests.get(url,timeout=5)
    html=result.text

    soup = BeautifulSoup(html, 'html.parser')

    price_elements = soup.find("div", {"class": "ws-product-price-type__value h3"})
    if price_elements:

        price_text = price_elements.text.strip()
        price_num = price_text.split()[0]
        price = float(price_num.replace(",", "."))

        return price
    else:
        print("Preis nicht gefunden.")

def get_hofer_price(url):
    result=requests.get(url,timeout=5)
    html=result.text

    soup = BeautifulSoup(html, 'html.parser')

    price_element = soup.find_all("span", {"class": "pdp_price__now at-productprice_lbl"})

    if price_element:
        for price in price_element:
            price_text=float(price.get("data-price"))
            return price_text
    else:
        print("Preis nicht gefunden.")

#spar cloudflare bypass
#lidl keine Preis angabe
#penny keine Preis angabe

prices={}

prices["semmel"]={"Billa":get_billa_price(url_billa),"Spar":get_hofer_price(url_hofer)}

try:
    if prices["semmel"]["Billa"] > prices["semmel"]["Spar"]:
        diff = prices["semmel"]["Billa"]-prices["semmel"]["Spar"]
        print(f"Spar Billiger um: {diff:.2f}€")
    else:
        diff=prices["semmel"]["Spar"]-prices["semmel"]["Billa"]
        print(f"Billa Billiger um:{diff:.2f}€")
except Exception as e:
    print("error e")