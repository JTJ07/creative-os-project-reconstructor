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
- scenariusze regresji;
- `VALIDATION.md`;
- `scripts/verify_reconstructor.py`;
- workflow GitHub Actions.

### EXECUTABLE MECHANISM

- Prompt może zostać wklejony do nowej rozmowy wraz z materiałami projektu i prowadzi analizę według stałego formatu A–I.
- Deterministyczny walidator może sprawdzić obecność plików, wersję, strukturę promptu, parking i kryteria regresji bez uruchamiania modelu AI.

### OBSERVED WORKING RESULT

Prompt poprawnie przeanalizował różne klasy projektów, między innymi:

- projekt historyczny z wieloma aliasami;
- projekt techniczny z rozjazdem między architekturą a implementacją;
- projekt biznesowy z wieloma konkurującymi dokumentami;
- projekt bez lokalnego źródła prawdy;
- system deliberacyjny wymagający przygotowania gotowego `PROJECT_STATE.md`.

Niezależny cold start Creative OS bez pamięci rozmowy poprawnie rozpoznał rolę Project Reconstructora, jego wersję i sposób użycia.

### REAL-VALUE RUN 001 — ScriptOps

2026-08-19 wykonano `LITE / READ_ONLY` na rzeczywistym projekcie `JTJ07/scriptops@daa6e5dc210e09171a530eeffe5601e0e74ae041` z cross-checkiem aktualnego COS i zaakceptowanej historii Saddle.

Wynik:

- Reconstructor poprawnie zachował lokalne `PROJECT_STATE.md` jako semantic owner szczegółowego stanu ScriptOps;
- odróżnił `PHASE 6 CONTROLLED WORKFLOW MECHANISM PASS` od maturity/production claim;
- wykrył trzy realne current-state contradictions: stale ScriptOps state owner, stale ScriptOps handoff i stale pochodny pointer/handoff w COS;
- wskazał state reconciliation jako pierwszy brakujący warunek zamiast nowej implementacji;
- nie utworzył hidden functional PASS, nie aktywował projektu i nie zaproponował nowej capability;
- nie ujawnił błędu wymagającego zmiany zamrożonego promptu v1.0.

Evidence: `evidence/REAL_VALUE_RUN_001_SCRIPTOPS_2026-08-19.md`.

### VALIDATED RESULT

Brak długoterminowej walidacji. Jeden real-value run zwiększa observed evidence, ale nie potwierdza jeszcze stabilności na większej liczbie niezależnych projektów ani zgodności wyników między różnymi modelami.

## Najnowsze decyzje

- Obecny prompt zostaje zamrożony jako wersja `v1.0`.
- Dalsze zmiany promptu wynikają wyłącznie z konkretnych, najlepiej powtarzalnych błędów.
- Widoczność repozytorium nie jest częścią kanonicznego stanu projektu.
- Pełne prywatne materiały źródłowe nie są przechowywane w testach niezależnie od widoczności repo.
- Creative OS przechowuje wyłącznie stan wysokiego poziomu; szczegółowy stan tego narzędzia należy do tego repozytorium.
- Deterministyczny walidator repo jest dozwoloną kontrolą spójności i nie zmienia zamrożonego promptu.
- Automatyczny runner modeli, scoring jakości i dodatkowa orkiestracja pozostają poza bieżącym zakresem.

## Znane ograniczenia

- Jakość wyniku zależy od kompletności materiałów.
- Sprzeczne jawne decyzje o podobnym pierwszeństwie wymagają rozstrzygnięcia użytkownika.
- AI może nadal formułować pojedyncze zdania zbyt mocno; przed zapisem do repo wymagany jest przegląd.
- Limit `LITE` może zostać przekroczony o minimalny draft źródła prawdy.
- Walidator deterministyczny nie ocenia semantycznej jakości odpowiedzi AI.
- Brak automatycznego runnera modeli.
- Jeden real-value run nie jest jeszcze długoterminową walidacją.

## Bieżąca faza

Stabilizacja przez rzeczywiste użycie bez rozbudowy promptu.

Pierwszy real-value run został wykonany. Nie znaleziono powodu do zmiany promptu; znaleziono realny drift w stanie targetu, który prompt poprawnie sklasyfikował.

## Jeden następny krok

Nie zmieniać promptu. Zachować wynik Run 001 jako observed evidence i wrócić do Reconstructora dopiero przy kolejnym rzeczywistym projekcie albo przy konkretnej porażce semantycznej. Globalny ekosystem może przejść do kolejnego materially-different workload po naprawie state drift ujawnionego przez Run 001.

## Warunek zmiany promptu

Prompt zmieniamy dopiero wtedy, gdy:

1. wystąpi konkretny błąd wpływający na decyzję lub stan projektu;
2. błąd nie wynika wyłącznie z braku materiałów;
3. nie da się go naprawić małą korektą samego raportu;
4. można opisać test, który odróżnia stan przed poprawką od stanu po poprawce.
