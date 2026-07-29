# Walidacja repozytorium

## Uruchomienie

```bash
python scripts/verify_reconstructor.py
```

Walidator jest deterministyczny. Sprawdza:

- obecność kanonicznego promptu, stanu, ewolucji, parkingu i testów;
- zgodność statusu `v1.0 — STABILIZATION`;
- obecność wymaganych sekcji i reguł w `PROMPT_STARTOWY.md`;
- kompletność pięciu scenariuszy regresji;
- zachowanie reguły zamrożenia v1.0;
- rozdzielenie parkingu automatycznego runnera modeli od bieżącej kontroli repo.

## Granica

Ten walidator:

- nie uruchamia modeli AI;
- nie ocenia semantycznej jakości odpowiedzi modelu;
- nie zmienia PROMPT_STARTOWY.md — kanoniczny plik pozostaje zamrożony;
- nie zastępuje rzeczywistych testów rekonstrukcji;
- nie aktywuje pomysłów z `IDEA_ARCHIVE.md`.

GitHub Actions uruchamia kontrolę przy pull requestach i zmianach na `main`.

Pełny automatyczny runner testów promptu pozostaje osobnym pomysłem `PARKING`. Powrót do niego wymaga warunku zapisanego w `IDEA_ARCHIVE.md`.
