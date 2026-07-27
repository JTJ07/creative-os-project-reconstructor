# Creative OS Project Reconstructor

Narzędzie do rekonstrukcji rzeczywistego stanu projektu z rozmów i załączników.

Repozytorium przechowuje stabilny prompt startowy, stan samego eksperymentu, historię problemów i poprawek, parking wartościowych pomysłów oraz kryteria regresji.

## Cel

Prompt ma pomóc AI:

- analizować projekt, a nie sam tekst rozmowy;
- odtwarzać pojęcia wewnętrzne, aliasy i mechanizmy;
- rozdzielać deklaracje, artefakty, implementację i dowody;
- ustalać miejsce zatrzymania oraz pierwszy brakujący warunek;
- przygotowywać minimalną propozycję delty do Creative OS;
- tworzyć gotowy draft lokalnego `PROJECT_STATE.md`, gdy projekt nie ma źródła prawdy;
- nie zmieniać repozytoriów bez jawnego zatwierdzenia użytkownika.

## Wersja

**v1.0 — STABILIZATION**

Obecna wersja przeszła testy na różnych typach materiałów: projektach historycznych, technicznych, biznesowych, narracyjnych i systemach bez kanonicznego źródła prawdy.

Status dowodu: `OBSERVED WORKING RESULT`. Nie jest to jeszcze długoterminowo zwalidowany system.

## Użycie

1. Otwórz nową rozmowę z AI.
2. Dodaj rozmowę źródłową i wszystkie związane z nią załączniki.
3. Wklej pełną treść `PROMPT_STARTOWY.md`.
4. Przejrzyj raport A–H.
5. Gdy powstanie sekcja I, zatwierdź albo skoryguj przedstawiony draft `PROJECT_STATE.md`.
6. Dopiero po zatwierdzeniu wykonuj zmiany w repozytorium projektu lub w Creative OS.

Domyślnym trybem jest `LITE / READ_ONLY`.

## Struktura

- `PROMPT_STARTOWY.md` — aktywna wersja promptu.
- `PROJECT_STATE.md` — kanoniczny stan tego narzędzia.
- `EVOLUTION_LOG.md` — problemy, opór, poprawki i wyniki testów.
- `IDEA_ARCHIVE.md` — wartościowe pomysły odłożone bez aktywacji.
- `tests/` — zanonimizowane scenariusze regresji i kryteria zaliczenia.

## Reguła rozwoju

> Rozwijamy prompt na podstawie powtarzalnych porażek w rzeczywistym użyciu, a nie dlatego, że można dopisać kolejną dobrą regułę.

Zmiana promptu wymaga konkretnego błędu, dowodu z testu i sprawdzenia, czy poprawka nie psuje wcześniejszych zachowań.

## Prywatność

Repozytorium jest prywatne. Mimo to nie należy zapisywać tu pełnych prywatnych rozmów, danych osobowych ani poufnych materiałów projektów. Testy przechowują wyłącznie zanonimizowany opis przypadku i oczekiwane zachowanie.
