# Process architecture: where verification and process management slow the fabric down

**Author:** 4.0.0_SA_CRO~B (Chief Research Officer, lane B)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Recon ID:** RCN-0016 -- registered in RECON_REGISTER.md
**Point of contact since 2026-09-24 ~15:5xZ:** `4.0.0_SA_CRO~A`, on Andrew's word ("CRO~B is offline, i took them
off, you are point of contact for both report2 and 3 and RCN 016"). Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_155xZ_CRO_A_POINT_OF_CONTACT_REPORTS_2_AND_3_CRO_B_OFFLINE.md`.
**Commissioned:** Andrew-direct 2026-09-24 ~14:46Z, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_144xZ_PROCESS_ARCHITECTURE_BRIEF.md` @2b16316b41
**Measured:** 2026-09-24 14:50-15:40Z on branch CLOUD (workspace) and DEV (portal). Re-runnable scripts:
`org/tier1_exec/4.0.0_SA_CRO/scripts/process_census/`. This is a PROPOSAL: the fixes belong to their owners, and
the law-locked items need Andrew's order.
**Amended 2026-09-24 ~15:4xZ by `4.0.0_SA_CRO~A` on Andrew's word** ("Yes agreed to both, recs approved. Make the edits
as needed to both your report and report3"). Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_154xZ_REPORT3_REFINEMENTS_APPROVED_BOTH_REPORTS_TO_CTO.md`.
- **Two refinements are approved:** one real run of each outcome at close, and a portal change landing on DEV only
  counts as `LOCAL`.
- **Where they land:** Cut 1, Wave 2, Wave 3 and section 4's overlap note. Each amended passage is marked
  `[AMENDED 09-24]`; the rest of the text is `4.0.0_SA_CRO~B`'s as committed at `2d1bf5528a`.
- **Status:** sent to `1.0.0_SA_CTO` for immediate implementation, on his word.

---

## Bottom line

The fabric spends most of its output checking and recording itself. In the last 7.6 days the workspace took **4,312
commits; 381 (8.8%) touched product code and 3,725 (86.4%) touched nothing but governance records.** Counting the
portal repo it is about 12.5%. In June the same share was **16-25%**. The drop tracks the arrival of the ten-limb
workflow and its workers (week 36 onward), not the size of CLAUDE.md.

The cause is structural, not behavioural. The workflow has one fact measured by three or four seats in sequence. Any
wording edit to a PRD reopens a two-seat sign-off. Any observation becomes a row that must be adjudicated before the
project can close. And the CTO routes nearly every ruling. **Rule 22 cannot fix this, because it asks agents to check
less inside a process whose gates require them to check more.** The fix has to live in fields and gates that decide how
much checking a piece of work gets, so no agent has to read a rule and reason its way to restraint.

On the specific questions:
- **The "3%" is real in spirit, partly an artifact in detail.** On the IRPT outcome-check page, 16 of 471 trunk commits
  were fixes and features (3.4%). But the same page shows 17,110 backend lines on one seat's local branches and 57
  portal commits that the trunk ratio cannot see. The estate-wide ratio (8.8% / ~12.5%) is the fair number. It has
  halved since June.
- **RAVC is mostly unfairly lumped in.** Its three evidence rules are good and now live inside proof-of-spec. What is
  wrong is the stale document: two months old, still "non-negotiable ... all inter-agent work", contradicting the spine.
  It also carries a 5-minute approval wait that has never been used once. Shrink it; do not blame it for the volume.

---

## 1. What is happening (measured)

### 1.1 The output mix

| Window (ISO week) | Commits/day | Touch product code | Process-named subjects | Governance lines : product lines |
|---|---|---|---|---|
| W23-W26 (June) | 91-177 | 11-26% | 30-43% | 0.0-3.0 : 1 |
| W30-W34 (late Jul-Aug) | 174-264 | 6-11% | 22-36% | 5-26 : 1 |
| W35-W38 (Aug 24 - Sep 20) | 298-721 | 5.9-8.2% | 38-49% | 8-51 : 1 |
| W39 (Sep 21-24, partial) | 323 | 11.4% | 47% | 5.7 : 1 |

"Process-named" = subject opens with log, row, record, review, ruling, amend, adjudicate, surprise, ledger, L4-R, sign,
analysis, packet, l9, disposition, correction, close, drive or register. Governance lines include generated evidence
dumps, so the commit share is the headline and the line ratio is supporting.

