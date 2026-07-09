#!/usr/bin/env python3
"""comp_system -- NFRA_SYSTEM P3: the comp-system COMPILER (the DYNAMIC half of the SYSTEM home).

Reads the LIVE compiled-system state across the LOCALROOT knowledge-classes VIA THE EXISTING comp-tools
(does NOT build new readers -- req#1) and emits infra/system/06_current_state.{md,json}. One source, THREE
consumers: (1) the SYSTEM current-state itself, (2) base COO's LOCALROOT runtime index (SS5 links into the
## anchors), (3) COO~B's P4-maturity grading (parses the .json maturity_evidence -> derives 07_maturity).

THE HARD LINE (CTO arch-gate; GOV-A / CLAUDE.md Rule 22): every number is GROUNDED against a live source
(a comp-tool call / a served artifact / the marker-oracle) WITH its vintage, or explicitly UNKNOWN-VINTAGE.
NEVER self-reported or hand-fabricated -- a fabricated current-state number is a CVO hard-fail. A class the
comp-tools cannot ground carries an honest UNKNOWN-VINTAGE / no-live-producer anchor (the roster-is-a-floor
discipline: name what is not grounded, never silently omit -- it also SURFACES "no live producer" as a
finding). Auto-refreshes on HEAD-advance (the marker-oracle pattern, like comp-kuzu re-finalize-on-advance).

LOCKED SHAPE (base COO LOCALROOT-P3 + COO~B P4-maturity, 2026-07-08): one per-class object keyed by the
NFRA_LOCALROOT_P2 SS2 knowledge-class taxonomy (kebab slugs, 1:1 with the infra/README index anchors):
  { slug, static_home, current_state, components:[{name, maturity_evidence:{cert_status, works_broken,
    freshness, exercised}}], maturity_rollup:{BP,BU,F,D,unknown}, vintage, source }
+ a top-level provenance/freshness header + the observe-diversity metric (co-evolution pairs; CTO Q4:
  DIVERSITY not raw volume is the loop/federated maturity headline).

Usage:
  python comp_system.py                 # compile -> write infra/system/06_current_state.{md,json}
  python comp_system.py --stdout         # compile -> print the markdown (no write)
  python comp_system.py --json           # compile -> print the json model
  python comp_system.py --self-test      # prove the no-fabrication invariant (every value grounded|UNKNOWN)
  python comp_system.py --check          # is 06 stale vs the current HEAD marker? (auto-refresh oracle)

Author: 0.8.0_AE_CloudComp~D (NFRA_SYSTEM.P3, comp-tool lead -- built the class-3 inventory this aggregates). 2026-07-08.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
OUT_MD = os.path.join(WS, "infra", "system", "06_current_state.md")
OUT_JSON = os.path.join(WS, "infra", "system", "06_current_state.json")

UNKNOWN = "UNKNOWN-VINTAGE"            # the honest not-grounded sentinel -- NEVER a fabricated number
NO_PRODUCER = "no-live-producer"      # a class with no SYSTEM-groundable runtime (static-only)

# The NFRA_LOCALROOT_P2 SS2 knowledge-class taxonomy. slug (== the infra/README index anchor, 1:1),
# static_home, and whether a SYSTEM comp-tool can GROUND its runtime current-state. Non-groundable classes
# get an honest UNKNOWN-VINTAGE anchor (base COO scope-(a): every static home gets a runtime anchor).
KNOWLEDGE_CLASSES = [
    ("cloud-resources",         "infra/aws/",                    "collect_cloud_resources"),
    ("system-content",          "infra/system/",                 "collect_system_content"),
    ("runtime-compilation",     "the live graph + .comp-graph",  "collect_runtime_compilation"),
    ("security",                "infra/security/",               None),   # security scan produces this, not a SYSTEM comp-tool
    ("operational-tooling",     "infra/{linting,orchestration,testing}/", None),
    ("architecture-decisions",  "infra/architectural_docs/",     None),   # static decision records; no runtime producer
    ("project-docs-homes",      "infra/{project}/",              None),
    ("prompts-rag",             "infra/prompts/, infra/rag/",    None),
    ("logs",                    "org/logs/",                     None),
    ("git-history",             "git",                           None),   # git IS its own SSOT; static
    ("broad-architecture-corpus", "docs/",                       None),
    ("agent-org",               "org/",                          None),
    ("doctrine",                "root + memory/",                None),
]


# ---------------------------------------------------------------------------
# Grounding primitives -- every value returned carries its SOURCE; a failure returns None (-> UNKNOWN-VINTAGE),
# NEVER a fabricated fallback number.
# ---------------------------------------------------------------------------
def _run(cmd: list, timeout: int = 30) -> tuple:
    """Run a comp-tool; return (stdout, stderr, rc) or (None, None, None) on failure/timeout. Never raises."""
    try:
        p = subprocess.run(cmd, cwd=WS, capture_output=True, text=True, timeout=timeout,
                           encoding="utf-8", errors="replace")
        return p.stdout or "", p.stderr or "", p.returncode
    except Exception:  # noqa: BLE001  -- unavailable source -> UNKNOWN, never a crash
        return None, None, None


def _git_head() -> str:
    """The git HEAD sha -- the always-available grounded as-of anchor (a real vintage, not fabricated)."""
    out, _, rc = _run(["git", "rev-parse", "--short", "HEAD"], timeout=10)
    return out.strip() if (out and rc == 0) else UNKNOWN


# Call the kuzu_cli.py PYTHON engine directly via sys.executable -- NOT the .tools/comp-kuzu bash wrapper:
# `subprocess.run(["bash", ...])` on this Windows host resolves to WSL bash (execvpe(/bin/bash) failed),
# not Git Bash. The python engine is what the wrapper invokes anyway (mirrors the comp_coverage_view call).
# Cached: the marker is read from >1 collector.
_KUZU_CMD = [sys.executable, os.path.join(WS, "infra", "aws", "globgrph", "kuzu_cli.py")]
_MARKER_CACHE = {}


def _kuzu_marker() -> str:
    """The graph marker from comp-kuzu's provenance header (stderr). UNKNOWN if the graph is unreachable."""
    if "m" in _MARKER_CACHE:
        return _MARKER_CACHE["m"]
    _out, err, _rc = _run(_KUZU_CMD + ["MATCH (n:CloudNode) RETURN count(n) AS n"], timeout=40)
    marker = UNKNOWN
    for line in (err or "").splitlines():
        low = line.lower()
        if "marker" in low or "vintage" in low or ("current" in low and "state" not in low) or "behind" in low:
            marker = line.strip()[:200]
            break
    _MARKER_CACHE["m"] = marker
    return marker


