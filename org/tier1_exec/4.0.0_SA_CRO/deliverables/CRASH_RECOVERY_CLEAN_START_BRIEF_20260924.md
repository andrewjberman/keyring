# Crash recovery and clean start point -- laptop, 2026-09-24

**For:** 1.0.0_SA_CTO. **From:** 4.0.0_SA_CRO. **Measured:** 10:26-10:48 ET (14:26-14:48Z). All times ET (UTC-4)
unless marked Z.

**Andrew-direct at the 4.0.0_SA_CRO terminal, verbatim.**
- ~10:2x ET: "We just had an unexpected crash with multiple active workstreams and I want you to research exactly
  where everyone left off on the basis of the recent commits and residue." ... "The first brief I need here is
  essentially a state report on the exact current state of the ajb_workspace and portal repos on the local device,
  looking through all active branches (anything touched locally in the last 6 hours)."
- ~10:4x ET: "Ok I want you to write a brief for CTO that covers not only this state, but how to remediate it, clear
  up residue, and give us a clean start point for continuing on."
- Seats he named as live at the crash: 0.0.0_AB_MSTR, 1.0.0_SA_CTO, 2.0.0_SA_COO~P, ~Y, ~M, ~D, 3.0.0_SA_CVO,
  4.0.0_SA_CRO.

**Scope.** Both repos on this laptop (ajb_workspace + portal), every worktree (20 + 18), every branch with a commit
since 04:27 ET, plus the broker delivery ledger of the seven crashed seats since 09:30 ET. NOT measured: AWS served
state, site Z's local trees, OS processes. The ONE ask of the CTO is at the end.

---

## 0. Verdict

1. **Crash window 10:19-10:22 ET.** The last read by any seat was 10:18:53 (2.0.0_SA_COO~D). This seat's spawn was
   logged at 10:22. [measured: delivery ledger + `org/mcp/agent-spawn-audit.log`]
2. **No git operation was interrupted.** 0 of 38 worktrees holds MERGE_HEAD, CHERRY_PICK_HEAD, REVERT_HEAD,
   rebase-merge/, rebase-apply/ or index.lock. The one leftover is an `AUTO_MERGE` ref in
   `irpt-smoke-p-backend-20260923` from the 10:01 cherry-pick. It is inert and needs no action.
3. **No deploy is half-landed.** Every deploy-ledger entry opened in the window is closed, and each OPEN has its
   CLOSE on CLOUD: ~P's six today (generate-installed-handler, status-owned-history, history-routes, upload-route-host,
   status-edge-a, performance-one-use-plan). [measured: the ledger union across all 20 workspace worktrees]
4. **Stranded uncommitted work: ONE worktree, ~P's installation.** Section 2, steps A1-A2.
5. **Trunks.**
   - Workspace `CLOUD` is DIVERGED from origin: 177 local / 323 origin, split at `f96a0b9dd4` (the 22:21 ET push on
     09-23). Origin is still moving: site Z pushed through 10:26.
   - A dry-run merge (`git merge-tree`) conflicts on exactly ONE path, the `portal` gitlink.
   - Portal: origin/DEV = `a3f4c860`, local DEV = `f1d02f30` (fast-forwardable), gitlink on CLOUD = `f1d02f30`.
6. **Mail in flight.**
   - Three load-bearing messages were never read: 100712 (CTO to ~P), 100713 (~D to CTO), 100714 (~D to MSTR).
   - 3.0.0_SA_CVO has been DEAF since 08:59 at the latest (6 unread), which predates the crash.
7. **Live now** (get_live_agents, 10:41): 4.0.0_SA_CRO, 4.0.0_SA_CRO~A, 4.0.0_SA_CRO~B (the last two starting
   up). Every crashed seat is down.

---

## 1. Where each seat left off

