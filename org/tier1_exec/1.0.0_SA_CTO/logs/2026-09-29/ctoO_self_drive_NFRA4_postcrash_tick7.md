# /self-drive NFRA four -- ticks 6-7 + Andrew's open-call word (1.0.0_SA_CTO~O, site Z, 2026-09-29 20:4xZ-21:5xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4

## Andrew's word (record @efff16d6aa, `ANDREW_DIRECT_20260929_204xZ_OPEN_CALLS_PUSH_YES_GC_IT_REMOVE_34_YES.md`)

> "yes to call 1. call 2 need to talk to IT, so blocked externally there. call 3 yes"

- **Call 1, push.** 0.0.0_AB_MSTR~Z pushed portal DEV (ac8265668d). Workspace CLOUD is held on 5 merge conflicts, taken
  to Andrew by MSTR~Z (msg 26703). 41ba3f747f is still not on origin (re-read 21:49Z), so MX-t-10 stays held.
- **Call 2, G-C.** BLOCKED-EXTERNAL on Opal IT; relayed to 2.0.0_SA_COO~O for NFRA_OPLGTW's blocking.
- **Call 3, removals: DONE, 34 of 34.** This seat 10 of 10; 2.0.0_SA_COO~O 11 of 11 (msg 26720); 2.0.0_SA_COO~MI 13 of 13
  (msg 26727). Every branch is kept. Five portal/node_modules junctions (1 here, 4 at COO~O) were unlinked before
  removal, and the main node_modules read 263 entries throughout.

## Measured (tick 7, 21:49Z)

- **Inbox:** 1 new (26727, acked); 0 unread after.
- **Open TOs: 12 of 180.** OG 4 (g-1, t-2, v-7, v-8), OA 4, MP 2, MX 2. Tick 5's figure was right.
  - **WITHDRAWN (21:5xZ):** this log first read "13, OG 5, OG-n-1 still staged". That was an instrument error in this
    seat: `grep -o '<status>[a-z_]*</status>' | tail -1` skips an annotated tag (`<status>complete -- ...</status>`),
    so the tail landed on the stale first tag.
  - OG-n-1 carries three appended tags at CLOUD (:139 staged, :140 pending, :141 complete). 2.0.0_SA_COO~O corrected
    it (msg 26731). The recount reads the LAST tag's first word (`<status>[a-z_]*` with no closing anchor).
  - The drain check stands: `safe-merge --verify-merge c72df75fce` shows 5 needed, 0 dropped.
- **Completion:** 0 of 4; 4 REACHABLE.

## Calls

No open calls in scope (ticks 6-7).

## Acts only Andrew can do (each cited)

- Resolve or route the 5 CLOUD merge conflicts for the site Z push (the shared-branch push is his hold; MSTR~Z brought
  them to him).
- G-C: blocked externally on Opal IT (his conversation with IT).
- G-ACCT step 5: the setup-token on Opal_Agent (his login). MCPORTAL G-2ND and G-CLOSE. OPLGTW G-D. MX-t-11: his widening
  word for platinum/advi.

## Compiler Tools

- `.tools/safe-merge.sh --verify-merge c72df75fce`: 5 needed, 0 dropped, 0 foreign.
- PowerShell reparse-point enumeration over 10 trees: 1 junction found.
