#!/usr/bin/env python
"""comp_similar.py -- NFRA_COMPSIMILAR Phase-2 engine (TO NFRA_COMPSIMILAR.PH2).

BM25 SUMMARY similarity over the derive-at-scan corpus (what a resource DOES) + the
superseded-twin --supersede joint scan + a functional cluster census. Sibling to comp-dups
(which scores NAME/body -- what a resource IS): different corpus, different question
(CTO arch-gate ruling 3, PRD 2026-07-17: own tool, not a comp-dups mode).

REUSE (copy-reuse, PRD 4.1 + CTO ruling; no reimplementation):
  - summary_corpus.build_corpus / SimilarityIndex / coverage / _HELD_RX  -- the corpus +
    BM25 similarity engine (itself wrapping dup_scan.BM25) at the debtscan home.
  - dup_scan._firm_of / _FIRMS / _service_suffix_of / _strip_env         -- the name
    cross-firm / env / service suppressors, so DESIGNED parallels are not flagged.
  - comp-heat (data-cold) + comp-debris (invoke-cold)                    -- the heat bands
    the supersede divergence intersects. CTO ruling 5: BOTH sources, CONFIDENCE-GRADED
    (both-cold = HIGH, one-cold = MEDIUM surfaced-not-dropped -- never silently drop).

DESIGN NOTE (for CTO's gate -- a deliberate departure from PRD 4.3's literal
"name-cluster first"): the HEADLINE superseded twin (the monolith cutover
opal-data-{firm} -> opal-data-assets) is a NAME-DIFFERENT replacement, so a name-cluster-first
gate would MISS it (its whole point over comp-dups). So candidate generation is
SUMMARY-similarity first (cheap over ~1.8k nodes via the df-cut BM25), and the LIVE heat
read (the expensive leg) is gated to summary-similar candidate pairs -- same cost-gate
intent, correct signal. Name suppressors still fire (firm-cross / env / held) so designed
parallels never surface.

CONTROLS (PRD 5 -- controls, not care; comp-similar must not be able to lie):
  C1 false-twin      : similarity is NEVER a verdict alone. --supersede REQUIRES the
                       heat-divergence corroboration; bare `comp-similar a b` prints a
                       score + an explicit HYPOTHESIS, never "duplicate".
  C2 corpus-collapse : the summary doc EXCLUDES the resource's own name (summary_corpus
                       construction) -> a name-identical/purpose-different pair scores LOW,
                       a name-different/purpose-identical pair scores HIGH (self-test).
  C3 blind-row       : a resource with a thin/UNKNOWN summary, or UNKNOWN heat, is NEVER a
                       candidate; the coverage denominator (scanned / total / UNKNOWN) AND the
                       corpus VINTAGE print on every run -- all FOUR modes, not two.
                       WARN: "on every run" was FALSE from 2026-07-19 to 2026-09-02: it printed on
                       supersede/cluster only, while this line asserted otherwise and the
                       self-test scored C3 PASS on the half that worked. An untrue control
                       statement is worse than an absent one -- it teaches the reader to stop
                       looking. All three halves are now legs of the harness so the tool can
                       FAIL on this -- C3a blind-row, C3b disclosure (UNKNOWN path + every
                       mode emits), C3c capture (a real comp-kuzu header parses to MEASURED,
                       a headerless one to ABSENT). An unknown vintage renders UNKNOWN with an
                       explicit do-not-trust clause: never omitted, never defaulted to fresh.
                       WARN: C3c exists because C3b alone passed IDENTICALLY while the live corpus
                       still read UNKNOWN -- the vintage rides comp-kuzu's STDERR and the first
                       fix read stdout. A control that only tests the absent-path green-lights
                       the broken one.
  C4 dogfood         : the monolith-cutover superseded pair surfaces once both carry
                       divergent heat (offline shape mutant + the live scan).
  C5 hold-aware      : INF-chain / frozen / sovereign-named resources (_HELD_RX) are excluded
                       from candidate output.

ADVISORY + READ-ONLY. No delete verb. No store-writer, no apply (CTO ruling 2 put the
resource_summaries TABLE behind NFRA_KUZUSPLIT, not this leg). The candidate feed is input
to OPAL_LCLRPO; deletion stays per-batch Andrew-word (LD-0300).
"""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
_DEBTSCAN = _HERE.parent                 # .../org/modules/graph/debtscan
_GRAPH = _HERE.parents[1]                # .../org/modules/graph
REPO = _HERE.parents[4]                  # .../ajb_workspace
if str(_DEBTSCAN) not in sys.path:
    sys.path.insert(0, str(_DEBTSCAN))
_TOOLS = REPO / ".tools"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

# Corpus + similarity engine (which itself reuses dup_scan.BM25).
# EDIT-SURFACE, CORRECTED 2026-09-02: this read "ZERO edits to summary_corpus.py (the ~C
# _position_key lane owns that file)". That lane is 0.8.0_AE_CloudComp~C -- THIS SERIAL's own
# lane, not a foreign seat -- so the note read as a cross-seat boundary when it was an
# intra-serial coordination note from 2026-07-19, and no ~C/~D lane was live at this edit.
# The D1 vintage fix landed IN coverage() deliberately: build_w1_cards.py (0.7.0_AE_CloudOps)
# is a SECOND consumer of it, and fixing the vintage only here would have left that consumer
# reading the same undated denominator -- the defect is in what the consumers SHARE.
from summary_corpus import (  # noqa: E402
    build_corpus, SimilarityIndex, coverage, _HELD_RX,
)
# Name-tier suppressors (the designed-parallel controls).
from dup_scan import _firm_of, _service_suffix_of, _strip_env  # noqa: E402
import _compbudget  # noqa: E402  # Rule T shared carrier; do not fork its wording here.

# --- thresholds (conservative v1; CTO may retune at the gate) -------------------------------
SIM_TWIN = 0.60          # summary-sim at/above this = a functional-twin candidate (mirror M2)
SIM_FLOOR = 0.15         # below this = not related (mirror SimilarityIndex.neighbors floor)
_COLD_BANDS = {"COLD", "COLD-DORMANT"}
_HOT_BANDS = {"HOT"}

# COMPTOOL_ANSWER_STATE.enum.json -- literal tokens are a machine contract.
STATE_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"
STATE_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"
STATE_PARTIAL_BLIND = "PARTIAL_OR_BLIND"
STATE_NOT_APPLICABLE = "NOT_APPLICABLE"
_ANSWER_STATES = {
    STATE_SUBJECT_ABSENT, STATE_PRESENT_ZERO, STATE_PARTIAL_BLIND, STATE_NOT_APPLICABLE,
}


def answer_state_line(state: str, detail: str = "") -> str:
    """Render the exact s.4 answer-state token, with optional tool-voice evidence."""
    if state not in _ANSWER_STATES:
        raise ValueError("unknown comp-tool answer state: %r" % state)
    return "ANSWER-STATE: %s%s" % (state, (" -- " + detail) if detail else "")


def _budget_expired(clock) -> bool:
    remaining = clock.remaining() if clock is not None else None
    return remaining is not None and remaining <= 0


