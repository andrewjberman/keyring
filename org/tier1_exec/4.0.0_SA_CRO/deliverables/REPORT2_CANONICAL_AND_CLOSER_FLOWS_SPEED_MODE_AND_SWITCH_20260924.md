# REPORT 2 -- The canonical flow and the closer flow: where the time goes, how heavy the task orders are, a fast mode, `/closer-drive`, and the switch between them

**Author:** `4.0.0_SA_CRO~A`. **Written:** 2026-09-24, about 11:00 AM-12:00 PM ET. **Kind:** a brief of proposals.
It is NOT a project: no L2-L10, no registration, no task orders. The changes go to `1.0.0_SA_CTO` (the process scribe)
to land, with six calls reserved to Andrew (section 9).

**Commissioned by:** Andrew-direct at this terminal ~10:3x AM ET, verbatim record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_143xZ_REPORT2_CANONICAL_AND_CLOSER_FLOWS_AND_THE_SWITCH.md`.

**Status (2026-09-24 ~11:4x AM ET): APPROVED and sent to `1.0.0_SA_CTO` for immediate implementation.**
- All seven `/open-calls` recs were approved at ~11:3x AM ET, with a GO for C1-C9. Record:
  `ANDREW_DIRECT_20260924_153xZ_REPORT2_ALL_SEVEN_RECS_APPROVED.md`.
- Two joint refinements with report 3 were approved at ~11:4x AM ET. Record:
  `ANDREW_DIRECT_20260924_154xZ_REPORT3_REFINEMENTS_APPROVED_BOTH_REPORTS_TO_CTO.md`.

Both records are in this folder. Section 12 carries the joint model. C6 and section 9 are amended to match, marked
`[AMENDED 09-24]`.

**Point of contact for report 2 AND report 3 (RCN-0016) since ~11:5x AM ET: `4.0.0_SA_CRO~A`.** CRO~B is offline on
Andrew's word. Record: `ANDREW_DIRECT_20260924_155xZ_CRO_A_POINT_OF_CONTACT_REPORTS_2_AND_3_CRO_B_OFFLINE.md`. Where
the text below names `4.0.0_SA_CRO~B` as report 3's holder, it names the author, not the current contact.

**How this fits with the other two reports.**
- **Report 1** is yesterday's brief, `BRIEF_CANONICAL_FLOW_SPEED_CLOSER_FLOW_SKILLS_PARITY_20260923.md` (same folder).
  Its three canonical changes are now law (spine v3.16-v3.18):
  - round 1 builds the live thread;
  - later rounds are enrichment rounds;
  - the verification diet, at most three mechanical checks per task order.

  Its fourth change became the `/closer` skill. This report measures what those changes did in their first full day.
- **Report 3** is the process-debt clean-out. `4.0.0_SA_CRO~B` holds it under Andrew's ~10:4x AM ET word (RCN-0016). This
  report stays inside the two flows' mechanics. Section 4.4 lists what it hands to report 3 instead of re-measuring.
- **Not re-proposed:** today's six process cuts are already law (CLAUDE.md @`41f50d7424`, Andrew's "yes to all" ~10:1x
  AM ET). They are the corroboration cap, test-only portal candidates landing on DEV by their author, issuer amendments
  without a CTO ruling, proportionate PRD sign-off, acked messages not re-delivered, and message discipline. Where a
  finding below is already answered by one of them, the finding says so.

Times are US Eastern. Every figure is **MEASURED** (counted or read, denominator printed) or **INFERRED** (a
classification or an estimate), and is labelled.

---

## 0. The answer

1. **Canonical is slow in EXECUTION, not in hand-offs.**
   - **Sample (MEASURED):** every canonical issuance in the last 12 hours (10:40 PM Wed to 10:40 AM Thu ET): 29 task
     orders in 4 issuances on 2 projects.
   - **Hand-off (MEASURED):** from the CVO's slug to the next round's cut took about 30 minutes on both projects. It
     works; leave it.
   - **Where the rounds' 3-6 hours went (MEASURED):**
     - a fabric-wide usage-limit stall of about 90 minutes;
     - orders queued one after another because they edit the same files;
     - 9 of 29 orders (31%) hit a defect in their OWN checks partway through the round, costing 11-24 minutes each
       where timed;
     - merges running up to about 75 minutes behind the work;
     - 2 hours of setup (5 PRD versions) before the first order of a new project.
2. **The task orders are light-to-moderate coding tasks wrapped in a heavy order.**
   - **Code per order (MEASURED):** median about 220 product lines changed. 10 of 24 orders changed 100 lines or fewer,
     and two changed no product code at all.
   - **Order size (MEASURED):** 11.8 KB on average, of which about a quarter is the build instruction.
   - **Test versus product code (MEASURED):** the workers wrote more test, harness and fixture code (6,967 lines) than
     product code (5,844 lines).
3. **Models: the workers are ALREADY on Sonnet at high effort.**
   - **Workers (MEASURED):** 68 of 68 worker commits in the window carry the Sonnet 5 trailer, and
     `.claude/agents/worker.md` has said `sonnet` / `high` since 09-16. The spine still says Opus, and that text is stale.
   - **The worker model is not where the cost is.**
   - **Where the cost is (MEASURED):**
     - the coordinating seats, on Fable 5.1 and Opus 5.5;
     - 81% of 602 commits in the window are records only;
     - 714 broker messages averaged about 3,000 characters each.

     That volume is what ran into the usage limit.
   - **Proposal:** a second, lighter worker type (Sonnet, medium effort) for the small and batch cells, tried for one
     round. Not Opus at low effort.
4. **The checks missed the defect that mattered.**
   - **What passed (MEASURED):** every mechanical check on the new Holdings map passed, graded on server-rendered
     static markup.
   - **What one look showed:** the first screenshot of the running page showed solid black treemap tiles and a raw CUSIP
     printed as a security name. Row `DSGN_IRPTV1-S6` says no graded artifact could have shown either defect.
   - **So:** one real look at the screen per round (or per candidate) is worth more than a stack of fixture checks, in
     both flows.
5. **The two flows collided on one page.**
   - **Overlap (MEASURED):** in the same 12 hours, the canonical DSGN_IRPTV1 workers and the closer seats `~P` and `~M`
     edited the same 5 product files of the Investor Reporting page.
   - **Cost:** two CTO rulings carving out eleven "touch" exceptions, and a family of "you may change only this one
     line" checks.
   - **Cause:** two drivers on one surface. The switch below removes it.
6. **Switching already happens several times a day, with no carrier.**
   - **Switches in 24 hours (MEASURED), none on the flag the spine defines:**
     - AMGT to closer loops without the `closer_contract` flag;
     - AMGT_RESAPP back to canonical rounds through PRD addenda;
     - DSGN_IRPTV1 landed on DEV partway through a round on your word, "you dont need to be working on a feature tree
       for this work".
   - **The flag itself:** only 2 of 26 project rows carry `closer_contract`.
7. **The proposal: ONE driver per project at a time, chosen by a MODE LEASE.**
   - **FAST:** you are at the computer. `/closer-drive` runs: one seat implements directly, you are the reviewer, and the
     CVO grades after the fact.
   - **FULL:** you are away. This is the default. `/canonical-drive` runs, with workers, the CVO slug and the CTO
     analysis.
   - **The lease is a timed marker like `/freeform`.** It expires back to FULL, so a forgotten fast mode can never run
     overnight.
   - **Same seat, same loop;** only the tick body changes.
   - **No work is lost at a switch:** each direction has a defined boundary act (section 7).

| # | Change | Fixes | Owner | Size |
|---|---|---|---|---|
| C1 | **The mode lease and `/drive-mode`**: arm, lapse, status, and a surface-overlap check at arm time | the switch; shared surfaces; duplicate work | `1.0.0_SA_CTO` (tool + skill); `0.0.0_AB_MSTR` (the optional presence hook) | one ~80-line tool, one ~50-line skill, one line in each drive skill |
| C2 | **`/closer-drive`**, the FAST tick body: no subagents, no task orders, one real look per item | the fast mode | `1.0.0_SA_CTO` | one ~70-line skill; reuses `/goal-set`, `/closer`'s STATUS template and `/frontend-dev` |
| C3 | **What FAST relaxes and what it never relaxes**, written once in the spine's Closer subsection | the fast mode | `1.0.0_SA_CTO` | one paragraph plus calls 2, 3 and 6 |
| C4 | **Checks are dry-run at the base before the cut**, and written as files, not inline one-liners | 31% mid-round defects | `2.0.0_SA_COO` (`/dispatch` Step 2; task-order protocol) | text |
| C5 | **Worker rules live in `worker.md`, not in every order** | about 2.5-3 KB (up to a quarter) of every AMGT order is the same worker rules | `1.0.0_SA_CTO` | text |
| C6 | **One real run of each outcome at close** -- a live page or the real entry point -- done by the COO at the merge (canonical), and one per candidate (closer). It replaces every seat-to-seat re-read of the same check and fixture-only judgment checks on UI outcomes. `[AMENDED 09-24: Andrew-approved, joint with report 3; section 12]` | the defect that passed | `2.0.0_SA_COO` (`/dispatch` Step 5); `/closer` | text; `/frontend-dev` exists |
| C7 | **Two worker tiers**, plus a spine line that names no model | cost and speed of small cells | `1.0.0_SA_CTO` (spine, agent type); `2.0.0_SA_COO` (the trial) | one agent file, one spine line |
| C8 | **Drain per chain in one commit; no blocking "instrument first" wave** | up to ~75-minute merge lag; an hour of wave 0 | `2.0.0_SA_COO` (`/dispatch`) | text |
| C9 | **A PRD header that fails its schema fails LOUD at commit** | a silent 7-minute, one-version loss | `1.0.0_SA_CTO` | one hook limb |

No new approval gate. The only new refusal is inside the command you asked for (C1): arming a second driver on files that
already have one.

---

## 1. What was measured, and how

- **Window:** 22:40 ET Wed 09-23 to 10:40 ET Thu 09-24 (02:40Z-14:40Z), the "last 12 hours" of the ask.
- **Canonical population (MEASURED):** every task order added under `org/missions/` in the window, on ALL refs. The
  first read of local `CLOUD` alone found one project; `origin/CLOUD` holds site Z's pushed work. The population:
  - **DSGN_IRPTV1** (laptop, `2.0.0_SA_COO~D`): round 1 of 4 orders, round 2 of 8.
  - **AMGT_RESAPP** (site Z, `2.0.0_SA_COO~Z`): round 37 of 10 orders, round 38 of 7.
  - **Total:** 29 orders, 4 issuances.
- **Closer population (MEASURED):** the IRPT Performance / Model-overlay / YCharts seats `2.0.0_SA_COO~P`, `~M` and
  `~Y`, run as 20-minute `/goal-set` loops on Andrew's 09-23 word. These are the closer flow as it actually runs today.
- **Instruments:**
  - `git log --all` in both repositories, de-duplicated by commit;
  - the task-order files at their issuance commits;
  - the laptop broker database `org/mcp/broker.db`, opened read-only;
  - the seats' own logs and surprise rows, printed at the bytes.

  Site Z's broker was not read, so message counts are laptop-only.
- **Scratch scripts** are in this session's scratchpad, not committed.

---

## 2. Canonical: where the time goes

### 2.1 The two specimens, end to end (MEASURED, commit times in ET)

**DSGN_IRPTV1**, the IRPT page redesign, from "make it its own project" to landed on DEV: about **9 h 20 min**.

| stretch | from -> to | took | what happened |
|---|---|---|---|
| setup (L1-L6) | 00:44 word recorded -> 02:44 round-1 cut | **2 h 00** | 5 PRD versions in 54 min: v0.1's header failed its schema **silently**, so nothing was routed; v0.2 was a header-only bump to make the notifier fire. Then 2 refusals, 3 signatures, and the decomposition committed 3 times to follow the PRD. |
| round 1, execution | 02:44 -> 05:49 last merge | **3 h 05** | 4 orders on 3 workers. **All three workers killed partway by the usage limit (~03:3x) and resumed after the reset** (the COO's own log). Two check amendments. |
| round 1, close | 05:49 -> 06:18 CTO analysis | 29 min | a typecheck red at the merge, fixed in 11 min; CVO slug 06:13; CTO analysis 06:18 |
| round 2, cut | 06:18 -> 06:43 | 25 min | decomposition v2 plus 8 orders |
| round 2, execution | 06:43 -> 09:52 last merge | **3 h 09** | 3 chains of up to 3 orders each run in sequence; two check amendments (21 and 24 minutes from failure to pass) |
| landing | ~10:0x | -- | **landed on DEV on Andrew's word ahead of the round's review**: 7 of 8 cells. The 8th (a "join" cell that waits for all the others) was never started. |

**AMGT_RESAPP** round 37, 10 orders:

| stretch | from -> to | took | what happened |
|---|---|---|---|
| setup | 01:15 PRD addendum -> 02:17 cut | 1 h 02 | an illegal PRD header key held the issuance until the CTO dropped it |
| wave 0 | 02:17 -> 03:16 | 59 min | ONE order, "the instrument": a checker the later orders use, with 0 product lines |
| wave 1 | 03:16 -> 05:46 | 2 h 30 | 7 orders; worker commits 04:08-04:36, merges 04:43-05:46 |
| wave 2 | 05:46 -> 08:04 | 2 h 18 | 2 orders that sweep the merged page |
| close and recut | 08:07 -> 08:46 | 39 min | CVO 08:18, CTO 08:23 (8 of 10 outcomes REALIZED), two corrections, round 38 cut 08:46 |

Round 37 delivered: **8 of 10 outcomes REALIZED.** The canonical flow works when the product exists and the cells are
right-sized. The question is only how long it takes.

### 2.2 The time sinks, ranked by measured minutes

| # | Sink | Measured | Mechanism |
|---|---|---|---|
| 1 | **Usage-limit stall** | Fabric commit rate fell from 15-31 per 20 min to **10, 5, 8** between 03:20 and 04:20 ET. `~P`: "usage pause 07:2xZ-08:52Z". `~D`: 3 workers killed. | Token volume across the whole fabric, not any one flow. See sinks 6 and 7. |
| 2 | **Chains run in sequence** | DSGN round 2 was 3 chains; chain A ran 3 orders one after another from 06:43 to 08:57 ET | Orders that touch the same file (`index.tsx`, the tabs) must queue. The file sharing is partly **caused by a second driver on the same page** (section 5.4). |
| 3 | **Defects in the checks, mid-round** | **9 of 29 orders (31%)**; 11-24 minutes each from failure to pass where timed (the 5 DSGN cases) | Section 3.3. Every one was caught by an assignee, a grader or the issuer's merge, never at the cut. |
| 4 | **Merge lag** | AMGT wave 1: worker commits 04:08-04:36, merges 04:43-05:46, up to ~75 min behind. Two commits per order (merge, then close). | Merges run one at a time, after the COO notices. INFERRED upper bound: the portal commit precedes the worker's final workspace commit. |
| 5 | **Setup of a new project** | 2 h 00 for DSGN_IRPTV1 (5 PRD versions) | Mostly answered by today's proportionate sign-off (cut 4). **Left over:** a header that fails its schema is silent (C9). |
| 6 | **Process text a seat carries** | To run the canonical loop the COO loads `/canonical-drive` 11.7 KB, `/canonical-flow` 51.7 KB, the spine 91.3 KB, `/dispatch` 30.8 KB, the task-order protocol 25.8 KB and `DRIVE.md` 26.0 KB = **237 KB**. The closer loop loads `/closer` 15.2 KB, `/goal-set` 2.5 KB and `/verify` 3.6 KB = **21 KB**. The same law files sit under both. | Each skill run re-reads its text. INFERRED: about 59k tokens against about 5k. |
| 7 | **Messages** | 714 in the window, about 3,000 characters each. `1.0.0_SA_CTO` sent 295 (41%): 109 rulings, 73 go-aheads/reviews, 60 asks. | Mostly answered by today's message discipline (cut 6, landed 10:1x ET, so most of the window predates it). |
| 8 | **The CTO inside a round** | DSGN_IRPTV1: 7 CTO rulings across 2 rounds (100332, 100467, 100499, 100522, 100553, 100625, 100631) | The spine says "the CTO waits". Cut 3 removes the check-amendment rulings. The **touch rulings on shared files** remain, and C1 retires them. |

### 2.3 What is NOT slow, and stays

- **The round hand-off.** From the CVO slug to the CTO analysis to the recut took about 30 minutes on both projects.
  Report 1 said to leave it alone, and the day confirms it.
- **The single issuance and the worker face.** DSGN_IRPTV1's round-2 decomposition and its 8-order issuance took 25
  minutes from the CTO's analysis.
- **The refusal clause.** It is how all 9 defects in section 3.3 surfaced. The fix is to catch those defects EARLIER
  (C4), not to remove the thing that catches them.

### 2.4 The one-font-weight question: fixed, partly

Report 1's specimen was a whole round and a 19.7 KB order to change `font-semibold` to `font-bold`. Under the v3.16 law
such a repair is **one batched cell per round, never a round of its own.**

- **Measured in the window:** DSGN_IRPTV1's batch cell `IV-e-2` ("style and instrument") changed **32 product lines**.
  It also wrote a **410-line fixture**, in an 11.1 KB order that needed one mid-round amendment.
- **So the font weight is no longer a round, but it is still a spawned worker, an 11 KB order and an amendment cycle.**
- **In FAST mode (section 6) it is an edit.**

---

## 3. Task orders: how light, and which model

### 3.1 The work each order produced (MEASURED; the 24 orders that committed code)

Product lines changed per order: added plus deleted, test, harness, fixture and script files excluded.

| product lines changed | orders | examples |
|---|---|---|
| 0 | 2 | `AMGT-rl-1` "the instrument", `AMGT-rm-1` "the instrument re-keyed": checkers only |
| 1-100 | 8 | `IV-e-1` 31, `IV-e-2` 32, `rl-10` 41, `IV-t-3` 59, `IV-e-4` 65, `rm-4` 83, `rl-9` 92, `rm-5` 100 |
| 101-350 | 9 | `IV-t-2` 156, `rl-4` 210, `IV-t-1` 233, `rl-5` 256, `IV-e-3` 280, `IV-e-8` 291, `IV-t-4` 301, `rl-7` 318, `rl-6` 319 |
| 351-807 | 5 | `rl-3` 447, `IV-e-5` 540, `rl-8` 589, `IV-e-6` 594, `rl-2` 807 |

- **Median:** about 220 lines. Most orders touch 1-3 product files; three touch 5, 6 and 10.
- **Kind of work:** all of it is single-page frontend work, a component built or restyled.
- **Test code versus product code:** 6,967 lines of test, harness and fixture against 5,844 lines of product (54% test).
- **Verdict on "the orders are very light":** **SUPPORTED for about 40% of the orders** (100 lines or fewer, or checkers
  only), **moderate for about 40%** (one new component), **substantial for about 20%.** No order in the window needed
  more than a single-page change.

### 3.2 What is inside an order (MEASURED over the 20 of 29 whose section headings parsed cleanly; 230 KB)

| part | share | what it is |
|---|---|---|
| **the build instruction** ("the cell", "what you build") | **about 25%** | the only part that says what to make |
| the checks | 23% (AMGT) to 43% (DSGN) | each check an inline invocation, often a multi-line Python one-liner inside XML |
| bounds and paths | about 14% | which files may be touched, and which files owned by other seats may not |
| header, references and worker rules | 11% (DSGN) to 24% (AMGT) | in the AMGT orders this is mostly who you are, the worktree rules, the toolchain, how to commit and "never push": **the same 2.5-3 KB in every order**. DSGN round 2 already shortened the same text to "as every order" pointers. |
| the record face | 7% (DSGN) to 15% (AMGT) | gate narrative the worker never sees |

- **Average order:** 11.8 KB.
- **Checks per order (MEASURED):** 3.45 (100 checks, 13 of them judgment checks). The three-mechanical-check diet is
  being followed.
- **The weight is in the wrapper, not the count.** The worker rules already have a home: `.claude/agents/worker.md`
  is loaded into every worker as its definition (C5).

### 3.3 Defects in the checks themselves (MEASURED: 9 of 29 orders)

| order | defect | how it surfaced |
|---|---|---|
| `IV-t-1`, `IV-t-2` | the ruled "one line in the shared file" bound was impossible for a new component that needs an import | the worker refused; amended `89e465b40c` |
| `IV-t-3` | the pathspec `fe-s-7` also matched `fe-s-71`..`fe-s-78`, one of which fails at the base | amended `f42548be58` |
| `IV-e-4` | the check failed on a failure that already existed at the base | recut as a difference control, `41e07da617` |
| `IV-e-2` | an unanchored expectation accepted `matched 2 of 5` as a PASS | the issuer caught it at the merge, `76d27f75b4`; amended `49dc5d9216` |
| `rm-1` | an `&&` chain could never print the census the check reads | read by the issuer, `d3f1d8620e` |
| `rm-6` | the same `&&` shape | amended before the run, `cf6b23c04a` |
| `rm-7` | `<paths>` named files the order's lane cannot write | amended, `b374f81234` |
| `rl-9` | the files the check needed were outside the round's cells | refused, `7d13903604` |

- **Seven of the nine are the check's own shape:** a bound, a pattern, a pipe, a path.
- **Every one is visible by running the check ONCE against the base before the cut.** A build check should FAIL at the
  base, and a bound check should PASS there.
- **That dry run is C4.** It costs seconds per check and is a step in `/dispatch`, not a gate.

### 3.4 Models (MEASURED state; INFERRED recommendation)

| who | model today (commit trailers in the window) | proposal |
|---|---|---|
| workers `0.9.0_WK_*` | **Sonnet 5, effort high**: 68 of 68 commits; `.claude/agents/worker.md` says `sonnet` / `high` since `6c118c12de` (09-16) | keep for build cells; add a `worker-light` type at **Sonnet 5, effort medium** for cells of 100 lines or fewer and for the batch repair cell; try it for ONE round against the next same-sized round (C7) |
| coordinating seats (CTO, COO, CVO, MSTR) | Fable 5.1 and Opus 5.5 (1M context) | keep. **7 of the 9 check defects were the issuer's, so do not downgrade the issuer; shrink what it writes** (C4, C5) |
| a FAST-mode implementer | the seat's own model | keep; it is the one context holding the product |

- **Why not Opus at low effort for workers:** no measured capability gap exists at Sonnet 5 on these cells. The defects
  were in the orders, not in the workers' code. Lowering Opus's effort buys less than moving small cells to a smaller
  setting.
- **One stale line:** spine L7 says the worker's model is "Opus at high effort". The file it cites says Sonnet. The
  spine should name no model and point at the agent file (C7), which is also the only place a merge can mis-set it.
- **The effort setting lives in the agent type's frontmatter.** The spawn call carries a model but no effort. So
  `worker-light` must be its own agent file, and the order face names which one (`<worker_class>`).

---

## 4. Canonical bureaucracy: keep, refine, cut (flow mechanics only)

### 4.1 Keep

- One issuance per round, and the worker face.
- The refusal clause.
- Worktree isolation and the `safe-merge.sh` row gate.
- The enrichment list.
- The round hand-off (25-40 min).
- Repo-wide hygiene once per merge.

### 4.2 Refine

| item | today | refine to | gain |
|---|---|---|---|
| checks as inline one-liners | 23-43% of the order; 31% break mid-round | **each mechanical check is a small test or script file the issuer writes and dry-runs at the base before the cut**; the face names the file and its expected line (C4) | the dominant defect class moves before the spawn |
| worker rules in every order | 2.5-3 KB per AMGT order | **move them into `worker.md`**; the face keeps cell-specific lines only (C5) | up to a quarter of an AMGT order, and of every worker's context |
| fixture-only judgment checks on UI outcomes | 12 of 12 DSGN orders carry one, graded on static markup or a stub page | **one real run of each outcome at close, by the COO at the merge**: the running page looked at (`/frontend-dev`), or the real entry point (C6) `[AMENDED 09-24]` | it catches what S6 caught |
| merge then close as two commits | 2 COO commits per order | **one commit per merged order, merged per chain end** (C8) | fewer record commits; less lag |
| "instrument first" as a blocking wave | 59 min of wave 0, 0 product lines | **checkers are the COO's merge tooling, or ride the one repair cell, never a wave the product waits on** (C8) | an hour per round that needs one |
| shared-file "touch" bounds | 2 CTO rulings, 11 touch exceptions; "one-line mount" checks | **one driver per surface** (C1) | the rulings stop being needed |
| a PRD header failing its schema | silent; the notifier skips it | **refused at commit with the schema error** (C9) | minutes and one version per occurrence |

### 4.3 Cut

- **The spine's model sentence** (C7).
- **The "join" cell that waits for every chain.** `IV-e-7` was never started, and the product landed without it. Fold
  a whole-page sweep into the merge step instead.
- **A second driver on a surface that already has one.** Measured in section 5.4; retired by C1.

### 4.4 Handed to report 3 (`4.0.0_SA_CRO~B`, RCN-0016), not re-measured here

- **Incident prose inside the flow skills.** `/canonical-flow` is 51.7 KB, and most of its probe section is incident
  history. `/canonical-drive` is 123 lines against its own "under 80 lines" rule. This is the same cut CLAUDE.md took
  today, one level down.
- **`/watcher` re-enters context every 30 minutes.** It is 20.7 KB; `~D` re-armed it 7 times in 5 hours.
- **Record-only commits are 81% of the window** (485 of 602), and 714 messages averaged about 3,000 characters.
- **A legacy test suite with 95 failures at baseline.** Nobody runs it, and CI does not. DSGN round 2 added 8 more to
  it unseen (`DSGN_IRPTV1-S7`).
- **The second-reader pattern.** The base CRO received 121 messages in the window. Some were second reads on another
  seat's result: call 2 of the 12:5xZ record names the CRO as the second read on `~P`'s result. The share was not
  measured. Today's corroboration cap addresses the rule; the traffic is report 3's to measure.

---

## 5. The closer flow today, and a FAST mode

### 5.1 What closer does well (MEASURED)

- **`2.0.0_SA_COO~P` implementing directly:** 100 workspace commits in 12 hours, 49 of them touching product code, plus
  22 commits in the portal repository. Several deploys landed inside the window, for example `irpt-directory-search`
  (12:21 AM ET) and `irpt-ycharts-generate` (6:24 AM ET), each reported by `~P` in its own message.
- **The canonical COO over the same hours:** 30 commits, none touching product. Its six workers made 13 portal commits.
- **Speed to code and speed to deploy are the closer flow's strengths, as report 1 measured.**

### 5.2 Where closer costs (MEASURED)

- **It does not follow its own FILES OVER MAIL rule.** `~P` sent 136 messages and received 190 in 12 hours; the
  canonical COO sent 20 and received 27.
- **It runs through the CTO for every step.** 95 of the CTO's 295 messages went to `~P`: a GO per portal candidate, an
  ACCEPT per deploy, a ruling per edge case.
- **Speed is capped by the CTO's turn-around.** The seat is fast; its bottleneck is one hub.
- **Today's message cuts help, but the structural fix is that while you are present, you are the reviewer**
  (section 6, calls 2 and 3).

### 5.3 FAST mode: what it relaxes, and what it never relaxes

| relaxed while a FAST lease is live | why it is safe to relax |
|---|---|
| no task orders, decomposition, issuance, proof-of-spec instance or surprise row for in-scope work; STATUS.md is the record | the work is one seat's own, reviewed by you on the screen |
| **no subagents**: the seat implements directly (your ask) | one context, no hand-off, no spawn rate-limit burst |
| **the seat lands product candidates on portal DEV itself** after pull-merge, with CI (VALGATE) running; no CTO GO, no MSTR push *(call 2)* | you are watching; DEV is not served to clients; PROD stays gated |
| **CVO grading is after the fact**: pins are graded as they land, a FAIL becomes the next item, nothing waits on it *(call 3)* | you are the live reviewer; the CVO remains the second axis |
| no CTO ruling inside the project's own surface; a cross-surface breaking change is one exchange with the owner, then the CTO | the lease names the surface (C1), so "inside" is defined |
| **the comp-tool search rail is stood down for the seat** (`/freeform` semantics) for the lease's life *(call 6)* | it is a search-speed rail, not a safety gate; freeform already exists for this |
| no second reads, no peer acknowledgements, no status messages | only three message kinds: interface published, blocker, review handoff |
| repo-wide hygiene at landing only; per item, the item's own test plus one real run | the real run is the check that caught S6 |

**Never relaxed:**
- `safe-commit.sh`;
- your own worktree;
- no rebase on a shared branch;
- the never-widen sign-off on served output;
- the deploy ledger (NEVER-2);
- `safe-apply` / Terraform only;
- vendor egress on your per-use word;
- PROD promotion;
- destructive-act confirmation;
- the cross-firm guard;
- LGIC builder output for any NEW address or name (or park the item);
- secrets.

FAST is a pace and a review model. It is not a license past a safety gate: the same boundary `/freeform` draws.

### 5.4 The two named risks: shared surfaces and duplicate work

**What happened in the window (MEASURED):**
- **The collision:** DSGN_IRPTV1 (canonical, `~D`'s workers) and IRPT Performance / Model overlay (closer, `~P` /
  `~M`) edited **the same 5 product files** of `portal/src/pages/InvestorReporting/`: `index.tsx`,
  `header/ClientSearch.tsx`, `tabs/holdings/HoldingsTab.tsx`, `tabs/reporting/ReportingTab.tsx` (with `~P`) and
  `tabs/holdings/DrillTree.tsx` (with `~M`).
- **What it cost:** two CTO rulings carving out eleven touch exceptions (100332: four in round 1; 100522: T1-T7 in round
  2); orders re-bounded to "the mount line plus one import"; a shared append-only channel file that conflicted at merge
  and had to be resolved by union.
- **A separate duplicate-work signal:** at 19:3xZ yesterday, `~Y`'s `docs(irpt)` commits were recorded as "possibly on
  another product", and it had to be asked which one.

**Guards (all inside C1 and C2; none is a new standing gate):**
1. **One driver per surface.** A lease names its surface (a directory or package). `/drive-mode arm` reads every other
   live lease's surface and every open canonical order's `<paths>`, prints any overlap, and refuses a second driver on
   files that already have one. You resolve it: pause the other (`/drive-mode <OTHER> hold`), or name a narrower
   surface. This is the only refusal the design adds, and it runs only when a lease is armed.
2. **Claim before build.** A FAST seat writes the item it is taking into STATUS.md (one line) before it starts.
   `/drive-mode status` prints every live lease's claims beside every open order's `<paths>`, so two seats never
   start the same item.
3. **One FAST seat per project** unless you name two seats with disjoint surfaces.
4. **Crash containment is unchanged.** The seat works in its own worktree and lands by merge, so a crash leaves a
   branch, never a half-edited shared tree. An unfinished item is committed on the branch as a work-in-progress pin
   at every switch (section 7.4).
5. **DEV landing** is pull-merge, then land. When two seats land in one window, the second merges forward, never by
   force.

---

## 6. `/closer-drive` (specification)

**What it is:** the FAST tick body. It runs when the project's lease reads FAST, on the seat that already holds the
project (the project's COO lane). It mirrors `/canonical-drive`'s shape: measure, act, log, heartbeat. The act is
"build the next thing yourself", not "cut and spawn".

| | `/canonical-drive` (FULL) | `/closer-drive` (FAST) |
|---|---|---|
| unit of work | a cell -> a task order -> a worker | an item from STATUS.md's next-list or the PRD's enrichment backlog |
| who builds | worker subagents (Sonnet 5 high) | the seat itself; no subagents |
| per-item checks | up to 3 mechanical + judgment, proof-of-spec instance, row gate | the item's own test, typecheck/lint on the touched package, **one real run looked at** |
| record | orders, instances, rows, slug, analysis | STATUS.md overwritten in place; commits |
| review | CVO slug per round; CTO analysis | **you, live**; CVO grades pins after the fact *(call 3)* |
| landing | MSTR on your word after CTO review | the seat, on portal DEV, CI running *(call 2)* |
| cadence | 10-20 min ticks | continuous while working; the loop wakes an idle seat every 10 min |
| stop | CLOSED on the grades | lease lapses (section 7.4), `/verify` SOUND on the goal, or your stand-down |

**Each tick:**
0. **Read the lease** (`python .tools/drive-mode.py read <CODE>`). FULL -> run the section 7.4 boundary act, then the
   `/canonical-drive` body.
1. **Read STATUS.md and the lease's surface.** Run `/drive-mode status` for overlapping claims.
2. **Pick ONE item.** A defect that breaks the live thread comes first. Otherwise take the top of the next-list, which
   is the enrichment backlog in order. Claim it in STATUS.md.
3. **Build it** in the seat's own worktree, across frontend and backend as the item needs.
4. **Check it.**
   - Run its own test; write one if that is cheap.
   - Run typecheck and lint on the touched package.
   - Do **one real run**: the page served with real or served data and **looked at** (`/frontend-dev`), or the real
     entry point for a backend item.

   That is the whole bar.
5. **Land it.**
   - Commit.
   - Land on DEV (call 2), or publish the pin.
   - If the item needs a deploy, deploy to QA/DEV under the normal rules: ledger entry, `safe-apply`.
6. **Overwrite STATUS.md** with pins, claims, next and limits. A finding off the item is one parked line with its owner
   and the condition that un-parks it, not a row and not a message.
7. **Messages:** only interface published, blocker or review handoff. No acknowledgements.
8. **Heartbeat**, then the next item.

**Reuse, not new machinery:**
- `/goal-set`'s loop (48 lines), which `~P`, `~M` and `~Y` already run;
- `/closer`'s STATUS template;
- `/frontend-dev` for the look;
- `/verify` as the stop.

`/closer-drive` is that loop with the lease read at the top and the item discipline above.

---

## 7. The switch

### 7.1 The lease

- **The command:** you type it at any terminal, or tell any seat.
  - `/drive-mode <CODE> fast [2h] [--seat <serial>] [--surface <dir>]` arms a lease.
  - `/drive-mode <CODE> full` ends it now.
  - `/drive-mode <CODE> hold` pauses both drivers.
  - `/drive-mode status` prints every live lease with its seat, surface, claims, expiry and overlaps.
- **Where it lives:** `org/mcp/drive_mode/<CODE>.json`, device-local, the way `/freeform`'s marker is.
  - It holds `{mode, seat, surface, armed_by, armed_at, expires_at}`.
  - Every arm, lapse and end appends one line to `org/mcp/drive-mode.log`, which is committed with the seat's record
    batch. That line is the durable record.
  - Projects are placed on one fabric, so device-local is the right scope.
- **Fail-closed to FULL.** A lease that is absent, expired or unreadable reads FULL. **A forgotten fast mode lapses to
  canonical by itself, so it can never run overnight.** That is your "canonical when I am sleeping" rule, made
  mechanical.
- **Optional presence extension** *(call 1)*. A one-line `UserPromptSubmit` hook stamps `org/mcp/presence/<device>.last`
  each time you type in any session on the device. A live lease then auto-extends while that stamp is under 30 minutes
  old, and lapses about 30 minutes after you stop.
  - This is a timestamp write, not a monitor or an alert.
  - Without the hook, the lease simply runs its stated length, and you re-arm.

### 7.2 One loop, two bodies

The project's seat runs ONE loop. Every tick reads the lease first and runs either the `/canonical-drive` body or the
`/closer-drive` body.
- **Nothing is re-armed at a switch**, no seat is handed over, and no context is lost: the COO that knows the project
  keeps it in both modes.
- **`/canonical-flow`** gains one class, `IN-FAST`, read from the lease the same way it reads `closer_contract`. It
  does not measure limbs; it reads STATUS.md.

### 7.3 FULL -> FAST (you sit down and arm a lease)

At its next tick (or at once, if you tell it directly), the seat:
1. **Cuts nothing new.**
2. **Lets each running worker finish the order in hand** (at most one per worker, since workers are its own subagents),
   and merges it as usual.
   - If you want it now: merge what is terminal and flip the rest `superseded`, which is the issuer's right, with the
     pointer "superseded by FAST lease, drive-mode.log line N".
   - Their cells go to STATUS.md's next-list. Nothing is lost; the cell text is the item.
3. **Writes STATUS.md** from the round's open cells plus the enrichment backlog, in order.
4. **Sends the CVO one message:** "FAST from <time>; pins graded after the fact". No partial-round slug is owed; the
   terminal orders' judgment checks are graded as pins.

### 7.4 FAST -> FULL (the lease lapses, or you say `full`)

The seat:
1. **Finishes or parks the item in hand.** What builds is committed. An unfinished edit is committed on the seat's
   branch as a work-in-progress pin, never left uncommitted in the shared tree.
2. **Overwrites STATUS.md.**
3. **At the next tick, cuts round N+1 directly from STATUS.md's next-list** under the verification diet, with no CTO
   round-N analysis for this one cut *(call 5)*. The CTO's analysis resumes at that round's L10.
4. **The CVO's next slug carries one section on the FAST interval:** what landed, and what was looked at.

### 7.5 How this relates to `closer_contract`

- **`closer_contract`** stays what it is. It is the multi-seat product rescue on your word: contract, writer table,
  mandates, per-seat CVOs. It suits a product with parts and no working journey.
- **The FAST lease** is the lighter, everyday switch: one seat, one project, your presence.
- **Both** make `/canonical-drive` stand aside.
- A closer contract whose seats you are watching can run FAST too. The lease names the seat and surface, and the
  contract's writer table already agrees with it.

---

## 8. Order of implementation

1. **C1 and C2 together.** Build `.tools/drive-mode.py` (`arm`, `read`, `status` with the overlap check, the log line)
   and the `/drive-mode` and `/closer-drive` skills. Put one line at the top of `/canonical-drive`: "read the lease;
   FAST -> `/closer-drive`". Add the `IN-FAST` class to `/canonical-flow`.
   - `/freeform`'s helper (`.tools/freeform.sh`) is the template for the marker, the expiry and the fail-closed read.
   - First exercise: DSGN_IRPTV1, whose seat `~D` already leads the IRPT frontend on your word.
2. **C3:** one "FAST mode" paragraph in the spine's Closer subsection, carrying the section 5.3 tables and your calls.
   One changelog line citing this report and your answers.
3. **C4, C5, C6 and C8** in `/dispatch`, the task-order protocol and `worker.md`. All are text; they take effect at the
   next issuance (an open round finishes under its cut orders).
4. **C7:** the `worker-light` agent file, the spine line, then a one-round trial. Grade it on minutes per order and
   check defects per order against the previous same-sized round.
5. **C9:** one limb in the PRD commit hook.

Cost: two small tools or skills, one agent file, one spine paragraph and edits to three existing documents. No new
seat. No standing gate beyond the arm-time overlap refusal.

## 9. Calls for Andrew

`[AMENDED 09-24]` **All approved at ~11:3x AM ET: "All of these recs are approved."** They were put to him as seven
cards: the six below, plus a GO for the CTO to build C1-C9. Each REC now binds at the scope it was written. Record:
`ANDREW_DIRECT_20260924_153xZ_REPORT2_ALL_SEVEN_RECS_APPROVED.md`.

1. **Lease length and presence.** Default 2 hours, renewable by saying so. Should a one-line prompt hook auto-extend it
   while you are typing? **REC: yes to both.** The hook write is a timestamp, not a monitor.
2. **Landing on DEV in FAST mode.** While a FAST lease is live, may the seat land PRODUCT candidates on portal DEV
   itself, with CI running, no CTO GO and no MSTR push? This touches the shared-branch push hold you set by name.
   **REC: yes, DEV only; PROD unchanged.** It is what you did by hand at ~10:0x today.
3. **CVO grading in FAST mode happens after the fact:** a FAIL becomes the next item, and nothing waits on it.
   **REC: yes.**
4. **A one-round trial of `worker-light`** (Sonnet 5, medium effort) on cells of 100 lines or fewer and on the batch
   repair cell. **REC: yes.** Not Opus at low effort.
5. **At a switch back to FULL,** the COO cuts the next round straight from the FAST seat's STATUS.md, with no CTO round-N
   analysis for that one cut. **REC: yes.**
6. **Arming a FAST lease also stands down the comp-tool search rail** (`/freeform`) for that seat, for the lease's life.
   **REC: yes.** Freeform needs your word; the lease is your word.

## 10. What this report does not claim

- **A small, recent sample.** 29 orders on 2 projects in 12 hours, both frontend-heavy. A backend or pipeline project
  might show different order sizes. The window was chosen by the ask, not by fit.
- **INFERRED classifications:**
  - product versus test (by path: `__tests__`, `__harness__`, fixtures and `scripts/` count as test);
  - "record-only" commits (no path under a product root);
  - message kinds (by subject keyword);
  - the section split of an order (by heading). Nine AMGT orders use headings the parser did not match; they are
    excluded from 3.2, not guessed.
- **Token figures are byte counts divided by about 4.** No model tokenizer was run.
- **Site Z's broker was not read.** Message counts are the laptop's only.
- **Merge lag is an upper bound.** The worker's portal commit precedes its final workspace commit.
- **The fast mode is a design, not a measurement.** Its gain is inferred from the canonical sinks it skips and from
  `~P`'s measured output. Its first run is its test (section 8, step 1).
- **No claim that the canonical rounds were wasted.** AMGT_RESAPP round 37 graded 8 of 10 outcomes REALIZED, and
  DSGN_IRPTV1 landed a working redesign in two rounds. The finding is time and wrapper weight, not output.

## 11. Evidence index

| claim | where | vintage |
|---|---|---|
| DSGN_IRPTV1 timeline | `git log -- org/missions/D13/DSGN/DSGN_IRPTV1` (56 commits) | HEAD `0905374fef` |
| usage limit killed the round-1 workers | `org/tier1_exec/2.0.0_SA_COO~D/logs/2026-09-24/dsgn_irptv1_round1_cut_and_drain_0507-1000Z.md` Summary | HEAD |
| round 1 fan-out and the four ruled touch points | issuance `e4552e6a05` message | -- |
| round 2 and the seven touches T1-T7 | issuance `ba8d5987c3` message | -- |
| the black tiles and the CUSIP; "no graded artifact ... could show either defect" | row `DSGN_IRPTV1-S6`, `surprise-channel/investigations/INVESTIGATION_v1.md` | `0905374fef` |
| DEV landing ahead of L8/L9; 95 -> 103 legacy failures | row `DSGN_IRPTV1-S7`, same file | `0905374fef` |
| "a proper canonical-flow ... from COO~D" | `ANDREW_DIRECT_20260924_052xZ_DSGN_IRPTV1_OWN_PROJECT_D13_COO_D.md` (this folder) | `5549279d96` |
| AMGT_RESAPP rounds 37-38 | `git log origin/CLOUD -- org/missions/D5/AMGT/AMGT_RESAPP`; issuances `53793b671f`, `7eaf2d7dae` | origin/CLOUD at read |
| AMGT back to canonical via addenda | `1ffb156ecd` message; closer loops record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` | -- |
| 2 of 26 rows carry `closer_contract` | `org/missions/*/*/*/project.json`; field history `git log -G closer_contract` (one commit, `ffa7a1533c`) | HEAD |
| worker model | `.claude/agents/worker.md` frontmatter; history `6c118c12de`, `0d57ceb2f9`, `65d7815288`, `4df363de8f`; 68 of 68 trailers | HEAD |
| spine says Opus | `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L7, "Its model is Opus at high effort" | HEAD |
| effort not passable per spawn | `.claude/skills/dispatch/SKILL.md` :231-236 | HEAD |
| messages | `org/mcp/broker.db` `messages`, `sent_at >= 2026-09-24T02:40`, read-only | 14:48Z |
| COO~P goal loop | `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md` | -- |
| today's six cuts | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_141xZ_YES_TO_ALL_SIX_PROCESS_CUTS.md`; CLAUDE.md `41f50d7424` | HEAD |
| the freeform template | `.claude/skills/freeform/SKILL.md`; `.tools/freeform.sh` | HEAD |
| no prompt hook today | `.claude/settings.json` hooks: PreToolUse, PostToolUse, SessionEnd only | HEAD |
| report 1 | `BRIEF_CANONICAL_FLOW_SPEED_CLOSER_FLOW_SKILLS_PARITY_20260923.md` (this folder) | `ea031c3987` |
| report 3 scope | `ANDREW_DIRECT_20260924_144xZ_PROCESS_ARCHITECTURE_BRIEF.md` (this folder) | `2b16316b41` |
| report 3 | `docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md` (RCN-0016) | `2d1bf5528a`, amended 09-24 |