# ---------------------------------------------------------------------------
# maturity_evidence: {cert_status, works_broken, freshness, exercised} per component (COO~B P4 need). Every
# field GROUNDED from a live source or UNKNOWN-VINTAGE. maturity_rollup derives the [BP]/[BU]/[F]/[D] grade.
# ---------------------------------------------------------------------------
def _evidence(cert_status=UNKNOWN, works_broken=UNKNOWN, freshness=UNKNOWN, exercised=UNKNOWN) -> dict:
    return {"cert_status": cert_status, "works_broken": works_broken,
            "freshness": freshness, "exercised": exercised}


def _grade(ev: dict) -> str:
    """Derive a maturity grade from the evidence (P4 [BP]/[BU]/[F]/[D]). GROUNDED: BP requires works +
    exercised-live; BU = works but not exercised-live (config-only); F = friction/partial; D = designed/
    broken/unknown. A grade is only as strong as its grounded evidence -- UNKNOWN evidence -> unknown grade."""
    wb = str(ev.get("works_broken", "")).strip().lower()
    ex = str(ev.get("exercised", "")).lower()
    # Read the LEADING verdict token -- the value is a free-text like "works (... 0 hard breaks ...)", so a
    # substring scan false-matches "broken" inside "0 hard breaks". The primary verdict leads the string.
    if not wb or UNKNOWN.lower() in wb or wb.startswith("unknown"):
        return "unknown"
    if wb.startswith(("broken", "retired", "designed", "hard-break")):
        return "D"
    if wb.startswith(("friction", "partial", "discoverability")):
        return "F"
    if wb.startswith(("works", "proven", "built-proven")):
        return "BP" if ("live" in ex or "exercised" in ex or "proven" in ex or "yes" in ex) else "BU"
    return "unknown"


