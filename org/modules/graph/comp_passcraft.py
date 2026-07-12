#!/usr/bin/env python3
"""
comp_passcraft.py -- NFRA_PASSCRAFT.TO-1 backend: the recon-scaffolding SDK.

Turns the hand-run tool front-pass from a per-tool re-derivation into a repeatable, evidence-emitting
procedure. It templates the SCAFFOLDING -- the 8 fixed opening moves, the 12-shape failure taxonomy as
a hunt-order, the archetype->lead-probe map -- and `comp-passcraft recon <tool>` runs ONLY the
MECHANICAL moves (read both layers, map the write surface, find the cache/oracle, enumerate the
universe + print the denominator, slot ground-truth-per-target, load the archetype's lead probes) and
emits an EVIDENCE PACK.

THE LOAD-BEARING INVARIANT (AC1/AC4, NFRA_PASSCRAFT_PRD sec.0 -- CTO~A gates this hardest):
    IT STOPS AT THE VERDICT DOOR. IT HAS NO VERDICT ENGINE. NO COMPONENT COMPUTES A PASS/FAIL.
A harness must encode the right answer to judge an output; if the right answer is computable it is a
second implementation of the tool, and two implementations that agree may share a predicate
(comp_route.py's own floor self-test passed forever, seeded with a string that never reached the
broken branch). So the verdict stays a hand-run paired test + falsifier, with the sovereign watching.
The evidence pack this returns carries NO `verdict` / `pass` / `fail` field -- structurally, by
construction -- so PASSCRAFT can be SHOWN UNABLE to emit a verdict (the AC4 mutant-kill on itself).

R0 / rc-check (PRD sec.3c): every emitted line carries a CLASS -- OBSERVED (a command ran and this is
its output), INFERRED / NOT-CHECKED (a DYNAMIC question -- which-branch-ran / did-a-side-effect-happen
-- that source cannot answer), or SLOT (a move the human must complete). A read that FAILS is
INVOCATION-ERROR, never a negative observation (a failed read is not "0 found").

Sovereign boundary: no bd / 49F / Schwab / opal-data-bd read or target. Read-only on the estate; the
recon session would map its OWN write surface only (this recon does not run the tool under test).

Usage:
    comp-passcraft recon <tool> [--archetype <shape>] [--json]   # the mechanical evidence pack
    comp-passcraft taxonomy [--json]                             # the 8 moves + 12 shapes + probe map
    comp-passcraft --self-test [--json]                          # AC1 (no verdict) + AC4 + AC5

Author: 0.8.0_AE_CloudComp (NFRA_PASSCRAFT.TO-1). 2026-07-10.
Spec: docs/architecture/NFRA_PASSCRAFT_PRD.md (sec.0 anti-harness, sec.3a moves, sec.3b shapes);
      docs/architecture/NFRA_TOOLPASS.md (the doctrine + the 4 rules + sec.6 oracle exemption);
      TO org/projects/NFRA_PASSCRAFT/task_orders/NFRA_PASSCRAFT.TO-1.*.md @ 8dfcf1e75.
Reference (human): docs/architecture/PASSCRAFT_RECON_REFERENCE.md (cites THIS module as authoritative).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
TOOLDIR = os.path.join(WS, ".tools")
# Per-tool archetype annotations have ONE home -- comp_toolgraph._ARCHETYPE_ANNOTATIONS (the sibling
# TOOLGRAPH module). recon MOVE 8 imports it directly (best-effort), so PASSCRAFT depends on no data
# FILE and no second home; comp_toolgraph_census.json is a rendered SNAPSHOT of the same dict, not a
# source. P2/P3 migrates the seed to an authoritative ToolAudit CSE stream.


# ============================================================================================
# THE TAXONOMY (PASSCRAFT owns this -- the single authoritative home; the reference doc renders it).
# ============================================================================================
# The 8 fixed opening moves, each with the FALSIFIER that forces the check (PRD sec.3a).
MOVES = [
    ("READ BOTH LAYERS (wrapper + backend)",
     "if the wrapper execs a backend you did not read, your read is of the SHIM, not the tool."),
    ("MAP THE WRITE SURFACE -- before running anything",
     "a 'removable/opt-in' write is safe ONLY if 0 consumers read it; enumerate them (R4). "
     "The move that would have caught tool-1's gate-disabling D9."),
    ("FIND THE CACHE / ORACLE",
     "a fixture used AS the measure passes forever; a shared cache is poisonable across agents."),
    ("ENUMERATE THE TARGET UNIVERSE FROM SOURCE + PRINT THE DENOMINATOR",
     "a count from the tool's own report is testimony from the defendant (R3); print the denominator "
     "of every scan you reason from."),
    ("PICK BRANCH-COVERAGE TARGETS whose membership is verified FROM THE TARGET",
     "a target chosen BY NAME may never enter the branch it was claimed to cover (R3, tool-1's own miss)."),
    ("PRE-STAGE REVERT-SAFETY off the mutated store",
     "a restore-in-finally skipped by an early-exit / crash leaves the prod store mutated."),
    ("ESTABLISH GROUND TRUTH FROM A NON-SHARING INSTRUMENT (NFRA_TOOLPASS sec.6 exemption)",
     "two instruments sharing a predicate are ONE instrument; their agreement is not corroboration."),
    ("CLASSIFY ARCHETYPE -> LOAD ITS LEAD PROBES",
     "a mis-classified archetype hunts the wrong shapes first, and the pass slows to a re-derivation."),
]

# The 12 failure shapes as a HUNT-ORDER: each shape -> a one-line early PROBE (a smell-exposer the human
# runs by hand) -> the archetype it names (PRD sec.3b). A probe EXPOSES a smell; it is never a verdict.
SHAPES = [
    ("guard-asymmetry",
     "does a KNOWN-bad input make it say NO *and* a known-good make it say YES? (both directions, "
     "not just the happy path)"),
    ("success-token-bound-to-wrong-step",
     "is the PASS / exit-0 bound to the step that MATTERS, or to an earlier step that ran regardless?"),
    ("aging-oracle",
     "does the freshness/vintage signal read the DATA (date-key / content), or a PROXY (mtime / "
     "filename) that ages independently of the data?"),
    ("terminal-honest/artifact-lies",
     "does the terminal summary match the ARTIFACT it claims to describe? read the artifact, not the "
     "summary."),
    ("mislabelled-control-flow",
     "does the tool's account of which path it took match the path it ACTUALLY took? it is the "
     "defendant (R3) -- 'S3 fetch failed' when S3 was never attempted."),
    ("test-writes-prod",
     "does an exercise / test path write to a PROD store, a shared index, or the estate?"),
    ("restore-in-finally",
     "if a mutation is restored in finally/except, does an early-exit or crash SKIP the restore?"),
    ("skip-on-missing-field",
     "does a missing / empty field SKIP the check silently (read as pass) instead of failing loud?"),
    ("resource-blind",
     "does the verdict CHANGE when the resource (bucket / table / ARN) changes but the action stays? "
     "it MUST (comp-iam GRANTED-regardless-of-resource)."),
    ("undiscriminating/constant-gate",
     "does the gate value change with the input, or is it a constant that always clears? R6: name a "
     "value it must NEVER produce if measuring the intended quantity, then check it."),
    ("vacuous-that-can-block",
     "can this check BLOCK while asserting nothing -- zero-checks / no-config reading as a pass?"),
    ("correct-but-unwired",
     "is it invoked where it CLAIMS to guard? textual invocation != effective enforcement "
     "(comp-surface-check is wired to safe-commit yet advisory-only)."),
]

_SHAPE_PROBE = {name: probe for name, probe in SHAPES}

# archetype -> the lead probes to hunt FIRST (its own probe, plus the siblings that co-occur with it).
# Clusters sharing a substrate share a failure mode, so the co-occurrence is the efficiency win.
ARCHETYPE_PROBES = {
    "aging-oracle": ["aging-oracle", "undiscriminating/constant-gate", "terminal-honest/artifact-lies"],
    "resource-blind": ["resource-blind", "guard-asymmetry", "undiscriminating/constant-gate"],
    "undiscriminating/constant-gate": ["undiscriminating/constant-gate", "guard-asymmetry", "aging-oracle"],
    "correct-but-unwired": ["correct-but-unwired", "vacuous-that-can-block"],
    "vacuous-that-can-block": ["vacuous-that-can-block", "correct-but-unwired", "skip-on-missing-field"],
    "mislabelled-control-flow": ["mislabelled-control-flow", "success-token-bound-to-wrong-step",
                                 "terminal-honest/artifact-lies"],
    "terminal-honest/artifact-lies": ["terminal-honest/artifact-lies", "mislabelled-control-flow"],
    "guard-asymmetry": ["guard-asymmetry", "success-token-bound-to-wrong-step"],
    "success-token-bound-to-wrong-step": ["success-token-bound-to-wrong-step", "guard-asymmetry"],
    "test-writes-prod": ["test-writes-prod", "restore-in-finally"],
    "restore-in-finally": ["restore-in-finally", "test-writes-prod"],
    "skip-on-missing-field": ["skip-on-missing-field", "vacuous-that-can-block"],
}


def lead_probes(archetype):
    """The lead probes for an archetype, each as (shape, probe). Unknown archetype -> the full
    hunt-order (hunt everything, in taxonomy order)."""
    order = ARCHETYPE_PROBES.get(archetype)
    if not order:
        order = [name for name, _ in SHAPES]
    return [(s, _SHAPE_PROBE[s]) for s in order if s in _SHAPE_PROBE]


# ============================================================================================
# Mechanical helpers (READ-ONLY -- never runs the tool under test).
# ============================================================================================
def _read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read(), None
    except OSError as e:
        return None, str(e)   # a failed read is INVOCATION-ERROR, never "0 found"


def _resolve_layers(tool):
    """(wrapper_path, [backend_paths], kind). Reuses the same resolution shape as TOOLGRAPH: a bash
    wrapper's exec targets, stripped of any shell-var prefix; a self-contained tool is its own layer."""
    wrapper = tool if os.path.isabs(tool) else os.path.join(TOOLDIR, tool)
    txt, err = _read(wrapper)
    if txt is None:
        return wrapper, [], "unreadable"
    backends = []
    for line in txt.splitlines():
        s = line.strip()
        if s.startswith("#") or ("exec" not in s and "python" not in s):
            continue
        for m in re.finditer(r'"([^"]*\.py)"|(\S*\.py)\b', line):
            tok = m.group(1) or m.group(2)
            if not tok:
                continue
            rel = re.sub(r'^\$\{?[A-Za-z_][A-Za-z0-9_]*(?::-[^}]*)?\}?/', "", tok)
            if os.path.basename(rel).startswith("comp_log_auto"):
                continue
            cand = rel if os.path.isabs(rel) else os.path.normpath(os.path.join(WS, rel))
            if os.path.isfile(cand) and cand not in backends:
                backends.append(cand)
    return (wrapper, backends, "wrapped") if backends else (wrapper, [wrapper], "self")