| Seat | Last git act (ET) | Where it stood | Unread at crash |
|---|---|---|---|
| 0.0.0_AB_MSTR | 08:59 `bfe9c40f39` (portal gitlink to candidate 7) | No commit in the 80 minutes before the crash; no live worktree. Owed: gitlink to `a3f4c860`, local portal DEV fast-forward, CLOUD push (on Andrew's word), `install-law-lock.sh` on site Z after the push, broker "acked mail never replays" (`org/mcp/server.py` untouched since 09-10). | 100714, 100715 |
| 1.0.0_SA_CTO | 10:16 `c0c06b1fec` (grant: two exact-file rows at Y pin `b398d27731`) | Law work DONE and committed, LOCAL only: `5142d67675` (10:11, law files cut + LAW LOCK) and `41f50d7424` (10:16, six cuts). Lock wired: `.git/hooks/pre-commit` references law-lock 3x, core.hooksPath is shared by every worktree here. Both order records are at HEAD. Residue: 2 PASS lines uncommitted in `org/law-edit-audit.log`. | 100700 (OFFER-EXHAUSTED), 100713 |
| 2.0.0_SA_COO~P | 10:00 `914044f869` on `irpt-smoke-p-backend-20260923` (DirectoryPage v1 contract) | Mid-work at the crash on (a) an `_authz` public-log-line fix and (b) portal candidate 8, both uncommitted (A1, A2). It had NOT yet read the CTO's order to cherry-pick Y's `b398d27731` (A3). Its installation branch is 250 ahead of CLOUD (not drained, by design). | 100684, 100687, 100694, 100709 (all OFFER-EXHAUSTED), 100712, 100716 |
| 2.0.0_SA_COO~Y | 10:12 `b398d27731` on `irpt-mvp-y-20260922`; 10:14 `0ade171e88` on CLOUD (STATUS) | Custody interpreter built: `47b2adf6df` (COT v1, cherry-picked into P's installation as `a6a1ec3d3b` at 10:01) and `b398d27731` (admits 49financial + inflection behind the installer's word; NOT yet in the installation, `git cherry` prints `+`). Its worktree has no recent uncommitted work. | 100718 |
| 2.0.0_SA_COO~M | 10:05 `da6d4e9365` on `codex/irpt-m-completion` | Clean tree. Waiting on Andrew's signed-in Holdings HAR: "the deployed holdings path fired at 13:36Z ... Andrew's HAR closes it" (card 4 of CTO 100605). Branch is 236 ahead of CLOUD (not drained). | none (10/10 READ) |
| 2.0.0_SA_COO~D | 10:16 `0905374fef` on CLOUD (surprise rows S6/S7) | DSGN_IRPTV1 round 2 drained (chains C 07:26, A 08:57, B 09:52). The candidate `04952bd2` merged into DEV on Andrew's word and was pushed after a pull-merge: origin/DEV = `a3f4c860`, landed AHEAD of round-2 L8/L9. Open rows: S6/S7 (8 new legacy fe-s failures that CI does not run; black treemap tiles; a CUSIP rendered as a name). `TO-IV-e-7` (the join cell) is PENDING. `localhost:5174` was served from `C:\tmp\dev-land`. | none (2/2 READ) |
| 3.0.0_SA_CVO | 06:15 `d4e3ccb97f` (DSGN_IRPTV1 round-1 L8-L10 slug `13baec35aa`) | Nothing on any branch after 06:15. Its filesystem inbox holds 6 unread (100605, 100626, 100628, 100632, 100707, 100721) back to 08:59, including its round-2 L9 read instructions (100626 / 100632: grade IVE2-AC4 from the driver's PNG). | 6 (above) |
| 4.0.0_SA_CRO | 08:22 `b74eb87e67` (Analysis brief addendum 3) | This session: the startup audit rewrote `org/audit/archive/FINDINGS.md` (uncommitted). The seat's two worktrees are fully merged (step D2). | n/a (live) |

**Andrew-direct relayed but not yet placed** (100713/100714, from ~D, ~10:0x ET): "also merge this in to the main DEV
branch, you dont need to be working on a feature tree for this work, I think that you should be leading frontend for
IRPT as a whole, none of the other COOs on IRPT are doing fucking anything on frontend anyway." ~D landed the merge. The
seat-scope sentence is the CTO's to place; ~D reads it as no stop on any other seat.

---

## 2. Remediation -- in order, one owner per step, each with the read that closes it

### A. Preserve (the only loss risk -- first)

All in `C:\Users\AndrewBerman\Desktop\irpt-smoke-p-backend-20260923` (DIR), ~P's shared installation. **Nobody
removes, resets or checks out in this worktree until A1-A3 are done.**

- **A1 -- 2.0.0_SA_COO~P -- commit the `_authz` fix.**
  - Files: `infra/aws/lambda/investor-reporting/_authz/errors.py` and `served.py` (modified 10:15), plus
    `_authz/tests/test_public_line_matches_answer.py` (untracked, 10:05).
  - Content, cited in the code: CTO 100681/100696 -- the public log line prints the same `public_reason_code` the
    response carries. Served case: the answer read SELECTION_UNSUPPORTED, the log read UNEXPECTED.
    Attributed to ~P by content and location, not authorship [inferred].
  - Run the new test plus the `_authz` suite, then `safe-commit.sh` on the branch. No deploy is implied.
  - Close: `git -C <wt> status --porcelain -- infra/aws/lambda/investor-reporting/_authz` prints nothing.
  - Also in this worktree, untracked since 08:57: `_contracts/fixtures/SelectedAccounts.valid.json` and
    `.invalid.json`. The `.valid` file is byte-identical to the orphan portal commit `814d7473`'s fixture (A2).
    ~P tracks or deletes them; `.scratch/fe-s-27/positive-control/seeded.ts` is scratch.
- **A2 -- 2.0.0_SA_COO~P -- save portal candidate 8.**
  - `...\irpt-smoke-p-backend-20260923\portal` (DIR) is on branch `irpt-dev-candidate-8-20260924`, created 10:03
    from `f1d02f30`. It holds two untracked files: `src/pages/InvestorReporting/contracts/wire/DirectoryPage.ts` and
    `fixtures/wire/DirectoryPage.valid.json` (10:06-10:09). Neither exists on origin/DEV.
  - Commit them on the candidate branch. Then bring the candidate up to origin/DEV `a3f4c860` (24 commits ahead of
    its base, including DSGN_IRPTV1 round 2, which touches InvestorReporting). A merge is simplest; the branch is
    scratch, so a rebase is also legal. Re-run the candidate's suites on the new tip.
  - Decide the orphan `814d7473`, which sits only on `irpt-dev-candidate-7-20260924` in
    `C:\Users\AndrewBerman\Desktop\portal-dev-consolidation-20260924`. It is a SelectedAccounts fixture re-copy that
    differs from origin/DEV by 2 lines and is NOT in origin/DEV. Fold it into candidate 8 or drop it.
  - Close: both files tracked on the candidate branch; its merge-base with origin/DEV = `a3f4c860`.
- **A3 -- 2.0.0_SA_COO~P -- apply Y's pin (CTO 100712, never read by P).**
  - `git cherry-pick -x b398d27731` onto `irpt-smoke-p-backend-20260923`, AFTER A1 (same worktree, clean tree
    first). The grant `c0c06b1fec` is on CLOUD.
  - The production default stays Cottonwood-only until P's ledgered apply names all three firms' objects (100712).
  - Close: `git cherry irpt-smoke-p-backend-20260923 b398d27731` prints `-` (today it prints `+`).

### B. Trunks (0.0.0_AB_MSTR)

- **B1 -- fast-forward local portal DEV.** In `C:\Users\AndrewBerman\Desktop\ajb_workspace\portal`:
  `git merge --ff-only origin/DEV`. Measured safe: all 254 dirty entries are untracked, and 0 of them collide with the
  36 files the fast-forward changes. Close: `git -C portal rev-parse DEV` == `git ls-remote origin DEV`.
- **B2 -- pull-merge CLOUD (never rebase), then push on Andrew's word.**
  - Use `.tools/safe-merge.sh` in the shared tree. Measured beforehand:
    - The dry-run conflicts on ONE path, `portal`: ours `f1d02f30`, theirs `c7b022a1`, base `c1ac41ecc1`. Resolve
      to origin/DEV's tip, which contains both (`a3f4c860` at 10:4x; ancestry measured).
    - The 10 dirty tracked files in the main tree overlap origin's 645 changed paths 0 times.
    - 0 of 1,453 untracked files collide with origin.
    - CLAUDE.md / org/XXX.md / `.tools/git-hooks/` changed on OUR side only, so the merge commit should not stage
      them against its first parent and the law lock should not fire [inferred; verify at the act -- if it
      refuses, the order record is `ANDREW_DIRECT_20260924_141xZ_YES_TO_ALL_SIX_PROCESS_CUTS.md`].
  - The push is Andrew's word (LD-0522). It also delivers the law cut and the lock to site Z (unlocked there until
    then). Afterwards MSTR runs `bash .tools/git-hooks/install-law-lock.sh` there (CTO 100707).
  - Close: `git rev-list --left-right --count origin/CLOUD...CLOUD` reads `N 0` at push time. Site Z keeps moving,
    so the laptop's half is the 0.
- **B3 -- the gitlink.** B2's resolution of `portal` to `a3f4c860` IS the owed LD-0613 gitlink chore for round 2. If
  B2 waits for Andrew, land the chore alone now.
  Close: `git ls-tree CLOUD portal` == `git -C portal rev-parse DEV` == origin/DEV.

### C. Ledgers and records

- **C1 -- 2.0.0_SA_COO~P -- the one genuinely OPEN deploy entry.**
  - `irpt-directory-bootstrap-20260923`, opened by ~P 09-23 13:36 (25 h), is OPEN at the tip of P's live branch.
  - Measure its artifact, then close it (SUPERSEDED if world-done) or re-affirm it with a reason.
- **C2 -- 2.0.0_SA_COO~M at its drain.** Two stale OPEN copies ride at the tip of `codex/irpt-m-completion`:
  - `irpt-resident-cutover-20260924`, closed by ~P at `8c05e5a321` (05:46);
  - `irpt-performance-reconcile-20260924`, closed at `3bcf720f31` (02:07; that commit's subject names
    irpt-holdings-schema, and it deletes this file too).
  - They are branch vintage, not open deploys: M never modified them, so a 3-way merge takes P's deletion [inferred;
    verify at the drain]. Do NOT close them a second time.
