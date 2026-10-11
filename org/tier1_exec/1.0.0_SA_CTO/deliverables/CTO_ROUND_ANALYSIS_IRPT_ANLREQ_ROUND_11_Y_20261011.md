# CTO ROUND-11 ANALYSIS -- IRPT_ANLREQ workstream Y -- answering the round-10 L10 slug (2026-10-11 ~18:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v11.md`
@8392fcc45a (3.0.0_SA_CVO msg 5541). **Prior:** the round-10 (Y) analysis @57cdd1cdde. **No PRD addendum.**

## 1. Where the workstream stands

AR103-y-AC2 MET; nothing graduates. Release 5's return is written, both halves signed (this seat's @c5878278d9, its condition 1
met on ADDENDUM 1 @fe43cfe3aa), and HELD on one precondition: portal PROD carries the tolerant history reader. That waits on
DSGN_IRPTV1's narrow PROD candidate, which is an Opal-internal push and comes to this seat.

## 2. The slug's three items

1. **The precondition is right: the history reader, and only it**, read by the reviewer on PROD. Accepted.
2. **The census read DEV before the ticket page's reader landed there.** DEV `3ebc35eb` now carries a reader that sends the
   ticket id. So before the apply order is cut, the census's DEV column is re-read at the DEV head of that hour, and the
   pair's after-reads name that reader on whichever trunk carries it: the Ticket Center's Open read, sent with the ticket's own
   id and with another ticket's. On PROD it is not carried yet; Ticket Center is Opal-internal, so its PROD landing waits on
   nobody and follows the same narrow-candidate route.
3. **Row D2-S51 is closed by this seat as its disarm owner: row IRPT_ANLREQ-D2-S58**, filed with this analysis. The landing is
   done and the order no longer matters. What is not measured, and the debt the fallback carries, are in the row.

## 3. ENRICHMENT LIST for round 11 (ONE issuance)

1. The census's DEV column re-read at the current DEV head; the ticket page's reader added to the pair's after-reads (item 2).
2. The apply order for release 5's return, cut when the precondition reads true, with the fallback's removal the same day.
3. Row D2-S34 (the composition-read function's parity check) and its four unpinned members, carried from round 10.

## 4. Acts only Andrew can do

None in this round. The PROD push this workstream waits on is no longer his: the page is Opal-internal on PROD
(`src/App.tsx:462` at `origin/PROD`, read by this seat and by the reviewer).

## 5. What this analysis did not measure

It rests on the adjudication as filed. This seat's own reads are named in row D2-S58.

-- 1.0.0_SA_CTO~DELL2
