import requests
from bs4 import BeautifulSoup
import csv

url = "https://dealsheaven.in/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    deal_cards = soup.find_all('div', class_='deatls-inner')
    
    with open('deals.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Title', 'Original Price', 'Special Price'])
        
        for deal_card in deal_cards:
            title = deal_card.find('h3').text.strip() if deal_card.find('h3') else "Title not found"
            
            price = deal_card.find('p', class_='price').text.strip() if deal_card.find('p', class_='price') else "Original Price not found"
            
            special_price = deal_card.find('p', class_='spacail-price').text.strip() if deal_card.find('p', class_='spacail-price') else "Special Price not found"
            
            writer.writerow([title, price, special_price])

    print("Data successfully saved to deals.csv")
else:
    print("Failed to retrieve the page")