_WRITE_PATTERNS = [
    (r"open\([^)]*['\"][wa]\+?['\"]", "file-write"),
    (r"\.write\(", "file-write"),
    (r"json\.dump\(", "json-write"),
    (r"put_object\(|PutObject|s3\.[^(]*put", "s3-write"),
    (r"put_item\(|update_item\(|PutItem", "ddb-write"),
    (r">\s*\"?\$", "shell-redirect-write"),
]
_ORACLE_PATTERNS = [
    (r"cache|_cache|\.parquet|\.pkl", "cache"),
    (r"fixture|baseline|golden|frozen", "fixture/baseline (frozen-as-measure risk)"),
    (r"marker|manifest|\.agent_context|head", "marker/manifest"),
]


def _scan(files, patterns):
    """Grep the given files for (pattern, label) hits. Returns (labels_found, errors). A file that
    cannot be read yields an INVOCATION-ERROR entry -- NOT an empty result (rc-check / R7)."""
    labels, errors = set(), []
    for f in files:
        txt, err = _read(f)
        if txt is None:
            errors.append("INVOCATION-ERROR: could not read %s (%s)" % (_rel(f), err))
            continue
        for pat, label in patterns:
            if re.search(pat, txt):
                labels.add(label)
    return sorted(labels), errors


