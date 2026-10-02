# Never-widen sign-off packet -- irpt-status at ONE commit `ff8fd77ba2`: E7b (comparisons only on include=comparisons) + E6 (the read memo) + item 22 (history by client)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~11:0xZ.
**Authority:** CTO rulings batch 142 (E7b; the queue no longer waits on the portal PROD promote) and batch 146 @11340658da
(ONE packet at one CLOUD commit for E7b + E6 + item 22). Batch 146's conditions are met in sections 1 to 4:
1. the packet names its one commit and the bundle hash;
2. every member changed since the live artifact is attributed;
3. each piece is proven separately;
4. the live artifact is the one-act rollback.

This packet SUPERSEDES E7's held packet (blob `cc3ecd9fbb`, ledger `irpt-status-e7-20261001`). E7's artifact is no longer the
key's latest version. **Ledger:** `irpt-status-e7b-20261002` (U1 proven; D1, V1). **One move:** a targeted apply of
`module.irpt_status.aws_lambda_function.this`. No IAM, route, table, schema or other function moves. No vendor call.

## 1. The commit and the bundle

| | |
|---|---|
| members at | `ff8fd77ba2` (CLOUD). The source-map row was repinned to it at `d3a8136304` (all 40 staged entries; 226 other rows unchanged) |
| built zip | S3 `opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip` version `Jg3uJ0x7mOrlV1MbGUp.KUNlmzfHlFsX` (uploaded 10:47:58Z), 330,611 bytes, sha256 (base64) `X/JLmPJZSDlexI7+AEGShnMU0ilrep3hnT9Vt6UsooE=`, 46 members. Read back by version: the sha256 is equal. `bundle_vs_live_census.py --zip`: 0 members differ from the pin's bundle; 0 carry CRLF |
| live | CodeSha256 `2V7xV1+zII4+g6tV722Tk5M9LWJFMzLShyjq6Q+v/J4=` since 2026-10-01T06:59:55Z = S3 version `m1LolBKFxtfUUbodMML8ZuM.Wfo6Op.C` (the downloaded live zip hashes to it) |
| targeted plan | `E7B_STATUS/plan_ops_targeted.txt`: 1 to change. `s3_object_version` `m1LolBKF..` becomes `Jg3uJ0x7..`; `source_code_hash` `2V7xV1..` becomes `X/JLmPJZ..`; `last_modified`. Nothing else |
| served closure | `served.py` and its 14 imports are identical to live (15 of 15) |

## 2. Every member changed since the live artifact, attributed (census at the pin against live: 36 identical, 9 changed, 1 added, 0 removed)

