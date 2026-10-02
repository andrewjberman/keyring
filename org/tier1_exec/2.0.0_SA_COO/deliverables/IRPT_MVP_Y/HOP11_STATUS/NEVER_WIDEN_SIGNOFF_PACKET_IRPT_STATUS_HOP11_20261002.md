# Never-widen sign-off packet -- hop 11: the vendor PDF link on irpt-status (IAM line, code at ONE commit `38986d35bb`, the API route), with item 22 served and the batch 154 guard

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~12:5xZ.
**Authority:**
- CTO rulings batch 123: hop 11, `GET analysis/requests/{requestId}/pdf` on irpt-status, an Opal-signed URL of at most
  300 s plus sha256; `vendor_documents` added to `irpt-status-policy` in `ops/iam.tf`, this seat's lane.
- Batch 154: the guard admits `client_id` on history only; item 22's proof re-runs at the served layer in this packet.
- Batch 163: the contract files, with census pins derived.
- Batch 148's rule: every changed member attributed.

**Ledger:** `irpt-status-hop11-20261002` (U1 proven; I1, D1, R1, V1). **Three moves, in order:** I1 the IAM line, D1 the code,
R1 the route (last, so no call reaches a function without the route). No table, schema migration, queue or other function
moves. No vendor call.

## 1. What ships

| move | resource | change (plans `HOP11_STATUS/plan_ops_full.txt`, `plan_api_full.txt`, read 12:1xZ-12:5xZ) |
|---|---|---|
| I1 | `aws_iam_role_policy.irpt_status` (ops root) | the retained-families read statement gains `irpt/{firm}/state/vendor_documents/*` on `opal-data-irpt` for the three registry firms (derived from `reporting_policies.json` by `local.vendor_pdf_family`, commit `dd6de6ced2`); nothing else in the policy moves |
| D1 | `module.irpt_status.aws_lambda_function.this` (ops root) | `s3_object_version` `Jg3uJ0x7..` becomes `9S5jAZLrUIb7OsqZW_jkSSc9HjI63f5E`; `source_code_hash` `X/JLmPJZ..` becomes `BNe2n9cV2tgsXE7pNy295NEhbiQsFM0VRE8OXeaolZU=` |
| R1 | `aws_apigatewayv2_route.irpt["GET /api/scoped/investor-reporting/analysis/requests/{requestId}/pdf"]` (api root) | ONE route created, target `integrations/8ogp332`, the same irpt-status integration as the request read. The full api plan: 1 to add, nothing else |

**The bundle:**
- 47 members, every one at `38986d35bb` (row repinned `f518096030`);
- uploaded 12:12:48Z, 335,359 bytes; read back by version with the sha256 equal;
- `bundle_vs_live_census.py --zip`: 0 members differ from the pin.

## 2. Every member changed since the live artifact `X/JLmPJZ..` (census: 41 identical, 5 changed, 1 added)

| member | commits | attributed to |
|---|---|---|
| `pdf_link.py` (ADDED) | `a41a349c8b` | hop 11: the signer, bound to the builder's destination, 300 s, host check |
| `entry.py` | `018a325a84` (merge of `a41a349c8b`) | hop 11: the PDF route in the owned Entry |
| `owned_report.py` | `018a325a84` | hop 11: `pdf()` -- READY receipt, retained artifact's sha256 binding, signer |
| `status_installed.py` | `b13bc47603` | hop 11: the installed declaration names the PDF route (without it `served.installed_entry` refuses the first call) |
| `served.py` | `2ad49400f8`, `7605bbf5ab` | the batch 154 guard (`OWNER_READ_QUERY_ALLOWLIST`: `client_id` admitted on analysis-request-history only), and IB-pr-293 (below) |
| `enforce.py` | `7605bbf5ab` | **IB-pr-293** (`~P`'s order, CTO batches 143-146): the Enforcer's prospect branch, taken ONLY when a loaded bundle carries a stored prospect scope. Such a scope exists only in export-render grants. irpt-status's owned reads load custody and owned-record scopes, so the branch is not reached here; `served.py`'s optional third port is not passed by irpt-status. `_authz/tests/test_guarded_entries.py` 32 passed at the pin. It rides because `_authz` is shared (`~P` msg 104221) |

## 3. Proofs

**Before the apply (live, recorded):** `E7B_STATUS/READS_AFTER_20261002.json` (11:1xZ) is the live answer today:
- plain reads `{accepted_at, identity}`, both requests;
- `include=comparisons` answers;
- history with `client_id` is refused (`INVALID_INPUT`), the guard not yet served;
- no `/pdf` route exists (API read 12:1xZ: the analysis routes list carries none).

**Offline at the pin:**
- ops 220 passed, including 12 `pdf_link` tests and 14 history-scope tests, 4 of them through the real `served.Entry`
  and guard: a filter is a subset of the plain page, an unknown client gives `items: []`, and `client_id` is refused on
  read, sections and status;
- reports `test_status_installed` 4 passed (six operations);
- `_contracts` 185 passed (the route and AnalysisRequestPdf contract, census pins derived);
- `_authz` guarded 32 passed.

**After the apply (V1):**
1. **Hop 11:** `live_walk/hop11_pdf_proof.py` on the READY requests `REQ-c07e64ca6c74b8e5310f56e0`,
   `REQ-59b42fab4293260d6d439c39`, `REQ-abec171d60e0aa1f359c18ed` and `REQ-a69e5751d42c374f1d2354f9`. Each must:
   - answer a URL on Opal's store (host printed, never the query);
   - expire in at most 300 s;
   - download a `%PDF-` body whose sha256 and length equal the route's claim.

   A request that is not READY must be refused by name.
2. **Item 22 served:** history with `client_id=no-such-client` answers `items: []`; with no `client_id`, it equals
   before.
3. **No regression:** `e7b_read_proof.py --compare READS_AFTER_20261002.json`. Every plain call must be equal; the one
   expected difference is history with `client_id`, which now answers.

Any plain call unequal, or a MISMATCH on the PDF, triggers the rollback.

## 4. Apply protocol and rollback

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - live CodeSha256 `X/JLmPJZ..`;
   - the artifact key's latest is `9S5jAZLr..` with sha `BNe2n9cV..`;
   - no `/pdf` route on API `7k3ed8px20`.
3. **I1:** a fresh targeted plan of `aws_iam_role_policy.irpt_status` showing only the three added resources; ONE
   `safe-apply`; the applied policy read back.
4. **D1:** a fresh targeted plan of `module.irpt_status.aws_lambda_function.this` showing only the code move; ONE
   `safe-apply`; CodeSha256 read back.
5. **R1:** a fresh targeted plan of the one route (1 to add); ONE `safe-apply`; the route read back on `7k3ed8px20`.
6. **V1:** section 3's after-reads. Then `2.0.0_SA_COO~D` may call the route, and the ledger closes.

**Rollback, per key:**
- R1: a targeted destroy of the one route.
- D1: a targeted apply back to S3 version `Jg3uJ0x7..` (code `X/JLmPJZ..`).
- I1: a targeted apply of the policy without the three resources.

Reverse order: R1, then D1, then I1. The function holds no state.

## 5. Not claimed

- That a portal page shows the PDF: `2.0.0_SA_COO~D` wires it after V1.
- IB-pr-293's behaviour in the export path: that is `~P`'s packet; here it is shown unreached only.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~12:5xZ, on this packet's bytes at the commit that carries it. The write set:
- one IAM statement's resources;
- one function's code version;
- one API route.

The blast radius is section 2's six members, each attributed, and the three moves. The rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
