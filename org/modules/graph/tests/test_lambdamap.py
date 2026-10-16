"""comp-lambdamap Phase-1 `check` regression tests.

Day-1 fixture = the live source-map drift state as of 2026-06-01 (CVO manual audit
359375d87 + the seeking-alpha TF-source_dir bug the tool found). These assert the
tool's *detection contract* (which classes it must catch + which it must NOT
false-positive), not exact counts, so they survive legit map fixes (e.g. when
derive --write resolves the 7 MISLOCATED, those assertions are updated then).
"""
from __future__ import annotations

import os
import sys

import pytest

GRAPH_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if GRAPH_DIR not in sys.path:
    sys.path.insert(0, GRAPH_DIR)

import lambdamap_cli as lm  # noqa: E402

ROOT = lm.workspace_root()

# CT-ca-1: the function map is one file per function under this folder (the old single map file is gone).
FMAP_REL = os.path.join("infra", "aws", "lambda", "ci", "function-map")


def _write_fmap(root, sm):
    """Write {"functions": {...}} as one file per function, clearing the folder first (the old single-file write)."""
    import json  # noqa: PLC0415
    d = os.path.join(str(root), FMAP_REL)
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.endswith(".json"):
            os.remove(os.path.join(d, f))
    for name, entry in sm["functions"].items():
        with open(os.path.join(d, name + ".json"), "w", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, indent=2) + "\n")


def _read_fmap(root):
    """The folder read back as {"functions": {...}} (the shape the old single file had)."""
    import json  # noqa: PLC0415
    d = os.path.join(str(root), FMAP_REL)
    out = {}
    for f in sorted(os.listdir(d)):
        if f.endswith(".json"):
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                out[f[:-5]] = json.load(fh)
    return {"functions": out}


@pytest.fixture(scope="module")
def findings():
    f, _stats = lm.compute_findings(ROOT)
    return f


def _by_class(findings, cls):
    return {name for c, name, _ in findings if c == cls}


def test_runs_and_returns_structured(findings):
    # every finding is (class, name, detail) with a known class
    for c, name, detail in findings:
        assert c in lm.CLASS_ORDER, f"unknown class {c}"
        assert name and isinstance(detail, str)


def test_external_sentinel_not_flagged(findings):
    # source_dir == "EXTERNAL" entries must NOT be WRONG_SOURCE_DIR/ORPHAN (intentional sentinel)
    wrong = _by_class(findings, "WRONG_SOURCE_DIR") | _by_class(findings, "ORPHAN_ENTRY")
    sm = lm.load_srcmap(ROOT)
    external = {k for k, v in sm.get("functions", {}).items()
                if isinstance(v, dict) and v.get("source_dir") == "EXTERNAL"}
    assert external, "expected some EXTERNAL-sentinel entries in the fixture"
    assert not (external & wrong), f"EXTERNAL entries false-flagged: {external & wrong}"


def test_detects_mislocated_top_level(findings):
    # the 7 top-level (outside functions{}) entries must be caught
    mis = _by_class(findings, "MISLOCATED")
    for expected in ("bd-incrparity-trigger", "inf-client-detail", "inf-gold-trigger",
                     "inf-bronze-trigger", "inf-otp-relay", "inf-portal-publisher",
                     "inf-portal-advisor-publisher"):
        assert expected in mis, f"MISLOCATED missed {expected}"


def test_detects_missing_entry_blindspots(findings):
    # TF-backed lambdas with no functions{} entry (the real CI blind spots)
    missing = _by_class(findings, "MISSING_ENTRY")
    for expected in ("inf-client-detail", "inf-portal-publisher", "bd-incrparity-trigger"):
        assert expected in missing, f"MISSING_ENTRY missed {expected}"


def test_detects_seeking_alpha_tf_sourcedir_bug(findings):
    # the bonus bug the tool found: TF source_dir -> absent dir (real dirs are analysis-*)
    wrong = _by_class(findings, "WRONG_SOURCE_DIR")
    assert "seeking-alpha-analysis-scraper" in wrong, \
        "WRONG_SOURCE_DIR missed the seeking-alpha TF source_dir bug"


# --- Phase 2: sha-vs-live CodeSha256 (compute_sha_findings is pure -> unit-testable) ---

_GOOD = "0" * 43 + "="          # well-formed 44-char base64 sha shape
_GOOD2 = "1" * 43 + "="
_PATHLEAK = "C:/Program Files/Git/abc123"   # the real record-terraform-deploy MSYS path-leak class


