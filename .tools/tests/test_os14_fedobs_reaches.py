#!/usr/bin/env python3
"""test_os14_fedobs_reaches.py -- NFRA_OUTSET TO-OS-s-14 / criterion O14-AC1.

THE QUESTION: does comp-fedobs's co-evolution signal REACH the report through the OS-s-10 seam?

Run at both required grains:
  python .tools/tests/test_os14_fedobs_reaches.py
  python -m pytest -q .tools/tests/test_os14_fedobs_reaches.py

ARMS
  A  a published comp_fedobs_coevolution.json REACHES GROUP B: its rows are the stratum's rows,
     its tool and argv become the stratum's re-run recipe, and the stratum DECLARES that these
     are FILE pairs and not resource pairs.
  B  RED MUTANT, the one the criterion names: the seam SEVERED -- the fedobs key removed from the
     declared precedence -- so the signal stops reaching the report. Mutated at the DEFINITION of
     OUTSET_GROUP_B_SOURCES, not at a use site (NFRA_OUTSET-W2-S17).
  C  PRECEDENCE: with BOTH sources published, the RESOURCE-grain one wins and no grain
     declaration is attached, because at that point none is needed.
  D  ⛔ THE LOAD-BEARING CONTROL: a PRESENT-BUT-BROKEN higher-precedence publish is NEVER masked
     by a healthy lower one. Only ABSENCE advances the search. A second RED MUTANT makes it fall
     through and must break the arm -- otherwise a broken producer hides behind a working one and
     the reader sees a clean answer where a failure exists.
  E  every declared source ABSENT under a CONFIGURED prefix reads FAILED in the established
     ABSENT vocabulary, and never quietly falls back to the host stand-in.
  F  the host stand-in is still reached when NO prefix is configured, still declaring itself.

NO AWS, NO NETWORK -- every arm runs against a tempfile directory with an injected loader. The
LIVE comp-fedobs measurement belongs to O14-AC2 and is deliberately NOT an arm here: this battery
proves the WIRE, and a network read would let AC1 go red for a reason that is not the wire.
"""
from __future__ import annotations

import datetime as _dt
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "infra" / "aws" / "ec2" / "estate-report-runner" / "estate_report_runner.py"

RUNNER_ENV = {
    "ESTATE_REPORT_BUCKET": "os14-battery-not-a-real-bucket",
    "ESTATE_GITHUB_SECRET_ID": "x", "ESTATE_KIMI_SECRET_ID": "x",
    "ESTATE_KIMI_URL": "http://127.0.0.1:1", "ESTATE_KIMI_MODEL": "x",
    "ESTATE_REPO_URL": "http://127.0.0.1:1/x.git",
}

# RED MUTANT 1 -- SEVER THE SEAM: drop the fedobs source from the declared precedence.
SEVER_ANCHOR = '''    (OUTSET_FEDOBS_KEY, "file-pair",'''
SEVER_MUTANT = '''    ("os14-red-mutant-key-that-is-never-published.json", "file-pair",'''

# RED MUTANT 2 -- MASK A BROKEN PUBLISH: let any failure advance the search, not just absence.
MASK_ANCHOR = '''            if r["status"] != "OK" and r.get("absent"):
                continue          # ONLY absence advances the search -- see OUTSET_GROUP_B_SOURCES'''
MASK_MUTANT = '''            if r["status"] != "OK":
                continue          # RED MUTANT: ANY failure falls through, masking a broken publish'''

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, bool(ok), str(detail).replace("\n", " ")[:300]))


