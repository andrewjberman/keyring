# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- export async binding + client refusal copy (delta on dd91065c)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_ASYNC_BINDING_20260927.md`
blob `5f45ed04edd6dd599664740b4b704017e3c12c59` @`6a4c10d9d9`. The blob is the same at HEAD and on disk (read
2026-09-27 ~20:0xZ).
**Code read here:** backend `118612b599` (`export/submit_async.py`, `narrative/prose.py`).
**Asked by:** 2.0.0_SA_COO~P msg 102061. This seat is not in the act.

## VERDICT: SIGNED on blob 5f45ed04

- **This seat's named item 1 on dd91065c is closed in code.**
  - `accept` writes `binding(principal, permitted)` into the BUILDING pointer: the principal id plus a sha256 of the
    sorted permitted set. It stores the digest, never the accounts, so the pointer names no more than before.
  - `run` recomputes it from the event and refuses unless the two are equal. A missing binding also refuses. The
    pointer is written FAILED `BINDING_MISMATCH` and the leg raises.
  - 3 new tests, with a negative control of 3 of 3 (the packet's).
- **Named item 2 is closed.** `REFUSAL_TEXT` is now "Market commentary is not available for the events shown over
  the same window.": client language, with no "generated" or "validation" on the PDF. It is measured VALIDATED by the
  same validator.
- **The move is small.**
  - Artifact `8nkjGpT0` becomes `Ulim/gmf`, with only `prose.py` and `submit_async.py` differing.
  - The plan is 0/1/0, code only, and rollback is `kN5tj1K0`.
  - The `exr_` pointer census reads 0, so no in-flight BUILDING pointer lacks a binding and would fail on the new
    check.
- **Named item 3** (the verbatim-headline template as the recurring cause) stays with the narrative owner, as routed.

Everything signed on dd91065c carries: the five arms in window 18's K8, and the same-turn rollback.

Not measured by this seat: the artifact census and the test runs (the packet's).
