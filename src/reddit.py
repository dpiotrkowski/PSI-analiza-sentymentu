from dotenv import load_dotenv
import os
import praw

# Inicjalizacja zmiennych środowiskowych z pliku .env
load_dotenv()

# Pobranie kluczy ze zmiennych środowiskowych .env
# WAŻNE: Upewnić się, że .env znajduje się w .gitignore
reddit_client_id = os.getenv('REDDIT_CLIENT_ID')
reddit_client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

# Krok 1: AUTORYZACJA
## REDDIT: Inicjalizacja PRAW z danymi logowania z Reddita
## https://github.com/praw-dev/praw
## Docs: https://praw.readthedocs.io/en/stable/index.html
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=user_agent
)
# Krok 2: WYBÓR DANYCH
## REDDIT: Wybór subreddita r/Polska
subreddit = reddit.subreddit('Polska')

# Krok 3: ZAPIS WYNIKÓW do txt
os.makedirs('data', exist_ok=True)
## REDDIT: Zapis wyników z Reddita do pliku
with open('data/results_reddit.txt', 'w', encoding='utf-8') as reddit_file:
    # Przeszukiwanie postów, zawierających frazę "wybory"
    for submission in subreddit.search('wybory', sort='new', limit=10):
        reddit_file.write(f"Tytuł: {submission.title}\n")
        reddit_file.write(f"Wynik: {submission.score}\n")
        reddit_file.write(f"URL: {submission.url}\n")
        reddit_file.write(f"Utworzono: {submission.created_utc}\n")
        reddit_file.write(f"Treść: {submission.selftext}\n\n")

