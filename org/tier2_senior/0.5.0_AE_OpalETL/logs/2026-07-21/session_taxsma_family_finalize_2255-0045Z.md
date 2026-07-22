# Session Log -- OPAL_TAXSMA family finalize (0.5.0_AE_OpalETL~A lane)
**archetype:** MIXED (IMPLEMENT primary; SCRIBE for the retraction/records; VALIDATE for the exercises + the tier-2 live probe)
**Window:** 2026-07-21 ~22:55Z -> 2026-07-22 ~00:45Z | **Agent:** 0.5.0_AE_OpalETL~A (sovereign-delegate lane)

## Summary
Andrew-direct: finalize the OPAL_TAXSMA family end-to-end. Corrected two stale premises in Andrew's
summary (PT2 was NOT "not started" -- a proven one-account Chiles slice; OPAL_TICKET P0 already shipped),
then built + exercised every buildable-now leg and staged every gated one. 8 commits, all pushed to CLOUD.

## Work done (commit-cited)
- **b29f82699 records:** fold-order retraction (CTO 07-16). Killed the step-2-manual/"not-derivable" premise
  (dated, not silent) in tax-pt1 SKILL + OPAL_TAXSMA.json; persisted the fact_ult-not-fact_uln FEED TRAP;
  README convert_optimization LANDED + ADVI->OPAL. (PRD banner + WS-2 TO drift = owned-paths out-of-lane ->
  handed to CTO / DS.)
- **4ffe7415d /tax-pt3:** step-3 FactSet-conversion runner. .claude/skills/tax-pt3/SKILL.md + tools/tax_sma/
  pt3_stage.py (SharePoint I/O glue) wrapping the CTO-blessed run_converter.py (byte-identical canonical).
  EXERCISED end-to-end on synthetic Schwab data (divest cross-ref, CASH_USD, /->. rewrite, lot numbering).
- **7d97a8bed + bb9e26566 registry chain WS-R1/R2/R3:** taxsma_registry.py (S3-JSON roster, ETag-conditional
  RMW -- conditional-PUT enforcement EXERCISED on live S3), taxsma_resolver.py (D2 exact ladder, never fuzzy),
  taxsma_seed.py; discover_accounts() stub -> registry read; +ReadTaxsmaRoster IAM (staged). SEED LANDED live:
  Chiles active (tier-1 exact 22596361), Bump+Macy pending_resolution.
