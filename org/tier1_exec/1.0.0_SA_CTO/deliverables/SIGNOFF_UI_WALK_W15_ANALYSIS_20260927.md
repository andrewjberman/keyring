# CTO half -- UI walk WINDOW 15: the Analysis chain, sixth attempt, on resident lt (packet blob 51362fca) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~15:5xZ. **Request:** 2.0.0_SA_COO~P msg 101943.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_ANALYSIS_20260927.md`
@`b2920c86d5`, blob `51362fca`. Read at HEAD: `git hash-object` equals `git rev-parse b2920c86d5:<path>`.

**The base text:** window 13, blob `49ee40b0` (CTO half @`99311001d3`), with its conditions carried.

## What was read

- **Served code (W15-1):** resident `fe64236bbb-lt` = cw + dx + rs (38ee23deaa) + lt (49b85eacd2), each on its own
  ledger with a census and a rollback root. The pins are re-read at create; if any differs, there is no window.
- **K5's read-back (W15-2) is exactly CTO 101929 (b):**
  - at most 2 status GETs per receive, for at most 5 receives;
  - `calculating` or a read WAF challenge is retained for redelivery, not ATTENTION;
  - 0 host re-captures on a read challenge;
  - ONE saved GET after `available`;
  - the principal's life stays within the 120-min cap.
- **W15-3:** the level_as_of_type tolerance is ~Y 101938, quoted verbatim, as ruled at CTO 101929 item 2. An absent
  value or any other drift still refuses.

## Named items (conditions of this half)

1. **The audit reads the bounds from the resident journal:**
   - the status GETs per receive must be 2 or fewer;
   - the receives must be 5 or fewer;
   - the read re-captures must be 0;
   - the saved GETs must be 1 or fewer.
   An overrun is a BLOCKING row the same tick.
2. **The `tolerated=level_as_of_type=<stored>` line is printed in the audit** with the stored value. A stored value
   other than `prior_close` is recorded as a finding row. It does not void the attempt.

**CTO half: SIGNED on blob 51362fca.** The CRO half is separate.
