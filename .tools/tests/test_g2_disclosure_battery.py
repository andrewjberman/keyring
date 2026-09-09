#!/usr/bin/env python3
"""G2 disclosure battery -- NFRA_COMPEFFICACY CE-g-2 (TO-CE-G-2, criterion G2-AC6), REPOINTED to the
SERVED cloud graph by NFRA_CLDGRPH TO-CG-D-7 (CG-s-8, R7 -- the retirement of the local copy).

WHAT CARRIED AND WHAT CHANGED. Both `comp-blast` and `comp-trace` still share ONE engine
(`org/modules/graph/cli.py`) and the disclosure is still ONE line per answer. What moved is the
SOURCE feeding comp-blast's half: it used to be the LOCAL canonical kuzu DB (its
`_build_manifest.json` for the age, and the rebuild seam's own `._refresh_status.json` marker for a
`STALE-SERVED:` label). TO-CG-D-7 retired the local DB and removed that seam, so comp-blast's
extraction is now `cli._served_vintage`, fed by the SERVICE's own response fields, and rendered by
`cli._format_served_vintage_line` / `cli._served_vintage_dict`. comp-trace's half is UNCHANGED: its
universe is still a local head-pinned TraceGraph cache, so it still reports `VINTAGE: DB: ...
built: ... (age: ...)` through `_format_vintage_line` / `_vintage_dict`, and this battery still
exercises that renderer directly.

THE STALE-SERVED ARM IS REPOINTED, NOT DELETED SILENTLY. On a served graph the pointer IS the
vintage: the service installs a generation atomically and hands every caller that generation, so
there is no state in which a caller is served one vintage while a fresher one is withheld. A
`STALE-SERVED:` field on that surface could never be populated, and a disclosure field that can
never fire is a false reassurance rather than a disclosure. So arm 2 now asserts the ABSENCE is
deliberate AND discriminating: the real renderer never emits the label, and a RED mutant that DOES
emit one fails the same check -- which is what keeps this from being a vacuous pass.

NO NETWORK IN TESTS. Arms 1-4 feed `_served_vintage` a STUBBED service payload (a dict in the same
shape `projection_client.query` returns). Nothing here calls the gateway, reads a secret, or opens
a database -- there is no database left to open. Arms 5-6 run the real CLIs end-to-end, bounded at
`--budget 90`; arm 6 is the one arm that does reach the served graph, because "the tool still
answers" is the property it exists to measure.

Each arm prints its own denominator. Each arm carries a RED MUTANT proving the arm actually
DISCRIMINATES (asserts the mutant FAILS the same check the real output PASSES) rather than merely
agreeing with itself -- the three defect classes the original TO names: (1) a block WITHOUT the
age sentence; (2) a fabricated age on an UNREADABLE vintage (the "never a default" bar); (3) a
disclosure field silently dropped.

Run direct:  python .tools/tests/test_g2_disclosure_battery.py   -> prints PASS + denominator.
Run pytest:  pytest .tools/tests/test_g2_disclosure_battery.py   -> FILE-grain collection of the
                                                                     same `test_*` functions.

READ-ONLY TO THE CLOUD ENGINE (the CG-s-8 bound): infra/aws/globgrph/kuzu_nessie_load.py,
kuzu_incremental_refresh.py, projection_server.py and projection_worker.py are never edited,
imported or monkeypatched here.
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

for _p in (str(_WORKSPACE), str(_WORKSPACE / ".tools"), str(_GLOBGRPH),
           str(_WORKSPACE / "org" / "modules" / "graph")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# The engine under test, loaded by PATH (never as `python -m ...`) so this battery runs the same
# whether invoked directly or under pytest, from any cwd.
_spec = importlib.util.spec_from_file_location("g2_cli_under_test", _CLI_PATH)
cli = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cli)

_DENOMINATORS: dict[str, int] = {}
# comp-trace's line (local head-pinned cache -- unchanged by CG-s-8).
_TRACE_VINTAGE_RX = re.compile(r"VINTAGE: DB:.*$", re.MULTILINE)
# comp-blast's line (served graph). The service's own sentence leads; the identifiers trail.
_SERVED_VINTAGE_RX = re.compile(r"VINTAGE: (?:Built from the estate as of|UNREAD).*$", re.MULTILINE)


# --------------------------------------------------------------------------------- fixture writers
def _served_payload(*, vintage, age_line, manifest="a" * 64, prefix=None, nodes=100, edges=200):
    """A stubbed service response in the shape `projection_client.query` returns, plus the two
    counts the universe load measures. This is a FIXTURE, not a call: no gateway, no secret, no
    database. Written here rather than imported from the client so a client refactor cannot make
    this battery agree with a broken shape by construction."""
    return {
        "vintage": vintage,
        "age_line": age_line,
        "manifest_sha256": manifest,
        "artifact_prefix": prefix or ("projection/%s/" % vintage),
        "nodes": nodes,
        "edges": edges,
    }


def _age_sentence(dt) -> str:
    """The service's own sentence shape (projection_server builds it from the manifest's
    committed_at). Reproduced here as a fixture value, never recomputed from a client clock."""
    return "Built from the estate as of %s UTC." % dt.strftime("%Y-%m-%d %H:%M:%S")


# --------------------------------------------------------------------------------- RED mutants
def _mutant_no_age(line: str) -> str:
    """Defect class 1: the disclosure WITHOUT its age sentence -- what G2-AC1 measured before the
    original order (provenance carried the facts on separate lines; there was no single line)."""
    return re.sub(r"Built from the estate as of[^\[]*", "", line)


def _mutant_fabricated_age(nodes, edges) -> str:
    """Defect class 2: an unreadable vintage renders a FABRICATED age instead of UNREAD -- the
    exact 'never a default' violation the TO bounds against."""
    return ("VINTAGE: Built from the estate as of 1970-01-01 00:00:00 UTC.  "
            "[vintage=1970-01-01T00:00:00+00:00 manifest=000000000000 nodes=%s edges=%s]"
            % (nodes, edges))


def _mutant_invents_stale(line: str) -> str:
    """Defect class 3, INVERTED for the served surface: a renderer that appends a STALE-SERVED
    label the served graph can never be in. The real line must not carry one; this must."""
    return line + "  STALE-SERVED: inc-served-labeled-stale"


# --------------------------------------------------------------------------------- arm 1: fresh
def test_fresh_arm():
    built = datetime.now(timezone.utc) - timedelta(hours=1)
    served = _served_payload(vintage=built.isoformat(), age_line=_age_sentence(built))
    fields = cli._served_vintage(served)
    line = cli._format_served_vintage_line(**fields)

    assert re.search(r"VINTAGE: Built from the estate as of \d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC\.",
                     line), line
    assert "UNREAD" not in line, line
    assert "nodes=100" in line and "edges=200" in line, line
    assert "manifest=aaaaaaaaaaaa" in line, ("the identifier must be the first 12 hex", line)

    mutant = _mutant_no_age(line)
    assert "Built from the estate as of" not in mutant, \
        ("RED mutant (no age sentence) failed to remove the clause -- arm cannot discriminate",
         mutant)
    _DENOMINATORS["fresh"] = 1
    print("OK fresh: real=%r" % line)
    print("OK fresh: mutant(no-age)=%r (correctly fails the age-sentence check)" % mutant)


# ------------------------------------------------------------------------- arm 2: no stale-served
def test_no_stale_served_arm():
    """The REPOINTED stale-served arm. A served graph cannot be labeled-stale, so the property under
    test inverted: the renderer must NEVER emit the label, and a mutant that does must fail."""
    old = datetime.now(timezone.utc) - timedelta(hours=40)
    served = _served_payload(vintage=old.isoformat(), age_line=_age_sentence(old))
    fields = cli._served_vintage(served)
    line = cli._format_served_vintage_line(**fields)
    d = cli._served_vintage_dict(**fields)

    assert "stale_served" not in fields, \
        ("the served extraction must not carry a field it can never populate", fields)
    assert "stale_served" not in d, d
    assert "STALE-SERVED" not in line, line
    # An OLD vintage is still fully disclosed -- removing the label must not remove the age.
    assert _age_sentence(old) in line, ("age must still be disclosed on an old vintage", line)

    mutant = _mutant_invents_stale(line)
    assert "STALE-SERVED" in mutant, \
        ("RED mutant (invented STALE-SERVED) failed to add the label -- arm cannot discriminate",
         mutant)
    _DENOMINATORS["no_stale_served"] = 1
    print("OK no_stale_served: real=%r" % line)
    print("OK no_stale_served: mutant(invented-stale)=%r (correctly fails the no-label check)"
          % mutant)


# --------------------------------------------------------------------------------- arm 3: unread
def test_unreadable_vintage_arm():
    served = _served_payload(vintage=None, age_line=None, nodes=5, edges=5)
    fields = cli._served_vintage(served)
    assert fields["vintage"] is None and fields["age_line"] is None, fields
    assert fields["unread_reason"], fields

    line = cli._format_served_vintage_line(**fields)
    assert "UNREAD (" in line, line
    assert "Built from the estate as of" not in line, line
    assert "vintage=UNREAD" in line, line

    d = cli._served_vintage_dict(**fields)
    assert d["vintage"] is None and d["age_line"] is None, d
    assert d["vintage_unread_reason"], d

    mutant = _mutant_fabricated_age(5, 5)
    assert "Built from the estate as of" in mutant and "UNREAD" not in mutant, \
        ("RED mutant (fabricated vintage on UNREAD) failed to fabricate -- arm cannot discriminate",
         mutant)
    _DENOMINATORS["unreadable_vintage"] = 1
    print("OK unreadable_vintage: real=%r" % line)
    print("OK unreadable_vintage: mutant(fabricated)=%r (correctly fails the UNREAD check)" % mutant)


# --------------------------------------------------------------------------------- arm 4: json field
def test_json_field_arm():
    built = datetime.now(timezone.utc)
    served = _served_payload(vintage=built.isoformat(), age_line=_age_sentence(built))
    healthy = cli._served_vintage_dict(**cli._served_vintage(served))
    for key in ("graph", "nodes", "edges", "vintage", "age_line", "manifest_sha256",
                "artifact_prefix"):
        assert key in healthy, (key, healthy)
    payload = json.dumps({"vintage": healthy})
    assert '"vintage"' in payload, payload

    # RED mutant: the pre-fix JSON shape (no vintage key at all) -- must fail the same check.
    mutant_payload = json.dumps({"other": "field"})
    assert '"vintage"' not in mutant_payload, \
        ("RED mutant (no vintage key) unexpectedly matched -- arm cannot discriminate",
         mutant_payload)
    _DENOMINATORS["json_field"] = 1
    print('OK json_field: real contains "vintage"; mutant correctly does not')


# ------------------------------------------------------------- arm 5: no local DB is reachable
def test_no_local_db_arm():
    """CG-s-8's own bound, exercised: the universe loader REFUSES a local database path instead of
    quietly answering from somewhere else. A tempdir path is used so this cannot pass by accident on
    a machine that happens to still carry the retired directory."""
    import comp_blast_universe as bu   # noqa: PLC0415 -- the engine's own module, by path

    with tempfile.TemporaryDirectory() as td:
        bogus = os.path.join(td, "kuzu_nessie_db")
        raised = None
        try:
            bu.load_kuzu_universe(db_path=bogus, refresh=False)
        except bu.KuzuUnavailable as ex:
            raised = str(ex)
        assert raised is not None, "a local db_path must be REFUSED, not silently substituted"
        assert "RETIRED" in raised.upper(), raised
    _DENOMINATORS["no_local_db"] = 1
    print("OK no_local_db: refusal=%r" % raised)


# --------------------------------------------------------------------------------- CLI runner
def _run_cli(subcommand: str, query: str, *extra: str, timeout_s: int = 110):
    return subprocess.run(
        [sys.executable, str(_CLI_PATH), subcommand, query, "--budget", "90", *extra],
        cwd=str(_WORKSPACE), capture_output=True, text=True, timeout=timeout_s,
    )


def _extract(rx, combined: str) -> str:
    m = rx.search(combined)
    assert m, ("no VINTAGE: line in CLI output", combined[-2000:])
    return m.group(0)


# --------------------------------------------------------------------------------- arm 6: comp-trace CLI
def test_comp_trace_arm():
    r = _run_cli("trace", "AdvisorsTab.tsx")
    combined = r.stdout + r.stderr
    line = _extract(_TRACE_VINTAGE_RX, combined)
    assert re.search(r"built: .+ \(age: .+\)", line), line

    mutant = re.sub(r"\s*built:.*?\(age:[^)]*\)", "", line)
    assert "built:" not in mutant, \
        ("RED mutant (no built:) failed on the real comp-trace VINTAGE line", mutant)
    _DENOMINATORS["comp_trace_cli"] = 1
    print("OK comp_trace_cli: rc=%s line=%r" % (r.returncode, line))


# --------------------------------------------------------------------------------- arm 7: comp-blast CLI
def test_comp_blast_arm():
    r = _run_cli("blast", "component:AdvisorsTab.tsx")
    combined = r.stdout + r.stderr
    line = _extract(_SERVED_VINTAGE_RX, combined)
    assert "Built from the estate as of" in line, line
    assert "vintage=" in line and "manifest=" in line, line
    assert "DB: kuzu_nessie_db" not in combined, \
        ("comp-blast must not name a local database anywhere in its output", line)

    mutant = _mutant_no_age(line)
    assert "Built from the estate as of" not in mutant, \
        ("RED mutant (no age sentence) failed on the real comp-blast VINTAGE line", mutant)
    _DENOMINATORS["comp_blast_cli"] = 1
    print("OK comp_blast_cli: rc=%s line=%r" % (r.returncode, line))


_ALL_TESTS = [
    test_fresh_arm, test_no_stale_served_arm, test_unreadable_vintage_arm,
    test_json_field_arm, test_no_local_db_arm, test_comp_trace_arm, test_comp_blast_arm,
]


def main() -> int:
    failures = []
    for t in _ALL_TESTS:
        try:
            t()
        except Exception as ex:  # noqa: BLE001 -- collect every arm's verdict, don't stop at the first
            failures.append((t.__name__, ex))
            print("FAIL: %s: %s" % (t.__name__, ex))
    print("DENOMINATOR: %d of %d arm(s) recorded a pass (%s)"
          % (len(_DENOMINATORS), len(_ALL_TESTS), sorted(_DENOMINATORS)))
    if failures:
        print("FAIL: %d of %d arm(s) failed" % (len(failures), len(_ALL_TESTS)))
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
