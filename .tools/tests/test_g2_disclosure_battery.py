#!/usr/bin/env python3
"""G2 disclosure battery -- NFRA_COMPEFFICACY CE-g-2, TO-CE-G-2, criterion G2-AC6.

Both `comp-blast` and `comp-trace` share ONE engine (`org/modules/graph/cli.py`) and now ONE
disclosure implementation (`_format_vintage_line` / `_vintage_dict`), fed by two per-tool
EXTRACTIONS (`_kuzu_vintage` for comp-blast's canonical kuzu DB; `_emit_trace_provenance`'s own
`_LOAD_PROVENANCE` read for comp-trace's local head-pinned TraceGraph). This battery exercises the
shared renderer directly (fresh / stale-served / unreadable-built / json-field arms -- fast, no
graph load) AND both real CLIs end-to-end (comp_trace / comp_blast arms -- bounded, `--budget 90`).

Each arm prints its own denominator. Each arm carries a RED MUTANT proving the arm actually
DISCRIMINATES (asserts the mutant FAILS the same check the real output PASSES) rather than merely
agreeing with itself -- the three defect classes the TO names: (1) today's block WITHOUT `built:`;
(2) a fabricated `age: 0.0h` on an UNREADABLE built (the "never a default" bar); (3) STALE-SERVED
silently omitted.

Run direct:  python .tools/tests/test_g2_disclosure_battery.py   -> prints PASS + denominator.
Run pytest:  pytest .tools/tests/test_g2_disclosure_battery.py   -> FILE-grain collection of the
                                                                     same `test_*` functions.

READ-ONLY TO THE SEAM (G2 bound): infra/aws/globgrph/_canonical.py, _provenance.py, kuzu_cli.py,
kuzu_nessie_load.py are never edited or monkeypatched here. The stale-served arm PLANTS a fixture
file in the seam's OWN on-disk schema (the `._refresh_status.json` marker `_write_refresh_failure`
writes) inside an isolated tempdir, then reads it back through the seam's OWN unedited public
reader (`_canonical.refresh_failure`) -- a fixture, not a mutation of the seam's code.
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[2]
_CLI_PATH = _WORKSPACE / "org" / "modules" / "graph" / "cli.py"
_GLOBGRPH = _WORKSPACE / "infra" / "aws" / "globgrph"

for _p in (str(_WORKSPACE), str(_WORKSPACE / ".tools"), str(_GLOBGRPH)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# The engine under test, loaded by PATH (never as `python -m ...`) so this battery runs the same
# whether invoked directly or under pytest, from any cwd.
_spec = importlib.util.spec_from_file_location("g2_cli_under_test", _CLI_PATH)
cli = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cli)

import _canonical as _canon  # noqa: E402 -- the seam's OWN reader, READ ONLY (never edited here)

_DENOMINATORS: dict[str, int] = {}
_VINTAGE_LINE_RX = re.compile(r"VINTAGE: DB:.*$", re.MULTILINE)


# --------------------------------------------------------------------------------- fixture writers
def _write_manifest(db_path: str, *, built_at, node_count, edge_count, source_kind="tarball") -> None:
    """The manifest schema `infra/aws/globgrph/_provenance.write_manifest` produces -- written
    directly (a fixture), never via calling the seam's writer, so this stays READ-ONLY to the seam."""
    m = {"schema_version": 1, "source_kind": source_kind, "source_vintage": {},
         "built_at": built_at, "node_count": node_count, "edge_count": edge_count}
    with open(db_path + "._build_manifest.json", "w", encoding="utf-8") as fh:
        json.dump(m, fh)


def _write_stale_marker(db_path: str, *, kind="inc-served-labeled-stale",
                        detail="behind-by-9001 nodes; served vintage 2026-01-01T00:00:00+00:00; mode=inc") -> None:
    """The SEAM'S OWN on-disk label schema (`_write_refresh_failure`, infra/aws/globgrph/
    _canonical.py) -- planted as a fixture in an isolated tempdir, read back through the seam's
    OWN unedited reader (`_canonical.refresh_failure`) below."""
    with open(db_path + "._refresh_status.json", "w", encoding="utf-8") as fh:
        json.dump({"failed_at_iso": datetime.now(timezone.utc).isoformat(),
                   "kind": kind, "detail": detail}, fh)