def _rel(p):
    try:
        return os.path.relpath(p, WS).replace("\\", "/")
    except ValueError:
        return p


def _census_archetype(tool):
    """The tool's archetype annotation from the SINGLE home -- comp_toolgraph._ARCHETYPE_ANNOTATIONS --
    or None. Imported directly (not read from the census JSON) so recon depends on no data file and the
    annotation has one home. best-effort: import failure -> None (recon still works, emits UNCLASSIFIED)."""
    try:
        import comp_toolgraph  # sibling module; sys.path includes _HERE via the wrapper / test shim
    except Exception:  # absent sibling -> UNCLASSIFIED, recon still emits its full pack
        return None
    ann = getattr(comp_toolgraph, "_ARCHETYPE_ANNOTATIONS", {}).get(os.path.basename(tool))
    if ann and ann.get("archetype"):
        return {"archetype": ann["archetype"], "class": ann.get("class"), "source": ann.get("source")}
    return None


# ============================================================================================
# recon -- the mechanical evidence pack. NO verdict field, by construction.
# ============================================================================================
def recon(tool, archetype=None):
    """Run the MECHANICAL moves and return an EVIDENCE PACK dict. STOPS at the verdict door.

    The returned dict has NO `verdict`/`pass`/`fail` key -- structurally, so PASSCRAFT can be SHOWN
    UNABLE to emit a verdict (AC1/AC4). Each move carries a CLASS per emitted item (OBSERVED /
    NOT-CHECKED / SLOT / INVOCATION-ERROR)."""
    wrapper, backends, kind = _resolve_layers(tool)
    layers = [wrapper] + [b for b in backends if b != wrapper]
    wtxt, werr = _read(wrapper)
    wlines = len(wtxt.splitlines()) if wtxt else 0

    writes, werrs = _scan(layers, _WRITE_PATTERNS)
    oracles, oerrs = _scan(layers, _ORACLE_PATTERNS)

    # archetype: an explicit hand-classification (--archetype) wins; else the census annotation; else
    # UNCLASSIFIED (the honest state -- move 8 is the human's to complete).
    ann = None
    if archetype:
        ann = {"archetype": archetype, "class": "HAND-CLASSIFIED (this recon)", "source": "--archetype"}
    else:
        ann = _census_archetype(tool)
    arch = ann["archetype"] if ann else None
    probes = [{"shape": s, "probe": p} for s, p in lead_probes(arch)]

    moves = [
        {"move": 1, "name": MOVES[0][0], "falsifier": MOVES[0][1], "class": "OBSERVED",
         "evidence": {"wrapper": _rel(wrapper), "wrapper_lines": wlines, "kind": kind,
                      "backends": [_rel(b) for b in backends if b != wrapper] or ["(self-contained)"]},
         "invocation_error": werr},
        {"move": 2, "name": MOVES[1][0], "falsifier": MOVES[1][1], "class": "OBSERVED",
         "evidence": {"write_surface": writes or ["(none matched by the write-pattern set)"]},
         "not_checked": "whether each write is LOAD-BEARING for a downstream reader (the D9 class) -- "
                        "enumerate consumers + print the denominator (R4), hand-run.",
         "invocation_error": werrs or None},
        {"move": 3, "name": MOVES[2][0], "falsifier": MOVES[2][1], "class": "OBSERVED",
         "evidence": {"cache_oracle_signals": oracles or ["(none matched)"]},
         "not_checked": "shared across agents? poisonable? a frozen fixture used AS the measure? hand-run.",
         "invocation_error": oerrs or None},
        {"move": 4, "name": MOVES[3][0], "falsifier": MOVES[3][1], "class": "SLOT",
         "slot": "enumerate the tool's TARGET universe FROM SOURCE (not from the tool's report) and "
                 "print the denominator; this is tool-specific and the human completes it."},
        {"move": 5, "name": MOVES[4][0], "falsifier": MOVES[4][1], "class": "SLOT",
         "slot": "pick branch-coverage targets and VERIFY each target's branch membership FROM THE "
                 "TARGET (inspect the target / an observation the tool does not produce), never by name."},
        {"move": 6, "name": MOVES[5][0], "falsifier": MOVES[5][1], "class": "SLOT",
         "slot": "snapshot the write surface found in MOVE 2 (%s) OFF the mutated store BEFORE any "
                 "paired-run mutation; do not rely on a restore-in-finally." % (", ".join(writes) or "none"),
         "derived_from_move": 2},
        {"move": 7, "name": MOVES[6][0], "falsifier": MOVES[6][1], "class": "SLOT",
         "slot": "establish ground truth from an instrument that does NOT share %s's predicate. "
                 "Off-rail marker (NFRA_TOOLPASS sec.6, a NAMED EXEMPTION not a coverage gap):" % os.path.basename(tool),
         "marker": "# rail-checked: assurance oracle for %s under test (NFRA_TOOLPASS sec.6) -- must "
                   "not share the tool's predicate" % os.path.basename(tool)},
        {"move": 8, "name": MOVES[7][0], "falsifier": MOVES[7][1],
         "class": "OBSERVED" if ann else "SLOT",
         "archetype": arch, "archetype_class": ann.get("class") if ann else None,
         "archetype_source": ann.get("source") if ann else None,
         "lead_probes": probes,
         "slot": None if ann else "classify the archetype BY HAND (from the taxonomy) and re-run with "
                                  "--archetype to load its lead probes; UNCLASSIFIED means hunt the full order."},
    ]
    return {
        "tool": os.path.basename(tool),
        "recon_of": _rel(wrapper),
        "layers_read": [_rel(x) for x in layers],
        "moves": moves,
        "verdict_door": "STOP. This is an EVIDENCE PACK. comp-passcraft computes NO pass/fail. The "
                        "verdict is a hand-run PAIRED TEST (TRUE target + FALSE twin) + its falsifier, "
                        "with the sovereign watching (NFRA_TOOLPASS sec.0). Run the lead probes above "
                        "by hand; each EXPOSES a smell, none concludes.",
    }
    # NOTE (invariant): the returned dict intentionally has NO 'verdict'/'pass'/'fail' key. AC4 asserts it.


