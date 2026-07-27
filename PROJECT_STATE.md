# PROJECT_STATE — Creative OS Project Reconstructor

## Status

`ACTIVE / V1.0 STABILIZATION`

## Cel

Rekonstruować projekt z rozmów i załączników tak, aby AI ustalało jego model działania, historię, rzeczywisty stan, punkt zatrzymania, pierwszy brakujący warunek oraz minimalną propozycję delty do Creative OS.

## Aktualny rezultat

Istnieje stabilny prompt startowy działający domyślnie w trybie `LITE / READ_ONLY`.

Prompt:

- traktuje rozmowę jako dokumentację projektu, a nie główny przedmiot analizy;
- rekonstruuje pojęcia wewnętrzne, aliasy i komponenty;
- oddziela implementację, status dowodu i pochodzenie informacji;
- odróżnia artefakt od obserwowanego oraz zwalidowanego rezultatu;
- wybiera pierwszy brakujący warunek w łańcuchu zależności;
- nie aktywuje projektu ani nie zmienia handoffu wyłącznie dlatego, że projekt został przeanalizowany;
- klasyfikuje kandydatów na źródło prawdy;
- przygotowuje kompletny minimalny draft `PROJECT_STATE.md`, zanim poprosi o jego zatwierdzenie;
- blokuje zapis do repo bez jawnej zgody użytkownika.

## Status dowodu

### EXISTING ARTIFACT

- `PROMPT_STARTOWY.md`;
- opis zasad pracy;
- archiwum ewolucji;
- scenariusze regresji.

### EXECUTABLE MECHANISM

Prompt może zostać wklejony do nowej rozmowy wraz z materiałami projektu i prowadzi analizę według stałego formatu A–I.

### OBSERVED WORKING RESULT

Prompt poprawnie przeanalizował różne klasy projektów, między innymi:

- projekt historyczny z wieloma aliasami;
- projekt techniczny z rozjazdem między architekturą a implementacją;
- projekt biznesowy z wieloma konkurującymi dokumentami;
- projekt bez lokalnego źródła prawdy;
- system deliberacyjny wymagający przygotowania gotowego `PROJECT_STATE.md`.

### VALIDATED RESULT

Brak długoterminowej walidacji. Nie potwierdzono jeszcze stabilności na większej liczbie niezależnych projektów ani zgodności wyników między różnymi modelami.

## Najnowsze decyzje

- Obecny prompt zostaje zamrożony jako wersja `v1.0`.
- Dalsze zmiany wynikają wyłącznie z konkretnych, najlepiej powtarzalnych błędów.
- Repozytorium pozostaje prywatne.
- Pełne prywatne materiały źródłowe nie są przechowywane w testach.
- Creative OS przechowuje wyłącznie stan wysokiego poziomu; szczegółowy stan tego narzędzia należy do tego repozytorium.
- Nie rozwijamy teraz automatyzacji ani dodatkowej architektury.

## Znane ograniczenia

- Jakość wyniku zależy od kompletności materiałów.
- Sprzeczne jawne decyzje o podobnym pierwszeństwie wymagają rozstrzygnięcia użytkownika.
- AI może nadal formułować pojedyncze zdania zbyt mocno; przed zapisem do repo wymagany jest przegląd.
- Limit `LITE` może zostać przekroczony o minimalny draft źródła prawdy.
- Brak automatycznego test runnera.

## Bieżąca faza

Stabilizacja przez rzeczywiste użycie bez rozbudowy promptu.

## Jeden następny krok

Użyć wersji `v1.0` na kolejnych rzeczywistych projektach i zapisywać wyłącznie konkretne porażki wraz z przypadkiem regresyjnym.

## Warunek zmiany promptu

Prompt zmieniamy dopiero wtedy, gdy:

1. wystąpi konkretny błąd wpływający na decyzję lub stan projektu;
2. błąd nie wynika wyłącznie z braku materiałów;
3. nie da się go naprawić małą korektą samego raportu;
4. można opisać test, który odróżnia stan przed poprawką od stanu po poprawce.
