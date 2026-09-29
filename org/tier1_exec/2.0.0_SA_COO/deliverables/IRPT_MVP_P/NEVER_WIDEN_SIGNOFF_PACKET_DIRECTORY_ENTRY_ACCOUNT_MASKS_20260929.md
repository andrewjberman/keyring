# Never-widen sign-off packet -- DirectoryEntry `account_masks` (AD-10) in the two functions that package it

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~13:2xZ.
**Asked by:** `2.0.0_SA_COO~M` 102808. This is step 1 of the release order in ~M's COO half @1a031f514d:
1. ~P deploys the contract copy (this act);
2. portal PROD reads 27eae57a (2.0.0_SA_COO~D);
3. the directory re-mint;
4. the Holdings re-mint.

**Ledger:** `irpt-directory-entry-account-masks-20260929` (U1 closed; D1 and A1 open).

## 1. What ships

The docs contract `docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` at 4ecbaca410 (blob 27d9a8f7), which
adds one OPTIONAL property, `account_masks`. It is an array, one item per account in `ids.account_ids`, each item
`{account_id, masked_discriminator}`, `additionalProperties: false`. Nothing else in the contract changes, and nothing
becomes required. The lambda-tree copy is already this blob (TO-IB-pr-231 @67d595b021).

| function | live -> new | S3 version | census vs live |
|---|---|---|---|
| irpt-directory-search | `o1TXq5PH..` -> `s0riHZ9h..` | `2RmObc9v0Wj4o3f_2PLOrYWgAWzu8mEh` | 20 -> 20; ONLY `contracts/DirectoryEntry.schema.json` |
| irpt-ycharts-generate | `wnt7hjAB..` -> `inrij6hL..` | `DWP1wKAI_ftLo9kcP3p_LC6vV1V2K6W2` | 111 -> 111; ONLY `contracts/DirectoryEntry.schema.json` |

The source map re-pins both DirectoryEntry rows (69144433df and 19d8f3038c) to 4ecbaca410. The generate resident-side
modules stay pinned to their live blobs.

## 2. Who reads the file -- both branches

- **irpt-directory-search reads it on the served path.** `entry.py:71-87` `_document_fields()` takes the search
  response's field set from the contract's `properties`, found through `IRPT_CONTRACTS_DIR=/var/task/contracts`.
  - After the act, a search answer carries `account_masks` on any entry document that holds it.
  - **Today no served entry holds it.** Read with the built handler's own `load_directory` under the function's
    environment: 49F 4,620, COT 258 and INF 292 entries; 0 carry `account_masks`, and 0 are invalid under either the
    live or the new copy.
  - So the wire is unchanged until ~M's directory re-mint (step 3), which the release order places after portal PROD
    reads the field (step 2).
- **irpt-ycharts-generate never validates a directory document.** DirectoryEntry is referenced by no schema in either
  zip. The file feeds only the two glob loaders named in `HOLDINGS_CONTRACT_GENERATE_READER_TRACE_20260929.md`
  (@1c9519d4a6):
  - The ingestion-revision digest moves from `schemas-4780eaf85be2..` to `schemas-cb6e1c3c3b75..`. New acceptances
    record the new string. Retained requests are unaffected, because the read checks only for a non-empty string
    (`owned_requests.py:92-93`).
  - The admission Registry loads one more property.

## 3. Apply protocol

Ordering: **after window 22 closes.** Both functions are W22 pins (ledger `irpt-ui-walk-principal-w22-20260929`).

1. Both halves at HEAD naming this file's blob.
2. BEFORE: the three-firm directory validation of section 2 under the live copy.
3. The S3 latest version of each key equals section 1's at apply, written in the ledger. Fresh plans are code-only
   (directory root, ycharts root); safe-apply each (halt gate; HALT_ACK=1 only on 0 STOP items).
4. Read back each CodeSha256; the deployed zips member-equal to the artifacts; re-plan both: No changes.
5. Deployed invokes on a fresh container:
   - irpt-ycharts-generate: a refused POST, which builds the ports and the digest, plus the import census;
   - irpt-directory-search: an API-shaped refused request, which proves the cold start. Its `_document_fields` read
     is exercised by the first signed-in search, so the AFTER read is a directory search on one firm through the page.
6. AFTER: section 2's validation under the deployed copy, and one signed-in directory search on one firm. Its
   response carries no `account_masks` and the same fields as before.

**Rollback per key:** irpt-directory-search -> the S3 version of `o1TXq5PH` restored as latest, then re-apply;
irpt-ycharts-generate -> `GP__8T1n` (`wnt7hjAB`) restored as latest, then re-apply.

## What the halves sign against

This file's committed blob; 4ecbaca410's blob 27d9a8f7; the two artifacts of section 1; section 2's reads; the apply
protocol of section 3.
