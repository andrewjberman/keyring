#!/usr/bin/env python3
"""
outset_seam -- THE CONSUMPTION SEAM (NFRA_OUTSET OS-s-10, PRD s.3).

An outset tool's answer reaches the estate-report host as a PUBLISHED ARTIFACT -- a producer
writes, the runner reads -- the shape the federated-observer and comp-learns producers already use.

THIS MODULE IS THE **PRODUCER** HALF ONLY, and the split is forced by the world rather than chosen:
the report host pulls exactly ONE file from S3 (`code/estate_report_runner.py`, see
infra/aws/terraform/estate-report/instance.tf:215) and has no estate workspace, so it cannot import
this module. The CONSUMER half therefore lives inside `estate_report_runner.py` itself. That is one
implementation of each half, not two of the same -- and the thing they share is the artifact SCHEMA,
which `.tools/tests/test_os10_seam.py` cross-checks as a contract test rather than trusting to
matching comments.

WHAT AN ARTIFACT CARRIES, and the cell asks for exactly these three:
    answer_state   the TOOL'S OWN state, in the tool's own vocabulary, never re-derived
    vintage        when the ANSWER was produced, plus the tool's own vintage if it emitted one
    denominators   what the number counted, out of what -- carried, not recomputed

WARN: A FAILED PUBLISH READS **FAILED**, NEVER ABSENT. That is the load-bearing property of the
whole seam and it is the reason the reader has three failure modes of its own (artifact ABSENT,
artifact UNREADABLE, artifact STALE) rather than returning an empty result. The estate has already
paid for the alternative: `estate_report_runner._stratum`'s own docstring says a broken instrument
and a clean zero "must never be byte-identical, because the model narrates both with equal
confidence". An omitted section reads as "nothing to report"; that is the exact lie this seam
exists to stop.

WARN: STALENESS IS A FAILURE, NOT A FOOTNOTE. PRD s.3 names the cost of this shape as "a publishing
step and a freshness question per artifact". The freshness question is answered HERE: an artifact
older than the consumer's declared ceiling reads FAILED with its measured age, because a stale
artifact is indistinguishable from a fresh one in every field except its vintage, and a consumer
that does not check the vintage will narrate 51-day-old numbers as today's. (That is not
hypothetical: NFRA_OUTSET OS-s-7 measured the `code_heat` parquet at 50.7 days with no owner and no
cadence.)

READ-ONLY WITH RESPECT TO THE ESTATE: publishing writes exactly one destination the CALLER names.
Nothing is deleted, nothing else is touched, and no destination is defaulted -- an artifact written
somewhere nobody asked for is the half-landed condition this project keeps finding.

Author: 0.9.0_WK_NFRA_OUTSET~1 (NFRA_OUTSET OS-s-10). 2026-09-05.
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import subprocess
import sys

SCHEMA_VERSION = "1.0"
SEAM_TAG = "NFRA_OUTSET/OS-s-10"

# THE DECLARED DOMAIN of `answer_state` a published artifact may carry: comp-heat's own four (its
# RC_BY_STATE vocabulary, inherited from NFRA_COMPEFFICACY s.4 and shared by every comp-tool that
# implements that bar) plus the two the SEAM itself can produce. The CONSUMER (in
# estate_report_runner.py) maps every one of these to a report stratum status, and the battery
# asserts the two sets match EXACTLY in both directions -- so a state added on one side and not the
# other is a test failure rather than a silent default to OK.
DECLARED_ANSWER_STATES = (
    "OK",                          # a complete answer; the rows ARE the answer
    "PRESENT_WITH_ZERO_RESULTS",   # a MEASURED zero -- a result, not a failure
    "SUBJECT_ABSENT_FROM_CORPUS",  # a MEASURED absence -- also a result, with its denominator
    "PARTIAL_OR_BLIND",            # Rule T: "results are a PREFIX, not the answer"
    "NOT_APPLICABLE",              # the question does not apply to this subject here
    "FAILED",                      # the producer itself failed -- the seam's whole point
)


def _now_utc() -> _dt.datetime:
    return _dt.datetime.now(_dt.timezone.utc)


def _iso(ts: _dt.datetime) -> str:
    return ts.astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_iso(s):
    try:
        return _dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc)
    except (TypeError, ValueError):
        return None


def build_artifact(tool: str, question: str, argv: list, rc, payload, *,
                   answer_state: str, denominators, vintage_of_answer=None,
                   tool_vintage=None, rows=None, error=None,
                   answer_state_claim: str = "measured") -> dict:
    """The artifact, one shape for every outset tool. Every field a consumer may act on carries its
    own claim; nothing here is inferred by the reader."""
    return {
        "schema_version": SCHEMA_VERSION,
        "seam": SEAM_TAG,
        "tool": tool,
        "question": question,
        "argv": list(argv),
        "rc": rc,
        "answer_state": answer_state,
        "answer_state_claim": answer_state_claim,
        "denominators": denominators,
        "vintage": {
            "answer_produced_utc": _iso(vintage_of_answer or _now_utc()),
            "tool_reported": tool_vintage,
            "claim": "measured",
        },
        "rows": rows if rows is not None else [],
        "error": error,
        "payload_excerpt": payload,
    }


def run_and_build(tool: str, question: str, argv: list, *, cwd=None, timeout_s: float = 60.0,
                  runner=None) -> dict:
    """Run one outset tool and build its artifact. A tool that CRASHES, TIMES OUT or returns
    unparseable output produces a FAILED artifact -- it never produces nothing, and it never
    produces an artifact that looks like a clean answer."""
    started = _now_utc()
    runner = runner or _default_runner
    try:
        rc, out, err = runner(argv, cwd, timeout_s)
    except Exception as e:                                                  # noqa: BLE001
        return build_artifact(tool, question, argv, None, None,
                              answer_state="FAILED", answer_state_claim="measured",
                              denominators={"claim": "absent",
                                            "reason": "the producer did not return an answer"},
                              vintage_of_answer=started,
                              error="producer did not complete: %s: %s"
                                    % (type(e).__name__, str(e)[:200]))
    doc = None
    if out:
        try:
            doc = json.loads(out)
        except json.JSONDecodeError:
            doc = None
    if doc is None:
        return build_artifact(tool, question, argv, rc, None,
                              answer_state="FAILED", answer_state_claim="measured",
                              denominators={"claim": "absent",
                                            "reason": "the producer did not return an answer"},
                              vintage_of_answer=started,
                              error="producer returned rc=%r and no parseable JSON answer "
                                    "(stderr excerpt: %s)" % (rc, (err or "")[:200]))
    state, state_claim = _answer_state_of(doc, rc)
    return build_artifact(
        tool, question, argv, rc, {k: doc[k] for k in ("summary", "budget", "denominator",
                                                       "basis", "scope") if k in doc},
        answer_state=state, answer_state_claim=state_claim,
        denominators=_denominators_of(doc),
        vintage_of_answer=started,
        tool_vintage=(doc.get("vintage") or {}).get("measured_at_utc")
        if isinstance(doc.get("vintage"), dict) else doc.get("vintage"),
        rows=doc.get("paths") or doc.get("rows") or doc.get("uncommitted") or [],
        error=None)


def _answer_state_of(doc: dict, rc):
    """(state, claim). NOT ALL COMP-TOOLS EMIT ONE, AND SOME EMIT null ON A CLEAN RUN -- measured
    2026-09-05: `comp-heat drift --json` has no answer_state key at all, and
    `comp-heat freshness --json` emits `"answer_state": null` on a healthy answer. Reading either as
    OK is an INFERENCE, so it is carried as one. A consumer can reject on the claim; it cannot
    reject on a value that quietly pretends the tool said it."""
    raw = doc.get("answer_state")
    if isinstance(raw, str) and raw.strip():
        return raw.strip(), "measured"
    if rc == 0:
        return "OK", "inferred (the tool emitted no answer_state and returned rc=0 with a " \
                     "parseable JSON answer)"
    return "FAILED", "inferred (the tool emitted no answer_state and returned rc=%r)" % (rc,)


def _denominators_of(doc: dict):
    """What the tool's own numbers counted, out of what. GENERIC BY RULE, not by per-tool knowledge:
    the tool's declared `denominator`/`summary` objects, plus every TOP-LEVEL SCALAR the tool chose
    to publish, plus Rule T's terminal line (which IS a denominator -- 'scanned N of N'). Never
    null: a tool that reported none says so with a claim, because a null denominator beside a real
    number is how a reader ends up trusting a count with no population."""
    out = {}
    for key in ("denominator", "summary"):
        if isinstance(doc.get(key), dict):
            out[key] = doc[key]
    scalars = {k: v for k, v in doc.items()
               if isinstance(v, (int, float, str, bool)) and k not in ("answer_state",)}
    if scalars:
        out["tool_scalars"] = scalars
    term = (doc.get("budget") or {}).get("terminal") if isinstance(doc.get("budget"), dict) else None
    if term:
        out["budget_terminal"] = term
    if not out:
        return {"claim": "absent",
                "reason": "the tool's JSON carried no denominator, no summary, no top-level "
                          "scalar and no Rule T terminal line"}
    out["claim"] = "measured"
    return out


def _default_runner(argv, cwd, timeout_s):
    """subprocess with a REAL bound. WARN: `timeout=` does NOT bound a shell LAUNCHER whose
    grandchild holds the stdout pipe -- a sibling cell measured `comp-pipescript deployed` running
    91.8 s against an 8 s deadline and then dying with zero output. So this launches the
    INTERPRETER directly (sys.executable + the tool path), never `bash -c`, and never a wrapper
    that forks. On this host a bare `subprocess.run(["bash", ...])` reaches the WSL stub and
    returns rc=1 with 504 bytes of UTF-16LE on stdout, which reads as a broken tool rather than as
    a wrong launcher."""
    p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout_s)
    return p.returncode, p.stdout, p.stderr


def publish_artifact(artifact: dict, dest: str, *, s3_client=None) -> dict:
    """Write ONE artifact to the ONE destination the caller named -- a local path or an s3:// URI.

    NO DEFAULT DESTINATION, deliberately: an artifact written somewhere nobody asked for is exactly
    the unowned, unscheduled object this project has already measured twice.
    Returns a receipt: {published: bool, dest, bytes, error}.
    """
    body = json.dumps(artifact, indent=2, sort_keys=False).encode("utf-8")
    try:
        if dest.startswith("s3://"):
            bucket, _, key = dest[len("s3://"):].partition("/")
            if not key:
                raise ValueError("s3 destination needs a key: %r" % dest)
            client = s3_client
            if client is None:
                import boto3
                client = boto3.client("s3")
            client.put_object(Bucket=bucket, Key=key, Body=body,
                              ContentType="application/json")
        else:
            parent = os.path.dirname(os.path.abspath(dest))
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(dest, "wb") as fh:
                fh.write(body)
    except Exception as e:                                                  # noqa: BLE001
        return {"published": False, "dest": dest, "bytes": 0,
                "error": "%s: %s" % (type(e).__name__, str(e)[:200])}
    return {"published": True, "dest": dest, "bytes": len(body), "error": None}


# The producers this seam publishes today. A DECLARED registry, not an enumeration of every outset
# tool: enumerating the full set is OS-s-12's census (FWD-5) and the seam must not fork a second
# one. Each entry is (key, tool, question, argv-suffix) -- argv[0] is filled by the CLI.
SEAM_PRODUCERS = [
    ("comp_heat_freshness_tools", "comp-heat freshness",
     "Which paths under .tools/ are hot, warm or cold, and how cold is the coldest?",
     ["freshness", ".tools", "--budget", "60", "--json"]),
    ("comp_heat_drift", "comp-heat drift",
     "What has been written in this workspace that is not in any commit?",
     ["drift", "--budget", "60", "--json"]),
]


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        description="OS-s-10 consumption seam: publish one outset-tool artifact per producer.")
    ap.add_argument("--tool", required=True, help="path to the comp-tool to run (e.g. .tools/comp-heat)")
    ap.add_argument("--out-dir", required=True,
                    help="destination DIRECTORY or s3:// PREFIX -- named by the caller, never defaulted")
    ap.add_argument("--timeout", type=float, default=90.0, help="per-producer bound in seconds")
    a = ap.parse_args(argv)
    ok = 0
    for key, tool, question, tail in SEAM_PRODUCERS:
        art = run_and_build(tool, question, [sys.executable, a.tool] + tail, timeout_s=a.timeout)
        dest = a.out_dir.rstrip("/") + "/" + key + ".json"
        receipt = publish_artifact(art, dest)
        ok += 1 if receipt["published"] and art["answer_state"] != "FAILED" else 0
        print("%-34s answer_state=%-26s published=%s bytes=%d %s"
              % (key, art["answer_state"], receipt["published"], receipt["bytes"],
                 receipt["error"] or ""))
    print("SEAM PUBLISH: %d of %d producer(s) published a non-FAILED artifact"
          % (ok, len(SEAM_PRODUCERS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
