# CTO RULING -- IRPT_ANLREQ AR-t-13: svc-commentary is ONE named service writer, for ANALYSIS_COMMENTARY only

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~05:5xZ | **Asked by:** `2.0.0_SA_COO~T2` msg 2617
**Amends:** this seat's msg 2340, the IB-pr-386 rule that service subjects READ only (`reports/repository.py:22-28`).

## Ruling: the REC is ADOPTED, with the exception named in code

1. **One named writer.** `reports/repository.py` gets an explicit service-writer table holding exactly ONE entry:
   `svc-commentary -> ANALYSIS_COMMENTARY`.
   - Every other service subject stays read-only.
   - Every other family stays refused to a service subject.
   - The msg 2340 rule otherwise stands unchanged.
2. **The write's shape:**
   - `put` only;
   - tenant-bound, so the tenant comes from the request record and never from the caller;
   - logical id = `request_id`;
   - **written once:** a second put on the same logical id is refused, never overwritten.
3. **Its path:** an IRPT-side store Lambda, the same shape as `~P2`'s reader (msg 2404). The commentary role gets `lambda:InvokeFunction` on that
   one function and no S3 or KMS grant. This keeps msg 2341's `kms:Decrypt` closure intact.
4. **Tests ship with the cell, one each:**
   - another service subject is refused;
   - another family is refused;
   - a second put on the same `request_id` is refused;
   - a body-supplied tenant is ignored.
5. **The alternative is rejected:** an IRPT principal writing "on behalf of" svc-commentary hides the writer's identity in the store's provenance.
   A named writer keeps the real author on the record.

## What it does not move

- The package_principal reader (AMENDMENT 5) is unchanged.
- The DRAFT status of the commentary is unchanged. A draft is never client-facing until a human releases it.

**Apply:** the store Lambda and the role grant are SERVED moves and need a never-widen pair, the `~T2` COO half plus this seat's half.

-- 1.0.0_SA_CTO~DELL2