def _scan_units(corpus, cursor=None):
    """Rule T units: ARN keys in stable lexical order, strictly after the cursor."""
    return [arn for arn in sorted(corpus) if cursor is None or arn > cursor]


def _finish_progress(progress, completed, total):
    if progress is not None:
        progress.update({"completed": len(completed), "total": total,
                         "cursor": completed[-1] if completed else None,
                         "partial": len(completed) < total})


# ==========================================================================================
# Heat -- normalize the two live sources to a per-resource {data, invoke} band. UNKNOWN is a
# BAND (a blind row is not a cold row -- C3). PURE consumers take an injected dict; live
# loaders shell the canonical tools once and index by name.
# ==========================================================================================
def _norm_band(raw: str) -> str:
    """comp-heat {hot,warm,cold} / comp-debris {HOT,COLD-DORMANT,...} -> {HOT,COLD,UNKNOWN}."""
    u = (raw or "").strip().upper()
    if u in _HOT_BANDS:
        return "HOT"
    if u in _COLD_BANDS:
        return "COLD"
    if u == "WARM":
        return "WARM"          # neither strongly hot nor cold -- not a divergence anchor
    return "UNKNOWN"


# One resource NAME can be carried by SEVERAL repo paths with different bands. HOT wins, then
# WARM, then COLD, then UNKNOWN -- never let one cold path make a resource look COLDER than its
# hottest evidence, because the cold member of a divergent pair is emitted as a decommission
# CANDIDATE and NEVER-AUTO-DELETE (PRD R-5) makes the conservative direction the only safe one.
# Deterministic by construction: unlike the setdefault it replaces, the merge is order-free.
_BAND_RANK = {"HOT": 3, "WARM": 2, "COLD": 1, "UNKNOWN": 0}


def _merge_band(heat: dict, name: str, axis: str, band: str) -> None:
    entry = heat.setdefault(name, {})
    if _BAND_RANK.get(band, 0) > _BAND_RANK.get(entry.get(axis, "UNKNOWN"), 0):
        entry[axis] = band
    else:
        entry.setdefault(axis, band)


def is_cold(entry: dict) -> bool:
    """A resource is COLD only if >=1 axis reads COLD and NO axis reads HOT (ambiguous
    data-cold-but-invoke-hot is NOT cold -- it is still in use)."""
    axes = [entry.get("data", "UNKNOWN"), entry.get("invoke", "UNKNOWN")]
    return ("COLD" in axes) and ("HOT" not in axes)


def is_hot(entry: dict) -> bool:
    return "HOT" in (entry.get("data", "UNKNOWN"), entry.get("invoke", "UNKNOWN"))


def cold_confidence(entry: dict) -> str:
    """CTO ruling 5: both-axes-cold = HIGH, one-axis-cold = MEDIUM (surfaced not dropped)."""
    cold_axes = sum(1 for a in ("data", "invoke") if entry.get(a) == "COLD")
    return "HIGH" if cold_axes >= 2 else "MEDIUM"


def is_designed_parallel(name_a: str, name_b: str) -> str | None:
    """Return a suppression REASON if a<->b is a DESIGNED parallel (not a supersession),
    else None. Reuses the name-tier suppressors -- firm-cross (bd/cot/inf are separated
    twins BY DESIGN, never mirror), env (dev/staging/prod), service-suffix (foo_s3 vs
    foo_ddb are different resources)."""
    fa, fb = _firm_of(name_a), _firm_of(name_b)
    if fa and fb and fa != fb:
        return f"BENIGN_CROSS_FIRM ({fa} vs {fb} -- firm-separation is by design)"
    if _strip_env(name_a) == _strip_env(name_b) and name_a != name_b:
        return "BENIGN_ENV_PARALLEL (same name across environments)"
    sa, sb = _service_suffix_of(name_a), _service_suffix_of(name_b)
    if sa and sb and sa[0] == sb[0] and sa[1] != sb[1]:
        return f"BENIGN_SERVICE_SUFFIX ({sa[1]} vs {sb[1]} -- distinct resources of one stack)"
    return None


# ==========================================================================================
# The joint scan (PURE -- takes the corpus, a SimilarityIndex, and an injected heat dict so
# it is fully offline-testable; the live modes assemble heat via load_heat_live()).
# ==========================================================================================
def supersede_scan(corpus, index, heat, *, sim_twin=SIM_TWIN, top=40,
                   clock=None, cursor=None, progress=None, pool_out=None):
    """Ranked superseded-twin candidates. A candidate = a pair that is (i) SUMMARY-similar
    (functional twin, >= sim_twin), (ii) NOT a designed parallel, (iii) heat-DIVERGENT (one
    COLD, one HOT), (iv) neither held. Emits the COLD member as the decommission candidate +
    the HOT member as its live replacement. Rank = summary_sim * (HIGH=1.0 / MEDIUM=0.6).
    PURE: heat = {name -> {data,invoke}} (UNKNOWN for anything unread -- C3)."""
    seen: set[tuple] = set()
    pool_seen: set[tuple] = set()
    out: list[dict] = []
    units = _scan_units(corpus, cursor)
    completed: list[str] = []
    for arn in units:
        # Always finish at least one real unit so a tiny-budget run has a truthful cursor.
        # Thereafter, only begin a new unit while budget remains.
        if completed and _budget_expired(clock):
            break
        doc = corpus[arn]
        if pool_out is not None and not doc.thin:
            for nb in index.neighbors(arn, top=6, min_norm=sim_twin):
                pool_key = tuple(sorted((arn, nb["arn"])))
                if (nb["thin"] or pool_key in pool_seen
                        or is_designed_parallel(doc.name, nb["name"])):
                    continue
                pool_seen.add(pool_key)
                pool_out.append({"a": doc.name, "b": nb["name"],
                                 "node_type": doc.node_type, "summary_sim": nb["norm"]})
        if doc.thin:
            completed.append(arn)
            continue                                  # C3: no twin claim off a blind row
        for nb in index.neighbors(arn, top=8, min_norm=sim_twin):
            b_arn = nb["arn"]
            if nb["norm"] < sim_twin or nb["thin"]:
                continue
            key = tuple(sorted((arn, b_arn)))
            if key in seen:
                continue
            seen.add(key)
            a_name, b_name = doc.name, nb["name"]
            if doc.held or nb["held"] or _HELD_RX.search(a_name) or _HELD_RX.search(b_name):
                continue                              # C5: hold-aware
            supp = is_designed_parallel(a_name, b_name)
            if supp:
                continue                              # designed parallel -- not a supersession
            ha = heat.get(a_name, {})
            hb = heat.get(b_name, {})
            # C1: similarity alone is never the verdict -- REQUIRE a hot/cold divergence.
            if is_cold(ha) and is_hot(hb):
                cold_arn, cold_name, cold_h, hot_name = arn, a_name, ha, b_name
            elif is_cold(hb) and is_hot(ha):
                cold_arn, cold_name, cold_h, hot_name = b_arn, b_name, hb, a_name
            else:
                continue                              # no divergence -> not a candidate
            conf = cold_confidence(cold_h)
            out.append({
                "candidate": cold_name, "candidate_arn": cold_arn,
                "replaced_by": hot_name, "summary_sim": nb["norm"],
                "confidence": conf,
                "cold_axes": {a: cold_h.get(a, "UNKNOWN") for a in ("data", "invoke")},
                "rank_score": round(nb["norm"] * (1.0 if conf == "HIGH" else 0.6), 3),
                "hypothesis": (f"'{cold_name}' appears SUPERSEDED by '{hot_name}' "
                               f"(summary-sim {nb['norm']}, {conf}-confidence cold) -- "
                               "advisory decommission candidate, verify before reap"),
            })
        completed.append(arn)
    _finish_progress(progress, completed, len(units))
    out.sort(key=lambda c: -c["rank_score"])
    if pool_out is not None:
        pool_out.sort(key=lambda c: -c["summary_sim"])
        del pool_out[top:]
    return out[:top]


