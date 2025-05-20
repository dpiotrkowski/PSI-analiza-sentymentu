## 𖦹 Echo wyborcze  
---
Aplikacja wykorzystuje dane tekstowe, pochodzące z wpisów użytkowników platform [Wykop](https://wykop.pl) i [Reddit](https://reddit.com). Umożliwia dobór tagów oraz subredditów, a następnie tworzy chmurę słów, analizę sentymentu i szuka asocjacji. Dane są pozyskiwane poprzez webscraping za pośrednictwem API powyższych serwisów.

Projekt powstał w ramach przedmiotu [Projektowania Systemów Informatycznych](https://github.com/karolinakuligowska/Projektowanie_systemow_informatycznych). 

```bash
git clone https://github.com/dpiotrkowski/PSI-analiza-sentymentu.git 
```

**Część I** *Reproducible Research*: 
- Kod źródłowy: [`analiza-sentymentu.ipynb`](https://github.com/dpiotrkowski/PSI-analiza-sentymentu/blob/main/analiza_sentymentu.ipynb)
- Dane tekstowe znajdują się w folderu
[`data/`](https://github.com/dpiotrkowski/PSI-analiza-sentymentu/blob/main/data/).
- [Raport](https://github.com/dpiotrkowski/PSI-analiza-sentymentu/blob/main/raport/analiza_sentymentu.html).

**Część II** Dokumentacja: 
- [Dokumentacja wymagań użytkownika](https://github.com/dpiotrkowski/PSI-analiza-sentymentu/blob/main/DOKUMENTACJA.md)
- [Dokumentacja scraperów](https://github.com/dpiotrkowski/PSI-analiza-sentymentu/blob/main/src/README.md).
- Wymagane biblioteki znajdują się w `pyproject.toml`.