- **C3 -- record logs.** Routine logs, committed by their owners on their normal cadence; none blocks anything:
  - 1.0.0_SA_CTO: `org/law-edit-audit.log` (2 lines).
  - 4.0.0_SA_CRO: `org/audit/archive/FINDINGS.md` (startup audit).
  - `org/mcp/agent-spawn-audit.log`.

### D. Residue (older than the crash; NOT blocking; clean when convenient)

- **D1 -- main-tree edits dated 09-23 or earlier (36 h+).**
  - Files and presumed owners:
    - `org/tier0/ledger/LD-0550.md` (+56; MSTR)
    - `org/tier1_exec/2.0.0_SA_COO/handoffs/2026-09-23_2017Z.md` (+7/-38; COO base)
    - three `.open_deploys` files: `d12-sms-origination-identity-activation.json`,
      `freshguard-leg4-writer-wiring-finish.json`, `.unindexed_red_state.json` (+1/-1 each; status unchanged,
      HELD-SOVEREIGN-GATED)
    - `org/modules/graph/nerves-risk-edges.json` (generated; +33,922/-24,568)
    - `deck_generation/prompt_view.py` (+6)
  - Measured: none matches any earlier committed version of itself, so these are real unfinished edits and not
    stale copies that would revert HEAD. None overlaps B2.
  - Each owner commits or discards. Never bulk-commit them.
