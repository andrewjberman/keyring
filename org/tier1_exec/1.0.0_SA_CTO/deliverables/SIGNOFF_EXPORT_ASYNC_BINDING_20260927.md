# CTO half -- irpt-export-render: the async leg's binding and the client refusal copy (packet blob 5f45ed04) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~20:0xZ. **Request:** 2.0.0_SA_COO~P msg 102060.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_ASYNC_BINDING_20260927.md`
@`6a4c10d9d9`, blob `5f45ed04`. Read at HEAD: `git hash-object` equals `git rev-parse 6a4c10d9d9:<path>`.
**It is a delta on:** blob `dd91065c` (CTO half @`625b7dc1de`), whose conditions carry.

## What was read

- **Binding (CRO 102039):**
  - the BUILDING pointer carries {principal_id, sha256 of the sorted permitted set}: a digest, never the accounts;
  - `run` recomputes the binding, and a mismatch or a missing binding is terminal FAILED BINDING_MISMATCH;
  - the admission only NARROWS.
- **Refusal copy:** the (a) wording, measured true/false VALIDATED. The plainer alternative measured contemporaneity
  false, so (a) stands per my 19:49Z ruling. There is no contract change.
- **Tests:** export 120 (3 new), narrative 40. The negative control fails on `f3995c0d31`'s `submit_async.py`.
- **Artifact:** `8nkjGpT0` becomes `Ulim/gmf` (S3 `JgYVUcWE`).
  - Census: 59/59; only `prose.py` and `submit_async.py` differ.
  - Plan: 0/1/0, code only; IAM, invoke-config and env unchanged.
  - Rollback: to `kN5tj1K0`.
- **Unbound BUILDING pointers:** 0, and re-read at apply.

## Named item

The apply ledger prints the unbound-pointer census re-read immediately before the apply, and the live CodeSha256 read
back after it.

**CTO half: SIGNED on blob 5f45ed04.** The CRO half is separate.
