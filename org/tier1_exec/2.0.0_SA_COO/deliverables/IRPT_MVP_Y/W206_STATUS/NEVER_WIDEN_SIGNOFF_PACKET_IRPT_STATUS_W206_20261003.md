# Never-widen sign-off packet -- irpt-status: W2-06 `include=composition`, with the Y-5 correction words attributed, code at ONE commit `ac1a847617`

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~04:1xZ.
**Authority:**
- CTO rulings batch 165, ruling 3: "W2-06's backend half (the owned-request read carries the composition to refill) goes to
  `2.0.0_SA_COO~Y`'s queue ... It is OPT-IN (`include=composition`, batch 142's pattern), so PROD's strict parser is
  unchanged."
- Batch 198: "The next irpt-status packet attributes the two new `ops/status.py` entries."
- Batch 148's rule: every changed member attributed.

**Ledger:** `irpt-status-w206-20261003`, opened at the start (03:49Z), before the upload. U1 is closed; D1 and V1 are open.
**One move:** D1, the code of `irpt-status`. No IAM, route, table, queue or other function moves. No vendor call.

## 1. What ships

| move | resource | change (`W206_STATUS/plan_d1_w206.txt`; full ops plan `plan_ops_full_w206.txt`: the same 1 change, nothing else) |
|---|---|---|
| D1 | `module.irpt_status.aws_lambda_function.this` (ops root) | `s3_object_version` `wXzz3_ghlWfn7pdM12GBxlzl_WOxYQUC` becomes `4CQOSM.R8WDlZQ.ts0HCSiH2JkA6jqQ8`; `source_code_hash` `h7H7KgX1..` becomes `6VQejBfsI/P3mfAVSFjLt/ythlcxXxi12cy9hxXhKNg=` |

**The bundle (U1, closed):**
- 47 members, every one at `ac1a847617` (row repinned `2be7ff7a54`). Built from a `core.autocrlf=false` checkout (S286).
- Uploaded 03:56:23Z, 338,660 bytes. Read back by version: the sha256 equals the build.
- `bundle_vs_live_census.py --zip`: 0 members differ from the pin, 0 carry CRLF, and every import-closure member is the pin's.
- Live `h7H7KgX1..` is S3 version `wXzz3_gh..`, which hashes to it (read 04:0xZ). That version is the rollback.

## 2. Every member changed since the live artifact (census: 41 identical, 6 changed, 0 added, 0 removed)

| member | commits | attributed to |
|---|---|---|
| `entry.py` | `7f1135f0ee` | **W2-06:** `include` is a comma list of distinct names from {comparisons, composition}. Any other value, empty token, duplicate, space or case variant refuses `INVALID_READ_INCLUDE`, as before. `include=comparisons` alone is unchanged |
| `owned_requests.py` | `7f1135f0ee` | **W2-06:** `_frozen_composition` returns a copy of the retained composition's `browser` half, the AnalysisSubmissionRequest that acceptance validated and froze. It never returns the resolved half. It is read through the SAME one retained read as the comparisons. A caller that asks for neither keeps the pre-E7 path key for key. A malformed browser half refuses `COMPOSITION_BROWSER_BINDING`, only for the caller that asked |
| `status.py` | `a42ad6b675` | **Y-5** (batch 198): `CORRECTION_WORDS` gains `TICKER_DATA_NOT_ENTITLED` and `TICKER_NOT_FOUND`. A status envelope in a correction state with either code now carries one `CORRECT` action with those words (none before). No other code or state moves. The locked copy in `intake/uploads.py` is not an irpt-status member |
| `maintained_sources.py` | `bb255c4cb2` | **Y-3:** a comparison key that no model holds but the etf-classifications table names is admitted, ONLY when a `read_classifications` port is passed. No irpt-status member passes one: the generate and prospect routes do. Here `_classified_etf(key, None)` is None, so an unknown key refuses with the same message as before. Import adds `re` (stdlib) |
| `infra/logic/registry/reporting_policies.json` | `b77e2af4d5` | **4.0.0_SA_CRO**, X10 / IRPT_DASHBD-S12: the PENDING policy `irpt-dashbd-x10-v1` gains two families. The ACTIVE `irpt-x10-v1`, the one this function resolves, is byte-equal; its `policy_sha256` is pinned by a test. It rides because the registry is shared |
| `lib/opal_naming.py` | `b77e2af4d5` | **4.0.0_SA_CRO**, the same commit: the registry validator admits a family naming one fixed served object, and `_reporting_destination` refuses such a family. `irpt-x10-v1` has none, so every address this function builds is unchanged. `lib/tests/test_irpt_destination.py` 72 passed at the pin |