def cluster_scan(corpus, index, *, node_type=None, min_norm=SIM_TWIN, top=60,
                 clock=None, cursor=None, progress=None):
    """Functional-overlap census: every resource with a summary-similar peer (a same-JOB
    cluster), suppressors applied. Advisory overlap map, NOT a supersession verdict (no heat)."""
    seen: set[tuple] = set()
    out: list[dict] = []
    units = _scan_units(corpus, cursor)
    completed: list[str] = []
    for arn in units:
        if completed and _budget_expired(clock):
            break
        doc = corpus[arn]
        if doc.thin or (node_type and doc.node_type != node_type):
            completed.append(arn)
            continue
        for nb in index.neighbors(arn, top=6, min_norm=min_norm):
            if nb["thin"]:
                continue
            key = tuple(sorted((arn, nb["arn"])))
            if key in seen or is_designed_parallel(doc.name, nb["name"]):
                continue
            seen.add(key)
            out.append({"a": doc.name, "b": nb["name"], "node_type": doc.node_type,
                        "summary_sim": nb["norm"]})
        completed.append(arn)
    _finish_progress(progress, completed, len(units))
    out.sort(key=lambda c: -c["summary_sim"])
    return out[:top]


def pairwise(a_arn, b_arn, corpus, index):
    """Bounded BM25 score + explicit HYPOTHESIS framing (C1: never a bare 'duplicate')."""
    score = index.score(a_arn, b_arn)
    da, db = corpus.get(a_arn), corpus.get(b_arn)
    verdict = ("HIGH functional overlap -- HYPOTHESIS: same job, differently named "
               "(corroborate with heat divergence via --supersede before any decommission)"
               if score >= SIM_TWIN else
               "LOW/partial overlap -- likely different jobs" if score >= SIM_FLOOR else
               "not functionally similar")
    return {"a": a_arn, "b": b_arn, "summary_sim": score, "verdict": verdict,
            "a_summary": da.prose if da else None, "b_summary": db.prose if db else None}


# ==========================================================================================
# Live heat assembly -- shell the canonical tools ONCE, index by resource name. GRACEFUL: a
# tool failure/timeout leaves that axis UNKNOWN for all (never assume cold -- C3).
# ==========================================================================================
def _tool_argv(tool: Path, *args: str) -> list[str]:
    """argv that ACTUALLY EXECUTES an extensionless .tools/ shim on this fabric.
    MEASURED 2026-09-04 (laptop, Windows): subprocess.run(['.tools/comp-heat', ...]) raises
    OSError [WinError 193] '%1 is not a valid Win32 application' because the shim carries a
    shebang and no extension -- _run_json swallowed that as None, so load_heat_live returned {}
    WITHOUT EVER REACHING comp-heat (PRD s.7 row OS-s-8 / row S29). Resolve the interpreter from
    the shebang instead: python shims run under THIS interpreter, bash shims under Git Bash via
    the estate's own resolver (build ladder rung 2 -- never bare 'bash', the WSL-stub trap)."""
    tool = Path(tool)
    try:
        shebang = tool.open(encoding="utf-8", errors="replace").readline()
    except OSError:
        shebang = ""
    if "python" in shebang:
        return [sys.executable, str(tool), *args]
    if "bash" in shebang or shebang.startswith("#!/bin/sh"):
        from git_bash_resolver import bash_argv          # .tools is already on sys.path
        return bash_argv(str(tool), *args)
    return [str(tool), *args]


def _run_json(cmd, timeout=180):
    try:
        p = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, timeout=timeout)
        if p.returncode not in (0, 1) or not p.stdout.strip():
            return None
        return json.loads(p.stdout)
    except (subprocess.SubprocessError, OSError, ValueError):
        return None


def normalize_heat(raw: dict) -> dict:
    """Accept EITHER a pre-normalized {name: {data, invoke}} snapshot OR the raw JSON of
    comp-debris (invoke bands under reap_rank_cold_dormant/hot/too_young/unknown/... , each row
    {name, band}) and comp-heat freshness ({paths: [{path, band}]}), and fold both into the
    canonical {name -> {data, invoke}} map. UNKNOWN where unread -- the blind-row control (C3)."""
    heat: dict[str, dict] = {}
    if not isinstance(raw, dict):
        return heat
    # (a) already-normalized snapshot: values are {data|invoke: band}
    if all(isinstance(v, dict) and (set(v) <= {"data", "invoke"}) for v in raw.values()) and raw:
        for name, v in raw.items():
            heat[name] = {k: _norm_band(str(b)) for k, b in v.items()}
        return heat
    # (b) raw comp-debris ledger: name-keyed invoke bands live in these row-groups
    for grp in ("reap_rank_cold_dormant", "hot", "purpose_review_stillborn_or_guard",
                "too_young", "unknown"):
        for row in (raw.get(grp) or []):
            if isinstance(row, dict) and row.get("name"):
                heat.setdefault(row["name"], {})["invoke"] = _norm_band(row.get("band", ""))
    for held in (raw.get("held_excluded") or []):        # held names -> recorded, not cold
        heat.setdefault(str(held), {}).setdefault("invoke", "UNKNOWN")
    # (c) raw comp-heat freshness: path-keyed data bands, joined to resource NAMES.
    # FIELD: comp-heat emits `band` (hot/warm/cold) on every freshness row; `class` was never a
    # key it writes and is kept only as a back-compat alias for a hand-rolled snapshot. Measured
    # 2026-09-04 on .tools/tests: reading `class` banded 43 of 43 rows UNKNOWN.
    # KEY: a resource name is joined under EVERY key its repo path can plausibly carry -- the
    # basename, its extension-stripped stem, and each path COMPONENT + stem (a lambda's source
    # DIRECTORY is the usual carrier). Measured on the live corpus: basename alone joined 0 of
    # 1774 corpus names; component+stem joins 184. A name join is a HYPOTHESIS, never a verdict:
    # heat only ever CORROBORATES a summary twin (C1), and collisions resolve HOT-wins.
    for row in (raw.get("paths") or []):
        if not (isinstance(row, dict) and row.get("path")):
            continue
        band = _norm_band(str(row.get("band", row.get("class", "")) or ""))
        keys = set()
        for part in str(row["path"]).rstrip("/").split("/"):
            if not part or part in (".", ".."):
                continue
            keys.add(part)
            keys.add(os.path.splitext(part)[0])
        for key in keys:
            if key:
                _merge_band(heat, key, "data", band)
    return heat