def test_sha_findings_classifies_all_buckets():
    funcs = {
        "match_fn":   {"artifact_sha256": _GOOD},
        "drift_fn":   {"artifact_sha256": _GOOD},
        "notlive_fn": {"artifact_sha256": _GOOD2},
        "norec_fn":   {},                                  # no artifact_sha256
        "corrupt_fn": {"artifact_sha256": _PATHLEAK},      # non-base64 -> CORRUPT_RECORD
    }
    live = {"match_fn": _GOOD, "drift_fn": _GOOD2}         # match equal; drift differs; notlive absent
    r = lm.compute_sha_findings(funcs, live)
    assert r["match"] == 1
    assert [d[0] for d in r["drift"]] == ["drift_fn"]
    assert r["not_live"] == ["notlive_fn"]
    assert r["no_record"] == 1
    assert [c[0] for c in r["corrupt"]] == ["corrupt_fn"]


def test_sha_corrupt_record_not_miscounted_as_drift():
    # a path-leaked sha must be CORRUPT_RECORD, never SHA_DRIFT (different fix path)
    funcs = {"x": {"artifact_sha256": _PATHLEAK}}
    r = lm.compute_sha_findings(funcs, {"x": _GOOD})
    assert not r["drift"], "path-leak corrupt record must not be reported as deploy-drift"
    assert r["corrupt"] and r["corrupt"][0][0] == "x"


def test_sha_dispositioned_note_suppresses_drift():
    # an entry whose _note documents an intentional divergence is DISPOSITIONED, not SHA_DRIFT
    funcs = {"vf": {"artifact_sha256": _GOOD, "_note": "S3 artifact is a stale re-zip NOT to apply; TF ignore_changes; intentional-leave"}}
    r = lm.compute_sha_findings(funcs, {"vf": _GOOD2})   # recorded != live, but dispositioned
    assert not r["drift"], "dispositioned divergence must not be SHA_DRIFT"
    assert [d[0] for d in r["dispositioned"]] == ["vf"]


def test_sha_plain_note_does_not_suppress_real_drift():
    # FALSE-NEGATIVE GUARD: a generic _note WITHOUT a disposition marker must NOT suppress real drift
    funcs = {"y": {"artifact_sha256": _GOOD, "_note": "just a normal description, deployed by the daily job"}}
    r = lm.compute_sha_findings(funcs, {"y": _GOOD2})   # recorded != live, no disposition marker
    assert [d[0] for d in r["drift"]] == ["y"], "a plain _note must not disposition-away real drift"
    assert not r["dispositioned"]


def test_classify_reconcile_holds_half_landed_and_unverifiable():
    # the CVO binding gate (ed13b714a) baked into the tool: --write reconciles ONLY STALE-RECORD
    # (live == S3 artifact); POSSIBLE-HALF-LANDED (live != S3) + UNVERIFIABLE (no S3 sha) are HELD,
    # else reconcile-to-live would LAUNDER a half-landed deploy.
    drift = [
        ("stale",      _GOOD,  "LIVEsha=="),   # live == S3 artifact -> SAFE
        ("halflanded", _GOOD2, "LIVEbad=="),   # live != S3 artifact -> HOLD
        ("unverif",    _GOOD,  "LIVEunk=="),   # S3 sha unreadable    -> HOLD
    ]
    def key_of(n):
        return f"k/{n}.zip"
    s3map = {"k/stale.zip": "LIVEsha==", "k/halflanded.zip": "OTHERsha==", "k/unverif.zip": None}
    safe, unsafe = lm.classify_reconcile(drift, key_of, lambda k: s3map.get(k))
    assert [s[0] for s in safe] == ["stale"], "only live==S3 is safe to reconcile"
    assert sorted(u[0] for u in unsafe) == ["halflanded", "unverif"], "half-landed + unverifiable must be HELD"
    assert any("HALF-LANDED" in u[3] for u in unsafe if u[0] == "halflanded")
    assert any("UNVERIFIABLE" in u[3] for u in unsafe if u[0] == "unverif")


def test_parity_settle_guard():
    # CVO race-sensitivity finding (660-class): a live!=S3 divergence whose live was JUST updated
    # (< 180s) is an in-flight deploy -> SETTLING (exit-2 transient), NOT a POSSIBLE-HALF-LANDED break.
    # An old divergence (live stable for hours) IS a real half-landed deploy.
    import datetime as dt
    now = dt.datetime(2026, 6, 29, 16, 0, 0, tzinfo=dt.timezone.utc)
    funcs = {"s": {"artifact_sha256": _GOOD, "artifact_s3_key": "ks"},
             "h": {"artifact_sha256": _GOOD, "artifact_s3_key": "kh"}}
    live = {"s": _GOOD2, "h": _GOOD2}
    s3 = {"ks": "X" * 43 + "=", "kh": "X" * 43 + "="}   # both live != s3
    mod = {"s": now - dt.timedelta(seconds=30), "h": now - dt.timedelta(hours=2)}
    v = lm.compute_parity(funcs, live, lambda n: funcs[n]["artifact_s3_key"],
                          lambda k: s3.get(k), modified=mod, now=now)
    assert v["s"][0] == "SETTLING", "a <180s-old divergence is an in-flight deploy, not a break"
    assert v["h"][0] == "POSSIBLE-HALF-LANDED", "a hours-old divergence is a real half-landed deploy"