---

## 12. The joint model with report 3 `[AMENDED 09-24: Andrew-approved ~11:4x AM ET]`

Record: `ANDREW_DIRECT_20260924_154xZ_REPORT3_REFINEMENTS_APPROVED_BOTH_REPORTS_TO_CTO.md` (this folder). Report 3
(`docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md`) carries the same text in its Cut 1,
Wave 2 and Wave 3.

**Two settings on every project, independent of each other:**

| setting | values | decides | source |
|---|---|---|---|
| **presence** | FAST lease (Andrew at the computer) / FULL (the fail-closed default) | pace and who reviews | this report, sections 5-7 |
| **risk and size** | `LOCAL` / `SERVED` / `WORLD`, plus the direct-act size floor | how much checking the work gets | report 3, Waves 2-3 |

**The two approved refinements:**
1. **One real run of each outcome at close.** A live page or the real entry point, done by the COO at the merge. It
   replaces every seat-to-seat re-read of the same check. The CTO's exercised read stays for `WORLD` work only.
2. **A portal change that lands on DEV only is `LOCAL`.** `SERVED` starts at a PROD promotion or a served data path.

**What each class gets, with both refinements in:**

| class | checks |
|---|---|
| `LOCAL` | the worker's proof plus the checker's match, plus the COO's one real run of the outcome at close |
| `SERVED` | adds the CVO's grade of judgment criteria, graded on the real run's artifact, never on static markup |
| `WORLD` | adds the CTO's exercised read and the change-management entry |

