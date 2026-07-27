# EVOLUTION LOG

Historia problemów, oporu i poprawek, które doprowadziły do wersji `v1.0`.

---

## EVOLUTION-001 — Analiza rozmowy zamiast projektu

**Problem:** AI analizowało rozmowę jako samodzielny tekst.

**Objaw:** raport oceniał styl rozmowy i wypowiedzi zamiast rekonstruować system, sposób pracy oraz stan projektu.

**Przyczyna:** rozmowa nie była jednoznacznie określona jako dokumentacja przebiegu projektu.

**Zmiana:** dodano nadrzędną regułę: rozmowa i załączniki są źródłem informacji o projekcie, a projekt jest głównym przedmiotem analizy.

**Wynik testu:** kolejne analizy rekonstruowały model działania projektu, historię, role, przepływy i punkt zatrzymania.

**Co zachowujemy:** rozróżnienie między materiałem źródłowym a przedmiotem oceny.

**Warunek ponownego otwarcia:** AI ponownie koncentruje raport na rozmowie zamiast na projekcie.

**Status:** `RESOLVED`

---

## EVOLUTION-002 — Pojęcia wewnętrzne uznawane za nowe lub niezrozumiałe

**Problem:** nazwy mechanizmów, narzędzi i aliasy projektu były traktowane jako luźne nowe pomysły.

**Objaw:** komponenty mogły trafić do Idea Inbox albo zostać opisane jako niejasne tylko dlatego, że nie występowały w Creative OS.

**Zmiana:** nakazano najpierw rekonstruować znaczenie terminów z kontekstu wszystkich materiałów i sprawdzać, czy są elementami jednego projektu.

**Wynik testu:** aliasy, etapy oraz mechanizmy były poprawnie scalane w jeden projekt.

**Co zachowujemy:** `reuse and reconstruct before classify as new`.

**Warunek ponownego otwarcia:** komponent jednego systemu zostaje ponownie wpisany jako osobny projekt lub pomysł.

**Status:** `RESOLVED`

---

## EVOLUTION-003 — Raport zbyt długi do codziennego użycia

**Problem:** pełna rekonstrukcja prowadziła do ciężkich, powtarzalnych raportów.

**Zmiana:** wprowadzono domyślny tryb `LITE`, limit 1200 słów oraz warunkowy tryb `FULL`.

**Wynik testu:** raporty zachowały model projektu, stan, rozjazdy, blokadę, jeden następny krok i deltę Creative OS bez przepisywania całej historii.

**Co zachowujemy:** `LITE` jako standard operacyjny.

**Warunek ponownego otwarcia:** raport regularnie przekracza zakres bez konieczności pokazania draftu źródła prawdy.

**Status:** `RESOLVED`

---

## EVOLUTION-004 — Artefakt mylony z działającym rezultatem

**Problem:** prompt, kod, checklista, dokument albo kompletna specyfikacja mogły zostać uznane za dowód działania.

**Zmiana:** rozdzielono status implementacji, pochodzenie informacji i cztery poziomy dowodu:

- `EXISTING ARTIFACT`;
- `EXECUTABLE MECHANISM`;
- `OBSERVED WORKING RESULT`;
- `VALIDATED RESULT`.

**Wynik testu:** dokumentacja, demo, plan i niezweryfikowane deklaracje nie były już opisywane jako działający system.

**Co zachowujemy:** brak zapisu rzeczywistego użycia oznacza najwyżej artefakt albo mechanizm wykonywalny.

**Warunek ponownego otwarcia:** raport ponownie uznaje deklarację lub dokument za obserwowany wynik.

**Status:** `RESOLVED`

---

## EVOLUTION-005 — Następny krok pomijał brakujący warunek

**Problem:** AI proponowało implementację lub test, mimo że brakowało repozytorium, pliku kanonicznego albo dostępu do artefaktów.

**Zmiana:** jeden następny krok musi być pierwszym brakującym warunkiem w rzeczywistym łańcuchu zależności.

**Wynik testu:** przy braku źródła prawdy analiza zatrzymywała się przed wdrożeniem i najpierw porządkowała stan.

**Co zachowujemy:** prerequisite-first.

**Warunek ponownego otwarcia:** zalecenie zależy od materiału lub dostępu, którego nie ma.

**Status:** `RESOLVED`

---

## EVOLUTION-006 — Samo rozpoznanie projektu zmieniało kanon Creative OS

**Problem:** analiza mogła automatycznie dodać projekt do tabeli albo zastąpić aktualny handoff.

**Zmiana:** każda nowa karta ma status `PROPOSED — REQUIRES USER APPROVAL`; rozdzielono ostatnio zrekonstruowany projekt od aktualnie aktywowanego.

**Wynik testu:** raporty proponowały kartę, ale nie aktywowały projektu i pozostawiały handoff bez zmiany.

**Co zachowujemy:** analiza nie jest decyzją kanoniczną.

**Warunek ponownego otwarcia:** wynik samodzielnie zmienia status projektu lub handoff.

**Status:** `RESOLVED`

---

## EVOLUTION-007 — Wybór źródła prawdy przerzucany na użytkownika

**Problem:** po wykryciu wielu konkurujących dokumentów AI zalecało użytkownikowi samodzielny wybór jednego pliku.

**Zmiana:** dodano klasyfikację `CURRENT`, `PARTIALLY CURRENT`, `SUPERSEDED`, `EVIDENCE ONLY`, `UNKNOWN` oraz obowiązek wskazania najlepszego kandydata.

**Wynik testu:** AI klasyfikowało dokumenty, wyłaniało kandydata i ograniczało pytania do rzeczywistych konfliktów decyzyjnych.

**Co zachowujemy:** AI wykonuje pracę przygotowawczą; użytkownik zatwierdza kierunek.

**Warunek ponownego otwarcia:** raport kończy się listą plików do ręcznego wyboru.

**Status:** `RESOLVED`

---

## EVOLUTION-008 — Zatwierdzenie dokumentu, którego AI nie pokazało

**Problem:** wynik zalecał „zatwierdzić minimalny PROJECT_STATE.md”, ale nie zawierał jego treści.

**Zmiana:** dodano zasadę domknięcia źródła prawdy i obowiązkową sekcję `I. REKOMENDOWANY MINIMALNY PROJECT_STATE.md`.

**Wynik testu:** analiza przygotowała kompletny minimalny dokument, a dopiero później wskazała zatwierdzenie jako następny krok.

**Co zachowujemy:** nie wolno prosić o zatwierdzenie nieprzedstawionego artefaktu.

**Warunek ponownego otwarcia:** raport ponownie zaleca utworzenie lub zatwierdzenie źródła prawdy bez pokazania treści.

**Status:** `RESOLVED`

---

## EVOLUTION-009 — Stabilizacja po udanym teście

**Decyzja:** wersja `v1.0` zostaje zamrożona.

**Zasada:** rozwijamy prompt na podstawie powtarzalnych porażek w rzeczywistym użyciu, a nie dlatego, że można dopisać kolejną dobrą regułę.

**Status:** `ACTIVE RULE`