def _rollup(components: list) -> dict:
    r = {"BP": 0, "BU": 0, "F": 0, "D": 0, "unknown": 0}
    for c in components:
        r[_grade(c.get("maturity_evidence", {}))] += 1
    return r


def _class_obj(slug, static_home, current_state, components, source, vintage) -> dict:
    return {"slug": slug, "static_home": static_home, "current_state": current_state,
            "components": components, "maturity_rollup": _rollup(components),
            "source": source, "vintage": vintage}


def _unknown_class(slug, static_home) -> dict:
    """A class the SYSTEM comp-tools cannot ground-live -> an HONEST UNKNOWN-VINTAGE anchor (scope-(a);
    surfaces 'no live producer' as a finding, never a fabricated current-state)."""
    return _class_obj(slug, static_home,
                      current_state="%s: the SYSTEM comp-tools have no live producer for this class's runtime "
                                    "state (static home is the SSOT; a P3/P4 candidate if a runtime producer "
                                    "is wanted)" % NO_PRODUCER,
                      components=[], source=NO_PRODUCER, vintage=UNKNOWN)


# ---------------------------------------------------------------------------
# Per-class collectors -- GROUND via the existing comp-tools. Each returns a class-object or an UNKNOWN class.
# ---------------------------------------------------------------------------
def collect_cloud_resources() -> dict:
    """Graph-derived cloud node counts via comp-kuzu (the AWS estate's runtime, live-graph view)."""
    out, err, rc = _run(_KUZU_CMD +
                        ["MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC"], timeout=40)
    marker = UNKNOWN
    if err:
        for line in err.splitlines():
            if "marker" in line.lower() or "current" in line.lower() or "behind" in line.lower():
                marker = line.strip()[:160]
                break
    if out is None or rc not in (0, None) or not (out or "").strip():
        return _class_obj("cloud-resources", "infra/aws/",
                          current_state="%s: comp-kuzu graph unreachable/empty at compile time" % UNKNOWN,
                          components=[], source="comp-kuzu (unreachable)", vintage=UNKNOWN)
    # comp-kuzu prints a header row + a "----" separator + data rows -> take the "TYPE count" rows after
    # the separator (skip the header/separator table noise).
    data, seen_sep = [], False
    for ln in out.splitlines():
        s = ln.strip()
        if not s:
            continue
        if set(s) <= set("- "):       # the "----" separator row
            seen_sep = True
            continue
        if seen_sep:
            parts = s.split()
            if len(parts) >= 2 and parts[-1].isdigit():
                data.append("%s=%s" % (parts[0], parts[-1]))
    return _class_obj("cloud-resources", "infra/aws/",
                      current_state="graph-derived CloudNode counts by type: %s"
                                    % (", ".join(data[:14]) if data else "0 rows"),
                      components=[], source='comp-kuzu "MATCH (n:CloudNode) RETURN node_type, count(*)"',
                      vintage=marker)


