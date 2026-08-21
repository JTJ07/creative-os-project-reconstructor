# Prompt startowy — rekonstrukcja projektu zgodnie z Creative OS

Pracujemy zgodnie z Creative OS zapisanym w repozytorium:

https://github.com/JTJ07/COS

Najpierw przeczytaj:

1. `README.md`
2. `CREATIVE_OS.md`

Załączona rozmowa i załączniki są dokumentacją przebiegu projektu.

Nie analizuj rozmowy jako samodzielnego tekstu.

Przeanalizuj projekt, jego sposób pracy, rozwój i aktualny stan.

Rozmowa jest źródłem informacji o projekcie, a nie głównym przedmiotem oceny.

Pracuj najpierw w trybie `READ_ONLY`.

---

## ETAP 1 — REKONSTRUKCJA PROJEKTU

### 1. Identyfikacja projektu

Ustal, jaki projekt opisują materiały.

### 2. Pojęcia wewnętrzne projektu

Terminy, nazwy narzędzi i mechanizmów występujące w załącznikach traktuj najpierw jako pojęcia wewnętrzne projektu.

Odtwórz ich znaczenie z kontekstu wszystkich materiałów.

Nie oznaczaj ich jako niezrozumiałe ani jako osobne nowe pomysły tylko dlatego, że nie występują jeszcze w Creative OS.

### 3. Model działania

Zrekonstruuj:

- główny cel projektu;
- problem, który projekt ma rozwiązać;
- oczekiwany rezultat dla użytkownika;
- sposób działania systemu krok po kroku;
- przepływ informacji;
- role użytkownika, AI, aplikacji i innych narzędzi;
- punkty, w których użytkownik podejmuje decyzję;
- wejścia i wyjścia procesu;
- używane artefakty;
- lokalne źródło prawdy;
- sposób zapisywania stanu;
- sposób rozpoczynania, prowadzenia i kończenia sesji;
- sposób wznawiania pracy po przerwie.

### 4. Historia rozwoju

Odtwórz:

- od czego projekt się zaczął;
- jakie kierunki zostały porzucone lub zastąpione;
- jakie jawne decyzje użytkownika zmieniły kierunek;
- jakie elementy pochodzą wyłącznie z rekomendacji AI;
- co zostało rzeczywiście wykonane;
- co istnieje tylko w dokumentacji lub roadmapie.

---

## ETAP 2 — OCENA SPOSOBU PRACY

### 5. Ocena prowadzenia projektu

Oceń:

- co działa dobrze;
- gdzie użytkownik zachowuje kontrolę;
- gdzie AI wykonuje właściwą pracę;
- gdzie istnieje zbędna praca ręczna;
- gdzie architektura została rozwinięta przed dowodem potrzeby;
- gdzie deklaracje dokumentacji są szersze niż implementacja;
- gdzie „artefakt istnieje” zostało pomylone z „rezultat działa”;
- gdzie brakuje jednego właściciela stanu;
- gdzie występuje ryzyko utraty kontekstu albo ponownego otwierania zamkniętych pomysłów.

### 6. Klasyfikacja implementacji, dowodu i pochodzenia informacji

Oddziel trzy różne wymiary.

**Status implementacji:**

- istniejący artefakt;
- wykonywalny mechanizm;
- częściowa implementacja;
- mock lub heurystyka;
- planowana funkcja.

**Status dowodu:**

- `EXISTING ARTIFACT`;
- `EXECUTABLE MECHANISM`;
- `OBSERVED WORKING RESULT`;
- `VALIDATED RESULT`.

**Pochodzenie informacji:**

- rekomendacja AI;
- jawna decyzja użytkownika;
- hipoteza wymagająca testu;
- dowód z rzeczywistego użycia.

Nie nazywaj elementu działającym rezultatem wyłącznie dlatego, że istnieje prompt, kod, dokumentacja, procedura albo kompletna specyfikacja.

---

## ETAP 3 — AKTUALNY STAN

### 7. Punkt zatrzymania

Ustal dokładnie:

- gdzie projekt się zatrzymał;
- jaki jest ostatni potwierdzony rezultat;
- czego jeszcze nie przetestowano;
- co blokuje wznowienie;
- czego brakuje do zakończenia obecnego etapu;
- jaki jest jeden najmniejszy następny krok;
- jaki dowód może zmienić dalszy plan.

### 8. Zakaz rozwijania roadmapy przed dowodem

Nie rozwijaj roadmapy.

Nie proponuj nowych funkcji, dopóki nie ocenisz, czy są potrzebne do wykonania najbliższego testu.

---

## ETAP 4 — CREATIVE OS

### 9. Porównanie ze stanem kanonicznym

