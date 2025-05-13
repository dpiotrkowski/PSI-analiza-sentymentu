from dotenv import load_dotenv
import os
import praw
import sys

# Inicjalizacja zmiennych środowiskowych z pliku .env
load_dotenv()

# Pobranie kluczy ze zmiennych środowiskowych .env
# WAŻNE: Upewnić się, że .env znajduje się w .gitignore
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")

# Krok 1: AUTORYZACJA
## REDDIT: Inicjalizacja PRAW z danymi logowania z Reddita
## https://github.com/praw-dev/praw
## Docs: https://praw.readthedocs.io/en/stable/index.html
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=user_agent,
)
# Krok 2: WYBÓR DANYCH
if len(sys.argv) < 2:
    sys.exit(1)

subreddits = sys.argv[1].split(",")  # Pobranie subredditów z argumentów
search_words = sys.argv[2].split(",")  # Pobranie słów do wyszukiwania z argumentów

# Krok 3: ZAPIS WYNIKÓW do txt
os.makedirs("../data", exist_ok=True)
with open("../data/results_reddit.txt", "w", encoding="utf-8") as reddit_file:
    for subreddit_name in subreddits:
        subreddit_name = subreddit_name.strip()
        subreddit = reddit.subreddit(subreddit_name)

        reddit_file.write(f"Subreddit: {subreddit_name}\n")

        for submission in subreddit.search(search_words, sort="new", limit=100):
            reddit_file.write(f"Tytuł: {submission.title}\n")
            # reddit_file.write(f"Wynik: {submission.score}\n")  # opcjonalne
            # reddit_file.write(f"URL: {submission.url}\n")  # opcjonalne
            # OPCJONALNE: Timestampy mogą się przydać do analizy sentymentu w czasie
            # reddit_file.write(f"Utworzono: {submission.created_utc}\n")
            reddit_file.write(f"Treść: {submission.selftext}\n\n")

        reddit_file.write("\n" + "-" * 50 + "\n\n")  # Separator między subreddits
