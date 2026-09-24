# IRPT: moving the P/M/Y closer work into IRPT_BCKEND under canonical flow, and a restart check on DSGN_IRPTV1

**Author:** 4.0.0_SA_CRO.
**Status:** v2. Andrew answered its five calls at ~12:4x PM ET; the answers are applied throughout. Sent to
1.0.0_SA_CTO on his word ("Yes once you've adjusted as needed based on these statements"). Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_164xZ_IRPT_RETURN_FIVE_CALLS_ANSWERED.md`.
**Measured:** 2026-09-24, 11:50 AM-12:45 PM ET, on this laptop. All times are US Eastern (UTC-4).
**Kind:** a brief. It changes nothing by itself; every act below names its owner.

**Andrew's answers to the five calls, verbatim (~12:4x PM ET):**
> 1.) Yes IRPT_BCKEND is fine to open up. We do not need to move it if the seats in question are positioned with the
> right context to close out all the journeys. If it is more cogent to just run it to closed journeys across all three
> channels, that is totally fine, there is not a rush to migrate, the crux is dependent on whichever has a higher
> efficacy. 2.) I would run all 3 COOs on IRPT_BCKEND, limit doesnt matter, COO~D runs in parallel on DSGN_IRPTV1.
> 3.) Yes. 4.) Yes once you've adjusted as needed based on these statements. 5.) Yes.

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

## 0. The answer (v2, on Andrew's five answers)

1. **Settled by Andrew:**
   - the 09-22 hold is lifted for IRPT_BCKEND;
   - all three COOs (~P, ~M, ~Y) stay on IRPT_BCKEND, with ~D in parallel on DSGN_IRPTV1 ("limit doesnt matter");
   - IRPT_FNTEND closes SUPERSEDED into DSGN_IRPTV1.

   Migration is NOT required: "the crux is dependent on whichever has a higher efficacy".
2. **REC on efficacy: finish the three journeys under the closer, then hand back to IRPT_BCKEND canonical rounds for
   enrichment.** That is the spine's own hand-back point ("once the thread and the named journeys pass live"). Why,
   measured:
   - **What is left to close each journey is mostly Andrew's acts and ~P-owned compositions, not cell-sized builds.**
     - Holdings: one signed-in read. ~M: "Nothing further owed by M on the build side".
     - Performance: one signed-in click on the plan armed until 8:00 PM ET today, then the retained report, reopen and
       export.
     - Analysis: two ~P compositions, ~Y's resident half, and one browser submission.
   - **The seats hold the context:** per-seat STATUS and INTERFACES, and 386 KB of CTO rulings. A canonical worker
     gets one task-order face.
   - **Migrating first costs setup before any product work:**
     - three drain windows (~25 minutes each, measured today);
     - a PRD addendum and its sign-off;
     - 8 order dispositions;
     - a round-19 decomposition and issuance.

     Report 2 measured 2 h of setup for a new project and 3-6 h per round. [INFERRED: hours of delay on work that is
     one read, one click and two compositions from done.]
   - **The closer's measured cost is CTO turnaround and message volume** (report 2 section 5.2), which today's Rule 31
     already cuts.

   **Switch criterion (a judgment, not a gate):** if a journey stops moving, the CTO moves that journey's remaining
   work to canonical at that point by section 3.
3. **Three acts now, on either path:**
   - **N1. Back up the seat branches.** **NEW, measured: origin carries exactly ONE branch, `CLOUD`.** ~P's 250
     commits, which hold the source of every IRPT function served today, plus ~M's 236 and ~Y's 45, exist only on this
     laptop's disk, hours after a crash.
     - Drain each branch's current tip to CLOUD now (section 3 Phase B order and conflict rule).
     - After that, drain each CTO-accepted pin within the hour. MSTR pushes on Andrew's word as usual.
   - **N2. Record hygiene on IRPT_BCKEND.**
     - Dispose of the 8 stale PENDING orders, keeping `IB-rtf-3`, the test principal.
     - Close round 18's parked L10 on its slug.
     - Correct the row (`coo_lane`, `phase`, `blocking`).
     - `closer_contract` stays until hand-back.
   - **N3. Close IRPT_FNTEND** (Andrew call 3). Its frontend outcomes re-home to DSGN_IRPTV1.
4. **The frontend has already left the closer.** Andrew's 11:31 AM ET word makes ~D the one integrator of IRPT portal
   frontend onto DEV; ~P, ~M and ~Y keep the backend.
5. **DSGN_IRPTV1 is clean to restart as is** (section 4). All code is merged and inside origin/DEV, and nothing is
   stranded. Five open items remain; none blocks the restart.

---

## 1. Where the closer stands (measured)

Sources: CTO `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTROL.md` (last commit
`98ad89c5c9`, 09:43 AM); each seat's STATUS **on its own branch** (see section 2); the delivery ledger.

| Tab (owner) | Served today | First failing hop / what closes it | Still required after that |
|---|---|---|---|
| **Holdings** (~M) | All three firms' labelled holdings publications are live: COT `dec293d6`, 49F `3d59c80b` + units `5a25ae76`, INF `d03e91a4` + units `d32e50c6`. `irpt-holdings` fired 6 times clean at 9:36 AM in a signed-in session. | M's STATUS (10:05 AM, its branch): "fired, envelope unread -- Andrew's HAR read in place closes it"; "Nothing further owed by M on the build side". | The snapshot model overlay; the 49F Tax runner (`c354c33a92`, awaiting CTO review); the NOT_READY reason vocabulary; receipting the two retained captures under the holdings migration project (card 6). |
| **Performance / Reporting** (~P) | `irpt-performance-adapter` `07lSH03z`, `irpt-status`, `irpt-ycharts-generate`, `irpt-directory-search`, `irpt-holdings`, two history routes, the upload route. Portal candidates 1-7 are on DEV. | The one-use plan for Anna (YTD) was ARMED at 9:12 AM and **expires 8:00 PM ET today**. It fires on Andrew's signed-in click of one account. The served log line for SELECTION_UNSUPPORTED is the uncommitted `_authz` fix (crash step A1). | The retained report, reopen (P-REOPEN-01 key shape), export and the branded PDF (render chain not proven), X10 enforcement, and the 49F SmartX and INF Orion calls. Andrew worded each ONCE on 09-23 ~8:4x PM ET (`RULINGS.md` "all recs approved", items 5-6), bound at execution to the exact request P presents. |
| **Analysis** (~Y) | The resident has run since 5:39 AM, with the session captured and graded. The three Analysis routes are served. Custody interpreter `47b2adf6df` + `b398d27731` is built and CTO-accepted. | NOT LIVE. Hop 2 (the upload composition, P's design card) and hop 4 (the custody composition, P, behind a ledgered FIRM-bucket grant plan) are missing. The first live submission is Andrew's browser act. | Y1-Y7 per Y's STATUS: most are OFFLINE ONLY or NOT STARTED live. |
| **Shared** (~P) | P's installation branch is the deploy source. The DirectoryPage v1 contract is on the backend (`914044f869`). | Portal candidate 8 is uncommitted (crash step A2); by Andrew's 11:31 word it goes to ~D. | -- |

**Holdings is the thread.** Andrew's signed-in HAR, the act he was about to take, is the read that makes it IRPT_BCKEND's
live FWD-1. That fits spine v3.16: "round 1 builds the thread; every later round enriches".

---

## 2. Where the code and records are (measured)

**Trunk:** local CLOUD `0ee6f5849b`; origin/CLOUD `19a22f2f51` (ls-remote 11:52 AM; site Z keeps pushing).

**Origin holds none of the seat branches.**
- `git ls-remote --heads origin` at 12:40 PM lists **1 head, `CLOUD`**. The glob form read `refs/heads/CLO*` prints
  `CLOUD` as a positive control.
- Every branch below exists only on this laptop.

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

## 3. The hand-back procedure -- in order, one owner per step

**When it runs (v2).**
- On the recommended path it runs at journey close.
- For a journey the CTO moves early (the section 0 switch criterion), it runs at that point.
- Three pieces run NOW on either path: N1 is Phase B, N2 is C3 and C4, N3 is C7.
- Phase D is settled by Andrew.

### Phase A -- freeze the closer seats (each seat, at hand-back; A1 at its restart)

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
- **A3 (each seat, then the CTO). The three closer loops end at their own stop.** XXX.md Step 1b-F carries three
  DIRECTED `/loop 20m` goal rows for ~P, ~M and ~Y. On the recommended path the loops ARE the mechanism that runs the
  journeys to close, and their stop is `/verify SOUND` on each goal. At that stop the lane deletes its cron and the CTO
  strikes the row.
  - A journey moved early needs Andrew's stand-down of that one loop. No lease or `closer_contract` read stops a
    `/goal-set` loop.

### Phase B -- the trunk (0.0.0_AB_MSTR, one safe-merge window per branch) -- NOW (N1), then per accepted pin

**Why now:** the three branches are local-only (section 2), and the laptop crashed this morning. Draining them is
integration, not migration: the closer keeps running on its branches after each drain.

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

- **C1. The hold: DONE.** Andrew lifted it for IRPT_BCKEND at ~12:4x PM ET ("Yes IRPT_BCKEND is fine to open up").
- **C2. The row.**
  - NOW: rewrite `phase` and `blocking` to the measured state above, and set `coo_lane` to name the three workstream
    lanes ~P, ~M and ~Y.
  - AT HAND-BACK: remove `closer_contract` (spine: "The field is removed at hand-back").
- **C3. NOW (N2): close round 18's L10** on the parked slug `f82fee6aad`. The hold that parked it is lifted, and closing
  it now keeps the hand-back to one act.
- **C4. NOW (N2), the issuer COO: dispose the 8 PENDING orders.** Each is flipped `superseded` or `cancelled` with its
  pointer; that is the issuer's right.
  - They are 3-13 days old, and the refuser counts open orders per project (LD-0521). Left open, they deadlock any
    later issuance and would register false overlaps under report 2's C1 check.
  - **Exception: `IB-rtf-3`, the bounded test principal Andrew approved on 09-18.** Keep it live. Section 5 G3 says
    why: it lets a seat make the real signed-in run without Andrew, on either path.
- **C5. AT HAND-BACK, a PRD addendum is the L10 answer.**
  - IRPT_BCKEND's ENDPOINT is re-cut to the closer's three journeys, backend half:
    - **FWD-1** = the Holdings journey for Anna's account, live;
    - Performance and Analysis are the next outcomes. On the recommended path they are already closed, and they
      grade REALIZED from the closer's pinned live traces.
    - S1-S7 and the P/M/Y acceptance matrices become the enrichment backlog.
  - Under proportionate sign-off only an ENDPOINT change re-signs, so the CVO signs that half once.
- **C6. Grants.** Retire the closer lanes (`IRPT_COMPLETION_P/M/Y`, `IRPT_LIVE_SCOPE_P`, `IRPT_Y_ACCESS_INTEGRATION_P`,
  `IRPT_TAX_MEMBERSHIP_M`) in the commit that re-points the row. Canonical write surfaces are each order's `<paths>`.
- **C7. NOW (N3): IRPT_FNTEND closes SUPERSEDED** (Andrew call 3, "Yes"). It has 0 open orders, and its round-15
  slug is parked under the hold. Its frontend outcomes (FWD-1, 3, 4, 5, 6, 8, 11, 12) re-home to DSGN_IRPTV1. The L3 carriers are the CTO's
  (tree row, generated index, DIRECTIVES.yaml members line).
- **C8. Keep as history:** `CONTROL.md`, `RULINGS.md`, the seat STATUS and INTERFACES files. The addendum cites them.
  IRPT_BCKEND's surprise channel is already in use, so nothing moves. SEQUENCE.yaml already lists IRPT_BCKEND (stage 0).

### Phase D -- seats: SETTLED by Andrew

- **All three COOs, ~P, ~M and ~Y, run on IRPT_BCKEND, and ~D runs in parallel on DSGN_IRPTV1:** four COO sessions on
  the laptop. "limit doesnt matter" is recorded as spoken, for this seating.
- **Under canonical (at hand-back)** the three are three WORKSTREAMS of IRPT_BCKEND. The contract's writer table is
  already their disjoint write-surface split:
  - ~P: shared auth, routes, IaC and packaging, plus Performance/Reporting;
  - ~M: Holdings custody, publication and the gold holdings snapshot;
  - ~Y: upload, resolution, the resident and the Analysis job semantics.

  Each workstream issues its own rounds for its own scope. The spine's rule is "ONE ISSUER PER ROUND; a WORKSTREAM is
  a SCOPE, not a round".

### Phase E -- the first canonical round (each workstream issuer, at hand-back)

- **E1.** Cut round 19 of each workstream directly from its seat's frozen next-list, with no CTO round-18 analysis
  beyond C3. On the recommended path the journeys are closed by then: they become FWD-1..3 REALIZED at the first
  canonical L10, and the leftover S1-S7 and P/M/Y matrix items are the enrichment backlog. Report 2's call 5
  approved this shape for FAST->FULL; the CTO places whether it covers a closer hand-back (recommended: yes).
- **E2.** Cells follow the verification diet: at most three mechanical checks, dry-run at the base before the cut
  (report 2 C4) once it lands. Each cell names its risk; nearly every backend cell is `WORLD`.
- **E3.** Andrew's acts in flight are named EXERCISED arms, never waits:
  - the signed-in Holdings HAR;
  - the one-use Performance plan: armed until 8:00 PM today; spent today, or re-armed later on a fresh word;
  - the 49F SmartX call and the INF Orion Scope call, each already worded once (09-23 ~8:4x PM ET) and bound at
    execution to the exact request P presents;
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
| G3 | **"One real run at close" needs a real principal.** For IRPT the real run is a real login, and today only Andrew has one, so C6 becomes a wait on him. | Every signed-in IRPT read so far was Andrew's session (latest 9:36 AM), and the HAR is his act. | IRPT_BCKEND's approved bounded test principal, `IB-rtf-3` (PENDING 5 days), is the missing instrument. Keep it live (C4) so a seat can make the signed-in run without Andrew, on either path. |
| G4 | **Stale ARMED labels will break report 3's Wave 1.2 as written.** "Only BLOCKING/ARMED rows gate the close" keys on a label that lags. | DSGN_IRPTV1: 7 ARMED labels, 2 open by content. `1.0.0_SA_CTO~Z` R-78 today: "three state-bearing fields and none is current state". | Key the gate on the disarm carriers (a later row that quotes the id, or the commit), never on `hazard_standing`. |
| G5 | **Branch residency is an unmeasured sink.** Both reports measure CLOUD. | Section 2: the closer's code sat 236-250 commits off-trunk for 1-2 days. Report 3 notes 17,110 backend lines its ratio cannot see. Today's cost: a drain window of about 25 minutes per branch, a crash surface spread over 38 worktrees, and STATUS stale on the trunk. | Extend report 2's C8 (drain per chain) to closer and FAST seats: an accepted pin lands on CLOUD within the hour. |
| G6 | **WORLD-heavy backend gets little relief.** Nearly every IRPT backend cell deploys or grants, so it keeps the CTO's exercised read and a ledger entry. | P's STATUS lists 8 of its own ledgered serving acts between 1 and 8 AM today. | Batch WORLD acts: one ledgered apply per round, not one per cell. |

**Minor points.**
- Report 2's 12-hour sample is frontend-heavy, as it says. Its order-size findings may not carry to backend rounds.
- Report 3's efficiency ratio will read low while code sits on seat branches (G5). Read it after B lands.

---

## 6. Andrew's answers (the five calls are closed)

Record: `ANDREW_DIRECT_20260924_164xZ_IRPT_RETURN_FIVE_CALLS_ANSWERED.md` (this folder).

1. **The hold is lifted for IRPT_BCKEND.** Migration is optional and goes by efficacy. This brief recommends finishing
   the journeys under the closer and handing back at close (section 0 item 2). The CTO places the path.
2. **All three COOs stay on IRPT_BCKEND, and ~D runs in parallel on DSGN_IRPTV1** ("limit doesnt matter", for this
   seating).
3. **IRPT_FNTEND closes SUPERSEDED into DSGN_IRPTV1.**
4. **This v2 goes to the CTO.**
5. **Removed:** `cro-listing-speed-20260924` and `cro-holdings-status-20260924`. Both `worktree remove` calls exited
   rc=0 and both directories are gone. The branches are kept.

**The ask of 1.0.0_SA_CTO:**
- place the path (REC: closer to closed journeys, then hand back);
- route N1-N3 now:
  - N1 to 0.0.0_AB_MSTR;
  - N2 to the IRPT_BCKEND issuer lanes and the CTO's own row edit;
  - N3 is the CTO's own act.

---

## 7. Each seat's direction on return (v2.1)

**Where the expectations and cutoffs already live.** Each seat has an Andrew-direct GOAL record in
`org/tier1_exec/2.0.0_SA_COO/deliverables/`. Each record:
- states **Done = `/verify` SOUND** on numbered criteria;
- names the stop ("`/verify` SOUND on the done criteria, or Andrew's stand-down");
- says "a successor at this seat re-arms off this record while the goal is not DONE".

These records are the per-seat mandate and the cutoff. Andrew's answer 1 ("run it to closed journeys across all three
channels") points at the same end state. No new `/closer trace` is needed: Andrew said to skip it when clear
expectations and cutoffs exist, and they do.

| Seat | Goal record (cutoff) | First act on return |
|---|---|---|
| ~P | `ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`. Done: (1) the signed-in journey, login -> selection -> provider calculation -> retained report -> reopen -> export, for a real client at each of 49F, INF and COT; (2) every active account resolvable; (3) COT structurally sound, window disclosed. | Crash steps A1-A3 and C1 (CTO-routed 100730). Then the COT journey on Anna's plan, armed until 8:00 PM ET today. Then the 49F SmartX and INF Orion calls, each worded once. Then retained report -> reopen -> export. The Analysis compositions Y waits on stay in P's queue: hop 2 upload and hop 4 custody. |
| ~M | `ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`. Done: (1) the signed-in Holdings journey for a real client at each of 49F, INF and COT; (2) every active 49F/INF account resolvable with a snapshot overlay, and every unsupported account refused explicitly; (3) COT soundness disclosed. | Run `/verify` against these three criteria on the served revisions. M's STATUS says the build side is done; criterion (2)'s account census is the untested part. Andrew's signed-in HAR closes (1) for COT. |
| ~Y | `ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`. Done: (1) the real-login 12.03 journey end to end with digests and revisions recorded; (2) the Y1-Y7 matrix, each case with one reconciled trace; (3) no live grade from synthetic or offline evidence. | Nothing is stranded (section 2). Build the resident half of RESOLVE_UPLOAD on P's design card (CTO 100667). The first live submission is Andrew's browser act once one of P's compositions serves. |

**The switch to canonical (section 0 item 2)** is the point where each goal reads `/verify` SOUND. For a journey the
CTO moves earlier, the point is that move.

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
