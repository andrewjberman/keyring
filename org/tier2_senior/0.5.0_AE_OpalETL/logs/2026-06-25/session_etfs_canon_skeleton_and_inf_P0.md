# Session Log -- 0.5.0_AE_OpalETL -- ETFS_CANON skeleton + inf-canonical P0 + m365 gateway help

**archetype:** MIXED (DEPLOY + DIAGNOSE + IMPLEMENT)
**secondary_archetypes:** COORDINATE
**Date:** 2026-06-25 | **Window:** ~18:51Z -> 19:57Z

## Summary

Three threads: (1) staged the ETFS_CANON AE Dynamo lane skeleton (CTO later BLESSED it); (2) executed the Andrew-direct P0 -- repointed the inflection ETFS producer from raw shared-Orion holdings to canonical (live Opal-ETF number $83.3M->$42.16M); (3) helped 0.6.0 reuse my m365 gateway for the BD OTP-relay (grounded a load-bearing gotcha). DS owner-reviewed my W2 49F producer = PASS.

## 1. ETFS_CANON Dynamo lane skeleton (COO 192223Z; CTO BLESSED 193246Z)

Staged (commit 3f617291d, un-wired TF root so it can't be applied): opal-etfs-ownership-daily table (PK client_etf={client_id}#{etf}/SK date + GSI-etf + GSI-client = 3 cuts, PAY_PER_REQUEST+PITR) + etfs-canon-fanin Lambda (daily-slice->Dynamo upsert, internal reader-IAM read-etfs-daily+write-table only, zero firm-bucket) + README finalize-on-bless checklist. CTO blessed; finalize/deploy is GATED behind the inf P0 (else the fan-in canonicalizes the inflated inf rows).

## 2. INF-CANONICAL P0 (Andrew-direct, DE-found, COO 194143Z) -- LANDED + verified

Repointed inf-etf-ownership-daily raw gold/holdings ($377.6M book / $83.3M Opal-ETFs, ~50% non-Inflection shared-Orion) -> gold/canonical/holdings_ ($202.3M / $42.16M, Inflection-owned, ties PartnerAnalytics Total AUA). Turned out 3-part (not env-only):
- ENV: HOLDINGS_PREFIX repoint.
- IAM: added gold/canonical/holdings_* read (the env repoint 403'd; role only had gold/holdings/*).
- CODE: part_date strips the "holdings_" prefix (canonical file = holdings_{date}.parquet -> the slice was wrongly keyed daily/inflection/holdings_{date}.json).
VERIFIED LIVE: inf 06-24 = $42,164,128.89 (was $83,336,938.68), correct key, source canonical. 49F W2 verified CLEAN separately (RPS book $1.63B ties canonical; DS owner-review confirmed $1.591B ties, single-custodian, no shared-account inflation).
PARTIAL backfill: June (06-08..06-24) corrected; May/early-June (26 dates) SKIP "no-valued-source" -- the MAY canonical has ~35% non-zero-MV rows (zero/closed positions) tripping the DS COMPLETENESS_FLOOR=0.5, though total value $203.8M IS present -> floor mis-fire (DS-contract question, flagged DS, recommend filter-zeros-before-floor).

## 3. m365 gateway help (0.6.0 BD OTP-relay)

GROUNDED (whoami): the gateway IS Andrew's identity (Andrew@opalinvest.com), not a bot -> reshaped 0.6.0's relay. Searched Andrew's mail: NO SS&C/BD OTP email (only Avanan/Atlassian codes + the AWS-SNS cookie-DEAD alerts) -> Path A (read-his-email) not viable via his mailbox; default Path B (Teams/SMS) or the BD-login-account's own inbox. 0.6.0 routed the MFA-channel Q to CVO for tonight's reseed.

## Deployment Sequence + Verification (AE)

inf P0 (deploy ledger 20260625T1942Z, tag inf-pipeline-v1.7.76):
- apply-1 env (1 changed) -> 403 -> apply-2 IAM canonical-read (1 changed) -> wrong-key -> code fix + build (sha YeoQp6K...) -> apply-3 (1 changed) -> 0-diff. Live invoke 06-24: $42,164,128.89 correct key. firm-sep unchanged (reads own-firm canonical, writes etfs only).
ETFS_CANON skeleton: NOT deployed (un-wired root); ds-gate PASS, terraform fmt clean.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-iam | inf producer firm-sep (canonical read added, no cross-firm) | PASS |
| comp-freshness | canonical holdings_ coverage + presentation platinum | PASS |
| ds-commit-gate | etfs-canon-fanin + inf producer code fix | PASS |
| terraform fmt | etfs-canon skeleton | PASS |

**What worked:** grounding the P0 against the actual artifacts (raw $83.3M vs canonical $42.16M, exact) before deploying; the staged-iteration (env->403->IAM->wrong-key->code) caught each layer via live invoke (never trust rc=0). whoami grounded the m365-gateway-is-Andrew gotcha.
**What failed:** the env-only assumption (the repoint needed IAM + a code fix too); the May backfill (canonical floor mis-fire). Both surfaced + flagged, not papered over.
**Gap found:** the DS COMPLETENESS_FLOOR mis-fires on the zero-MV-heavy May canonical (value present, row-fraction low) -- DS-contract question.

## Current State

- inf-etf-ownership-daily LIVE on canonical (inf-pipeline-v1.7.76); inf Opal-ETF slices corrected for June; live/recent number = $42.16M.
- 49F W2 (bd-v2.39.0): DS owner-review PASS, tie-out clean.
- ETFS presentation (shared-infra-v1.32.x): deployed + CVO-certed; SES sender live (0.7.0), push inert pending Andrew recipient list.
- ETFS_CANON skeleton: CTO-blessed, finalize/deploy gated on the inf-P0 completing (May) + COO sequence.

## Next Steps

- **[2.0.0_SA_COO]** confirm the S3-delete of the stray daily/inflection/holdings_2026-06-24.json (correctness hazard) -> then I re-run the dashboard (platinum drops ~$41M to ~$552M).
- **[0.4.0_DS_ClientPlatform]** the COMPLETENESS_FLOOR semantics for the May canonical (recommend filter-zeros-before-floor) -> unblocks the May inflection backfill; + AVGCAP June re-run (signaled).
- **[self]** on stray-clear: re-run dashboard + RAVC COO; then finalize/deploy ETFS_CANON (COO sequence); fold the canonical-daily orchestrator into /49-schwab-conv (DS, no-rush).
- **[Andrew/0.7.0]** SES recipient list -> activate the presentation push (held for the inf correction).