# --------------------------------------------------------------------------------- RED mutants
def _mutant_no_built(line: str) -> str:
    """Defect class 1: today's block WITHOUT `built:` -- what G2-AC1 measured before this order
    (comp-blast's multi-line provenance carried `built:` and `DB:` as SEPARATE lines; there was no
    single disclosure line at all)."""
    return re.sub(r"\s*built:.*?\(age:[^)]*\)", "", line)


def _mutant_zero_age_on_unread(db_name, nodes, edges) -> str:
    """Defect class 2: an unreadable built prints a FABRICATED age instead of UNKNOWN -- the exact
    'never a default' violation the TO bounds against."""
    return f"VINTAGE: DB: {db_name}  ({nodes} nodes / {edges} edges)  built: UNREAD (mutant) (age: 0.0h)"


def _mutant_omit_stale(line: str) -> str:
    """Defect class 3: STALE-SERVED silently dropped from an otherwise-correct line."""
    return re.sub(r"\s*STALE-SERVED:.*$", "", line)


# --------------------------------------------------------------------------------- arm 1: fresh
def test_fresh_arm():
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "fake_kuzu_db")
        built = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        _write_manifest(db_path, built_at=built, node_count=100, edge_count=200)
        # no ._refresh_status.json marker planted -> refresh_failure() reads genuinely ABSENT;
        # source_kind="tarball" skips the nessie-HEAD-behind check; age (1h) < DEFAULT_AGE_WARN_HOURS.
        fields = cli._kuzu_vintage(db_path)
        line = cli._format_vintage_line(**fields)

        assert re.search(r"built: \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \(age: \d+\.\d+h\)", line), line
        assert "UNREAD" not in line, line
        assert "STALE-SERVED" not in line, ("fresh arm must carry NO stale label", line)

        mutant = _mutant_no_built(line)
        assert "built:" not in mutant and "(age:" not in mutant, \
            ("RED mutant (no built:) failed to remove the clause -- arm cannot discriminate", mutant)
        _DENOMINATORS["fresh"] = 1
        print(f"OK fresh: real={line!r}")
        print(f"OK fresh: mutant(no-built)={mutant!r} (correctly fails the built:/age: check)")


# --------------------------------------------------------------------------------- arm 2: stale-served
def test_stale_served_arm():
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "fake_kuzu_db")
        built = (datetime.now(timezone.utc) - timedelta(hours=40)).isoformat()
        _write_manifest(db_path, built_at=built, node_count=100, edge_count=200)
        _write_stale_marker(db_path)

        # Read the planted fixture back through the SEAM'S OWN unedited public reader first --
        # proves the fixture is faithful to the seam's real schema, not just to our own reader.
        rf = _canon.refresh_failure(db_path)
        assert rf is not None and rf.get("kind") == "inc-served-labeled-stale", rf

        fields = cli._kuzu_vintage(db_path)
        assert fields["stale_served"] == "inc-served-labeled-stale", fields
        line = cli._format_vintage_line(**fields)
        assert "STALE-SERVED: inc-served-labeled-stale" in line, line

        mutant = _mutant_omit_stale(line)
        assert "STALE-SERVED" not in mutant, \
            ("RED mutant (omit STALE-SERVED) failed to remove the clause -- arm cannot discriminate", mutant)
        _DENOMINATORS["stale_served"] = 1
        print(f"OK stale_served: real={line!r}")
        print(f"OK stale_served: mutant(omit-stale)={mutant!r} (correctly fails the STALE-SERVED check)")