# ============================================================================================
# Rendering + CLI
# ============================================================================================
def render_recon(pack):
    L = ['=== comp-passcraft recon %s -- EVIDENCE PACK (no verdict; stops at the verdict door) ==='
         % pack["tool"], ""]
    for m in pack["moves"]:
        L.append("[MOVE %d] %s   <%s>" % (m["move"], m["name"], m["class"]))
        if "evidence" in m:
            for k, v in m["evidence"].items():
                L.append("    OBSERVED %s: %s" % (k, v))
        if m.get("invocation_error"):
            L.append("    INVOCATION-ERROR: %s" % m["invocation_error"])
        if m.get("not_checked"):
            L.append("    NOT-CHECKED: %s" % m["not_checked"])
        if m.get("slot"):
            L.append("    SLOT: %s" % m["slot"])
        if m.get("marker"):
            L.append("      %s" % m["marker"])
        if m["move"] == 8:
            if m.get("archetype"):
                L.append("    archetype: %s (%s) -- %s" % (m["archetype"], m.get("archetype_class"),
                                                           m.get("archetype_source")))
            else:
                L.append("    archetype: UNCLASSIFIED")
            L.append("    lead probes (hunt FIRST -- each exposes a smell, none is a verdict):")
            for pr in m["lead_probes"]:
                L.append("      - [%s] %s" % (pr["shape"], pr["probe"]))
        L.append("    falsifier: %s" % m["falsifier"])
        L.append("")
    L.append("=== VERDICT DOOR ===")
    L.append(pack["verdict_door"])
    return "\n".join(L)


def render_taxonomy():
    L = ["=== PASSCRAFT recon reference (the authoritative machine-readable taxonomy) ===", "",
         "THE 8 FIXED OPENING MOVES (each with the falsifier that forces the check):"]
    for i, (name, fal) in enumerate(MOVES, 1):
        L.append("  %d. %s" % (i, name))
        L.append("       falsifier: %s" % fal)
    L.append("")
    L.append("THE 12 FAILURE SHAPES as a HUNT-ORDER (shape -> early probe; a probe exposes a smell, "
             "never a verdict):")
    for name, probe in SHAPES:
        L.append("  - %-32s %s" % (name, probe))
    L.append("")
    L.append("ARCHETYPE -> LEAD PROBES (hunt these first per cluster):")
    for arch in ARCHETYPE_PROBES:
        L.append("  %-32s -> %s" % (arch, ", ".join(ARCHETYPE_PROBES[arch])))
    L.append("")
    L.append("INVARIANT: this is SCAFFOLDING. The verdict is hand-run (NFRA_TOOLPASS sec.0). No "
             "component here computes a pass/fail.")
    return "\n".join(L)


# ============================================================================================
# TO-2: the ToolAudit CSE EMITTER -- serializes a HAND-AUTHORED verdict into an NFRA_CSE-conformant
# envelope so a hand-run pass FEEDS the graph instead of evaporating (the source for TOOLGRAPH's
# Assurance plane + PASSCRAFT.TO-3 backfill). ANTI-HARNESS ONE LAYER UP (PRD sec.0):
#   verdict / class / per-rail assessment are INPUTS the caller hand-authors; NOTHING here derives
#   them. Unlike the recon pack (PRE-verdict, no verdict key at all), a ToolAudit is POST-verdict and
#   LEGITIMATELY carries `verdict`. So the emitter's anti-harness proof is NOT "no verdict key" but
#   "no verdict-DERIVING code path": emit REQUIRES a hand-authored verdict + class and FAILS CLOSED
#   without them; there is no compute step. R0 is DEFERRED (TO-R0, off CVO's lane) -- class is R1
#   self-classification only; no QUESTION-class tag is folded here.
# ============================================================================================
_TOOLAUDIT_CLASSES = ("OBSERVED", "INFERRED", "NOT-CHECKED")   # FP-R1 claim-class self-classification
_RAIL_VERDICTS = ("pass", "fail", "n/a", "unknown")
_CLASS_CONFIDENCE = {"OBSERVED": 0.9, "INFERRED": 0.3, "NOT-CHECKED": 0.1}   # serializes the FP-R1 class
# FP-R0 (FRONTPASS_RULES_canonical_20260712, R0 RULED IN 20260712): classify the QUESTION before the
# CLAIM. A DYNAMIC question answered from SOURCE is auto-INFERRED, never OBSERVED. question_class is a
# HAND-AUTHORED field (the auditor names the question's dynamism from the 5-type vocabulary below); the
# emitter LINTS it against the claim-class -- it does NOT compute it (anti-harness holds).
_QUESTION_CLASSES = ("STATIC", "DYNAMIC")
_DYNAMIC_QUESTION_TYPES = ("which-branch-ran", "what-value-flowed", "did-a-side-effect-happen",
                           "who-reads-X-at-runtime", "what-the-served-artifact-contains")
_REQUIRED_AUDIT_FIELDS = ("tool", "verdict", "class", "evidence_ref", "question_class")  # all HAND-AUTHORED


class ToolAuditError(Exception):
    """A ToolAudit failed fail-closed validation (schema / provenance / fidelity / missing judgment)."""


def _load_cse():
    """Lazy import of the NFRA_CSE contract (org/modules/graph/cse_schema.py). Lazy so recon/taxonomy
    work without it; emit REQUIRES it (NFRA_CSE-conformance is the point of TO-2)."""
    import cse_schema  # sibling module
    return cse_schema


