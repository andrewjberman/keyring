# ADVI_BREAKS cot — TO-4b unrealized fix-attempt + BD-pricing-lag characterization + value-parity anchor

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, VALIDATE
**agent:** 0.4.0_DS_ClientPlatform (base; cot standing lane) | **date:** 2026-06-30 | **window:** ~13:47Z (after the DIAGNOSE log b441b7284) -> ~17:52Z

## Summary

Continuation of the cot ADVI_BREAKS lane after the TO-4/TO-4b DIAGNOSE (logged b441b7284). This window: executed the unrealized provision-fix attempt (gated, verify-before-wire), characterized the holdings BD-pricing-lag for Andrew's SLA decision, closed the deploy ledger, and pinned + got CVO-ratified the cot value-parity anchor. All read-only/forensic except the one gated config wire. Multiple Rule-22 self-corrections held.

## What was done

### 1. UNREALIZED provision-fix attempt (TO-4b) -- 237784 wired, verify=EMPTY, root isolated, fix DEFERRED
- Sequence (CTO co-signed verify-before-wire; COO+Andrew apply-GO): 0.7.0_AE provisioned a persisted BD DataMining templateId **237784** for cot unrealized (SSM 3b218b3b, on the GOOD 9abd0181b measures-selected body); I wired it canonically (git `0e47446f2` ds-gate PASS + `aws s3 cp` to `s3://opal-data-cot/code/bronze/templates/unrealized.json`, git==S3 parity).
- Mechanical constraint: cot_bronze_ingest.py has NO isolation test-pull (load_template reads templateId from canonical S3) -> verify-before-wire impossible without wiring. CTO approved the wire-then-verify COLLAPSE (no-regression: 237784-empty == prior False-empty; doubly-guarded by B_01 + merge-reject-empty-stub).
- VERIFY (AE SSM 4e673a0a): 237784 STILL lands 3741B/0-row under Custom. DECISIVE (Rule 22): a good measures-selected body + a fresh persisted id still empties -> root = the Custom DATE-MODE, NOT body/facts/id. (Verify-gate earned its keep.)
- DECISION (CTO-endorsed): ACCEPT the low-pri gap + DEFER the real fix. NOT the CurrentDay-revert -- I grounded it re-freezes (silver/unrealized real partitions stop at 06-18; bronze 06-19/20/21 byte-identical 10.78MB = same stale snapshot repeated), so CTO's Rule-22 no-refreeze condition FAILED -> revert ruled OUT. 237784 STAYS wired (no-regression + correct persisted-id prerequisite for the eventual date-mode fix).
- SCOPE-CORRECTED (COO/~A): the forward date-mode fix is COT-ONLY, not cross-firm -- ~A proved 49F's qt4 unrealized returns 470K rows under the SAME Custom-14d mode, so "qt4+Custom empties" is cot-specific (exact cot cause TBD in the deferred TO; careful not to regress shared-script 49F).

