# słowocieć do analizy sentymentu
import plwordnet
# wn = plwordnet.load('plwordnet_4_2/plwordnet_4_2.xml')

#morfeusz2 posłuży do lematyzacji
# dla morfeusza2 obecnie wymagana jest maksymalnie wersja 3.11 pythona
import morfeusz2
import pandas as pd

# *Załadowanie polskiego słownika sentymentu (ręcznie przefiltrowany plwordnet w csv)
slownik_sentymentu = pd.read_csv('słowniki/SłownikSentymentu.csv', sep=';',encoding='cp1250')
print(slownik_sentymentu.columns.tolist())
# Wczytanie zescrapowanego pliku tekstowego z Reddita/Wykopu
with open('src/data/results_reddit.txt', 'r', encoding='utf-8') as file:
    tekst_cały = file.read()
# Podział wczytanego pliku na słowa (nie jest wyczyszczony)
slowa = tekst_cały.split()
# Utworzenie ramki danych, gdzie każde słowo jest w osobnym wierszu
ramka_slow = pd.DataFrame(slowa, columns=['słowa'])
# Czyszczenie ramki z niepotrzebnych słów i danych
to_remove = '-,? .>#:"/\[]+=!%<*()|–„'
table = str.maketrans('', '', to_remove)
cleaned_slowa = [word.translate(table) for word in slowa]

# Usuń niechciane słowa
remove_slowa = ['Tytuł:', 'Treść:', 'Tag:', 'Subreddit:']
filtered_words = [word for word in cleaned_slowa if word not in remove_slowa and word != '']
# Usuwanie linków
filtered_words_no_links = [
    word for word in filtered_words
    if not (word.startswith('http') or word.startswith('www'))
]
# Usuwanie liczb
filtered_words_no_links_no_digits = [
    word for word in filtered_words_no_links
    if not word.isdigit()
]
# Utwórz DataFrame
ramka_slow = pd.DataFrame(filtered_words_no_links_no_digits, columns=['slowa'])
print(ramka_slow)
# Lematyzacja każdego ze słów
morfeusz = morfeusz2.Morfeusz()

def lemmatize_word(word):
    analyses = morfeusz.analyse(word)
    if analyses:
        # analyses to lista krotek: (start, end, (lemma, tag), score)
        # Bierzemy pierwszą lematę z analizy
        lemma = analyses[0][2][1]  # [0] - pierwszy wynik, [2] - tuple (base, lemma, tag), [1] - lemma
        return lemma
    else:
        return word

ramka_slow['lemma'] = ramka_slow['slowa'].apply(lemmatize_word)

# Najczęstsze słowa:
ramka_slow['lemma_clean'] = ramka_slow['lemma'].apply(lambda x: x.split(':')[0])
lemma_counts = ramka_slow['lemma_clean'].value_counts()
print(lemma_counts.head(50))

# czyszczenie lematów ze zbędnych słów - stopwords (się, na, i, w, itp...) 
# https://github.com/stopwords-iso/stopwords-pl/blob/master/stopwords-pl.txt

with open('stopwords-pl.txt', 'r', encoding='utf-8') as file:
    df_polish_stop_words = file.read().splitlines()
ramka_slow = ramka_slow[~ramka_slow['lemma_clean'].isin(df_polish_stop_words)]
print(ramka_slow['lemma_clean'].value_counts().head(50))

# Chmura słów będzie tutaj

# Przypisanie sentymentu 
print(slownik_sentymentu.columns)
# Połączenie ramki lematów z ramką słownika sentymentu
ramka_slow = ramka_slow.merge(
    slownik_sentymentu,
    left_on='lemma_clean', 
    right_on='lemat',
    how='left'
)

# Użyj poprawnej nazwy kolumny z sentymentem
#ramka_slow['nacechowanie'] = ramka_slow['nacechowanie'].fillna(0) 

# Wyświetlenie kilku pierwszych wierszy z oceną sentymentu
#print(ramka_slow[['lemma_clean', 'nacechowanie']].head(10))
#print(df_polish_stop_words)