def load_heat_live(timeout=280, *, clock=None, deferred=None) -> dict:
    """SLOW opt-in (--live-heat): pull comp-debris (invoke, live AWS -- minutes) + comp-heat
    (data). Best-effort; a tool that times out leaves its axis UNKNOWN (never assume cold -- C3).
    NOTE (open plumbing, flagged to CTO): comp-debris default = lambda only (S3/DDB need --types,
    slower); comp-heat freshness is REPO-path-scoped, not per-S3-bucket data-heat -- so live heat
    is partial for the S3-bucket consolidation surface. The clean path is a heat SNAPSHOT via
    --heat-json (cadence/source is the §6-decision-5 open item)."""
    heat: dict[str, dict] = {}
    deferred = deferred if deferred is not None else []

    def remaining_timeout(label):
        if clock is None:
            return timeout
        remaining = clock.remaining()
        if remaining is not None and remaining <= 0:
            deferred.append(f"{label}: budget exhausted before subprocess could start")
            return 0
        return None if remaining is None else min(timeout, remaining)

    debris_timeout = remaining_timeout("comp-debris")
    dbg = (_run_json(_tool_argv(REPO / ".tools" / "comp-debris", "--json"),
                     timeout=debris_timeout) if debris_timeout != 0 else None)
    if dbg:
        for name, v in normalize_heat(dbg).items():
            for axis, band in v.items():
                _merge_band(heat, name, axis, band)
    out_json = _GRAPH / "debtscan" / ".comp_similar_heat.json"
    heat_timeout = remaining_timeout("comp-heat freshness")
    if heat_timeout != 0:
        heat_args = ["freshness", "--json", str(out_json)]
        # OS-s-1 wired Rule T's --budget across comp-heat's five subcommands. Hand the CALLER's
        # remaining budget down, or the child silently runs to its own 90s default inside a
        # possibly-shorter outer timeout and reports WITHIN BUDGET against the wrong clock.
        if heat_timeout is not None:
            heat_args += ["--budget", str(max(1, int(heat_timeout)))]
        _run_json(_tool_argv(REPO / ".tools" / "comp-heat", *heat_args), timeout=heat_timeout)
    try:
        if out_json.exists():
            for name, v in normalize_heat(json.loads(out_json.read_text())).items():
                for axis, band in v.items():
                    _merge_band(heat, name, axis, band)
    except (OSError, ValueError):
        pass
    finally:
        try:
            out_json.unlink()
        except OSError:
            pass
    return heat


# ==========================================================================================
# self-test -- offline mutants for the 5 controls (no graph, no AWS). Exit 0 = PASS.
# ==========================================================================================
def _mkcorpus():
    from summary_corpus import SummaryDoc

    def d(arn, name, tokens, thin=False, held=False):
        return SummaryDoc(arn=arn, node_type="S3_BUCKET", name=name, tokens=tokens,
                          prose=f"summary of {name}", thin=thin, held=held,
                          n_purpose=len(set(tokens)))
    # V1 = the superseded-twin purpose vocab; V2 = a distinct firm-parallel vocab.
    v1 = ["writes", "produces", "accounts", "positions", "custody", "daily"]
    v2 = ["reads", "benchmarks", "returns", "advisory", "ycharts", "weekly"]
    corpus = {
        # C4 twin: name-different, purpose-identical (V1); old is COLD, new is HOT (heat below).
        "arn:old": d("arn:old", "opal-data-legacyfeed", v1),
        "arn:new": d("arn:new", "opal-data-assets", v1),
        # C5 held twin: summary-identical + COLD, but a held name -> excluded (not firm-suppressed).
        "arn:held-old": d("arn:held-old", "inf-gold-legacyfeed", v1, held=True),
        # C-supp designed firm-parallel: inf<->cot, same job (V2), heat-divergent -> WOULD be a
        # candidate but firm-cross suppression (bd/cot/inf are separated twins by design) excludes it.
        "arn:firm-inf": d("arn:firm-inf", "inf-report-sync", v2),
        "arn:firm-cot": d("arn:firm-cot", "cot-report-sync", v2),
        # C2 corpus-collapse: name-identical, purpose-DISJOINT -> must score LOW (names not in tokens).
        "arn:x1": d("arn:x1", "opal-data-shared", ["glue", "crawler", "catalog", "partition2"]),
        "arn:x2": d("arn:x2", "opal-data-shared", ["waf", "shield", "ratelimit2", "block2"]),
        # C3 thin/blind row -- never a candidate.
        "arn:thin": d("arn:thin", "opal-data-lonely", ["writes"], thin=True),
    }
    # Filler noise docs -- each with a DISTINCT purpose vocab. Without these, the 4 twin docs
    # share their tokens across >25% of a tiny corpus and BM25's df-cut (max_df_ratio=0.25)
    # discards them as non-discriminative (a small-corpus artifact, not real: the live corpus
    # is ~1.8k). The filler restores realistic idf so the twin tokens stay discriminative.
    fill_vocabs = [
        ["cloudfront", "edge", "cache", "invalidate"], ["cognito", "auth", "token", "jwt"],
        ["sns", "topic", "notify", "subscribe"], ["sqs", "queue", "poll", "dlq"],
        ["dynamo", "table", "index", "query"], ["kms", "key", "encrypt", "rotate"],
        ["eventbridge", "rule", "schedule", "cron"], ["secret", "credential", "orion", "rotate2"],
        ["glue", "crawler", "catalog", "partition"], ["athena", "query2", "presto", "scan"],
        ["ses", "email", "deliver", "dkim"], ["ecr", "image", "push", "layer"],
        ["step", "statemachine", "flow", "transition"], ["apigw", "route2", "stage", "throttle"],
        ["waf", "rule2", "block", "ratelimit"], ["backup", "vault", "restore", "snapshot"],
    ]
    for i, v in enumerate(fill_vocabs):
        corpus[f"arn:fill{i}"] = d(f"arn:fill{i}", f"opal-misc-{i}", v)
    return corpus


