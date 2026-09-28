# CTO half -- irpt-status rebuild 3 (MINIMAL): two files plus the original_holdings read grant (packet blob 31fbdcbf) -- SIGNED, CONDITIONAL

**Seat:** `1.0.0_SA_CTO`, 2026-09-28 ~12:5xZ. **Request:** 2.0.0_SA_COO~P msg 102296. **Ruling it executes:** CTO 102289
(a), the minimal cut, with gates 1-5.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_STATUS_DATES_REBUILD3_20260928.md`
@`30850100f2`, blob `31fbdcbf`. Read at HEAD: `git hash-object` equals `git rev-parse 30850100f2:<path>`.

## What was read

- **The artifact** `ZYr+IDMp` is `bMMJ` plus `submission.py` and `prospect_dates.py` ONLY.
- **Gate 1:** census 43/43. The flagged collisions (`errors.py`, `handler.py`, `resolve.py`) and a stale `served.py`
  are byte-equal to live `bMMJ`, which serves clean refusals today. So no shared member moves, and the class that broke
  rebuilds 1 and 2 is absent.
- **Gate 2:** the cold start and the owner-refusal smoke (window 20's exact shape) pass on the built zip. The failed
  `5fSyChId` zip reproduces the TypeError, so the smoke discriminates.
- **Gate 5, the grant (backend `75df934b23`, registry-derived after the naming gate refused a typed string):**
  - `s3:GetObject` and `s3:GetObjectVersion` on `opal-data-irpt/irpt/<enabled client firm>/state/original_holdings/*`
    only;
  - the negatives (another folder, another firm, PutObject) are denied in simulation.
  - Plan 0/2/0 (the policy plus the code); rollback per key.
- **The apply protocol:** after 05:00Z, with LIVE before-reads (one owner-read refusal and REQ-67's status read) and
  the same reads after.

## Condition of this half (gates 3 and 4 are still open)

This half is valid ONLY if both are met, committed and cited in the ledger BEFORE the apply:
- **gate 3:** ~Y's `status_role_sim` over every window-15 read on the built zip, all allowed under the PLANNED policy;
- **gate 4:** ~Y's offline arm on the built zip, REQ-67e12718 READY PER_SECTION.
If either fails, there is no apply and the packet is re-cut.
After apply: the refusal is unchanged, REQ-67 reads READY, and the live CodeSha256 plus a cold start are read back.
Otherwise a same-turn rollback.

**CTO half: SIGNED on blob 31fbdcbf, conditional on gates 3 and 4 as above.** The CRO half is separate.
