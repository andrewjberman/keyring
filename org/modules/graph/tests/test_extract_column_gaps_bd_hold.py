"""NFRA_TOOLPASS C0 (census-found reader #2, HIGHEST priority): extract_pipeline._extract_column_gaps
read a gold-script's CONTENT (read_text :994) with NO _held_path_hit guard -- UNLIKE every other read in
that module. It is the primitive comp-pipescript `io` invokes on gold scripts (pipeline_cli), so `io` read
bd gold-script SOURCE unguarded while `deployed` was guarded (COMP_PIPESCRIPT_INCLUDE_HELD) -- comp-pipescript
was HALF-guarded. FIX: skip a held bd/schwab path (return no column-gap findings), matching the module's
own _held_path_hit chokepoint contract.

bd-SAFE + hermetic: writes SYNTHETIC tmp files whose PATH STRING contains "data/black_diamond/" (that
substring is what _held_path_hit matches) -- it NEVER touches the real bd tree. Non-vacuous: identical
content at an inf path yields a column-gap finding (proves the read happens); at a bd path it returns []
(proves the guard skips before the read).

# rail-checked: assurance oracle for extract_pipeline._extract_column_gaps under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import os
import sys
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
if _WS not in sys.path:
    sys.path.insert(0, _WS)

from org.modules.graph import extract_pipeline as ep  # noqa: E402

# A gold-script with a real column gap: loads columns ['a','b'] but accesses 'missing_col'.
_SCRIPT = (
    "KEY = 's3://x/y.parquet'\n"
    "df = _load_parquet(KEY, columns=['a', 'b'])\n"
    "x = df['missing_col']\n"
)


def _write(dirpath: Path) -> Path:
    dirpath.mkdir(parents=True, exist_ok=True)
    f = dirpath / "fake_gold.py"
    f.write_text(_SCRIPT, encoding="utf-8")
    return f


def test_inf_path_reads_and_finds_the_gap_but_bd_path_is_skipped():
    with tempfile.TemporaryDirectory() as d:
        inf_file = _write(Path(d) / "data" / "inf" / "scripts" / "gold")
        bd_file = _write(Path(d) / "data" / "black_diamond" / "scripts" / "gold")
        inf_gaps = ep._extract_column_gaps(inf_file)
        bd_gaps = ep._extract_column_gaps(bd_file)
    # inf (not held): the read happens + the analyzer finds the gap -> non-empty (the read is real).
    assert inf_gaps, f"an inf gold path must be READ + analyzed (expect a column-gap finding): {inf_gaps}"
    # bd (held): the guard returns [] BEFORE the read, even though the file has the same gap. Non-vacuous.
    assert bd_gaps == [], f"a HELD bd gold path must be SKIPPED (guard) -> [] despite the same gap: {bd_gaps}"


def test_schwab_silver_path_also_skipped():
    with tempfile.TemporaryDirectory() as d:
        sch_file = _write(Path(d) / "data" / "canonical" / "schwab" / "silver")
        assert ep._extract_column_gaps(sch_file) == [], "a held schwab/silver path must be skipped too"


def test_include_held_override_reads_the_bd_gold_script():
    # C io-threading: comp-pipescript io passes include_held_override=include_held("COMP_PIPESCRIPT_INCLUDE_HELD"),
    # so a bd gold path IS read under the DS deploy/verify override -- the same finding the inf path yields.
    with tempfile.TemporaryDirectory() as d:
        bd_file = _write(Path(d) / "data" / "black_diamond" / "scripts" / "gold")
        skipped = ep._extract_column_gaps(bd_file)                            # default -> []
        read = ep._extract_column_gaps(bd_file, include_held_override=True)   # override -> reads
    assert skipped == [], f"default (no override) must still skip a held bd path: {skipped}"
    assert read, f"include_held_override=True must READ the bd gold script's column-gaps (non-vacuous): {read}"


if __name__ == "__main__":
    test_inf_path_reads_and_finds_the_gap_but_bd_path_is_skipped()
    print("PASS: inf path reads+finds the gap; held bd path is skipped ([]) -- guard non-vacuous")
    test_schwab_silver_path_also_skipped()
    print("PASS: held schwab/silver path skipped too")
    test_include_held_override_reads_the_bd_gold_script()
    print("PASS: include_held_override reads the bd gold script (io honors the lift like deployed)")
    print("=== extract_column_gaps bd-hold: ALL PASS ===")