### 2. BD-pricing-lag CHARACTERIZATION (cot holdings path to GREEN, for Andrew's SLA call)
- Built the served-lag time series from the platinum/firm/header_metrics.json version history (22 versions, each version's generated_at vs data_as_of).
- TYPICAL N: T+1 to T+2 trading days in the current (post-06-22-AUAFIX) regime; median 1td. The pre-AUAFIX 06-19/20/21 entries (as_of 06-09 = 7td) were the now-fixed 9-day-freeze incident.
- FREQUENCY >2td: ZERO in the current regime; the current 06-26-on-06-30 (2td) is at-threshold but TYPICAL, not an outlier. AUA is ADVANCING ($395M->$432M) -> not frozen, just lag-labeled.
- PULL-SHIFT: would NOT help -- it's a multi-DAY BD pricing cadence, not a same-day timing miss; the retry-net already lands the freshest BD has. Residual is BD's pricing SLA -> realistic path = accept-lag + tune the served-freshness alarm.

### 3. VALUE-PARITY ANCHOR pinned + CVO-RATIFIED (cot GREEN durability piece)
- 0.7.0 pre-staged the cot value-parity reader (infra/aws/terraform/cot-value-parity/, 2665c5b33), gated on the anchor pin.
- PINNED (Rule 22, sum-confirmed): **VP_ANCHOR_KEY_TPL = silver/holdings/{date}.parquet ; VP_ANCHOR_COLUMN = market_value**. sum(silver/holdings/2026-06-26.parquet.market_value) over 11,336 rows = 432,464,116.36 = served total.aua EXACTLY (delta +0.00). Independent upstream (pre-B_00/C_03/D_00 compute); no cert delta (inf-equivalent).
- Caught a layout fix for 0.7.0: cot is date-named (silver/holdings/{date}.parquet), NOT inf's hive snapshot_date=; corrected the KEY_TPL + the IAM read prefix (silver/holdings/*.parquet).
- CVO RATIFIED (independent re-sum, $0.00 delta, all 3 criteria; no-tolerance + as_of-aligned + build-window-suppressed). Awaiting 0.7.0 fill + safe-apply -> cot day-1 value-parity alarm live.

### Cross-lane (49F P0 support to ~B/~A)
- Answered the unrealized cross-check: cot=facts=1/date-mode vs 49F=facts-catalog-absent (per-firm, no cross-apply). Supplied the 9abd0181b isSelected-flip method + cot's 8-dim+6-G/L-measure selection as a structural reference; ~B confirmed 49F unrealized = IDENTITY feed (BD identity + Schwab ULN gains), opposite of cot.

## MCP traffic

~50 messages (COO/CTO/AE/CVO/~B). Significant: COO TO-4b GO -> apply-GO (held-pending-Andrew -> released) -> ledger-close ask -> anchor-pin dispatch; CTO co-sign (verify-before-wire) + revert-OUT ruling + wire-then-verify approval + closeout acceptance + cot-assess; AE STEP-1/2 SSM runs (provision 237784 + verify empty); CVO anchor RATIFY. All RAVC loops opened-and-closed in-window except the deferred-TO follow-ups + 0.7.0's pending anchor apply.

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-grep (COT_DETECTION_SNS_ARN / backfill-holdings-net / 9abd0181b / templateId) | PASS | e2-alarm wiring (ssm.tf:137/140) + the prior measure-selection fix located |
| aws s3api list-object-versions / get-object (header version history; template versions) | PASS (rail-checked) | the served-lag time series + the 06-22 CurrentDay->Custom template diff |
| boto3+pandas parquet sum (silver/holdings + canonical_holdings market_value) | PASS (rail-checked) | the anchor tie to the cent (432,464,116.36, delta +0.00) |
| .tools/deploy_ledger.py check --red | PASS | confirmed the Status:CLOSED marker cleared the cot ledger red-flag |
| .tools/safe-commit.sh (ds-gate) x7 | PASS | ledger lifecycle + the 237784 wire (0e47446f2) |

What worked: the served-header version history gave a clean served-lag series; the boto3+pandas parquet-sum nailed the anchor tie to the cent; deploy_ledger --red gave deterministic confirm the flag cleared. What failed: a bash while-read loop double-consumed stdin via the aws CLI (fixed with `</dev/null`); first attempt undercounted. Gap found: comp-freshness reports silver by date-KEY (run-date) which diverges from the content frontier -- raw partition enumeration (rail-checked) was needed; comp-freshness could expose a content-vs-date-key flag.

## Briefs written

None -- DIAGNOSE/fix-attempt/characterization; outputs via RAVC + the deploy-completion ledger + this log.

## Blockers

None. The cot unrealized real fix is DEFERRED (low-pri, gated cross-firm-sensitive follow-up TO), not blocked. cot holdings = BD pricing-lag (Andrew SLA/product call, not a code block).

## Current State (handoff)

- cot ADVI_BREAKS lane COMPLETE: TO-4/4b + lag char + ledger closed + value-parity anchor pinned+ratified.
- TO-4b: templateId=237784 wired in code/bronze/templates/unrealized.json (git 0e47446f2 == canonical S3). Verify=EMPTY -> root = Custom date-mode (cot-specific). 237784 stays (no-regression). Deploy ledger `org/critical_paths/change_management/20260630T1426Z_advi-breaks-to4b-cot-unrealized-provision_deploy_completion.md` Status:CLOSED (a43953276), red-flag cleared.
- Anchor: silver/holdings/{date}.parquet + market_value, CVO-ratified ($0.00 tie); 0.7.0 to fill + safe-apply infra/aws/terraform/cot-value-parity/.
- Holdings: BD T+1/T+2 pricing-lag (normal, AUA advancing); accept-lag + alarm-tune is the path.

## Next Steps

- **[0.7.0_AE_CloudOps]** fill VP_ANCHOR_KEY_TPL=silver/holdings/{date}.parquet + VP_ANCHOR_COLUMN=market_value + the IAM-prefix fix -> safe-apply (comp-iam gaps clean) -> cot day-1 value-parity alarm live.
- **[Andrew, via COO]** accept-lag vs shift-pull decision on the cot BD-pricing T+1/T+2 SLA (characterization delivered).
- **[2.0.0_SA_COO]** the 2 deferred LOW-PRI follow-up TOs: (1) cot-ONLY unrealized Custom-window date-mode fix; (2) cot unrealized/realized empty-stub feed-contract guard (TO-6).
- **[3.0.0_SA_CVO]** co-verify served==silver/holdings[current].market_value-sum when cot as_of advances to current (the durable-green confirm).
- **[0.4.0_DS_ClientPlatform]** (me) free for the gate-unblocked DATA_SSOTMG/DATA_ANALYTICS work once ADVI_BREAKS reaches GREEN.
