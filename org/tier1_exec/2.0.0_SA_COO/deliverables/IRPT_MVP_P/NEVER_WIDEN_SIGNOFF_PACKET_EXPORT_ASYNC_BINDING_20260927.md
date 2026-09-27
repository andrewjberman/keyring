# Never-widen sign-off packet -- irpt-export-render: the async leg's binding, and the client refusal copy

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~20:0xZ.
**Asks it answers:** 4.0.0_SA_CRO 102039 (bind `run` to what `accept` authorized); 1.0.0_SA_CTO 102041 item 1 and
102044 (a) (client refusal copy). **Ledger (opened before any write):** `irpt-export-async-binding-20260927`
@e816dc6cec (U1 closed, D1 open).

This is the async-submit packet (`NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_ASYNC_SUBMIT_20260927.md`, blob dd91065c, both halves:
CTO @625b7dc1de, CRO @db22c99603) with ONLY the deltas below. Its blast radius, arms and rollback pattern stand.

## A1 -- the change (backend 118612b599; publish e861ec930c)

- **Binding.** `submit_async.accept` writes `binding = {principal_id, sha256 of the sorted permitted account set}` into
  the BUILDING pointer: a digest, never the accounts. `run` recomputes it from the event. On a mismatch, or on a
  pointer with no binding, it writes FAILED with reason `BINDING_MISMATCH` and refuses. That is terminal, like every
  other exit (102031 condition 2).
- **Refusal copy.** `prose.REFUSAL_TEXT` = "Market commentary is not available for the events shown over the same
  window." Measured: states_contemporaneity true, asserts_causation false, VALIDATED. The 102041 sentence and the
  102044 alternative both measure states_contemporaneity false, so 102044 rules this (a) wording. No contract change.
- **Tests:** export 120 passed (3 new: two tampered events refused and terminal with nothing built; the pointer carries
  a digest, order-free); narrative 40 passed. Negative control: the 3 new tests fail on f3995c0d31's
  `submit_async.py`.

## A2 -- the artifact and the move

| | live | new |
|---|---|---|
| irpt-export-render CodeSha256 | `8nkjGpT0..` (S3 version kN5tj1K0.) | `Ulim/gmf..` (S3 version JgYVUcWE.) |

- **Census:** 59 -> 59 members; ONLY `prose.py` and `submit_async.py` differ. The flat extract-and-import passes.
- **Dry plan:** 0/1/0, code only (s3_object_version, source_code_hash). IAM, the event-invoke-config (retries 0) and
  the env are unchanged.
- **Rollback:** re-apply at S3 version kN5tj1K0. (8nkjGpT0).

## A3 -- blast radius delta

- **The async leg's admission narrows:** it now builds only when the event reproduces `accept`'s principal and
  permitted set. Nothing a caller can reach widens.
- **BUILDING pointers written by 8nkjGpT0** carry no binding and would read BINDING_MISMATCH under the new code. The
  census of such pointers is 0: no POST has reached the served async code (no walk window since 19:43Z). It is
  re-read at apply.
- **Withheld narrative:** the PDF's commentary slot reads the client sentence instead of naming validation.

## What the halves sign against

This file's committed blob; backend 118612b599 (publish e861ec930c); artifact Ulim/gmf at S3 version JgYVUcWE with its
0/1/0 plan and rollback; the async-submit packet's arms, run in the next K8 window on THIS artifact.
