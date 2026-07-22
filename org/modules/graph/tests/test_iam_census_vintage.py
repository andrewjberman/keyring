#!/usr/bin/env python3
"""comp-iam APPLIED-plane vintage gate: does it REFUSE a stale/undated census AND ACCEPT a fresh one?

WHY THIS FILE EXISTS -- THE ASYMMETRY IT CLOSES
------------------------------------------------
The vintage gate was built 2026-07-22 and, at the moment work halted, it was verified to REFUSE the
shipped 2026-06-03 census (exit 3, loud) and NOT verified to ACCEPT a fresh one -- the fresh-census
control errored on an MSYS-vs-Windows path before it ever executed.

    A gate proven only on the deny side has never been asked a question it could answer YES to.
    It passes review looking exactly like a working control, and it is undiscriminating.

That is the same class as `comp-constants`' missing "the hold is OFF and that is correct" control on
the same day: every test asserted the guard FIRES, none asserted it stays SILENT when it should, so a
retraction had no expressible success state. Here the failure would be worse -- a gate that refuses
EVERY census silently converts the whole APPLIED plane into a permanent no-answer, which reads as
"comp-iam has no drift findings."

THE LOAD-BEARING TEST is test_refuse_and_accept_differ_ONLY_by_vintage: it runs the SAME census
content twice, differing in one field, and asserts the verdicts differ. A single-sided test cannot
distinguish "the gate works" from "the gate always refuses"; only the DIFFERENCE can.

Hermetic: no AWS, no network. `reconcile` parses local Terraform for the DESIRED plane and reads the
census from disk; nothing here calls IAM. The census fixtures are derived from the committed
2026-06-03 file so the content is real, and only the vintage is manipulated.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_GRAPH = _HERE.parent
_WS = _GRAPH.parent.parent.parent
_CLI = _GRAPH / "iam_cli.py"
_REAL_CENSUS = _WS / "docs/briefs/cmpaws-iam-axis-census-20260603.json"

sys.path.insert(0, str(_GRAPH))
import comp_iam_census as C  # noqa: E402

_ISO_Z = "%Y-%m-%dT%H:%M:%SZ"

REFUSED_EXIT = 3   # distinct from 0=clean and 1=drift-found, on purpose


def _run(*args):
    p = subprocess.run([sys.executable, str(_CLI), *args],
                       capture_output=True, text=True, timeout=300, cwd=str(_WS))
    return p.returncode, p.stdout, p.stderr


def _census_with_vintage(tmp_path, generated_utc, name):
    """The REAL committed census, re-stamped. Content held constant; only the vintage varies."""
    d = json.loads(_REAL_CENSUS.read_text(encoding="utf-8"))
    if generated_utc is None:
        d["_meta"].pop("generated_utc", None)
    else:
        d["_meta"]["generated_utc"] = generated_utc
        d["_meta"]["accounts_swept"] = 1
        d["_meta"]["scope"] = "single-account, customer roles (test fixture)"
    p = tmp_path / name
    p.write_text(json.dumps(d), encoding="utf-8")
    return p


@pytest.mark.skipif(not _REAL_CENSUS.exists(), reason="committed census fixture absent")
def test_refuse_and_accept_differ_ONLY_by_vintage(tmp_path):
    """THE discriminating test. Same census content; one field differs; verdicts must differ.

    Without this pair, "the gate refuses the stale census" is equally consistent with "the gate
    refuses everything" -- and the second is a silent outage of the entire APPLIED plane.
    """
    fresh = _census_with_vintage(
        tmp_path, (datetime.now(timezone.utc) - timedelta(hours=1)).strftime(_ISO_Z), "fresh.json")
    undated = _census_with_vintage(tmp_path, None, "undated.json")

    rc_u, out_u, _ = _run("reconcile", "--census", str(undated))
    rc_f, out_f, _ = _run("reconcile", "--census", str(fresh))

    assert rc_u == REFUSED_EXIT, f"undated census must REFUSE (exit {REFUSED_EXIT}); got {rc_u}\n{out_u}"
    assert rc_f != REFUSED_EXIT, (
        f"FRESH census must NOT be refused -- a gate that refuses everything is undiscriminating "
        f"and silently disables the APPLIED plane. got {rc_f}\n{out_f}")
    assert "REFUSED" in out_u and "REFUSED" not in out_f, "refused/accepted must differ on stdout alone"
    assert "IAM DESIRED-vs-LIVE RECONCILE" in out_f, "the fresh run must actually reconcile, not no-op"


@pytest.mark.skipif(not _REAL_CENSUS.exists(), reason="committed census fixture absent")
def test_stale_is_refused_and_names_the_TTL(tmp_path):
    stale = _census_with_vintage(
        tmp_path, (datetime.now(timezone.utc) - timedelta(days=30)).strftime(_ISO_Z), "stale.json")
    rc, out, _ = _run("reconcile", "--census", str(stale))
    assert rc == REFUSED_EXIT, f"30-day-old census must REFUSE; got {rc}\n{out}"
    assert "STALE" in out and "TTL" in out, "a refusal must say WHY and against what threshold"


@pytest.mark.skipif(not _REAL_CENSUS.exists(), reason="committed census fixture absent")
def test_refusal_is_loud_on_STDOUT_not_only_stderr(tmp_path):
    """A refusal must be visible to a caller reading stdout alone.

    Same defect class fixed in comp-constants hours earlier: a REFUSE that printed only to stderr
    left `out=$(...)` callers with a clean-empty result, so a refusal read as a pass.
    """
    undated = _census_with_vintage(tmp_path, None, "undated2.json")
    rc, out, _ = _run("reconcile", "--census", str(undated))
    assert rc == REFUSED_EXIT
    assert out.strip(), "REFUSE must be non-empty on stdout"
    assert "REFUSED" in out and "NOT PERFORMED" in out
    assert "not a clean result" in out, "the refusal must say it is a coverage refusal, not a pass"


@pytest.mark.skipif(not _REAL_CENSUS.exists(), reason="committed census fixture absent")
def test_override_reconciles_but_disclaims_authority(tmp_path):
    """--allow-stale-census must work AND must strip the verdict of APPLIED authority in the output.
    An override that is silent is just a hole; an override that announces itself is a decision."""
    undated = _census_with_vintage(tmp_path, None, "undated3.json")
    rc, out, _ = _run("reconcile", "--allow-stale-census", "--census", str(undated))
    assert rc != REFUSED_EXIT, "override must proceed"
    assert "OVERRIDE" in out and "NOT an APPLIED-plane authority" in out


def test_the_SHIPPED_census_is_the_thing_being_guarded_against():
    """Anchor on reality: the committed census really does lack a vintage. If someone later adds one,
    this test fails and tells them to re-point the fixture -- rather than the suite quietly passing
    against a file that no longer demonstrates the defect."""
    if not _REAL_CENSUS.exists():
        pytest.skip("committed census absent")
    d = json.loads(_REAL_CENSUS.read_text(encoding="utf-8"))
    assert (d.get("_meta") or {}).get("generated_utc") is None, (
        "the 2026-06-03 census now HAS a generated_utc -- good, but this fixture no longer "
        "demonstrates the undated case; re-point it at a synthetic undated census")
    assert C.census_freshness(d)[0] == C.NO_VINTAGE