def _load(path, name):
    keep = {}
    for k, v in RUNNER_ENV.items():
        keep[k] = os.environ.get(k)
        os.environ[k] = v
    keep["ESTATE_OUTSET_SEAM_PREFIX"] = os.environ.pop("ESTATE_OUTSET_SEAM_PREFIX", None)
    try:
        spec = importlib.util.spec_from_file_location(name, str(path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


NOW = _dt.datetime(2026, 9, 5, 12, 0, 0, tzinfo=_dt.timezone.utc)
EMPTY_MAPS = {"lambda_prefixes": [], "ec2_prefixes": [], "producer_paths": [], "prod_to_thread": {}}

# Sentinels: a row shape neither the host git walk nor the OTHER source can emit, so "which
# source did this come from" is FALSIFIABLE rather than inferred from a plausible-looking value.
FEDOBS_SENTINEL = "OS14-FEDOBS-FILE-PAIR-SENTINEL"
COCHANGE_SENTINEL = "OS14-COCHANGE-RESOURCE-PAIR-SENTINEL"

FEDOBS_ROWS = [{"pair": FEDOBS_SENTINEL, "co_sessions": 24}]
COCHANGE_ROWS = [{"pair": COCHANGE_SENTINEL, "co_commits": 9}]


def _doc(rows, tool, argv, *, produced=None, state="OK", tag="NFRA_OUTSET/OS-s-10"):
    return {
        "schema_version": 1, "seam": tag, "tool": tool, "question": "q", "argv": argv,
        "rc": 0, "answer_state": state, "answer_state_claim": "measured",
        "denominators": {"pairs": len(rows)},
        "vintage": {"answer_produced_utc": (produced or NOW - _dt.timedelta(hours=2)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"), "tool_reported": "served @f437d60b3c65", "claim": "measured"},
        "rows": rows, "error": None, "payload_excerpt": None,
    }


FEDOBS_DOC = _doc(FEDOBS_ROWS, "comp-fedobs coevolution",
                  ["python", ".tools/comp-fedobs", "coevolution", "--json"])
COCHANGE_DOC = _doc(COCHANGE_ROWS, "comp-cochange (resource grain)",
                    ["python", ".tools/comp-cochange", "matrix", "--json"])


def _prefix(tmp: Path, name: str, **keys) -> str:
    d = tmp / name
    d.mkdir(parents=True, exist_ok=True)
    for key, payload in keys.items():
        fn = {"fedobs": "comp_fedobs_coevolution.json", "cochange": "comp_cochange.json"}[key]
        (d / fn).write_text(payload if isinstance(payload, str) else json.dumps(payload),
                            encoding="utf-8")
    return str(d)


def _loader(source: str) -> str:
    with open(source, encoding="utf-8") as fh:
        return fh.read()


def _b(mod, prefix):
    return mod._stratum_cochange(str(ROOT), NOW, EMPTY_MAPS, "PIN", prefix=prefix,
                                 loader=_loader, now=NOW, max_age_hours=26.0)


# =============================================================================================
def arm_a_signal_reaches(mod, tmp):
    s = _b(mod, _prefix(tmp, "fedobs_only", fedobs=FEDOBS_DOC))
    reached = s["status"] == "OK" and FEDOBS_SENTINEL in json.dumps(s["rows"])
    _record("A1 the fedobs co-evolution signal REACHES GROUP B", reached,
            "status=%s rows=%s" % (s["status"], json.dumps(s["rows"])[:110]))
    _record("A2 the stratum DECLARES the grain (file pairs, NOT resource pairs)",
            "grain=file-pair" in s["vintage"] and "GRAIN DECLARATION" in s["denominator"]
            and "NOT resource-grain" in s["vintage"],
            "vintage=%s" % s["vintage"][:150])
    t = s.get("reproduce") or {}
    _record("A3 the row is TRACEABLE to comp-fedobs (OS-s-11's contract holds on this source)",
            t.get("claim") == "rail-reproducible" and "comp-fedobs" in (t.get("tool") or "")
            and any("comp-fedobs" in ln for ln in (t.get("invocation") or [])),
            "tool=%r invocation=%r" % (t.get("tool"), t.get("invocation")))


def arm_b_red_mutant_sever(tmp):
    src = RUNNER.read_text(encoding="utf-8")
    assert src.count(SEVER_ANCHOR) == 1, "sever anchor not unique"
    mpath = tmp / "runner_severed.py"
    mpath.write_text(src.replace(SEVER_ANCHOR, SEVER_MUTANT), encoding="utf-8")
    mod = _load(mpath, "os14_mutant_severed")
    s = _b(mod, _prefix(tmp, "sever", fedobs=FEDOBS_DOC))
    gone = FEDOBS_SENTINEL not in json.dumps(s["rows"])
    _record("B RED MUTANT (seam SEVERED) stops the signal reaching the report", gone,
            "status=%s sentinel_present=%s rows=%d" % (s["status"], not gone, len(s["rows"])))


def arm_c_precedence(mod, tmp):
    s = _b(mod, _prefix(tmp, "both", fedobs=FEDOBS_DOC, cochange=COCHANGE_DOC))
    won = COCHANGE_SENTINEL in json.dumps(s["rows"]) and FEDOBS_SENTINEL not in json.dumps(s["rows"])
    _record("C1 with BOTH published, the RESOURCE-grain source wins", won,
            "rows=%s" % json.dumps(s["rows"])[:110])
    _record("C2 and no grain declaration is attached when none is needed",
            "GRAIN DECLARATION" not in s["denominator"] and "grain=file-pair" not in s["vintage"],
            "vintage=%s" % s["vintage"][:120])


def arm_d_broken_is_not_masked(mod, tmp):
    """A present-but-BROKEN higher-precedence publish must not be hidden by a healthy lower one."""
    broken = _prefix(tmp, "broken_first", cochange="{not json at all",
                     fedobs=FEDOBS_DOC)
    s = _b(mod, broken)
    not_masked = (s["status"] != "OK" and s["rows"] == []
                  and FEDOBS_SENTINEL not in json.dumps(s["rows"])
                  and "UNREADABLE" in (s["instrument_error"] or ""))
    _record("D1 a BROKEN higher-precedence publish is NOT masked by a healthy lower one",
            not_masked,
            "status=%s err=%s" % (s["status"], (s["instrument_error"] or "")[:110]))
    # Same for a STALE publish, which is the quieter of the two failure shapes.
    stale = _prefix(tmp, "stale_first", fedobs=FEDOBS_DOC,
                    cochange=_doc(COCHANGE_ROWS, "comp-cochange", ["x"],
                                  produced=NOW - _dt.timedelta(hours=80)))
    s2 = _b(mod, stale)
    _record("D2 same for a STALE higher-precedence publish",
            s2["status"] != "OK" and "STALE" in (s2["instrument_error"] or ""),
            "status=%s err=%s" % (s2["status"], (s2["instrument_error"] or "")[:100]))
    # RED MUTANT: let ANY failure advance the search -> the broken publish IS masked.
    src = RUNNER.read_text(encoding="utf-8")
    assert src.count(MASK_ANCHOR) == 1, "mask anchor not unique"
    mpath = tmp / "runner_masking.py"
    mpath.write_text(src.replace(MASK_ANCHOR, MASK_MUTANT), encoding="utf-8")
    m2 = _load(mpath, "os14_mutant_masking")
    s3 = _b(m2, broken)
    _record("D3 RED MUTANT (any failure falls through) MASKS the broken publish, breaking D1",
            s3["status"] == "OK" and FEDOBS_SENTINEL in json.dumps(s3["rows"]),
            "status=%s rows=%s" % (s3["status"], json.dumps(s3["rows"])[:90]))


def arm_e_all_absent(mod, tmp):
    empty = tmp / "empty_prefix"
    empty.mkdir(parents=True, exist_ok=True)
    s = _b(mod, str(empty))
    ok = (s["status"] != "OK" and s["rows"] == [] and s["row_count"] is None
          and "ABSENT" in (s["instrument_error"] or "")
          and "STAND-IN" not in s["vintage"])
    _record("E every source ABSENT under a CONFIGURED prefix reads FAILED, never the host number",
            ok, "status=%s err=%s" % (s["status"], (s["instrument_error"] or "")[:130]))


def arm_f_host_standin_intact(mod):
    s = _b(mod, None)
    _record("F with NO prefix configured the host stand-in still runs and still declares itself",
            "STAND-IN" in s["vintage"] and "claim=host-computed" in s["vintage"],
            "status=%s vintage=%s" % (s["status"], s["vintage"][:110]))


def main() -> int:
    print("=== OS-s-14 O14-AC1: comp-fedobs's co-evolution signal reaches the report ===")
    with tempfile.TemporaryDirectory(prefix="os14_") as td:
        tmp = Path(td)
        mod = _load(RUNNER, "os14_runner")
        arm_a_signal_reaches(mod, tmp)
        arm_b_red_mutant_sever(tmp)
        arm_c_precedence(mod, tmp)
        arm_d_broken_is_not_masked(mod, tmp)
        arm_e_all_absent(mod, tmp)
        arm_f_host_standin_intact(mod)
    for name, ok, detail in RESULTS:
        print("  %s  %s: %s" % ("PASS" if ok else "FAIL", name, detail))
    n_ok = sum(1 for _, ok, _ in RESULTS if ok)
    n = len(RESULTS)
    print("=== test_os14_fedobs_reaches: %s (%d/%d) ===" %
          ("PASS" if n_ok == n else "FAIL", n_ok, n))
    return 0 if n_ok == n else 1


def test_os14_fedobs_reaches():
    assert main() == 0


if __name__ == "__main__":
    sys.exit(main())
