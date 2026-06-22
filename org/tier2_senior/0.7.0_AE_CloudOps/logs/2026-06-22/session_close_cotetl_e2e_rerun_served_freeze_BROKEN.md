# Session close -- COTETL e2e re-run: SERVED AUA freeze BROKEN (06-09->06-18, $373M->$395.3M), DS-confirmed

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, COORDINATE

Window: ~16:17Z (prior log) -> ~16:47Z + session-close handoff. Serial: 0.7.0_AE_CloudOps. TO: ADVI_COTETL.E2E-RERUN (the binding finish of the same-day P0).

## Current State (the binding finish + the day's handoff)

**COTETL served-AUA freeze BROKEN -- demonstrated on the served artifact + DS-independently-confirmed. CVO firm-AUA cert (criterion #5) pending; DS owns the fix-deploy ledger close (rides that cert).**

Re-run leg (this window):
- DS deployed the snapshot-perf wiring fix (commit 5c80bf6ca): C_03.account_performance (cot snapshot branch: total_aua=sum(canonical_holdings.market_value)) + C_01.canonical_nna (date-axis re-point). Firm-separated (49F/bd untouched).
- I PARITY-VERIFIED deployed code/gold C_03/C_01 == 5c80bf6ca (independent sha, NOT DS self-report). Re-ran full gold (opal-cot-gold-run 62baea04, Success).
- GROUND-TRUTHED the SERVED (Rule 22, never rc=0): platinum/firm clients-tab-slim + header_metrics data_as_of=2026-06-18; header total.aua=$395,300,238 (off the $373,157,665/06-09 freeze); account_performance max=06-18 CONTIGUOUS 04-22->06-18 (56 dates, 13231 rows); canonical/nna->06-18.
- Surfaced 2 anomalies (ground-truth, not gloss) -> DS dispositioned both as EXPECTED/pre-existing (NOT fix-defects): (1) nna qtd==ytd==12m=$391.18M = cot onboarding starts 04-22 so all windows = same period (AUA = NNA + ~$4M appreciation); (2) $395.30M-vs-$397.65M-raw-MV = pre-existing D_00 707->694 account filter (drops 13 unmapped), not the snapshot fix. fee-side (fee_count=0) filed to CVO/AP-gate, out-of-scope.
- DS independently re-confirmed the served (06-18/$395.30M/contiguous). DS owns the ledger close-leg (their 1630Z fix-deploy ledger) on CVO cert.

THE DAY'S HEADLINE: ground-truthing the SERVED artifact (not rc=0) caught a FALSE-SUCCESS on Rule 22's first opportunity (the e2e cascade was rc=0 across every stage but served firm-AUA never moved off 06-09) -> grounded the deeper lots-vs-snapshot wiring bug -> drove it through to a real demonstrated served advance. CTO/COO: "first real proof Rule 22 works."

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| (parity) | s3 cp code/gold C_03/C_01 vs git show 5c80bf6ca -- # rail-checked | PASS | deployed==DS-commit, independent (comp-pipescript cot-blind) |
| (SSM/aws) | opal-cot-gold-run 62baea04 + served head-object/parquet ground-truth | PASS | operational (Rule 21 free); the SERVED proof, not rc=0 |
| deploy_ledger.py | (e2e-run ledger closed prior; fix-deploy ledger is DS's) | n/a | DS owns the fix-deploy close-leg |

**What worked:** verify-on-SERVED carried from the false-success catch all the way through the fix -- re-run ground-truthed to 06-18/$395.3M/contiguous, never rc=0; surfaced 2 anomalies (both dispositioned expected) rather than glossing. Independent parity (deployed==commit) not DS self-report. **What failed:** nothing this window. **Gap:** comp-pipescript/comp-freshness cot-blind (rail-checked overrides logged repeatedly today -- a real cot-coverage gap for a future comp-tool).

## Blockers

None. COTETL served-AUA fix is demonstrated; FORMAL close pending CVO firm-AUA cert (criterion #5 served=06-18) -> DS close-legs their fix-deploy ledger on it. That's CVO+DS's lane.

## Next Steps

- **[3.0.0_SA_CVO]** firm-AUA cert (criterion #5 served=06-18/$395.3M; #3 canonical contiguous 04-22->06-18) + disposition the fee-side flag (fee_count=0). -> DS closes the ledger leg.
- **[0.7.0_AE_CloudOps] TOMORROW-AM:** verify DATEMODE-B/C nightly STUCK (served AUA advances PAST 06-18 on 06-23 nightly -- the daily-cadence verify) + A_00 forward-tripwire (A_00 rewrites after 06-23 lands a new bd txn file) -> RAVC COO.
- **[Andrew]** F-1 critical-surface email confirm click -> I verify Delivered>0 + ping AE0.6 (4 SS4c alarms).
- **[0.6.0_AE_PartnerETL]** watch-the-watcher critical-surfaces.yaml draft -> my review+commit.
- **[deferred, COO-allocate]** DEBTSCAN TO-D3 / TSGRAPH P2-2 / ETFS_SETUP.W1 (staged) -- resumable now that COTETL is resolved.

## Ops note

cot-exporter EC2 i-0643a5bee8a8feabf LEFT RUNNING (COO directive -- tomorrow's nightly needs it + tomorrow's served-advance is the DATEMODE-C daily-cadence verify that the fix STICKS). All today's cot writes were the sanctioned bronze-backfill + silver-reprocess + gold-runs via deployed code (no ad-hoc inline).