- **A FAST lease never lowers a class.** A deploy inside a FAST lease is still `WORLD` and keeps every guard in section
  5.3's "never relaxed" list.
- **Report 3's direct-act path and this report's FAST mode land as ONE rule:** presence decides pace and reviewer;
  risk and size decide checking. The CTO carries it in the spine's Closer subsection (C3) and in Wave 2's field.

---

## 13. C10 -- cut task orders by write set `[ADDED 09-24: Andrew-approved ~17:0xZ, "Yes, i like that item 1, send it"]`

Record: `ANDREW_DIRECT_20260924_170xZ_C10_CUT_TASK_ORDERS_BY_WRITE_SET.md` (this folder).

**The measurement behind it.** None of the window's four rounds reached the fan-out cap of 8:

| round | orders | most in parallel |
|---|---|---|
| DSGN_IRPTV1 r1 | 4 | 3 |
| DSGN_IRPTV1 r2 | 8 | 3 |
| AMGT_RESAPP r37 | 10 | 7 |
| AMGT_RESAPP r38 | 7 | 4 |

Orders were serialized for four reasons, each read from its issuance commit's `fanout:` line:
- **shared files, the largest cause:** DSGN r2's header chain `IV-e-3` -> `IV-e-4` -> `IV-e-8` queued on `index.tsx`,
  and `IV-t-3` -> `IV-t-4` on `HoldingsTab.tsx`;
