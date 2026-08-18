# Deploy completion — Global account-distribution cottonwood heal (Andrew-direct)

**Status:** CLOSED 2026-08-18 (all three open legs discharged: publisher live-verify, DE render PASS 08-04, scheduled runs daily through today)
<!-- disposition act 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md); evidence in the CLOSE block at foot. -->

**Deployer:** 0.2.0_DS_PortfolioAnalytics · 2026-08-04 18:26–18:32Z (publisher leg pends AE)
**Authority:** Andrew-direct ~17:5xZ (verbatim record committed) + never-widen sign-off COMPLETE: CTO 182546Z (4 riders) + COO 182632Z. Spec: `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/deliverables/GLOBAL_ACCT_DIST_COTTONWOOD_INCLUSION_SPEC_20260804.md`.

## What deployed (review/deploy split honored — hash-pinned)

`data/mdpf/scripts/gold/dim_mdpf_account_distribution.py` — repo HEAD copy, file last modified by **@34e38a8e55** (W-6, 07-23, 0.4.0_DS-reviewed; the fold @fa491f9b61) → `s3://opal-data-mdpf/code/scripts/gold/`. Pre-heal deployed vintage: 2026-07-21 17:42:42Z, ZERO cottonwood references (the 12-day committed-but-never-deployed gap). Post-deploy oracle: **comp-pipescript deployed MATCH** (rider 1).

## Execution + evidence (riders 2–3)

| step | invocation | observed | prediction bound |
|---|---|---|---|
| re-emit | `dim_mdpf_account_distribution.py --firm global --upload` (production script, 18:29Z) | `OK UPLOAD+VERIFIED gold/mdpf_revamp/global/account_distribution.json` 7,640B ETag 45230662526b | — |
| staged content read | independent S3 get | `meta.cottonwood_fold` PRESENT: **accounts_folded=295**, by_model_folded {int 224, lta 12, ltc 96, st 105, ust 6}, source=the pair sidecar | `total.account_count` **7925 == the dry-run prediction exactly** |
| accrual | `build_portal_gold_accrual.py --only portal/gold/mdpf/global/account-distribution/2026-08-04.json --allow-overwrite` (the R5 deliberate same-date repair pair — replacing the 2-firm content at the same as-of) | `OK wrote ... (7,640B md5 45230662526b)` written=1 errors=0; PLANNED 14, **0 R4 errors** (the aum-metrics declared-absent class fully cleared post-round-4) | md5 == staged ETag (bridge verbatim) |

Full-figure record (all deliberately moved vs the 2-firm serve): count 7632→7925 (+293 = cottonwood's 295 dim accounts net of the funded-$1K floor), total_aum $1,694,070,546.01, mean $213,762.84, median $73,299.37, p10 $8,108.58 / p25 $24,284.52 / p50 $73,299.37 / p75 $202,074.20 / p90 $476,683.44, max $34,028,927.20, std $651,726.71.

## Open legs (close conditions)

- **Publisher (AE, one-invoker grant):** asked 183215Z with the bound predictions. CLOSE on their live-verify of `platinum/mdpf/global/account-distribution.json` (3-firm body + marker). *(Note: their invoke also re-publishes the round-4 fresh aum-metrics set — intended supersession per CTO 142446Z.)*
- **DE render check (rider 4):** pinged 182550Z; bell curve + container metrics on the served heal.
- **Scheduled-run evidence (NEVER#4):** tomorrow's 6b cycle reproduces the 3-firm emit — this ad-hoc is the heal, not the production proof.

## Riders noted

- F5 crosswalk WARN (eclipse_id=31 blend candidate) — pre-existing, routed in the spec.
- Gate candidate (CTO routed 182546Z): commit-time deploy-parity stage = GATE-class on the CANRTE candidates ledger; scheduled sweeper = monitor-class, waits for Andrew's word.
- Sub-cent by_model representation (COO 182632Z note 1, my lane): ruling = reconcile-by-construction (largest-remainder cent allocation at emit) on the emitter's NEXT touch; sub-material, not blocking, tie law unaffected.


---

## CLOSE (2026-08-18, 0.0.0_AB_MSTR disposition act)

Leg (a) publisher live-verify + leg (c) scheduled-run evidence, live 2026-08-18: `head-object
opal-data-portal-v2/platinum/mdpf/global/account-distribution.json` = LastModified 2026-08-18 13:50:50 GMT, 8,136 B;
body generated_at 2026-08-18T13:31:08Z (one minute after the live mdpf-scheduled-floor 13:30Z fire) carrying
`meta.cottonwood_fold` (accounts_folded=315, in-band 3-firm marker, source gold/mdpf_revamp/cottonwood/account_units.json);
total.account_count=8009 (evolved from heal-day 7,925 under 14 days of scheduled runs). Positive control: sibling
aum-metrics.json heads fine, same batch. Leg (b): `2a1df45844` (2026-08-04T21:32Z, 0.4.0_DE) acct-dist render leg PASSED.
Later context, not a leg: the legacy smartx-account-distribution-daily trigger set was killed 08-18 by OPAL_MDPFCLEANUP K2
(@5dc5863a7d); the platinum publisher path named by leg (a) is the one serving live today.
