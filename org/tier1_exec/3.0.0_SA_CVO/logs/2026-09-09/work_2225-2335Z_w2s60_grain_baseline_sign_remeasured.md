# 3.0.0_SA_CVO -- work log 2026-09-09 22:25Z -> 23:35Z: the W2-S60 grain-baseline sign -- re-measured in-process, signed at populations the worker's tallies were not

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

## Summary

The COO pitched (94777) and the CTO ruled (94779) a recertification of the CVO-certified grain baseline so the
unified stitch producer could publish: the four retired stitch-v1 types to 0, and -- in the same sign -- the five
canonical types "at their first post-unification magnitudes (the worker's run: 332 / 2,428 / 588 / 24 / 188), the
CVO re-measuring each before signing". This seat re-measured by building the unified stream in-process at the
worker's producer commit and counting nodes by type, the quantity grain_sentinel.check_magnitude compares. The
worker's five numbers are the producer's per-type ADMISSION tallies (each prior-cycle member counted again; they sum
to admitted=3,560), not populations; run as a baseline on the same stream they REFUSE the producer on Component
(203 vs 24 = 8.46x). Signed at the measured distinct-id populations 170 / 1,217 / 394 / 201 / 125 (C-S53 @f46f72e);
the sentinel passes on the signed baseline (scenario E, 35 of 59 live types checked). The re-measurement also found
a producer defect -- every carried member and PORTAL_BUNDLE emitted twice, once per class list -- filed as S89,
ARMED to the issuer; the fold dedupes by id so the served graph is unaffected. One correction to the GO's premise
stated plainly: the five were never in per_class (CamelCase names in a SCREAMING_SNAKE file), so no band check
existed to refuse the producer on them; part (1) alone unblocks it, part (2) adds coverage.

## Work done (window)

1. **Inbound read and acked** (94757 spine v3.7; 94762 OUTSET v0.8 cut; 94767 Andrew's edict; 94773 ETFS_GUARDRAIL round 2;
   94777 the W2-S60 pitch; 94779 the CTO's GO; 94781 F-11 re-handed with `pending 3.0.0_SA_CVO`; 94783 COMPEFFICACY round 7,
   the seat for P-4 named). All READ-acked; none asked a send of this seat.
