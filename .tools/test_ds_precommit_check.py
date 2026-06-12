#!/usr/bin/env python3
"""
Test runner for .tools/ds-precommit-check.py rule family.

Silver ID dtype enforcement (ADVI_INFNNA.ID-DTYPE-ENFORCEMENT AC2):
  PASS  — build_* calls coerce_silver_ids before return        -> 0 blocks, 0 warns
  FAIL1 — build_* returns DataFrame, no coerce call            -> >=1 block
  FAIL2 — build_* calls astype(str) on *_id column            -> >=1 warn

AST-DEDUP CLASS-N detector (ADHC_GLDINC.AST-DEDUP):
  FIRE   — completion-order append -> concat -> order-sensitive dedup  -> >=1 finding
  SILENT — index-slot assembly (CLASS-I)                              -> 0 findings
  SILENT — sort_values chained before drop_duplicates                 -> 0 findings
  SILENT — dedup on an unrelated lookup dim (no data-flow link)       -> 0 findings

Exit 0 if all assertions hold; exit 1 with details on any failure.
"""
from __future__ import annotations

import ast
import pathlib
import sys

# Add .tools/ to path so we can import ds-precommit-check as a module.
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import importlib
import importlib.util

_spec = importlib.util.spec_from_file_location(
    'ds_precommit_check',
    pathlib.Path(__file__).parent / 'ds-precommit-check.py',
)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
check_silver_id_dtype = _mod.check_silver_id_dtype
check_completion_order_dedup = _mod.check_completion_order_dedup

FIXTURE_DIR = pathlib.Path(__file__).parent / 'test_fixtures' / 'ds-precommit-check'
# Spoof the filepath so path-pattern check fires as if fixtures are real silver scripts.
_FAKE_SILVER_PATH = 'data/test/scripts/silver/fixture.py'
# Spoof a gold path so the AST-DEDUP path-pattern check fires (_ASTDEDUP_PATTERNS).
_FAKE_GOLD_PATH = 'data/test/scripts/gold/fixture.py'


def _run(fixture_name: str) -> tuple[list[str], list[str]]:
    src = (FIXTURE_DIR / fixture_name).read_text(encoding='utf-8')
    tree = ast.parse(src)
    return check_silver_id_dtype(src, tree, _FAKE_SILVER_PATH)


def _run_astdedup(fixture_name: str) -> list[str]:
    src = (FIXTURE_DIR / fixture_name).read_text(encoding='utf-8')
    tree = ast.parse(src)
    return check_completion_order_dedup(tree, _FAKE_GOLD_PATH)


def main() -> int:
    results = []

    # Case 1: PASS — no blocks, no warns
    blocks, warns = _run('silver_id_dtype_pass.py')
    ok = len(blocks) == 0 and len(warns) == 0
    results.append(('PASS fixture (no errors expected)', ok,
                    f'blocks={blocks} warns={warns}'))

    # Case 2: FAIL — missing coerce_silver_ids in DataFrame-returning build_*
    blocks, warns = _run('silver_id_dtype_fail_coerce.py')
    ok = len(blocks) >= 1
    results.append(('FAIL fixture: missing coerce (>=1 block expected)', ok,
                    f'blocks={blocks}'))

    # Case 3: FAIL — astype(str) on *_id column
    blocks, warns = _run('silver_id_dtype_fail_astype.py')
    ok = len(warns) >= 1
    results.append(('FAIL fixture: astype regression (>=1 warn expected)', ok,
                    f'warns={warns}'))

    # --- AST-DEDUP (ADHC_GLDINC.AST-DEDUP) CLASS-N detector ---
    # Case 4: FIRE — completion-order append -> concat -> order-sensitive dedup (A_01/A_04 pre-fix shape)
    msgs = _run_astdedup('astdedup_fire_completion_order.py')
    ok = len(msgs) >= 1
    results.append(('AST-DEDUP FIRE fixture: completion-order build (>=1 finding expected)', ok,
                    f'msgs={msgs}'))

    # Case 5: SILENT — index-slot assembly is deterministic (A_04 post-fix shape)
    msgs = _run_astdedup('astdedup_silent_index_slot.py')
    ok = len(msgs) == 0
    results.append(('AST-DEDUP SILENT fixture: index-slot CLASS-I (0 findings expected)', ok,
                    f'msgs={msgs}'))

    # Case 6: SILENT — sort_values chained before drop_duplicates (A_01 post-fix shape)
    msgs = _run_astdedup('astdedup_silent_sort_guarded.py')
    ok = len(msgs) == 0
    results.append(('AST-DEDUP SILENT fixture: sort-guarded dedup (0 findings expected)', ok,
                    f'msgs={msgs}'))

    # Case 7: SILENT — dedup is on an unrelated lookup dim, not the concat frame (C_02 FP shape)
    msgs = _run_astdedup('astdedup_silent_unrelated_dedup.py')
    ok = len(msgs) == 0
    results.append(('AST-DEDUP SILENT fixture: unrelated-dedup no-dataflow (0 findings expected)', ok,
                    f'msgs={msgs}'))

    all_pass = True
    for label, ok, detail in results:
        status = 'PASS' if ok else 'FAIL'
        print(f'{status}: {label}')
        if not ok:
            print(f'  detail: {detail}')
            all_pass = False

    if all_pass:
        print(f'All {len(results)} fixture assertions PASS.')
        return 0
    else:
        print('One or more fixture assertions FAILED.')
        return 1


if __name__ == '__main__':
    sys.exit(main())
