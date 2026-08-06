#!/usr/bin/env python3
"""LOCAL STEP-RUNNER for the SUBDIVIDED Kimi pipeline (SPEC @58505c291 s.4).

Andrew-direct 2026-08-06: "strictly structured, not one big prompt file, rather splitting it up into
excerpts for each call. then each prompt/call step is gated behind receipt/proof of the prior calls
completion. It should be cached in a manner that there is continuity."

This implements exactly that, LOCALLY, so the step function can be walked and inspected BEFORE any
production code is written.

  CALL 0        deterministic strata compilation (NO MODEL). Every stratum carries a DENOMINATOR
                and a VINTAGE per SPEC s.5, and a tool FAILURE is a distinct state from a zero row
                count -- a clean zero and a broken instrument must never be byte-identical.
  CALL 1        NARRATE  -- stratum SUMMARIES only. Audience: Andrew. No proposals.
  CALLS 2..5    DETECT   -- one per group (A/B/C/D). Emits CANDIDATES ONLY, no prose.
  CALLS 6..N    AUTHOR   -- one per candidate. Small prompt, own budget, must cite evidence.

THE THREE PROPERTIES ANDREW ASKED FOR, and where each lives:

  STRUCTURED   every call has its own prompt built from a bounded excerpt. No call ever receives
               the whole corpus. See build_* functions.
  GATED        a step cannot fire until every id in its `needs` list is RECORDED COMPLETE in the
               run ledger. This is a MECHANICAL DATA DEPENDENCY, not an approval gate -- call N+1
               consumes call N's validated output. See Run.gate().
  CACHED       every step writes its output to the run directory before the next fires. A re-run
               with --resume replays completed steps from disk and only executes what is missing.
               Continuity across runs, and a failed call resumes instead of restarting.

TWO ENFORCEMENTS THAT ARE DONE IN CODE, NOT BY ASKING THE MODEL NICELY (SPEC s.4, ":26 -- prompt
discipline is not a control"):
  * a DETECT candidate naming an entity outside the canon universe is REJECTED BY THE RUNNER.
  * an AUTHOR proposal whose evidence_cited does not resolve to a real stratum row or nugget id is
    REJECTED BY THE RUNNER.
Both rejections are COUNTED and REPORTED. A silently dropped candidate would rebuild the exact
`degraded_sources: []` shape this pipeline was built to stop.

EGRESS: --dry-run is the DEFAULT and builds every prompt without calling anything. --live performs
vendor egress (Moonshot) and requires Andrew's explicit per-use word for that run.

Usage:
  python kimi_pipeline.py                      # dry-run, builds all prompts, no egress
  python kimi_pipeline.py --live               # real calls (needs Andrew's word)
  python kimi_pipeline.py --resume             # replay cache, run only what is missing
  python kimi_pipeline.py --only 3             # run one step (deps must already be cached)
  python kimi_pipeline.py --from 2             # invalidate step 2 onward and re-run
  python kimi_pipeline.py --show 3             # print a completed step's prompt + output
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone

REPO = r"C:\Users\AndrewBerman\Desktop\ajb_workspace"
RUNNER_DIR = os.path.join(REPO, "infra", "aws", "ec2", "estate-report-runner")
HERE = os.path.dirname(os.path.abspath(__file__))

KIMI_URL = "https://api.moonshot.ai/v1/chat/completions"
KIMI_MODEL = "kimi-k3"
KIMI_SECRET = "astn/kimi/api-key"

# Per-call budgets. SPEC s.4: "each call gets its own budget, so narration and proposal no longer
# compete." These are STARTING VALUES to be re-derived from the first full run, not derived answers
# -- the monolith's 32000 was never the binding constraint (measured 2026-08-06: it used 8,872 of
# 32,000 and finish_reason was `stop`), so sizing against max_tokens tunes the wrong knob. What
# drives elapsed time is REASONING over prompt complexity: 8,006 of 8,872 completion tokens (90.2%)
# were reasoning. Bounded prompts are the lever; these ceilings are just headroom.
#
# AND DO NOT SIZE THE SMALL CALLS TIGHT. Measured on a 31-char probe: 35 of 51 completion tokens
# were reasoning for an answer of "OK". A call whose JOB is small still reasons first, so "small
# task means small budget" would re-derive the KIMI_EMPTY starvation once per call instead of once.
# MEASURED 2026-08-06, and the detect number is a CORRECTION OF MY OWN: at 12000 the group-B detect
# call STARVED -- finish_reason `length`, 11,997 of 12,000 completion tokens spent on reasoning,
# content 0 bytes. That is KIMI_LENGTH_STARVED reproduced PER CALL, which is precisely what the
# comment below warns against, written by the same hand that then set 12000. Knowing a failure mode
# by name does not immunise you against writing it.
# Observed reasoning spend on real detect calls: 7,674 / 11,729 / 11,997+ tokens. 32000 gives the
# worst observed case ~2.7x headroom. It is a CEILING, not a target -- the monolith used 8,872 of
# 32,000 and stopped cleanly, so a generous ceiling costs nothing when the model does not need it.
BUDGETS = {
    "narrate": 16000,
    "detect": 32000,
    "author": 16000,
}
TIMEOUTS = {"narrate": 900, "detect": 900, "author": 600}

GROUPS = {
    "A": "DID WHAT WE WROTE ACTUALLY TAKE EFFECT?  (the propagation ladder)",
    "B": "ARE OUR RELATIONSHIPS WHAT WE THINK?     (structural / behavioral / temporal)",
    "C": "IS OUR LIFECYCLE PICTURE TRUE?           (cold subtrees x citation)",
    "D": "DO THINGS HAVE THEIR REAL NAMES?         (SUBSTRATE -- sequenced first)",
}

PROSE_FIELDS = ["classification", "classification_reason", "description", "enrichment"]


# ===========================================================================================
# RUN LEDGER -- the cache + the gate. This is the continuity layer.
# ===========================================================================================
class Run:
    """A resumable, gated, cached execution of the subdivided pipeline.

    The ledger (`run.json`) is the single source of truth for what has completed. A step is COMPLETE
    only when its output file exists AND the ledger records it -- two conditions deliberately, so a
    half-written file cannot be mistaken for a finished step (the file is written first, the ledger
    entry second; a crash between them re-runs the step, which is the safe direction).
    """

    def __init__(self, root: str, live: bool):
        self.root = root
        self.live = live
        os.makedirs(root, exist_ok=True)
        self.ledger_path = os.path.join(root, "run.json")
        self.ledger = self._load()

    def _load(self) -> dict:
        if os.path.exists(self.ledger_path):
            with open(self.ledger_path, encoding="utf-8") as fh:
                return json.load(fh)
        return {"created": datetime.now(timezone.utc).isoformat(), "steps": {}}

    def _save(self) -> None:
        with open(self.ledger_path, "w", encoding="utf-8") as fh:
            json.dump(self.ledger, fh, indent=2, default=str)

    def path(self, sid: str, suffix: str) -> str:
        return os.path.join(self.root, "%s.%s" % (sid, suffix))

    def complete(self, sid: str) -> bool:
        e = self.ledger["steps"].get(sid)
        return bool(e and e.get("status") == "COMPLETE" and os.path.exists(self.path(sid, "out.json")))

    def gate(self, sid: str, needs: list[str]) -> None:
        """THE GATE. A step cannot fire until every dependency is RECORDED COMPLETE.

        Mechanical data dependency, not an approval step: this asks "does the input exist?", never
        "has someone signed off?". Missing input is a hard stop with the reason named, because a
        step that runs on absent input produces confident output from nothing -- which is the
        failure mode this whole pipeline exists to prevent.
        """
        missing = [n for n in needs if not self.complete(n)]
        if missing:
            raise RuntimeError(
                "GATE BLOCKED for step %s -- prior step(s) not complete: %s\n"
                "  Run them first, or use --resume to execute the whole chain in order."
                % (sid, ", ".join(missing)))

    def load_out(self, sid: str) -> dict:
        with open(self.path(sid, "out.json"), encoding="utf-8") as fh:
            return json.load(fh)

    def record(self, sid: str, name: str, out: dict, meta: dict) -> None:
        with open(self.path(sid, "out.json"), "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2, default=str)
        self.ledger["steps"][sid] = dict(
            meta, name=name, status="COMPLETE", at=datetime.now(timezone.utc).isoformat())
        self._save()

    def invalidate_from(self, n: int) -> list[str]:
        killed = []
        for sid in sorted(self.ledger["steps"]):
            try:
                if int(sid.split("_")[0]) >= n:
                    killed.append(sid)
            except ValueError:
                continue
        for sid in killed:
            self.ledger["steps"].pop(sid, None)
            for suf in ("out.json", "prompt.txt", "response.json"):
                p = self.path(sid, suf)
                if os.path.exists(p):
                    os.remove(p)
        self._save()
        return killed


# ===========================================================================================
# MODEL CALL -- one place, fully instrumented, every artifact on disk
# ===========================================================================================
_ASCII_MAP = {
    "—": "--", "–": "-", "‘": "'", "’": "'",
    "“": '"', "”": '"', "…": "...", " ": " ",
    "→": "->", "≥": ">=", "≤": "<=", "×": "x",
}


def scrub_ascii(obj):
    """Substitute non-ASCII in every string value. Returns (obj, count_substituted).

    Known typographic characters map to their ASCII equivalent; anything else becomes '?'. The
    COUNT is returned so a scrub is visible in telemetry -- a silent scrub would hide how often
    the model ignores the instruction, which is the thing worth knowing.
    """
    n = 0

    def walk(o):
        nonlocal n
        if isinstance(o, str):
            if all(ord(c) < 128 for c in o):
                return o
            out = []
            for c in o:
                if ord(c) < 128:
                    out.append(c)
                else:
                    n += 1
                    out.append(_ASCII_MAP.get(c, "?"))
            return "".join(out)
        if isinstance(o, dict):
            return {walk(k): walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        return o

    return walk(obj), n


_API_KEY: str | None = None


def api_key() -> str:
    global _API_KEY
    if _API_KEY is None:
        import boto3
        raw = (boto3.client("secretsmanager", region_name="us-east-1")
               .get_secret_value(SecretId=KIMI_SECRET)["SecretString"])
        try:
            k = json.loads(raw)
            _API_KEY = (k.get("api_key") or k.get("key") or next(iter(k.values()))
                        ) if isinstance(k, dict) else str(k)
        except json.JSONDecodeError:
            _API_KEY = raw.strip()
    return _API_KEY


def model_call(run: Run, sid: str, prompt: str, kind: str) -> tuple[dict | None, dict]:
    """Returns (parsed_or_None, telemetry). Telemetry is captured BEFORE the call so it survives a
    timeout -- the exact gap that made 2026-08-06 an argument instead of data."""
    with open(run.path(sid, "prompt.txt"), "w", encoding="utf-8") as fh:
        fh.write(prompt)

    tel = {
        "kind": kind,
        "prompt_chars": len(prompt),
        # chars/4 MEASURED 11.5% LOW against this endpoint on 2026-08-06 (est 18,241 vs actual
        # 20,614 -> 3.54 chars/token). Kept as the pre-call estimate because it is all we have
        # before the response, and labelled so nobody reads it as the real number.
        "prompt_tokens_est": len(prompt) // 4,
        "max_tokens": BUDGETS[kind],
        "timeout_s": TIMEOUTS[kind],
    }
    if not run.live:
        tel["outcome"] = "DRY_RUN_NOT_SENT"
        return None, tel

    payload = json.dumps({
        "model": KIMI_MODEL,
        "temperature": 1,          # MANDATORY for kimi-k3; anything else is HTTP 400
        "max_tokens": BUDGETS[kind],
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        KIMI_URL, data=payload,
        headers={"Authorization": "Bearer %s" % api_key(), "Content-Type": "application/json"},
        method="POST")

    started = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUTS[kind]) as resp:
            body = json.loads(resp.read())
    except Exception as exc:  # noqa: BLE001
        tel["elapsed_s"] = round(time.monotonic() - started, 1)
        tel["outcome"] = "%s: %s" % (type(exc).__name__, str(exc)[:200])
        return None, tel

    tel["elapsed_s"] = round(time.monotonic() - started, 1)
    with open(run.path(sid, "response.json"), "w", encoding="utf-8") as fh:
        json.dump(body, fh, indent=2)

    usage = body.get("usage") or {}
    det = usage.get("completion_tokens_details") or {}
    choice = body["choices"][0]
    content = choice["message"].get("content") or ""
    tel.update({
        "outcome": "OK",
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "reasoning_tokens": det.get("reasoning_tokens"),
        "finish_reason": choice.get("finish_reason"),
        "content_bytes": len(content),
    })
    if usage.get("completion_tokens") and det.get("reasoning_tokens"):
        tel["reasoning_pct"] = round(100.0 * det["reasoning_tokens"] / usage["completion_tokens"], 1)

    txt = content.strip()
    if txt.startswith("```"):
        txt = txt.split("\n", 1)[-1].rsplit("```", 1)[0]
    try:
        parsed = json.loads(txt)
        # ASCII IS ENFORCED HERE, not requested in the prompt. Measured 2026-08-06: the narrate
        # call emitted 4 non-ASCII chars (em-dashes) despite the instruction, and the monolith
        # emitted them too. This output lands in an S3 markdown artifact, and CLAUDE.md bans
        # non-ASCII in anything that runs on AWS -- CloudWatch/charmap/grep breakage. Asking the
        # model is not a control; substituting is.
        parsed, n = scrub_ascii(parsed)
        tel["non_ascii_substituted"] = n
        return parsed, tel
    except json.JSONDecodeError as exc:
        tel["outcome"] = "JSON_PARSE_FAILED: %s" % exc
        tel["raw_head"] = content[:400]
        return None, tel


# ===========================================================================================
# STRATUM COMPILATION -- SPEC s.5. Denominator + vintage, and FAILURE != ZERO.
# ===========================================================================================
def _dispatch(cmd: list[str]) -> list[str]:
    """Resolve a comp-tool to something Windows can actually exec.

    The tools are shebang scripts; native Windows cannot exec a shebang, so the interpreter has to
    be named explicitly. Bash-backed tools go through the estate's ONE canonical Git-Bash resolver,
    never a bare `bash` -- a python-spawned bare `bash` Windows-resolves to the System32 WSL stub
    and fails either loudly or, worse, silently (CLAUDE.md Git section).
    """
    tool = os.path.join(REPO, cmd[0].replace("/", os.sep))
    if not os.path.exists(tool):
        return cmd
    with open(tool, "rb") as fh:
        shebang = fh.readline(120).decode("utf-8", "replace")
    if "python" in shebang:
        return [sys.executable, tool] + cmd[1:]
    if "bash" in shebang or "sh" in shebang:
        sys.path.insert(0, os.path.join(REPO, ".tools"))
        try:
            from git_bash_resolver import git_bash  # type: ignore
            return [git_bash(), tool] + cmd[1:]
        except Exception:  # noqa: BLE001 - fall through to the unresolved form, which fails LOUDLY
            return cmd
    return cmd


def run_tool(cmd: list[str], timeout: int = 180) -> dict:
    """Run a comp-tool. Returns a result carrying rc, so a FAILURE is a distinct state from a zero.

    SPEC s.5 is explicit that this distinction is load-bearing: a stratum computed by a tool that
    errored is byte-identical to one with genuinely nothing to report, and the model narrates both
    with equal confidence. rc is therefore part of the stratum, not part of the logging.
    """
    try:
        p = subprocess.run(_dispatch(cmd), cwd=REPO, capture_output=True, text=True,
                           timeout=timeout)
        return {"cmd": " ".join(cmd), "rc": p.returncode,
                "stdout": p.stdout, "stderr": p.stderr[:800]}
    except subprocess.TimeoutExpired:
        return {"cmd": " ".join(cmd), "rc": -1, "stdout": "", "stderr": "TIMEOUT after %ds" % timeout}
    except Exception as exc:  # noqa: BLE001
        return {"cmd": " ".join(cmd), "rc": -2, "stdout": "",
                "stderr": "%s: %s" % (type(exc).__name__, exc)}


def stratum(name: str, question: str, tool_result: dict, rows: list, vintage: str,
            denominator: str) -> dict:
    """One stratum, in the SPEC s.5 contract shape."""
    ok = tool_result["rc"] == 0
    return {
        "stratum": name,
        "question": question,
        "tool": tool_result["cmd"],
        "vintage": vintage,
        "denominator": denominator,
        "rows": rows if ok else [],
        "row_count": len(rows) if ok else None,
        # The whole point: a tool that failed says INSTRUMENT_FAILED, never "0 rows".
        "status": "OK" if ok else "INSTRUMENT_FAILED",
        "instrument_error": None if ok else (tool_result["stderr"] or "rc=%d" % tool_result["rc"]),
    }


def render_stratum(s: dict, max_rows: int = 25) -> str:
    """Render a stratum for a prompt. An INSTRUMENT_FAILED stratum renders its failure LOUDLY --
    it is never silently omitted, because an omitted stratum reads as 'nothing to report'."""
    head = ("stratum: %s\nquestion: %s\ntool: %s\nvintage: %s\ndenominator: %s\n"
            % (s["stratum"], s["question"], s["tool"], s["vintage"], s["denominator"]))
    if s["status"] != "OK":
        return head + ("STATUS: *** INSTRUMENT FAILED -- %s ***\n"
                       "THIS STRATUM PRODUCED NO DATA. Do NOT treat it as 'nothing found'. Any\n"
                       "claim about this question is UNMEASURED today.\n" % s["instrument_error"])
    shown = s["rows"][:max_rows]
    body = "rows: %d%s\n" % (s["row_count"],
                             "" if len(shown) == len(s["rows"])
                             else " (showing %d, SAMPLE not the full set)" % len(shown))
    for r in shown:
        body += "  - %s\n" % (json.dumps(r, default=str) if not isinstance(r, str) else r)
    if s["row_count"] == 0:
        body += "  (zero rows -- this is a RESULT, the instrument ran and found nothing)\n"
    return head + body


# ===========================================================================================
# CALL 0 -- deterministic. No model anywhere in this function, by construction.
# ===========================================================================================
def step0_compile(run: Run) -> dict:
    os.environ.setdefault("ESTATE_KIMI_SECRET_ID", "LOCAL")
    os.environ.setdefault("ESTATE_KIMI_URL", "http://local.invalid")
    os.environ.setdefault("ESTATE_KIMI_MODEL", "LOCAL")
    os.environ.setdefault("ESTATE_GITHUB_SECRET_ID", "LOCAL")
    os.environ.setdefault("ESTATE_REPORT_BUCKET", "LOCAL")
    os.environ.setdefault("ESTATE_REPO_URL", "https://local.invalid/x.git")
    sys.path.insert(0, RUNNER_DIR)
    import estate_report_runner as R

    now_utc = datetime.now(timezone.utc)
    start_local, end_local = R.resolve_window(now_utc)
    window_desc = "%s -> %s" % (start_local.strftime("%Y-%m-%d %H:%M %Z"),
                                end_local.strftime("%Y-%m-%d %H:%M %Z"))
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()

    commits = R.commits_in_window(REPO, start_local, end_local)
    nuggets, corpus_cov = R.capture_census(REPO, start_local, end_local)
    maps = R.load_attribution_maps(REPO)
    resources, attr_cov = R.compile_changed_resources(commits, maps)

    # ---- GROUP D FIRST (SPEC s.3: substrate, sequenced first). The canon universe is DERIVED as a
    # PREDICATE over the resolver -- every thread_id plus every producer:* the resolver knows -- not
    # a hand-written allowlist. "A predicate is not a roster": a hand-drawn list silently freezes
    # while the estate moves, and then the runner rejects real entities as non-canon.
    canon = sorted(set(maps["prod_to_thread"].values())
                   | {"producer:%s" % n for n in maps["prod_to_thread"]})

    # AN EMPTY CANON UNIVERSE IS A BROKEN INPUT, NOT A VALID STATE -- and it is INVISIBLE without
    # this check. MEASURED 2026-08-06: a concurrent commit by another agent made
    # load_attribution_maps degrade mid-run; prod_to_thread came back empty, canon went 386 -> 0,
    # and every DETECT call then reported "0 candidates" because NO CANDIDATE COULD BE ACCEPTED.
    # The runner printed "a zero-candidate day costs nothing -- this is the funnel working."
    #
    # It was not working. It was structurally incapable of working, and it said the same thing it
    # says on a genuinely clean day. load_attribution_maps degrades gracefully BY DESIGN (each hop
    # is independently optional), which is correct for attribution and WRONG as a silent input to
    # a gate -- graceful degradation upstream becomes a confident zero downstream unless someone
    # asks whether the input is usable.
    canon_ok = len(canon) > 0 and not maps["degraded"]
    attribution_health = {
        "degraded_hops": maps["degraded"],
        "prod_to_thread": len(maps["prod_to_thread"]),
        "lambda_prefixes": len(maps["lambda_prefixes"]),
        "ec2_prefixes": len(maps["ec2_prefixes"]),
        "canon_usable": canon_ok,
    }
    fallback_labels = sorted(k for k in resources if k.startswith("area:") or k == "UNRESOLVED")
    canon_paths = sum(len(v.get("paths", [])) for k, v in resources.items()
                      if k not in fallback_labels)
    total_paths = attr_cov["changed_paths_total"]

    d_rows = [{"label": k, "paths": len(resources[k].get("paths", [])),
               "is_canon": k not in fallback_labels} for k in
              sorted(resources, key=lambda x: -len(resources[x].get("paths", [])))]
    sD = stratum(
        "D_naming", GROUPS["D"],
        {"cmd": "estate_report_runner.compile_changed_resources (in-process)", "rc": 0,
         "stdout": "", "stderr": ""},
        d_rows, "repo @%s" % head,
        "%d of %d changed paths carry a CANON name (%.1f%%); %d land on compiled fallback labels"
        % (canon_paths, total_paths, 100.0 * canon_paths / max(total_paths, 1),
           total_paths - canon_paths))

    # ---- GROUP A: the propagation ladder.
    a_heat = run_tool([".tools/comp-heat", "drift"])
    a_rows = [ln for ln in a_heat["stdout"].splitlines() if ln.strip()][:60]
    sA = stratum("A_propagation", GROUPS["A"], a_heat, a_rows, "live working tree @%s" % head,
                 "comp-heat drift over the tracked tree; %d output line(s)" % len(a_rows))

    # ---- GROUP B: relationship integrity.
    b_cc = run_tool([".tools/comp-cochange", "matrix", "--grain", "type"])
    b_rows = [ln for ln in b_cc["stdout"].splitlines() if ln.strip()][:60]
    sB = stratum("B_relationships", GROUPS["B"], b_cc, b_rows, "git history @%s" % head,
                 "comp-cochange matrix --grain type; %d output line(s)" % len(b_rows))

    # ---- GROUP C: lifecycle truth.
    c_fresh = run_tool([".tools/comp-heat", "freshness"])
    c_rows = [ln for ln in c_fresh["stdout"].splitlines() if ln.strip()][:60]
    sC = stratum("C_lifecycle", GROUPS["C"], c_fresh, c_rows, "git history @%s" % head,
                 "comp-heat freshness over tracked subtrees; %d output line(s)" % len(c_rows))

    strata = {"D": sD, "A": sA, "B": sB, "C": sC}
    return {
        "window": window_desc,
        "head": head,
        "commits_in_window": len(commits),
        "nuggets": nuggets,
        "corpus_coverage": corpus_cov,
        "resources": resources,
        "attribution_coverage": attr_cov,
        "canon_universe": canon,
        "canon_universe_size": len(canon),
        "attribution_health": attribution_health,
        "canon_usable": canon_ok,
        "fallback_labels": fallback_labels,
        "strata": strata,
    }


# ===========================================================================================
# PROMPT BUILDERS -- each call gets a BOUNDED EXCERPT, never the whole corpus.
# ===========================================================================================
def summarize_stratum(s: dict) -> str:
    if s["status"] != "OK":
        return "- %s: INSTRUMENT FAILED (%s) -- UNMEASURED today" % (s["stratum"],
                                                                     s["instrument_error"])
    return "- %s: %d row(s). %s" % (s["stratum"], s["row_count"], s["denominator"])


def build_narrate(c0: dict) -> str:
    cov = c0["corpus_coverage"]
    return (
        "You are writing a plain-English daily brief for the owner of a cloud data estate.\n"
        "WINDOW: %s\n\n"
        "=== WHAT THE INSTRUMENTS FOUND (SUMMARIES ONLY -- you are not being given the raw rows) ===\n"
        "%s\n\n"
        "=== CONTEXT ===\n"
        "commits in window: %d\n"
        "changed paths: %d (%d carry a real canonical name; the rest fell back to location labels)\n"
        "captured operator rulings available: %d\n"
        "CORPUS FRESHNESS: %s\n\n"
        "Write ONLY a JSON object: {\"brief\": \"...\"}\n"
        "The brief is 3-6 sentences of plain English for a busy owner. No jargon, no serials, no\n"
        "commit hashes, no tool names. Say what happened and what it means.\n"
        "DO NOT propose any changes -- that is a different call and not your job here.\n"
        "If an instrument failed, say that the question went unmeasured rather than implying\n"
        "nothing was found."
        % (c0["window"],
           "\n".join(summarize_stratum(c0["strata"][g]) for g in ("D", "A", "B", "C")),
           c0["commits_in_window"], c0["attribution_coverage"]["changed_paths_total"],
           c0["attribution_coverage"]["chain_resolved"], cov.get("nuggets_total", 0),
           cov.get("corpus_freshness", "UNKNOWN"))
    )


def nugget_excerpt(nuggets: list, budget: int) -> tuple[str, int]:
    """A BOUNDED excerpt. Returns (text, shown). The count shown is reported into the prompt so the
    model knows it is looking at a sample -- an unlabelled sample reads as the whole set."""
    out, n = [], 0
    for x in nuggets:
        line = "- [%s] %s\n  ruling: %s\n" % (x.get("provenance", "?"),
                                              str(x.get("basis") or x.get("id"))[:150],
                                              str(x.get("ruling"))[:300])
        if sum(len(o) for o in out) + len(line) > budget:
            break
        out.append(line)
        n += 1
    return "".join(out), n


def order_canon(canon: list, resources: dict) -> list:
    """In-window entities FIRST, then the rest. ORDER, never FILTER (Andrew-ruled 2026-08-06).

    The truncation problem is real -- 386 entities, ~80 fit the prompt -- but filtering to entities
    that changed in the window would structurally delete the "should have changed and did NOT"
    finding, which is a legitimate Group A/B result and arguably the more interesting one. Ordering
    keeps the whole universe reachable while guaranteeing the day's actual subjects survive the cut.
    """
    in_window = [e for e in canon if e in resources]
    rest = [e for e in canon if e not in resources]
    return in_window + rest


def build_detect(c0: dict, group: str) -> str:
    s = c0["strata"][group]
    corpus_text, shown = nugget_excerpt(c0["nuggets"], 18000)
    canon = order_canon(c0["canon_universe"], c0["resources"])
    return (
        "You are auditing ONE question about a cloud data estate. Only this question.\n"
        "WINDOW: %s\n\n"
        "=== THE QUESTION ===\n%s\n\n"
        "=== THE EVIDENCE (this stratum, with its denominator and vintage) ===\n%s\n"
        "=== CAPTURED OPERATOR RULINGS (excerpt: %d of %d shown -- a SAMPLE) ===\n"
        "CORPUS FRESHNESS: %s\n\n%s\n\n"
        "=== YOUR JOB ===\n"
        "Identify entities whose RECORDED PROSE may have drifted from reality, based on the\n"
        "evidence above. Output CANDIDATES ONLY. Do NOT write any replacement prose -- a later\n"
        "call does that.\n\n"
        "Return ONLY JSON: {\"candidates\": [{\"entity\": ..., \"field\": ..., \"why_suspect\": ...,\n"
        "\"evidence_ref\": ...}]}\n\n"
        "HARD CONSTRAINTS, enforced by the runner and not by trust:\n"
        "  * `entity` MUST be one of these canonical entities. Anything else is DISCARDED.\n"
        "    SHOWING %d of %d canonical entities -- the runner accepts any of the %d, but you can\n"
        "    only see these. If the right subject is not listed, say so in why_suspect rather than\n"
        "    forcing a candidate onto a name you were shown.\n%s\n"
        "  * `field` MUST be one of: %s\n"
        "  * `evidence_ref` MUST point at a row of the stratum above or a ruling id.\n\n"
        "Returning zero candidates is a valid and useful answer. If the stratum above says the\n"
        "instrument FAILED, return zero candidates and say so in why_suspect of nothing -- do not\n"
        "infer drift from an unmeasured question."
        % (c0["window"], GROUPS[group], render_stratum(s), shown,
           len(c0["nuggets"]), c0["corpus_coverage"].get("corpus_freshness", "UNKNOWN"),
           corpus_text,
           min(80, len(canon)), len(canon), len(canon),
           "\n".join("    %s" % e for e in canon[:80]) or "    (none -- canon universe is EMPTY)",
           ", ".join(PROSE_FIELDS))
    )


def build_author(c0: dict, cand: dict) -> str:
    ent = cand.get("entity")
    res = c0["resources"].get(ent, {})
    paths = res.get("paths", [])[:15]
    corpus_text, shown = nugget_excerpt(c0["nuggets"], 6000)
    return (
        "You are writing ONE prose field for ONE entity. Nothing else.\n\n"
        "ENTITY: %s\nFIELD:  %s\n\n"
        "=== WHY IT WAS FLAGGED ===\n%s\nevidence_ref: %s\n\n"
        "=== WHAT CHANGED FOR THIS ENTITY IN THE WINDOW (%d path(s), showing %d) ===\n%s\n\n"
        "=== RELEVANT CAPTURED RULINGS (%d shown) ===\n%s\n\n"
        "Return ONLY JSON: {\"proposed_text\": ..., \"rationale\": ..., \"evidence_cited\": ...}\n"
        "`evidence_cited` MUST reference the evidence_ref above or a ruling id shown here. A\n"
        "proposal that cannot cite what it saw is DISCARDED BY THE RUNNER -- this exists to stop\n"
        "prose inventing its own warrant.\n"
        "Write ASCII only. No em-dashes, no smart quotes."
        % (ent, cand.get("field"), cand.get("why_suspect"), cand.get("evidence_ref"),
           len(res.get("paths", [])), len(paths),
           "\n".join("  " + p for p in paths) or "  (none)",
           shown, corpus_text)
    )


# ===========================================================================================
# STEPS
# ===========================================================================================
def step_narrate(run: Run, c0: dict) -> tuple[dict, dict]:
    prompt = build_narrate(c0)
    parsed, tel = model_call(run, "1_narrate", prompt, "narrate")
    return {"brief": (parsed or {}).get("brief"), "telemetry": tel}, tel


def step_detect(run: Run, c0: dict, group: str, sid: str) -> tuple[dict, dict]:
    # REFUSE, LOUDLY, RATHER THAN RETURN A ZERO NOBODY CAN INTERPRET. With an unusable canon
    # universe every candidate is rejected by construction, so the call would burn a real vendor
    # call to produce a zero that is indistinguishable from a clean day. Spending money to
    # manufacture an ambiguous zero is the worst of both.
    if not c0.get("canon_usable", True):
        tel = {"kind": "detect", "outcome": "SKIPPED_CANON_UNUSABLE", "prompt_chars": 0}
        return {
            "group": group, "status": "DETECT_FAILED", "unmeasured": True,
            "stratum_status": c0["strata"][group]["status"],
            "call_outcome": "SKIPPED -- canon universe unusable (%s)"
                            % (c0.get("attribution_health", {}).get("degraded_hops") or "size 0"),
            "candidates_raw": None, "candidates_kept": [], "candidates_rejected": [],
            "telemetry": tel,
        }, tel
    prompt = build_detect(c0, group)
    parsed, tel = model_call(run, sid, prompt, "detect")
    # A CALL THAT FAILED IS NOT A CALL THAT FOUND NOTHING. Measured live 2026-08-06: detect_B
    # starved (finish_reason `length`, content 0 bytes) and this function recorded it as
    # `candidates_raw: 0` -- byte-identical to an honest zero. That is the degraded_sources:[]
    # shape rebuilt one layer up, inside the harness written to prevent it. The distinction is
    # therefore a FIELD, not a log line, and it propagates to the adjudication contract:
    # zero candidates is a RESULT; a failed call is an ABSENCE OF MEASUREMENT.
    call_failed = parsed is None
    raw = (parsed or {}).get("candidates") or []
    canon = set(c0["canon_universe"])
    kept, rejected = [], []
    for cand in raw:
        if cand.get("entity") not in canon:
            rejected.append({**cand, "_rejected": "entity not in canon universe"})
        elif cand.get("field") not in PROSE_FIELDS:
            rejected.append({**cand, "_rejected": "field not in allowed prose fields"})
        else:
            kept.append(cand)
    return {
        "group": group,
        # SPEC s.4/s.5: the funnel must be VISIBLE. A run that failed and a run that found nothing
        # are different facts and are recorded as different fields.
        "status": "DETECT_FAILED" if call_failed else "OK",
        "unmeasured": call_failed,
        "stratum_status": c0["strata"][group]["status"],
        "call_outcome": tel.get("outcome"),
        "candidates_raw": None if call_failed else len(raw),
        "candidates_kept": kept,
        "candidates_rejected": rejected,
        "telemetry": tel,
    }, tel


_BOILERPLATE = {"stratum", "row", "rows", "label", "paths", "true", "false", "evidence_ref",
                "modified", "untracked", "the", "and", "for", "with", "ruling", "id", "is_canon"}


def distinctive_tokens(ref: str) -> set[str]:
    """The CONTENT-BEARING tokens of an evidence_ref -- entity names, path fragments, ids.

    Everything a fabricated citation could reproduce from FORMAT ALONE is excluded. A stratum row
    renders as `stratum row {"label": "producer:x", "paths": 4, "is_canon": true}`, so the first
    24 characters are pure boilerplate and shared by EVERY row.
    """
    raw = re.split(r"[^A-Za-z0-9_./:-]+", ref)
    out = set()
    for t in raw:
        t = t.strip(":.-/")
        if len(t) >= 6 and t.lower() not in _BOILERPLATE and not t.isdigit():
            out.add(t)
    return out


def evidence_resolves(cited: str, ref: str, nugget_ids: set[str]) -> bool:
    """Does `cited` actually point at the evidence, or merely LOOK like it does?

    MEASURED BROKEN 2026-08-06 and this is the repair. The original predicate was
    `ref[:24] in cited or cited[:24] in ref`, which accepted a wholly FABRICATED stratum row
    (`producer:NOPE-invented`) because the two strings share a 24-char format prefix. It passed
    7 of 7 live author calls and I recorded that as the control working -- it was the control
    being undiscriminating, and only a mutation revealed the difference.

    A PREFIX MATCH ON A STRUCTURED STRING TESTS THE FORMAT, NOT THE CONTENT. The repair requires
    at least one CONTENT-BEARING token to survive into the citation.
    """
    if not cited:
        return False
    if any(i and len(i) >= 6 and i in cited for i in nugget_ids):
        return True
    toks = distinctive_tokens(ref)
    if not toks:
        # Nothing distinctive to match against. FAIL CLOSED and say why -- an un-checkable
        # citation must not be silently promoted to a verified one.
        return False
    return any(t in cited for t in toks)


def step_author(run: Run, c0: dict, cand: dict, sid: str) -> tuple[dict, dict]:
    prompt = build_author(c0, cand)
    parsed, tel = model_call(run, sid, prompt, "author")
    p = parsed or {}
    cited = str(p.get("evidence_cited") or "")
    ref = str(cand.get("evidence_ref") or "")
    nugget_ids = {str(x.get("id")) for x in c0["nuggets"]}
    ok = evidence_resolves(cited, ref, nugget_ids)
    return {
        "candidate": cand,
        "proposal": p if ok else None,
        "discarded": None if ok else "evidence_cited does not resolve to the stated evidence_ref or a known ruling id",
        "evidence_cited": cited,
        "telemetry": tel,
    }, tel


# ===========================================================================================
# DRIVER
# ===========================================================================================
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", default=os.path.join(HERE, "kimi_run"))
    ap.add_argument("--live", action="store_true", help="perform vendor egress (needs Andrew's word)")
    ap.add_argument("--resume", action="store_true", help="replay cache, run only what is missing")
    ap.add_argument("--from", dest="frm", type=int, help="invalidate step N onward, then run")
    ap.add_argument("--only", type=int, help="run exactly one step number")
    ap.add_argument("--show", type=int, help="print a completed step's prompt + output")
    args = ap.parse_args()

    run = Run(args.run_dir, live=args.live)

    if args.show is not None:
        for sid in sorted(run.ledger["steps"]):
            if sid.startswith("%d_" % args.show):
                print("### %s -- %s" % (sid, run.ledger["steps"][sid]["name"]))
                p = run.path(sid, "prompt.txt")
                if os.path.exists(p):
                    t = open(p, encoding="utf-8").read()
                    print("\n--- PROMPT (%d chars) ---\n%s" % (len(t), t[:4000]))
                print("\n--- OUTPUT ---\n%s" % json.dumps(run.load_out(sid), indent=2)[:6000])
                return 0
        print("no completed step %s" % args.show)
        return 1

    if args.frm is not None:
        killed = run.invalidate_from(args.frm)
        print("invalidated: %s" % (", ".join(killed) or "(nothing)"))

    mode = "LIVE (vendor egress)" if args.live else "DRY-RUN (no egress; prompts built only)"
    print("=" * 78)
    print("SUBDIVIDED KIMI PIPELINE -- LOCAL STEP-RUNNER")
    print("mode    : %s" % mode)
    print("run dir : %s" % run.root)
    print("=" * 78)

    def want(n: int) -> bool:
        return args.only is None or args.only == n

    # ---------------- STEP 0 ----------------
    if want(0):
        if run.complete("0_compile") and args.resume:
            print("\n[0] compile          CACHED")
        else:
            print("\n[0] compile          running deterministic strata (no model) ...")
            t0 = time.monotonic()
            out = step0_compile(run)
            run.record("0_compile", "deterministic strata compilation", out,
                       {"elapsed_s": round(time.monotonic() - t0, 1), "model": False})
            print("    window %s | HEAD %s | %d commits" %
                  (out["window"], out["head"], out["commits_in_window"]))
            ah = out["attribution_health"]
            print("    canon universe : %d entities (predicate over the resolver) -- %s"
                  % (out["canon_universe_size"], "USABLE" if out["canon_usable"]
                     else "*** UNUSABLE ***"))
            print("    attribution    : %d threads, %d lambda, %d ec2 | degraded hops: %s"
                  % (ah["prod_to_thread"], ah["lambda_prefixes"], ah["ec2_prefixes"],
                     ah["degraded_hops"] or "none"))
            if not out["canon_usable"]:
                print("    *** DETECT CALLS WILL BE SKIPPED. With no canon universe every")
                print("        candidate is rejected by construction, so a zero would mean")
                print("        nothing. This is a BROKEN INPUT, not a clean day.")
            for g in ("D", "A", "B", "C"):
                s = out["strata"][g]
                print("    stratum %s : %-16s %s" % (
                    g, s["stratum"],
                    "%d rows" % s["row_count"] if s["status"] == "OK"
                    else "*** INSTRUMENT FAILED: %s" % (s["instrument_error"] or "")[:60]))
    c0 = run.load_out("0_compile") if run.complete("0_compile") else None

    # ---------------- STEP 1: NARRATE ----------------
    if want(1):
        run.gate("1_narrate", ["0_compile"])
        if run.complete("1_narrate") and args.resume:
            print("\n[1] narrate          CACHED")
        else:
            print("\n[1] narrate          gate OK (needs 0_compile) ...")
            out, tel = step_narrate(run, c0)
            run.record("1_narrate", "NARRATE -- plain-English brief", out, tel)
            print("    prompt %d chars | %s" % (tel["prompt_chars"], tel.get("outcome")))
            if out.get("brief"):
                print("    brief: %s" % out["brief"][:300])

    # ---------------- STEPS 2..5: DETECT ----------------
    detect_ids = {}
    for i, g in enumerate(("D", "A", "B", "C"), start=2):
        sid = "%d_detect_%s" % (i, g)
        detect_ids[g] = sid
        if not want(i):
            continue
        run.gate(sid, ["0_compile"])
        if run.complete(sid) and args.resume:
            print("\n[%d] detect %s        CACHED" % (i, g))
            continue
        print("\n[%d] detect %s        gate OK (needs 0_compile) ..." % (i, g))
        out, tel = step_detect(run, c0, g, sid)
        run.record(sid, "DETECT group %s" % g, out, tel)
        print("    prompt %d chars | %s | stratum=%s" %
              (tel["prompt_chars"], tel.get("outcome"), out["stratum_status"]))
        if out["unmeasured"]:
            print("    *** DETECT FAILED -- %s" % out["call_outcome"])
            print("    *** THIS GROUP IS UNMEASURED. It is NOT 'no drift found'. Adjudicating")
            print("        this day as clean would be a false negative with a real-looking zero.")
        else:
            print("    candidates: %d raw -> %d kept, %d REJECTED BY RUNNER" %
                  (out["candidates_raw"], len(out["candidates_kept"]),
                   len(out["candidates_rejected"])))
        for r in out["candidates_rejected"]:
            print("      REJECTED %s (%s)" % (r.get("entity"), r["_rejected"]))

    # ---------------- STEPS 6..N: AUTHOR ----------------
    if args.only is None or args.only >= 6:
        cands = []
        for g, sid in detect_ids.items():
            if run.complete(sid):
                for c in run.load_out(sid)["candidates_kept"]:
                    cands.append((g, c))
        if not cands:
            print("\n[6..N] author        ZERO CANDIDATES -- no author calls fire.")
            print("       A zero-candidate day costs nothing. This is the funnel working,")
            print("       not a failure. (Denominator: %d detect call(s) completed.)"
                  % sum(1 for s in detect_ids.values() if run.complete(s)))
        for j, (g, cand) in enumerate(cands, start=6):
            sid = "%d_author_%s_%d" % (j, g, j)
            if not want(j):
                continue
            run.gate(sid, ["0_compile", detect_ids[g]])
            if run.complete(sid) and args.resume:
                print("\n[%d] author %s        CACHED" % (j, cand.get("entity")))
                continue
            print("\n[%d] author           gate OK (needs 0_compile + %s)" % (j, detect_ids[g]))
            print("    entity=%s field=%s" % (cand.get("entity"), cand.get("field")))
            out, tel = step_author(run, c0, cand, sid)
            run.record(sid, "AUTHOR %s.%s" % (cand.get("entity"), cand.get("field")), out, tel)
            print("    prompt %d chars | %s" % (tel["prompt_chars"], tel.get("outcome")))
            if out["discarded"]:
                print("    DISCARDED BY RUNNER: %s" % out["discarded"])
            elif out["proposal"]:
                print("    proposed: %s" % str(out["proposal"].get("proposed_text"))[:250])

    # ---------------- LEDGER ----------------
    print("\n" + "=" * 78)
    print("RUN LEDGER")
    print("=" * 78)
    tot_prompt = tot_completion = tot_elapsed = 0
    for sid in sorted(run.ledger["steps"], key=lambda s: (int(s.split("_")[0]), s)):
        e = run.ledger["steps"][sid]
        bits = []
        if e.get("prompt_chars"):
            bits.append("prompt %6d ch" % e["prompt_chars"])
        if e.get("prompt_tokens"):
            bits.append("in %5d tok" % e["prompt_tokens"])
            tot_prompt += e["prompt_tokens"]
        if e.get("completion_tokens"):
            bits.append("out %5d tok" % e["completion_tokens"])
            tot_completion += e["completion_tokens"]
        if e.get("reasoning_pct") is not None:
            bits.append("reasoning %4.1f%%" % e["reasoning_pct"])
        if e.get("elapsed_s"):
            bits.append("%6.1fs" % e["elapsed_s"])
            tot_elapsed += e["elapsed_s"]
        print("  %-22s %-9s %s" % (sid, e["status"], "  ".join(bits)))
    if tot_prompt or tot_completion:
        print("\n  TOTAL: in %d tok | out %d tok | %.1fs wall across all model calls"
              % (tot_prompt, tot_completion, tot_elapsed))
    print("\n  artifacts: %s" % run.root)
    print("  inspect a step: python %s --show N" % os.path.basename(__file__))
    return 0


if __name__ == "__main__":
    sys.exit(main())
