# IDEA ARCHIVE

Pomysły wartościowe, ale nieaktywne. Nie są częścią zakresu `v1.0`.

---

## IDEA-001 — Automatyczny runner testów promptu

**Status:** `PARKING`

**Wartość:** uruchamianie tego samego zestawu zanonimizowanych przypadków po każdej zmianie promptu i porównywanie wyników z kryteriami.

**Dlaczego nie teraz:** obecna liczba zmian nie uzasadnia budowy infrastruktury testowej.

**Warunek powrotu:** co najmniej dwie kolejne zmiany promptu albo regresja niewykryta ręcznie.

---

## IDEA-002 — Porównanie wyników wielu modeli

**Status:** `PARKING`

**Wartość:** sprawdzenie, czy różne modele podobnie rekonstruują projekt, dowody i pierwszy brakujący warunek.

**Dlaczego nie teraz:** najpierw potrzebne są kolejne rzeczywiste przypadki użycia wersji `v1.0`.

**Warunek powrotu:** istotne rozbieżności między modelami wpływające na decyzję użytkownika.

---

## IDEA-003 — Skrócony prompt dla prostych projektów

**Status:** `PARKING`

**Wartość:** mniejszy koszt wejścia dla materiałów krótkich i niesprzecznych.

**Dlaczego nie teraz:** dwa warianty promptu zwiększyłyby ryzyko rozjazdu zasad.

**Warunek powrotu:** regularne przypadki, w których pełny prompt utrudnia pracę mimo trybu `LITE`.

---

## IDEA-004 — Generator minimalnego patcha do PROJECT_STATE.md

**Status:** `PARKING`

**Wartość:** zamiast pełnego nowego dokumentu wynik mógłby tworzyć precyzyjną deltę do istniejącego lokalnego stanu.

**Dlaczego nie teraz:** obecny prompt już nakazuje pokazać minimalną deltę, gdy istniejący dokument wymaga tylko małej korekty.

**Warunek powrotu:** częste ręczne przenoszenie tych samych zmian do plików projektów.

---

## IDEA-005 — Walidator formatu odpowiedzi A–I

**Status:** `PARKING`

**Wartość:** automatyczne wykrywanie brakujących sekcji, nieprawidłowego statusu projektu albo braku draftu przy `SOURCE OF TRUTH REQUIRED`.

**Dlaczego nie teraz:** kryteria regresji wystarczają do ręcznej kontroli w fazie stabilizacji.

**Warunek powrotu:** powtarzalne błędy struktury odpowiedzi.

---

## IDEA-006 — Ocena jakości rekonstrukcji punktami

**Status:** `PARKING`

**Wartość:** wspólna rubryka dla identyfikacji projektu, dowodów, zależności, kanonu Creative OS i autonomii AI.

**Dlaczego nie teraz:** punktacja mogłaby stworzyć pozór precyzji bez odpowiedniej liczby danych.

**Warunek powrotu:** potrzeba porównania większej liczby wersji promptu lub modeli.
