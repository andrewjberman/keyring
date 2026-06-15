# Deploy Completion Record
**Date opened:** 2026-06-12T22:00Z (push/deploy start of the BRONZE-FIX bundle)
**Date closed:** 2026-06-15T19:20Z — **CLOSED: RECONCILED-NOT-APPLIED, 0-data-harm** (COO disposition 191820Z, AE reconcile; CC CTO). Originally phased for the 2026-06-13 AM window (COO-ACCEPTED phasing, RAVC3 213944Z); that window was not executed (bd-pipeline priorities), the improvement legs were never applied, and 2026-06-15 ground-truth confirms the served state stayed SAFE on the proven path. See **## CLOSE** below.
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
| #2 orchestrator + contract -> s3://opal-data-inf/code/bronze/ | s3-prefix | CLOSED 2026-06-12T21:58Z (push 5ba07e0b6, safe-deploy PASS) | `[BRONZE] orchestrator.py MATCH` + `[BRONZE] bronze_required_dims.py MATCH` (inf-bronze 4/4 MATCH); bronze-runner/orchestrator.py untouched (16:49 R1 timestamp) -- INERT until fetch leg |
| fetch script -> s3://opal-data-inf/code/bronze-runner/inf-bronze-fetch.sh | s3-prefix | OPEN | upload + TOOL-03 [aux:bronze-runner] inf-bronze-fetch.sh MATCH (currently DRIFT = repo ahead, tool-watched) |
| on-instance /usr/local/bin/inf-bronze-fetch.sh refresh | ec2-baked-asset | OPEN | SSM cp from S3 + on-instance md5 == repo md5 (2026-06-13 ~13:05Z, mid-run window is safe — running procs hold their own copies) |
| code/bronze-runner/orchestrator.py DELETE (stale pipeline-code slot) | s3-delete | OPEN (COO-authorized conditional, RAVC3 213944Z) | gated on fetch-leg verify; per-object verify-before-delete |
| manual_api collision-safe consolidation (code/manual_api refresh + code/bronze twins, cross-prefix md5 pre-check) | s3-prefix | OPEN (Finding 2; DEBTSCAN 2a ledger files with the bundle) | TOOL-03 [aux:manual_api] 9 DRIFT -> 0; no basename-collision across the gold runner's 4 flat-synced prefixes |
| contract ACTIVATION (runner executes contract-enforcing orchestrator) | activation | OPEN | first post-bundle scheduled run's _BRONZE_COMPLETE.json carries the "contract" block (validate on the scheduled run, not a manufactured one) |
| BRONZE-FIX #9 AC5 concurrency-aware self-shutdown (folded into the fetch-script legs by AE 0.7 handoff 220430Z -- same baked asset, no double-deploy) | rides fetch-script legs | OPEN | ShutdownArmed/ShutdownDeferred CW metrics present in the next run's log; bronze-runner keeps its watchdog timer (deferral safe; gold-runner asymmetry = #9-F1, AE 0.7 lane) |

## Sequencing (tomorrow AM bundle, in order)
1. ~13:00Z instance self-starts for the daily pull (runs OLD fetch + OLD orchestrator — proven path, unaffected).
2. While up: SSM-refresh the baked fetch script; verify md5. Upload fetch script to code/bronze-runner/ (S3 leg).
3. Verify fetch-leg: TOOL-03 aux row MATCH.
4. Delete code/bronze-runner/orchestrator.py (verify-before-delete; COO conditional auth).
5. manual_api consolidation with cross-prefix collision pre-check.
6. Close this entry; activation leg closes on the next scheduled run's sentinel.

---

## CLOSE — 2026-06-15T19:20Z — RECONCILED-NOT-APPLIED, 0-DATA-HARM