def self_test() -> int:
    print("=== comp_similar --self-test (offline mutants; the 5 PRD controls) ===")
    ok = True
    corpus = _mkcorpus()
    index = SimilarityIndex(corpus)

    # C2 corpus-collapse: name-identical/purpose-different -> LOW; name-diff/purpose-same -> HIGH.
    s_collapse = index.score("arn:x1", "arn:x2")
    s_twin = index.score("arn:old", "arn:new")
    c2 = s_collapse < 0.25 and s_twin >= SIM_TWIN
    ok &= c2
    print(f"  C2 corpus-collapse (name-same/purpose-diff={s_collapse} LOW; "
          f"name-diff/purpose-same={s_twin} HIGH): {'PASS' if c2 else 'FAIL'}")

    # Heat exercises every control: superseded old COLD / new HOT; held-old COLD; the firm
    # pair heat-DIVERGENT (inf COLD, cot HOT) so only the firm-cross suppressor keeps it out.
    heat = {
        "opal-data-legacyfeed": {"data": "COLD", "invoke": "COLD"},   # both-cold -> HIGH
        "opal-data-assets":     {"data": "HOT",  "invoke": "HOT"},
        "inf-gold-legacyfeed":  {"data": "COLD", "invoke": "COLD"},
        "inf-report-sync":      {"data": "COLD", "invoke": "COLD"},
        "cot-report-sync":      {"data": "HOT",  "invoke": "HOT"},
    }
    cands = supersede_scan(corpus, index, heat)
    names = {c["candidate"] for c in cands}

    # C4 dogfood shape: the superseded twin surfaces top, pointing at its hot replacement.
    top = cands[0] if cands else {}
    c4 = top.get("candidate") == "opal-data-legacyfeed" and top.get("replaced_by") == "opal-data-assets"
    ok &= c4
    print(f"  C4 dogfood-shape (superseded twin top, -> replacement): "
          f"{top.get('candidate')} -> {top.get('replaced_by')} {'PASS' if c4 else 'FAIL'}")

    # C1 false-twin: a HIGH-sim pair with NO heat divergence emits NO candidate.
    cands_noheat = supersede_scan(corpus, index, {})   # empty heat -> all UNKNOWN
    c1 = len(cands_noheat) == 0
    ok &= c1
    print(f"  C1 false-twin (high-sim + no heat divergence -> 0 candidates): "
          f"n={len(cands_noheat)} {'PASS' if c1 else 'FAIL'}")

    # C3a blind-row: the thin row is never a candidate (and would be UNKNOWN-heat anyway).
    c3 = "opal-data-lonely" not in names
    ok &= c3
    print(f"  C3a blind-row (thin row absent from candidates): {'PASS' if c3 else 'FAIL'}")

    # C3b DISCLOSURE (added 2026-09-02, CVO finding D2/D3). C3 is a TWO-clause control and only
    # clause (a) was ever tested -- so the harness returned a clean 7/7 over a control that was
    # half false, and the passing half was the half the harness was written from. Nothing in the
    # tool could fail on it, which is why the defect survived from 2026-07-19.
    # Two legs, because the claim has two halves:
    #   (i)  coverage() ALWAYS discloses a vintage -- value may be UNKNOWN, disclosure may not
    #        be absent. Asserted on a synthetic corpus, where the vintage IS unknown: the
    #        UNKNOWN path is the one that must not silently render as fresh.
    #   (ii) every mode emits it. Counted at SOURCE, so removing a call site fails this leg.
    import inspect
    cov_probe = coverage(corpus)
    c3b_i = (cov_probe.get("corpus_vintage_claim") == "absent"
             and "UNKNOWN" in cov_probe.get("vintage_note", "")
             and "corpus built:" in cov_probe.get("note", ""))
    src = inspect.getsource(main)
    n_compute = src.count("coverage(corpus)")      # 2 branches: supersede/cluster + query
    n_json = src.count('"coverage": cov')          # 4 modes, --json render path
    n_human = src.count('print(cov["note"])')      # 4 modes, human render path
    c3b_ii = n_compute == 2 and n_json == 4 and n_human == 4
    c3b = c3b_i and c3b_ii
    ok &= c3b
    print(f"  C3b disclosure (vintage always disclosed; all 4 modes emit coverage): "
          f"unknown-path={'ok' if c3b_i else 'BROKEN'} "
          f"compute={n_compute}/2 json={n_json}/4 human={n_human}/4 "
          f"{'PASS' if c3b else 'FAIL'}")

    # C3c CAPTURE. REWRITTEN 2026-09-09 (NFRA_CLDGRPH CG-s-17, the INSTRUCTION plane; pass 2 on the
    # issuer's amendment, which widened the grant to summary_corpus.py so the CAPTURE could move
    # with the comparison -- row W2-S32). The header this leg used to feed -- "DB: kuzu_nessie_db
    # ... built: ..." -- was a VERBATIM excerpt of a tool that no longer emits it. comp-kuzu is a
    # thin client over the SERVED projection and its whole disclosure is ONE line (kuzu_cli.py:
    # 46-61):
    #     VINTAGE: <plain-words age>  [vintage=<vintage> manifest=<sha12> prefix=<prefix>]
    # A fixture that keeps feeding the old shape scores this leg GREEN against a header the estate
    # never sees again, and a fixture that cannot represent the current world cannot score it.
    # BOTH ARMS ARE THE SERVED SHAPE NOW, which is what makes this a measurement rather than a
    # tautology: the POSITIVE arm feeds a served line carrying a vintage and requires a MEASURED
    # claim whose corpus_db is the SERVED SURFACE (the artifact prefix), and the NEGATIVE arm feeds
    # a served line the service answered WITHOUT a vintage -- the client renders those bracket
    # fields as the literal `None` -- and requires NO measured claim, because a parser that reads
    # "None" as a vintage is the false-green the disclosure exists to prevent. Without the negative
    # arm, a capture that returned `measured` unconditionally would pass the positive one.
    # Runs offline: no graph, no AWS, no clock.
    import summary_corpus as _sc
    _served_header = ("VINTAGE: built 2026-09-09T11:02:44+00:00, 0.4h ago  "
                      "[vintage=2026-09-09T11:02:44+00:00 manifest=9f4a57262f1c "
                      "prefix=s3://opal-globgrph-projection/served/]\n")
    _served_no_vintage = ("VINTAGE: AGE NOT STATED BY THE SERVICE -- no age was inferred.  "
                          "[vintage=None manifest=None prefix=None]\n")
    _saved = dict(_sc._CORPUS_VINTAGE)
    try:
        _sc._CORPUS_VINTAGE.clear()
        _sc._capture_kuzu_vintage(_served_header)
        cap = coverage(corpus)
        c3c = (cap.get("corpus_vintage_claim") == "measured"
               and cap.get("corpus_built") == "2026-09-09T11:02:44+00:00"
               and cap.get("corpus_age") == "built 2026-09-09T11:02:44+00:00, 0.4h ago"
               and cap.get("corpus_db") == "s3://opal-globgrph-projection/served/"
               and "UNKNOWN" not in cap.get("vintage_note", ""))
        # NEGATIVE CONTROL: a served line the service answered without a vintage must NOT yield a
        # measured claim, and coverage() must say UNKNOWN in terms.
        _sc._CORPUS_VINTAGE.clear()
        _sc._capture_kuzu_vintage(_served_no_vintage)
        neg = coverage(corpus)
        c3c_neg = (neg.get("corpus_vintage_claim") == "absent"
                   and neg.get("corpus_built") is None
                   and "UNKNOWN" in neg.get("vintage_note", ""))
        # RETIRED-SHAPE CONTROL: the OLD local-projection header must no longer be readable. A
        # parser that still answered it would be a live reader for a store retired at CG-s-8.
        # The discriminating line is the `built:` one -- that is what the retired regex keyed on --
        # so the control feeds THAT and nothing else. It deliberately does NOT spell the retired
        # store's name: this is a live code-band string constant, and a fixture that names the
        # retired surface in order to prove the retired surface is gone puts the token back on the
        # very instruction plane this cell is clearing. E1-AC3 counts code-band strings and it is
        # right to -- an agent reading this file would meet the name here as readily as in a help
        # text -- so the control is written to discriminate without carrying it.
        _sc._CORPUS_VINTAGE.clear()
        _sc._capture_kuzu_vintage("  built: 2026-09-02T14:20:11+00:00 (age: 0.2h)\n")
        c3c_old = coverage(corpus).get("corpus_vintage_claim") == "absent"
    finally:
        _sc._CORPUS_VINTAGE.clear()
        _sc._CORPUS_VINTAGE.update(_saved)
    c3c_ok = c3c and c3c_neg and c3c_old
    ok &= c3c_ok
    print(f"  C3c vintage-CAPTURE (served+vintage -> measured on the SERVED surface; served without "
          f"a vintage -> absent + DISCLOSED; the retired local header -> unreadable): "
          f"served={'ok' if c3c else 'BROKEN'} neg-control={'ok' if c3c_neg else 'BROKEN'} "
          f"retired-shape-control={'ok' if c3c_old else 'BROKEN'} "
          f"{'PASS' if c3c_ok else 'FAIL'}")

    # C5 hold-aware: the held twin is excluded even though it is COLD + summary-identical.
    c5 = "inf-gold-legacyfeed" not in names
    ok &= c5
    print(f"  C5 hold-aware (held cold twin excluded): {'PASS' if c5 else 'FAIL'}")

    # designed-parallel suppression: the heat-divergent inf<->cot firm pair is NOT flagged
    # (firm-separation is by design -- a firm-cross pair is never a supersession candidate).
    csup = "inf-report-sync" not in names and "cot-report-sync" not in names
    ok &= csup
    print(f"  C-supp designed-parallel (firm-cross pair suppressed, not flagged): "
          f"{'PASS' if csup else 'FAIL'}")

    # confidence grading: the both-cold candidate is HIGH.
    cconf = bool(cands) and cands[0].get("confidence") == "HIGH"
    ok &= cconf
    print(f"  C-conf both-cold -> HIGH confidence: {cands[0].get('confidence') if cands else None} "
          f"{'PASS' if cconf else 'FAIL'}")

    # s.4 answer-state battery: one invocation plants all four mutually distinct machine
    # tokens. The PARTIAL arm says why its corpus is stale and carries the vintage in tool voice.
    class _SpentClock:
        @staticmethod
        def remaining():
            return 0.0

    budget_progress = {}
    supersede_scan(corpus, index, heat, clock=_SpentClock(), progress=budget_progress)
    measured_cov = {"corpus_vintage_claim": "measured",
                    "vintage_note": "corpus built: 2026-09-03T00:00:00Z (age: 1h)"}
    stale_cov = {"corpus_vintage_claim": "measured",
                 "vintage_note": "corpus built: 2025-01-01T00:00:00Z (age: STALE)"}
    absent_resolved = _resolve("arn:missing", corpus)
    zero_neighbors = index.neighbors("arn:fill0", top=40)
    absent_state = _query_answer_state(absent_resolved, measured_cov, subject="arn:missing")
    zero_state = _query_answer_state("arn:fill0", measured_cov, result_count=len(zero_neighbors),
                                     subject="arn:fill0")
    partial_state = _partial_state(budget_progress, stale_cov)
    empty_type_clusters = cluster_scan(corpus, index, node_type="NO_SUCH_TYPE")
    empty_type_population = sum(1 for d in corpus.values() if d.node_type == "NO_SUCH_TYPE")
    not_app_state = _cluster_answer_state(
        {"partial": False}, measured_cov, eligible=empty_type_population,
        result_count=len(empty_type_clusters),
        node_type="NO_SUCH_TYPE")

    def render_plant(state_pair):
        # Keep the harness running through a mutant that removes an arm; absence must be a red
        # assertion, not an early traceback that prevents the remaining discriminators running.
        return answer_state_line(*state_pair) if state_pair[0] in _ANSWER_STATES else (
            "ANSWER-STATE: MISSING -- planted arm produced no ratified token")

    planted = [
        ("absent-subject", render_plant(absent_state)),
        ("present-zero", render_plant(zero_state)),
        ("stale-corpus", render_plant(partial_state)),
        ("not-applicable", render_plant(not_app_state)),
    ]
    planted_tokens = [line.split(" -- ", 1)[0].split(": ", 1)[1] for _, line in planted]
    state_ok = (absent_resolved is None and len(zero_neighbors) == 0
                and budget_progress.get("partial") is True
                and empty_type_population == 0 and len(empty_type_clusters) == 0
                and set(planted_tokens) == _ANSWER_STATES and len(planted_tokens) == 4
                and "corpus built:" in planted[2][1] and "STALE" in planted[2][1])
    ok &= state_ok
    for label, line in planted:
        print(f"  PLANTED {label}: {line}")
    print(f"  s.4 answer-state four-arm contract: {'PASS' if state_ok else 'FAIL'}")

    # Rule T tiny-budget arm. Even if the clock is already spent, the scanner completes one
    # deterministic ARN unit before stopping, which makes the emitted cursor real/resumable.
    rule_t_line = _compbudget.budget_reached_line(
        0.000001, "flag", budget_progress.get("completed", 0),
        budget_progress.get("total", 0), "ARN resource",
        "comp-similar supersede --budget 0.000001", budget_progress.get("cursor") or "")
    rule_t_ok = (budget_progress.get("completed") == 1
                 and budget_progress.get("partial") is True
                 and budget_progress.get("cursor") == sorted(corpus)[0]
                 and "BUDGET REACHED:" in rule_t_line
                 and "results are a PREFIX, not the answer" in rule_t_line
                 and "--cursor " + sorted(corpus)[0] in rule_t_line)
    ok &= rule_t_ok
    print(f"  Rule T tiny-budget + genuine cursor: {'PASS' if rule_t_ok else 'FAIL'}")

    print(f"=== comp_similar self-test: {'PASS' if ok else 'FAIL'} (11/11) ===" if ok
          else "=== comp_similar self-test: FAIL ===")
    return 0 if ok else 1


