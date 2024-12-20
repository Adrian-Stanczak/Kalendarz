# Kalendarz Artysty
### Projekt by Adrian Stańczak

---

## Założenia programu

Program ma za zadanie zapisywanie wydarzeń do konkretnej daty by pomóc .np grafikowi w pracy.

## Wyamgania

Program należy uruchomić na wersji 3.12 lub nowszej 

## Atrybuty

- `"id"` - Przechowuje id wydarzenia wygenerowane z puli wolnych numerów.
- `"name"` - Przechowuje imię osoby tworzącej wydarzenie.
- `"date"` - Przechowuje date w foramcie (Rok-Miesiąc-Dzień) przyłączoną do wydarzenia.
- `"event"` - Przechowuje opis wydarzenia

## Funkcje programu

- `def main()` - Funkcja ta jest ciałem naszego programu. Ma za zadanie wywoływanie naszych pozostałych funkcji w pętli `while`, z którą wchodzimi w interakcję poprzez decydowanie co chcemy zrobić poprzez opcje `match` dzięki której możemy rozpatrzeć wiele przypadków użycia programu.

- `def add_event(kalendar:list)` - Jest to jedna z najważniejszych funkcji programu. Ma za zadanie pobranie danych od użytkownika, wygenerowanie id dla wydarzenia `event` oraz wpisania danych w słownik (`dict`), który zostanie wpisany w listę `kalendar`. Po ówczesnym załadowaniu danych, dodajemy słownik do listy i wywołujemy funkcję `def save_to_file(kalendar)` by zapisała nam dane do pliku `events.json`.

- `def save_to_file(kalendar)` - Funkcja sprawdza czy istnieje już dodane jakieś wydarzenie (jeśli nie to tworzy pustą listę `x`. Jeśli istnieje to zaczytuje plik do zmiennej oraz zapisuje zmainy do pliku `events.json`.)

- `def remove_event(kalendar)` - Funkcja jak sama nazwa ma za zadanie usunięcie danego wydarzenia z listy `kalendar` poprzez ówczesne podanie przez użytkownika `id`. Wpierw sprawdza czy lista `kalendar` istnieje oraz zaczytuje plik `events.json`. Ppo czym sprawdza po zaczytanym pliku czy istnieje `"kalendar[id]"` któe jest równe `event_id`.Jeśli tak to usuwa dany słownik i zapisuje zmiany wywłując funkcje `def save_to_file(kalendar)`.

- `def show_events()` - Jak poprzednia funkcja pobiera od użytkownika `event_id` i sprawdza czy istnieje jakieś wydarzenie w liście `kalendar`. Zaczytuje plik `events.json` i szuka czy w pliku znajdują się identyczne `events[id]` do `event_id`. Jeśli tak to wypisuje nam dane osoby, dead-line oraz treść wydarzenia.