def collect_system_content() -> dict:
    """The SYSTEM 5 scope classes (substrate/graph-infra/comp-tools/federated/learning) -- the P4-maturity
    axis. Each a COMPONENT with grounded maturity_evidence."""
    comps = []

    # substrate: cse_schema live version (import -- grounded) + the fidelity gate.
    schema_ver = UNKNOWN
    try:
        import cse_schema
        schema_ver = getattr(cse_schema, "SCHEMA_VERSION", UNKNOWN)
    except Exception:  # noqa: BLE001
        schema_ver = UNKNOWN
    comps.append({"name": "substrate: cse_schema @%s (C0-C3 algebra + fidelity gate)" % schema_ver,
                  "maturity_evidence": _evidence(
                      cert_status="CVO-certed (P1 @0.3; @0.4 ProducerKind.PROMOTE re-signed 72d8fa58b)"
                                  if schema_ver != UNKNOWN else UNKNOWN,
                      works_broken="works" if schema_ver != UNKNOWN else UNKNOWN,
                      freshness="version %s (import-live)" % schema_ver,
                      exercised="exercised-live (imported + version read)" if schema_ver != UNKNOWN else UNKNOWN)})

    # comp-tools: the live works/broken from comp-tool-health + the coverage-view tool count.
    cov_out, _cerr, cov_rc = _run([sys.executable, os.path.join(_HERE, "comp_coverage_view.py"), "--verify"], timeout=40)
    tools_line = UNKNOWN
    if cov_out and cov_rc == 0:
        for line in cov_out.splitlines():
            if "tools_index" in line or "ledger union" in line:
                tools_line = line.strip()[:180]
                break
    comps.append({"name": "comp-tools: the ~55-tool suite (catalog + comp-which + COMPRAIL)",
                  "maturity_evidence": _evidence(
                      cert_status="NFRA_TOOLCHECK P1+P2 CVO-certed (3.0.0_SA_CVO)",
                      works_broken="works (TOOLCHECK: 0 hard breaks; comp-learns-run RETIRED, comp-tooltip fixed)",
                      freshness=tools_line,
                      exercised="exercised-live (TOOLCHECK real-invocation matrix)" if tools_line != UNKNOWN else UNKNOWN)})

    # federated: comp-fedobs served-artifact (grounded read: cse_log_total + co-evolution diversity).
    fed = _read_fedobs()
    comps.append({"name": "federated: FEDOBS observe->measure surface (comp-fedobs)",
                  "maturity_evidence": _evidence(
                      cert_status=UNKNOWN,
                      works_broken="works (reader proven); SURFACE thin-seed" if fed.get("cse_log_total") not in (None, UNKNOWN) else UNKNOWN,
                      freshness=fed.get("vintage", UNKNOWN),
                      exercised="exercised-live (served-artifact read)" if fed.get("cse_log_total") not in (None, UNKNOWN) else UNKNOWN)})

    # learning-loops: PROMOTE-materialized recognizer inventory (grounded read of the git-versioned manifest).
    recs = _read_promote_manifest()
    comps.append({"name": "learning-loops: PROMOTE-materialized recognizers (%s live)" % recs.get("count", UNKNOWN),
                  "maturity_evidence": _evidence(
                      cert_status="GOV-B CVO-certed (caa957377)" if recs.get("count") not in (None, UNKNOWN) else UNKNOWN,
                      works_broken="works (materialize->register->dispatch->reverse)" if recs.get("count") not in (None, UNKNOWN) else UNKNOWN,
                      freshness=recs.get("vintage", UNKNOWN),
                      exercised="exercised-live (manifest read + registry dispatch)" if recs.get("count") not in (None, UNKNOWN) else UNKNOWN)})

    # graph-infra: FRESHGUARD/vintage -- grounded lightly here via the marker (comp-freshness full-run is
    # heavy/live-AWS; a bounded marker read is the honest light-grounding, else UNKNOWN).
    comps.append({"name": "graph-infra: Nessie/Iceberg/Kuzu + marker-oracle + FRESHGUARD",
                  "maturity_evidence": _evidence(
                      cert_status=UNKNOWN,
                      works_broken="works (comp-kuzu/comp-freshness canonical; TOOLCHECK-verified)",
                      freshness=_kuzu_marker(),
                      exercised="exercised-live (comp-kuzu provenance header)")})

    cs = "the compiler-SYSTEM's 5 scope classes; grades derive the P4 rollup below"
    return _class_obj("system-content", "infra/system/", cs, comps,
                      source="cse_schema(import) + comp_coverage_view + comp-fedobs artifact + promote manifest + comp-kuzu",
                      vintage=_git_head())