# --------------------------------------------------------------------------------- arm 3: unreadable built
def test_unreadable_built_arm():
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "fake_kuzu_db")
        _write_manifest(db_path, built_at="not-a-real-timestamp", node_count=5, edge_count=5)
        fields = cli._kuzu_vintage(db_path)
        assert fields["built_iso"] is None and fields["age_h"] is None, fields
        assert fields["unread_reason"], fields

        line = cli._format_vintage_line(**fields)
        assert "built: UNREAD (" in line, line
        assert "age: UNKNOWN" in line, line
        assert "age: 0.0h" not in line, line

        d = cli._vintage_dict(**fields)
        assert d["built"] is None and d["age_h"] is None, d
        assert d["built_unread_reason"], d

        mutant = _mutant_zero_age_on_unread(fields["db_name"], "5", "5")
        assert "age: 0.0h" in mutant and "age: UNKNOWN" not in mutant, \
            ("RED mutant (fabricated age on UNREAD) failed to fabricate -- arm cannot discriminate", mutant)
        _DENOMINATORS["unreadable_built"] = 1
        print(f"OK unreadable_built: real={line!r}")
        print(f"OK unreadable_built: mutant(zero-age)={mutant!r} (correctly fails the UNKNOWN check)")


# --------------------------------------------------------------------------------- arm 4: json field
def test_json_field_arm():
    healthy = cli._vintage_dict(db_name="x", nodes=1, edges=2, built_iso="2026-01-01T00:00:00Z", age_h=3.4)
    for key in ("db", "nodes", "edges", "built", "age_h", "stale_served"):
        assert key in healthy, (key, healthy)
    payload = json.dumps({"vintage": healthy})
    assert '"vintage"' in payload, payload

    # RED mutant: the pre-fix JSON shape (no vintage key at all) -- must fail the same check.
    mutant_payload = json.dumps({"other": "field"})
    assert '"vintage"' not in mutant_payload, \
        ("RED mutant (no vintage key) unexpectedly matched -- arm cannot discriminate", mutant_payload)
    _DENOMINATORS["json_field"] = 1
    print("OK json_field: real contains \"vintage\"; mutant correctly does not")


# --------------------------------------------------------------------------------- CLI runner
def _run_cli(subcommand: str, query: str, *extra: str, timeout_s: int = 110) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_CLI_PATH), subcommand, query, "--budget", "90", *extra],
        cwd=str(_WORKSPACE), capture_output=True, text=True, timeout=timeout_s,
    )


def _extract_vintage_line(combined: str) -> str:
    m = _VINTAGE_LINE_RX.search(combined)
    assert m, ("no VINTAGE: line in CLI output", combined[-2000:])
    return m.group(0)


# --------------------------------------------------------------------------------- arm 5: comp-trace CLI
def test_comp_trace_arm():
    r = _run_cli("trace", "AdvisorsTab.tsx")
    combined = r.stdout + r.stderr
    line = _extract_vintage_line(combined)
    assert re.search(r"built: .+ \(age: .+\)", line), line

    mutant = _mutant_no_built(line)
    assert "built:" not in mutant, \
        ("RED mutant (no built:) failed on the real comp-trace VINTAGE line", mutant)
    _DENOMINATORS["comp_trace_cli"] = 1
    print(f"OK comp_trace_cli: rc={r.returncode} line={line!r}")


# --------------------------------------------------------------------------------- arm 6: comp-blast CLI
def test_comp_blast_arm():
    r = _run_cli("blast", "component:AdvisorsTab.tsx")
    combined = r.stdout + r.stderr
    line = _extract_vintage_line(combined)
    assert re.search(r"built: .+ \(age: .+\)", line), line

    mutant = _mutant_no_built(line)
    assert "built:" not in mutant, \
        ("RED mutant (no built:) failed on the real comp-blast VINTAGE line", mutant)
    _DENOMINATORS["comp_blast_cli"] = 1
    print(f"OK comp_blast_cli: rc={r.returncode} line={line!r}")


_ALL_TESTS = [
    test_fresh_arm, test_stale_served_arm, test_unreadable_built_arm,
    test_json_field_arm, test_comp_trace_arm, test_comp_blast_arm,
]


def main() -> int:
    failures = []
    for t in _ALL_TESTS:
        try:
            t()
        except Exception as ex:  # noqa: BLE001 -- collect every arm's verdict, don't stop at the first
            failures.append((t.__name__, ex))
            print(f"FAIL: {t.__name__}: {ex}")
    print(f"DENOMINATOR: {len(_DENOMINATORS)} of {len(_ALL_TESTS)} arm(s) recorded a pass "
          f"({sorted(_DENOMINATORS)})")
    if failures:
        print(f"FAIL: {len(failures)} of {len(_ALL_TESTS)} arm(s) failed")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