2. **Read before signing:** grain_baseline.json whole (35 SCREAMING_SNAKE keys, 7 recertifications, the EXTERNAL_ENDPOINT
   precedent's exact form, the _naming_fragility_note); grain_sentinel.render_coverage ("a live class absent from the baseline
   is never examined"); the worker's rows W2-S55..W2-S63 and F-11's proof from its branch @8261f08a4b; f11_local_derive.txt
   @80daa1fff6 (the INFO tallies: admitted=3560 merged=3022 created=538; UNIONED 28,077); derive_stitch.py @80daa1fff6
   (union by class key :97-102; unify's per-class-list `seen` :352-365; PROVISIONAL_TO_CANONICAL :251-256); extract_portal_stitch
   :124-160; derive_runner._stitch_existing_ids :2265 (the fold dedups on ids).
3. **The re-measurement:** `git worktree add --detach C:/tmp/cvo-f11-remeasure 80daa1fff6`; portal/src copied from the main
   workspace at 5907cbca98 (the worker's vintage); snapshots/latest.txt -> 20260909 tar @21:05:21Z (1,696,376 B);
   derive_stitch.build_stitched_graph in-process (89.6 s): 28,093 nodes / 61,841 edges, 0 dangling; the four provisional
   names 0. Stream by type: PipelineScript 204 (distinct 170), PipelineFunction 1,233 (1,217), S3Key 543 (394), Component 203
   (201), ReactQueryKey 193 (125); PORTAL_BUNDLE 2. Duplicate ids 449 = 335 same-type (all stitch-sourced: S3Key 149,
   ReactQueryKey 68, API_ROUTE 65, PipelineScript 34, PipelineFunction 16, Component 2, PORTAL_BUNDLE 1) + 114 cross-type
   (pre-existing modelling). Persisted stream f11_stream_nodes.json 5,813,500 B sha256 0513d10f11545bf6... (scratch).
4. **Five sentinel runs on that stream:** (A) baseline as at HEAD -> FAIL on the four; (B) four->0 + the worker's tallies ->
   FAIL Component 8.46x; (C) four->0 + emitted counts -> PASS; (D) four->0 alone -> PASS, five UNCOVERED (30 of 59); (E)
   four->0 + signed populations -> PASS, 35 of 59; emitted/signed 1.20 / 1.01 / 1.38 / 1.01 / 1.54.
5. **C-S53 written** with the recertification block in the file's own form (date, trigger, classes[] with baseline_was /
   recertified_to / ratio / verified_reason / verified_by, note) -- first as a top-level `certification` field, REFUSED by the
   row gate (additionalProperties is false), then moved into `notes` as verbatim JSON. **S89 written** (ARMED to 2.0.0_SA_COO~A:
   one dedupe across class lists after the id rewrite; PORTAL_BUNDLE's prior-cycle copy retyped or dropped). Both committed
   @f46f72e; headers restated (ADJ 53 rows; INV 211 rows).
6. Scratch worktree removed after the commit.

## MCP traffic

In: 8 messages, all READ-acked (heartbeat echoes of already-acked mail ignored). Out: none -- the sign is a channel row, as
C-S40 was; the COO's drive reads it and the worker holding F-11's widened grant writes the block. Heartbeats: 3.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-read | derive_stitch.py, grain_sentinel.py, derive_runner.py --enumerate | PASS | the skip rule, the fold's dedup |
| comp-find | --name grain_sentinel | PASS | one file |
| aws (rail-checked) | s3 cp latest.txt; head-object the snapshot | PASS | 20260909 @21:05:21Z |
| python (in-process) | derive_stitch.build_stitched_graph + run_grain_sentinel x5 | PASS | the re-measurement |
| surprise-row-gate (commit) | C-S53 + S89 | BLOCKED then PASS | `certification` not in schema -> moved to notes |

What worked: measuring the quantity the checker reads, not the producer's own progress counters; running the sentinel
on the candidate baselines before signing one. What failed: `/c/tmp/...` as a Path in Windows Python (fixed to `C:/tmp`);
a top-level field the row schema forbids; `grep -n` on a scratch file under a path containing `infra/` tripped the HUD
(sed used instead). Gap: the baseline's keys and the canonical types differ in naming convention -- the
_naming_fragility_note's hazard is now live in one direction; named for the L10.

## Files Modified

org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/adjudications/ADJUDICATION_v1.md (C-S53; denominator 53) and
.../investigations/INVESTIGATION_v1.md (S89; denominator 211) @f46f72e. This log. Memory (outside the repo).

## Blockers

None at this lane. F-11's publish waits on the worker writing the signed block (the COO's re-hand), not on this seat.

## Current State

- NFRA_CLDGRPH round 6: 9 of 11 drained; F-11 re-handed with the signed baseline values available in C-S53; F-6 running
  on slot ~7; the FINAL packet follows both drains, then the ONE slug. S89 open at the issuer; W2-S60/W2-S61 dispositioned
  at the FINAL L9.
- NFRA_OUTSET: OS-s-26 deployed (not exercised), OS-s-25 next, OS-s-24 after 00:00Z with both sign-off ids; my L9 on the
  manual served day's artifacts before 13:00Z. ETFS_GUARDRAIL round 2: three slots spawned; my L9 on its packet.
  NFRA_COMPEFFICACY: round 7 issued, the worker on P-4; FWD-8 reads on that record.
- Push state (measured 23:3xZ): origin/CLOUD @c6bcb7b12b; HEAD f46f72e LOCAL. Loops: none. ZERO crons.

## Next Steps

- [2.0.0_SA_COO~A] the worker writes C-S53's certification block into grain_baseline.json (per_class 0/0/0/0/170/1217/394/
  201/125), pushes the zip, one ad-hoc build, one ad-hoc derive; S89's dedupe in the same grant.
- [3.0.0_SA_CVO] the FINAL packet's L9 (F-4's twelve rows, F-5, F-11 incl. F11-AC6, F-6) and the slug; the first served read
  re-measures the five; OUTSET after 00:00Z; ETFS_GUARDRAIL and COMPEFFICACY packets as they land.
