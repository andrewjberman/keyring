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

## Addendum 1 (2026-09-27 ~03:3xZ) -- K11 refused unspent; YES to re-cutting the plan to end 09-22 for the next window

The source is 2.0.0_SA_COO~P msg 101741 (window 7 closed). This seat's reading, not re-measured:
- **What happened:** the page clamps every INF window to the INF directory as-of, 2026-09-22.
  - All 3 reads missed the plan's 09-25 end and got the unarmed refusal.
  - They made **0 Orion calls**; the plan was never claimed.
  - The arm was removed at 03:21:34Z.
  - The named invariant held: Orion calls are graded, not GETs.
- **Andrew's call 2 is still unused.** The record is `ANDREW_DIRECT_20260927_025xZ_YES_TO_ALL_THREE_P_OPEN_CALLS.md`,
  read here. The call is "ONE new Inflection Orion one-use Performance call, on one single-account-household INF
  client picked by `inf_one_use_plan.py`'s stated rule, YTD, armed under both halves, used in one signed-in window,
  then spent".
  - It names no particular window, and no call was spent in window 7.
  - A YTD plan ending at the directory as-of the page actually sends is still that one call.
  - So a re-cut is inside the word, not wider.
- **YES, under a new arm packet for the next window, on these terms:**
  - the re-cut changes only the window's end (to 2026-09-22), its expiry and its sha;
  - the account is still the rule's pick, and if the pick changes, it is printed with the reason;
  - the next window's packet names the plan;
  - the audit still grades Orion calls from the adapter log, exactly 1 across Andrew's call 2 as a whole (window 7's
    0 plus the next window's 1).
- **Order:** Andrew's call 3 (COT) still comes after INF's call is spent, because the adapter holds one plan at a time.

## Addendum 2 (2026-09-27 ~03:3xZ) -- addendum 1's premise was false; its YES to 09-22 is WITHDRAWN; (a) instead

The source is 2.0.0_SA_COO~P msg 101746, measured by ~P through the served directory browse, not re-measured here:
- the INF directory as-of is **2026-09-25** for 292 of 292 entries, including the target `acc_5510a..`;
- Cottonwood's is 2026-09-22 and 49F's is 2026-09-24.

So the page's 09-22 clamp on an INF account is **Cottonwood's as-of applied across firms**: a page defect, likely in
Global mode.
- **Withdrawn:** addendum 1's yes to re-cutting the plan to 09-22. Bending the plan to a page defect would have been
  the wrong fix.
- **YES to (a):**
  - the SAME plan f0de098f (end 09-25, which is the served truth) is re-armed. It is the env-only act this half
    signed in section 2, now under its own ledger entry, and it must be claimed before its 12:00Z expiry;
  - ~D reads with the page's firm selector on **Inflection**, not Global;
  - the next window's packet carries K11 as before.
- **If the page still clamps under Inflection,** the reads are refused unspent (0 Orion calls), and that ends the
  attempt. There is no third workaround in the plan.
- **The defect goes in its own row** in ~D's lane: a cross-firm as-of in the page makes INF reads stop at another
  firm's date.

## Addendum 3 (2026-09-27 ~03:4xZ) -- addendum 2's premise was also false; YES to (b), end = INF's served holdings as-of

The source is 2.0.0_SA_COO~P msg 101753. It corrects ~P's own 101745 and cites ~D's window-7 HAR (101750). As
reported, not re-measured here:
- the page issued `POST selections?selected_tenant=inflection`, then a holdings GET answering `business_date
  2026-09-22`;
- the page ends Performance windows on that holdings as-of, per CTO 101422.

So the 09-22 is **INF's own holdings as-of**, not Cottonwood's, and there is no cross-firm page defect. Addendum 2
rested on a matching-dates inference that its own source has now withdrawn. **Addendum 2's "(a)" and its defect row
are withdrawn.**
- **YES to (b).** A new plan ends at the served INF holdings as-of, **read at build from the served holdings answer
  and printed with its source**, never typed (today it is 2026-09-22).
  - Everything else follows 3a68bb2d's terms: the rule's pick, the env-only arm and its rollback, ONE Orion call,
    no retry.
  - It runs in a new window, under that window's packet.
  - It is still Andrew's call 2 (0 spent), per addendum 1's reading of his word.
- **The CTO's pre-check (101749) carries, adapted.** With the arm OFF, ~D's Inflection-mode read shows the page
  requesting an end equal to the new plan's end. That costs nothing and spends nothing, and it has to pass before
  the arm goes on. If it does not match, nothing arms.
- **Not this act's question:** the INF directory reads 09-25 while the INF holdings read 09-22. Whether Performance
  should end on its own source's as-of is ~D's PRD question, as ~P says.
- **What this sequence teaches, for this seat:** two decisions in 15 minutes rested on an inferred premise, and each
  was reversed by the next measurement. This half now takes the page's end date only from the HAR or the served
  answer, never from a matching date.
