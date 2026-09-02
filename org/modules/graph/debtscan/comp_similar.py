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
                       ⛔ "on every run" was FALSE from 2026-07-19 to 2026-09-02: it printed on
                       supersede/cluster only, while this line asserted otherwise and the
                       self-test scored C3 PASS on the half that worked. An untrue control
                       statement is worse than an absent one -- it teaches the reader to stop
                       looking. All three halves are now legs of the harness so the tool can
                       FAIL on this -- C3a blind-row, C3b disclosure (UNKNOWN path + every
                       mode emits), C3c capture (a real comp-kuzu header parses to MEASURED,
                       a headerless one to ABSENT). An unknown vintage renders UNKNOWN with an
                       explicit do-not-trust clause: never omitted, never defaulted to fresh.
                       ⛔ C3c exists because C3b alone passed IDENTICALLY while the live corpus
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
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
_DEBTSCAN = _HERE.parent                 # .../org/modules/graph/debtscan
_GRAPH = _HERE.parents[1]                # .../org/modules/graph
REPO = _HERE.parents[4]                  # .../ajb_workspace
if str(_DEBTSCAN) not in sys.path:
    sys.path.insert(0, str(_DEBTSCAN))

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

# --- thresholds (conservative v1; CTO may retune at the gate) -------------------------------
SIM_TWIN = 0.60          # summary-sim at/above this = a functional-twin candidate (mirror M2)
SIM_FLOOR = 0.15         # below this = not related (mirror SimilarityIndex.neighbors floor)
_COLD_BANDS = {"COLD", "COLD-DORMANT"}
_HOT_BANDS = {"HOT"}


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
def supersede_scan(corpus, index, heat, *, sim_twin=SIM_TWIN, top=40):
    """Ranked superseded-twin candidates. A candidate = a pair that is (i) SUMMARY-similar
    (functional twin, >= sim_twin), (ii) NOT a designed parallel, (iii) heat-DIVERGENT (one
    COLD, one HOT), (iv) neither held. Emits the COLD member as the decommission candidate +
    the HOT member as its live replacement. Rank = summary_sim * (HIGH=1.0 / MEDIUM=0.6).
    PURE: heat = {name -> {data,invoke}} (UNKNOWN for anything unread -- C3)."""
    seen: set[tuple] = set()
    out: list[dict] = []
    for arn, doc in corpus.items():
        if doc.thin:
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
    out.sort(key=lambda c: -c["rank_score"])
    return out[:top]


def cluster_scan(corpus, index, *, node_type=None, min_norm=SIM_TWIN, top=60):
    """Functional-overlap census: every resource with a summary-similar peer (a same-JOB
    cluster), suppressors applied. Advisory overlap map, NOT a supersession verdict (no heat)."""
    seen: set[tuple] = set()
    out: list[dict] = []
    for arn, doc in corpus.items():
        if doc.thin or (node_type and doc.node_type != node_type):
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
    {name, band}) and comp-heat freshness ({paths: [{path, class}]}), and fold both into the
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
    # (c) raw comp-heat freshness: path-keyed data bands (map basename -> resource name)
    for row in (raw.get("paths") or []):
        if isinstance(row, dict) and row.get("path"):
            base = os.path.basename(str(row["path"]).rstrip("/"))
            heat.setdefault(base, {}).setdefault("data", _norm_band(row.get("class", "")))
    return heat


