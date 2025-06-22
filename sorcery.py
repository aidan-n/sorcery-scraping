import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = "https://curiosa.io/decks/cmbcn15x3003cl704euvw894m"

response = session.get(url)

# load url from DevTools
url = 'https://curiosa.io/api/trpc/deck.getDecklistById,deck.getAvatarById,deck.getSideboardById,deck.getMaybeboardById?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22id%22%3A%22cmbcn15x3003cl704euvw894m%22%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22id%22%3A%22cmbcn15x3003cl704euvw894m%22%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22id%22%3A%22cmbcn15x3003cl704euvw894m%22%7D%7D%2C%223%22%3A%7B%22json%22%3A%7B%22id%22%3A%22cmbcn15x3003cl704euvw894m%22%7D%7D%7D'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://curiosa.io/decks/cmbcn15x3003cl704euvw894m",
    "content-type": "application/json",
    "x-build-id": "f7b49bf06ceefe470ea1bd27506c319176a942f8",
    "x-trpc-source": "nextjs-react",
}

response = session.get(url, headers=headers)

data = response.json()

for item in data:

    item = item['result']['data']['json']

    # sometimes it is a single dictionary instead of a list of dictionaries
    if isinstance(item, dict):
        item = [item]

    for element in item:
        quantity = element['quantity']
        name  = element['card']['name']
        type_ = element['card']['guardian']['type']
        print(f"({quantity}) {name} ({type_})")
    print()
