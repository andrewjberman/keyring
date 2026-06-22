# 0.6.0_AE_PartnerETL -- 06-22 Schwab June ingest + /49-schwab-conv skill + SS4c TIER-2 deploy-close
**archetype:** MIXED
**secondary_archetypes:** DEPLOY (Schwab ingest + gold_dispatch deploy), SCRIBE (skill)

## Window
06-22 ~1420Z-1432Z, since session_ss4c_tier1_canary_deploy (9ac0b52d7). Three Andrew-direct items:
(1) Schwab June data upload+conversion, (2) create /49-schwab-conv skill, + (3) SS4c TIER-2 deploy-close.

## 1. Schwab 49F ingest (Andrew-direct) -- COMPLETE through 20260618
Protocol = prompt.md sec Schwab Ingest (6 steps). Account 08242234.
- Step 1 (sync OneDrive->S3): dry-run first (--since 20260605 -> 81 missing in 01_raw/, 7 in bronze/rps/),
  then --upload (background): 81 raw -> s3://opal-data-schwab/01_raw/ + 7 *.RPS -> bronze/rps/.
- Steps 2-6 (5 silver converters, background): ACC/RPS/TRN/ULN/RLD all OK=7 ERR=0 through 20260618.
  New dates: 20260610,0611,0612,0615,0616,0617,0618 (0605/08/09 already present from a prior ingest --
  the converters' "To convert: 7" is the authoritative delta, not the calendar span). Counts at 0618:
  ACC 7,039 | RPS 91,972 | TRN 28,091 | ULN 251,417 | RLD 996 (1 benign SKIP 20250109 no-DL). RLD present
  (B_02 primary). Dest s3://opal-data-bd/schwab/silver/{acc,rps,trn,uln,rld}/date=YYYYMMDD/data.parquet.
- Step 7 (verify): comp-freshness artifact on all 5 20260618 partitions -> STATUS PASS each (written 14:25-14:29Z).
- Step 8 (notify): Andrew direct (in-session) + DS (reconciliation, 143237Z) + MSTR (143241Z).

## 2. /49-schwab-conv skill (Andrew-direct) -- CREATED
.claude/skills/49-schwab-conv/SKILL.md (commit c8d9ff932). Memorializes the 6-step ingest as an
executable runbook: fixed facts table (source/dest/account/SSE), Step 0 AE-only gate + scope, Step 1
dry-run-then-upload(background), Steps 2-6 the 5 converters (RLD non-optional callout), Step 7
comp-freshness verify, Step 8 notify. Folds the banked gotchas (opal-data-schwab AES256-SSE deny = why
AE-owned not DS; ACC triple-state header; idempotency; partial-prior-ingest delta). Registered + visible.

## 3. SS4c TIER-2 deploy-close (continuation)
DS RAVC2 (142103Z): DS committed the gold .py (gldinc_ss4c_weekly.py 8f7de75d1, safe-deploy PASS) but
owned-paths BLOCKED DS on gold_dispatch.sh (AE CLOUD_OPS_OR_ETL lane, .owned-paths.yaml:844) -- correct
lane bounce (I had over-bundled). I committed the .sh Wed-leg (4edf917c7) + DEPLOYED via aws s3 cp to
s3://opal-data-bd/code/gold/gold_dispatch.sh (safe-deploy skips .sh -> manual cp, the AE dispatcher-deploy
path). VERIFIED: deployed copy byte-IDENTICAL to local HEAD; delta-vs-prior-deployed = ONLY my leg. Both
TIER-2 legs now on the runner for the 06-24 Wed run. RAVC closed to DS (142705Z, CC COO).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-freshness artifact (x5) | verify each 20260618 schwab silver partition (Step 7) | PASS all 5 |
| comp-which | route the silver-partition verify (rail Rule 21; gated my aws s3 ls) | -> comp-freshness artifact s3://... |
What worked: the comp-rail gate correctly redirected my `aws s3 ls` freshness eyeball to comp-freshness
(richer EXISTS/age/PASS). The Schwab converters' own OK=N + row counts cross-checked the comp-freshness PASS.
What failed: none. Gap: comp-freshness `artifact <s3-uri>` mode isn't surfaced by comp-which's top routing
(found it via the comp-grep fallback hit on .tools/comp-freshness:790) -- minor discoverability note.

## MCP traffic
~5 significant. IN: DS RAVC2 (TIER-2 .py deployed + .sh lane-bounce). OUT: DS RAVC-close (.sh deployed +
validated .py); DS + MSTR Schwab-complete notifications. (Re-surfaced/handled broadcasts not re-counted.)

## Blockers
None. All three items complete. TIER-2 weekly oracle dormant until the 06-24 Wed run (CVO synthetic +
DS/me pair-verify then). Schwab silver through 20260618 available for DS reconciliation.

## Current State / Next Steps
- Schwab: 5 silver tables through 20260618 (comp-freshness PASS). /49-schwab-conv skill live for next time.
- SS4c TIER-2: both legs deployed to the runner; first WeeklyScorecardClean datapoint expected 06-24.
- [0.4.0_DS_ClientPlatform] BD<->Schwab reconciliation on the new partitions; pair-verify 06-24 weekly scorecard.
- [3.0.0_SA_CVO] gate-3 synthetic divergence/absence test post-06-24.
- [0.6.0_AE_PartnerETL] 06-24: pair-verify the first SS4c weekly run (GLDINC/SS4c WeeklyScorecardClean + gold/_parity/load_flows/ss4c/).
