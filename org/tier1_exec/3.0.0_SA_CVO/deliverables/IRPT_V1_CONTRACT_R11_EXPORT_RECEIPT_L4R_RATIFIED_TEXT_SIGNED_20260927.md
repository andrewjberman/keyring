# L4-R review -- IRPT v1 contract, ruling R11: export-receipt response (`3.0.0_SA_CVO`)

**Asked by:** 1.0.0_SA_CTO msg 102226. **Object:** `docs/contracts/investor-reporting/v1/responses/export-receipt.response.schema.json`
@`3c053cdf3f`, blob `e241d449168b871d89929cd8a172f8aeea2f25e7` (re-read with `git rev-parse`; matches the ask). **Half:** ratified-text.
**Cause:** DSGN_IRPTV1-S27 (a pending receipt has no sha256 or page_count yet).

**Verdict: SIGN.** The change says what the ruling says, the enforced logic is R2's, and no state other than QUEUED and RUNNING moves.
Two prose lines are stale (below). They are wording, not the rule, and are owed at the next touch; they are not conditions of this sign.

## What changed (the whole diff, 4d45502659 -> e241d44916)

- `data` leaves the top-level `required` list.
- One `allOf` entry: if `status.state` is QUEUED or RUNNING, nothing more is required; else `data` is required.

## Checks (Draft 2020-12, `jsonschema` 4.26.0, every v1 `*.schema.json` in the registry)

| check | result |
|---|---|
| `check_schema` on the blob | OK |
| the `allOf` logic against R2's live block in `submit-export.response.schema.json` (descriptions removed) | byte-equal |
| QUEUED and RUNNING, no `data` | 0 errors each |
| READY, PARTIAL, STALE, UNAVAILABLE, NEEDS_CORRECTION, UNCERTAIN, FAILED, no `data` | `'data' is a required property` in each (7 of 7); the state list is PublicStatusEnvelope's nine, exhaustive |
| no `status` at all, no `data` | `data` required (the `if` needs `status`, so the rule fails closed) |
| QUEUED with a `data` that is not a receipt (`{}`) | refused (7 errors): a present `data` is still a whole ExportReceipt |
| positive control: the pre-R11 shape (no `status`, the `ExportReceipt.valid.json` fixture instance) | 0 errors -- nothing valid before is invalid now |

## Owed at the next touch (wording only)

1. The file's own top-level `description` still reads the envelope as `{contract_version, operation, firm_id, data, status?}`, with `data`
   unconditional. R2 updated submit-export's description ("while status.state is QUEUED or RUNNING the receipt does not exist yet and
   `data` may be absent"); this file needs the same sentence.
2. `docs/contracts/investor-reporting/v1/CONTRACT.md:192` still says `"data": { ... }, // REQUIRED`. It has been stale for
   submit-export since R2 and is now stale for export-receipt as well. A consumer that reads it expects `data` on every answer, which is
   the page failure S26 recorded.

## Observation

R2 landed with a test (`infra/aws/lambda/investor-reporting/_contracts/tests/test_submit_export_queued.py`). R11 has none. The grid above
is that test's shape for export-receipt, if the producer seat wants it pinned.

## Attribution note

The ask calls R2 "your signed R2". This seat's git history holds no sign of R2 (`git log --author=3.0.0_SA_CVO`, 2026-09-24 onward, no
R2 or submit-export commit). R11 is signed here on its own bytes, not on that premise.

-- `3.0.0_SA_CVO`, 2026-09-27 ~23:5xZ
