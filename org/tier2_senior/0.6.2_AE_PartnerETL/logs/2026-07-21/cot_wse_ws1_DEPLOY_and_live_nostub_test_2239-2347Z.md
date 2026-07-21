# WSE_COTMDL.WS1 -- DEPLOY + live no-stub test (cot-rebalancer-runner v0.1.0)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Agent:** 0.6.2_AE_PartnerETL · **Window:** 2026-07-21 ~22:39Z -> ~23:47Z · **TO:** WSE_COTMDL.WS1 (COMPLETE)

## Summary

Andrew-direct DEPLOY-NOW (@b5be0f680): deploy cot-rebalancer-runner now, test it (no stubs), confirm, issue to CVO -- overriding the sequence-behind-MDPF deferral. Grounded that NOTHING was deployed (live AWS: Lambda/role/rule all ResourceNotFound), then drove the full deploy: artifact -> source-map -> CTO-gated apply (0.7.0 monolith lane) -> Rule-22a verify -> LIVE no-stub test -> tag v0.1.0. DEPLOYED, live-tested (real 806KB pull, no stubs), confirmed to Andrew, issued to CVO.

## Andrew-direct (verbatim, recorded @b5be0f680)

> "I want it deployed now and after it is done and tested (make sure none are stubs) then i want a confirmation from you this is the case and have you issue your work to CVO to check"

## Work done (the 5-leg deploy, ledger CLOSED 5/5)

1. **Pre-deploy ground-truth:** verified NOTHING deployed (live AWS -- Lambda/role/rule ResourceNotFound; no artifact; no source-map entry; no tag). Answered Andrew honestly: not deployed.
2. **My parts:** registered cot-rebalancer-runner in lambda-source-map (Rule 4) @4fc02edfd; ran central build-and-upload.sh opal-assets cot-rebalancer-runner -> zip uploaded + write-verified (sha eeeXhavS..., 10187B) @4e668df37.
3. **Apply (L1/L2, 0.7.0 monolith lane, CTO plan-gated):** safe-apply RC0, 10 added / 0 changed / 0 destroyed (PURE-ADD, CTO-verified), re-plan 0-diff PASS. Lambda cot-rebalancer-runner (py3.12/512/300) + role live. Clean window (MDPF apply HELD -> no shared-state collision).
4. **Rule-22a IAM verify (L3, 0.7.0+me co-verified on the LANDED role):** GetSecretValue cot/session=ALLOW, PutSecretValue=implicitDeny, PutObject cottonwood/{bronze,meta}=ALLOW, PutObject 49f=explicitDeny -- read-only cookie-rider ENFORCED, applied-truth == TF.
5. **LIVE no-stub test (L4, mine -- Andrew's "make sure none are stubs"):** invoked the deployed Lambda (real Rebalancer pull, standing egress). Landed **34 real objects / 805,975 bytes** under blackdiamond/cottonwood/bronze/2026-07-21/: models(1pg/26KB/60 models) + accounts(5 pages, DISTINCT ETags, 911 accounts, ~557KB) + model_detail(25 real compositions) + meta complete-stamp. **Both fail-closed gates PASS** (pagination-integrity + count-reconcile), **opal_assigned=296** (matches discovery ground truth EXACTLY), transitive closure fired (25 details > 17 assignable Opal). Verified LANDED artifacts (ListObjectsV2 + stamp), NOT the invoke rc (CTO gate-4).
6. **Tag (L5, 0.7.0):** cot-rebalancer-runner-v0.1.0 on 4e668df37, pushed --follow-tags, record-terraform-deploy. Ledger CLOSED 5/5.
7. **Andrew CONFIRMED + CVO (3.0.0_SA_CVO) ISSUED** for the independent check (Andrew's explicit sequence).

## Compiler Tools (TO acceptance #4 -- every <run> vs <expect>)

| Tool | Result vs expect |
|---|---|
| `aws lambda get-function` / `iam get-role` (pre-deploy) | ResourceNotFound (both) -> confirmed NOT deployed (ground truth for the honest answer). |
| `build-and-upload.sh opal-assets cot-rebalancer-runner` | zip built + uploaded + WRITE-VERIFIED (size+sha metadata match). |
| Rule-22a `simulate-principal-policy` (isolated 1-arn/call) + live `get-role-policy` (0.7.0+me) | ALL-PASS: GetSecretValue ALLOW / PutSecretValue DENY / cottonwood ALLOW / 49f DENY. Applied-truth, not DESIRED. |
| live invoke + ListObjectsV2 + stamp read (no-stub test) | PASS -- 34 real objects/806KB, distinct ETags, both gates PASS, 296/14, closure fired. |
| `# rail-checked` on the pre-deploy aws-inspection | verifying LANDED/applied state (comp-* model DESIRED, can't tell landed-from-planned; live primitive is the only applied-truth oracle, Rule 22a). |

**What worked:** the no-stub test grounded on LANDED artifacts (distinct ETags per account page = real distinct pages, not a stub copied) + the count-reconcile gate reproducing 296 on live data = definitive no-stub proof, not an rc. **What failed:** n/a -- clean deploy. **Gap:** none new.

## Files Modified

- `infra/aws/lambda/ci/lambda-source-map.json` (cot-rebalancer-runner entry + sha) @4fc02edfd / @4e668df37.
- Records: `deliverables/COT_REBALANCER_DEPLOY_NOW_DIRECTIVE_20260721.md` @b5be0f680.
- Deployed (0.7.0 lane): `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` applied; tag cot-rebalancer-runner-v0.1.0.
- All pushed CLOUD.

## Compliance

Live egress this session was the AUTHORIZED test invoke (standing egress @64fdd919c, cot-BD). Read-only cookie-rider (GetSecretValue-only, IAM-enforced). Firm-clean (cottonwood only; 49f explicit-Deny verified). Bronze raw JSON (17a). No stubs (verified). Apply pure-add (0 change/0 destroy). CTO-gated, 0.7.0-applied, co-verified.

## Blockers / Next Steps

- **[3.0.0_SA_CVO]** independent verification issued -- awaiting verdict (I relay to Andrew).
- **[schedule]** exact daily cron DEFERRED to the WS-2/3/4 chain-timing confirm (06:00Z placeholder; standalone bronze needs no downstream alignment yet).
- **[WS-2/3/4 -- DS/DT lanes]** silver (fact_*) -> gold (dim_model_portfolio) -> MDPF DDB fold-in, triggered by the meta/{date}-complete.json stamp (WS-2 owns the stamp->silver trigger per COO ruling). Not my lane.
- **[self]** WS-1 COMPLETE. Reachable for CVO's verdict, the schedule-time pin, or downstream coordination.
