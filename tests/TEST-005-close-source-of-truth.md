# TEST-005 — Domknięcie źródła prawdy

## Materiał

Kilka dokumentów konkuruje o rolę źródła prawdy. Żaden nie jest w pełni aktualny.

## Ryzyko regresji

AI zaleca użytkownikowi wybrać plik albo zatwierdzić nieprzedstawiony `PROJECT_STATE.md`.

## PASS

- dokumenty są klasyfikowane jako `CURRENT`, `PARTIALLY CURRENT`, `SUPERSEDED`, `EVIDENCE ONLY` albo `UNKNOWN`;
- AI wskazuje najlepszego kandydata;
- gdy żaden dokument nie wystarcza, raport zawiera pełną sekcję I;
- następny krok może dotyczyć zatwierdzenia tylko pokazanego draftu;
- nierozstrzygalne konflikty mają oznaczenie `USER DECISION REQUIRED`.
