# Never-widen sign-off packet -- Y-4 enrichment: the check gate's per-upload total on the resident (st17 -> st18) and the runner's exact Kimi secret, at ONE commit `a6f6e7165e`

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~05:0xZ.
**Authority:** CTO msg 104515 (batch 199): "Y-4's next enrichment, not a condition of this ship: (1) a per-upload total
budget for the gate (worst case today: 6 x 120 s); (2) narrow the runner resource to `astn/kimi/api-key-??????`."
Batch 148's rule: every changed member attributed.
**Ledger:** `irpt-y4e-20261003`, opened at the start (04:54Z). U2 is closed; D3, D2 and V1 are open.
**Two moves**, in one window: D3 (IAM), then D2 (resident). Roll back both or neither. No vendor call. `irpt-ycharts-generate`
does not move: it composes no gate, and the full ycharts plan shows no change for it.

## 1. What ships

**The code:** `4ed0c7b816`, merged `d82ba47e4e`, packaged whole-tree at `a6f6e7165e`.

| file | change |
|---|---|
| `intake/resolution_kimi.py` | `KimiAdvisory.call(..., deadline=None)`: an outer deadline on the advisory's own clock can only SHORTEN the kind's 120 s budget. One already past makes no attempt, writes no telemetry and sends nothing (`KIMI_TIMEOUT`). A malformed one refuses `KIMI_DEADLINE_INVALID`. A caller that passes nothing is unchanged |
| `intake/upload_suggestions.py` | `TOTAL_SUGGEST_SECONDS = 240` (two check budgets). Every ask carries the upload's one deadline. Once it is spent, the remaining rows are not asked (`unasked`) and keep their findings as the freeze wrote them. A symbol on two rows is asked once. The counts carry the elapsed seconds |
| `ycharts/generate/resident_worker.py` | `_check_gate` runs the gate on the advisory's own clock. The journal reads `IRPT_RESIDENT_SUGGEST asked= suggested= verified= unasked= elapsed_s=` (counts only), which is the elapsed figure Y-4's V1 must record |
| `ycharts/resident.tf` | `ReadTheEstateKimiKey`: Resource `astn/kimi/api-key-*` becomes `astn/kimi/api-key-??????` |

**The worst case:** 720 s becomes 240 s of Kimi time per upload, inside the resolve message's 900 s visibility. The verify
read that follows is the provider's own securities_info read, with its own timeouts.

**Artifacts (U2, closed):**
- **The resident tar:** `irpt-resident-a6f6e7165e-st18.tar.gz`, S3 version `UnePbYDlYpd7nsLpRd8Lpi4WqJ8rUzOV`, 790,317 bytes,
  sha256 `ff1ce55bd09a8defdd5289901d9e0ff5058fe3a7d7a40b474bd2c8fb024537bd`.
- **The install script:** `resident_host_install_a6f6e7165e-st18.sh`, S3 version `g6Lx_XPK5_QL3qwUNmVI4.37nsFqUGxt`, sha256
  `a44b55795b65d71288f2c398cb82fa6973504889a87bc109db3350c220bb64e6`.
- Both keys read 404 before the upload, and both read back by version equal.
- **The fetch-and-run:** `Y4E/install_fetch_and_run.sh`, sha256 `27690608ac0ebb790f4f9b73fc35574187860ecc42530bc6e004baf575270e2d`.
- **The gate:** `Y4E/GATE_OUTPUT_Y4E_RESIDENT_20261003.txt`, G1-G5 PASS: 249 of 249 members equal `git show a6f6e7165e`;
  102 of 102 .py members compile. The host library and wrapper are unchanged (`857d90b8..`, `55ddb8f7..`).
- **The plans:** `Y4E/plan_d3_y4e.txt` (targeted) and `plan_ycharts_full_y4e.txt` (full) each show ONE change, the
  Resource string.

## 2. Every resident member changed since the running st17 (G5: 12 changed, 0 added, 0 removed, 239 identical)