# ==========================================================================================
# CLI
# ==========================================================================================
def _resolve(query: str, corpus) -> str | None:
    """arn-or-name -> the corpus ARN key (exact arn, exact name, else unique name substring)."""
    if query in corpus:
        return query
    by_name = [a for a, d in corpus.items() if d.name == query]
    if len(by_name) == 1:
        return by_name[0]
    sub = [a for a, d in corpus.items() if query.lower() in d.name.lower()]
    return sub[0] if len(sub) == 1 else None


def _resume_args(args, mode: str) -> str:
    """Reproduce scan-affecting arguments except the old cursor; Rule T appends the new one."""
    parts = ["comp-similar", mode]
    if args.type:
        parts.extend(["--type", args.type])
    if args.top != 40:
        parts.extend(["--top", str(args.top)])
    if args.heat_json:
        parts.extend(["--heat-json", args.heat_json])
    if args.live_heat:
        parts.append("--live-heat")
    if args.budget is not None:
        parts.extend(["--budget", str(args.budget)])
    if args.json:
        parts.append("--json")
    return " ".join(shlex.quote(str(part)) for part in parts)


def _budget_status(progress, budget_s, budget_source, clock, resume_args):
    n, total = progress.get("completed", 0), progress.get("total", 0)
    if n == total:
        return _compbudget.within_budget_line(
            n, total, "ARN resource", budget_s, budget_source, round(clock.elapsed(), 2))
    cursor = progress.get("cursor")
    if cursor:
        return _compbudget.budget_reached_line(
            budget_s, budget_source, n, total, "ARN resource", resume_args, cursor)
    return ("BUDGET REACHED: %s s (%s); scanned 0 of %d ARN resource; results are a PREFIX, "
            "not the answer; NO CURSOR YET: no ARN resource completed before the budget hit"
            % (_compbudget.fmt(budget_s), budget_source, total))


