import requests
from bs4 import BeautifulSoup
import pandas as pd

user_login = '289099'

def collect_user_rates(user_login):
    page_num = 1

    data = []

    while True:
        url = f'https://www.russianfood.com/blogs/?id={user_login}&page={page_num}'

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'lxml')

        entries = soup.find_all('div', class_='annonce annonce_orange')

        if len(entries) == 0:
            break

        for entry in entries:
            food_details = entry.find('td', class_='tc22')
            food_name = food_details.find('a').text
            release_date = entry.find('td', class_='data date').text
            data.append({'food_name': food_name, 'release_date': release_date})

        page_num += 1

    return data

user_rates = collect_user_rates(user_login='289099')
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')