from dotenv import load_dotenv
import os
from wykop_sdk_reloaded.v3.client import AuthClient, WykopApiClient
from wykop_sdk_reloaded.v3.types import StreamSortType
import sys 

# Ładowanie zmiennych środowiskowych
load_dotenv()

wykop_app_key = os.getenv("WYKOP_APP_KEY")
wykop_app_secret = os.getenv("WYKOP_APP_SECRET")

auth = AuthClient()
auth.authenticate_app(wykop_app_key, wykop_app_secret)

client = WykopApiClient(auth)

# Sprawdzenie, czy podano tagi
if len(sys.argv) < 2:
    print("Proszę podać tagi jako argumenty.")
    exit()

# Pobieranie tagów z argumentów
wykop_tags = sys.argv[1].split(',')

# Pobieranie ARTYKUŁÓW z tagiem
with open("../data/results_wykop.txt", "w", encoding="utf-8") as f:
    for tag in wykop_tags:
        tag = tag.strip() # Usunięcie białych znaków
        try:
            result = client.articles_list_articles_by_tag(  
                tag=tag,
                sort=StreamSortType.ALL,
                limit=300
            )
        except Exception as e:
            print(f"Błąd pobierania danych dla tagu '{tag}': {e}")
            exit()

        if not result.get('data'):
            print(f"Brak artykułów dla tagu {tag}\n")
            continue 
            
        for article in result['data']:
            try:
                content = article.get('content')
                
                if content and content != 'None':
                    f.write(
                        f"#{tag}\n"
                        f"{content}\n"
                        f"{'-'*50}\n\n"
                    )
            except Exception as e:
                print(f"Błąd przetwarzania artykułu: {e}")
                continue