- **D2 -- worktree sweep.** Removal deletes a directory: Andrew confirms. Use `/cleanup`; a portal sub-worktree's
  `node_modules` junction needs `rmdir`.

  | Worktree (DIR) | State | Owner / when |
  |---|---|---|
  | `C:\tmp\wk-dsgn_irptv1-2-4`, `-2-5`, `-2-6` (+ each `\portal`) | 0 ahead of CLOUD; the portal heads (`090e5b98`, `04f1aa21`, `97da9e2d`) all in origin/DEV; only `.scratch` outputs | ~D, after round-2 L9 |
  | `C:\tmp\dsgn-irptv1-r2`, `C:\tmp\dev-base`, `C:\tmp\dsgn-irptv1-base` | clean; heads in origin/DEV | ~D / MSTR, now |
  | `C:\tmp\dev-land` | = origin/DEV; **the 5174 dev server's tree** | KEEP until B1 and 5174 is re-pointed |
  | `C:\Users\AndrewBerman\Desktop\cro-listing-speed-20260924`, `cro-holdings-status-20260924` | clean; both tips are ancestors of P's installation branch | 4.0.0_SA_CRO, on the word |
  | `C:\Users\AndrewBerman\AppData\Local\Temp\cvo-p-final-a538-xg9zno5z` (`\backend` + `\portal`) | GUTTED: `\backend` has 40,568 tracked files gone from disk, only `docs/` left; its commit `cd8d118254` is on CLOUD, and `\portal`'s `a5382179` is in origin/DEV | `worktree remove --force` + `prune`; CVO or MSTR |
  | 13 older worktrees (last commit before 04:27 ET today, most 09-18..09-23): `wk-oplgtw-2r2` (4,665 dirty), `wk-taxsma-2c`, `wk-irpt_fntend-15-1/-2`, `wk-mdpf-autocustom-pin` (9 ahead), `wk-aeo-recorder-scope` (7 ahead), `mstr-naming-waiver` (detached), `ajb_irpt_m_rp10`; portal: `portal-local-live-20260923`, `irpt-smoke-p-portal-20260923` (34 dirty), `ajb_irpt_m_live_portal` (6 ahead), `irpt-mvp-y-portal-20260922`, `ajb_irpt_m_portal` | not crash residue; some hold unmerged commits or dirty files | each owner's word; NOT part of the restart |

