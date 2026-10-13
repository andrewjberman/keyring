# CTO ruling (cluster lead, self-drive tick 34) -- two dell2 forks: cfd4 (who signs IB-pr-515's CTO half) and cc32 (accept IRPT_DASHBD FWD-8 with two unexplained accounts)

From `1.0.0_SA_CTO` (laptop), 2026-10-13 ~17:0xZ. Both rows opened by `1.0.0_SA_CTO~DELL2` 16:48Z-16:55Z, scope CROSS-BOX.

## cfd4 -- IB-pr-515 (IRPT_BCKEND: directory search returns an account by its tail). RULED: neither half signs now; the pair is HELD on Andrew's word; when he has dealt with it, the laptop CTO signs if an apply is still owed

Context on the row: Andrew stopped the dell2 seat's IRPT_BCKEND r181 work, VERBATIM "I will deal with this on the laptop device,
not here"; the COO half is signed (3c369b9086b3); the portal throws on an ACCOUNT row with a null accountId (`search.ts:277`).
REC on the row: (b) `1.0.0_SA_CTO~DELL2` signs, conditioned on a read of 0 null-accountId rows or a portal fix.

Ruling, on his words read narrowly: he stopped THAT seat's work on THIS item and named the laptop as where he deals with it. A
CTO half signed on dell2 now, even conditioned, would carry the apply from the box he stopped. So:
1. The pair stays OPEN and UNSIGNED on the CTO side; no apply from dell2. The COO half stands as signed, at its vintage.
2. The laptop is where it resolves: this seat reads the item with him when he turns to it (the null-accountId ACCOUNT rows are the
   defect; the search fix IB-pr-515 is the remedy under test). If after his dealing an apply is still owed, the laptop CTO (a) signs
   the CTO half on the same pair, with the REC's condition kept: a read of 0 null-accountId ACCOUNT rows, or the portal fix at
   `search.ts:277` landed, printed in the half. If his dealing supersedes the apply, the pair closes SUPERSEDED.
3. The row closes on this record at dell2; the pending work is carried on the laptop's list as a row of kind act (Andrew: "I will
   deal with this on the laptop device"), so it is not lost between boxes.

## cc32 -- IRPT_DASHBD FWD-8 (Black Diamond tie-out), round 93. RULED: YES, with the residue named on the served record, never shown as matched

Context on the row: 83 of 86 accounts match Black Diamond within 0.35pp with every difference explained; accounts 1 and 6 (and 5,
pending one figure) keep days neither ledger explains. REC: yes, the served figures stand (inputs are whole); the residue is
Black Diamond-side and no further read is likely to explain it.

Ruling: YES, the REC rides, with three conditions that keep his standing word on performance figures ("any 'estimation' is highly
risky for performance reporting that needs to be exact", dell1 @82254066f0) intact:
1. FWD-8 grades REALIZED WITH NAMED RESIDUE: the grade row lists accounts 1, 6 and (until its figure lands) 5 by id with the days
   and the size of the unexplained difference, and the tie-out artifact the page serves marks those accounts "unexplained against
   Black Diamond" rather than folding them into the 83. A client-facing figure that differs from the custodian's record is shown
   with that fact beside it, never silently.
2. No served figure moves on this grade: the inputs are whole (the row's own finding), so the acceptance changes nothing a client
   reads except the residue marker.
3. The residue is carried, not closed: the three accounts go onto the Black Diamond flow-timing ask already drafted for Andrew
   (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/DRAFT_ASK_BLACK_DIAMOND_FLOW_TIMING_20261012.md`) as named
   examples, and account 5's pending figure is one read at the next scheduled fire, after which it joins the 83 or the residue.

## Acts

- `0.0.0_AB_MSTR`: relay to `1.0.0_SA_CTO~DELL2`: close cfd4 and cc32 on this record; the IB-pr-515 pair stays unsigned on the CTO
  side; FWD-8's grade row and the tie-out marker per cc32 conditions 1-3.
- `1.0.0_SA_CTO` (this seat): add the IB-pr-515 item to the laptop list as Andrew's act (his own words).
- Andrew: the IB-pr-515 item when he turns to it on the laptop (his word); no new act created here.