def _resolve_evidence_ref(evidence_ref):
    """AC2 (ToolAudit layer): evidence_ref must be NON-EMPTY and point at REAL evidence. A file / file:line
    ref must resolve on disk (best-effort, WS-relative); a recon-pack / command / oracle / commit-ish ref
    is accepted as-is. Empty -> not ok (a verdict with no cited evidence is inadmissible, NFRA_TOOLPASS R1)."""
    ev = str(evidence_ref or "").strip()
    if not ev:
        return False, "evidence_ref empty -- a verdict with no cited evidence is inadmissible (R1)"
    m = re.match(r"^([\w./\\-]+\.\w+)(?::\d+(?:-\d+)?)?$", ev)
    if m:
        cand = m.group(1)
        path = cand if os.path.isabs(cand) else os.path.join(WS, cand)
        return (os.path.isfile(path),
                "resolves to %s" % cand if os.path.isfile(path) else "file ref %r does not resolve" % cand)
    return True, "non-path evidence (recon-pack / command / oracle / commit-ish) accepted"


def _evidence_is_source(evidence_ref):
    """True iff evidence_ref is a SOURCE citation (a `file` / `file:line`), False if it is an EXERCISED
    observation (a run / command / oracle / commit-ish). FP-R0 uses this to bar an OBSERVED claim on a
    DYNAMIC question backed only by source: reading the code that COULD produce a runtime fact does not
    OBSERVE it. Same file-ref shape _resolve_evidence_ref keys on, named for the FP-R0 use."""
    ev = str(evidence_ref or "").strip()
    return bool(re.match(r"^([\w./\\-]+\.\w+)(?::\d+(?:-\d+)?)?$", ev))


def build_tool_audit_cse(audit, marker_head, actor="comp-passcraft"):
    """Map a HAND-AUTHORED ToolAudit assessment (PRD sec.3d) into a valid NFRA_CSE CSE: subject=Tool,
    verb=reclassify. The verdict/class are the caller's judgment -- serialized into provenance +
    confidence, never computed. C1 edges (shared_substrate->imports, invoked_by->governs) ride along."""
    cs = _load_cse()
    tool = audit["tool"]
    conf = _CLASS_CONFIDENCE.get(audit.get("class"), 0.1)
    edges = [cs.RelationshipDelta(cs.Relationship.IMPORTS.value,
                                  cs.EntityRef(cs.Entity.MODULE.value, "module:%s" % s))
             for s in (audit.get("shared_substrate") or [])]
    edges += [cs.RelationshipDelta(cs.Relationship.GOVERNS.value,
                                   cs.EntityRef(cs.Entity.POLICY.value, "gate:%s" % g))
              for g in (audit.get("invoked_by") or []) if g and g != "UNWIRED"]
    return cs.CSE(
        event_id="toolaudit:%s@%s" % (tool, marker_head),
        schema_version=cs.SCHEMA_VERSION,
        producer={"kind": cs.ProducerKind.AGENT.value, "ref": actor},
        compiler={"id": "comp-passcraft", "artifact_class": "tool_audit", "version": cs.SCHEMA_VERSION},
        transformation={"verb": cs.Transformation.RECLASSIFY.value,
                        "subject": cs.EntityRef(cs.Entity.TOOL.value, "tool:%s" % tool),
                        "edges": edges},
        provenance=cs.Provenance(
            source=str(audit.get("oracle") or (".tools/%s" % tool)),
            locus=str(audit.get("vintage") or "recon"),
            recognizer="comp-passcraft-recon",
            evidence=str(audit.get("evidence_ref") or "")),
        execution_meta={"timestamp": str(audit.get("vintage") or ""), "actor": actor, "run_id": "toolaudit"},
        head={"marker_head": str(marker_head or "")},
        qualifiers={cs.Qualifier.CONFIDENCE.value: conf,
                    cs.Qualifier.SCOPE.value: str(audit.get("domain") or "tool")},
    )


def validate_tool_audit(audit, marker_head):
    """FAIL-CLOSED validation before emit. Returns (ok, errors). (a) the hand-authored judgment is
    PRESENT (tool/verdict/class/evidence_ref) -- the emitter cannot supply a verdict (anti-harness);
    (b) class in the R1 enum, per-rail verdicts in the rail enum; (c) the derived CSE passes
    cse_schema.validate (schema + provenance + confidence + AC6 head + fidelity decompression); (d)
    evidence_ref resolves (AC2)."""
    errors = []
    for f in _REQUIRED_AUDIT_FIELDS:
        if not str(audit.get(f) or "").strip():
            errors.append("HAND-AUTHORED field %r missing -- the emitter serializes a verdict, it does "
                          "NOT compute one (anti-harness)" % f)
    if audit.get("class") and audit["class"] not in _TOOLAUDIT_CLASSES:
        errors.append("class %r not in FP-R1 enum %s" % (audit.get("class"), _TOOLAUDIT_CLASSES))
    # FP-R0 (FRONTPASS_RULES_canonical_20260712, R0 RULED IN): classify the QUESTION before the CLAIM.
    # A CONSISTENCY LINT, NOT a verdict engine -- it checks the hand-authored (question_class, class,
    # evidence_ref) triple for coherence and computes NO tool verdict (anti-harness holds, same category
    # as the class-enum check). (a) question_class in the enum; (b) a DYNAMIC question answered from
    # SOURCE (a file:line evidence_ref) may NOT be class=OBSERVED -- reading the code that COULD produce a
    # runtime fact does not OBSERVE it, so that claim is INFERRED. Fail-closed.
    qc = audit.get("question_class")
    if qc and qc not in _QUESTION_CLASSES:
        errors.append("question_class %r not in %s (FP-R0)" % (qc, _QUESTION_CLASSES))
    if qc == "DYNAMIC" and audit.get("class") == "OBSERVED" and _evidence_is_source(audit.get("evidence_ref")):
        errors.append(
            "FP-R0: a DYNAMIC question answered from SOURCE (evidence_ref=%r is a file:line, not an "
            "exercised run) is INFERRED, never OBSERVED -- cite an EXERCISED observation (a run / command "
            "/ commit-ish) or downgrade class to INFERRED (FP-R0@FRONTPASS_RULES_canonical_20260712)"
            % audit.get("evidence_ref"))
    for rk, rv in (audit.get("rail") or {}).items():
        if rv not in _RAIL_VERDICTS:
            errors.append("rail[%s]=%r not in %s" % (rk, rv, _RAIL_VERDICTS))
    ev_ok, ev_note = _resolve_evidence_ref(audit.get("evidence_ref"))
    if not ev_ok:
        errors.append("evidence_ref: " + ev_note)
    try:
        cs = _load_cse()
        cok, cerr = cs.validate(build_tool_audit_cse(audit, marker_head))
        errors += ["CSE: " + e for e in cerr] if not cok else []
    except Exception as e:  # a build/import failure is a validation FAILURE, never a silent pass
        errors.append("CSE build/validate raised: %s" % e)
    return (not errors, errors)


