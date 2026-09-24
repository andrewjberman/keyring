# Crash recovery -- CTO adoption and routing, laptop, 2026-09-24

**Seat:** 1.0.0_SA_CTO. **Adopts:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/CRASH_RECOVERY_CLEAN_START_BRIEF_20260924.md`
@6f8eefcfe7 (4.0.0_SA_CRO msg 100725, Andrew-direct at the CRO terminal ~14:4xZ). **Written:** 15:10Z.

## 1. Adoption

Section 2 of the brief is adopted AS WRITTEN: steps A1-A3, B1-B3, C1-C3, D1-D2, in that order, one owner per step,
each closed by the read the brief names. Section 4 (S1-S7) is the clean start point. The B2 push stays Andrew's word
(LD-0522). D2 worktree removal stays on Andrew's confirmation. The CRO's measurements are cited, not re-taken
(corroboration cap); section 2 below re-reads only the values that can move with time.

## 2. Re-measured at 15:07-15:10Z (one read each)

| Item | Brief (14:26-14:48Z) | Now | Read |
|---|---|---|---|
| A1 `_authz` fix in P's installation | uncommitted | STILL uncommitted (errors.py, served.py M; test ?? ; 2 fixtures ??) | `git -C ...\irpt-smoke-p-backend-20260923 status --porcelain -- .../_authz .../_contracts` |
| A2 candidate 8 | 2 untracked files | STILL 2 untracked, branch `irpt-dev-candidate-8-20260924` | `git -C ...\portal status --porcelain` |
| A3 Y's pin | `+` | STILL `+ b398d27731` | `git cherry irpt-smoke-p-backend-20260923 b398d27731` |
| origin/DEV (portal) | `a3f4c860` | **`7952976b`** -- site Z pull-merged a3f4c860 into its DEV at 11:02 ET (0.0.0_AB_MSTR~Z), carrying 2.0.0_SA_COO~Z's AMGT-rm-3 drain `ffef75aa` + `f326daff`. a3f4c860 IS an ancestor; f1d02f30 IS an ancestor | `git ls-remote origin DEV`; `git fetch origin DEV`; `merge-base --is-ancestor` x2 |
| local portal DEV / CLOUD gitlink | `f1d02f30` / `f1d02f30` | unchanged | `git -C portal rev-parse DEV`; `git ls-tree CLOUD portal` |
| CLOUD vs origin/CLOUD | 177 local / 323 origin | 180 / 329 (tracking ref); origin/CLOUD head `918ca7abe0` | `rev-list --left-right --count`; `git ls-remote origin CLOUD` |
| Live seats | CRO, CRO~A, CRO~B | + 0.0.0_AB_MSTR, 1.0.0_SA_CTO. Down: ~P, ~Y, ~M, ~D, 3.0.0_SA_CVO | `get_live_agents` |

**Consequence, binding on B1, B3, B2 and A2:** "origin/DEV" in the brief means **origin/DEV's tip at the act**,
re-read by `git ls-remote origin DEV` in the same step -- never the literal `a3f4c860`. Site Z is still moving.

## 3. Routing

| Step | Owner | Carrier | State at send | Un-parks when |
|---|---|---|---|---|
| B1, B3, then B2 to Andrew for the push word | 0.0.0_AB_MSTR | msg 100729 | DELIVERED (live; its watcher moved it to read/ at 15:11:46Z) | now |
| A1 -> A3 -> A2 -> C1 | 2.0.0_SA_COO~P | msg 100730 | QUEUED (down) | ~P restarts; its `/watcher` emits the file; B.0 since 13:30Z |
| seat-scope placement (section 4); S6/S7; `TO-IV-e-7`; re-serve 5174 from DEV's tip; round-2 drain packet | 2.0.0_SA_COO~D | msg 100731 | QUEUED (down) | ~D restarts |
| fresh `/watcher`; 6 unread; round-2 L8-L10 on ~D's packet | 3.0.0_SA_CVO | msg 100732 | QUEUED (down) | the CVO restarts; B.0 since 12:00Z |
| C2 (two stale OPEN copies at its drain -- do not close twice) | 2.0.0_SA_COO~M | msg 100733 | QUEUED (down) | ~M's drain |
| nothing stranded; resume from STATUS `0ade171e88`; read 100718 | 2.0.0_SA_COO~Y | this record (no act owed, so no message) | -- | ~Y restarts |
| C3 1.0.0_SA_CTO: `org/law-edit-audit.log` (2 lines) | 1.0.0_SA_CTO | this commit | DONE | -- |
| C3 4.0.0_SA_CRO: `org/audit/archive/FINDINGS.md`; open item 8 (card 2 second read) | 4.0.0_SA_CRO | the brief | live | -- |
| D1 main-tree edits | each named owner | the brief | -- | at each owner's restart; never bulk-committed |

Also in this commit: `org/law-edit-audit.log` added to `org/audit/archive/MANIFEST.txt`. The audit-archive invoker
raised `[COVERAGE/UNCOVERED-AUDIT-LOG]` on it at this startup (15:06Z). It is the law lock's own pass/refusal
trail, so it is the same class as the jq-ban and pipescript precedents.

## 4. Andrew's seat-scope word to 2.0.0_SA_COO~D -- placed

Verbatim, relayed by 2.0.0_SA_COO~D msg 100713 (Andrew at the ~D terminal ~14:0xZ): "also merge this in to the main
DEV branch, you dont need to be working on a feature tree for this work, I think that you should be leading frontend
for IRPT as a whole, none of the other COOs on IRPT are doing fucking anything on frontend anyway."

Placed as spoken: **2.0.0_SA_COO~D leads IRPT frontend as a whole**, landing on portal DEV directly (no feature
tree), across DSGN_IRPTV1 and the IRPT portal surface. A Tier-1 seat may hold several projects (Rule 27 seating
reaches Tier 2 only). **It is not a stop or a gate on any other seat.** ~P, ~M and ~Y keep their current write
surfaces, and ~P's A2 (save candidate 8) proceeds as routed because it is loss prevention.

**Asked of Andrew at 15:1xZ, not adjudicated here:** does the lead mean the other IRPT seats' portal frontend
candidates (today: ~P's candidate 8, `contracts/wire/DirectoryPage.ts`) are handed to ~D to land on DEV? That reading
is wider than the words and plausible, so per CLAUDE.md section 2 (b) it is asked, not placed. Until he answers,
nothing changes for ~P, ~M or ~Y.

**ANSWERED ~15:31Z, at the 1.0.0_SA_CTO terminal: "Yes, hand to ~D (Recommended)."** Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_153xZ_IRPT_FRONTEND_CANDIDATES_HAND_TO_COO_D.md`.
- ~P, ~M and ~Y commit their contract and fixture files on their own candidate branches.
- They hand each IRPT portal candidate to 2.0.0_SA_COO~D, which lands it on DEV.
- ~P's A2 runs first, unchanged.
The paragraph above is superseded by this answer and kept as written.

## 5. Read, acked, no act owed

- 100700 (2.0.0_SA_COO~M): confirms Y 100691 by line. Neither the 49F nor the INF producer reads an accrual or a
  cash indicator; M withdraws its hop-3 page inference. This confirms the premise of CTO ruling (3); nothing moves.
- 100723 (4.0.0_SA_CRO~B, RCN-0016) and 100726 (4.0.0_SA_CRO~A, RCN-0017): research and proposals, with six calls
  at Andrew. No act asked of this seat.
