# MAYBEREADME

## Opis projektu
Nasz projekt dotyczy prototypowania chatbota, który zwraca precyzyjne odpowiedzi z dokumentów PDF wykorzystując embedding. Celem jest umożliwienie szybkiego i dokładnego wyszukiwania informacji w dużych zbiorach dokumentów.
## Ważna informacja
Projekt wymaga pliku `key.txt` umieszczonego w głównym folderze, który nie jest dołączony i nie zostanie tutaj umieszczony, ponieważ znajduje się w pliku `.gitignore`. Plik `key.txt` powinien zawierać klucz do ChatGPT. Aby projekt działał prawidłowo, należy samodzielnie utworzyć ten plik i umieścić w nim odpowiedni klucz.

## Struktura folderów
- `/Doc` - folder na dokumenty PDF do embeddingu.
- `/Saved` - folder do przechowywania danych używanych pomiędzy funkcjami.

## Wymagania
- `requirements.txt` - plik zawierający listę wymaganych modułów.
- `installreqs.bat` - plik batch do instalacji modułów wymienionych w `requirements.txt` (dla systemów Windows).

## Pliki źródłowe
- `ourfuncs.py` - plik zawierający funkcje wykorzystywane wielokrotnie.
- `test_gpt.ipynb` - sprawdzenie połączenia z API.
- `doc_process.ipynb` - przetwarza PDFy z folderu `/Doc` na listę list, zapisuje pickle w `/Saved/textdata.pkl`. Struktura listy: `[... , ['Document', 'Page', 'Block', "WordCount", 'Text'] , ...]`.
- `text_embedding.ipynb` - wczytuje wcześniej wspomniany pickle i tworzy embeddingi dla każdego tekstu, dołącza do listy i zapisuje jako nowy pickle `[... , ['Document', 'Page', 'Block', "WordCount", 'Text', 'Embedding'] , ...]`.
- `chat_embedded.ipynb` - minimalny produkt; tworzy embedding zapytania użytkownika, porównuje go z zapisanymi embeddingami tekstów i zwraca top X pasujących tekstów.

## Instrukcja uruchomienia
1. Zainstaluj wymagane moduły za pomocą `installreqs.bat`.
2. Umieść swoje dokumenty PDF w folderze `/Doc`.
3. Uruchom `doc_process.ipynb`, aby przetworzyć dokumenty PDF.
4. Uruchom `text_embedding.ipynb`, aby stworzyć embeddingi tekstów.
5. Uruchom `chat_embedded.ipynb`, aby testować chatbota.