Dopiero po pełnej rekonstrukcji projektu porównaj wynik z `CREATIVE_OS.md`.

### 10. Klasyfikacja projektu

Określ, czy materiał opisuje:

- istniejący aktywny projekt;
- istniejący projekt historyczny lub zarchiwizowany;
- kandydata na nowy projekt;
- część innego projektu;
- alias istniejącego projektu;
- projekt, którego nie da się przypisać i który pozostaje `UNASSIGNED`.

### 11. Idea Inbox

Nie traktuj wszystkich funkcji, komponentów, nazw roboczych, wariantów i etapów projektu jako osobnych wpisów Idea Inbox.

Do Idea Inbox trafiają tylko rzeczywiste nowe kierunki, które nie są częścią już zrekonstruowanego projektu.

### 12. Minimalna propozycja aktualizacji

Przygotuj minimalną propozycję aktualizacji:

- tabeli Projekty;
- Idea Inbox tylko dla rzeczywiście nowych kierunków;
- Aktualnego Handoffu;
- sekcji Ewolucja tylko wtedy, gdy zmieniła się trwała reguła albo architektura Creative OS.

### 13. Brak zapisu bez zatwierdzenia

Nie zapisuj niczego do repo.

Nie twórz brancha, commitu ani PR.

---

## FORMAT ODPOWIEDZI

Na końcu pokaż:

### A. MODEL DZIAŁANIA PROJEKTU

### B. HISTORIA I EWOLUCJA PROJEKTU

### C. CO RZECZYWIŚCIE DZIAŁA

### D. ROZJAZDY MIĘDZY DEKLARACJĄ A IMPLEMENTACJĄ

### E. GDZIE ZATRZYMAŁA SIĘ PRACA

### F. CZEGO BRAKUJE DO WZNOWIENIA LUB ZAKOŃCZENIA

### G. JEDEN NAJLEPSZY NASTĘPNY KROK

### H. MINIMALNA DELTA DO `CREATIVE_OS.md`

### I. REKOMENDOWANY MINIMALNY `PROJECT_STATE.md`

Sekcję I pokaż tylko wtedy, gdy projekt wymaga nowego źródła prawdy i żaden istniejący dokument nie jest wystarczający.

---

## TRYB WYJŚCIA

Domyślnie pracuj w trybie `LITE`.

### LITE

- maksymalnie 1200 słów;
- nie powtarzaj całej historii materiału;
- pokaż tylko ustalony model projektu, aktualny stan, najważniejsze rozjazdy, brak do wznowienia, jeden następny krok i minimalną deltę Creative OS.

Jeżeli wymagane jest pokazanie kompletnego draftu w sekcji I, możesz przekroczyć limit wyłącznie o treść tego minimalnego draftu.

### FULL

Użyj tylko wtedy, gdy:

- użytkownik jawnie napisze `FULL`;
- materiały dotyczą rekonstrukcji dużego projektu historycznego;
- istnieją sprzeczne źródła, których nie da się rzetelnie rozstrzygnąć w wersji LITE.

---

## ZASADA DOWODU

Nie nazywaj funkcji „działającą” wyłącznie dlatego, że istnieje prompt, kod, procedura, dokumentacja albo specyfikacja.

Rozróżnij:

- `EXISTING ARTIFACT`;
- `EXECUTABLE MECHANISM`;
- `OBSERVED WORKING RESULT`;
- `VALIDATED RESULT`.

Brak zapisu rzeczywistego użycia oznacza najwyżej `EXISTING ARTIFACT` albo `EXECUTABLE MECHANISM`.

---

## ZASADA NASTĘPNEGO KROKU

Jeden następny krok musi być pierwszym brakującym warunkiem w rzeczywistym łańcuchu zależności.

Jeżeli brakuje źródła prawdy, repozytorium, pliku kanonicznego albo dostępu do istniejących artefaktów, nie proponuj jeszcze implementacji ani testu zależnego od tych materiałów.

Nie wskazuj użytkownikowi samej czynności zatwierdzenia czegoś, czego nie pokazałeś w odpowiedzi.

---

## ZASADA ZMIANY CREATIVE OS

Rozpoznanie istniejącego projektu w materiałach nie oznacza automatycznego dodania go do kanonicznej tabeli Projektów.

Każdą nową kartę projektu oznacz:

`PROPOSED — REQUIRES USER APPROVAL`

Aktualnego Handoffu nie zmieniaj wyłącznie dlatego, że projekt został przeanalizowany.

Rozróżnij:

- ostatnio zrekonstruowany projekt;
- aktualnie aktywowany projekt.

---

## ZASADA AUTONOMII PRZY ŹRÓDLE PRAWDY

Jeżeli projekt nie ma jednego kanonicznego źródła prawdy:

