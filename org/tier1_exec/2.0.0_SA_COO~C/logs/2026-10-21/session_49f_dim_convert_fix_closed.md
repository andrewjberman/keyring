# 2.0.0_SA_COO~C session log -- the 49F dim-convert fix, three parts, closed (2026-10-20 18:20Z to 2026-10-21 07:35Z)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, DEPLOY, VALIDATE

## Summary

Seated by MSTR on the CTO's msg 109978 (no project owned the producer; placed on NFRA_CTLPLN). The Lambda `opal-assets-bd49f-dim-convert` ran out of memory on every trading day since 2026-09-29, so the 49F `dim_account_xref` stopped at 2026-09-28. Root cause (CTO, msg 109983, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/DIAG_BD49F_DIM_CONVERT_OOM_XREF_STALE_20261020.md` @e99ca8caa4): the SCD2 fold compared tuples as strings, `flat_fee` read "0.0" from the stored partition and "0" from today's frame, so all 5,338 accounts reopened daily. Three parts, all live and read by me.

## Current State (for a reader with zero context)

- **Lambda `opal-assets-bd49f-dim-convert` (us-east-1):** MemorySize 3008, Timeout 900, CodeSha256 `blu8AGfkLFODrFvcNY7MKpk5INoT6LnyKG96pg7F1P8=` (was `Iosob5...`, 1024 MB). Rollback artifact version `e1QAG_MImQG4spPuHu8kmBA4ZjMIByAD`. Deployed `bd49f_dim_conversion.py` sha256 `bc3019570d49ac1ee10d7cd7668dfdc23a09e938d14dece7abd7c662cf00d503` (equal to both repo copies).
- **Served data, `s3://opal-data-assets/blackdiamond/49f/silver/`:** `dim_account_xref` and `dim_advisor_fee_role` carry `date=2026-10-19` (the one invoke, TO-APPLY-34, written 19:22Z 10-20; dim 288,194 rows) and `date=2026-10-20` (the scheduled 07:05Z fire of 10-21, written 07:06:23Z with the fixed code: 288,195 rows, 5,338 of 5,339 open rows kept `effective_from`, one real change). The compaction then rewrote ONE key, `dim_advisor_fee_role/date=2026-10-20/data.parquet`, at 07:21:37Z: 288,195 to 6,670 rows, new VersionId `3yoa4VexY5YhzGcdRDdb6E6YKgqjusj0`, prior `DHV5BykUPo_kPlbZZ9Umf_dJkooaLzTH` kept (versioning on). `date=2026-10-19` and `date=2026-09-28` untouched. The 15 missed days stay missing as partitions.
- **Code on `box/laptop` (LOCAL, push state not read by me; the lanes read origin at 824f66237 / 74b86b6db):** fold fix and three tests `data/assets/scripts/silver/bd49f_dim_conversion.py` + the vendored copy under `infra/aws/lambda/opal-assets/opal-assets-bd49f-dim-convert/` (merge 82484219d4b); compaction tool `data/assets/scripts/silver/bd49f_dim_compact.py` + six tests (merge 40cecd5f66f); decomposition `org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md` amendments 12-15; never-widen pair: CTO half @dee04e1b01, COO half `deliverables/2.0.0_SA_COO~C/NEVER_WIDEN_BD49F_DIM_COMPACTION_COO_HALF_20261020.md`; probe `deliverables/2.0.0_SA_COO~C/seam_probe_bd49f_scd2.py`.
- **Open, none blocking:** NFRA_SCHWABBF's own Terraform change (71495f3448e, now 3 add + 2 change) is still pending in the `opal-assets` root for its owner; the lane applied only with `-target`. The CTO closed the latest-partition-cut item (msg 110080): no cut needed, 6,670 rows at 1,193 MB peak.

## Work done

| step | cell / order | result |
|---|---|---|
| memory | CT-ck-1 TO-APPLY-34, round 38, `0.7.0_AE_CloudOps~NFRA2` (a second NFRA lane, seated on the CTO's "seat your own applier"; `~NFRA1` was blocked) | stopped at the plan (2 add + 2 change: SCHWABBF's change in the same root); I ruled `-target` in step 3a (bb84de95205); applied 1024 to 3008, one invoke (date 2026-10-19, not 10-20: the scheduler's empty event), Max Memory 1177 MB, 0 of 162 old ETags changed; I read the live config and listings |
| dtype fix | CT-cl-1, round 39, worker `~153` | `29 passed` (base 26); first run blocked by MY sparse checkout omitting `data/assets/scripts/lib` (row W153-S1); my seam probe on the real stored dim 09-28: unfixed closes 5338 of 5338, fixed 0, one-change control 1; merge 82484219d4b |
| deploy | CT-cm-1 TO-APPLY-35, round 40 | build-and-upload, `-target` apply, deployed-bytes diff equal to the pin, probe on deployed bytes 0 of 5338; NO invoke (an invoke on the default date would have overwritten the 10-19 partition) |
| compaction tool | CT-cn-1, round 41, worker `~154` | `6 passed`; my read-only plan on the real 10-19 partition: 288194 to 6669, both proofs True; merge 40cecd5f66f |
| compaction run | CT-co-1 TO-APPLY-36, round 42 | staged until I read the 07:05Z fire; GO 8616ef0dbb; one apply, `readback_equal=True`; I read the plan (merged=0 now), the next fold from the compacted seed (closes 0), dtypes, and both partitions' versions |

## Rulings and interpretations

- `-target` apply on the one function (TO-APPLY-34 step 3a).
- The CTO's "invoke for today's date" read as the scheduler's empty event (partition 2026-10-19).
- The tool takes `effective_to`, `is_current`, `absent_from_feed_since` from the LAST row of a run; the CTO confirmed (msg 110080).
- MSTR/site Z/dell1 CTO informed of the fresh xref partition (one relay request); CTO told at the close.

## Blockers

None.

## Compiler Tools

| tool | use | result |
|---|---|---|
| `comp-find` | locate the converter copies, the build script, precedent orders | PASS (a few rail denials on shell loops, rerun per RUN NEXT) |
| `python .tools/to-check.py --all --assignee` | lane encumbrance for `~NFRA2` | PASS (substring-matched other lanes; read the rows) |
| `.tools/to-pipeline-gate.py` (via safe-commit) | two new orders per issuance | PASS with notes (no PRD FWD for these orders, as for CT-cc-1 to CT-cf-1) |
| `.tools/wk-provision.sh` | two sparse worktrees | WARN: sparse sets missed `data/assets/scripts/lib`, the silver folder and the Lambda folder; I added them by hand |
| `.tools/safe-merge.sh` | two drains | PASS |

What worked: reading the served state myself after each lane report; a read-only probe on the real stored dim as the difference control. What failed: the worktree provisioning left out folders the converter imports (cost one worker round). Gap found: `wk-provision.sh` does not derive the sparse set from the order's `<paths>` plus import closure.

## Next Steps

1. `0.7.0_AE_CloudOps~NFRA2` has no open order: release the lane (`/mstr-kill`), since rule 34 seats one lane per macro.
2. [`1.0.0_SA_CTO`] NFRA_SCHWABBF's pending Terraform change in `opal-assets` belongs to its owner; nothing for this seat.
3. The scheduled fire of 2026-10-22 07:05Z is the next unattended proof; expect no growth beyond real changes.
