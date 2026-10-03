# Never-widen sign-off packet -- Y-4 enrichment, RE-PACKET: the runner's Kimi read narrowed at its ONE carrier (both statements), with the resident st17 -> st18

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~05:4xZ.
**Authority:**
- CTO msg 104515 (batch 199), the enrichment.
- CTO msg 104552 (batch 208): "iam.tf granted to you for the one local; re-packet D3 + D2 together ... printing
  MatchedStatements before and after. The rollback was correct."

**Ledger:** `irpt-y4e2-20261003`, opened at the start (05:38Z): D3, D2 and V1 are open. U2 is REUSED from
`irpt-y4e-20261003` (closed, its U2 proven). The first packet (`NEVER_WIDEN_SIGNOFF_PACKET_Y4E_20261003.md`) stands for
D2's artifacts and the 12-member attribution; this packet replaces its D3 and its apply protocol.
**Two moves**, in one window: D3 (both IAM policies), then D2 (resident). Both or neither. No vendor call.

## 1. What changed since the first packet

- **The cause of the rollback, measured.** `iam.tf:96` `ReadYChartsAndSharedVisionSecrets` (inline policy
  `irpt-ycharts-runner`) grants GetSecretValue + DescribeSecret on `local.kimi_secret_arn`, which read
  `astn/kimi/api-key-*`. The runner therefore read the Kimi key before Y-4; Y-4's `ReadTheEstateKimiKey` was redundant.
- **The fix, ONE carrier:**
  - `iam.tf:63` `kimi_secret_arn = ...astn/kimi/api-key-??????` (`40fcacb067`, the one line batch 208 grants);
  - `resident.tf` `ReadTheEstateKimiKey` Resource = `[local.kimi_secret_arn]` (`f1f5aca07e`).
  Both statements now narrow together or not at all.
- **The plans** (`Y4E/plan_d3_y4e2.txt` targeted, `plan_ycharts_full_y4e2.txt` full): 2 to change, `runner` and
  `runner_resident`. Exactly two values change, each the Kimi ARN `api-key-*` to `api-key-??????` (a count of ` -> `
  lines in the targeted plan: 2). The login and session ARNs do not move.

## 2. MatchedStatements before (`Y4E/IAM_SIMULATION_REPACKET_BEFORE_20261003.txt`, 05:40:19Z)

| name | decision | matched |
|---|---|---|
| the estate Kimi secret (6-character suffix) | allowed | `irpt-ycharts-runner`, `irpt-ycharts-runner-resident-policy` |
| a sibling `astn/kimi/api-key-extra-AbCdEf` | allowed | `irpt-ycharts-runner`, `irpt-ycharts-runner-resident-policy` |

**Required after D3:** the estate secret `allowed` (matched by both policies); the sibling `implicitDeny` (matched by
none). Otherwise D3 rolls back, as the first time.

## 3. D2 (unchanged from the first packet, section 1)

- Resident `a6f6e7165e-st18`: tar version `UnePbYDl..` (`ff1ce55b..`) and install script version `g6Lx_XPK..`
  (`a44b5579..`); fetch-and-run `Y4E/install_fetch_and_run.sh` (`27690608..`).
- Gate G1-G5 PASS. The package holds no Terraform file, so the two IAM commits since do not change it.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - running root `828c37c6f7-st17`;
   - queue 0/0, no non-terminal job, the provider lease empty;
   - both policies' Kimi ARN read `api-key-*`.
3. **D3:** the targeted plan (re-planned if stale), ONE `HALT_ACK=1 safe-apply`. Both policies read back.
   `live_walk/kimi_resource_simulation.py` must show section 2's required result, or D3 rolls back and D2 does not run.
4. **D2:** `head-object` of the script key printing `g6Lx_XPK..`; the fetch-and-run over Systems Manager. Read back:
   - root `a6f6e7165e-st18`;
   - the st18 digests equal git, and `TOTAL_SUGGEST_SECONDS = 240` present;
   - unit active, queue 0/0.
5. **V1:** the installed worker carries `unasked=` and `elapsed_s=`. The live typo run is `irpt-y4-20261003`'s V1, after
   option A.

## 5. Rollback

- **D3:** a targeted apply with `local.kimi_secret_arn` back to `api-key-*`. Both statements return together.
- **D2:** root `828c37c6f7-st17` stays on the host; the install script's rollback branch restores it.

## 6. Not claimed

- `iam.tf:59-60`'s comment still calls `-*` "not a wildcard over other names". Batch 208 grants this seat the one line
  only, so the comment is parked for the file's owner (`2.0.0_SA_COO~P`); the wording is in
  `Y4E/P_IAM_KIMI_CARRIER_PATCH_20261003.patch`.
- The login and session ARNs carry the same `-*` shape. They are not narrowed here.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~05:4xZ, on this packet's bytes at the commit that carries it. The write set is the Kimi ARN in two
IAM policy statements and one resident root with its unit's ExecStart and cutover receipt. The rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