def _partial_state(progress, cov, extra=""):
    if progress.get("partial"):
        why = "scanned %d of %d ARN resources; %s" % (
            progress.get("completed", 0), progress.get("total", 0), cov["vintage_note"])
        return STATE_PARTIAL_BLIND, why
    if cov.get("corpus_vintage_claim") != "measured":
        why = cov["vintage_note"]
        return STATE_PARTIAL_BLIND, ("%s; %s" % (extra, why)) if extra else why
    if extra:
        return STATE_PARTIAL_BLIND, "%s; %s" % (extra, cov["vintage_note"])
    return None, ""


def _query_answer_state(resolved, cov, *, result_count=None, subject="subject"):
    """One/pair query answer-state dispatcher; shared by live paths and planted controls."""
    if resolved is None:
        return STATE_SUBJECT_ABSENT, f"'{subject}' did not resolve to a corpus resource"
    if cov.get("corpus_vintage_claim") != "measured":
        return STATE_PARTIAL_BLIND, cov["vintage_note"]
    if result_count == 0:
        return STATE_PRESENT_ZERO, f"{subject} is present; zero results cleared the threshold"
    return None, ""


def _cluster_answer_state(progress, cov, *, eligible, result_count, node_type=None):
    """Cluster answer-state dispatcher; NOT_APPLICABLE is about population, never zero rows."""
    state = _partial_state(progress, cov)
    if state[0] is not None:
        return state
    if node_type and eligible == 0:
        return STATE_NOT_APPLICABLE, f"node_type={node_type} has no applicable population"
    if result_count == 0:
        return (STATE_PRESENT_ZERO,
                "subject population present; zero overlaps cleared the threshold")
    return None, ""


