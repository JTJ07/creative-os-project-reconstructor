#!/usr/bin/env python3
"""Deterministyczna kontrola repozytorium Creative OS Project Reconstructor."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEST_FILES = [
    "tests/TEST-001-conversation-is-documentation.md",
    "tests/TEST-002-artifact-is-not-result.md",
    "tests/TEST-003-prerequisite-first.md",
    "tests/TEST-004-no-auto-activation.md",
    "tests/TEST-005-close-source-of-truth.md",
]

REQUIRED_FILES = [
    "README.md",
    "PROMPT_STARTOWY.md",
    "PROJECT_STATE.md",
    "EVOLUTION_LOG.md",
    "IDEA_ARCHIVE.md",
    "tests/README.md",
    "VALIDATION.md",
    ".github/pull_request_template.md",
] + TEST_FILES


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(relative_path: str) -> str:
    try:
        return (ROOT / relative_path).read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{relative_path} nie jest poprawnym UTF-8: {exc}")
    raise AssertionError("unreachable")


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("brak wymaganych plików: " + ", ".join(missing))
    print(f"[PASS] wymagane pliki: {len(REQUIRED_FILES)}")


def check_version_and_state() -> None:
    readme = read_text("README.md")
    state = read_text("PROJECT_STATE.md")

    if "v1.0 — STABILIZATION" not in readme:
        fail("README.md nie zachowuje wersji v1.0 — STABILIZATION")
    if "ACTIVE / V1.0 STABILIZATION" not in state:
        fail("PROJECT_STATE.md ma niespójny status")
    if "PROMPT_STARTOWY.md" not in readme or "PROMPT_STARTOWY.md" not in state:
        fail("kanoniczny prompt nie jest wskazany w README i PROJECT_STATE")
    if "Repozytorium jest prywatne" in readme or "Repozytorium pozostaje prywatne" in state:
        fail("dokumentacja utrwala zmienną właściwość widoczności repozytorium")
    print("[PASS] wersja, status i właściciel promptu są spójne")


def check_prompt_contract() -> None:
    prompt = read_text("PROMPT_STARTOWY.md")
    required_markers = [
        "Pracuj najpierw w trybie `READ_ONLY`",
        "## ETAP 1 — REKONSTRUKCJA PROJEKTU",
        "## ETAP 2 — OCENA SPOSOBU PRACY",
        "## ETAP 3 — AKTUALNY STAN",
        "## ETAP 4 — CREATIVE OS",
        "### A. MODEL DZIAŁANIA PROJEKTU",
        "### I. REKOMENDOWANY MINIMALNY `PROJECT_STATE.md`",
        "`EXISTING ARTIFACT`",
        "`EXECUTABLE MECHANISM`",
        "`OBSERVED WORKING RESULT`",
        "`VALIDATED RESULT`",
        "PROPOSED — REQUIRES USER APPROVAL",
        "## ZASADA DOMKNIĘCIA ŹRÓDŁA PRAWDY",
        "Nie twórz brancha, commitu ani PR",
    ]
    for marker in required_markers:
        if marker not in prompt:
            fail(f"PROMPT_STARTOWY.md nie zawiera wymaganej reguły: {marker}")

    if len(prompt.splitlines()) < 350:
        fail("PROMPT_STARTOWY.md jest podejrzanie skrócony")
    print("[PASS] kontrakt promptu v1.0 jest kompletny")


def check_regression_tests() -> None:
    test_index = read_text("tests/README.md")
    if "Globalne kryteria" not in test_index:
        fail("tests/README.md nie zawiera globalnych kryteriów")

    for path in TEST_FILES:
        content = read_text(path)
        if "## PASS" not in content:
            fail(f"{path} nie zawiera kryteriów PASS")
        if "## Ryzyko regresji" not in content:
            fail(f"{path} nie opisuje ryzyka regresji")
    print(f"[PASS] testy regresji: {len(TEST_FILES)} scenariuszy")


def check_evolution_and_parking() -> None:
    evolution = read_text("EVOLUTION_LOG.md")
    ideas = read_text("IDEA_ARCHIVE.md")

    required_evolution = [
        "EVOLUTION-001",
        "EVOLUTION-008",
        "EVOLUTION-009",
        "wersja `v1.0` zostaje zamrożona",
    ]
    for marker in required_evolution:
        if marker not in evolution:
            fail(f"EVOLUTION_LOG.md nie zawiera: {marker}")

    if ideas.count("## IDEA-") < 6:
        fail("IDEA_ARCHIVE.md nie zachowuje pełnego parkingu v1.0")
    if "Automatyczny runner testów promptu" not in ideas:
        fail("IDEA_ARCHIVE.md nie zachowuje oddzielonego runnera modeli")
    print("[PASS] ewolucja i parking są zabezpieczone")


def check_validation_boundary() -> None:
    validation = read_text("VALIDATION.md")
    required = [
        "python scripts/verify_reconstructor.py",
        "deterministyczny",
        "nie uruchamia modeli AI",
        "nie zmienia PROMPT_STARTOWY.md",
        "GitHub Actions",
        "lekkiego filtra PR",
        "zwykłej zmiany technicznej",
    ]
    for marker in required:
        if marker not in validation:
            fail(f"VALIDATION.md nie zawiera granicy: {marker}")
    print("[PASS] walidator jest oddzielony od runnera modeli i promptu")


def check_pull_request_filter() -> None:
    template = read_text(".github/pull_request_template.md")
    required = [
        "Konkretna porażka lub regresja",
        "Dlaczego obecny mechanizm nie wystarcza",
        "Obserwowalny dowód zaliczenia",
        "Test regresji",
        "Dodany koszt utrzymania",
        "Poza zakresem",
        "BRAK ZMIANY PROMPTU",
    ]
    for marker in required:
        if marker not in template:
            fail(f"szablon PR nie zawiera filtra: {marker}")
    print("[PASS] filtr PR wymaga dowodu przy zmianie promptu bez narzutu dla poprawek technicznych")


def main() -> None:
    check_required_files()
    check_version_and_state()
    check_prompt_contract()
    check_regression_tests()
    check_evolution_and_parking()
    check_validation_boundary()
    check_pull_request_filter()
    print("[PASS] Project Reconstructor v1.0 jest spójny na poziomie repozytorium")


if __name__ == "__main__":
    main()
