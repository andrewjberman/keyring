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


# ---------------------------------------------------------------------------
# CVO verify @da7478839 -- F1/F2/F3 regression locks.
# ---------------------------------------------------------------------------

@pytest.mark.skipif(not _REAL_CENSUS.exists(), reason="committed census fixture absent")
def test_F1_future_dated_census_is_REFUSED_not_treated_as_fresh(tmp_path):
    """A future-dated census must REFUSE, not read as very fresh.

    Before the fix, `FRESH if age <= ttl` meant pushing the date FORWARD made a census read FRESHER,
    so any stale census became authoritative via a one-field edit -- while the sanctioned override
    (--allow-stale-census) is audited and stamps the verdict non-authoritative.
    A CONTROL WHOSE BYPASS IS CHEAPER THAN ITS OVERRIDE CHANNELS BEHAVIOUR TOWARD THE BYPASS.
    """
    fut = _census_with_vintage(
        tmp_path, (datetime.now(timezone.utc) + timedelta(hours=48)).strftime(_ISO_Z), "future.json")
    rc, out, _ = _run("reconcile", "--census", str(fut))
    assert rc == REFUSED_EXIT, f"future-dated census must REFUSE; got {rc} :: {out}"
    assert "FUTURE" in out and "IMPOSSIBLE" in out
    # the refusal must name the ACTUAL reason -- calling it STALE is the record-one-notch-off defect
    assert "dated in the FUTURE" in out, "the refusal must not misreport a FUTURE census as STALE"


def test_F1_clock_skew_tolerated_but_impossible_is_not():
    """The boundary: minutes of skew are real, hours are not. Without this the fix would refuse
    healthy runs on a slightly-fast clock -- trading a false-accept for a false-refuse."""
    now = datetime(2026, 7, 22, 20, 0, 0, tzinfo=timezone.utc)
    def cen(dt):
        return {"_meta": {"generated_utc": dt.strftime(_ISO_Z)}, "roles": []}
    assert C.census_freshness(cen(now + timedelta(minutes=5)), now=now)[0] == C.FRESH
    assert C.census_freshness(cen(now + timedelta(hours=48)), now=now)[0] == C.FUTURE


def test_F3_future_census_provenance_carries_a_LOUD_marker():
    """The docstring claimed future-dating was 'flagged by the provenance line'. It was not -- it
    printed [FRESH] with no marker. VISIBLE-TO-A-CAREFUL-READER IS NOT A FLAG."""
    now = datetime(2026, 7, 22, 20, 0, 0, tzinfo=timezone.utc)
    cen = {"_meta": {"generated_utc": (now + timedelta(hours=48)).strftime(_ISO_Z)}, "roles": []}
    prov = " | ".join(C.provenance_lines(cen, "f.json", now=now))
    assert "!!" in prov and "IMPOSSIBLE" in prov
    assert "[FRESH]" not in prov


@pytest.mark.skipif(not _REAL_CENSUS.exists(), reason="committed census fixture absent")
def test_F2_live_census_limb_is_gated_and_DISQUALIFIED_not_silently_used(tmp_path):
    """`live --census` applied no vintage gate at all -- two census-overlay surfaces, one gated.

    The limb is DISQUALIFIED rather than the whole report REFUSED: the graph is `live`'s primary
    source and remains trustworthy, so a bad census must invalidate the cross-check only. And the
    follow-on line must not then claim no census was supplied -- one was; it was unusable."""
    fut = _census_with_vintage(
        tmp_path, (datetime.now(timezone.utc) + timedelta(hours=48)).strftime(_ISO_Z), "f2.json")
    rc, out, _ = _run("live", "--census", str(fut))
    assert rc != REFUSED_EXIT, "a bad census must not invalidate the graph-primary report"
    assert "DISQUALIFIED" in out
    assert "no --census" not in out, "must not report 'no --census' when one was supplied"


# ---------------------------------------------------------------------------
# D4 scope-exclusion: the standing falsifier.
#
# CVO flagged the D4 rule (service-linked roles reclassified MISS -> EXCLUSION) as the item most
# deserving adversarial checking, precisely because it SUPPRESSES 12 findings. Adversarial pass run
# 2026-07-22: 0 service-linked roles are Terraform-declared, 0 path/name disagreements either way.
#
# BUT "0 TODAY" IS A DATA-DEPENDENT RESULT, NOT A PROPERTY OF THE RULE. The rule is sound only while
# nothing we govern lives under /aws-service-role/. The moment someone Terraform-declares a
# service-linked role, the exclusion starts hiding a gap we OWN -- silently, because suppression is
# invisible by construction.
#
# So the falsifier becomes a standing control instead of a one-off finding. If this ever fails, the
# D4 exclusion must be narrowed to "service-linked AND NOT TF-declared" -- do not silence the test.
# ---------------------------------------------------------------------------

def test_D4_scope_exclusion_assumption_still_holds__service_linked_is_never_TF_declared():
    """The falsifier for the D4 suppression. Data-dependent BY DESIGN -- that is the point."""
    import sys as _s
    _s.path.insert(0, str(_WS))
    try:
        from org.modules.graph.extract_iam import build_iam_report
    except ImportError:
        pytest.skip("extract_iam unavailable")
    _p, tf_roles, _g = build_iam_report(_WS)
    offenders = [n for n in tf_roles if "aws-service-role" in str(n).lower()
                 or str(n).startswith("AWSServiceRoleFor")]
    assert not offenders, (
        "A service-linked role is now TERRAFORM-DECLARED: " + str(offenders) + ". "
        "The D4 scope-exclusion suppresses service-linked roles as 'not IaC-governable'. That "
        "assumption is now FALSE, and the exclusion is hiding a gap we own. Narrow the rule to "
        "'service-linked AND NOT TF-declared' -- do NOT silence this test.")
