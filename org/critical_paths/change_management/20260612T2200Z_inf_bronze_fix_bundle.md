# Deploy Completion Record
**Date opened:** 2026-06-12T22:00Z (push/deploy start of the BRONZE-FIX bundle)
**Date closed:** OPEN — phased close in the 2026-06-13 AM bundle window (COO-ACCEPTED phasing, RAVC3 213944Z: "textbook NO-HALF-DEPLOYS ... deferred to ONE ledgered bundle tomorrow AM")
**Deploy:** ADVI_INFETL.BRONZE-FIX #1 (dual-prefix collapse, ad1f03b7f) + #2 (_BRONZE_COMPLETE required-dim contract)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (2026-06-12 Andrew-direct NEVER rule)

---

## Why this entry is open by design

The inf-bronze-runner (i-083ad9ae297f88e9f) is STOPPED (start-on-demand); its
fetch script is bootstrap-baked on-instance (recovery follow-up (g)). The
runner-side legs can only land in the instance's natural up-window (~13:00Z
daily pull). Interim is PROVABLY safe: the runner's live source
(code/bronze-runner/orchestrator.py) is untouched tonight — tomorrow's 13:00Z
run executes today's proven orchestrator regardless of the legs below.
HARD INVARIANT until close: nobody refreshes code/bronze-runner/orchestrator.py.

## Legs

| leg | kind | state | evidence / close condition |
|---|---|---|---|
| #2 orchestrator + contract -> s3://opal-data-inf/code/bronze/ | s3-prefix | pending push (auto via safe-deploy pre-push hook) | comp-pipescript deployed --pipeline inf-bronze = all MATCH. INERT until fetch leg (runner reads bronze-runner/ till then) |
| fetch script -> s3://opal-data-inf/code/bronze-runner/inf-bronze-fetch.sh | s3-prefix | OPEN | upload + TOOL-03 [aux:bronze-runner] inf-bronze-fetch.sh MATCH (currently DRIFT = repo ahead, tool-watched) |
| on-instance /usr/local/bin/inf-bronze-fetch.sh refresh | ec2-baked-asset | OPEN | SSM cp from S3 + on-instance md5 == repo md5 (2026-06-13 ~13:05Z, mid-run window is safe — running procs hold their own copies) |
| code/bronze-runner/orchestrator.py DELETE (stale pipeline-code slot) | s3-delete | OPEN (COO-authorized conditional, RAVC3 213944Z) | gated on fetch-leg verify; per-object verify-before-delete |
| manual_api collision-safe consolidation (code/manual_api refresh + code/bronze twins, cross-prefix md5 pre-check) | s3-prefix | OPEN (Finding 2; DEBTSCAN 2a ledger files with the bundle) | TOOL-03 [aux:manual_api] 9 DRIFT -> 0; no basename-collision across the gold runner's 4 flat-synced prefixes |
| contract ACTIVATION (runner executes contract-enforcing orchestrator) | activation | OPEN | first post-bundle scheduled run's _BRONZE_COMPLETE.json carries the "contract" block (validate on the scheduled run, not a manufactured one) |

## Sequencing (tomorrow AM bundle, in order)
1. ~13:00Z instance self-starts for the daily pull (runs OLD fetch + OLD orchestrator — proven path, unaffected).
2. While up: SSM-refresh the baked fetch script; verify md5. Upload fetch script to code/bronze-runner/ (S3 leg).
3. Verify fetch-leg: TOOL-03 aux row MATCH.
4. Delete code/bronze-runner/orchestrator.py (verify-before-delete; COO conditional auth).
5. manual_api consolidation with cross-prefix collision pre-check.
6. Close this entry; activation leg closes on the next scheduled run's sentinel.
