# CTO ROUND-13 ANALYSIS -- IRPT_ANLREQ workstream Y -- answering the round-12 L10 slug (2026-10-11 ~20:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the round-12 slug (3.0.0_SA_CVO msg 5764; grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_12_Y_L9_GRADE_20261011.md` @643e3c424b; channel @428d98cb09).
**Prior:** the round-12 analysis @06b01d9b88. **No PRD addendum.**

## 1. Where the workstream stands

AR121-y-AC3 MET: the queue list shows each waiting ticket's age in words, on portal DEV c2c6a8ae (this seat read the diff
and the page's class on PROD: Opal-internal). Row D2-S59 is closed on its owner's disarm. Release 5's return is still held
on the PROD push of portal fc876722, which waits on Andrew.

## 2. The reviewer's three limits

1. **47 hours reads "1 day": CORRECTED in the next cell.** TCKT_VNEXT FWD-5's ACCEPT is that a person reads how long a
   request has waited and picks the next one from the queue alone. A floor to whole days hides almost a day of waiting on
   exactly the tickets being ranked. Rule: hours are shown up to 72 hours ("47 hours"); from 72 hours on, whole days.
2. **The age does not tick on an open page: ACCEPTED as it is.** The list is read when it loads; a timer is not built for it.
   The page does not claim to be live.
3. **The code shows an age for every status except completed, wider than the packet's wording: NARROWED.** The age is shown
   for the statuses in which a ticket is waiting, named as a closed list in the code, and for no other. A status added
   later shows no age until someone decides it is a waiting one. Which statuses exist is read from the ticket type's
   definition first; this seat has not read it.

## 3. ENRICHMENT LIST for round 13 (ONE issuance)

1. The age's two corrections (items 1 and 3), one cell, with the test's fixed clock; a portal candidate to this seat.
2. TCKT_VNEXT FWD-3's one-account check in the upload door (2.0.0_SA_COO~V2 msg 5745): first a read of how "several
   accounts in one file" can be recognised at all, since the normalizer reads no account column today.
3. Held, not cut: release 5's return and the fallback's removal, in that order, after the PROD push.

## 4. Acts only Andrew can do

- The PROD push of portal fc876722 (CLAUDE.md, Agent Autonomy: unsure is client-facing).

## 5. What this analysis did not measure

No rendered page was looked at by this seat or by the reviewer.

-- 1.0.0_SA_CTO~DELL2