def _supersede_answer_state(progress, cov, *, heat_present, result_count):
    """Supersede dispatcher; absent heat makes the answer partial, never a measured zero."""
    state = _partial_state(progress, cov, "" if heat_present else "heat source absent")
    if state[0] is not None:
        return state
    if result_count == 0:
        return (STATE_PRESENT_ZERO,
                "subject population present; zero heat-corroborated twins")
    return None, ""


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="comp-similar",
        description="BM25 SUMMARY similarity (what a resource DOES) + superseded-twin scan. "
                    "Advisory, read-only, hold-aware. NFRA_COMPSIMILAR PH2.",
        epilog="Engine: org/modules/graph/debtscan/comp_similar.py\n"
               "Rule T: --budget SECONDS > COMP_BUDGET_S > 90s default; 0 is unbounded. "
               "Corpus scans stop on deterministic ARN boundaries and emit --cursor.")
    ap.add_argument("query", nargs="*",
                    help="'<a> <b>' pairwise | '<a>' one-vs-corpus neighbors | "
                         "'supersede' | 'cluster'")
    ap.add_argument("--type", help="cluster: restrict to a node_type")
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--heat-json", metavar="FILE",
                    help="supersede: heat snapshot ({name:{data,invoke}} OR raw comp-debris/"
                         "comp-heat JSON). The fast, decoupled heat source (preferred).")
    ap.add_argument("--live-heat", action="store_true",
                    help="supersede: pull heat live via comp-debris+comp-heat (SLOW, minutes; "
                         "partial for S3 buckets -- see --heat-json).")
    ap.add_argument("--budget", metavar="SECONDS",
                    help="Rule T wall-clock budget (flag > COMP_BUDGET_S > 90s; 0=unbounded)")
    ap.add_argument("--cursor", metavar="LAST_ARN",
                    help="resume a bounded supersede/cluster scan strictly after this ARN")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="offline mutant gate (no graph/AWS)")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    mode = args.query[0] if args.query else None

    # supersede / cluster need the corpus + (supersede) live heat.
    if mode in ("supersede", "cluster"):
        try:
            budget_s, budget_source = _compbudget.resolve_budget(args.budget)
        except ValueError as exc:
            ap.error(str(exc))
        clock = _compbudget.Clock(budget_s)
        corpus = build_corpus()
        if not corpus:
            sys.stderr.write(_compbudget.disclosure_line(budget_s, budget_source) + "\n")
            sys.stderr.write("comp-similar: EMPTY corpus (broken retrieval, not an empty estate)\n")
            return 2
        cov = coverage(corpus)
        index = SimilarityIndex(corpus)
        progress = {}
        deferred = []
        if mode == "supersede":
            # Heat source: --heat-json snapshot (preferred/fast) | --live-heat (slow) | none.
            heat, heat_src = {}, "none"
            if args.heat_json:
                try:
                    heat = normalize_heat(json.loads(Path(args.heat_json).read_text()))
                    heat_src = f"snapshot:{args.heat_json}"
                except (OSError, ValueError) as e:
                    sys.stderr.write(f"comp-similar: --heat-json unreadable ({e})\n")
                    return 1
            elif args.live_heat:
                heat = load_heat_live(clock=clock, deferred=deferred)
                heat_src = "live (comp-debris+comp-heat)"
            # THE CONSUMPTION MEASUREMENT: len(heat) counts KEYS THE HEAT SOURCE OFFERED, which
            # is not the question -- the question is how many CORPUS resources the heat actually
            # reached with a usable band. An all-UNKNOWN heat map is a heat map in NAME ONLY, and
            # counting its keys reported a confident denominator for a blind result.
            heat_banded = sum(1 for d in corpus.values()
                              if any(b != "UNKNOWN" for b in (heat.get(d.name) or {}).values()))
            # One deterministic outer sweep produces both views. Their similarity thresholds and
            # neighbor widths remain the legacy 8 (supersede) / 6 (pool); only scheduling changed.
            pool = []
            cands = supersede_scan(corpus, index, heat, top=args.top, clock=clock,
                                   cursor=args.cursor, progress=progress, pool_out=pool)
            # The candidate POOL (summary-twin + unheld + not-designed-parallel) -- what WOULD be a
            # supersede candidate once heat diverges. Shown so a no-heat run is still useful + honest.
            budget_status = _budget_status(
                progress, budget_s, budget_source, clock, _resume_args(args, mode))
            resume_note = f"RESUMED AFTER: {args.cursor}" if args.cursor else None
            state, state_detail = _supersede_answer_state(
                progress, cov, heat_present=bool(heat_banded), result_count=len(cands))
            state_text = answer_state_line(state, state_detail) if state else None
            deferred_lines = _compbudget.deferred_bucket(
                len(deferred), 2 if args.live_heat else 0, "heat subprocess", deferred)
            if args.json:
                print(json.dumps({"budget_status": budget_status, "resume_basis": resume_note,
                                  "answer_state": state,
                                  "answer_state_detail": state_detail,
                                  "deferred": deferred_lines, "coverage": cov, "heat_source": heat_src,
                                  "heat_keys": len(heat), "heat_banded": heat_banded,
                                  "heat_corpus_denominator": len(corpus),
                                  "heat_resources": heat_banded, "candidates": cands,
                                  "summary_twin_pool": pool}, indent=2))
                return 0
            if resume_note:
                print(resume_note)
            print(budget_status)
            for line in deferred_lines:
                print(line)
            if state_text:
                print(state_text)
            print(cov["note"])
            print(f"heat: source={heat_src}, {heat_banded} of {len(corpus)} corpus "
                  f"resources banded from {len(heat)} heat key(s) "
                  f"(UNKNOWN heat -> never a candidate -- C3)")
            if not heat_banded:
                if not heat:
                    print("\nNO HEAT SOURCE -> 0 supersede verdicts (similarity alone "
                          "is never a verdict -- C1). Provide --heat-json <snapshot> or "
                          "--live-heat (slow).")
                else:
                    print(f"\nHEAT READ BUT 0 OF {len(corpus)} CORPUS RESOURCES BANDED "
                          f"(source={heat_src}, {len(heat)} key(s) offered) -> 0 supersede "
                          f"verdicts. The heat source did not JOIN this corpus by name: this "
                          f"is a BLIND result, not a measured zero -- C1/C3.")
                print(f"\n=== summary-twin POOL (supersede candidates PENDING heat corroboration) "
                      f"[{len(pool)}] ===")
                for c in pool:
                    print(f"  sim={c['summary_sim']:<5} {c['node_type']:<18} {c['a']}  ~  {c['b']}")
                return 0
            print(f"\n=== superseded-twin candidates (advisory; verify before reap) "
                  f"[{len(cands)}] ===")
            for c in cands:
                print(f"  [{c['confidence']:<6} sim={c['summary_sim']:<5}] "
                      f"{c['candidate']}  ->replaced by->  {c['replaced_by']}  cold{c['cold_axes']}")
            if not cands:
                print("  (none -- no summary-twin + heat-divergent + unheld pair in this heat set)")
            return 0
        # cluster
        clusters = cluster_scan(corpus, index, node_type=args.type, top=args.top,
                                clock=clock, cursor=args.cursor, progress=progress)
        budget_status = _budget_status(
            progress, budget_s, budget_source, clock, _resume_args(args, mode))
        resume_note = f"RESUMED AFTER: {args.cursor}" if args.cursor else None
        eligible = sum(1 for d in corpus.values() if not args.type or d.node_type == args.type)
        state, state_detail = _cluster_answer_state(
            progress, cov, eligible=eligible, result_count=len(clusters), node_type=args.type)
        state_text = answer_state_line(state, state_detail) if state else None
        deferred_lines = _compbudget.deferred_bucket(0, 0, "heat subprocess", [])
        if args.json:
            print(json.dumps({"budget_status": budget_status, "resume_basis": resume_note,
                              "answer_state": state,
                              "answer_state_detail": state_detail,
                              "deferred": deferred_lines, "coverage": cov,
                              "clusters": clusters}, indent=2))
        else:
            if resume_note:
                print(resume_note)
            print(budget_status)
            for line in deferred_lines:
                print(line)
            if state_text:
                print(state_text)
            print(cov["note"])
            print(f"\n=== functional-overlap clusters (same-JOB, advisory) [{len(clusters)}] ===")
            for c in clusters:
                print(f"  sim={c['summary_sim']:<5} {c['node_type']:<18} {c['a']}  ~  {c['b']}")
        return 0

    if mode and len(args.query) >= 1:
        if args.cursor is not None:
            ap.error("--cursor applies only to supersede/cluster corpus scans")
        corpus = build_corpus()
        if not corpus:
            sys.stderr.write("comp-similar: EMPTY corpus (broken retrieval, not an empty estate)\n")
            return 2
        # D2 (CVO finding 2026-09-02): the C3 control says the coverage denominator prints on
        # EVERY run. It printed on supersede/cluster only -- and the two query modes are the
        # ones a human reaches for FIRST, whose bare `sim=` / [THIN] / [HELD] output most looks
        # like a finished answer. The docstring was the thing that was wrong; the code is now
        # what it always claimed to be.
        cov = coverage(corpus)
        index = SimilarityIndex(corpus)
        a = _resolve(args.query[0], corpus)
        if a is None:
            state, detail = _query_answer_state(None, cov, subject=args.query[0])
            payload = {"answer_state": state, "answer_state_detail": detail}
            payload["coverage"] = cov
            if args.json:
                print(json.dumps(payload, indent=2))
            else:
                print(cov.get("note", ""))
                print(answer_state_line(state, detail))
            return 0
        if len(args.query) >= 2:                     # pairwise
            b = _resolve(args.query[1], corpus)
            if b is None:
                state, detail = _query_answer_state(None, cov, subject=args.query[1])
                payload = {"answer_state": state, "answer_state_detail": detail}
                payload["coverage"] = cov
                if args.json:
                    print(json.dumps(payload, indent=2))
                else:
                    print(cov.get("note", ""))
                    print(answer_state_line(state, detail))
                return 0
            res = pairwise(a, b, corpus, index)
            state, state_detail = _query_answer_state(
                a, cov, result_count=0 if res["summary_sim"] == 0 else 1,
                subject="both subjects")
            if args.json:
                print(json.dumps({"coverage": cov, "answer_state": state,
                                  "answer_state_detail": state_detail, **res}, indent=2))
            else:
                print(cov["note"])
                if state:
                    print(answer_state_line(state, state_detail))
                print(f"\nsummary_sim={res['summary_sim']}\n  {res['verdict']}\n"
                      f"  a: {res['a_summary']}\n  b: {res['b_summary']}")
            return 0
        # one-vs-corpus neighbors
        nbrs = index.neighbors(a, top=args.top)
        state, state_detail = _query_answer_state(
            a, cov, result_count=len(nbrs), subject=corpus[a].name)
        if args.json:
            print(json.dumps({"coverage": cov, "answer_state": state,
                              "answer_state_detail": state_detail,
                              "arn": a, "neighbors": nbrs}, indent=2))
        else:
            print(cov["note"])
            if state:
                print(answer_state_line(state, state_detail))
            print(f"\nsummary-similar peers of {corpus[a].name}:")
            for n in nbrs:
                flags = (" [THIN]" if n["thin"] else "") + (" [HELD]" if n["held"] else "")
                print(f"  sim={n['norm']:<6} {n['node_type']:<18} {n['name']}{flags}")
            if not nbrs:
                print("  (none above threshold)")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
