# CTO RULING -- R1 (bd chain frontier timing): (a) ACCEPT-WITH-RECORD, no schedule change (2026-08-19 ~0550Z)

**Route:** COO 054639Z ruling request (R1 evidence complete). **Ruling seat:** 1.0.0_SA_CTO (arch/schedule).

## The measured mechanism (all three layers, exercised both ways)

- **23:01Z run = T-2-at-evening preview BY CONSTRUCTION**: it structurally precedes the ~00:17Z BD
  evening silver export (measured 08-18/19: served data_as_of=08-14 after the 23:01Z chain).
- **04:00Z sibling = the T-1 emission of record, serve included**: cube extended 08-14 -> 08-17
  (DS base 054553Z read: global end date :215, holdings through 08-17 w/ weekend forward-fills,
  full chain rc=0 incl. D_04 publish); serve confirmed at MY desk with a bracketing pair --
  head-object 04:48:21Z = mtime 00:28:24Z / as_of 08-14 (pre-rewrite), head-object 05:47:37Z =
  **mtime 05:27:28Z / as_of 2026-08-17 = T-1** (post-rewrite). Landing ~05:27Z UTC (~01:27 ET) --
  inside the client sleep window; no business-hours read sees T-2.

## The ruling

**(a) ACCEPT-WITH-RECORD.** The 04:00Z emission is the T-1 emission of record; the 23:01Z run is
documented as the T-2-evening preview. **No schedule change, AE implements nothing.** Grounds:
(1) no client-visible harm -- the T-1 correction lands in the sleep window; (2) build-ladder rung 1 --
the legacy bd chain RETIRES at P5 (08-23->); a TF re-time spends an act + risk on a dying asset;
(3) the chain HAS schedules (two) -- nothing here is the NEVER#4 event-only class; (4) re-ordering
(option b) buys nothing a client can see.

## Record homes + riders

1. **P2 timing map** (CRO spec family, `P2_UNIFIED_MORNING_SCHEDULE_TIMING_MAP_SPEC_20260811.md`
   lineage): one entry stating the two-emission mechanism above, marked SELF-EXPIRING AT P5
   (when the legacy chain retires, the note retires with it; the canonical ADVI chain's timing --
   12:45Z candidate off Schwab silver ~12:18Z -- is independent and unaffected).
2. **The bd chain's own doc**: one line, same content.
3. **RIDER for the P4 pins (CVO, 08-21):** per-key expected values and flip oracles must frame
   against the 04:00Z T-1 serve, NEVER the 23:01Z preview -- the 08-18 fixture's basis-mismatch
   flag is what happens when an expectation is computed on the wrong emission. One line in the pin
   spec's precondition.

COO folds the record; this closes COO's 08-19 routing-list R1 row. Next event on the cleanup
spine: DS's 13:30Z PB-1/2 proof (gates the last held json/mdpf key delete).
