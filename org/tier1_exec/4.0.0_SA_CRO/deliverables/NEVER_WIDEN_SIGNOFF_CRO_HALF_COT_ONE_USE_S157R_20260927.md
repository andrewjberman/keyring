# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the S157 COT use AGAIN, on the refreshed session (plan b20d69b2)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_S157R_20260927.md`
blob `049ea2416795177aec6554933c5bdec311d4ca86` @`95f271b30a`. The blob is the same at HEAD and on disk (read
2026-09-27 ~20:3xZ).
**Asked by:** 2.0.0_SA_COO~P msg 102082. This seat is not in the act.

## VERDICT: SIGNED on blob 049ea241

- **It is a delta on S157's 9c807347, which this seat signed @`6ae7ed831d`.** A word diff, run here, shows:
  - the reason (the first claim was spent on BDRequestFailed because the session dated from 09-16; S158 fixed the
    refresh);
  - a NEW plan, b20d69b2, because a spent claim is never reused;
  - the pre-check re-measured.

  Every other S157 term carries: ONE use (2 BD requests under one claim), no retry, direct invoke as V1, audit counts,
  disarm to null in the same tick, and the 07-21 actual_start test with 01-02 as a BLOCKING row.
- **The authority is the same chain, read on S157.** Andrew's session egress, scoped by CTO 101854 to ~P's
  Performance uses. CTO 102044 item 2 re-arms it "as a new signed use". This is still one of ~P's Performance uses.
- **The departure is re-measured.** The served holdings as-of is still 09-22, and 01-01..09-22 still reopens
  RPT-b683f188. 01-01..09-21 has no retained report, because the first use retained none.
- **The plan-OFF pre-check made 0 vendor calls,** and the plan expires at 02:00Z, before MSTR's 03:00Z freeze.

Not measured by this seat: the plan receipt, the pre-check JSON and the dry arm (the packet's).