def load_heat_live(timeout=280) -> dict:
    """SLOW opt-in (--live-heat): pull comp-debris (invoke, live AWS -- minutes) + comp-heat
    (data). Best-effort; a tool that times out leaves its axis UNKNOWN (never assume cold -- C3).
    NOTE (open plumbing, flagged to CTO): comp-debris default = lambda only (S3/DDB need --types,
    slower); comp-heat freshness is REPO-path-scoped, not per-S3-bucket data-heat -- so live heat
    is partial for the S3-bucket consolidation surface. The clean path is a heat SNAPSHOT via
    --heat-json (cadence/source is the §6-decision-5 open item)."""
    heat: dict[str, dict] = {}
    dbg = _run_json([str(REPO / ".tools" / "comp-debris"), "--json"], timeout=timeout)
    if dbg:
        heat.update(normalize_heat(dbg))
    out_json = _GRAPH / "debtscan" / ".comp_similar_heat.json"
    _run_json([str(REPO / ".tools" / "comp-heat"), "freshness", "--json", str(out_json)],
              timeout=timeout)
    try:
        if out_json.exists():
            for name, v in normalize_heat(json.loads(out_json.read_text())).items():
                heat.setdefault(name, {}).update(v)
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

    # C3c CAPTURE (added 2026-09-02, same session, after C3b was caught committing C3's own
    # defect). ⛔ C3b tests ONLY the UNKNOWN path -- it passed IDENTICALLY before and after the
    # stderr fix, while the live corpus still rendered UNKNOWN. A control that green-lights the
    # broken state is the D3 shape one domain over, so the MEASURED path needs its own leg.
    # The header below is a VERBATIM excerpt of real comp-kuzu output (streams separated,
    # 2026-09-02), so this tests the shape the parser actually meets -- not one written to fit
    # the parser. Runs offline: no graph, no AWS.
    import summary_corpus as _sc
    _saved = dict(_sc._CORPUS_VINTAGE)
    try:
        _sc._CORPUS_VINTAGE.clear()
        _sc._capture_kuzu_vintage(
            "=== comp-kuzu provenance ===\n"
            "  DB: kuzu_nessie_db  (27122 nodes / 60670 edges)\n"
            "  source: nessie\n"
            "  built: 2026-09-02T14:20:11.113748+00:00 (age: 0.2h)\n"
            "============================\n")
        cap = coverage(corpus)
        c3c = (cap.get("corpus_vintage_claim") == "measured"
               and cap.get("corpus_built") == "2026-09-02T14:20:11.113748+00:00"
               and cap.get("corpus_age") == "0.2h"
               and cap.get("corpus_db") == "kuzu_nessie_db"
               and "UNKNOWN" not in cap.get("vintage_note", ""))
        # negative control: a header with NO built: line must NOT yield a measured claim.
        _sc._CORPUS_VINTAGE.clear()
        _sc._capture_kuzu_vintage("=== comp-kuzu provenance ===\n  DB: kuzu_nessie_db\n")
        c3c_neg = coverage(corpus).get("corpus_vintage_claim") == "absent"
    finally:
        _sc._CORPUS_VINTAGE.clear()
        _sc._CORPUS_VINTAGE.update(_saved)
    c3c_ok = c3c and c3c_neg
    ok &= c3c_ok
    print(f"  C3c vintage-CAPTURE (real header parsed -> measured; headerless -> absent): "
          f"parse={'ok' if c3c else 'BROKEN'} neg-control={'ok' if c3c_neg else 'BROKEN'} "
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

    print(f"=== comp_similar self-test: {'PASS' if ok else 'FAIL'} (9/9) ===" if ok
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


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="comp-similar",
        description="BM25 SUMMARY similarity (what a resource DOES) + superseded-twin scan. "
                    "Advisory, read-only, hold-aware. NFRA_COMPSIMILAR PH2.")
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
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="offline mutant gate (no graph/AWS)")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    mode = args.query[0] if args.query else None

    # supersede / cluster need the corpus + (supersede) live heat.
    if mode in ("supersede", "cluster"):
        corpus = build_corpus()
        if not corpus:
            sys.stderr.write("comp-similar: EMPTY corpus (broken retrieval, not an empty estate)\n")
            return 2
        cov = coverage(corpus)
        index = SimilarityIndex(corpus)
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
                heat = load_heat_live()
                heat_src = "live (comp-debris+comp-heat)"
            cands = supersede_scan(corpus, index, heat, top=args.top)
            # The candidate POOL (summary-twin + unheld + not-designed-parallel) -- what WOULD be a
            # supersede candidate once heat diverges. Shown so a no-heat run is still useful + honest.
            pool = cluster_scan(corpus, index, top=args.top)
            if args.json:
                print(json.dumps({"coverage": cov, "heat_source": heat_src,
                                  "heat_resources": len(heat), "candidates": cands,
                                  "summary_twin_pool": pool}, indent=2))
                return 0
            print(cov["note"])
            print(f"heat: source={heat_src}, {len(heat)} resources banded "
                  f"(UNKNOWN heat -> never a candidate -- C3)")
            if not heat:
                print("\nNO HEAT SOURCE -> 0 supersede verdicts (similarity alone is never a "
                      "verdict -- C1). Provide --heat-json <snapshot> or --live-heat (slow).")
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
        clusters = cluster_scan(corpus, index, node_type=args.type, top=args.top)
        if args.json:
            print(json.dumps({"coverage": cov, "clusters": clusters}, indent=2))
        else:
            print(cov["note"])
            print(f"\n=== functional-overlap clusters (same-JOB, advisory) [{len(clusters)}] ===")
            for c in clusters:
                print(f"  sim={c['summary_sim']:<5} {c['node_type']:<18} {c['a']}  ~  {c['b']}")
        return 0

    if mode and len(args.query) >= 1:
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
            sys.stderr.write(f"comp-similar: '{args.query[0]}' did not resolve to a corpus resource\n")
            return 1
        if len(args.query) >= 2:                     # pairwise
            b = _resolve(args.query[1], corpus)
            if b is None:
                sys.stderr.write(f"comp-similar: '{args.query[1]}' did not resolve\n")
                return 1
            res = pairwise(a, b, corpus, index)
            if args.json:
                print(json.dumps({"coverage": cov, **res}, indent=2))
            else:
                print(cov["note"])
                print(f"\nsummary_sim={res['summary_sim']}\n  {res['verdict']}\n"
                      f"  a: {res['a_summary']}\n  b: {res['b_summary']}")
            return 0
        # one-vs-corpus neighbors
        nbrs = index.neighbors(a, top=args.top)
        if args.json:
            print(json.dumps({"coverage": cov, "arn": a, "neighbors": nbrs}, indent=2))
        else:
            print(cov["note"])
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
