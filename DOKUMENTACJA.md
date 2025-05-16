## Dokumentacja specyfikacji wymagań 
Zawartość dokumentacji projektowej w formie Dokumentacji SRS:
### Wprowadzenie 
- **Opis aplikacji:** Aplikacja ma na celu analizę sentymentu oraz asocjacji słów w kontekście wyborów prezydenckich na platformach Reddit i Wykop.
- **Znaczenie analizy:** W dobie rosnącej roli mediów społecznościowych w kształtowaniu opinii publicznej, analiza sentymentu może dostarczyć cennych informacji na temat nastrojów wyborców.
- **Zakres projektu:** Aplikacja będzie zbierać dane, przetwarzać je, a następnie wizualizować wyniki w formie chmury słów oraz analizować asocjacje między słowami.

### Cele systemu 
1. **Zbieranie danych:** Automatyczne pobieranie danych z platform Reddit i Wykop w kontekście wyborów prezydenckich.
2. **Analiza sentymentu:** Klasyfikacja postów i komentarzy jako pozytywne, negatywne lub neutralne.
3. **Wizualizacja danych:** Tworzenie chmury słów oraz wykresów ilustrujących wyniki analizy sentymentu i asocjacji.
4. **Umożliwienie użytkownikom:** Użytkownikom łatwego dostępu do wyników analizy oraz możliwości dostosowania parametrów zbierania danych.

### Wymagania funkcjonalne  
1. **Scraping danych:**
   - Aplikacja powinna być w stanie pobierać dane z wybranych subreddits na Reddit oraz z odpowiednich tagów lub kategorii na Wykop.
   - Użytkownik powinien mieć możliwość określenia zakresu czasowego oraz liczby postów do pobrania.
   - Zebrane dane powinny obejmować treść postów, komentarze oraz metadane (np. liczba głosów, daty publikacji).
2. **Przetwarzanie danych:**
   - Aplikacja powinna oczyszczać zebrane dane z niepotrzebnych znaków, linków oraz emotikon.
   - Powinna być możliwość usunięcia stop-słów (ang. stop words) oraz normalizacji tekstu (np. konwersja do małych liter).
3. **Tworzenie chmury słów:**
   - Aplikacja powinna generować chmurę słów na podstawie przetworzonych danych, z możliwością dostosowania parametrów (np. minimalna liczba wystąpień słowa).
   - Użytkownik powinien mieć możliwość wizualizacji chmury słów w formie graficznej.
4. **Analiza sentymentu:**
   - Aplikacja powinna przeprowadzać analizę sentymentu na podstawie zebranych danych, klasyfikując je jako pozytywne, negatywne lub neutralne.
   - Powinna być możliwość wizualizacji wyników analizy sentymentu (np. wykresy, tabele).
5. **Analiza asocjacji:**
   - Aplikacja powinna identyfikować asocjacje między słowami, np. za pomocą algorytmu Apriori lub podobnych.
   - Użytkownik powinien mieć możliwość przeglądania wyników analizy asocjacji w formie tabeli lub wykresu.
### Wymagania niefunkcjonalne
1. **Wydajność:**
   - Aplikacja powinna być zoptymalizowana pod kątem wydajności, aby szybko przetwarzać duże zbiory danych.
2. **Interfejs użytkownika:**
   - Aplikacja powinna być przyjazna dla użytkownika, z dobrze zorganizowanym kodem i komentarzami.
   - Powinna zawierać instrukcje dotyczące uruchamiania poszczególnych sekcji oraz interpretacji wyników.
3. **Zależności:**
   - Aplikacja powinna zawierać listę wymaganych bibliotek i pakietów (np. `pandas`, `numpy`, `matplotlib`, `nltk`, `wordcloud`, `requests`, `BeautifulSoup`, `scikit-learn` itp.) oraz instrukcje dotyczące ich instalacji.
4. **Dokumentacja:**
   - Aplikacja powinna być dobrze udokumentowana, z opisem funkcji, parametrów oraz przykładami użycia.
5. **Zgodność z regulacjami:**
   - Aplikacja powinna przestrzegać regulacji dotyczących scrapingu danych oraz polityki prywatności platform Reddit i Wykop.
### Interfejsy użytkownika i wymagania dotyczące danych  
1. **Interfejs użytkownika:**
   - Aplikacja powinna być zbudowana w formie Jupyter Notebook, co umożliwia interaktywną pracę z kodem i wynikami.
   - Powinna zawierać sekcje z nagłówkami, które jasno określają funkcjonalności (np. "Scraping danych", "Analiza sentymentu", "Chmura słów").
   - Użytkownik powinien mieć możliwość wprowadzania parametrów (np. zakres czasowy, liczba postów) w formie komórek kodu lub formularzy.