def test_reconcile_deployed_holds_half_landed(tmp_path, monkeypatch):
    # CVO gate b56df0083 C1 safety: the UNATTENDED post-apply reconcile must reconcile a STALE-RECORD
    # (live==S3) but HOLD a half-landed (live!=S3) -- record UNCHANGED, exit 1 (alert) -- never launder.
    import json
    smdir = tmp_path / "infra" / "aws" / "lambda" / "ci"
    smdir.mkdir(parents=True)
    sm = {"functions": {
        "stale": {"artifact_sha256": _GOOD, "artifact_s3_key": "ks"},   # live==S3 -> reconcile
        "half":  {"artifact_sha256": _GOOD, "artifact_s3_key": "kh"},   # live!=S3 -> HOLD
    }}
    _write_fmap(tmp_path, sm)
    LIVE = "Z" * 43 + "="
    monkeypatch.setattr(lm, "live_code_shas", lambda: {"stale": LIVE, "half": LIVE})
    monkeypatch.setattr(lm, "s3_artifact_sha", lambda k: {"ks": LIVE, "kh": "Q" * 43 + "="}.get(k))
    monkeypatch.setattr(lm, "live_lambda_modified", lambda: {})        # no settling -> persistent
    rc = lm.reconcile_deployed(str(tmp_path), ["stale", "half"], settle_retry_seconds=0)
    assert rc == 1, "a held half-landed must exit 1 (C1 alert)"
    out = _read_fmap(tmp_path)
    assert out["functions"]["stale"]["artifact_sha256"] == LIVE, "stale-record reconciled to live"
    assert out["functions"]["half"]["artifact_sha256"] == _GOOD, "half-landed record UNCHANGED (not laundered)"
    actions = {json.loads(ln)["fn"]: json.loads(ln)["action"]
               for ln in (smdir / "source-map-reconcile-audit.jsonl").read_text().splitlines()}
    assert actions["stale"] == "reconcile" and actions["half"] == "HOLD", "C3 audit records both"


def test_reconcile_deployed_first_records_no_record(tmp_path, monkeypatch):
    # AMGT_RESAPP-D1-S6: a just-deployed fn with NO sha was counted already-in-parity and never recorded.
    # live==S3 -> first record; live!=S3 -> HOLD (exit 1); no S3 proof -> left unrecorded, no alert.
    import json
    smdir = tmp_path / "infra" / "aws" / "lambda" / "ci"
    smdir.mkdir(parents=True)
    sm = {"functions": {
        "fresh": {"artifact_s3_key": "kf"},   # live==S3 -> first record
        "local": {},                          # no S3 key -> left unrecorded
    }}
    _write_fmap(tmp_path, sm)
    LIVE = "Z" * 43 + "="
    monkeypatch.setattr(lm, "live_code_shas", lambda: {"fresh": LIVE, "local": LIVE, "half": LIVE})
    monkeypatch.setattr(lm, "s3_artifact_sha", lambda k: {"kf": LIVE, "kh": "Q" * 43 + "="}.get(k))
    monkeypatch.setattr(lm, "live_lambda_modified", lambda: {})
    assert lm.reconcile_deployed(str(tmp_path), ["fresh", "local"], settle_retry_seconds=0) == 0
    out = _read_fmap(tmp_path)
    assert out["functions"]["fresh"]["artifact_sha256"] == LIVE, "no-record + live==S3 is first-recorded"
    assert "artifact_sha256" not in out["functions"]["local"], "no S3 proof -> never recorded from live alone"
    rows = [json.loads(ln) for ln in (smdir / "source-map-reconcile-audit.jsonl").read_text().splitlines()]
    assert [(r["fn"], r["action"]) for r in rows] == [("fresh", "first-record")]
    sm["functions"] = {"half": {"artifact_s3_key": "kh"}}   # no record, live!=S3 -> HOLD
    _write_fmap(tmp_path, sm)
    assert lm.reconcile_deployed(str(tmp_path), ["half"], settle_retry_seconds=0) == 1
    assert "artifact_sha256" not in _read_fmap(tmp_path)["functions"]["half"]


def test_reconcile_deployed_fail_safe_empty_set(tmp_path):
    # FAIL-SAFE (CTO condition): empty/unknown deployed set -> NO-OP exit 0 (never reconcile-all)
    smdir = tmp_path / "infra" / "aws" / "lambda" / "ci"
    smdir.mkdir(parents=True)
    _write_fmap(tmp_path, {"functions": {"x": {"artifact_sha256": _GOOD}}})
    assert lm.reconcile_deployed(str(tmp_path), [], settle_retry_seconds=0) == 0
    assert lm.reconcile_deployed(str(tmp_path), ["no-such-fn"], settle_retry_seconds=0) == 0
