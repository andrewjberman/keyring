# POSN_AGGFIX round 1, the middle: five of seven orders drained, the edge gate live, and every worker refusal traced to the issuer's own cut -- 2.0.0_SA_COO~Z

**Date:** 2026-09-15
**Task Order:** POSN_AGGFIX round 1 (L7 drains, mid-round amendments)
**Status:** IN PROGRESS (TO-A3-1 producer deploy running on worker ~1; TO-B3-1 queued behind it)

---

## Objective

Drain each worker's order as it reported, re-cut every criterion a worker correctly refused, carry Andrew's two scope words and the CTO's sign-off
conditions into the orders before the legs they gate, and keep the round moving toward the two deploys and the served read.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-merge.sh | 6 drains (A1 partial, A1, B1, C1 partial, C1, A2 partial, A2, B2) | PASS | every channel conflict unioned by row id and re-graded through `--continue`; no bare commit |
| proof-of-spec-check | run from each worker's own worktree before each drain | PASS | VALID rc=0 each time; the FAIL rows were read, not trusted from the report |
| surprise-row-gate | via safe-merge and safe-commit | PASS | graded the merged index each time; 24 rows at HEAD |
| terraform plan | the issuer's 18:3xZ whole-root plan | PASS | the WAF leaf detail it held matched the worker's show -json and the CTO's |
| boto3 live reads | CloudFront association versions, twice | PASS | 25 of 25 at version 20 before and after the CTO's urgent hold |

**What worked:** reading the proof instance with the worktree's own checker before every drain; the live association read as the discriminator for "did a rollback start".
**What failed:** the comp-tool rail aborted one proof-check call on a stray grep; resuming a finished worker by message failed ("no transcript"), so every continuation was a respawn with coordinates.
**Gap found:** nothing reads a Terraform plan's leaf diff; each seat built its own `show -json` reader.

---

## Work Completed

### 1. Andrew-direct, recorded and broadcast twice
~19:0xZ: "We do not need Opal Fixed Income for any of this" and "We are only interested in the Primary Models, that is UST ST INT LT and ULT"; ~19:1xZ: "a) Yes they split into primary models" and "50/50 ST INT would be 50% into ST and 50% into INT". Record `deliverables/ANDREW_DIRECT_20260915_190xZ_POSN_AGGFIX_NO_OPAL_FIXED_INCOME_PRIMARY_MODELS_ONLY.md` @fc8cdf1a1e; nothing issued changed. The $8.3M gap later measured to be exactly opal_fixed_income (row W1-S1, disarmed for this project by Z-S3).

### 2. The never-widen halves
CTO halves @ae1c985da4: producer SIGNED with N = 3 writers (two restore writers by prefix; residual row Z-S2); edge SIGNED on three conditions. The COO producer half corrected to N = 3 and later to 4 write sites; both producer halves agree a served difference is a parsed-value difference (CTO ADDENDUM 1 @10d61c774f, COO ADDENDUM 2 @02c0bb8d91). The edge halves re-signed for the WAF provider normalization (@e2c0b284e4, @31995abe76) and for its permanent re-plan residual (@b2628856f5).

### 3. Drains and amendments, by order
| Order | Outcome | Issuer cut defects the workers refused, and the re-cut |
|---|---|---|
| TO-A1-1 | COMPLETE @1189f40808 | A1-AC2 named one writer where the file has two write sites; A1-AC6's IAM query missed ResourceSpecificResults (@48a00724ca) |
| TO-B1-1 | COMPLETE @4a9e12f2bf | the tab mount hand-over sat outside both portal grants; moved into TO-B2-1 (@e2c0b284e4) |
| TO-C1-1 | COMPLETE @70e74a93bb, gate LIVE v20 on 25 of 25 | the CTO's three conditions (@b62ea1caa3); `-target` pulls the WAF in (@e2c0b284e4); the re-plan can never read No changes (@b2628856f5, after the CTO's urgent hold) |
| TO-B2-1 | COMPLETE @7e538e4387, portal drain ref at 3ec1f83c | none |
| TO-A2-1 | COMPLETE @1c71fb87be | A2-AC11's diff base carried other orders' infra files; A2-AC13 could not equal a CLI path that predates the order (@b6a6efb45f) |

### 4. The one live-risk moment
At 21:10Z worker ~2's re-plan reader printed BRANCH B on the permanent WAF residual, which would have rolled back a correct live gate. 1.0.0_SA_CTO~Z flagged it (msg 23255); this seat sent the worker a HOLD through its queue, read the live associations (25 of 25 at v20, no rollback started), re-cut C1-AC11 and let the worker finish. Nothing rolled back.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Re-cut criteria at partial drains rather than override | every refusal was correct; the defect was in the cut, and an override would have shipped an unmet criterion |
| Respawn with coordinates instead of resuming | a finished worker could not be resumed; the prompt carries branch tip, standing criteria and next row id |
| HOLD then re-cut C1-AC11, not roll back | the residual sits inside both signed halves and the live WAF read equal; a rollback would remove a verified gate over a no-op |
| Operating facts written into TO-A3-1 before hand-off | the halt gate's serial path, the HALT_ACK procedure and the recorder's python path cost TO-C1-1 two refused applies |

---

## Blockers

None. TO-A3-1 runs on worker ~1 under both producer halves; TO-B3-1 waits only on TO-A3-1's drain (TO-B2-1 and TO-C1-1 are drained).

---

## Current State

POSN_AGGFIX round 1 has 5 of 7 orders COMPLETE at SITEZ (latest drain 1c71fb87be, TO-A3-1 amendment 33dad02f79). The edge refusal is live: auth-validator-edge version 20 on 25 of 25 associations of EVTSA9VEHNZVH, the deploy ledger closed. The producer change is committed but not deployed; worker ~1 is deploying it now (TO-A3-1) in /c/tmp/wk-aggfix-1-1. The portal work sits on refs/drains/aggfix-1-portal = 3ec1f83c (5 files from PROD edf85ce503), not promoted. 24 channel rows. Every commit LOCAL.

---

## Next Steps

1. **Drain TO-A3-1 on its report** -- proof check, the served Branch A/B read, then hand TO-B3-1 to worker ~3 with TO-A3-1's VersionIds.
2. **Drain TO-B3-1**, then the drain-end message to 1.0.0_SA_CTO~Z: the CVO's watermark against the row count and any armed row without a seated owner.
3. **[1.0.0_SA_CTO~Z, round analysis]** rows Z-S1 (PRD fallback sentence), Z-S2 (restore writers residual), W1-S1 (MDPF MODEL_ORDER defect for 0.4.0_DS_ClientPlatform), W2-S4 (the WAF normalization on this root).
4. **[Andrew's goal, via 23229]** after validated completion: 0.0.0_AB_MSTR~Z's portal /integrate, then 1.0.0_SA_CTO~Z's /prod-deploy.
