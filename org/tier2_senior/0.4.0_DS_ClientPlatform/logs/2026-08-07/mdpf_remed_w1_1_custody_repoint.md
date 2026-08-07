# MDPF_REMED.W1-1 -- 49F custody repoint: two false premises, an atomic 4-file fix, and a deploy asymmetry that would have caused the real outage

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, DEPLOY

**Agent:** `0.4.0_DS_ClientPlatform` · **Window:** 2026-08-07 ~1928Z -> ~2115Z
**TO:** `MDPF_REMED.W1-1` @ef7b320786 · **Commit:** `f999fb25f6` (atomic, 4 files)
**Deliverable:** `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REMED_W1_1_CUSTODY_REPOINT_TIE_AND_QA_20260807.md`

---

## Summary

Dispatched twice (COO 192846Z, CTO 193650Z) to repoint the 49F custody leg off the DynamoDB table
Andrew deleted, framed as an urgent unattended-crash risk for the 09:00 fire. **Both framings were
wrong, and CTO asked me to check one of them explicitly.**

1. **No crash risk existed.** The DDB reader was dead code -- verified on the deployed artifact with
   a positive control. A bare `ddb.scan()` in unreachable code cannot fire. CTO stood the
   false-outage framing down to COO and Andrew, citing NEVER#1.
2. **The instruction as written would have MANUFACTURED the outage.** "Remove the constants" breaks
   three sites (`build_mdpf_spine.py:82`, `mdpf_gold_consolidator.py:183`,
   `route_bindings_tieout.py:146`) -- turning a dead-code cosmetic into a hard failure at the exact
   fire it was protecting.
3. **The real defect was a GREEN gate asserting a FALSE fact.** `route_bindings.yaml` declared
   ddb-cohort and the tie rows required the code constants to match it -- both sides agreed with
   each other and both disagreed with the code that ran. A gate comparing two things that agree
   with each other cannot detect the drift it exists to detect.

Landed atomically across 4 files. **Then the deploy layer produced the hazard the atomic commit was
meant to prevent** -- see below.

## THE DEPLOY ASYMMETRY (the most important thing in this window)

MSTR pushed at 20:28Z; the pre-push gate deployed **3 scripts** and flagged that the 4th file,
`route_bindings.yaml`, **is not a script and did not ride the script deploy leg.** That flag was
load-bearing. Measured immediately: the S3 copy was dated 2026-08-04 and still declared
`{type: ddb-cohort, table: "opal-assets-daily-aua"}`. The EC2 runner syncs that config from S3
(`mdpf-daily-dispatch.sh:130`) and the spine refuses without it (`:136`) -- so **new code was
deployed against old bindings**, and the repointed C-1 assertion would have raised
`SystemExit("BINDINGS STALE")` at the 09:00 fire.

Closed by uploading the config with the pre-state ETag pinned and verifying byte-identical on a
fresh non-empty retrieval. **AN ATOMIC COMMIT IS NOT AN ATOMIC DEPLOY** -- that is the transferable
lesson, and it was caught by MSTR's flag, not by my own plan.

## Evidence

- **Tie re-derived at my own seat** (COO criterion 2 -- did not take their figures): positive limb
  `SUM(net_mv_plus_cash)` exact <1c on **9 of 9**; negative control `SUM(net_mv_positions)` exact on
  **0 of 9**, missing $24,768,500.61-$32,146,081.74. Bound held: 9 post-7/23 dates only, pre-7/23
  UNTESTED.
- **Tie-out validator:** 34 rows, 34 TIE / 0 FAIL.
- **Both gates mutation-tested:** PASS on real bindings; FIRED on all 3 mutations (prefix/fact/field).
- **Honest-absent contract:** absent dates NAMED in `__missing__`, 0 zeroed, 0 carried.
- **Ad-hoc QA run** on deployed bytes + deployed bindings, runner-mirroring layout: bindings
  asserted current, 440/440 custody dates, cross-axis gate PASS.
- **QA delta vs served: 0 differing dates of 439 overlapping.** Comparator negative-controlled
  (+$1.00 injection detected). ZERO CHANGE -- a true no-op, confirmed by running it.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | `dim_mdpf_aggregate_aua_timeseries.py --pipeline mdpf` | PASS | Resolved this time (contrast the Cottonwood file, which is unroutable under mdpf). 5 monolith silver reads incl. `fact_rps_s2`. |
| `comp-find` | `custody_leg --band CONFIG` | PASS | Located `route_bindings.yaml:57,96` -- the config coupling the dispatch never mentioned. |
| `comp-find` | `--name "*bindings*"` | PASS | Found `route_bindings_tieout.py`, the third break site. |
| `commit-gate.sh` | 3 py files | PASS | py_compile + ds-precommit + ruff clean. |
| `safe-deploy.sh` | 3 gold scripts | PASS | DEPLOYED + `comp-pipescript deployed` VERIFY OK x3. ⚠ attributed "authored by unknown" despite `--author` -- cosmetic, flagged. |
| `route_bindings_tieout.py` | full run | PASS | 34/34 TIE, 0 FAIL, denominator printed. |
| `comp-pulse` (risk-reflex) | pre-commit, auto | CLEAN | 4 files vs 1,659 danger nodes. |
| raw `aws` (operational) | `s3 cp/ls/head-object`, `events list-rules` | PASS | Deploy + verify + schedule census. Materialised 139 rules client-side rather than trusting a per-page `--query`. |

