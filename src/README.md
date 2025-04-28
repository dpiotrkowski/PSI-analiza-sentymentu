## Disclaimer
> [!WARNING]  
> **Uwaga:** Prosimy o przestrzeganie zasad korzystania z danych platform oraz o zapoznanie się z dokumentacją API przed rozpoczęciem scrapowania. Niektóre platformy mogą pobierać opłaty za korzystanie z API. Oto linki do dokumentacji:

- [Wykop APIv3 dla programistów](https://wykop.pl/dla-programistow)
- [Reddit API Documentation](https://developers.reddit.com/docs/api)
- [X API Documentation](https://developer.x.com/en/docs/x-api)

Prosimy również o zapoznanie się z dokumentacją następujących bibliotek:
- [PRAW: The Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/)
- [Wykop SDK Reloaded](https://lukas346.github.io/wykop_sdk_reloaded/)

## Wymagania
- Konta na platformach Wykop, Reddit i X (potrzebne do uzyskania kluczy dostępu do API).
- `python>=3.13.2`
- Biblioteki z `pyproject.toml`. Można to zrobić za pomocą swojego ulubionego menedżera np. [`uv`](https://github.com/astral-sh/uv), [`poetry`](https://github.com/python-poetry/poetry) lub za pomocą `pip`. 
## Ustawienie środowiska
Stworzenie pliku `.env` ze zmiennymi środowiskowymi. 
```bash
# Ustawienia dla Reddita
# https://praw.readthedocs.io/en/stable/getting_started/authentication.html
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
USER_AGENT=

# Ustawienia dla Wykop
# https://lukas346.github.io/wykop_sdk_reloaded/readme.html#instalacja
WYKOP_APP_KEY=
WYKOP_APP_SECRET=
```
## Zautomatyzowany webscraping danych
Folder `src/` zawiera skrypty do zbierania danych z różnych źródeł, w tym Wykopa, Reddita i X. Umożliwia łatwe uruchamianie skryptów za pomocą jednego pliku `main.py`, do którego przekazywane są argumenty ze skryptów `wykop.py`, `reddit.py` i `x.py`. W ten sposób użytkownik nie musi manualnie uruchamiać skryptów z folderu `scrapers/`.
```bash 
python run main.py wykop
python run main.py reddit
python run main.py x
```
Otrzymane dane tekstowe znajdują się w folderze `data/`.  



