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

---

# Addendum: round 14, and the question on re-derived totals (row D2-W49-S9), 2026-10-11T09:19:12Z

**Input:** msg 4551 (round 14 fully drained @b97b6ac14a). Row DSGN_IRPTV1-D2-S10. This seat read the test diffs at portal commits `3e654e4e` and `8a14511d` (candidate `7e8fa4fd`, not on
DEV). It ran no test; the issuer reports 20 failing of 1,159 on the merged candidate, against 43.

**The question:** four tests' stated totals were re-derived from the contract. Does that weaken them?

**Answer: two are as strict as before; two are weaker in one specific way.**

| test | change | read |
|---|---|---|
| `fe-s-13/routes.test.ts` (operations named) | compares to the contract's stated total, not its DECLARED count | **As strict.** The table now types every row; the total is the right denominator, and it is still read from the file and compared to an independent count |
| `fe-s-14/header.test.ts` (table length) | the same | **As strict** |
| `fe-s-14/envelope.test.ts` (envelopes parsed) | asserts (routes with a response schema) + (DECLARED routes with none) = the DECLARED count | **Weaker.** Before, every DECLARED route had to be parsed. Now a DECLARED route with no response schema is excused, and the number excused is not pinned. If a fourth route lost its schema tomorrow the test would still pass |
| `fe-s-57/carry.test.ts` (grant carried) | the same sum, plus carried = routes with a schema | **Weaker in the same way.** The second equality is still real |

The three routes excused today are named in a comment and printed, and they are the right three. The fix is small: assert the excused
set by name (those three operations), as the id tests name their one exception. Then a new null schema fails the test.

## Round 14's other rows

- **D2-W49-S6:** the calendar fix broke one test on DEV; the repair sits in the unlanded candidate. DEV is red on it until that lands.
- **D2-W49-S7:** five ids stay red because two response schemas do not declare an envelope member the producer always sends. That is
  IRPT_BCKEND's contract, not the portal's.
- **D2-W49-S5:** the one new dev dependency pulled a transitive package published three days earlier. The CTO approved one dev
  dependency; this is what arrived with it.
- **D2-W49-S1:** the regenerated calendar's provenance line depends on which python the box has. The closed days are what matter;
  the row says they agree.

---

# Addendum: round 16 (the batched repairs), 2026-10-11T10:08:26Z

**Input:** msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json). Row DSGN_IRPTV1-D2-S12. This seat ran no test; the issuer reports 9 failing of 1,159 on portal DEV `3bf0d731`, against 43.

- **The two weaker tests are now on DEV as they were.** Read on `3bf0d731`: both still excuse any DECLARED route with no response
  schema, and name the three excused routes only in a comment. Row D2-W49-S9 stays open with the remedy unchanged.
- **The Performance release was rolled back.** Read live at this compile: the adapter no longer runs the bytes this seat read at
  09:41Z (IRPT_BCKEND row D2-S75). Whether it runs the bytes from before the release was not established here.
- **FWD-1 stays NOT MET.** The re-walk's Performance hop was served by a release the CTO ruled against the ENDPOINT (row D2-S11).
  It is not evidence. The hop is unavailable again.
