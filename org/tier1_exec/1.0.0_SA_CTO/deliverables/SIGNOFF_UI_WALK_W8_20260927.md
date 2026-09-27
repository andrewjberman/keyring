# CTO half -- UI walk WINDOW 8: INF's ONE Orion read (plan 7f64b166) + an optional third Analysis attempt -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~03:5xZ. **Request:** 2.0.0_SA_COO~P msg 101772.

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W8_20260927.md`
@`1282a22bf5`, blob `e2462004`. Read at HEAD: `git hash-object` equals `git rev-parse 1282a22bf5:<path>`.

**The base text:** window 7, blob `3ab51a52`, re-hashed at HEAD (CTO half @`c226ade7a3`).

## What was read

- **W8-1** is Andrew's call 2 ("yes to all three", @`6039c2f680`), with 0 Orion calls spent so far.
  - Plan `7f64b166`: its end 2026-09-22 is READ at build from the served INF holdings `business_date`, as ruled at
    ~P 101752 and in R10 @`54323a0fb5`. Same account pick; expiry 12:00Z.
  - The arm-OFF pre-check (CRO 101753): the page must request `end=2026-09-22`, or nothing arms.
  - The arm runs on 3a68bb2d's terms: safe-apply re-plans 0/1/0 with the two env keys, and reads back.
  - Then ONE read (K11), and a disarm the same tick if it is unclaimed at delete.
  - The audit counts exactly ONE Orion call across call 2, from the adapter log.
- **W8-2** runs ONLY on Andrew's word at the ~Y terminal. It uses resident `fe64236bbb-rb` (the read-back poll fix;
  ledger `irpt-resident-read-back-poll-20260927`). K5's named vendor reads include up to 12 status GETs, 5 s apart
  (CTO 101763). K10 is limited by DSGN_IRPTV1-S18.
- **W8-3** re-reads the pins at create: generate `G/TqLPdL..`, resident `fe64236bbb-rb`, and the adapter
  `Ll6t4VPa..` with the live plan 01209afb. If any differs, there is no window.

## Named item (a condition of this half)

**The pre-check's evidence lands in the INF ledger entry BEFORE the arm:** the request URL or HAR line showing
`end=2026-09-22`, and the adapter's `VendorEgressRefused` with zero vendor calls. An arm with no recorded pre-check is
outside this half.

**CTO half: SIGNED on blob e2462004** (with window 7 blob 3ab51a52 as amended by W8-1..3). The CRO half is separate.
W8-2 still needs Andrew's word.
