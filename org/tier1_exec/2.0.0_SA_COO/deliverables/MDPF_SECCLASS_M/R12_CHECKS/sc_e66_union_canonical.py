#!/usr/bin/env python3
"""sc_e66_union_canonical.py -- MDPF_SECCLASS round 11 SC-e-66 (row W41-S4): the BD silver assets dim's scheduled union path
writes the canonical class columns.

READ-ONLY, no AWS, text read. data/black_diamond/scripts/silver/build_bd_assets_dim.py's build_union_dim() body must name
asset_class_canonical, sub_asset_class_canonical and class_source, and must no longer assert that the union keeps the
current dim's column set unchanged. Prints SC-E66 ok=<bool>. Run from the repo root you are grading.
"""
import ast
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
SRC = ROOT / "data/black_diamond/scripts/silver/build_bd_assets_dim.py"
COLS = ("asset_class_canonical", "sub_asset_class_canonical", "class_source")


def main():
    text = SRC.read_text(encoding="utf-8")
    fn = next((n for n in ast.walk(ast.parse(text)) if isinstance(n, ast.FunctionDef) and n.name == "build_union_dim"), None)
    if fn is None:
        print("SC-E66 ok=False reason=no build_union_dim")
        return 1
    body = ast.get_source_segment(text, fn) or ""
    named = [c for c in COLS if c in body]
    frozen = "len(out.columns) == len(dim.columns)" in body
    ok = len(named) == len(COLS) and not frozen
    print(f"SC-E66 ok={ok} canonical_cols_named={len(named)}/{len(COLS)} column_set_frozen_assert={frozen}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
