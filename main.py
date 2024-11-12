import requests
from bs4 import BeautifulSoup

url = "https://dealsheaven.in/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    deal_cards = soup.find_all('div', class_='deatls-inner')
    
    for deal_card in deal_cards:
        title = deal_card.find('h3').text.strip() if deal_card.find('h3') else "Title not found"
        
        price = deal_card.find('p', class_='price').text.strip() if deal_card.find('p', class_='price') else "Original Price not found"
        
        special_price = deal_card.find('p', class_='spacail-price').text.strip() if deal_card.find('p', class_='spacail-price') else "Special Price not found"
        
        print(f"Title: {title}")
        print(f"Original Price: {price}")
        print(f"Special Price: {special_price}")
        print("---------------")
else:
    print("Failed to retrieve the page")
