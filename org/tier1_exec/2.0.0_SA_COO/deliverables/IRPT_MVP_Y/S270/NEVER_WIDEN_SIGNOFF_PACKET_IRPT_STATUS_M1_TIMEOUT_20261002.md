# Never-widen sign-off packet -- S270 M1: irpt-status timeout 15 -> 29 s (one line), the mitigation before M2

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~13:4xZ.
**Authority:** CTO rulings batch 171 (M1 NOW; `ops/lambda.tf` granted as an exact file in lane `IRPT_BCKEND_FAST_Y_TFPOLICY`,
for that line only; "the packet shows a targeted plan with that one change and a cold default-page history answering
200") on ARMED row IRPT_BCKEND-S270. **Ledger:** `irpt-status-m1-timeout-20261002` (D1, V1). **One move.** No code, IAM,
route or other function moves. No vendor call.

## 1. What ships

- `infra/aws/terraform/investor-reporting/ops/lambda.tf`: `timeout = 15` becomes `29` (commit `d4a494c1e8`, merged
  `d2ae757ce6`).
- 29 s is the margin under the HTTP API's 30 s integration ceiling.
- **Targeted plan** (`S270/plan_m1.txt`, read 13:4xZ): `module.irpt_status.aws_lambda_function.this`, 1 to change,
  `timeout 15 -> 29`. Nothing else: the code stays `BNe2n9cV..`, the artifact's latest.

## 2. Blast radius, by branch

| an irpt-status invocation that | BEFORE | AFTER |
|---|---|---|
| finishes under 15 s | answers | the same |
| would finish between 15 and 29 s (the cold default-page history, measured 15000 ms timed out) | killed at 15 s, HTTP 500 | answers |
| runs past 29 s | killed at 15 s | killed at 29 s; the HTTP API's 30 s ceiling answers first or at once |

Only the wait changes: a longer timeout lets a slow call finish, and bills the same work it already does. This
mitigates S270; it does not meet the 10 s bar. M2 does that.

## 3. Apply protocol, proof and rollback

1. Both halves at HEAD naming this file's blob.
2. Before-read: timeout 15, CodeSha256 `BNe2n9cV..`.
3. D1: a fresh targeted plan showing only `timeout 15 -> 29`; ONE `safe-apply`; the configuration read back
   (timeout 29, CodeSha256 unchanged).
4. V1: the next invocation is cold, because a configuration change starts a new environment. A default-page history
   must answer HTTP 200, with its REPORT duration and Init Duration read (`live_walk/s270_timing.py`). Then the warm
   reads.
5. Rollback: one targeted apply with `timeout = 15`.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~13:4xZ, on this packet's bytes at the commit that carries it. The write set is one attribute of one
function.

## CTO half -- 1.0.0_SA_CTO

(not signed)