1. Nie przerzucaj na użytkownika obowiązku samodzielnego wyboru spośród wielu dokumentów.

2. Zidentyfikuj wszystkie realne kandydatury na lokalne źródło prawdy.

3. Ustal najnowsze jawne decyzje użytkownika dotyczące:

   - aktualnego celu;
   - obowiązującego rezultatu;
   - zakresu;
   - statusu;
   - struktury produktu lub projektu;
   - modelu działania;
   - jednego następnego kroku.

4. Oznacz dokumenty jako:

   - `CURRENT` — zgodny z najnowszymi decyzjami;
   - `PARTIALLY CURRENT` — zawiera nadal ważne elementy, ale wymaga korekty;
   - `SUPERSEDED` — zastąpiony późniejszą decyzją;
   - `EVIDENCE ONLY` — zachowuje obserwacje lub historię, ale nie jest źródłem aktualnego stanu;
   - `UNKNOWN` — nie da się ustalić statusu bez dodatkowego dowodu.

5. Wskaż jednego najlepszego kandydata na źródło prawdy.

6. Jeżeli żaden istniejący dokument nie jest wystarczający, przygotuj w tej samej odpowiedzi kompletny minimalny draft kanonicznego stanu projektu.

   Draft ma zawierać wyłącznie:

   - nazwę projektu;
   - status;
   - aktualny rezultat;
   - najnowsze jawne decyzje użytkownika;
   - potwierdzone rezultaty i istniejące artefakty;
   - elementy niepotwierdzone;
   - aktualne sprzeczności;
   - miejsce zatrzymania;
   - rzeczywistą blokadę;
   - jeden następny krok;
   - odwołania do szczegółowych źródeł.

   Jeżeli wymagany jest nowy plik, pokaż jego pełną gotową treść w sekcji:

   `I. REKOMENDOWANY MINIMALNY PROJECT_STATE.md`

7. Nie twórz pełnej nowej dokumentacji projektu.

   Przygotuj najmniejszy stan wystarczający do poprawnego wznowienia.

8. Nie pytaj użytkownika, który z wielu plików wybrać, jeżeli możesz przygotować jedną uzasadnioną rekomendację.

9. Poproś użytkownika wyłącznie o:

   - zatwierdzenie rekomendowanego źródła prawdy;
   - wybór między sprzecznymi jawnymi decyzjami o podobnym pierwszeństwie;
   - zmianę celu, kierunku albo priorytetu;
   - decyzję, której nie można wiarygodnie odtworzyć z materiałów.

10. Rozróżnij:

    - projekt istniejący historycznie;
    - projekt rozpoznany w materiałach;
    - projekt wpisany do Creative OS;
    - projekt aktywowany do dalszej pracy.

Jeżeli projekt nie jest jeszcze wpisany do Creative OS, nie nadawaj mu kanonicznego statusu `PAUSED`, `ACTIVE` ani `CLOSED`.

Użyj:

`PROPOSED / NOT ACTIVATED`

Następnie dodaj rzeczywistą blokadę, jeżeli została potwierdzona, na przykład:

- `SOURCE OF TRUTH REQUIRED`;
- `ACCESS REQUIRED`;
- `VALIDATION REQUIRED`;
- `USER DIRECTION REQUIRED`;
- `EXTERNAL DEPENDENCY`;
- `NO CURRENT BLOCKER`.

Przykład:

`PROPOSED / NOT ACTIVATED / SOURCE OF TRUTH REQUIRED`

W sekcji minimalnej delty do Creative OS przedstaw:

1. proponowaną kartę projektu;
2. jej uzasadnienie;
3. jednego rekomendowanego właściciela szczegółowego stanu;
4. informację:

   `PROPOSED — REQUIRES USER APPROVAL`

---

## ZASADA DOMKNIĘCIA ŹRÓDŁA PRAWDY

Jeżeli projekt ma blokadę `SOURCE OF TRUTH REQUIRED`:

1. Nie kończ zaleceniem utworzenia, przygotowania albo zatwierdzenia źródła prawdy bez pokazania jego treści.

2. Następny krok może brzmieć:

   „Zatwierdzić przedstawiony draft źródła prawdy”

   tylko wtedy, gdy pełny draft został pokazany w tej samej odpowiedzi.

3. Sprzeczności, których nie da się rozstrzygnąć na podstawie materiałów, oznacz:

   `USER DECISION REQUIRED`

4. Jeżeli istniejący dokument jest wystarczający po małej korekcie, pokaż dokładną minimalną deltę zamiast tworzyć nowy plik.

5. Nie zapisuj proponowanej karty ani draftu do repo bez jawnego zatwierdzenia użytkownika.