**Disposition:** COO 191820Z (CC CTO) — close as RECONCILED-NOT-APPLIED rather than leave park-open.
This is a **process-debt strand (un-started improvement bundle), NOT a half-landed served-state strand**.
The NEVER-law's target is a CONFIRMED deploy left half-landed + invisible; here the served state is SAFE
and the improvement legs were simply never applied (effectively an abandoned deploy *attempt*, not a
stranded leg), now made VISIBLE via this reconcile.

**Ground-truth reconcile evidence (AE, read-only, 2026-06-15):**
- SERVED STATE SAFE + FRESH: `s3://opal-data-inf/bronze/orion-api/{2026-06-13,-06-14,-06-15}/_BRONZE_COMPLETE.json`
  all present, `overall:success`, full dim coverage (06-15: 8 dims, 0 real fail, 1 expected_fail=assets
  py3.10-dep, 1 skip=geo). Runner executed the proven 06-12 orchestrator on the old path = the ledger's
  designed HARD INVARIANT (leg-1 inert + safe). Zero data harm across the 3-day window.
- IMPROVEMENT LEGS NEVER APPLIED (all consistent): fetch-script S3 = repo md5 `de2addad…` != S3 ETag
  `70d6fdc4…` (S3 still the 06-12 copy); `code/bronze-runner/orchestrator.py` still present (delete leg
  never ran, correctly gated on the un-landed fetch leg); contract ACTIVATION confirmed inactive (no
  `contract` block in the 06-15 `_BRONZE_COMPLETE.json` — consistent with the orchestrator not being
  updated). manual_api consolidation likewise not applied.
- AUTOMATED RED-GATE STATUS: `deploy_ledger.py check --red` = **already GREEN** ("OK: no open deploy
  ledgers"). This entry is a *hand-authored* change_management `.md`; it was NOT opened via
  `deploy_ledger.py open`, so there is **no `org/critical_paths/.open_deploys/<slug>.json` sentinel**
  backing it. The tool's `--red` gate scans only `STATE_DIR.glob("*.json")` sentinels, so it never saw
  this `.md`. The close is therefore for **doctrine + human-visibility** (an open-looking `.md` reads as a
  silent strand), not to clear a firing automated gate. (Premise-correction surfaced to COO 192xZ.)

**Leg final states:** all OPEN legs (fetch-script S3, on-instance refresh, orchestrator delete, manual_api
consolidation, contract activation, #9 AC5 self-shutdown) = **NOT-APPLIED**. Leg #2 (`code/bronze/`
orchestrator+contract upload) remains CLOSED-as-deployed-inert per the original table (the canonical
pipeline-code prefix carries the improvement, but the runner does not fetch from it until the
un-applied fetch leg lands — so it is inert/harmless).

## FORWARD WORK (tracked — critical-paths forward-line)

**inf-bronze improvement-bundle RE-DRIVE — DEFERRED, 0-harm reconciled 06-15.** A *future* deploy (gets its
OWN new `deploy_ledger.py open` ledger when executed). Scope to re-drive in a deliberate inf window when
the bd-TRIO frees: (1) fetch-script S3 sync `infra/aws/ec2/inf-bronze-runner/inf-bronze-fetch.sh` ->
`s3://opal-data-inf/code/bronze-runner/` (carries #1 dual-prefix collapse + #9 AC5 self-shutdown);
(2) on-instance `/usr/local/bin/inf-bronze-fetch.sh` SSM refresh + md5 verify (instance up-window);
(3) conditional `code/bronze-runner/orchestrator.py` delete (verify-before-delete, COO conditional auth);
(4) manual_api collision-safe consolidation (cross-prefix md5 pre-check); (5) contract ACTIVATION (validate
on the next scheduled run's `_BRONZE_COMPLETE.json` carrying the `contract` block). Owner: 0.6.0_AE_PartnerETL.
Repo commits already landed (ad1f03b7f #1, 82b8d4190 #2, 5afbcaad5 #9) — only the runner-side application is
deferred. (Registry mirror offered to COO; this forward-line is the canonical record until then.)