| member | commits the pin adds over live | attributed to |
|---|---|---|
| `entry.py` | `c4210d2785`, `f27418381d` | E7b (the read admits `include=comparisons`); item 22 (history admits `client_id`) |
| `owned_requests.py` | `c4210d2785`, `f27418381d`, `4c23ef5d98`, `8c4398e32a` | E7b, including E7's `_chosen_comparisons` (`8c4398e32a`, ratified by batch 105, byte-identical since); item 22; E6 (`_fresh_reads` around `_final`) |
| `owned_report.py` | `4c23ef5d98` | E6 (the post-read recheck reads fresh) |
| `prospect_dates.py` | `4c23ef5d98` | E6 (`final` reads fresh) |
| `status_installed.py` | `0d6ec02cd0` | E6 (the memo over the table port; one scope per invocation) |
| `read_memo.py` (ADDED) | `4c23ef5d98` | E6 |
| `durable_job.py` | `7122afefc1` | **outside the three:** item 16 (row S253, `append_vendor_requests`, a write method the status reads never call). Already in E7's signed bundle at `b1db201025` |
| `status.py` | `951afdf4e6` | **outside the three:** item 19 (`RESOLVE_PROVIDER_BUSY`'s words in `CORRECTION_WORDS`). st11's half: the words "ride the next generate and irpt-status bundles" |
| `infra/logic/registry/reporting_policies.json` | `11bf813387` | **outside the three:** the registry row st11's packet read (`reporting_policy("irpt-x10-v1")` digest `e0046398..`, equal to the live registry's and to every request's `destination_policy_revision`, as the live reads print) |
| `org/standards/NAMING_SCHEMA.json` | `aa2b5a42ff` | **outside the three:** one cadence token, read by `opal_naming` (st11's packet) |

**The four outside the three were put to the CTO at 10:50Z (msg on batch 146's condition). This packet does not apply
until that ruling admits them or names what to drop.**

## 3. Each piece, proven separately

**Before the apply, read live** (`E7B_STATUS/READS_BEFORE_20261002.json`; `live_walk/e7b_read_proof.py`; one login as
`svc-irpt-analysis`, GETs only, 10:5xZ):

| call | live answer |
|---|---|
| read, Overview `REQ-a69e5751d42c374f1d2354f9` | 200, `{accepted_at, identity}` (values recorded) |
| read, Multi-Comp `REQ-a1d9abc0bc037ea3d9e4a7ed` | 200, `{accepted_at, identity}` (values recorded) |
| read with `include=comparisons`, both | refused `INVALID_INPUT`: the served read admits no parameter but `selected_tenant` |
| history (no `client_id`) | 200, `{items, next_cursor}` (values recorded) |
| history with `client_id` | refused `INVALID_INPUT` |
| status, both (no dates header) | 200, `state UNAVAILABLE`, `ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE`, keys recorded |

**E7b:**
- WITHOUT the parameter, the read takes the pre-E7 path, `_materialize`, `_final`, `_public`: the live code's own path,
  so the answer is `{identity, accepted_at}` key for key. Tests: the entry read without `include` equals `_public`;
  with it, only `comparisons` is added; 4 refused queries.
- WITH it, the names come from `_chosen_comparisons`, byte-identical to E7's. Run at the pin over every accepted request
  (`E7B_STATUS/COMPOSITION_CENSUS_E7B_20261002.txt`): 22 of 22 derive, 0 refuse. **Multi-Comp:
  `[{"key": "opal_short_term", "label": "Opal Short-Term"}, {"key": "opal_intermediate_term", "label": "Opal
  Intermediate-Term"}]`, in key order; Overview: `[]`.**

**Item 22:** without `client_id` the history query and page are unchanged; with it, items are filtered by the frozen
selection (10 tests). All requests read so far are upload-lane (client `null`).

**E6:** the memo changes no shape. It answers repeated identical `get_item` calls within ONE invocation, and the final
re-reads are fresh (6 tests, two negative controls).

**After the apply (V1)**, the same tool with `--compare READS_BEFORE_20261002.json`:
- every plain call must be equal key for key and value for value: both reads, history, both statuses by key names;
- the include reads must answer and name exactly the comparisons above;
- history with an unknown `client_id` must answer `items: []`.

Any plain call unequal is the rollback trigger.

**Suites at the pin:** ops 208 passed, 22 skipped; `_contracts` owned-request 3, seam 62, selection 2, upload 8; `_authz`
guarded 32. `_authz/tests/test_unguarded_census.py` fails 6 on CLOUD too (row W98-S1, parked; not this change).

## 4. Apply protocol and rollback

1. Both halves at HEAD naming this file's blob, and the ruling on section 2's four members.
2. **Before-read:** live CodeSha256 `2V7xV1..`; the key's latest version is still `Jg3uJ0x7..` with sha `X/JLmPJZ..`.
3. **D1:** a fresh targeted plan of `module.irpt_status.aws_lambda_function.this` showing exactly section 1's change;
   ONE `HALT_ACK=1 safe-apply` of it.
4. **V1:** live CodeSha256 `X/JLmPJZ..`; section 3's after-read and compare; then E7's ledger legs close as superseded.
   `2.0.0_SA_COO~D` may add `include=comparisons` to the DEV page ONLY after V1: before it, the parameter is refused.
5. **Rollback, one act:** a targeted apply of the function back to S3 version `m1LolBKFxtfUUbodMML8ZuM.Wfo6Op.C` (code
   `2V7xV1..`), the live artifact. The function holds no state.

## 5. Not claimed

- That E6's memo makes the page fast enough under the 15 s timeout; its effect is measured at V1, not promised.
- The Cottonwood cap (20) lifts per batch 132 when E6 serves, which is this apply.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~11:0xZ, on this packet's bytes at the commit that carries it. The write set is one function's code
version. The blast radius is section 2's ten members, each attributed, with four awaiting the ruling. The proof is
section 3. The rollback is section 4 step 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