| member | commit | attributed to |
|---|---|---|
| `intake/resolution_kimi.py`, `intake/upload_suggestions.py`, `ycharts/generate/resident_worker.py` | `4ed0c7b816` | this enrichment (section 1) |
| `ops/entry.py`, `ops/owned_requests.py` | `7f1135f0ee` | **W2-06** (CTO batch 165, half batch 204), served on irpt-status since 04:28Z. The resident makes no owned read with an include, so its default path is the pre-E7 path, key for key |
| `docs/contracts/.../OwnedAnalysisRequest.schema.json`, `docs/contracts/.../routes.json` | `7f1135f0ee` | W2-06's contract (additive `composition`; the include note) |
| `_contracts/ExportBundle.schema.json`, `docs/contracts/.../ExportBundle.schema.json` | `b66691eb1b` | **IB-pr-301** (`2.0.0_SA_COO~P`'s worker, CTO batch 203): additive `performance_source`. No resident module loads ExportBundle (a census of the package's .py members finds only two comments). It rides inert by the whole-tree rule |
| `infra/logic/registry/reporting_policies.json`, `lib/opal_naming.py` | `b77e2af4d5` | **4.0.0_SA_CRO** (X10 / IRPT_DASHBD-S12): the PENDING `irpt-dashbd-x10-v1` gains two families. The ACTIVE `irpt-x10-v1` is byte-equal; served on irpt-status since 04:28Z (attributed in the W2-06 packet) |
| `reports/resident_bindings.json` | (generated) | `provenance` only, the build timestamp. Queue, tables, library and wrapper bindings are unchanged |

## 3. Proofs

**Offline at the code commit:**
- `ycharts/generate/tests/test_y4_check_gate.py`, 16 tests. Two are new: at 100 s per ask, the total bounds the gate to 3
  asked and 1 unasked, each ask carrying the one deadline; a repeated symbol is asked once.
- `intake/tests/test_resolution_kimi.py`, 48 tests. Five are new: an outer deadline only shortens the budget; a spent one
  sends nothing and records nothing; three malformed deadlines are refused.
- Negative control: on HEAD's three modules, 9 fail.
- Suites: intake 272 passed; ycharts/generate 396 passed, 30 skipped; ycharts/session 117 passed with 1 failed (the
  parked POSIX-host node of test_host_capture, a file this change does not touch).

**IAM before D3** (`Y4E/IAM_SIMULATION_BEFORE_20261003.txt`, 05:01:57Z): GetSecretValue on the estate Kimi secret is
`allowed`. On a sibling name `astn/kimi/api-key-extra-AbCdEf` it is ALSO `allowed`; that is the gap D3 closes.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - running root `828c37c6f7-st17`;
   - queue 0/0, no non-terminal job, the provider lease empty;
   - the runner policy's Kimi Resource reads `astn/kimi/api-key-*`.
3. **D3:** the targeted plan, re-planned if stale; ONE `HALT_ACK=1 safe-apply`. Read the policy back. Re-run
   `live_walk/kimi_resource_simulation.py`: the estate secret must read `allowed` and the sibling `implicitDeny`.
4. **D2:** `head-object` of the script key printing `g6Lx_XPK..`; `Y4E/install_fetch_and_run.sh` over Systems Manager.
   Read back:
   - root `a6f6e7165e-st18`;
   - the st18 digests equal git;
   - `TOTAL_SUGGEST_SECONDS = 240` present;
   - unit active, queue 0/0.
5. **V1:** the two reads above close this ledger. The live typo run is `irpt-y4-20261003`'s V1, after option A. It
   records the gate's elapsed seconds from the new journal field.

## 5. Rollback

- **D2:** root `828c37c6f7-st17` stays on the host; the install script's rollback branch restores it.
- **D3:** a targeted apply with the Resource back to `astn/kimi/api-key-*`.

## 6. Not claimed

- The live gate time: no upload can reach the gate until option A (S288).
- The 240 s figure: chosen as two check budgets inside the 900 s visibility. It is a constant, tunable by a later ruling.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~05:0xZ, on this packet's bytes at the commit that carries it. The write set is one IAM policy
statement's Resource and one resident root with its unit's ExecStart and cutover receipt. The blast radius is section 2.
The rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
