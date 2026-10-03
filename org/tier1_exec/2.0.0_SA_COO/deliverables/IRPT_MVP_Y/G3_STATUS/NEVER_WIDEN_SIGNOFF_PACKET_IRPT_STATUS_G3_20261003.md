# Never-widen sign-off packet -- G3: irpt-status gains the render-grant ports (the grant read, then the code and `IRPT_EVIDENCE_BUCKET`), code at ONE commit `b6bce5866a`

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~06:1xZ.
**Authority:** CTO rulings batch 175, `E4-G3-RENDER-PORTS-ON-IRPT-STATUS-AND-G4-ONE-DOWNLOAD-ROUTE-20261002` item 2:
- "CARRIER: `2.0.0_SA_COO~Y` ... `~P` supplies the render-port requirements: the env, the IAM read on the stored render
  grants, `grant.py`, `report_owner.py` and `reports/repository.py`."
- "Render ports on irpt-status are now intended: they make IB-pr-293's prospect branch reachable there for the Analysis
  print."

The requirements are `2.0.0_SA_COO~P` msg 104292. Batch 148's rule: every changed member attributed.
**Ledger:** `irpt-status-g3-20261003`, opened at the start (05:44Z). U1 is closed; I1, D1 and V1 are open.
**Two moves, in order:** I1 the grant read, then D1 the code and the variable. That way no render read reaches a function
without the read. Nothing else moves: no route, table, queue or other function.

## 1. What ships

| move | resource (ops root) | change (`G3_STATUS/plan_i1_g3.txt`; full `plan_ops_full_g3.txt`: these two, nothing else) |
|---|---|---|
| I1 | `aws_iam_role_policy.irpt_status_render_grant_read` (NEW) | `s3:GetObject` on `<core evidence_bucket>/firms/*/generations/exr_*/render_grant.json` only. `s3:ListBucket` on the bucket, bounded by `s3:prefix` to that shape, so a missing grant reads 404 and refuses, not 403 and raises. Decrypt is already this role's (`UseSystemKeyToDecryptTheTenantTablesAndDirectoryObjects`). The same two statements as `performance/render_grant.tf` for the adapter |
| D1 | `module.irpt_status.aws_lambda_function.this` | code `6VQejBfs..` becomes `hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E=` (S3 `4CQOSM..` becomes `In5BnMbPSWafGWf16g4CasBPJRhM.Ykl`); env gains `IRPT_EVIDENCE_BUCKET` = core's `evidence_bucket` output, never typed |

**The bundle (U1, closed):**
- 49 members, every one at the pin. Built from a `core.autocrlf=false` checkout: row repinned `899b9cad63`; `grant.py` and
  `report_owner.py` registered in `files[]` `9b3e128a3b` after the parity check (ADHC_DRIFTD.002) refused them unlisted,
  before any upload.
- Uploaded 06:0xZ, 347,090 bytes, read back by version equal.
- `bundle_vs_live_census.py --zip`: 0 differ from the pin, 0 CRLF; every import-closure member is the pin's.

## 2. Every member changed since live `6VQejBfs..` (census: 46 identical, 1 changed, 2 added, 0 removed)

| member | commit | attributed to |
|---|---|---|
| `grant.py` (ADDED) | `6ff301a693` (staging only; blob `51785ed4..`) | **G3:** `served.render_ports_from_env()` imports it once the bucket is set. It is the same blob `irpt-performance-adapter` ships |
| `report_owner.py` (ADDED) | `6ff301a693` (staging only; blob `610982ce..`) | **G3:** the ports' third, read-only port (the retained report's owner), read only by the Enforcer's PROSPECT branch (IB-pr-293), which batch 175 intends to be reachable here. It is the same blob the adapter ships |
| `enforce.py` | `8d08ee54e4` | **IB-pr-302** (`2.0.0_SA_COO~P`'s worker, CTO batch 205): `RENDER_DELEGATE_OPERATIONS` gains `reporting_read`, the 49F reporting route, which irpt-status does not serve. `_delegate_path_ids` translates ids ONLY for that operation and returns every other operation's ids unchanged. A render decision's record gains `bundle_id` beside its counts. It rides because `_authz` is shared |

`reports/repository.py` was already a member; nothing about it changes.

## 3. Proofs

**At the pin, offline:**
- The cold-start smoke of the BUILT zip, with the planned `IRPT_EVIDENCE_BUCKET` set (`--env`;
  `ZIP_COLD_START_SMOKE_G3_20261003.txt`): PASS on `status/{jobId}`, `analysis/{jobId}/sections`, the request read and
  history. Each has the owner-refusal arm named. History's `UNEXPECTED` is live's own answer (measured on `wXzz3` in the
  W2-06 packet).
- `RENDER_PORTS_AT_PIN_20261003.txt`: with the bucket set, `render_ports_from_env()` returns the ports, and `grant` and
  `report_owner` import from the zip. Without it the answer is `None` (the control; hop 11's at-pin verdict was `NONE`).

**Before the apply (live, recorded 06:0xZ):** `READS_BEFORE_G3_W206SHAPE_20261003.json` and
`READS_BEFORE_G3_E7BSHAPE_20261003.json`, two accepted requests (tenant cottonwood):
- history, history with client, read, read with comparisons, read with composition (sha256 per request), the duplicate
  include (refused), and status (`ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE`).

**After the apply (V1), batch 175's three arms:**
1. **Every non-render read equal to live, key for key:** both instruments re-run with `--compare` to the before files.
2. **A render token for another report refused (negative arm).** This needs a render token: the render key
   (`opal/auth/irpt-render-jwt-private-key`) and a frozen bundle. The grants that exist today are 3 Performance exports
   (`exr_` on `shl_`, 49financial). Presented to irpt-status's `status/{jobId}` or `sections` for an Analysis job, any
   such token must refuse (`OBJECT_NOT_COVERED`). **The carrier of this arm is asked of the CTO half:** this seat mints one
   token from an existing frozen bundle with the render key read by name, or `2.0.0_SA_COO~P`, the render identity's
   owner, runs it.
3. **A RENDER_DELEGATE read of status and sections for one real Analysis export (positive arm):** none exists. Census of
   `firms/*/generations/exr_*/render_grant.json`: 3 grants, all Performance. E4's packet waits on G3, so this arm runs
   at E4's first Analysis export print.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:** irpt-status `6VQejBfs..`, with no `IRPT_EVIDENCE_BUCKET`; the key's latest `In5BnMbP..`; no policy named
   `irpt-status-render-grant-read-policy`.
3. **I1:** a targeted plan of the policy (re-planned if stale), ONE `HALT_ACK=1 safe-apply`, and the policy read back.
4. **D1:** a targeted plan of the function (code + env), ONE `safe-apply`. Read back CodeSha256 `hC6Pramt..` and the env
   names. A live empty-headers invoke must answer `CONTRACT_VERSION`, with no FunctionError.
5. **V1:** arm 1; arm 2 by the ruled carrier; arm 3 at E4.

## 5. Rollback

- **D1:** re-promote S3 `4CQOSM.R8WDlZQ.ts0HCSiH2JkA6jqQ8` and drop the variable, then a targeted apply. The code returns
  to `6VQejBfs..` and the ports to `None`.
- **I1:** delete the policy.

## 6. Not claimed

- That the Analysis print renders: that is E4 (arm 3).
- G4, the download route: `~P`'s, ruled separately in batch 175.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~06:1xZ, on this packet's bytes at the commit that carries it. The write set is one new IAM policy (two
read statements) and one Lambda code and env update. The blast radius is section 2. The rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
