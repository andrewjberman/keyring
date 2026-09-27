# CTO half -- UI walk WINDOW 14: K8, the first real export, re-cut on the fixed submit (packet blob 423314f1) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~14:5xZ. **Request:** 2.0.0_SA_COO~P msg 101920.

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W14_K8_EXPORT_20260927.md`
@`a68848d634`, blob `423314f1`. Read at HEAD: `git hash-object` equals `git rev-parse a68848d634:<path>`.

**The base text:** window 12, blob `36c196ed` (CTO half @`0fe93a1b92`), itself window 10's `a15c2ffb`, re-hashed at HEAD.

## What was read

- The file was diffed against window 12. Only the page pin moves, to local DEV `55bbdd71`, which carries:
  - TO-IV-e-53, the preview;
  - TO-IV-e-64, the submit, receipt and download carrying selectedTenant. It is complete @`b56568b53c` (IVE64-AC1
    PASS-by-output, proof-of-spec VALID) and closes row S23.
- Window 12's refusal (UNEXPECTED, BucketUnmapped) came from the submit omitting `selected_tenant`, and IV-e-64 is that
  fix.
- K7/K8, the route classes, the interval, and every signing condition carry verbatim: no download body in the HAR, no
  PDF, PNG or HAR in git, the served-object audit, and the byte-proof.
- **Numbering:** this is window 14, and the next Analysis attempt is window 15.

## Named item

None new.

**CTO half: SIGNED on blob 423314f1.** The CRO half is separate.
