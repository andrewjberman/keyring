# Session 2026-06-22 ~1356-1421Z (cont.) — DATEMODE-A deploy + SS4c .py leg — 0.4.0_DS_ClientPlatform

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, COORDINATE

## Window
Execution follow-on to the morning's diagnosis log (session_cotetl_chainfix_catch_and_nna_to1_reverify.md).
The COTETL L2 ruling landed (CTO confirmed my CurrentDay-mislabel hypothesis) -> I executed the real fix.

## THREAD 1 — ADVI_COTETL.AUAFIX-DATEMODE-A — DEPLOYED + ACCEPTED (deploy leg)
The real COTETL fix (consolidated-merge CHAINFIX officially RETIRED). CTO L2 (135603Z): holdings/alloc/
unrealized BD exports use dateRangeType=CurrentDay, which mis-stamps LIVE data with a stale early-June
asOfDate (AE probe: BD HAS date-distinct data thru 06/18). P0 = ~$24M/6.5% served-AUA understatement.

Coordinated the fix contract with AE 0.7 + CTO (both legs needed: TABLE_DATE_MODE drives _window_for's
start/end; the STORED template JSON's dateRangeType is what load_template/run_query read). Two DS catches
folded into the contract as BINDING RAVC-checks: (1) Custom-14 not Custom-3 — a 3d lookback over the
Juneteenth weekend yields [06-19,06-22] which MISSES the last complete biz day 06-18 (verified); 14d
always contains it; (2) the 3 template JSONs are REPO files -> AE's edit must be repo+deploy, not
S3-direct (else next-deploy reverts). COO cleared the atomic option-b (DS commits code+templates in one
push, supersedes the TO's AE-first since both half-states are broken).

THE EDIT (commit **a7a4d974c**, atomic, deployed + MATCH-verified all 4):
- cot_bronze_ingest.py TABLE_DATE_MODE: holdings/allocations/unrealized ("CurrentDay",0) -> ("Custom",14)
  [14 = holiday-gap FLOOR reaching last-complete-biz-day, NOT a restatement lookback]; comment block
  rewritten (removed the buggy "CurrentDay auto-rolls so BD ignores start/end" assumption).
- templates/{holdings,allocations,unrealized}.json: "dateRangeType":"CurrentDay" -> "Custom" (in-place,
  templateIds preserved 226355/226334/False; surgical 1-line each, valid JSON).
- Deploy: safe-deploy auto-deployed the .py on push ([cot] gate PASS); DS aws s3 cp the 3 JSONs (the
  repo->S3 leg safe-deploy skips for non-.py). All 4 local md5 == S3 etag; read-back confirms S3
  dateRangeType=Custom.
COO ACCEPTED the deploy leg (141734Z, both binding checks PASS; no change_management ledger needed —
atomic-complete in-session, not a stranding cutover). BINDING VERIFY rides the next nightly: served cot
firm-AUA data_as_of past 06-09 + total_aua ~$397.7M. AE 0.7 fires the per-day backfill (06-10..06-18);
I confirm silver/holdings gains partitions >06-09.

## THREAD 2 — ADHC_GLDINC.SS4c TIER-2 .py leg — COMMITTED + DEPLOYED (commit-through-owner)
AE 0.6 requested Rule-13 commit-through-owner of 2 reviewed files (gldinc_ss4c_weekly.py + gold_dispatch.sh
Wed-leg). I re-verified before committing (not rubber-stamp): pure-swap correct (:108
SERVED=load_flows_from_transactions_windowed(read_load_flows_watermark())[0]), ds-commit-gate clean,
gold_dispatch.sh diff = only the SS4c Wed-leg (22 lines, bash -n clean).
- LANE CATCH: the combined commit was BLOCKED by the owned-paths guard — gold_dispatch.sh is the
  CLOUD_OPS_OR_ETL (AE) lane (.owned-paths.yaml:844), NOT DS. AE's "commit both" request crossed a lane
  boundary. Correct enforcement. Recovery: safe-commit force-staged both before the hook aborted ->
  git restore --staged both (non-destructive, no HEAD move) -> committed the gold .py ALONE.
- gldinc_ss4c_weekly.py committed **8f7de75d1** + DEPLOYED to s3://opal-data-bd/code/gold/ (safe-deploy
  [bd] gate PASS). gold_dispatch.sh left modified in the shared tree for AE to commit (his lane); surfaced
  to AE. 2-commit split is fine — leg dormant until 06-24 Wed, .py deployed-but-uninvoked is harmless.

## Files Modified
- data/cot/scripts/bronze/cot_bronze_ingest.py + templates/{holdings,allocations,unrealized}.json (a7a4d974c)
- data/black_diamond/scripts/gold/gldinc_ss4c_weekly.py (8f7de75d1)
- (gold_dispatch.sh = AE lane, NOT committed by me — handed to AE)
- this log

## Compiler Tools
| Tool | Where | Result |
|---|---|---|
| comp-which | rail routing (earlier session) | used |
| ds-commit-gate.sh | cot_bronze_ingest.py + gldinc_ss4c_weekly.py | PASS both (py_compile+AST+ruff py39+FA) |
| comp-pipescript io | gldinc_ss4c_weekly | Unknown (new auxiliary parity script, not numbered producer — accounted, not miscounted clean) |
| comp-pipescript deployed | cot_bronze_ingest (intended phase-3) | cot silent-Unknown (banked) -> substituted md5/etag MATCH on all 4 |
| safe-deploy (pre-push hook) | cot .py + bd .py | DEPLOYED + gate PASS both pushes |
| owned-paths guard | gold_dispatch.sh commit attempt | BLOCKED (correct — AE lane); recovered via restore --staged |

- **What worked:** the atomic code+templates push (zero half-state); md5/etag MATCH as the deploy-verify
  when comp-pipescript can't see cot; the Juneteenth-edge window check; surfacing the lane-cross instead
  of force-committing AE's file.
- **What failed/banked:** comp-pipescript io/deployed don't cover cot bronze OR new auxiliary bd scripts
  (Unknown); python-subprocess can't launch the Windows `aws` launcher (md5-verify rewritten to Bash-aws +
  inline-python-md5); the combined SS4c commit hit the owned-paths AE lane.
- **Gap:** an owned-paths-aware pre-check (warn at TO-authoring that gold_dispatch.sh is cross-lane) would
  have pre-split the SS4c commit; AE's commit-through-owner ask should have scoped only the gold .py.

## Blockers
None. DATEMODE-A deploy ACCEPTED, binding verify event-gated on the next nightly + AE backfill. SS4c .py
deployed; gold_dispatch.sh pending AE's own-lane commit (before 06-24 Wed).

## Next Steps
1. **[self, event-driven]** On AE's DATEMODE backfill-landed ping: confirm silver/holdings gains partitions
   >06-09. On the next nightly: verify served cot firm-AUA past 06-09 + ~$397.7M -> RAVC COO (final project-accept).
2. **[0.6.0_AE]** commit the gold_dispatch.sh SS4c Wed-leg (AE lane) before 06-24 Wed; I pair-verify the
   first Wed run's WeeklyScorecardClean + gold/_parity/load_flows/ss4c/.
3. **[2.0.0_SA_COO]** P2 donut-migration TO (retire FE override, data-layer) — self + AE lane, when authored.
