# IRPT: moving the P/M/Y closer work into IRPT_BCKEND under canonical flow, and a restart check on DSGN_IRPTV1

**Author:** 4.0.0_SA_CRO. **Status:** DRAFT for Andrew's review; it goes to 1.0.0_SA_CTO on his word.
**Measured:** 2026-09-24, 11:50 AM-12:15 PM ET, on this laptop. All times are US Eastern (UTC-4).
**Kind:** a brief. It changes nothing by itself; every act below names its owner.

**Andrew-direct at the 4.0.0_SA_CRO terminal, ~11:5x AM ET, verbatim:**
> CRO~A is issuing two briefs to CTO now which will cover implementation upgrades to process architecture and agent
> fabric ops. In the interim, I want you to assess those two documents, and draft a brief specific to current state on
> the IRPT work that has been done, in essence what must be done to pull the remaining workstreams from the /closer work
> that COO~P ~M ~Y were doing into IRPT_BCKEND so we can return to canonical-flow for that work, and then the work that
> COO~D was doing on DSGN_IRPTV1 should be good as is for a clean restart, but check on it anyway.

The two documents:
- **Report 2** (RCN-0017, `4.0.0_SA_CRO~A`):
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`.
- **Report 3** (RCN-0016, `4.0.0_SA_CRO~B`, amended by ~A):
  `docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md`.

Both are at HEAD `0ee6f5849b`. Section 5 assesses them.

---

## 0. The answer

1. **Returning now is an EARLY hand-back, and the record should say so.**
   - The closer's contract says "Hand-back only after every required journey is proven". CTO `CONTROL.md` reads "All
     three products INCOMPLETE".
   - No tab journey has passed live end to end. Holdings is one signed-in read from it (Andrew's HAR).
   - Andrew's word can hand back early: it is the closer's own authority. Nothing is lost at the hand-back: the three
     unfinished journeys become IRPT_BCKEND's outcomes.
2. **The frontend has already left the closer.** Andrew's 11:31 AM ET answer at the CTO terminal (record
   `ANDREW_DIRECT_20260924_153xZ_IRPT_FRONTEND_CANDIDATES_HAND_TO_COO_D.md`) makes 2.0.0_SA_COO~D the one integrator of
   IRPT portal frontend onto DEV. ~P, ~M and ~Y keep the backend. So:
   - **IRPT_BCKEND** = the backend, in canonical;
   - **DSGN_IRPTV1** = the frontend, in canonical under ~D;
   - **IRPT_FNTEND** closes SUPERSEDED (call 2).
3. **Five phases, in order:** A freeze the three closer seats; B put their code on the trunk; C re-point IRPT_BCKEND's
   records; D re-seat under the three-COO cap; E cut round 19 from the seats' next-lists.
   - **Phase B is the hard part:** three seat branches carry 250, 236 and 45 commits that CLOUD does not have,
     including the source of every IRPT function served today. Canonical workers branch from CLOUD, so until this lands
     they build on code that is not deployed.
4. **DSGN_IRPTV1 is clean to restart as is.** All code is merged and inside origin/DEV, and nothing is stranded. Five
   open items remain (section 4); none blocks the restart.
5. **Three calls for Andrew** (section 6):
   - does today's word lift his 09-22 IRPT hold for IRPT_BCKEND;
   - close IRPT_FNTEND into DSGN_IRPTV1;
   - which seats run under the three-COO cap.

---

## 1. Where the closer stands (measured)

Sources: CTO `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTROL.md` (last commit
`98ad89c5c9`, 09:43 AM); each seat's STATUS **on its own branch** (see section 2); the delivery ledger.

| Tab (owner) | Served today | First failing hop / what closes it | Still required after that |
|---|---|---|---|
| **Holdings** (~M) | All three firms' labelled holdings publications are live: COT `dec293d6`, 49F `3d59c80b` + units `5a25ae76`, INF `d03e91a4` + units `d32e50c6`. `irpt-holdings` fired 6 times clean at 9:36 AM in a signed-in session. | M's STATUS (10:05 AM, its branch): "fired, envelope unread -- Andrew's HAR read in place closes it"; "Nothing further owed by M on the build side". | The snapshot model overlay; the 49F Tax runner (`c354c33a92`, awaiting CTO review); the NOT_READY reason vocabulary; receipting the two retained captures under the holdings migration project (card 6). |
| **Performance / Reporting** (~P) | `irpt-performance-adapter` `07lSH03z`, `irpt-status`, `irpt-ycharts-generate`, `irpt-directory-search`, `irpt-holdings`, two history routes, the upload route. Portal candidates 1-7 are on DEV. | The one-use plan for Anna (YTD) was ARMED at 9:12 AM and **expires 8:00 PM ET today**. It fires on Andrew's signed-in click of one account. The served log line for SELECTION_UNSUPPORTED is the uncommitted `_authz` fix (crash step A1). | The retained report, reopen (P-REOPEN-01 key shape), export and the branded PDF (render chain not proven), X10 enforcement, and the 49F SmartX and INF Orion paths, both on Andrew's per-use words. |
| **Analysis** (~Y) | The resident has run since 5:39 AM, with the session captured and graded. The three Analysis routes are served. Custody interpreter `47b2adf6df` + `b398d27731` is built and CTO-accepted. | NOT LIVE. Hop 2 (the upload composition, P's design card) and hop 4 (the custody composition, P, behind a ledgered FIRM-bucket grant plan) are missing. The first live submission is Andrew's browser act. | Y1-Y7 per Y's STATUS: most are OFFLINE ONLY or NOT STARTED live. |
| **Shared** (~P) | P's installation branch is the deploy source. The DirectoryPage v1 contract is on the backend (`914044f869`). | Portal candidate 8 is uncommitted (crash step A2); by Andrew's 11:31 word it goes to ~D. | -- |

**Holdings is the thread.** Andrew's signed-in HAR, the act he was about to take, is the read that makes it IRPT_BCKEND's
live FWD-1. That fits spine v3.16: "round 1 builds the thread; every later round enriches".

---

## 2. Where the code and records are (measured)

**Trunk:** local CLOUD `0ee6f5849b`; origin/CLOUD `19a22f2f51` (ls-remote 11:52 AM; site Z keeps pushing).

| Seat branch (worktree) | Tip | Ahead / behind CLOUD | Product paths changed | Dry-run merge into CLOUD |
|---|---|---|---|---|
| ~P `irpt-smoke-p-backend-20260923` (`C:\Users\AndrewBerman\Desktop\irpt-smoke-p-backend-20260923`) | `a6a1ec3d3b` | **250** / 1675 | 163 (ycharts 41, performance 19, intake 15, reports 13, _scope 11, holdings 9) | **1 conflict: `.owned-paths.yaml`** |
| ~P `irpt-p-publish-20260923` | `bf090cb303` | 238 / 1675 | -- | contained in the branch above |
| ~M `codex/irpt-m-completion` (`C:\Users\AndrewBerman\Desktop\ajb_irpt_m`) | `da6d4e9365` | **236** / 1675 | 159 (incl. `data/assets/scripts/gold/investor_reporting` 17) | clean |
| ~Y `irpt-mvp-y-20260922` (`C:\Users\AndrewBerman\Desktop\irpt-mvp-y-20260922`) | `b398d27731` | **45** / 1883 | 79 (ycharts 41, intake 17, ops 8) | clean |

**Between the branches (dry-run `git merge-tree`):**
- P x M: clean.
- **P x Y: 1 conflict**, `intake/custody_interpreter.py`. P holds the cherry-pick of `47b2adf6df`, while Y holds
  `b398d27731` on top of it. This is crash step A3 not yet done; the CTO ruled P cherry-picks it (100712).
- **M x Y: 3 conflicts**, `ycharts/generate/recipe.py`, `transport.py` and `tests/test_resident_worker.py`. M's branch
  carries copies of Y's surface.
- **Patch-equivalence** (`git cherry`): 73 of M's commits and 25 of Y's have no equivalent in P's branch. P consumed
  pins by cherry-pick, so each branch holds unique work.

**Records are on the branches too, which is a trap for anyone reading CLOUD.** The current STATUS files live only on
the seat branches:
- **P:** 9:13 AM on its branch; CLOUD's copy dates from 09-23 2:48 AM.
- **M:** 10:05 AM on its branch; CLOUD's copy dates from 09-22 5:40 PM.
- **Y:** its current STATUS is on CLOUD (10:14 AM).

`CONTROL.md` (29 KB) and `RULINGS.md` (386 KB) are on CLOUD.

**Portal:** candidates 1-7 are on DEV (origin/DEV `7952976b`, which contains DSGN_IRPTV1 round 2); candidate 8 is
uncommitted.

**IRPT_BCKEND's canonical state:**
- Round 18 compiled (`2506c70874`, 09-22 4:47 PM) and adjudicated: `f82fee6aad`, 09-22 5:16 PM, "AC5 FAIL ... L10
  park under Andrew hold".
- **L10 is parked** under Andrew's 09-22 hold (below).
- The row (`project.json`) still reads round 4 / 09-18, names dead lane `~B`, and carries `closer_contract`.
- **8 task orders are still PENDING:** `IB-rt-6` (13 d), `IB-rtf-3`, `-4`, `-7`, `-10`, `-12`, `-14` (5 d; five of them,
  `-3`, `-7`, `-10`, `-12` and `-14`, issued to `0.7.0_AE_CloudOps~V`), and `IB-rth-7` (3 d).
- Its surprise channel is live: P filed S121-S123 there today.

**The hold** (`ANDREW_DIRECT_20260922_1517ET_IRPT_HOLD_AFTER_CVO_SLUGS.md`), verbatim:
> After you receive the most recent slugs from the CVOs I want you to hold analysis and the canonical flow cycle,
> because we may want to bring in some alterations.

The record's execution line: "Resume analysis/progression only on his further instruction."

---

## 3. What must be done -- in order, one owner per step

### Phase A -- freeze the closer seats (each seat, at its restart)

- **A1 (~P). Finish the crash steps first:**
  - A1: commit the `_authz` fix.
  - A2: commit candidate 8, bring it to origin/DEV's tip, hand it to ~D (Andrew 11:31).
  - A3: `git cherry-pick -x b398d27731`.
  - C1: close or re-affirm `irpt-directory-bootstrap-20260923`, OPEN since 09-23 1:36 PM ET (about 23 h). The crash
    brief's "25 h" was an arithmetic slip.

  Routed by the CTO @`e0d6973af0`.
- **A2 (~P, ~M, ~Y). Commit every work in progress on the seat's own branch, then overwrite STATUS.md.** This is
  report 2's FAST->FULL boundary act, section 7.4. STATUS.md must carry:
  - the pins;
  - **deployed artifact -> source commit, per served function**;
  - open ledger entries;
  - the **next-list in priority order**, which becomes round 19's cells;
  - the Andrew acts in flight.

  Round 19 is cut from these files, so they must be current.
- **A3 (Andrew, then the CTO). Stop the three closer loops.** XXX.md Step 1b-F carries three DIRECTED `/loop 20m` goal
  rows for ~P, ~M and ~Y. Their stop is `/verify SOUND` or Andrew's stand-down. Under canonical they would keep running
  closer-style ticks, and no lease or `closer_contract` read stops a `/goal-set` loop. Andrew's stand-down ends them,
  and the CTO strikes the rows (call 3).

### Phase B -- the trunk (0.0.0_AB_MSTR, one safe-merge window per branch)

- **B1. Drain order:** ~P's installation branch first (the deploy source; it contains `irpt-p-publish`), then ~Y's,
  then ~M's. Each gets its own `.tools/safe-merge.sh` window; today's B2 window ran about 25 minutes (open 11:14,
  close 11:38).
- **B2. The conflict rule is the contract's writer table: the SEMANTIC owner's bytes win on its surface.**
  - Y: `ycharts/**`, `intake/**` semantics.
  - M: holdings, custody and `data/assets/scripts/gold/investor_reporting/**`.
  - P: shared auth, routes, IaC and packaging.
  - The CTO: `.owned-paths.yaml`, resolved in the same act that retires the closer lanes (C6).

  Expected at the act:
  - CLOUD x P: `.owned-paths.yaml` only.
  - Y: clean once A3 has landed on P's branch [inferred; verify at the act].
  - M x Y: the three ycharts files, which take Y's bytes.
- **B3. Proof the trunk carries what is served.** After the drain, every served IRPT function's source must be in
  CLOUD. Check it by the build manifest / source map, **by content, not filename** (CLAUDE.md 22a). This is the one
  precondition for canonical workers.
- **B4. The push is on Andrew's word**, as today.

### Phase C -- the records (1.0.0_SA_CTO unless named)

- **C1. The hold.** The CTO places whether today's word is the "further instruction" for IRPT_BCKEND (call 1).
- **C2. The row.**
  - Remove `closer_contract` (spine: "The field is removed at hand-back").
  - Set `coo_lane` to the seat chosen at call 3.
  - Rewrite `phase` and `blocking` to the measured state above.
- **C3. Close round 18's L10** on the parked slug `f82fee6aad`, folded into C5's addendum: one act, not a second
  analysis.
- **C4 (the issuer COO). Dispose the 8 PENDING orders before any issuance.** Each is flipped `superseded` or
  `cancelled` with its pointer; that is the issuer's right. The refuser counts open orders per project (LD-0521), so a
  round-19 issuance over them deadlocks.
  **Exception: `IB-rtf-3`, the bounded test principal Andrew approved on 09-18.** Carry it into round 19; section 5 G3
  says why.
- **C5. A PRD addendum is the L10 answer.**
  - IRPT_BCKEND's ENDPOINT is re-cut to the closer's three journeys, backend half:
    - **FWD-1** = the Holdings journey for Anna's account, live;
    - Performance and Analysis are the next outcomes;
    - S1-S7 and the P/M/Y acceptance matrices become the enrichment backlog.
  - Under proportionate sign-off only an ENDPOINT change re-signs, so the CVO signs that half once.
- **C6. Grants.** Retire the closer lanes (`IRPT_COMPLETION_P/M/Y`, `IRPT_LIVE_SCOPE_P`, `IRPT_Y_ACCESS_INTEGRATION_P`,
  `IRPT_TAX_MEMBERSHIP_M`) in the commit that re-points the row. Canonical write surfaces are each order's `<paths>`.
- **C7. IRPT_FNTEND** (call 2). Close it SUPERSEDED; it has 0 open orders and its round-15 slug is parked under the
  hold. Its frontend outcomes (FWD-1, 3, 4, 5, 6, 8, 11, 12) re-home to DSGN_IRPTV1. The L3 carriers are the CTO's
  (tree row, generated index, DIRECTIVES.yaml members line).
- **C8. Keep as history:** `CONTROL.md`, `RULINGS.md`, the seat STATUS and INTERFACES files. The addendum cites them.
  IRPT_BCKEND's surprise channel is already in use, so nothing moves. SEQUENCE.yaml already lists IRPT_BCKEND (stage 0).

### Phase D -- seats under the three-COO cap (call 3)

- **The cap:** at most three COO sessions on the laptop, Codex seats included (Andrew 09-14 and 09-23).
- **At the crash four ran:** ~P, ~M, ~Y and ~D. Canonical also adds each COO's worker subagents.
- **Option (b), recommended:** two IRPT_BCKEND workstreams plus ~D, which puts the laptop at the cap. The spine
  allows several workstreams per project with disjoint write surfaces under different lanes.
  - ~P: shared installation, Performance, Analysis composition.
  - ~M: Holdings data and publication -- 49F, INF, Tax, the overlay.
- **~Y folds into ~P's workstream either way.** Y's remaining items are the resident half of RESOLVE_UPLOAD and live
  exercise; both blocking compositions are P's.
- **Option (a):** ~P alone as the IRPT_BCKEND issuer, with M's items as cells. Use it if a COO slot must stay free.

### Phase E -- the first canonical round (the IRPT_BCKEND issuer)

- **E1.** Cut round 19 directly from the frozen next-lists, with no CTO round-18 analysis beyond C3. Report 2's call 5
  approved this shape for FAST->FULL; the CTO places whether it covers a closer hand-back (recommended: yes).
- **E2.** Cells follow the verification diet: at most three mechanical checks, dry-run at the base before the cut
  (report 2 C4) once it lands. Each cell names its risk; nearly every backend cell is `WORLD`.
- **E3.** Andrew's acts in flight are named EXERCISED arms, never waits:
  - the signed-in Holdings HAR;
  - the one-use Performance plan: armed until 8:00 PM today; spent today, or re-armed later on a fresh word;
  - the 49F SmartX capture word and the INF Orion Scope word;
  - the first live Analysis submission from his browser.

---

## 4. DSGN_IRPTV1 -- restart check

**Verdict: clean to restart as is.** Measured:
- **Task orders:** 11 of 12 complete.
- **Code:** every round-2 worker commit is inside origin/DEV `7952976b`, and the three worker worktrees hold only
  scratch files. Nothing is stranded.
- **Rows:** 22 in `INVESTIGATION_v1.md`, 7 of them labelled ARMED. Read by content, only 2 are open:
  - **S6:** black treemap tiles and a CUSIP rendered as a name.
  - **S7:** 8 new failures in the legacy `fe-s` suites, which CI does not run.

  The rest are closed by a later carrier:
  - S1 and S3 are disarmed by S2 and S4;
  - S5 by the amendment `49dc5d9216`;
  - W3-S2 by the CTO (CONTROL batch 36);
  - W1-S1 is a merge-union note.

Five items for the restart; none blocks it:

1. **Round-2 L8-L10 is owed.**
   - The CVO has been deaf since 8:59 AM. Its 6 unread messages include CTO 100626 and 100632, which say how to grade
     IVE2-AC4.
   - The round landed on DEV ahead of L8/L9 on Andrew's word, so L9 grades the landed candidate.
   - Round 2's 16 rows are unadjudicated.
2. **`IV-e-7`, the join cell, is PENDING and was never started.**
   - It blocks the round's terminality.
   - The issuer supersedes it with its pointer. Report 2 section 4.3 says to cut join cells and fold the whole-page
     sweep into the merge step.
   - The alternative is to re-cut it in round 3.
3. **S6 and S7 go to round 3's work list**, as their disarm owner states.
4. **The row is stale.**
   - `blocking` still describes the pre-landing cut.
   - The scope line says "owns ... `portal/src/pages/InvestorReporting/**` only". The integrator role from Andrew's
     11:31 AM word (CTO record `cf59de98c0`) and, under call 2, the re-homed IRPT_FNTEND outcomes belong in the row
     and the PRD. These are CTO L3/L4 carriers.
5. **Still owed:**
   - FWD-1's trace (Andrew's signed-in walk of Anna on DEV).
   - Serving 5174 from the main portal checkout (DEV `7952976b`), no longer `C:\tmp\dev-land`.
   - When the CTO lands report 2's `/drive-mode`, DSGN_IRPTV1 is its named first FAST exercise.

---

## 5. Assessment of reports 2 and 3

**What holds up.**
- Both reports measure and print their denominators.
- The joint model is coherent: presence decides pace and reviewer; `<risk>` plus a size floor decides checking; one real
  run of each outcome at close.
- Report 2's one-driver-per-surface rule (C1) removes today's DSGN/closer collision on five `InvestorReporting` files.
- C4 (dry-run each check at the base before the cut) is the cheapest high-yield change in either report; 9 of 29
  orders broke on their own checks.
- Report 3's contradiction table is accurate. Item 1 is live at every startup: XXX.md bans the Task agent in its first
  lines while L7 runs on worker subagents.

**Six gaps, each measured here:**

| # | Gap | Evidence | Fix |
|---|---|---|---|
| G1 | **A closer hand-back has no boundary act.** Report 2 defines FAST->FULL (7.4) and says `closer_contract` "stays what it is" (7.5). Today's IRPT return is exactly the missing case. | Phases A and E above had to borrow 7.4. | Write the hand-back act once in the spine's Closer subsection when C3 lands: WIP pins, STATUS next-list, drain to trunk, round cut from STATUS. |
| G2 | **Goal loops sit outside the lease.** Fail-closed-to-FULL works only for a seat whose tick reads the lease. | ~P, ~M and ~Y run `/goal-set` `/loop 20m` under DIRECTED rows; nothing in C1/C2 reads them. | At hand-back or a switch, the loop's row is struck (A3), or `/goal-set` reads the lease too. |
| G3 | **"One real run at close" needs a real principal.** For IRPT the real run is a real login, and today only Andrew has one, so C6 becomes a wait on him. | Every signed-in IRPT read so far was Andrew's session (latest 9:36 AM), and the HAR is his act. | IRPT_BCKEND's approved bounded test principal, `IB-rtf-3` (PENDING 5 days), is the missing instrument. Carry it into round 19 so the COO can do the run. |
| G4 | **Stale ARMED labels will break report 3's Wave 1.2 as written.** "Only BLOCKING/ARMED rows gate the close" keys on a label that lags. | DSGN_IRPTV1: 7 ARMED labels, 2 open by content. `1.0.0_SA_CTO~Z` R-78 today: "three state-bearing fields and none is current state". | Key the gate on the disarm carriers (a later row that quotes the id, or the commit), never on `hazard_standing`. |
| G5 | **Branch residency is an unmeasured sink.** Both reports measure CLOUD. | Section 2: the closer's code sat 236-250 commits off-trunk for 1-2 days. Report 3 notes 17,110 backend lines its ratio cannot see. Today's cost: a drain window of about 25 minutes per branch, a crash surface spread over 38 worktrees, and STATUS stale on the trunk. | Extend report 2's C8 (drain per chain) to closer and FAST seats: an accepted pin lands on CLOUD within the hour. |
| G6 | **WORLD-heavy backend gets little relief.** Nearly every IRPT backend cell deploys or grants, so it keeps the CTO's exercised read and a ledger entry. | P's STATUS lists 8 of its own ledgered serving acts between 1 and 8 AM today. | Batch WORLD acts: one ledgered apply per round, not one per cell. |

**Minor points.**
- Report 2's 12-hour sample is frontend-heavy, as it says. Its order-size findings may not carry to backend rounds.
- Report 3's efficiency ratio will read low while code sits on seat branches (G5). Read it after B lands.

---

## 6. Calls for Andrew

1. **The 09-22 hold.** Does today's word ("so we can return to canonical-flow for that work") lift the hold for
   IRPT_BCKEND? **REC: yes, for IRPT_BCKEND only.** IRPT_FNTEND closes instead of resuming (call 2). The CTO places
   it.
2. **IRPT_FNTEND.** Close it SUPERSEDED, with its frontend outcomes re-homed to DSGN_IRPTV1 under ~D? **REC: yes.** It
   matches his 11:31 AM word and replaces the spine's "one product" hand-back with backend = IRPT_BCKEND and
   frontend = DSGN_IRPTV1.
3. **Seats and loops.**
   - (b) ~P and ~M as IRPT_BCKEND workstreams plus ~D on DSGN_IRPTV1, at the cap, with ~Y folded into ~P; or
   - (a) ~P alone.

   The same word stands down the three `/loop 20m` goal loops. **REC: (b)** if no other laptop project needs a COO
   slot now.

---

## Instruments and limits

- **git:**
  - `rev-list --left-right`, `merge-tree --write-tree` (dry runs that touch nothing), `cherry` (patch-equivalence),
    `show <branch>:<path>` for branch-resident STATUS;
  - `to-check.py --all --project` for open orders;
  - the surprise-row JSON parsed and printed.
- **Not measured:**
  - deployed-bytes-to-source per function (that is step B3's own act);
  - AWS state;
  - whether A3 alone clears the P x Y conflict;
  - the CVO's and ~D's process state (not live at the read).
- **Reads, not re-measurements:** `CONTROL.md` and the seats' STATUS figures are cited as their authors wrote them.
