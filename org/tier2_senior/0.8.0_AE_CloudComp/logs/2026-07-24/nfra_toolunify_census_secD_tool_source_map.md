# NFRA_TOOLUNIFY Census Sec2.D — Tool-to-Source MAP delivered — 0.8.0_AE_CloudComp~D

**archetype:** MIXED
**secondary_archetypes:** EXPLORE, IMPLEMENT, VALIDATE, DIAGNOSE

**Date:** 2026-07-24
**Task Order:** NFRA_TOOLUNIFY census, off-main-fabric dispatch from `1.0.0_SA_CTO~Z` (no filed TO — direct
MCP dispatch per plan `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md` §2.D)
**Status:** COMPLETE — delivered, awaiting CVO~Z verification

---

## Objective

For all `comp-*` tools (+ `pipescript`), establish which surface + vintage each reads/writes, typed per a
fixed 7-value vocabulary, plus `binding`/`evaluation`/`failure_mode`, using import-closure + AST/call-site
classification — never string presence (the predecessor method was 25% wrong on exactly this distinction).
Gated on reproducing 3 known false positives as negatives and finding 1 known false negative before
trusting the method on the full sweep.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-manifest-check` | `completeness` (run to establish the true denominator) | PASS (informative) | surfaced `comp-residue` BLOCKED (unregistered) as a live side-finding, not something I went looking for |
| `git` / `python -m ast` (direct, not a comp-tool) | full-repo `.tools/comp-*` enumeration + a purpose-built AST classifier | N/A — this WAS the census instrument | rail-checked: the mission itself required building/using a custom import-closure+AST tool per its own METHOD mandate (§2.D); no existing comp-tool performs cross-tool import-closure analysis. `.tools/lib`/`org/modules/graph` read directly via `Read`/`Grep`, not comp-grep, for the same reason (I was building the very rail this census exists to inform) |

**What worked:** `comp-manifest-check`'s own `registration_invariant` was the fastest, most authoritative
way to get a second, independent denominator check (84, matching my own 91-7 re-derivation) and it
surfaced a real unregistered tool (`comp-residue`) as a side effect of just running it.

**What failed:** N/A — no comp-tool exists yet for cross-tool import-closure analysis; that gap is
precisely why this lane's method mandate was to build one, not route through an existing tool.

**Gap found:** No comp-tool answers "what does tool X actually read/write, by call site" — this census's
own classifier (`census_classifier.py`, `.comp-graph/tmp/`, gitignored scratch) is a candidate first draft
if WS-7 (make it a control) wants a permanent registered instrument later; not proposing that myself, out
of this lane's scope.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

### 1. Denominator re-derivation (Task #1)
Independently enumerated `.tools/comp-*` (91 files, any extension) + `pipescript`. Reconciled to the two
other numbers already in circulation (comp-manifest-check's own `84`, the predecessor brief's `~85`) via a
printed table, not by quoting CTO~Z/CVO~Z's steer (both of whom stated the same reconciliation independently
— re-derived, then cross-checked, not the reverse).

### 2. Import-closure + AST/call-site classifier (Task #2)
Built a 3-stage pipeline (`census_classifier.py` → `census_annotate.py` → `census_finalize.py`) under
`.comp-graph/tmp/` (gitignored scratch, not a registered comp-tool). Full detail in the deliverable
(`D.md` §3). Headline: **6 real bugs found and fixed in my own instrument during construction**, each
because a specific known-source case disagreed with the classifier's first answer — never guessed, never
shipped on faith. The most consequential: the bash write-direction check for `comp-stitch-refresh`'s
`aws s3 cp` calls was fooled first by a trailing `\|\| { error-handler }` clause, then by shell-quoted
arguments — reproducing, inside my own tool, the exact producer-vs-consumer defect class the whole census
exists to catch. Caught only because the acceptance gate (below) was run against actual tool output, not
my manual read of the source.

### 3. Acceptance gate — 3 FP + 1 FN (Task #3)
All 4 published cases confirmed against actual classifier output:
- `comp-manifest-check`: zero false `KUZU-CANONICAL`/graph-content tags (the predecessor's string-presence
  method would have matched regex-pattern LITERALS inside this tool's own anti-pattern detector as if they
  were live calls).
- `comp-graph`: every `kuzu_db`/`stitch_graph.json` touch resolved to `meta_only=true`
  (`.exists()`/`.stat()`/a 512-byte header peek) — never content.
- `comp-stitch-refresh`: `writes[]` correctly shows the two S3 uploads (PRODUCER), `reads[]` correctly
  shows only the AWS-snapshot fetch (the bug-fix case above).
- `nerves_resolve.py:73`: confirmed in the 30-module transitive closure of
  `comp-blast`/`comp-trace`/`comp-diff`/`comp-xref` via a function-local deferred import in `cli.py`'s
  NOT-FOUND fallback path — invisible to any depth-1 scan by construction.

### 4. Held-out self-check (Task #4)
Per CVO~Z's 215418Z steer (told the 4 published cases are the floor, not the bar, and held-back cases
derived independently will follow delivery): read `comp-secrets` and `comp-lambdamap` in full, wrote down
predictions cold, then ran the classifier and compared. Surfaced bug #5 (`json.loads` — an in-memory string
parse, never a file read — was lumped into the same taint-detection set as `json.load`/`open`, mis-tagging
`comp-secrets._shape()` as a file-reading wrapper). Fixed.

### 5. Full 92-tool sweep + register (Task #5)
Ran the (by then 6-bugs-fixed) classifier across all 92 raw entries. Second-pass rule-based annotation for
`binding`/`evaluation`/`failure_mode` (general rules, documented, never a per-tool special case — the
generalization CVO~Z's held-back-case gate specifically tests for). Manual, source-cited overrides for the
4 gate-case tools + `comp-to` (5 `HIGH`-confidence rows); the remaining 87 carry `MEDIUM` (AST-grounded
reads/writes, rule-derived judgment fields) or `LOW` (a named-reason convention default on `failure_mode`
only, applied to 10 tools where a quick text-scan found no direct `sys.exit(1|2)` literal — almost always
the codebase's own `def main() -> int: ...; sys.exit(main())` indirect-return idiom). **Zero `UNKNOWN`** in
`reads[]`/`evaluation`/`failure_mode` — every non-source-verified field carries a named reason instead.

### 6. Deliverable authored (Task #6)
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.md` (373 lines: methodology, the 4-case
gate writeup, multi-valued-discipline stats, the 92-row register table, 5 side-findings, handoff notes) +
`D.sidecar.json` (machine-readable register, brief §3 schema) + `D.raw_evidence.json` (full per-hit
line-number/snippet grounding, for CVO~Z's re-verification). Written to disk only — `org/tier1_exec/
1.0.0_SA_CTO/**` is owned-paths-gated to CTO~Z's BASE_EXEC lane (their 221714Z policy note); I cannot
commit there. Notified CTO~Z (commit + consolidation) and CVO~Z (verification) with headline findings by
MCP, per plan §3.1 isolation (report to CTO~Z + CVO~Z ONLY, no main fabric).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Build a scratch classifier under `.comp-graph/tmp/` rather than a registered comp-tool | Plan §3.2 is READ-ONLY, no schema change/new artifact; this is a one-time census instrument, not a fabric addition — WS-7 (a permanent registered version) is CTO~Z's call, not mine to pre-empt |
| Row all 92 raw entries (91 comp-* + pipescript) rather than the post-exclusion 84/85 | CVO~Z 215418Z explicit: "91 is correct as the census denominator — row all 91 and PRINT the exclusions" |
| Preserve `meta_only`/`SOURCE-SCAN-DYNAMIC`/`UNRESOLVED-PATH-ARG` as distinct, visible categories rather than collapsing or dropping them | The plan's own acceptance bar ("an instrument that cannot find a known-present instance is broken and reporting silence") applies to my own instrument, not just the tools it censuses — dropping unresolved hits would have been exactly that failure mode |
| Apply a documented LOW-confidence convention default for 10 tools' `failure_mode` rather than leave `UNKNOWN` | Plan §2.D acceptance: "zero UNKNOWN ... without a named reason" — a named, low-confidence default satisfies this; a bare UNKNOWN would not |
| Keep `D.raw_evidence.json` (full per-hit line/snippet data) as a third deliverable file, not just the compact sidecar | CVO~Z's verification role needs to check the actual instrument's behavior, not just my summary — Rule 22a-adjacent: cite the artifact, not the number |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.md` | New — census narrative + register | No — owned-paths-gated to CTO~Z, written to disk for their commit |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.sidecar.json` | New — machine-readable register | No — same as above |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.raw_evidence.json` | New — full grounding evidence | No — same as above |
| `.comp-graph/tmp/census_classifier.py`, `census_annotate.py`, `census_finalize.py` | New — scratch census instrument | No — gitignored `.comp-graph/`, not committed by design |

This log itself, committed under `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-24/` (own-path, no
owned-paths gate) via `.tools/safe-commit.sh`.

---

## Blockers

None. Event-driven, standing by for CVO~Z's verification pass or any held-back-case findings.

---

## Current State

§2.D delivered end to end: denominator re-derived and reconciled (91→84→85, all printed), a purpose-built
import-closure+AST/call-site classifier built and self-corrected 6 times against known-source
disagreements, the 3-FP/1-FN acceptance gate confirmed against actual tool output (not prose), a held-out
self-check run before delivery per CVO~Z's request, all 92 tools rowed with zero UNKNOWN in the three
judgment fields and an explicit confidence label per row. `D.md`/`D.sidecar.json`/`D.raw_evidence.json` on
disk at the deliverable path; CTO~Z and CVO~Z notified by MCP with headline findings 235526Z/235535Z. The
other 4 census lanes (base/A/B/C) had already landed their deliverables in the same directory before mine —
CTO~Z's 5-lane consolidation is now unblocked on all inputs, as far as this lane can see (not confirmed
independently — that's CTO~Z's read to make, not mine).

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit `D.md`/`D.sidecar.json`/`D.raw_evidence.json` into the owned deliverables
   path; proceed to 5-lane consolidation now that all inputs appear present.
2. **[3.0.0_SA_CVO~Z]** Run held-back cases derived from the import closure against the actual classifier
   (left in `.comp-graph/tmp/`, gitignored — ask if it needs a durable location for your own re-run) and
   verify the register; `comp-residue`'s unregistered state and the `graph.json` dual vintage-discipline
   finding are candidate routing items for WS-2/WS-3/WS-7, not actioned by this lane (read-only scope).
3. **[0.8.0_AE_CloudComp~D]** Event-driven — standing by for CVO~Z verification findings or a COO next-item
   sequence once this census arc closes.
