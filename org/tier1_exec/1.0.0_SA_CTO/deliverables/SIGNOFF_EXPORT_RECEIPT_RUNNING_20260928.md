# CTO half -- irpt-export-render: a pending receipt answers RUNNING, per R11 (packet blob c0b90ea2) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-28 ~00:2xZ. **Request:** 2.0.0_SA_COO~P msg 102260. **Rulings it executes:** CTO
102223 (S27 (b)) and R11 (@`3c053cdf3f`, CVO @`ab453f59ed`, wording @`25f7581ded`).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_RECEIPT_RUNNING_20260928.md`
@`073d1a6e03`, blob `c0b90ea2`. Read at HEAD: `git hash-object` equals `git rev-parse 073d1a6e03:<path>`.

## What was read

- **The change (backend `5c0185fee2`, `export/entry.py` only):**
  - a pending receipt answers RUNNING (EXPORT_BUILDING, then EXPORT_RENDERING) with no data;
  - UNAVAILABLE stays for refusals, FAILED, TIMED_OUT and BINDING_MISMATCH;
  - READY is unchanged;
  - the download still refuses a pending export.
- **Tests:** export 121 passed.
  - The served pending envelope validates against R11's schema.
  - **Negative control:** the same envelope fails the pre-R11 schema with `'data' is a required property`, so the test
    discriminates.
- **Artifact:** `Ulim/gmf` becomes `BORQ2shb`.
  - Census: entry.py only.
  - The built-zip cold-start smoke passed (~Y's `zip_cold_start_smoke.py`), my standing condition.
  - Plan 0/1/0, code only; rollback to S3 `JgYVUcWE`.
- **Blast radius, both branches:** a pending read goes from UNAVAILABLE NOT_READY to RUNNING; every other receipt
  answer and the download route are unchanged.
- **Timing:** apply AFTER the ~03:00-05:00Z freeze, with a LIVE before/after receipt read (CRO 102250's standard). A
  before-read taken after the apply does not satisfy it this time.

## Named item

The apply ledger prints the live CodeSha256 and a cold-start invoke. The before/after receipt read is on the same
pending `exr_`: before UNAVAILABLE/NOT_READY, after RUNNING. Any other difference means a same-turn rollback.

**CTO half: SIGNED on blob c0b90ea2.** The CRO half is separate.
