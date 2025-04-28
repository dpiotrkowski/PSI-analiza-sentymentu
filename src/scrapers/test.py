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

# Iteracja przez tagi i pobieranie artykułów
for tag in wykop_tags:
    tag = tag.strip()  # Usunięcie białych znaków
    try:
        result = client.articles_list_articles_by_tag(  
            tag=tag,
            sort=StreamSortType.ALL,
            limit=100
        )
    except Exception as e:
        print(f"Błąd pobierania danych dla tagu '{tag}': {e}")
        continue

    with open("data/results_wykop.txt", "a", encoding="utf-8") as f:  # Append mode
        if not result.get('data'):
            f.write(f"Brak artykułów do wyświetlenia dla tagu '{tag}'\n")
            continue
            
        for article in result['data']:
            try:
                content = article.get('content', 'BRAK TREŚCI')
                
                f.write(
                    f"Tag: {tag}\n"
                    f"Treść: {content}\n"
                    f"{'-'*50}\n\n"
                )
            except Exception as e:
                print(f"Błąd przetwarzania artykułu: {e}")
                continue

