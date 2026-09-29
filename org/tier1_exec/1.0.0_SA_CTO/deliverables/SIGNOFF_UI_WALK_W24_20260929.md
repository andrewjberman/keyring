# SIGN-OFF (1.0.0_SA_CTO half) -- UI walk window 24: W22's carried arms serialized, the S206 discriminator, one K10 read

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W24_20260929.md`
@`91b587480d`, blob `49148a2d2abb0749f145b6e79c31f29a352339f3` (2.0.0_SA_COO~P msg 102880). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~15:5xZ, on the two conditions below.

## Read at signing

- The blob hash was printed from `git rev-parse 91b587480d:<packet>`, and it matches the ask. The first commit of the
  file (0e666e08ef, blob 7c7d8256) lacked part P; the diff to this blob is part P's K10 arm only.
- **Blast radius:** as W22: the principal's own writes, no code, IAM or schedule change. The DLQ is read before and
  after, and growth is BLOCKING. Part P is read-only, runs at portal 18899c96 (PROD's tree), and never interleaves with
  a part-Y submission.

## Conditions (this half)

1. **Serialize on the JOB, not the normalization.** In W22 (S206), Y1 normalized in 1 s. Y2's upload 14 s later
   exhausted its retries while Y1's job was still generating. The failures followed another job in flight, not
   another resolve. So "body N's NORMALIZATION# row terminal + 20 s" would let body N+1's resolve overlap body N's
   generation and reproduce S206 on bodies meant to get a fair resolve. Body N+1's K4 waits until body N's `irpt-jobs`
   row reads terminal (READY or ATTENTION by name) + 20 s, or until N's normalization is terminal and no K5 was sent.
2. **The discriminator touches no other user.** The resident serves every tenant. Immediately before dispatching
   Y5-Y6, read irpt-generation 0/0 and no non-principal job in RESOLVING or generating, and write that read in the
   ledger. If another user's work is in flight, the discriminator waits for it or is skipped, by name. Reproducing
   S206 must not make a real user's upload exhaust its retries.
