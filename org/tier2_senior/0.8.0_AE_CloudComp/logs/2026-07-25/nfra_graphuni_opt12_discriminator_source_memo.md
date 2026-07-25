# NFRA_GRAPHUNI option-1-vs-2 discriminator memo — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch (routing CVO~Z's ruling), 20260725T063020Z
**Status:** COMPLETE

---

## Objective

CTO~Z routed the last input the GRAPHUNI option-1-vs-2 architecture call needs: can the GRAPHUNI Phase-A/B
compute producer emit `READS_S3` (s3->consumer) edges at function grain, or does that relationship only
exist in `build_graph`'s AST pass? Source question only — no build, no producer change, no re-point.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `Read`/`Grep` (source) | traced `extract_s3.py`, `extract_gold_compute.py`, `trace_graph.py` call chains | PASS | found the producer already imports/calls `build_graph` directly |
| `python3 -c "import json..."` | inspected `NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` + `NFRA_GRAPHUNI.P1.d_s3key_firm_qualified.json` on disk | PASS | found 192 already-computed READS_S3 edges, matching two of this session's own missing-blast-radius nodes |
| `grep -rln "gold_compute_producer" --include="*.py" .` | search for an ingestion/fold consumer of the producer's output | PASS (zero hits, itself the finding) | confirmed no script reads that JSON back in — the integration gap |

**What worked:** reading the actual committed producer-output JSON directly (not just the producer's
source code) turned a source-only question into a decisive answer — the capability isn't hypothetical, it
already ran and its output is sitting on disk, cross-referenceable against this session's own earlier
re-measurement (the same two node ids, `A_00.accounts_dimension`/`A_01.advisor_assignments`, appeared in
both).

**What failed:** nothing.

**Gap found:** none new in tooling — the gap found is architectural (a computed artifact with no
consumer), the memo's actual subject.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

Traced `build_graph`'s READS_S3 derivation to `extract_s3.py:448-455` (`_extract_s3_reads()`,
`extract_s3.py:296-322`) — a whole-file regex/pattern scan, structurally SCRIPT-grain by construction (no
per-function pass exists for reads, unlike writes which have two dedicated function-level passes). Traced
the GRAPHUNI compute producer (`infra/aws/globgrph/extract_gold_compute.py`) and found it already imports
and calls `build_graph` directly (`:63`, `:82-84`) and already has READS_S3-consuming logic at the matching
grain (`:182-195`). Found a prior, committed run of this producer
(`org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1-D.gold_compute_producer.json`) already contains 192
READS_S3 edges, two of which are the exact node ids this session's own earlier re-measurement
(`REASSERT_20260725_result.json`) found missing from a live blast radius. Confirmed via
`grep -rln "gold_compute_producer" --include="*.py" .` (zero hits) that nothing in the codebase ever reads
this file back in — no ingestion/fold step exists. Cross-checked the Phase-A deferral count
(`coverage.phase_b_deferred_count: 112`) against CVO~Z's "306 needed" figure: 192+112=304, within rounding
of 306 given the producer's own 2 named `S3KEY_FIRM_UNRESOLVED` cases. Delivered
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_OPT12_DISCRIMINATOR.md` (CTO~Z's
BASE_EXEC lane, written for his commit per established convention).

**Headline answer**: neither original option is quite right. The producer does not need new derivation
capability (it already has and has exercised it); the actual gap is an unbuilt ingestion path between an
already-computed artifact and the live graph, plus a smaller, already-named Phase-B scope item (~112
deferred read-only-input edges). This reframes the option-1-vs-2 choice into a smaller, costed next step
rather than a fork between two expensive alternatives.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Cross-reference the producer's committed JSON output against this session's own earlier re-measurement result | Two independent artifacts from two different investigation threads this same session corroborating each other (same missing node ids) is stronger grounding than either alone, and was free to check since both were already on disk. |
| Flag the unstamped vintage of `gold_compute_producer.json` rather than guess a date | The file's own `generated_at` field was null in this copy; CLAUDE.md Rule 22's grounding discipline requires stating what is and isn't known, not rounding an absence into a claim. |
| Did not execute `extract_gold_compute.py` or attempt to wire the ingestion myself | Explicitly out of scope per CTO~Z's "source question only — no build, no producer change, no re-point" instruction. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_OPT12_DISCRIMINATOR.md` | New — the source memo | No — CTO~Z's BASE_EXEC lane, written for his commit |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_opt12_discriminator_source_memo.md` | This log | Yes — own lane |

---

## Blockers

None.

---

## Current State

Memo delivered with file:line citations for every load-bearing claim, per the dispatch's requirement.
Reported to CTO~Z + CVO~Z this turn. The option-1-vs-2 architecture call is now theirs to make on grounded
cost, per the ruling chain (Andrew -> CVO~Z sequencing ruling -> CTO~Z routing -> this memo -> back to
CTO~Z/CVO~Z for the decision).

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit the memo; make the option-1-vs-2 call (now reframed as a narrower
   ingestion-wiring question) with CVO~Z.
2. **[3.0.0_SA_CVO~Z]** Verify the file:line citations; the two cross-referenced node ids are independently
   re-checkable against both committed artifacts.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