- **a checker order every later order is graded by:** AMGT `rl-1`, `rm-1`;
- **a sweep order over the merged page:** `rl-9`, `rl-10`, `IV-e-7`;
- **a seat order waiting on another lane:** `rm-7`.

Real data dependencies between cells were rare.

**The rule (L5 and L6, `/dispatch` Steps 1-2, the task-order protocol):**
1. **Each cell owns a disjoint set of files.** Its `<paths>` names only files no other cell of the round writes.
2. **A one-line hookup in a shared file is not part of any cell.** Examples: a mount, an import, a route entry, a
   registry line in a page shell such as `index.tsx`.
   - The cell builds and exports its component, and its report names the hookup line it needs.
   - The COO adds every hookup line at the merge, in one commit, then runs C6's one real run of the outcome.
3. **Chains then carry only real dependencies:** a cell that consumes another cell's output. File contention is no
   longer a reason to chain.
4. **A batch cell that touches many cells' files runs last in its round, or folds into the merge.** Examples: the
   style, record and instrument repair cell. Checker and sweep orders follow C8: merge tooling, not a wave.
5. **The `fanout:` line and the cap of 8 are unchanged.** The "touch" rulings and "one-line mount" checks that guarded
   shared files are no longer needed.

**Expected effect (INFERRED, from the round's own file lists):** DSGN r2 runs about 6 orders at once instead of 3. The
style batch `IV-e-2` still waits, because it touches files of `IV-e-1`, `IV-e-3` and `IV-e-6`.

**Limit:** past that, the ceiling is usage. This morning 3 parallel workers were cut off by the usage limit. The
Sonnet-medium trial (call 7) and shorter orders (C5) are what buy room for more at once.

**Owner:** `1.0.0_SA_CTO` (spine L5/L6, `/dispatch`, task-order protocol). **Non-application:** a round whose cells
share no file.

---

## 14. C11 -- goal loops read the lease `[ADDED 09-24: Andrew-approved ~18:1xZ, "Yes agreed, do it"]`

Record: `ANDREW_DIRECT_20260924_181xZ_C11_GOAL_LOOPS_READ_THE_LEASE_P_M_Y.md` (this folder).

**The gap.** The IRPT return brief (`IRPT_CLOSER_TO_CANONICAL_RETURN_BRIEF_20260924.md`, gap G2) found that `/goal-set`
loops never read a lease. `2.0.0_SA_COO~P`, `~M` and `~Y` work IRPT_BCKEND in closer mode on 20-minute goal loops. So
when Andrew leaves, `~D` drops to FULL but they keep blast-mode freedoms.

**The rule:**
1. **One FAST lease per project may name several seats**, each with its own surface, pairwise disjoint.
   `.tools/drive-mode.py` gains that form; the arm-time overlap refusal still applies between seats.
2. **Every `/goal-set` loop that works a project reads that project's lease at the start of each tick:**
   - **FAST:** the FAST relaxations of section 5.3.
   - **FULL:** keep working under the project's normal checks. For a closer project, that means the CVO grades each
     pinned change before it counts and the CTO lands DEV candidates.
   - **HOLD:** pause.
3. **IRPT_BCKEND** gets one such lease for `~P`, `~M` and `~Y`, extended by presence like `~D`'s, so all four seats
   change pace together.

**Owner:** `1.0.0_SA_CTO` (`drive-mode.py`, `/drive-mode`, `/goal-set`, the IRPT_BCKEND lease; surfaces from each
seat's STATUS write claims). **Non-application:** a goal loop that works no registered project.
