"""
Regression: comp-trace / comp-blast / comp-xref NOT-FOUND must be LOUD (rc != 0).

Root cause (3.0.0_SA_CVO 2026-06-26, comp-tools duress sweep):
cli.py cmd_trace / cmd_blast / _xref_symbol_lookup exited 0 ("No nodes matching: X")
when the query resolved to ZERO graph nodes. On these Rule-20 change-safety gates
("what breaks if I change X?", "what's upstream/downstream?", "where is this symbol
referenced?") a TYPO'd or wrong target then reads identically to a verified
"nothing depends on this" clear -- a FALSE-CLEAR. An agent running
`comp-blast my_scriptt` (typo) saw rc=0 + empty output and could conclude the change
was safe. This is the same false-green shape as the cot mtime-not-content and the
comp-iam collision: a verdict returned ABOVE its actual grounding.

Fix: a query that resolves to zero nodes exits 3 (NOT-FOUND, distinct from argparse's
usage-2 and operational-error-1) and prints a NOT-FOUND marker to stderr. A SUCCESSFUL
match that legitimately has zero upstream/downstream results still exits 0 -- that is a
real "nothing breaks" answer and must stay quiet.

CTO standing lens applied: this exercises ADVERSARIAL input (a guaranteed-nonexistent
target), not just a canonical happy-path query, AND a positive control (a real node id
pulled live from the graph) so found-with-results still clears rc=0.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve()
_GRAPH_DIR = _HERE.parents[1]            # org/modules/graph
_CLI = _GRAPH_DIR / "cli.py"

_GARBAGE = "__nonexistent_zzz_target_no_node_has_this__"


def _run(subcmd: str, query: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_CLI), subcmd, query],
        capture_output=True, text=True, cwd=str(_GRAPH_DIR.parents[2]),
    )


def _a_real_node_id() -> str:
    """Pull a real node id live from the built graph (robust to graph changes)."""
    sys.path.insert(0, str(_GRAPH_DIR))
    from cli import _get_graph  # noqa: E402

    g = _get_graph()
    assert g.nodes, "graph has zero nodes -- cannot run positive control"
    return next(iter(g.nodes))


@pytest.mark.parametrize("subcmd", ["trace", "blast", "xref"])
def test_notfound_target_is_loud_rc_nonzero(subcmd):
    """A garbage target must exit NON-ZERO (the false-clear regression)."""
    r = _run(subcmd, _GARBAGE)
    assert r.returncode != 0, (
        f"comp-{subcmd} on a nonexistent target returned rc=0 (FALSE-CLEAR): "
        f"a typo reads as a verified 'nothing breaks/depends' clear.\n"
        f"stdout={r.stdout!r}\nstderr={r.stderr!r}"
    )
    assert r.returncode == 3, f"expected the dedicated NOT-FOUND code 3, got {r.returncode}"
    assert "NOT-FOUND" in (r.stdout + r.stderr).upper() or "NO MATCHES" in (r.stdout + r.stderr).upper()


@pytest.mark.parametrize("subcmd", ["trace", "blast", "xref"])
def test_real_node_still_clears_rc_zero(subcmd):
    """A SUCCESSFUL match (even with zero up/down results) must still exit 0 --
    the fix must not break the legitimate 'found, nothing breaks' answer."""
    real = _a_real_node_id()
    r = _run(subcmd, real)
    assert r.returncode == 0, (
        f"comp-{subcmd} on a REAL node '{real}' returned rc={r.returncode} -- the "
        f"NOT-FOUND fix wrongly fired on a found node.\nstderr={r.stderr!r}"
    )
