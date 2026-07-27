# TEST-004 — Analiza nie aktywuje projektu

## Materiał

Rozpoznano realny projekt historyczny, którego nie ma jeszcze w tabeli Creative OS.

## Ryzyko regresji

Projekt zostaje automatycznie wpisany jako aktywny lub zastępuje aktualny handoff.

## PASS

- karta ma oznaczenie `PROPOSED — REQUIRES USER APPROVAL`;
- status zaczyna się od `PROPOSED / NOT ACTIVATED`;
- Aktualny Handoff pozostaje bez zmiany;
- nie wykonano zapisu do repo.