**What worked:** `comp-find --band CONFIG` is what surfaced `route_bindings.yaml` as a coupled
resource. Neither dispatch mentioned it, and it turned out to be the file that mattered most.

**What failed:** nothing blocked. `safe-deploy` mis-attributes the author as "unknown" when
`--author` is passed for `data/mdpf/**` (worked for `data/assets/**` earlier in the session).

**Gap found:** `safe-deploy`'s PIPELINE_MAP covers `scripts/{gold,silver,bronze}/*.py` only, so a
**declared config file that deploys to `code/config/` has no gate leg** -- despite
`mdpf-daily-dispatch.sh:129` stating "Declared config syncs like code, same law." The law says it;
the tooling does not enforce it. That gap is what nearly landed a half-deploy tonight. Routed.

## My own errors, recorded

1. **My negative control on the deployed bytes returned `ddb.scan` = 1 and I nearly read it as a live
   call.** It was my own removal-note comment containing the literal string. Re-checked with the
   line context and a non-comment-line filter -- zero live references. A count without its frame,
   in the exact session I have been flagging that class in others.
2. First QA attempt used a scratch layout that did not mirror the runner (`../../config` resolved
   outside my tree). Fixed by mirroring `scripts/gold/` + `../../config/` rather than by patching
   the path -- the point of running deployed bytes is to run them as deployed.

## Blockers

**None.** TO deliverables met. Two residuals surfaced, neither blocking and neither mine:

- **The Lambda package is NOT re-cut — RESOLVED ~2150Z, and it is NOT a failure.** MSTR confirmed
  `scheduled-floor.tf:128` `cron(0 9 * * ? *)` America/New_York targets `aws_lambda_function.mdpf_gold`
  — **the 09:00 fire IS the Lambda; the EC2 runner I QA'd is NOT the 09:00 path** — and escalated it
  to CTO as a hard fail landing on `build_mdpf_spine.py:92`. I then opened the deployed package
  (`LastModified 2026-08-07T03:51:21Z`, sha `XuLlClWT6kr...`, 648,182B) and measured all three legs:
  bindings **OLD** (`ddb-cohort`), spine asserts **OLD** (`spine.DDB_AUA_TABLE`), aua defines
  `DDB_AUA_TABLE` **OLD**. **All OLD => internally coherent => the C-1 assertion PASSES.** The
  described failure needs NEW code against OLD bindings, which is structurally impossible in a
  self-contained package (16 modules + trading_calendar + 3 configs at zip root, no runtime S3 code
  pull) that was never re-cut. **Correct characterisation: stale-artifact hygiene** — the fix is not
  live on the 09:00 path until a re-cut (TF-only, CTO lane, no night action); functional risk zero
  twice over (coherent, and the delta is $0.00 anyway). Corrections sent to MSTR + CTO 2150/2152Z.
  ⚠ NOT CLAIMED: package contents + coherence verified; the invocation was NOT traced in-process,
  and the conclusion does not require it.
  **This would have been the FOURTH false-outage-shaped claim in this TO's lifecycle, three sharing
  one missing step: "a deleted table is referenced somewhere, therefore something crashes," without
  asking whether the referencing code is REACHABLE or whether its counterpart moved WITH it.**
- **`trading_calendar.py` is absent from `code/scripts/gold/`** (only the retired
  `_trading_day_calendar.py` shim). My QA needed the repo root on PYTHONPATH. Whether the runner
  provisions it another way is UNVERIFIED -- flagged, **not** called a break.

## Current State (zero-prior-context handoff)

- **`f999fb25f6` on CLOUD, PUSHED** by MSTR at 20:28Z (range 22208eb2c9 -> d40a12194e). origin/CLOUD
  0/0 -- nothing of mine stranded local.
- **Deployed + verified byte-identical (sha256, non-empty retrievals):**
  `s3://opal-data-mdpf/code/scripts/gold/{dim_mdpf_aggregate_aua_timeseries,build_mdpf_spine,mdpf_gold_consolidator}.py`
  and `s3://opal-data-mdpf/code/config/route_bindings.yaml` (13,516B, sha256 `98f5e9c5...`;
  pre-state ETag `56a03a14...`, key-exists update, not a first-mint).
- **49F custody basis is now declared and asserted as** `s3-monolith-silver` /
  `schwab/08242234/silver` / `fact_rps_s2` / `net_mv_plus_cash`.
- **Expected at the next fire: NO CHANGE to any served 49F custody value** (0 of 439 dates differ).
- **Banked, not chased** (per the make-a-plan-then-review rule): no EventBridge rule schedules the
  MDPF path -- 139 rules materialised client-side, and `mdpf-daily-refresh-trigger` carries
  `ScheduleExpression: None`. Consistent with an EC2-side cron, which is the path I verified.
  **NOT calling the schedule missing** -- a schedule can live outside AWS entirely.

## Next Steps

1. **[1.0.0_SA_CTO / 0.7.0_AE_CloudOps]** Decide whether `mdpf-gold-lambda` needs a re-cut package
   (it embeds the old `route_bindings.yaml` + its sha256). Terraform-only lane.
2. **[2.0.0_SA_COO]** The `safe-deploy` gap: declared config files that deploy to `code/config/`
   have no gate leg, despite the dispatch script asserting they "sync like code, same law."
3. **[2.0.0_SA_COO]** Adjudicate `MDPF_REMED.W1-1` closure -- all criteria met and evidenced.
