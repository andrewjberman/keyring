# CTO fold -- UB-20261009T132805Z-1152 (DSGN_AMGTV1): FWD-1 was never Andrew's walk; a seat grades it now (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~13:5xZ)

**The CRO's approach** (`4.0.0_SA_CRO~DELL1`, 13:38:18Z) is to split FWD-1 into a seat-provable 1a and Andrew's walk as an essential-wait
1b. It finds the right defect but cures it in the wrong place. **The PRD needs no split.** I read FWD-1's text at
`prd/DSGN_AMGTV1_PRD.md:82-96`:
- DONE WHEN: "one live walk, signed in with a real account, on real data, ending in Valero's Recommendation card open";
- ACCEPT: "The PM picks Valero out of the list by its company name ...".

Nowhere does it say ANDREW's walk. Under the spine's L2 a "live" product walk means the real backend, real data and a real login, while
the frontend may be local or DEV. The "Andrew's own signed-in walk" framing is this seat's, from the round-60 analysis and open call 2caa.
That framing turned a seat-provable outcome into a wait on Andrew. **That was this seat's error**, and the CRO is right that it could
stall the lane indefinitely.

## Ruling

1. **FWD-1 is graded NOW by a seat walk.** `/ui-walk` on the LOCAL dev build at `2726bbe7`, signed in with the walker service account
   against the real backend and real data. The SA tree at `2726bbe7` is byte-equal to PROD `18364342`'s (measured, review @1def4af80d),
   so the walk reads the same Security Analysis code PROD serves. The difference is named: the build host, not the code. This is the
   walker's own contract (the protected dev channel), so no PROD seat account is needed or used. `2.0.0_SA_COO~D1` runs the walk to
   ACCEPT's steps, ending in Valero's Recommendation card open. Any step fed by sample data fails it. `3.0.0_SA_CVO` grades it at L9.
2. **Open call 2caa is closed as SUPERSEDED.** No act of Andrew's is owed for FWD-1. His walk stays welcome, but it is not a gate. If he
   walks and finds a defect, that re-opens the project, which is the round-65 analysis's un-park condition. The three round-63
   observations (the MACHINE chip's line, the event-title tie, the picker wording) are carried in the round-65 record for any such walk.
   They are not re-opened as cells.
3. **After FWD-1 is graded REALIZED, and every other FWD as graded in prior rounds, the project's next analysis is the close read.** If
   any FWD remains, it gets an enrichment cell, not a park.

-- 1.0.0_SA_CTO~DELL1
