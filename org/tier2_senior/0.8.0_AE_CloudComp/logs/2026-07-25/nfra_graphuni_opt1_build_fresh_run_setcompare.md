# NFRA_GRAPHUNI OPT1-BUILD — fresh --full run + member-level set-compare — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch NFRA_GRAPHUNI OPT1-BUILD (20260725T064248Z) + supplement (20260725T064432Z)
**Status:** COMPLETE

---

## Objective

Execute CVO~Z's Andrew-delegated Option 1 ruling's three steps, measurement only, hard boundary against
any live ingestion wiring: (1) fresh `--full` producer run, vintage stamped; (2) resolve the 2
`S3KEY_FIRM_UNRESOLVED` keys; (3) canonicalize polarity/namespace and run a member-level set-compare
against the P0-CVO fixture, upgrading CVO~Z's count reconciliation to a proven-or-refuted verdict.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3` | `extract_gold_compute.py --full --stats --out <own path>` | PASS (TRUE_RC=0, in-stdout) | fresh producer run, 1366 nodes/3609 edges, 0 unresolved, 0 deferred |
| `git log -S "_READ_OVERRIDE"` | history search for the 2-key resolution | PASS | found it already landed, commit `62063ee602`, this same lane |
| `python3` (custom reconstruction script) | `opt1_setcompare.py` — rebuild TraceGraph from producer JSON, run real `cli.main()` blast | PASS (TRUE_RC=0) | 11/28 match, SET-IDENTITY REFUTED |

**What worked:** checking `git log -S` for the unresolved-key fix before assuming I needed to newly ground
it — found the work was already done and verified by a prior commit's own before/after numbers, saving a
full re-investigation.

**What failed:** nothing outright, but the reconstruction surfaced a residual (see Findings) I could not
fully root-cause within this pass's scope — disclosed as a limit, not smoothed over.

**Gap found:** `TraceGraph.find_node()`'s substring-match semantics interact with the set-compare in a way
not fully traced — real code, unmodified, same in both the fixture's original capture and this
reconstruction, but its effect differs between the two graphs in a way this pass didn't finish tracing.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

Confirmed write-safety before running anything (`extract_gold_compute.py` has zero `boto3`/S3 calls — pure
local JSON output; docstring's "(uploaded to s3://...)" describes a LATER, separate coordinated-derive step
this script does not itself perform). Ran the fresh `--full` producer to this lane's own output path
(did not touch the historical `NFRA_GRAPHUNI.P1-D.gold_compute_producer.json`), stamped the vintage myself
since the tool's own `generated_at` field is null by design. Confirmed the 2 previously-unresolved keys are
already resolved by a prior commit (`62063ee602`, this same lane) rather than needing fresh grounding work.
Built a reconstruction script that inverts the producer's own id-canonicalization
(`pipeline:<firm>:gold:<body>` → `gold:<body>`, `opal-data-<firm>/<key>` → `s3:<key>`) and flips `READS_S3`
polarity to match `build_graph`'s own convention (the specific detail CTO~Z flagged), then drives the real
`cli.main()` blast code in-process against the reconstructed graph — same method as the earlier
marker-head re-assert, different graph source. Result: **11/28 (39%) match, SET-IDENTITY REFUTED** — same
rate and same root cause (missing cross-script `READS_S3`-mediated reachability at script grain) as the
live marker-head measurement earlier this session, now independently confirmed a third way (live kuzu,
this fresh producer reconstruction, and both showing the identical function-clean/script-broken split).

Delivered `GRAPHUNI_OPT1_RUN.md` + sidecar to the census dir (CTO~Z's BASE_EXEC lane, written for his
commit, per established convention this session).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Trust the git-history evidence for step 2 rather than re-derive the fix from scratch | `62063ee602`'s own commit message states the exact before/after (0 unresolved, was 2) and names the grounding source; re-verified it still holds in the fresh run rather than redo the original grounding work. |
| Disclose the `find_node` substring-match residual rather than omit it | The headline verdict (REFUTED) doesn't change whether or not this residual is explained, but silently smoothing over an unexplained detail in a measurement report would violate this whole project's own grounding discipline. |
| Did not re-run comp-trace/comp-xref against the reconstruction | Dispatch centered on the producer's own CALLS/READS_S3/WRITES_S3 output (what comp-blast consumes directly); named as a scope boundary in the deliverable rather than silently narrowing without saying so. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_OPT1_RUN.md` | New — the run report | No — CTO~Z's BASE_EXEC lane |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_OPT1_RUN.sidecar.json` | New — full 28-target result | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/gold_compute_producer_FULL_20260725.json` | New — Step 1 fresh producer output | Yes — own lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/opt1_setcompare.py` | New — Step 3 reconstruction script | Yes — own lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/OPT1_SETCOMPARE_20260725_result.json` | New — full result JSON | Yes — own lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_opt1_build_fresh_run_setcompare.md` | This log | Yes — own lane |

---

## Blockers

None. Hard boundary (no ingestion wiring) observed throughout — confirmed nothing this session wrote to
S3 or the live Nessie/Kuzu store.

---

## Current State

Set-identity REFUTED at member level (11/28), consistent with and independently confirming the earlier
live-marker-head measurement's root cause. The 2 previously-unresolved keys are confirmed already fixed.
Reported to CTO~Z + CVO~Z this turn (CVO~Z verifies against the same fixture recipe it already used, per
the dispatch).

---

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the set-compare (script + full per-target JSON on disk, reproducible);
   decide whether the `find_node` substring-match residual needs its own follow-up trace.
2. **[1.0.0_SA_CTO~Z]** Commit the deliverable; the ingestion-wiring decision (still gated, per this
   dispatch's own hard boundary) is the next step once the set-compare result is accepted.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
