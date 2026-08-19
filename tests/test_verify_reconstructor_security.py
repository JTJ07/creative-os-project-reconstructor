from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "verify_reconstructor.py"

spec = importlib.util.spec_from_file_location("verify_reconstructor", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load verifier")
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class ValidatorRepositoryBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root_tmp = tempfile.TemporaryDirectory()
        self.outside_tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.root_tmp.name)
        self.outside = Path(self.outside_tmp.name)
        self.original_root = verifier.ROOT
        verifier.ROOT = self.root

    def tearDown(self) -> None:
        verifier.ROOT = self.original_root
        self.root_tmp.cleanup()
        self.outside_tmp.cleanup()

    def test_regular_file_inside_root_is_allowed(self) -> None:
        path = self.root / "README.md"
        path.write_text("safe\n", encoding="utf-8")
        self.assertEqual(verifier.regular_repository_file("README.md"), path.resolve())

    def test_required_file_symlink_outside_root_is_blocked(self) -> None:
        outside = self.outside / "secret.md"
        outside.write_text("outside\n", encoding="utf-8")
        (self.root / "README.md").symlink_to(outside)
        with self.assertRaises(SystemExit):
            verifier.regular_repository_file("README.md")

    def test_hardlinked_required_file_is_blocked(self) -> None:
        source = self.root / "source.md"
        source.write_text("shared inode\n", encoding="utf-8")
        os.link(source, self.root / "README.md")
        with self.assertRaises(SystemExit):
            verifier.regular_repository_file("README.md")


if __name__ == "__main__":
    unittest.main()
