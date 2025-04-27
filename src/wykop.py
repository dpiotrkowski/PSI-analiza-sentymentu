from dotenv import load_dotenv
import os
from wykop_sdk_reloaded.v3.client import AuthClient, WykopApiClient
from wykop_sdk_reloaded.v3.types import StreamSortType

# Ładowanie zmiennych środowiskowych
load_dotenv()

wykop_app_key = os.getenv("WYKOP_APP_KEY")
wykop_app_secret = os.getenv("WYKOP_APP_SECRET")

auth = AuthClient()
auth.authenticate_app(wykop_app_key, wykop_app_secret)

client = WykopApiClient(auth)

# Pobieranie ARTYKUŁÓW z tagiem
try:
    result = client.articles_list_articles_by_tag(  
        tag='wybory',
        sort=StreamSortType.ALL,
        limit=100
    )
except Exception as e:
    print(f"Błąd pobierania danych: {e}")
    exit()

with open("data/results_wykop.txt", "w", encoding="utf-8") as f:
    if not result.get('data'):
        f.write("Brak artykułów do wyświetlenia")
        exit()
        
    for article in result['data']:
        try:
            content = article.get('content', 'BRAK TREŚCI')
            
            f.write(
                f"Treść: {content}\n"
                f"{'-'*50}\n\n"
            )
        except Exception as e:
            print(f"Błąd przetwarzania artykułu: {e}")
            continue