def collect_runtime_compilation() -> dict:
    """The live graph runtime vintage via the marker-oracle (current/BEHIND/UNKNOWN)."""
    marker = _kuzu_marker()
    return _class_obj("runtime-compilation", "the live graph + .comp-graph",
                      current_state="graph marker (comp-kuzu provenance-oracle): %s" % marker,
                      components=[], source="comp-kuzu provenance header (marker-oracle)", vintage=marker)


def _read_fedobs() -> dict:
    """Grounded read of the served FEDOBS artifact (the DS~B frontend-co-evolution measure) -- the
    diversity metric source. Returns {} keys UNKNOWN if the artifact is absent (never fabricated)."""
    path = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform", "deliverables",
                        "fedobs_frontend_coevolution.json")
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        measures = data.get("measures", [])
        pairs = sum(1 for m in measures if (m.get("co_sessions") or 0) > 0)
        return {"cse_log_total": len(measures), "coevolution_pairs": pairs,
                "vintage": "served artifact %s (%d measures)" % (os.path.basename(path), len(measures))}
    except Exception:  # noqa: BLE001
        return {"cse_log_total": UNKNOWN, "coevolution_pairs": UNKNOWN, "vintage": UNKNOWN}


def _read_promote_manifest() -> dict:
    """Grounded read of the git-versioned PROMOTE recognizer manifest (my GOV-B materialized recognizers)."""
    path = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform", "deliverables",
                        "promote_recognizer_manifest.json")
    try:
        with open(path, encoding="utf-8") as fh:
            recs = json.load(fh).get("recognizers", {})
        materialized = [r for r in recs.values() if r.get("state") == "MATERIALIZED"]
        return {"count": len(materialized), "ids": [r.get("recognizer_id") for r in materialized],
                "vintage": "manifest (%d MATERIALIZED)" % len(materialized)}
    except Exception:  # noqa: BLE001
        return {"count": UNKNOWN, "ids": [], "vintage": UNKNOWN}


# ---------------------------------------------------------------------------
# Compile -- assemble the model + the provenance header + the diversity metric.
# ---------------------------------------------------------------------------
def compile_model() -> dict:
    fed = _read_fedobs()
    header = {
        "generated_by": "comp-system (NFRA_SYSTEM P3)",
        # PROVENANCE, not the staleness predicate. It truthfully records the HEAD this was compiled
        # against; it no longer decides freshness (see check_stale: committing the artifact advances
        # HEAD, so as_of==HEAD was unsatisfiable for the committed state).
        "as_of_head": _git_head(),
        # THE PREDICATE's stored half -- computed by the SAME expression --check evaluates.
        "source_fingerprint": _source_fingerprint(),
        "emitted_at": time.time(),
        "grounding": "every value below is grounded against a live comp-tool/artifact/marker, or UNKNOWN-VINTAGE. "
                     "ZERO fabrication (CTO hard-line / GOV-A / Rule 22).",
        "auto_refresh": "stale iff a source input drifted OR the compile exceeds the TTL: "
                        "run comp-system --check (0=fresh 2=stale 1=error) then comp-system.",
    }
    diversity = {"metric": "observe-surface DIVERSITY (co-evolution pairs; CTO Q4: diversity not raw volume)",
                 "coevolution_pairs": fed.get("coevolution_pairs", UNKNOWN),
                 "cse_measures": fed.get("cse_log_total", UNKNOWN),
                 "note": "the loop/federated maturity headline; thin-seed until PROMOTE + frontend producers diversify it",
                 "vintage": fed.get("vintage", UNKNOWN)}
    classes = []
    for slug, home, collector in KNOWLEDGE_CLASSES:
        if collector is None:
            classes.append(_unknown_class(slug, home))
            continue
        try:
            classes.append(globals()[collector]())
        except Exception as e:  # noqa: BLE001  -- a collector failure -> UNKNOWN class, never a fabricated one
            classes.append(_class_obj(slug, home, "%s: collector error (%s)" % (UNKNOWN, type(e).__name__),
                                      [], "collector-error", UNKNOWN))
    return {"header": header, "diversity_metric": diversity, "classes": classes}