In the last 7.6 days, by seat role: COO lanes made 1,344 commits (9.2% touching product), workers 1,023 (20.8%), CTO
988 (1.0%), CVO 480 (0.2%), CRO 233 (4.3%). Workers are the only role that mostly builds, and they are 24% of commits.

### 1.2 Per project (commits since June; product lines = added + deleted in code files)

| Project | Commits | Touch product | Product lines | Task-order files / text |
|---|---|---|---|---|
| AMGT_RESAPP | 1,517 | 167 | 77,532 | 191 / 3.7 MB |
| IRPT_BCKEND | 1,014 | 90 | 45,976 | 102 / 1.9 MB |
| LGIC_ENFORCE | 562 | 21 | 3,555 | 74 / 801 KB |
| NFRA_COMPEFFICACY | 260 | 2 | 127 | 28 / 346 KB |
| LGIC_NAMING (closed) | 208 | 3 | 200 | 34 / 295 KB |
| LGIC_CANON | 236 | 4 | 712 | 30 / 284 KB |

A project that changes 200 lines of code ran 34 task orders, 208 commits and 20+ sign-off commits.

### 1.3 Per unit of work

- 1,053 task-order cells since Sep 1: median 3 commits and 2 authors each; **835 (79%) never had a commit that touched
  product code** (upper bound: portal cells commit in the portal repo).
- **Specimen A, EG-s-21 (ETFS_GUARDRAIL):** 16 commits over 17 hours, zero product lines. The criterion was ruled
  "unsatisfiable as cut", re-cut five times, and the project closed with the run UNSPENT.
- **Specimen B, IB-rt-2 (IRPT_BCKEND):** 36 commits over 18 hours, 7 of them code (3,349 lines). The issuer amended
  it 11 times, several because the process layer itself blocked the work. In the issuer's own subjects: "my C1 grant
  was PROSE-ONLY and the lane gate reads the BLOCK"; "my E3 guard was written BACKWARDS and blocked a deploy it never
  meant to stop".
- **Specimen C, the DSGN_IRPTV1 PRD today:** five versions in 57 minutes. v0.1 was refused by the header schema over a
  status value; v0.2 was a header-only bump made to trigger the sign-off notifier; v0.3 was refused by both halves;
  v0.4 was signed; v0.5 was re-signed because backlog items were re-lettered. Estate-wide: **537 L4-R sign-off commits
  since Sep 1.**
- **Specimen D, the adjudication tail:** LGIC_ENFORCE has 177 commits (31%) after its last product commit. They are
  mostly `row`, `adjudicate`, `disposition`, `rule`, `l9` and `l10`, including "my armed-row tally was wrong by 20 rows and I
  published it for eight ticks". NFRA_CLDGRPH ran 310 hours of activity after its last code change.
- **Specimen E, this seat's own startup:** about 35 tool calls before the first research act. One heartbeat also
  replayed 82 month-old unacked messages (263,254 characters) into a fresh context.

### 1.4 Messaging

- 4,167 broker messages since Sep 14 (about 380 a day). **Median 391 words; 79-98% of each day's messages exceed the
  new 150-word cap.** Average body size grew from ~1 KB (April) to 3-3.7 KB (September).
- The CTO sent 1,771 of them (about 160 a day), 870 to the COO. By subject: RULING/RULED 199, SIGN 92, GO 86, AMEND
  56, CORRECTION 46. Many are micro-rulings, for example "Re tick 58: RULED (a) -- fold the partner-allowlist removal
  into FE-s-49 amendment 1".
- Pure acknowledgement subjects (the RAVC "A" step) fell from 15-20% of traffic in April-May to 1-3% in September.

### 1.5 The rule corpus

- CLAUDE.md has 249 commits and a sawtooth: 33 KB (Jul 15), cut to 24.6 KB (Sep 1), back to **46.5 KB (Sep 15)**,
  cut to 30.7 KB today. org/XXX.md: 97 KB (Sep 1), 51 KB, 70 KB (Sep 22), 19.8 KB today. **Cutting has never stopped
  the growth; the text comes back within two weeks.**