def emit_tool_audit(audit, marker_head, actor="comp-passcraft"):
    """Emit a ToolAudit record IFF it validates fail-closed. Returns
    {tool_audit: <hand-authored assessment>, cse: <validated NFRA_CSE envelope as a dict>}. Raises
    ToolAuditError on any failure (never emits an invalid / unprovenanced record)."""
    ok, errors = validate_tool_audit(audit, marker_head)
    if not ok:
        raise ToolAuditError("; ".join(errors))
    cse = build_tool_audit_cse(audit, marker_head, actor)
    subj = cse.transformation["subject"]
    return {
        "tool_audit": audit,
        "cse": {
            "event_id": cse.event_id, "schema_version": cse.schema_version,
            "producer": cse.producer, "compiler": cse.compiler,
            "transformation": {"verb": cse.transformation["verb"],
                               "subject": {"etype": subj.etype, "ref": subj.ref},
                               "edges": [{"rtype": e.rtype,
                                          "target": {"etype": e.target.etype, "ref": e.target.ref}}
                                         for e in cse.transformation["edges"]]},
            "provenance": {"source": cse.provenance.source, "locus": cse.provenance.locus,
                           "recognizer": cse.provenance.recognizer, "evidence": cse.provenance.evidence},
            "execution_meta": cse.execution_meta, "head": cse.head, "qualifiers": cse.qualifiers,
        },
    }


def _resolve_marker_head():
    """The vintage a ToolAudit pins (head.marker_head, AC6): the COMMIT-ISH it was authored at (git HEAD
    short sha) -- the honest vintage, harness-attached. --marker-head overrides. Never returns empty
    (the validator would reject) so emit stays exercisable offline."""
    try:
        import subprocess
        out = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=WS,
                             capture_output=True, text=True, timeout=10)
        if out.returncode == 0 and out.stdout.strip():
            return "git:%s" % out.stdout.strip()
    except Exception:
        pass
    return "toolaudit-unpinned"


def recon_mechanical_fields(tool):
    """The MECHANICAL ToolAudit fields the recon auto-populates (tool/archetype/domain/write_surface).
    The JUDGMENT fields (verdict/class/rail/oracle/falsifier/evidence_ref/shared_substrate-selection)
    are the human's, merged OVER these. This is the TO-2 wiring of TO-1's recon into the emitter."""
    pack = recon(tool)
    m8 = pack["moves"][7]
    return {"tool": os.path.basename(tool), "archetype": m8.get("archetype"),
            "susceptible_to": [m8["archetype"]] if m8.get("archetype") else [],
            "write_surface": pack["moves"][1].get("evidence", {}).get("write_surface")}


# ============================================================================================
# self-test -- AC1 (no verdict) + AC4 (known-defective -> no flag, surfaces lead probes) + AC5
#   + TO-2 (emit: NFRA_CSE-conformant, AC2 fidelity, anti-harness = no verdict-deriving path).
# ============================================================================================
_VERDICT_KEYS = {"verdict", "pass", "fail", "passed", "failed", "defect", "defective",
                 "assured", "broken", "ok", "result", "status"}


