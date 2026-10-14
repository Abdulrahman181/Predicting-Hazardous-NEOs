"""Fast repository checks that do not require the external NEO CSV."""

from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from neos_pipeline import resolve_data_path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_missing_dataset_has_actionable_error(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError, match="NEO data file not found"):
        resolve_data_path(missing)


def test_notebook_code_cells_parse_and_have_no_stale_outputs() -> None:
    notebook_path = REPO_ROOT / "Project_NEOs.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    assert notebook["nbformat"] >= 4
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell.get("source", []))
            ast.parse(source)
            assert cell.get("outputs", []) == []
            assert cell.get("execution_count") is None


def test_required_project_files_exist() -> None:
    for relative_path in ("README.md", "requirements.txt", "neos_pipeline.py", "ENGINEERING_REVIEW.md"):
        assert (REPO_ROOT / relative_path).is_file()
