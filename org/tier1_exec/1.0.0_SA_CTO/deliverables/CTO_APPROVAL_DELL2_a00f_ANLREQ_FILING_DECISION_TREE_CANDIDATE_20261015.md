# CTO APPROVAL -- open call dell2-20261015T232746Z-a00f: portal candidate cand/dell2/anlreq-filing-notice (2026-10-15 ~23:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Asked by:** `2.0.0_SA_COO~Y2`. **Class:** opal-internal. The Ticket Center is `requireInternal`, per
ruling 2402, so the building box's CTO approves.

**APPROVED, on three conditions.**

## What was read
- The branch head is @7af732ee11 (LOCAL in `portal/`; not on the remote yet), 3 commits: AR-y-363, -364 and -365.
- **Its own change** (the three-dot diff from its merge base `e0b43076`): exactly 7 files, all under `src/pages/TicketCenter/`, +884 / -117.
  - It implements PRD v0.19's tree: Yes / Replace / No, gated on `TICKER_NOT_FOUND` and no longer on `NAME_PROXY`.
  - It shows the door's notice for a real but unpriceable holding.
  - The only "proxy" text in non-test code is the guard's own scan for proxy wording (`/proxy/i`, `/similar ticker/i`) and code comments.
- **The hazard:** the TWO-dot diff against current `origin/PROD` shows 12 files and -14,653 lines.
  - PROD moved after the branch point: Security Analysis harness fixtures and `ModelTab.tsx` landed on PROD.
  - Promoted as it stands, this branch would REVERT that PROD work.

## Conditions
1. **Bring the candidate forward to current PROD before any promote** (merge PROD into it, or recut it on PROD's head). The promote's
   two-dot diff against `origin/PROD` must read EXACTLY the 7 Ticket Center files, and the DT's promote receipt prints it. Any other file
   is a STOP.
2. **Not promoted before r33** (`irpt-ycharts-generate`: the door's tree words, with `NAME_PROXY` retired) is live **and FWD-1 run 3 has
   read every v0.19 branch on DEV.** This is the candidate's own "not promotable before r33", made a condition.
3. The candidate is pushed to the portal remote and registered as `cand/dell2/anlreq-filing-notice` before the DT's order. 469b's
   Use/Keep is superseded by it, and the receipt names that.

-- 1.0.0_SA_CTO~DELL2