---

## 3. Restart order

Each seat runs `/watcher` and the XXX.md startup. **B.0 (delivery ledger) runs with `since=2026-09-24T13:30:00Z`**
(the CVO uses `12:00:00Z`, since it was deaf from 12:59Z). The later last-read time is NOT a safe start: ~P's unread
rows date from 13:55Z, before its last READ at 14:14Z. B.0 reads every row the seat did not READ -- including
OFFER-EXHAUSTED rows, which `check-inbox` cannot see -- and acks from the Msg-ID line.

1. **0.0.0_AB_MSTR:** B1, B3, then B2 to Andrew for the push word. Reads 100714, 100715.
2. **1.0.0_SA_CTO:** this brief; places Andrew's seat-scope word to ~D (100713); reads 100700.
3. **2.0.0_SA_COO~P:** A1 -> A3 -> A2 -> C1. Reads 100684, 100687, 100694, 100709, 100712, 100716.
4. **2.0.0_SA_COO~Y:** nothing stranded. Its pin's integration is P's act (A3); resume from STATUS `0ade171e88`.
   Reads 100718.
5. **2.0.0_SA_COO~M:** clean; resumes waiting on Andrew's signed-in Holdings HAR.
6. **2.0.0_SA_COO~D:** re-serve 5174 from DEV's tip; rows S6/S7; `TO-IV-e-7`; then the round-2 drain packet to the
   CVO.
7. **3.0.0_SA_CVO:** a FRESH `/watcher` (deaf since 08:59); read the 6 unread; round-2 L8-L10 once ~D's packet lands.
8. **4.0.0_SA_CRO:** live. Open item: confirm whether card 2's second read of the one-use Performance result (100605)
   is owed -- the plan was ARMED at 09:12; this seat has not read a served result.

## 4. The clean start point -- DONE WHEN (each line is one read)

| # | Condition | The read |
|---|---|---|
| S1 | No stranded edits in P's installation | `git -C ...\irpt-smoke-p-backend-20260923 status --porcelain -- infra/aws/lambda/investor-reporting/_authz` empty; candidate-8 files tracked |
| S2 | Y's pin applied | `git cherry irpt-smoke-p-backend-20260923 b398d27731` prints `-` |
| S3 | One portal DEV | local DEV == `git ls-remote origin DEV` == `git ls-tree CLOUD portal` |
| S4 | CLOUD not behind at push | `origin/CLOUD...CLOUD` reads `N 0` after B2 and the push on Andrew's word |
| S5 | No OPEN ledger over a world-done artifact | `irpt-directory-bootstrap-20260923` closed or re-affirmed by ~P |
| S6 | Every seat hearing | each seat: its Monitor running + B.0 read since 13:30Z (CVO 12:00Z), unread ids above acked |
| S7 | Merged scratch worktrees gone | the "now" rows of D2 removed on Andrew's confirmation |

---

## Instruments and limits

- **git:** `worktree list --porcelain` + `status -uall` + `rev-list --left-right` per worktree, via one script (38 of
  38 read). `merge-tree --write-tree` was the dry run. The union of `ls-tree` over `.open_deploys` covered all 20
  workspace worktrees. `git cherry` for patch equivalence.
- **Broker:** `get_delivery_state` per seat since 13:30Z; `check_inbox` without mark_read (inspection only).
- **One write to shared state:** `git fetch origin CLOUD` moved only the tracking ref, `d6c05a7a49` ->
  `e116ed8aa4`. No local branch or worktree changed.
- **Trap avoided:** every older workspace branch shows a reflog mtime of 09:43:42, a gc pass, not activity. Branches
  were dated by tip commit.
- **Not measured:** AWS served state (no ledger open in the window, so no move is expected; none re-read); whether
  DEV `a3f4c860` is deployed to opalinvest.dev; site Z's trees; orphan OS processes (watchers, the 5174 server) --
  `/kill scripts` dry-run shows them.
- **Not this seat's to place:** 4.0.0_SA_CRO~A and ~B registered at 10:39-10:41.

## The ask

**1.0.0_SA_CTO: adopt section 2's order and route each step to its named owner at restart.** Steps A1-A3 (~P) come
first because they are the only loss risk. The B2 push stays Andrew's word.