def _has_verdict_key(obj):
    """True if any key ANYWHERE in the evidence pack is a verdict word -- the value PASSCRAFT must
    NEVER produce (R6 on itself). Recurses dicts/lists."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and k.lower() in _VERDICT_KEYS:
                return True
            if _has_verdict_key(v):
                return True
    elif isinstance(obj, list):
        return any(_has_verdict_key(x) for x in obj)
    return False


def _self_test():
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    # AC1 -- the anti-harness invariant, exercised: recon returns an evidence pack with NO verdict
    # key anywhere. This is the value PASSCRAFT must never produce if it is scaffolding not a harness.
    pack = recon("comp-freshness")
    ck("AC1.evidence_pack_has_moves", isinstance(pack.get("moves"), list) and len(pack["moves"]) == 8,
       "8 mechanical moves emitted")
    ck("AC1.NO_verdict_key_anywhere", not _has_verdict_key(pack),
       "the pack carries no verdict/pass/fail key -- structurally unable to conclude")
    ck("AC1.stops_at_verdict_door", "STOP" in pack.get("verdict_door", ""),
       "explicit verdict-door stop")

    # AC4 -- the mutant-kill on PASSCRAFT itself: a KNOWN-defective tool (comp-freshness is annotated
    # aging-oracle in the census; anti-correlated is BELIEVED) must NOT be auto-flagged, AND its
    # archetype's lead probes -- the ones that WOULD expose it -- must be surfaced.
    m8 = pack["moves"][7]
    ck("AC4.no_auto_flag_on_known_defective", not _has_verdict_key(pack),
       "recon of a believed-defective tool still emits NO verdict")
    probe_shapes = {p["shape"] for p in m8["lead_probes"]}
    ck("AC4.surfaces_the_exposing_probe", "aging-oracle" in probe_shapes,
       "the aging-oracle lead probe (the one that would expose comp-freshness) is surfaced")

    # AC4b -- a HAND-CLASSIFIED injected archetype loads the RIGHT exposing probe (resource-blind ->
    # the resource-changes-verdict probe), still with no verdict.
    injected = recon("comp-iam", archetype="resource-blind")
    inj_shapes = {p["shape"] for p in injected["moves"][7]["lead_probes"]}
    ck("AC4b.injected_archetype_loads_exposing_probe",
       "resource-blind" in inj_shapes and not _has_verdict_key(injected),
       "resource-blind -> resource-blind probe surfaced, no verdict")

    # AC5 -- class-agnostic: recon a NON-comp scanner (the 12 shapes are structural, not Opal facts).
    non_comp = os.path.join(TOOLDIR, "kill-orphans")
    target = non_comp if os.path.isfile(non_comp) else __file__
    npack = recon(target, archetype="test-writes-prod")
    ck("AC5.class_agnostic_non_comp_scanner",
       len(npack["moves"]) == 8 and not _has_verdict_key(npack)
       and "test-writes-prod" in {p["shape"] for p in npack["moves"][7]["lead_probes"]},
       "a non-comp target reconned through the SAME 8 moves + taxonomy, no schema fork, no verdict")

    # rc-check / R7: a target that cannot be read yields INVOCATION-ERROR, never a clean empty pack.
    ghost = recon(os.path.join(TOOLDIR, "comp-zzzz-does-not-exist"))
    ck("rc_check.unreadable_is_invocation_error_not_empty",
       ghost["moves"][0].get("invocation_error") is not None,
       "an unreadable target -> INVOCATION-ERROR on MOVE 1, not a silent '0 found'")

    # ============== TO-2: the ToolAudit CSE emitter (NFRA_CSE-conformant, anti-harness) ============
    def _raises(fn):
        try:
            fn()
            return False
        except Exception:
            return True

    try:
        cs = _load_cse()
        cse_ok = True
    except Exception as e:  # cse_schema absent -> emit is unusable; surface it, don't silently pass
        cse_ok = ck("TO2.cse_schema_importable", False, "cse_schema import failed: %s" % e)
    if cse_ok:
        mk = _resolve_marker_head()
        valid = {"tool": "comp-freshness", "archetype": "aging-oracle",
                 "shared_substrate": ["trading_calendar"], "invoked_by": ["UNWIRED"],
                 "domain": "aws-cloud", "susceptible_to": ["aging-oracle"],
                 "axis": {"mechanical": "reads mtime", "declarative": "docstring claims date-key",
                          "semantic": "frozen-as-of rewrite reads FRESH"},
                 "rail": {"R1": "fail"},
                 "verdict": "DEFECTIVE (believed anti-correlated) -- HAND-AUTHORED lead, not computed",
                 "class": "INFERRED", "evidence_ref": ".tools/comp-freshness",
                 "question_class": "DYNAMIC",   # FP-R0: aging-oracle = a what-value-flowed question;
                 "falsifier": "false if it reads the partition date-key, not mtime",
                 "oracle": ".tools/comp-freshness", "vintage": mk}
        rec = emit_tool_audit(valid, mk)
        ck("TO2.valid_toolaudit_emitted", isinstance(rec, dict) and {"cse", "tool_audit"} <= set(rec),
           "a hand-authored ToolAudit emits {tool_audit, cse}")
        cok, cerr = cs.validate(build_tool_audit_cse(valid, mk))
        ck("TO2.nfra_cse_conformant_and_AC2_fidelity", cok,
           "derived CSE passes cse_schema.validate @%s (schema+provenance+confidence+AC6 head+fidelity "
           "decompression): %s" % (cs.SCHEMA_VERSION, cerr))
        ck("TO2.AC2_empty_evidence_ref_REJECTED",
           _raises(lambda: emit_tool_audit(dict(valid, evidence_ref=""), mk)),
           "a ToolAudit with no cited evidence is rejected fail-closed")
        ck("TO2.anti_harness_missing_verdict_REJECTED",
           _raises(lambda: emit_tool_audit({k: v for k, v in valid.items() if k != "verdict"}, mk)),
           "emit REQUIRES a hand-authored verdict -- it has NO verdict-deriving path (anti-harness)")
        ck("TO2.verdict_serialized_verbatim", rec["tool_audit"]["verdict"] == valid["verdict"],
           "the hand-authored verdict is serialized unchanged (never altered/computed)")
        bad_class = dict(valid)
        bad_class["class"] = "MAYBE"
        ck("TO2.class_off_FPR1_enum_REJECTED", _raises(lambda: emit_tool_audit(bad_class, mk)),
           "a class outside the FP-R1 enum is rejected")

        # ===== FP-R0 (FRONTPASS_RULES_canonical_20260712): the QUESTION-class CONSISTENCY LINT =====
        # A consistency lint, NOT a verdict engine: it rejects an incoherent hand-authored
        # (question_class, class, evidence_ref) triple and computes no tool verdict (anti-harness holds).
        ck("TO2.FPR0_question_class_required",
           _raises(lambda: emit_tool_audit({k: v for k, v in valid.items() if k != "question_class"}, mk)),
           "question_class is REQUIRED -- an absent question-class is 'never classified', fail-closed")
        ck("TO2.FPR0_question_class_off_vocab_REJECTED",
           _raises(lambda: emit_tool_audit(dict(valid, question_class="MAYBE"), mk)),
           "question_class outside STATIC|DYNAMIC is rejected")
        # THE BITE: a DYNAMIC question + class=OBSERVED + a SOURCE (file:line) evidence_ref is
        # inadmissible -- reading source does not OBSERVE a runtime fact; that claim is INFERRED.
        dyn_obs_source = dict(valid, question_class="DYNAMIC",
                              evidence_ref="org/modules/graph/comp_passcraft.py:1")
        dyn_obs_source["class"] = "OBSERVED"
        ck("TO2.FPR0_dynamic_OBSERVED_from_source_REJECTED",
           _raises(lambda: emit_tool_audit(dyn_obs_source, mk)),
           "FP-R0: a DYNAMIC question claimed OBSERVED from a source file:line is rejected (must be INFERRED)")
        # NOT over-firing: the SAME dynamic OBSERVED claim backed by an EXERCISED run is admissible.
        dyn_obs_exercised = dict(dyn_obs_source,
                                 evidence_ref="EXERCISED: paired-run 2026-07-12 shows FRESH-on-stale")
        ck("TO2.FPR0_dynamic_OBSERVED_from_exercise_ACCEPTED",
           not _raises(lambda: emit_tool_audit(dyn_obs_exercised, mk)),
           "FP-R0 promotes an EXERCISED dynamic claim to OBSERVED -- it bars source, not exercise")
        # TOUCHES ONLY dynamic: a STATIC fact IS observable from source (e.g. 'does the file define X').
        static_obs_source = dict(valid, question_class="STATIC",
                                 evidence_ref="org/modules/graph/comp_passcraft.py:1")
        static_obs_source["class"] = "OBSERVED"
        ck("TO2.FPR0_static_OBSERVED_from_source_ACCEPTED",
           not _raises(lambda: emit_tool_audit(static_obs_source, mk)),
           "FP-R0 bars DYNAMIC-from-source only; a STATIC fact is observable from source")

        # ===== AC4 NON-VACUITY: the anti-harness 'no verdict-deriving path' property must BITE against an
        # INJECTED derive path -- not be vacuously true (a name-based structural check misses a
        # verdict-computer named innocuously). Neuter: wrap validate so a missing verdict is auto-supplied
        # (a DERIVE path); the missing-verdict audit is then NO LONGER rejected -> the property FLIPS,
        # proving it holds ONLY because no derive path exists. Restore in finally. =====
        _real_v = globals()["validate_tool_audit"]

        def _deriving_validate(a, mkh):   # the mutant: emit now DERIVES a verdict instead of requiring one
            return _real_v(dict(a, verdict=(a.get("verdict") or "DERIVED-BY-MUTANT")), mkh)

        globals()["validate_tool_audit"] = _deriving_validate
        try:
            _nv = {k: v for k, v in valid.items() if k != "verdict"}
            ck("AC4.anti_harness_missing_verdict_reject_is_NON_VACUOUS",
               not _raises(lambda: emit_tool_audit(_nv, mk)),
               "with an injected verdict-DERIVING path the missing-verdict audit is NO LONGER rejected -- "
               "so the real REJECT property is non-vacuous (it holds only because no derive path exists)")
        finally:
            globals()["validate_tool_audit"] = _real_v

    ok = all(c["pass"] for c in checks)
    return ok, checks


def main():
    ap = argparse.ArgumentParser(description="comp-passcraft -- the recon-scaffolding SDK "
                                             "(NFRA_PASSCRAFT.TO-1; anti-harness, no verdict engine)")
    sub = ap.add_subparsers(dest="cmd")
    pr = sub.add_parser("recon")
    pr.add_argument("tool", help="a comp-tool name (or a path to any scanner)")
    pr.add_argument("--archetype", default=None, help="a hand-classification to load its lead probes")
    pr.add_argument("--json", action="store_true")
    sub.add_parser("taxonomy").add_argument("--json", action="store_true")
    pe = sub.add_parser("emit", help="serialize a HAND-AUTHORED ToolAudit into an NFRA_CSE CSE")
    pe.add_argument("tool", help="the tool being audited")
    pe.add_argument("--audit", required=True,
                    help="path to a JSON file carrying the HAND-AUTHORED assessment "
                         "(verdict/class/rail/evidence_ref/... -- the judgment the emitter serializes)")
    pe.add_argument("--marker-head", default=None, help="head.marker_head vintage (default: git HEAD)")
    pe.add_argument("--actor", default="comp-passcraft", help="producer.ref (the auditor serial)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        ok, checks = _self_test()
        if args.json:
            print(json.dumps({"pass": ok, "checks": checks}, indent=2))
        else:
            print("=== comp-passcraft --self-test (AC1 no-verdict + AC4 + AC5) ===")
            for c in checks:
                print("  [%s] %s%s" % ("PASS" if c["pass"] else "FAIL", c["check"],
                                       ("   (%s)" % c["detail"]) if c["detail"] else ""))
            print("\n%s" % ("OK: all checks pass" if ok else "ERROR: one or more checks FAILED"))
        return 0 if ok else 1

    if args.cmd == "recon":
        pack = recon(args.tool, archetype=args.archetype)
        print(json.dumps(pack, indent=2) if args.json else render_recon(pack))
        return 0
    if args.cmd == "taxonomy":
        if args.json:
            print(json.dumps({"moves": [{"name": n, "falsifier": f} for n, f in MOVES],
                              "shapes": [{"shape": s, "probe": p} for s, p in SHAPES],
                              "archetype_probes": ARCHETYPE_PROBES}, indent=2))
        else:
            print(render_taxonomy())
        return 0
    if args.cmd == "emit":
        try:
            with open(args.audit, "r", encoding="utf-8") as fh:
                hand = json.load(fh)
        except OSError as e:
            print("INVOCATION-ERROR: could not read --audit %r (%s)" % (args.audit, e))
            return 3
        except json.JSONDecodeError as e:
            print("INVOCATION-ERROR: --audit %r is not valid JSON (%s)" % (args.audit, e))
            return 3
        if not isinstance(hand, dict):
            print("INVOCATION-ERROR: --audit must be a JSON object (the hand-authored assessment)")
            return 3
        audit = dict(recon_mechanical_fields(args.tool))   # mechanical scaffolding from recon
        audit.update(hand)                                 # the human's HAND-AUTHORED judgment wins
        audit.setdefault("tool", os.path.basename(args.tool))
        mk = args.marker_head or _resolve_marker_head()
        try:
            rec = emit_tool_audit(audit, mk, actor=args.actor)
        except ToolAuditError as e:
            print("REJECTED (fail-closed): %s" % e)
            return 1
        print(json.dumps(rec, indent=2))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