- The text did not disappear; it moved. The spine is 91 KB, 110 skills total 1.37 MB (canonical-flow 52 KB, dispatch 31 KB), doctrine 226 KB, org/ref 262 KB.
  Memory holds **1,475 files, 5.3 MB, 929 of them "feedback" lessons**. Its index, MEMORY.md (24.5 KB, over its own
  24.4 KB ceiling), loads into every seat at startup and reads as an incident index ("MY STANDING FAILURE MODE ... 10
  FACES"). That is CLAUDE.md's pre-cut disease, uncut.
- 21-37% of commit subjects each week since W29 are corrections, amendments, retractions or "my own" confessions. Each
  confession tends to become a memory entry or a rule.
- The estate has 62 gate/check/lint/guard/validate tools, 45 git hooks and 12 tool hooks; 36 gate or hook files were
  added since Andrew's Aug 4 "no inferred gates" record. 16 of the 36 (44%) name Andrew in the adding commit's
  subject; the other 20 cite no Andrew word there. Some belong to
  projects he directed, such as LGIC_ENFORCE's naming gates, so 20 is an upper bound on gates a seat added on its own.
- The comp-tool search rail: **983 denials since Sep 17 (~130 a day)**. Agents then used the audited override 331 times,
  and the rail's own router logged "no tool fits" 1,455 times. A denial aborts the whole shell call.

### 1.6 Carried from report 2 (RCN-0017, 4.0.0_SA_CRO~A), cited not re-measured

Report 2 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`
@6273825a91, section 4.4) measured the flow mechanics and handed five items here:

- **Incident prose inside the flow skills.** `/canonical-flow` is 51.7 KB, and most of its probe section is incident
  history. `/canonical-drive` is 123 lines against its own "under 80 lines" rule. It is the same cut CLAUDE.md took
  today, one level down.
- **`/watcher` re-enters context every 30 minutes.** It is 20.7 KB, and one seat re-armed it 7 times in 5 hours. The
  Monitor's 30-minute cap turns a one-line re-arm into a full skill load, about 40 KB per seat per hour.
- **Record-only commits were 81% of report 2's window** (485 of 602), and its 714 messages averaged about 3,000
  characters.
- **A legacy test suite with 95 failures at baseline** that nobody runs, CI included. One round added 8 more unseen
  (`DSGN_IRPTV1-S7`). Checking that looks thorough is not the same as checking that catches things.
- **The second-reader pattern, measured here:**
  - 303 of 4,170 broker messages since Sep 14 (7.3%) carry explicit second-read or re-verify language. They mostly
    reach the CTO (93) and COO (93), then the CVO (48), MSTR (36) and CRO (29).
  - 181 commits in the 7.6-day window (4.2%) say the same in their subject, and 1 of them touched product code.
  - This is a floor: the spine's built-in re-reads (L9, the L10 exercised read) do not announce themselves in those
    words.

Report 2 also found that 9 of 29 orders (31%) carried a defect in their own checks. Every one could have been caught
by running the check once against the base before the cut (its C4). Most verification cost is spent downstream on
defects the verification layer created upstream.

### 1.7 What does work (measured, so the cuts are aimed)

- **The lane gate is cheap and right:** 3,862 commits graded since Sep 17; 3,693 passed, 62 refused, 61 overridden.
- **Workers with a literal proof-of-spec are fast when the cell is well cut:** AMGT-rk-115 went from issue to
  complete in 20 minutes.
- **The surprise channel finds real things:** of 1,447 dispositions, 55% GRADUATED (mechanism attributed, remedy holder
  named) and 43% DISMISSED_WITH_REASON. The problem is the cost per row and the fact that rows block the close; the idea
  itself is sound.
- **Quiet drive ticks mostly commit nothing, as Andrew ruled.** Only ~8% of the 597 log/drive commits report a tick
  where nothing moved. The volume is narration of every step, not empty ticks.

---

## 2. When and where the debt occurs

**When.** It came in two steps. Late July (W29-W31): self-correction subjects rose to ~30% and the governance:product
line ratio to 25:1. Then Aug 24 onward (W35-W38): spine v3, workers and the L4-R gate arrived, volume reached 4-5K
commits a week, and product share sat at 6-8%.

**Where, by limb:**

| Where | Mechanism | Evidence |
|---|---|---|
| Before code (L1-L6) | PRD sign-off bound to the hash of every non-endpoint section; task orders averaging ~19 KB; decomposition and battery authored per cell | 537 L4-R commits since Sep 1; DSGN_IRPTV1 five versions in 57 min; ETFS_GUARDRAIL 56 h from first commit to first code; LGIC_NAMING 20 h |
| During code (L7) | Path grants the gate cannot read, guards that block the work, mid-round amendments, rail denials | IB-rt-2 amended 11 times; 983 rail denials in 7 days |
| After code (L8-L10) | Every row dispositioned before the slug; the CTO re-reads exercised artifacts; completion report and grades per round | LGIC_ENFORCE 31% of commits after its last code; NFRA_CLDGRPH 310 h tail |
| Around everything | CTO as the router of every ruling; long messages; one commit per log; incident -> memory -> rule | 870 CTO->COO messages in 11 days; median 391 words; 597 log/drive commits/week (40,738 lines) |

**The multiplier.** A mechanical criterion (a literal invocation and an expected output) is run by the worker, matched
by the checker, re-read by the CVO at L9, and re-read against the exercised artifact by the CTO at L10. Then the
requester "validates" under RAVC, and a spot-check or /verify may run again. That is the "checked five times" Andrew
sees, and it is written into the spine, not improvised by agents.

---

## 3. Qualification: keep, refine, cut

### Keep (it earns its cost)

1. Worker subagents with a literal proof-of-spec. "Done" is machine-checkable without a second seat.
2. The lane / owned-paths gate, the never-rebase gate, the commit-message rule and the law lock. They are cheap, rarely
   wrong and prevent real damage.
3. `/outcome-check`. It separates outcomes from process, and it is the instrument that made this visible.
4. The surprise-row idea: record and keep working instead of halting. It has 55% graduation yield.
5. RAVC's core: completion carries evidence, rework names a specific gap, and the requester looks before closing.

### RAVC verdict: keep the core, delete the rest

RAVC is not causing the volume: acknowledgement traffic is 1-3%. The harm is that its document is stale and
contradicts the spine:

- `org/ref/RAVC_PROTOCOL.md:3` says "Non-negotiable ... all inter-agent work", and `org/XXX.md:22-24` points every
  seat at it. The spine forbids those messages on project work: tracks share files, workers cannot be messaged, and
  the CVO has one send.
- The acceptance-flex rule (`RAVC_PROTOCOL.md:79-80`, "Wait 5 minutes for redline") is an approval wait. **It appears
  in zero broker messages, ever.**
- It was last edited 2026-07-24, before the spine existed.

Rewrite it to about 15 lines: the three evidence rules, scoped to ad-hoc requests outside a project.

### Refine (right intent, wrong mechanism)

1. **L4-R sign-off.** It binds the brief half to every non-endpoint section (`.tools/prd_signoff_lib.py:13`), and LIMB 6
   then refuses new task orders (`.tools/to-pipeline-gate.py:2378ff`). Today's proportionate sign-off law
   (CLAUDE.md:39-44) says a wording change withholds nothing; **the gate still withholds.** The law is DESIRED but not
   APPLIED. Fix: bind to the ENDPOINT hash only, with one reviewer.
2. **Surprise channel.** A row costs a worker one append and costs the CVO an adjudication, and the L10 precondition
   (spine :482) makes every row block the close. Fix: only BLOCKING and ARMED rows gate the close; OBSERVATION rows
   auto-disposition as NOTED at round close.
3. **One workflow for every size of work.** LGIC_NAMING needed 34 orders for 200 lines. Fix: add a size floor. The
   gate already recognises `<direct_act>true</direct_act>`; make it the default path for small, local work.
4. **Logs as commits.** Logging is fine; one trunk commit per narrated step is not. Fix: write ticks to a gitignored
   runtime file and commit one log per closed decision or per hour (Rule 31 already says hourly; make it mechanical).
5. **Message length.** Rule 31 is right but binds by reading. Fix: enforce it at the broker send path, the way
   `cvo_send_guard.py` already refuses.
6. **The search rail.** The intent is right, but the denial is often wrong: 1,455 "no fit" results and 331 overrides
   against 983 denials. Fix: when comp-which returns no fit, allow the search and log it.
7. **Rule 22.** It points the right way but has no carrier, so it can only work if agents read it and reason well
   (Andrew's own objection). Fix: Wave 2 below turns its table into a field the gates read.

### Cut (ruthlessly)

1. **Serial re-measurement of mechanical criteria.** `[AMENDED 09-24, Andrew-approved]` For a criterion with a literal
   invocation and expectation, the checker's match is the verdict.
   - **Cut:** the CVO's L9 re-read, and every other seat-to-seat re-read of the same check.
   - **Keep ONE real run of each outcome at close:** a live page or the real entry point, done by the COO at the merge.
     It replaces the CTO's L10 exercised read for `LOCAL` and `SERVED` work. The CTO's exercised read stays only for
     `WORLD` work (Wave 2).
   - **Why the one run stays:** on 09-24 every mechanical check on DSGN_IRPTV1's new Holdings map passed on static
     markup, and the first real render showed solid black tiles and a raw CUSIP printed as a security name. Row
     `DSGN_IRPTV1-S6` records it; report 2 (RCN-0017) section 0 item 4 measures it. Of all the checks, only the look
     at the real thing found it.
2. **The incident -> memory -> rule pipeline.** It feeds 929 feedback memories and a 24.5 KB auto-loaded index of
   incidents. Keep only stable preferences in the index (under 6 KB) and move lessons out of auto-load. Stop writing
   incident narrative into commit subjects.
3. **The CTO as universal router.** Today's word already lets the issuer amend its own criteria; extend it so the
   issuer rules on everything inside its own decomposition. The CTO rules only on ENDPOINT changes and on work that
   moves served output or the world.
4. **Law that documents a gate bug.** CLAUDE.md:58 (LD-0521) warns seats that the refuser counts open orders per
   project, not per round. Fix the refuser and delete the sentence.
5. **The RAVC acceptance-flex wait.** Delete it.
6. **Checks nobody runs.** The 95-failure legacy suite either joins CI or is deleted. A suite that stays red adds
   the look of coverage and catches nothing (report 2, `DSGN_IRPTV1-S7`).

### The contradictions (holes) found

| # | One rule says | Another says | Where |
|---|---|---|---|
| 1 | "BANNED: ... Task agent (unreliable)" | L7 execution is worker subagents | org/XXX.md:11 vs CLAUDE.md:49 |
| 2 | Broadcast every Andrew-direct to COO + CTO + MSTR | CTO copied on decisions only; FYIs go to the record | org/XXX.md:18 vs CLAUDE.md:315 |
| 3 | RAVC: acknowledge, report and accept by message, "non-negotiable" | Tracks share files, never messages; workers cannot be messaged | RAVC_PROTOCOL.md:3 vs CLAUDE.md:66-68 |
| 4 | RAVC: "Wait 5 minutes for redline" | NO FWD IS A WAIT; do not manufacture friction | RAVC_PROTOCOL.md:80 vs CLAUDE.md:30, :120 |
| 5 | Corroboration cap: one fact, one measurement | "NEVER trust a producer's self-report"; the CTO re-reads the exercised artifact at close | CLAUDE.md:99 vs :206; spine :513 |
| 6 | A PRD wording change withholds no delivery | LIMB 6 refuses on any brief-half hash change | CLAUDE.md:39-44 vs prd_signoff_lib.py:13 |
| 7 | Mid-round the spec and decomposition are FROZEN | The issuer amends criteria mid-round (IB-rt-2: 11 times) | CLAUDE.md:68 vs :46 |
| 8 | Found something odd: append one row and keep working | Every row must be dispositioned before the round can close | CLAUDE.md:112 vs spine :482 |
| 9 | L4-R exists because Andrew asked for "entirely automatic and gated" | It became 537 human sign-off commits in 24 days | to-pipeline-gate.py:2378-2388 |
| 10 | The law is cut to rules only | The auto-loaded memory index is 24.5 KB of incident narrative | MEMORY.md |

---

## 4. How to implement

**Principle: every fix is a field, a gate change or a deletion. Nothing that binds by reading.**

**One proposal per fact.** Report 2 (RCN-0017) owns the flow-speed mechanics, and this brief defers to it on them:

- FAST mode and `/closer-drive`.
- C4, dry-running each check at the base before the cut.
- C5, moving worker rules into `worker.md`.
- C1, one driver per surface.
- C8, one commit per merged order.

Two items overlap. Wave 3's direct-act path below is the canonical-side counterpart of report 2's FAST mode; they
should land as one rule with one size floor. The CTO decides which document carries it.
`[AMENDED 09-24]` Andrew approved report 2's recs (~15:3xZ) and the joint model (~15:4xZ). The single rule:
- presence (report 2's FAST lease or FULL) decides pace and reviewer;
- `<risk>` plus the size floor decides checking;
- every outcome gets one real run at close by the COO.

Report 2's section 12 states it in full. The CTO carries it in the spine's Closer subsection and in Wave 2's field.

**Step 0 (Andrew).** Choose which items to authorize. Items 1.4 and 1.5 touch law-locked or law-cited files and need
his express order.

**Wave 1: fix the gates that contradict his rulings (days).**

| # | Change | Owner | Done when |
|---|---|---|---|
| 1.1 | `prd_signoff_lib.py`: bind to the ENDPOINT hash only; brief half auto-admitted when the CRO wrote the brief | 1.0.0_SA_CTO | A wording-only PRD edit leaves `prd-signoff.py status` ADMITTED |
| 1.2 | L10 precondition and row gate: only BLOCKING/ARMED rows need a disposition before the slug | 3.0.0_SA_CVO (lane TREE_CVO) + CTO (spine) | A round with open OBSERVATION rows issues its slug |
| 1.3 | Refuser counts open orders per round (LD-0521); delete CLAUDE.md:58's warning | 1.0.0_SA_CTO | A round N+1 issuance no longer deadlocks round N |
| 1.4 | org/XXX.md: remove "BANNED Task agent"; replace the three-seat broadcast with record-only (plus one line to the CTO when a directive changes another seat's work); scope the RAVC pointer | CTO, on Andrew's order | The law-lock audit shows the order |
| 1.5 | RAVC_PROTOCOL.md cut to ~15 lines: three evidence rules, ad-hoc scope; delete acceptance flex and the session-log count | CTO | File under 2 KB |
| 1.6 | Rail: allow the Bash search when comp-which returns no fit; keep the HUD nudge | 0.8.0_AE_CloudComp | NOFIT events stop producing DENY |
| 1.7 | Incident prose out of `/watcher`, `/canonical-flow` and `/canonical-drive` into `docs/references/`; the 30-minute re-arm becomes one script call, not a skill load | 0.0.0_AB_MSTR (watcher), CTO (flow skills) | watcher under 5 KB; canonical-drive under its own 80 lines |

**Wave 2: the risk class, the systematic replacement for Rule 22 (one week).**

- Add `<risk>` to every task order `[AMENDED 09-24, Andrew-approved]`. The to-pipeline gate refuses an order without
  it and infers a floor from `<paths>` (infra paths or a deploy verb means WORLD). The three values:
  - `LOCAL`: code, tests or records, including **a portal change that lands on DEV only**; nothing served moves.
  - `SERVED`: changes what a person or pipeline reads in production, meaning **a PROD promotion or a served data path**.
  - `WORLD`: deploy, delete, grant, key, or a claim to Andrew.
- The class mechanically decides which limbs engage:
  - **LOCAL:** the worker's proof plus the checker's match, plus **the COO's one real run of the outcome at close**
    (Cut 1). No CVO grade, no CTO exercised read, rows OBSERVATION-only.
  - **SERVED:** adds the CVO's grade of judgment criteria, **graded on the real run's artifact, never on static
    markup.**
  - **WORLD:** adds the CTO's exercised read and the change-management entry.
  - `COMPLETION_GRADES` skips LOCAL cells; the COO's real-run record is their close.
- Rule 22's table becomes the data behind `<risk>`, and the rule shrinks to a pointer. Agents no longer have to read
  it or reason about it; the gate assigns the checking.

**Wave 3: size floor and router (one to two weeks).**

- **Direct-act path:** one cell, a declared small size (for example under ~300 lines) and risk LOCAL means no L2,
  L4-R or L8-L10. The COO writes one order with `<direct_act>true</direct_act>`, a worker executes, and the order drains.
  `[AMENDED 09-24]` Two consequences of the approved refinements:
  - **A portal change landing on DEV only is LOCAL,** so it qualifies when it is under the floor. Report 2's 12-hour
    sample had 19 of 24 orders under ~300 lines.
  - **The direct-act path and report 2's FAST mode (approved 09-24) are ONE rule.** Presence (a FAST lease, or FULL)
    decides pace and reviewer; risk and size decide checking. A FAST lease never lowers a class.
- **Rulings:** the issuer rules inside its own decomposition (amend, re-point, grant paths). The CTO rules only on
  ENDPOINT changes and SERVED/WORLD work.
- **Broker:**
  - Refuse sends over 150 words unless the body is a file path plus one line (the CVO send guard is the pattern).
  - Piggyback replay carries only mail under 7 days old; anything older becomes one summary line.
- **Logs:** `/canonical-drive` and `/self-drive` write ticks to a gitignored runtime file and commit once per closed
  decision or per hour.

**Wave 4: memory (Andrew's call, since a size check is a gate).** `[AMENDED 09-24: Andrew-approved ~17:0xZ, replacing
the 6 KB cap; record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_170xZ_MEMORY_PREFERENCES_ONLY_AND_THREE_HELD_ITEMS_YES.md]`

His direction: *"the entire point of canonical flow and our ops is that we shouldnt 'need' memory."*

- **MEMORY.md holds Andrew's stable working preferences only,** about 2 KB.
- **Seats stop writing lessons to memory.** A lesson that matters becomes a gate, field or skill fix by its owner; an
  incident stays in git history. The stop is mechanical, not a rule to read: the harness's auto-memory instructions
  would outvote a text rule.
- **The memory files (1,481 at ~16:5xZ) are ARCHIVED, never deleted,** out of the auto-loaded directory and
  recoverable.
- **The memory directory is per device and outside the repo.** This binds the laptop; site Z's is its own.

---

## 5. Staying clean

1. **One number, every week.** The efficiency ratio (commits touching product code, workspace plus portal, divided by
   all commits) and the governance:product line ratio, estate-wide and per project.
   - Script: `org/tier1_exec/4.0.0_SA_CRO/scripts/process_census/census.py`.
   - Put it in the `/daily-sprint` packet as a report line, not an alert, so it respects the monitor moratorium.
   - Baseline: W38 5.9%, W39 11.4% (workspace). Target: back to the June band (15-20% or better) within four weeks of
     Waves 1 and 2.
2. **Byte budgets on every auto-loaded carrier, enforced by the law lock.**
   - CLAUDE.md 30 KB or less; org/XXX.md 20 KB or less; any SKILL.md 25 KB or less.
   - `[AMENDED 09-24, Andrew-approved]` MEMORY.md becomes preferences-only (Wave 4), in place of a 6 KB budget.
   - A file already over its budget may only shrink. The skill budget covers the flow and process skills, not
     general-purpose skills. The law lock is a git hook, so it cannot see MEMORY.md, which lives outside the repo.
   - One in, one out. The sawtooth shows that cuts without a budget regrow in two weeks.
3. **A rule lands only with a carrier.** A new rule names the gate or field that enforces it, its cost and its
   non-application. Otherwise it goes to `docs/doctrine/` and binds nothing.
4. **Gates earn their keep.** Every gate already audits its refusals and overrides.
   - Read them monthly. A gate overridden more than ~30% of the time, or with no true refusal in 30 days, is
     downgraded to advisory or deleted.
   - The search rail is the first candidate.
5. **An incident is not a rule.** The narrative goes once to `docs/references/`. A rule needs two incidents or
   Andrew's word.
6. **Process edits take a light path.** The CTO owns them and Andrew approves. They never go through L1-L10.

---

## Method, denominators, and what was not measured

- **Commits:** `git log --no-merges --numstat` on CLOUD, 2026-06-01 to 2026-09-24T15:00Z (33,482 non-merge commits).
  - Paths are classified PRODUCT when a code extension (.py .ts .tsx .js .sh .ps1 .tf .sql .css .html and so on) sits
    outside org/, docs/, .tools/, .claude/ and rcg/.
  - The 7.6-day window is 2026-09-17T00:00Z to 2026-09-24T15:00Z.
  - Portal: `git log --all --no-merges` in portal/ over the same window (181 commits).
  - Code on unpushed local branches of another seat is invisible to both.
- **Cells:** regex over subjects and task-order file names, since Sep 1 (1,053 ids).
- **Messages:**
  - `org/mcp/broker.db`, read-only: 4,167 messages since Sep 14.
  - `org/mcp/message_archive/*.jsonl`: 89,885 messages through Sep 21.
- **Rail:** `org/mcp/comp-which-rail.log` events since Sep 17.
- **Lane gate:** `org/git-author-override-audit.log` since Sep 17.
- **Surprise channel:** 237 files under the missions tree plus the legacy root; dispositions counted over 118
  adjudication files.
- **Tried and dropped:** a keyword classification of task-order titles into product and meta. It was too noisy to
  quote (it filed a harvest writer as meta).
- **Not measured:**
  - Wall-clock cost of safe-commit and safe-merge per commit.
  - Token spend.
  - Whether graduated rows concerned product defects or instrument defects. This is the one number that would price
    the verification layer's yield, and it is the next measurement to take.