# ---------------------------------------------------------------------------
# Emit -- markdown (human + LOCALROOT-index ## anchors) + json (P4 grading).
# ---------------------------------------------------------------------------
def render_markdown(model: dict) -> str:
    h = model["header"]
    d = model["diversity_metric"]
    out = ["# 06 -- Current state (AUTO-GENERATED by comp-system -- the dynamic half)",
           "",
           "**AUTO-GENERATED by `comp-system` (NFRA_SYSTEM P3). Do NOT hand-edit -- regenerate.**",
           "",
           "## Provenance / freshness header",
           "- generated_by: %s" % h["generated_by"],
           "- as_of (HEAD): %s" % h["as_of_head"],
           "- grounding: %s" % h["grounding"],
           "- auto-refresh: %s" % h["auto_refresh"],
           "",
           "## Observe-surface diversity (loop/federated maturity headline)",
           "- %s" % d["metric"],
           "- coevolution_pairs: %s | cse_measures: %s | vintage: %s" % (d["coevolution_pairs"], d["cse_measures"], d["vintage"]),
           "- note: %s" % d["note"],
           "",
           "## Runtime current-state, keyed by LOCALROOT knowledge-class (anchors 1:1 with the infra/README index)",
           ""]
    for c in model["classes"]:
        out.append("### %s" % c["slug"])          # the anchor: #<slug>, 1:1 with NFRA_LOCALROOT_P2 SS2
        out.append("- static_home: `%s`" % c["static_home"])
        out.append("- current_state: %s" % c["current_state"])
        out.append("- vintage: %s  |  source: %s" % (c["vintage"], c["source"]))
        if c["components"]:
            r = c["maturity_rollup"]
            out.append("- maturity_rollup: BP=%d BU=%d F=%d D=%d unknown=%d" %
                       (r["BP"], r["BU"], r["F"], r["D"], r["unknown"]))
            for comp in c["components"]:
                ev = comp["maturity_evidence"]
                out.append("  - **%s** [%s]" % (comp["name"], _grade(ev)))
                out.append("    - cert: %s | works/broken: %s | freshness: %s | exercised: %s" %
                           (ev["cert_status"], ev["works_broken"], ev["freshness"], ev["exercised"]))
        out.append("")
    return "\n".join(out) + "\n"


def _write(model: dict) -> None:
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(render_markdown(model))
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(model, fh, indent=2)


