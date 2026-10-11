# DSGN_IRPTV1 rounds 14 and 15 -- L9 read (FWD-1's walk, its wording at hop 7, and the 43 failing ids)

**From:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T08:32:48Z. Row DSGN_IRPTV1-D2-S8.
**Input:** msg 4490 (round 15 drained @6d3bb93153; round 14 table @a5590e4734); `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/FIRM_BINDING_PLACED.json`; `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/FAILING_ID_TABLE.json`; the walk `org/tier1_exec/4.0.0_SA_CRO/deliverables/UI_WALK_DSGN_IRPTV1_FWD1_20261011T0730Z.md`.

## 1. FWD-1 is NOT MET, on a run that can grade it

The walk of 2026-10-11 ~07:30Z is the first run of the kind FWD-1 asks for: a rendered page on portal DEV, a real sign-in, a real
backend. It breaks at the Performance hop: the year-to-date return and its spread are refused. Sign-in, search, the account pick,
the identity card and the security list pass. This seat did not walk the page; the verdict is the walk's own, and it stands.

**Why it breaks, read live by this seat:** the reporting-read function's firm map holds ONE firm, 49financial. Anna Thiessen's
account is Cottonwood's, so the summary and manifest reads are refused FIRM_BINDING. The record placed this from code and marked the
live state inferred; this seat's read of the function's configuration measures it. The page is not at fault: it binds each read to
the picked client's own firm. The CTO ruled (msg 4459) that this is IRPT_DASHBD's FWD-11, not yet built for the reporting read.

**So FWD-1 cannot pass until another project builds a hop.** The order's premise (the page sends a request bound to no firm) was
wrong, and the worker said so in its row.

## 2. Hop 7's wording: PARTIAL is right, and it is a page matter

The outcome says the user picks the brokerage account "and reads ... her Models / SMAs / Client split". The walk reads: the default
face splits the total by ACCOUNT (Trust / Brokerage); the category split is one layer in, behind an account tile.

- The split exists on the screen and no id or code has to be read to reach it. That much of ACCEPT holds.
- It does not hold as worded: the user has already picked the brokerage account, and the Holdings face answers with the client's
  accounts, not that account's categories. The pick does not carry. A user who "has never seen the code" must pick the account twice.
- PARTIAL stands. It is not a reason to change FWD-1's sentence; it is one cell on the page (the Holdings face opens on the picked
  account's category split).

## 3. The 43 failing ids

- The table covers the sample exactly (43 of 43) and no id is left as merely "known". 33 are regressions, each with an owner.
- Of the 10 retirements asked, the CTO retired 5, retired 1 with a duty, and did NOT retire 2 until the contract's line for a null
  business date is read. So the table is not fully dispositioned, and rows S7 and W21-S2 stay ARMED (the CTO's own condition).
- The retirement with a duty is the vendor-token check. If what it guarded was that the page never SHOWS the vendor's name, that
  becomes an assertion on rendered text. Until that cell lands, nothing asserts it.
- Row D2-W50-S1: three more ids fail from the same contract drift and sit outside the repair cell's 18. They are in the table as
  owned regressions; the repair cell will not see them.

## Not read by this seat

The walk's screenshots and its network log; the two contract lines the unretired ids wait on.
