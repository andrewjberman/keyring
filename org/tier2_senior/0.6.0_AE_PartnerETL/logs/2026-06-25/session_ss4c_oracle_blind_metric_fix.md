# Session Log — 0.6.0_AE_PartnerETL — SS4c oracle "built but blind" root-cause + IAM fix

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, COORDINATE
**Date:** 2026-06-25 (~1657–1711Z)
**Project:** ADHC_GLDINC.SS4c.ae-periodic-oracle-revalidation (TO pending)
**Driver:** 2.0.0_SA_COO (GO'd the build). CVO = spec author (cvo_1330Z). DS = gold-lib + gold-script deploy lane.

## Summary

COO GO'd the SS4c TIER-2 weekly-oracle build (BD interrupt cleared). Grounding found
the oracle is NOT unbuilt — it's **built + deployed + wired + running but BLIND**: it
emits no metric, so the alarm layer is dead (the silent-verifier class cvo_1330Z warns
about, one level up). Root-caused both breaks, fixed the IAM half (mine), handed the
script half to DS, and corrected COO's "build it" framing.

## Grounded state (not self-report)
- `gldinc_ss4c_weekly.py` deployed to `opal-data-bd/code/gold/` (06-22); Wed leg wired into
  `gold_dispatch.sh:1349-69` ("CloudOps RAVC1-confirmed placement"); TIER-2 alarms exist;
  TIER-1 daily canary live (`gldinc-ss4c-canary`). HAS run — parity scorecards at
  `gold/_parity/load_flows/ss4c/{06-23,06-24}/`.
- BUT `WeeklyScorecardClean` = **0 datapoints / 30d** → `ss4c-weekly-absence` alarm firing
  on a working verifier.

## Two root breaks (both block the emit)
1. **IAM (FIXED + APPLIED, commit `3ad886929`):** `bd-exporter-ec2-role` (the gold runner)
   had **no `cloudwatch:PutMetricData` at all** → the emit to `GLDINC/SS4c` AccessDenied'd
   (also silently ate the `gold_dispatch` `BD/GoldRunner` ShutdownDeferred emit via `|| true`).
   Granted ns-scoped (`GLDINC/SS4c` + `BD/GoldRunner`). comp-iam: no GLDINC gap. The "SS4c
   IAM fast-follow" from my prior log.
2. **`_emit` `float(None)` crash (authored; handed to DS — Rule 13/owned-paths gold-script
   lane):** `compute_scorecard` leaves `max_abs_diff/key_set_symmetric_diff/row_count_delta`
   = None on a clean DELTA=0 run (06-24 scorecard: `targets_met=True`, those 3 = None);
   `float(scorecard.get("max_abs_diff", 0.0))` → key present-but-None → `float(None)`
   TypeError → `_emit` crashes after `_write_parity` → parity records, no metric. Fix:
   None-safe `_num()` + non-fatal `_emit` + load-bearing-flag-first. Unit-verified
   (clean None-field scorecard → `WeeklyScorecardClean=1.0` lands). Patch handed to DS:
   `org/tier2_senior/0.6.0_AE_PartnerETL/handoffs/ss4c_emit_fix_for_DS.patch`.

## Cost-gate correction (resolved COO's hold)
NOT the cost-gated part. The cost gate was the runner COMPUTE-FOOTPRINT (the Wed full_scan
on the c6i) — placement was already CloudOps-signed 06-22 and running. My fixes change ZERO
compute; they just let the running oracle's metric LAND. No new NFRA_COSTAWS sign needed.

## Lane handling
The owned-paths gate correctly blocked my commit of `gldinc_ss4c_weekly.py` (POD4/DS lane).
Committed the IAM (`iam.tf`, AE lane) alone; routed the `_emit` fix to DS as a patch
(commit-through-owner, LD-0193). (Git footnote: the first patch-capture was empty because the
edit was staged from the blocked commit — re-cut from `git diff --cached`, working tree clean.)

## Current State / Next Steps
- **[0.4.0_DS_ClientPlatform]** `git apply` the patch → ds-commit-gate → commit (DS author) →
  deploy to `opal-data-bd/code/gold/`. No re-run (NFRA_COSTAWS); metric lands the next
  WEDNESDAY nightly (07-01) — IAM half already live → absence alarm clears then.
- **[2.0.0_SA_COO]** sequence watch-the-watcher (TO §4c #2): register `ss4c-weekly-absence`
  subscriber-presence into `comp-surface-check`/D8 critical-surface registry (NOT there —
  checked). I offered to author the limb (through 0.7.0/base-AE owner per LD-0193).
- **[CloudOps/CTO]** cost-model line (TO #3): NFRA_COSTAWS §7 permanent-recurring.

## Blockers
None. SS4c core is one DS-deploy from done; watch-the-watcher + cost-line are coordination items.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-iam gaps` | confirm the GLDINC/SS4c PutMetricData gap + post-fix | gap → granted; no GLDINC gap after |
| `comp-glob` | locate `cvo_1330Z`, `gldinc_ss4c_weekly.py`, `nna_flows`, `gold_dispatch` | found |
| `ds-commit-gate` | the gold-script edit (pre-handoff) | clean |
| Read (cvo_1330Z + gold_dispatch + nna_flows + iam.tf) | ground the §4c spec + the wiring + the IAM gap | grounded both root breaks |

Rail note: several `aws s3 ls`/`cloudwatch get-metric-statistics`/iam.tf-grep diagnostic calls
carried inline `# rail-checked:` markers (deployed-existence + metric-datapoint-count + IAM
role-block reads that comp-iam/comp-pipescript don't enumerate for this oracle).