**The contract** (not a bundle member): `OwnedAnalysisRequest.schema.json` gains an optional `composition`, a `$ref` to
`AnalysisSubmissionRequest.schema.json`, so a field that contract does not declare is invalid. `routes.json` describes the
include list. Additive: a caller that does not ask receives no new key.

## 3. Proofs

**Before the apply (live, recorded):** `W206_STATUS/READS_BEFORE_W206_20261003.json` (04:0xZ, tenant cottonwood, two
accepted requests), the live answer today:
- plain read and `include=comparisons` answer (HTTP 200);
- `include=composition`, `include=comparisons,composition` and `include=composition,composition` are each refused
  `INVALID_INPUT`.

**Offline at the pin:**
- ops 238 passed, 22 skipped. The new W2-06 tests cover the reader (a copy; three broken browser halves refuse only the
  asking read; history items omit it), the entry (both orders, ten refused queries), and the paired fixture
  `read_with_composition`, generated by the actual reader and validated against both contracts.
- `_contracts` 185, `_scope` 207, `reports/test_status_installed` 4, `reports/test_retention` 18 and
  `lib/tests/test_irpt_destination` 72: all passed.
- Negative control: on HEAD's two modules (before W2-06), the 2 new behaviour tests fail.
- Cold-start smoke of the BUILT zip (`ZIP_COLD_START_SMOKE_W206_20261003.txt`): PASS on the request read, history and
  PDF routes, each with the owner-refusal arm answering a named refusal. The history arm answers `UNEXPECTED`; the
  same smoke on live `wXzz3` (= `h7H7..`) answers the same, so this packet does not cause it.

**After the apply (V1):** `live_walk/w206_read_proof.py` on the same two requests, with `--compare` to the before file.
- Plain and `include=comparisons`: equal to before, key for key.
- `include=composition` and `include=comparisons,composition`: answer HTTP 200 with `composition`. Its key names lie
  within the AnalysisSubmissionRequest's, and the composition sha256 is equal across the two reads.
- `include=composition,composition`: still refused.

A composition is recorded by key names and sha256 only, never by value: it carries a client's display text.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:** irpt-status `h7H7KgX1..`; the key's latest `4CQOSM..`; the targeted plan still exactly this one change.
3. **D1:** ONE `HALT_ACK=1 safe-apply` of `w206_d1.tfplan`, re-planned if stale. CodeSha256 read back `6VQejBfs..`. A live
   empty-headers invoke must answer `CONTRACT_VERSION`, with no FunctionError.
4. **V1:** the after-read above. Then one line to `2.0.0_SA_COO~D` (the W2-06 front half): the field is live.

## 5. Rollback

- **D1:** re-promote S3 `wXzz3_ghlWfn7pdM12GBxlzl_WOxYQUC`, then a targeted apply. The code returns to `h7H7KgX1..`.
  Nothing else moved.

## 6. Not claimed

- The W2-06 front half (the composer refill) is `2.0.0_SA_COO~D`'s. This packet serves the read it consumes.
- A refill must submit a NEW `request_id` (contract description). This packet does not enforce that on the browser.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~04:1xZ, on this packet's bytes at the commit that carries it. The write set is one Lambda code update.
The blast radius is section 2. The rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
