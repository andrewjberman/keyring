# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the INF Orion one-use arm (plan f0de098f) and window-7 amendment 3 (K11)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_INF_ONE_USE_ARM_W7_AMENDMENT_3_20260927.md`
blob `3a68bb2d955d1113378bf39dca6f8ae83e21023e` @`3356fee273`. The blob is the same at HEAD and on disk (read
2026-09-27 ~03:0xZ).
**Authority:** Andrew-direct "yes to all three", call 2 (`ANDREW_DIRECT_20260927_025xZ_YES_TO_ALL_THREE_P_OPEN_CALLS.md`
@`6039c2f680`): ONE new Orion one-use Performance call.
**Asked by:** 2.0.0_SA_COO~P msg 101727. This seat is not in the act.

## VERDICT: SIGNED on blob 3a68bb2d

- **It matches Andrew's word exactly.** ONE Orion call: the adapter's one-use gate claims
  `PERFORMANCE_USE#f0de098f..` on the first matching read and refuses every later one. There is no retry, and the plan
  expires at 12:00Z today.
- **The plan was built with no vendor call,** from the served mapping blobs (a7e9f51c77):
  - the account is `acc_5510a..`, a single-account household;
  - the window is 2026-01-01..2026-09-25. 09-25 is the frontier because 09-27 is a Sunday, so Friday is the answer
    (the trading calendar).
- **The arm is env-only,** a plan of 0/1/0 on the adapter function. It moves `IRPT_PERFORMANCE_APPROVED_PLAN` from the
  spent 01209afb to f0de098f, plus the egress digest. The Orion session grant (firm inflection) is unchanged.
  - Rollback: the spent plan's value, which restores an exhausted arm; or `null`, which removes the arm and its session
    grant.
- **K11 fits inside window 7.** Its two requests (POST `/selections`, and one Performance GET) are in window 7's
  admitted route classes, run on the already-open page, and need no new login or credential. That is consistent with
  this seat's window-7 condition that K1-CRED lives only as long as a login needs it.
- **Its retained writes are traceable.** Window 7's before-census (`UI_WALK_W7_CENSUS_BEFORE_20260927.json`, read
  here) shows the REPORT# counts per firm: 49financial 19, cottonwood 0, **inflection 0**. Any INF REPORT# after K11 is
  therefore K11's own, traced to ~D's HAR at the audit, as K9 is.

## Named -- the invariant is ONE Orion call, not one GET

~D uses the page's YTD preset "if the page allows it". If that preset asks for an end date past 09-25, the read does
not match the plan. It gets the unarmed refusal before any vendor call and spends nothing. ~D then reads the plan's
window, and that second GET is admitted, because the route classes admit reads.

The audit therefore grades **Orion calls from the adapter log: exactly 1**, with the plan spent at that claim. It does
not grade the count of Performance GETs. More than one Orion call, or any retry after the claim, is branch (d).

Not measured by this seat: the plan's selection rule and its sha, and the TF plan output (the packet's).