2. **Wymagania dotyczące danych:**
   - Aplikacja powinna przyjmować dane w formacie JSON lub CSV, które będą zawierały zebrane posty i komentarze.
   - Powinna być możliwość wczytywania danych z plików lokalnych oraz zdalnych źródeł (np. API Reddit i Wykop).
   - Zebrane dane powinny być przechowywane w strukturze umożliwiającej łatwe przetwarzanie i analizę.

### Słownictwo dokumentacji  
- **Scraping:** Proces automatycznego pobierania danych z internetu.
- **Sentiment Analysis (Analiza sentymentu):** Technika oceny emocji wyrażonych w tekście.
- **Chmura słów:** Wizualizacja najczęściej występujących słów w zbiorze tekstów.
- **Asocjacje:** Związki między słowami, które występują razem w tekstach.
### Przypadki użycia (use cases)  
1. Użytkownik chce zebrać dane: Użytkownik wprowadza parametry (np. subreddity, zakres czasowy) i uruchamia sekcję scrapującą dane.
2. Użytkownik chce przeprowadzić analizę sentymentu: Użytkownik uruchamia sekcję analizy sentymentu, aby zobaczyć wyniki klasyfikacji postów.
3. Użytkownik chce zobaczyć chmurę słów: Użytkownik uruchamia sekcję wizualizacji, aby zobaczyć chmurę słów na podstaw
### Scenariusze użytkownika (user stories)  

#### Scenariusz 1: Analiza porównawcza powiązana z wyborami prezydenckimi

**Użytkownik:** Ania, analityk danych w agencji badawczej.

**Cel:** Ania chce przeprowadzić analizę porównawczą sentymentu dotyczącego dwóch kandydatów w nadchodzących wyborach prezydenckich.

**Kroki:**
1. **Zbieranie danych:**
   - Ania otwiera Jupyter Notebook i wprowadza parametry do sekcji scrapującej dane.
   - Wybiera subreddity związane z polityką oraz odpowiednie tagi na Wykop, które dotyczą obu kandydatów.
   - Ustala zakres czasowy na ostatnie trzy miesiące przed wyborami.
   - Uruchamia sekcję scrapującą, aby pobrać dane dotyczące postów i komentarzy.

2. **Przetwarzanie danych:**
   - Ania uruchamia sekcję przetwarzania danych, która oczyszcza zebrane dane z niepotrzebnych znaków i stop-słów.

3. **Analiza sentymentu:**
   - Ania uruchamia sekcję analizy sentymentu, aby sklasyfikować posty i komentarze jako pozytywne, negatywne lub neutralne dla obu kandydatów.
   - Otrzymuje wyniki w formie wykresu porównawczego, który pokazuje, jak zmieniały się nastroje w czasie.

4. **Wizualizacja chmury słów:**
   - Ania generuje chmurę słów dla obu kandydatów, aby zobaczyć, które słowa najczęściej pojawiają się w kontekście ich kampanii.

5. **Wnioski:**
   - Ania analizuje wyniki i przygotowuje raport, który przedstawia różnice w sentymencie oraz kluczowe tematy, które dominowały w dyskusjach na temat obu kandydatów.

---

#### Scenariusz 2: Analiza porównawcza powiązana z wyborami konsumentów (Lidl vs Biedronka)

**Użytkownik:** Marek, badacz rynku w firmie konsultingowej.

**Cel:** Marek chce przeprowadzić analizę porównawczą sentymentu dotyczącego dwóch popularnych sieci supermarketów: Lidla i Biedronki.

**Kroki:**
1. **Zbieranie danych:**
   - Marek otwiera Jupyter Notebook i wprowadza parametry do sekcji scrapującej dane.
   - Wybiera odpowiednie subreddity oraz tagi na Wykop, które dotyczą opinii o Lidlu i Biedronce.
   - Ustala zakres czasowy na ostatnie sześć miesięcy.
   - Uruchamia sekcję scrapującą, aby pobrać dane dotyczące postów i komentarzy.

2. **Przetwarzanie danych:**
   - Marek uruchamia sekcję przetwarzania danych, która oczyszcza zebrane dane z niepotrzebnych znaków i stop-słów.

3. **Analiza sentymentu:**
   - Marek uruchamia sekcję analizy sentymentu, aby sklasyfikować posty i komentarze jako pozytywne, negatywne lub neutralne dla obu sieci.
   - Otrzymuje wyniki w formie wykresu porównawczego, który pokazuje, jak klienci oceniają obie sieci.

4. **Wizualizacja chmury słów:**
   - Marek generuje chmurę słów dla Lidla i Biedronki, aby zobaczyć, które słowa najczęściej pojawiają się w kontekście opinii o tych supermarketach.

5. **Wnioski:**
   - Marek analizuje wyniki i przygotowuje raport, który przedstawia różnice w sentymencie oraz kluczowe tematy, które dominowały w dyskusjach na temat obu sieci, co może pomóc w strategii marketingowej.