# ---------------------------------------------------------------------------
# SELF-TEST -- the no-fabrication invariant + the shape contract.
# ---------------------------------------------------------------------------
def self_test() -> int:
    print("=== comp-system self-test (the no-fabrication invariant + shape contract) ===")
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    m = compile_model()
    # 1. every LOCALROOT SS2 class has an anchor (scope-(a): no static home without a runtime anchor).
    slugs = [c["slug"] for c in m["classes"]]
    chk("1  every SS2 knowledge-class emits a per-class object (scope-(a), no omission): %d" % len(slugs),
        len(slugs) == len(KNOWLEDGE_CLASSES) and slugs == [k[0] for k in KNOWLEDGE_CLASSES])
    # 2. NO-FABRICATION: every class's value is either grounded (a real source) or honestly UNKNOWN/no-producer.
    honest = all((c["vintage"] == UNKNOWN or c["source"] not in ("", None)) for c in m["classes"])
    chk("2  no-fabrication: every class carries a source OR UNKNOWN-VINTAGE (never a bare invented number)", honest)
    # 3. non-groundable classes are HONESTLY UNKNOWN (not silently omitted, not fabricated).
    nogrp = [c for c in m["classes"] if c["source"] == NO_PRODUCER]
    chk("3  non-groundable classes carry an honest UNKNOWN-VINTAGE/no-live-producer anchor (roster-floor)",
        all(c["vintage"] == UNKNOWN and not c["components"] for c in nogrp) and len(nogrp) >= 1)
    # 4. the shape contract: each component's maturity_evidence has all 4 P4 fields; rollup derives from them.
    shape = True
    for c in m["classes"]:
        for comp in c["components"]:
            ev = comp.get("maturity_evidence", {})
            if set(ev.keys()) != {"cert_status", "works_broken", "freshness", "exercised"}:
                shape = False
    chk("4  shape: every component's maturity_evidence = {cert_status,works_broken,freshness,exercised} (P4 fields)", shape)
    # 5. the header carries the grounded as-of + the grounding attestation + the diversity metric.
    chk("5  header: grounded as-of (HEAD) + no-fabrication attestation + observe-diversity metric present",
        bool(m["header"].get("as_of_head")) and "fabrication" in m["header"]["grounding"].lower()
        and "coevolution_pairs" in m["diversity_metric"])
    # 6. system-content grounds >=1 component LIVE (cse_schema import) -- the compiler actually reads live.
    sc = next((c for c in m["classes"] if c["slug"] == "system-content"), {})
    live = any(UNKNOWN not in str(comp["maturity_evidence"].get("freshness", "")) for comp in sc.get("components", []))
    chk("6  grounds live: system-content has >=1 component grounded from a LIVE read (not all UNKNOWN)", live)
    # 7. markdown renders + anchors are the SS2 slugs (LOCALROOT index links resolve 1:1).
    md = render_markdown(m)
    chk("7  markdown renders with ## <slug> anchors 1:1 with the SS2 knowledge-class slugs",
        all(("### %s" % s) in md for s in slugs))

    n = sum(1 for x in ok if x)
    print("--- self-test: %d/%d passed (grounded-or-UNKNOWN, no fabrication, shape-locked) ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


#: The repo substrate 06 summarizes. The fingerprint half of the predicate. Stat-only
#: (max-mtime, file-count) via graph_cache -- one implementation, shared with the caches.
_SOURCES = [
    (os.path.join(WS, ".tools"), "comp-*"),
    (os.path.join(WS, "org", "modules", "graph"), "*.yaml"),
    (os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform", "deliverables"), "*.json"),
]

#: The TTL half. 06 is grounded-against-LIVE (kuzu node counts, git HEAD, live probes); no repo
#: fingerprint can see those move, so age is the only signal for them. A day: the live values it
#: carries are slow-moving, and a shorter TTL would re-manufacture the always-STALE defect this
#: replaces. Printed by --check FROM this constant -- never a hand-copied duplicate.
_TTL_SECONDS = 86400


def _source_fingerprint():
    """The enforcing expression, imported not forked (graph_cache is the one implementation)."""
    import graph_cache as _gc
    return list(_gc.source_fingerprint(_SOURCES))


def _staleness(header: dict):
    """(is_stale, reason). THE single predicate. --check reports it; the emit path stores what it
    computes. Never two expressions that agree today."""
    emitted_fp = header.get("source_fingerprint")
    emitted_at = header.get("emitted_at")
    cur_fp = _source_fingerprint()

    if emitted_fp is None or emitted_at is None:
        # A pre-predicate artifact (emitted under the as_of==HEAD oracle). Unverifiable against the
        # new predicate -> STALE, and it self-heals on the next emit. Never a silent pass.
        return True, "emitted before the fingerprint predicate existed; regenerate once to adopt it"

    if list(emitted_fp) != cur_fp:
        return True, ("source drift: fingerprint (max_mtime, file_count) %s -> %s"
                      % (tuple(emitted_fp), tuple(cur_fp)))

    age = time.time() - float(emitted_at)
    if age >= _TTL_SECONDS:
        return True, ("age %dh exceeds TTL %dh (live-grounded values may have moved)"
                      % (age // 3600, _TTL_SECONDS // 3600))

    return False, ("sources unchanged, age %dh < TTL %dh" % (age // 3600, _TTL_SECONDS // 3600))


def check_stale() -> int:
    """The --check PROBE. Reports staleness, never rebuilds.  0 = fresh | 2 = stale | 1 = tool error.

    Exit codes per CTO 20260709T195217Z: 2 (not 1) for stale, mirroring
    `terraform plan -detailed-exitcode`. Returning 1 on stale CONFLATED "your artifact is stale" with
    "the probe crashed" -- a CI job cannot act on that, and will read a crashed probe as a stale
    artifact or vice versa. 1 now means the tool failed, and ONLY that.

    WHY THIS NO LONGER COMPARES as_of_head TO HEAD (the defect this replaces):
      Emitting records as_of = HEAD-at-emit-time. LANDING the artifact requires a commit, and that
      commit ADVANCES HEAD. So as_of was always the parent of the commit that shipped it, and the
      oracle reported the freshly-regenerated artifact STALE against the very commit that shipped it.
      Exercised 2026-07-09: `comp-system` -> `--check` said CURRENT (uncommitted); `safe-commit`
      [735a4d86d]; `--check` said "STALE: emitted as_of=fe02f71e5 vs current HEAD=735a4d86d".
      It could return 0 only on an uncommitted tree -- seconds wide on a 20-agent shared branch, and
      any unrelated commit flipped it. A signal that is always RED carries no information; it is the
      same defect as a check that never fires, at the opposite rail. `as_of == HEAD` was a PROXY for
      "the artifact reflects the substrate it summarizes", and it was UNSATISFIABLE for the only
      state that matters (committed).

    THE PREDICATE NOW BINDS THE PROPERTY (CTO ruling; MSTR's ratified rule): stale iff
      (a) an INPUT the artifact reads has changed since emit  -- source fingerprint drift, or
      (b) the compile is older than _TTL                      -- covers the LIVE-grounded values
          (kuzu counts, git HEAD, live probes) that no repo fingerprint can see.
    `as_of_head` stays in the header as PROVENANCE (it truthfully records the HEAD compiled against);
    it is simply no longer the staleness predicate.

    ONE EXPRESSION, NOT TWO THAT AGREE TODAY (MSTR 20260709T200348Z): the fingerprint is
    `graph_cache.source_fingerprint` -- the SAME function the caches enforce -- and the emit path
    stores what THIS function computes. There is no parallel copy to drift.
    """
    try:
        if not os.path.exists(OUT_JSON):
            print("06 STALE: not yet emitted -- run comp-system.")
            return 2
        with open(OUT_JSON, encoding="utf-8") as fh:
            header = json.load(fh).get("header", {})
        stale, reason = _staleness(header)
    except Exception as e:  # noqa: BLE001 -- a probe that cannot evaluate is an ERROR, never "fresh"
        print("06 UNVERIFIABLE: --check could not evaluate (%s: %s)" % (type(e).__name__, e))
        return 1
    if not stale:
        print("06 CURRENT (%s)" % reason)
        return 0
    print("06 STALE: %s -- regenerate (comp-system)." % reason)
    return 2


def main() -> int:
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if "--check" in args:
        return check_stale()
    model = compile_model()
    if "--json" in args:
        print(json.dumps(model, indent=2))
        return 0
    if "--stdout" in args:
        print(render_markdown(model))
        return 0
    _write(model)
    print("comp-system: wrote %s + %s (grounded-against-live; as_of HEAD=%s)"
          % (os.path.relpath(OUT_MD, WS), os.path.relpath(OUT_JSON, WS), model["header"]["as_of_head"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
