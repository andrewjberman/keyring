# CTO rulings -- cluster-lead tick 2 (2026-10-11 03:57Z)

Read: `python .tools/open-calls.py list --all --cloud` at 03:57:51Z: 4 of 4 boxes, 10 OPEN (act 10, fork 0), 76 closed.
keep-driving scan=off empty_tick=off on all four.

## dell1-20261011T033643Z-e7f2 -- portal PROD promote (AMGT_RESAPP r89 item 7)

**Ruling: the promote is CLIENT-FACING, so it waits on Andrew's word (push law, `ANDREW_DIRECT_20261009_044xZ_PUSHES_NEED_NO_APPROVAL_EXCEPT_CLIENT_FACING_PROD.md`). Listed to Andrew this tick.**

Measured (portal `origin/DEV` 26f621d5 vs `origin/PROD` 37aa1247, 46 commits):

| Page | Route guard (`portal/src/App.tsx`) | Class |
|---|---|---|
| SecurityAnalysis (7 files) | `requireDev requireAdmin` (:470) | Opal-internal |
| TicketCenter (8) | `requireInternal` (:500) | Opal-internal |
| InvestorReporting (3) | `requireAdmin requireInternal requireDev` (:459, :611) | Opal-internal |
| AdvisorIntelligence (4) + `api/endpoints/advi-billing.ts` | bare `ProtectedRoute` (:478-485); `/advisor-intelligence` is in `FIRM_ALLOWED_PATHS` for 49financial, inflection and cottonwood (`portal/src/lib/firmAccess.ts:44+`) | **CLIENT-FACING** |

The client-facing content is ADVI_BILLING's new Advisor Book Fee panel (one billed quarter's fee, computed vs the Schwab
debit; commits f0a301c1, 29b18a8c, 6d383958) mounted on /advisor-intelligence. `/prod-deploy` ships DEV whole, so item 7's
Opal-internal card cannot go alone.

Two answers Andrew can give: (a) promote DEV whole now; (b) hold until ADVI_BILLING's panel is graded for partner eyes.
Recommendation: (b) for tonight; (a) once 3.0.0_SA_CVO has graded the fee panel on DEV against a real partner login
(the figure is a client's fee). Item 7 parks either way; nothing else waits on it.

Who runs it: `0.0.0_AB_MSTR~DELL1`, as for the last two promotes (bf780f94 2026-10-09, f73f9ab0 2026-10-08), under a
CTO+COO pair; no DT seat is live on dell1.

## dell1-20261011T033641Z-1b2f -- remove 8 MDPF_SECCLASS worktrees

**Ruling: YES, exactly as proposed by 2.0.0_SA_COO~M1.** Tag each tip `archive/MDPF_SECCLASS/<branch>`, `git worktree
remove` WITHOUT `--force` (a dirty tree refuses and stays with its owner), then drop the branch names. This is narrower than
the standing word (Andrew 2026-10-08: a merged worktree is force-removed at each drain) and loses no commit: every tip is
tagged first, and a tree with uncommitted files stays. `0.0.0_AB_MSTR~DELL1` executes; the tags are the rollback.

## Reserved to Andrew (unchanged, listed once at tick 1): sitez 058e, 21c5, f0d2, 8ed7, a519 (moot, closing); dell2 01c5, 3cb1, fbb1.