- **6d724cd47 /tax-newacc WS-R4:** taxsma_newacc.py + skill (resolve->enroll->ad-hoc pull). Exercised dry-run.
- **0ac99a72c WS-R2 tier-2 finding:** Andrew-authorized live probe -> PROVEN the sanctioned portfolioreporting
  AccountDetailSearch is masked-last-4 / no-exact-filter (positive-controlled Chiles). Exact full number is
  ONLY on account-api/* (tier-3 new egress). Resolver updated; Bump/Macy stay pending until Andrew's word.
- **e819903b2 records:** PT2+REGISTRY JSON ground-truth + owner -> 0.5.0~A (Andrew 07-21, CTO ACK).
- **806b7cfcf WS-4/WS-R5 IAM plan:** taxsma_gateway_iam.tf (opal-mcp-emp-alyssa-read: WS-4 gold-read + WS-R5
  invoke-producer/roster-RW) + taxsma_rule22a_verify.sh + apply-plan doc. terraform fmt clean. NOT applied.

## Compiler Tools
| Tool | When | Result | Note |
|---|---|---|---|
| comp-surface-check | every commit (via safe-commit) | PASS (no critical surface) | 9 commits, all clean |
| comp-pulse (risk-reflex) | every commit (via safe-commit) | CLEAN / advisory-HOLD | tax-pt1/pt3/newacc HOLDs cited a 53-day-old superseded memory node (COO-sole-committer, CL fabric) -- READ + discharged as stale |

**What worked:** the risk-reflex surfaced a stale danger-node; reading it (per the reflex) confirmed non-applicability fast.
**Gap:** the danger map is 186h STALE; the coupling-citation is a false-ish positive on a superseded regime.
**Why not comp-which/comp-iam/comp-kuzu:** this window was greenfield module authoring (registry/resolver/skills)
+ operational aws (s3 ls/cp existence checks, the Andrew-authorized vendor probe) + a new-role IAM plan. comp-iam
is NECESSARY-NOT-SUFFICIENT for NEW roles (models action, not (action,resource)) -> used the live simulate PLAN
(taxsma_rule22a_verify.sh) instead, per Rule 22a. Estate-search tools didn't fit code-build work.

## Deployment Sequence + Verification (AE)
**NO APPLIES this session -- everything is STAGED for the CTO gate (COO cond a; CTO confirmed post-MDPF-flip).**
- Producer WS-R3 (code+IAM committed): build+upload+plan -> CTO apply-gate (plan-check pure-add + Rule-22a on
  the landed role incl +ReadTaxsmaRoster + firm-sep negative). Not yet built/uploaded.
- WS-4/WS-R5 IAM (TF+script+plan committed): terraform plan -> CTO plan-gate + Andrew security sign-off -> apply
  -> taxsma_rule22a_verify.sh evidence -> go-live. Not applied.
- Live exercises that DID run (read-only / control-write): registry_selftest (real S3 RMW on a probe key, cleaned
  up), resolver vs real dim_account_xref, seed LANDED to _ops/taxsma_roster.json (verified via s3 cp), the
  Andrew-authorized tier-2 probe (ClientView token mint + AccountDetailSearch enumerate, positive-controlled Chiles).

## Blockers
None BLOCKED. Gated (evidence-cited, not assumption):
- Bump/Macy exact resolution: needs Andrew's account-api (tier-3) egress-word extension (tier-2 PROVEN masked, @0ac99a72c). [Andrew]
- Producer WS-R3 deploy apply + WS-4/WS-R5 IAM apply: [1.0.0_SA_CTO] post-MDPF-flip (his ACK) + Andrew IAM sign-off.
- WS-4 go-live COND-2/COND-3 (re-id map location + gold anonymization holds): [0.4.0_DS_ClientPlatform] WS-3 layout.
- WS-5 daily trigger: DEFERRED by the consolidation automation-suspension (Andrew standing).
- /tax-pt3 + PT2 live-validation: fresh Tax-Lot export (timing).

## Current State (zero-context handoff)
- **Registry LIVE:** s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json -- Chiles 0027265115 active
  (bd_internal_id 22596361), Bump 0035940058 + Macy 0091939812 pending_resolution.
- **Producer** opal-assets-bd49f-reporting-pull: DEPLOYED (last 07-20, DRY_RUN=0, manual-invoke). discover_accounts()
  now reads the registry (committed @7d97a8bed, NOT yet deployed -- staged). Modules colocated in its dir:
  taxsma_registry.py (packaged, stdlib+boto3), taxsma_resolver.py/taxsma_seed.py/taxsma_newacc.py (enroll-context, NOT packaged).
- **Skills:** /tax-pt1 (live), /tax-pt2 (live, DT), /tax-pt3 (new, exercised), /tax-newacc (new, exercised).
- **WS-4/WS-R5 IAM:** infra/aws/terraform/m365-mcp-gateway/taxsma_gateway_iam.tf + taxsma_rule22a_verify.sh (ready, unapplied).
- **PT2 pipeline:** bronze->silver->gold proven one-account (Chiles, 07-17); multi-account waits on Bump/Macy resolve
  + producer deploy + DS silver/gold multi-account generalization (Rule-13 DS lane).

## Next Steps
1. [Andrew] account-api (tier-3) egress word -> I resolve+activate Bump/Macy immediately (positive-controlled).
2. [1.0.0_SA_CTO] post-flip: producer WS-R3 deploy apply + WS-4/WS-R5 IAM apply (I drive build+upload+plan on his window).
3. [0.5.0_AE_OpalETL~A] optional next: draft the WS-6 gateway read-path (email->ARN->assume->read); or the producer
   build-to-plan bundle for CTO. Holding reachable, no wind-down.
4. [0.4.0_DS_ClientPlatform] WS-4 COND-2/3 (re-id map location + gold anonymization) before IAM go-live; silver/gold multi-account when Bump/Macy land.
