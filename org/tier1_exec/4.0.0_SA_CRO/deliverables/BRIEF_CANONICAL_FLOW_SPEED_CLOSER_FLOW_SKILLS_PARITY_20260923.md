# BRIEF -- canonical-flow speed, the closer flow, and Claude/Codex skills parity

**Author:** `4.0.0_SA_CRO` (Claude runtime). **UTC:** 2026-09-23 ~16:0xZ. **Kind:** a BRIEF with a handful of ranked
changes, returned to `1.0.0_SA_CTO~C` to implement as needed. **NOT a project:** no L2-L10, no registration, no task
orders.

**Commissioned by:** Andrew-direct at the `1.0.0_SA_CTO~C` terminal 2026-09-23 ~14:5xZ, relayed as message 99661.
VERBATIM: *"Have CRO investigate this in depth and write a proper brief. I don't believe we need a whole project, i
think they just need to identify a handful of high-leverage improvement opportunities, they send it back to you and you
get those implemented as needed. This includes what i described in the transcript as well as making sure we have the
necessary skills represented in both claude and codex environments."* The transcript is recorded verbatim at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260923_CANONICAL_FLOW_OPS_AND_CLOSER_FLOW.md` @`c564b6262a`.
The HOLD of MSTR message 99652 is lifted for this task only, per the same relay.

**How this was measured.**
- Workspace HEAD moved from `a28305aefc` to `7a3fd28e11` during the work. The portal was at DEV `fac3b6a0`.
- Three read-only research subagents worked in parallel:
  - the canonical IRPT rounds (IRPT = Investor Reporting);
  - the closer run, reconstructed from git, inboxes and records;
  - the skills census.
- This seat re-read the load-bearing claims itself before quoting them, printing the bytes at each cited line.
- Every figure below is labelled **MEASURED** (counted or read, with its denominator) or **INFERRED** (a
  classification or a reading).
- The agents' scripts and JSON outputs are in this session's scratchpad (`parse_tos.py`, `rounds.py`, `classify2.py`,
  and the skills census script). They are reproducible but not committed.

---

## 0. The answer

1. **The two flows have ONE defect in common, and it is the defect Andrew named in issue 1.** Both prove work
   component by component, against fixtures, offline, and reach a live end-to-end journey LAST.
   - **Canonical:** after 15 frontend rounds and 18 backend rounds, **zero** product journeys work end to end and
     **zero** outcomes grade REALIZED.
   - **Closer:** it got to code in 46 minutes, but it ran about 8 hours of offline "bounded" closures before first live
     contact. **Both** live contacts then failed on seam defects the fixtures could not see.
2. **The canonical machinery is not the slow part.** Hand-offs between rounds take 4-72 minutes (MEASURED). The time
   goes into WHAT a round contains:
   - verification scaffolding;
   - repairs to test instruments and records;
   - styling residuals;
   - a frontend/backend split in which **no cell owns the seam between the two**.
3. **So the leverage is in five places:**

| # | Change | Kind |
|---|---|---|
| R1 | **Live thread first.** Round 1, and the first milestone of any closer effort, is ONE live journey end to end at coarse resolution, and the seam is inside it. | light canonical edit + closer skill |
| R2 | **Every later round is an ENRICHMENT round with a named list.** Remediation rides along; it no longer defines the round. | light canonical edit |
| R3 | **Verification diet on the task order.** At most three mechanical criteria. Repo-wide checks move to the drain; judgment criteria only where an outcome needs one. | light canonical edit |
| R4 | **`/closer`: the closer flow as a skill.** Trace brief -> one-page contract -> seat mandates -> live-first execution, with its three measured costs fixed. | closer skill |
| R5 | **One skill source, both runtimes.** Extend the existing Codex installer from 2 hard-coded skills to a manifest; fix the frontmatter that makes 28 of 29 Claude skills fail Codex's validator. | parity |

   Cost of all five together: one spine amendment, edits to four existing skills, one new skill with four templates,
   one installer change and one manifest. **No new gate** (§2 of CLAUDE.md: no approval gate unless Andrew asks).

---

## 1. The diagnosis -- one defect, two flows

### 1.1 Canonical: the specimen is IRPT_FNTEND + IRPT_BCKEND

Both projects live under `org/missions/D9/IRPT/`. Rounds are drawn from the first task-order add to the CTO's L10
commit.

- **Scale (MEASURED):**
  - Frontend: 15 rounds, 91 task orders (TOs) totalling 1.34 MB, 788 parsed criteria.
  - Backend: 18 rounds, 102 TOs totalling 1.95 MB, 213 parsed criteria. The backend declares about 8 more that were
    written as prose.
  - Surprise channel: 683 investigation rows, 414 adjudication rows and 377 remediation rows across the two projects.
- **Outcome (MEASURED):** zero journeys end to end, zero outcomes REALIZED.
  - The CTO's own assessment: *"The reviewed evidence establishes **zero of the three requested product journeys end to
    end**."* (`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_DISTANCE_AND_THREE_AGENT_ASSESSMENT_20260922.md:9`
    @`b2b2f0f4c1`, printed by this seat).
  - Frontend round-9 grades: 8 of 8 outcomes NOT_EVALUATED (`ledger/COMPLETION_GRADES.round9.json` at HEAD, parsed by
    this seat).
  - Backend round 3: "ZERO of 10 REALIZED" (`5c59f68d70`).
- **The seam belonged to no one (MEASURED text, INFERRED consequence).** Both PRDs say at `:16`: *"Two projects, two
  decompositions, two task-order sets, two adjudications; no cell is jointly owned."* Each side then proved against
  its own fixtures, and the seam defects only showed up at the end:
  - The CTO assessment names the mismatches:
    - `:34`: *"The frontend sends dates in query parameters ... the entry reads different date fields and interprets
      the path value as an account ID."*
    - `:36`: *"Six of the composer's seven keys do not intersect the generation entry's accepted field list."*
  - The backend states it about itself at `IRPT_BCKEND.TO-IB-rtr-e:1` @`34366c30d1`: *"every prior round proved its
    own component against its own fixtures."*
- **Fixtures were designed in at round 1, cell 1 (MEASURED).** The frontend decomposition's round-1 rectangle is
  **eleven horizontal cells over the PRD's surface manifest**: contracts/client, page shell, tabs, render package, one
  cell per tab, export, global view, design. Cell `FE-s-1` is *"contracts, typed client, **fixture adapter**, consumer
  fixtures"* (`decompositions/IRPT_FNTEND_DECOMP.md:83` at HEAD). No cell is a vertical journey.
  - The spine produces this shape by construction: L5 is *"the rectangle over the manifest's surfaces"* (spine L5).
  - ⚠ The spine names `/atom-decomp` as the L5 tool, but the IRPT decomposition carries **zero** atom-decomp markers.
    The method is not the cause. The grid is: it is laid over surfaces instead of over the hops of a journey.
- **The rounds stopped building product (MEASURED count, INFERRED classification).**
  - Frontend BUILD share of criteria by round: 68% in round 1, **0%** in round 10, 16% in round 14, **0%** in round 15.
  - Frontend rounds 12-15 held 17 TOs: 8 instrument/fixture/checker, 8 styling, 1 functional.
  - The whole build step of `FE-s-87`, a 19.7 KB order with 8 criteria, is *"**Fix.** `AnswerStatus.tsx:84`:
    `font-semibold` -> `font-bold`"* (`:24` @`7d82ec72e5`, printed).
  - Backend round 15 is one TO correcting a transposed hash in a record. Round 16 is one TO qualifying a prose line.
    Rounds 9-14 are six consecutive repairs of one capture tool, each with its own never-widen sign-off (24 CTO-half
    sign-off files).
- **Verification dominates the task order.**
  - Frontend criteria: VERIFY 424 of 788 (53.8%), BUILD 294 (37.3%), RECORD 70 (8.9%) (INFERRED classification over the
    whole population).
  - Backend criteria: VERIFY 97 of 213 (45.5%).
  - Build instruction as a share of TO bytes, in five sampled TOs: 20.7%, 9.3%, 5.4%, 12.1% and about 3.5% (MEASURED
    bytes, INFERRED line classes).
  - Repo-wide `typecheck`: 83 of 91 frontend TO files (MEASURED by this seat, file-level; the agent's criterion-level
    count is 82).
  - A judgment criterion: 86 of 91 frontend TO files.
  - IRPT portal code at DEV `fac3b6a0`: 17.7k lines of product against 34.6k lines of tests and 16.5k lines of fixtures.
- **Where the calendar went (MEASURED).**
  - Frontend: 123 h inside rounds and 165.6 h between them, of which **146.4 h is one gap** (round 8 -> 9, zero
    commits on 09-16 through 09-18).
  - Backend: 281.9 h inside rounds, including one round held open 157.6 h.
  - Both idle windows ended on Andrew's 09-21 re-prioritisation (`7df516b46e`). That is prioritisation, not flow
    mechanics, and no edit here fixes it (§3).
  - Excluding the two outliers, the L10 -> next-issuance hand-off is 4-72 minutes.

**The spine sentence that makes every round after the first a repair loop** (spine L6, and `/dispatch` Step 1):
*"No cell is left for a later round; a later round exists only when the CTO's round-N analysis sends work back."*
Round 1 must cover the whole rectangle at full resolution. Every later round exists only to repair. There is no concept
of coarse-first and enrich-later. That absence is issue 1, stated in the spine's own words.

### 1.2 Closer: the IRPT P/M/Y run, 2026-09-22 19:18Z to now

- **What it is (MEASURED).** It is not only a Codex CRO method. It is a chain with four stages:
  1. **CRO trace briefs:** six briefs committed about 12 minutes apart, 19:21 -> 20:38Z, 2.4-2.6k words each, 9-13 hops
     per tab.
  2. **The CTO's distance assessment**, 20:21Z.
  3. **The CTO's contract plus seat mandates**, 20:33Z, `a28ca2dd73`
     (`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2, 94 lines).
  4. **Three Codex COO seats implementing directly, with three CVO seats reviewing each pinned candidate.**
- **Why it was fast (MEASURED).**
  - First product code landed at 21:19-21:28Z, **46-55 minutes after the contract**.
  - The fix-and-retest cycle ran 20-40 minutes. Example: R-P05 was found at 21:19, fixed at 21:31 and closed by 21:45.
  - There were 31 pin "consume" merges between the seats and no product merge conflict was found. That absence is weak
    evidence, because the Codex commit messages carry subjects only.
- **Why it has not finished (MEASURED).**
  - About 8.5 h passed from the contract to the first live contact, the PROD portal release v2.1.184 at 05:07Z on 09-23.
  - **Both live contacts failed:**
    - 05:09Z: *"Scope could not be resolved."* Cause: the handler returns selection fields while `ResolvedScope` needs 7
      others; the directory Lambda was last deployed 09-21; the `/selections` route was absent.
    - 13:13Z: an authenticated bootstrap returned HTTP 200 with `ok:false UNAVAILABLE/UNEXPECTED`, and the deployed
      artifact reproduces `BucketUnmapped` (`IRPT_MVP_COMPLETION_20260922/LOCAL_LIVE_PARTNER_SCOPE_20260923.md`,
      read by this seat).
  - Sensitivity: *"All14 integrated criteria remain NOT_EVALUATED"* (`3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/ACCEPTANCE_MATRIX.md:572`,
    printed).
  - ⚠ The Performance CVO matrix was last committed at 21:01Z on 09-22, before any code, so it proves nothing either
    way. The live failure record is the measurement for P.
- **The shared first hop is the blocker (INFERRED from the two failures).** Both failures sit on the scope/bootstrap
  hop, which **every** tab crosses first. An offline closure on any downstream hop could not have been worth anything
  live while that hop failed.
- **What it cost (MEASURED; ten inboxes, 09-22 19:00Z to about 15:10Z on 09-23).**
  - 1,544 messages, 88% with IRPT in the subject.
  - 135 subjects prefixed ACK, although the contract says *"do not flood peers with routine status or ACK loops"*.
  - The CTO sent 366 of the 1,544 (24%).
  - Of about 400 unique commits by these seats, about 38% touch product and the rest are records.
  - STATUS and INTERFACES files grew into 30-47 KB timestamped journals. M's 5 KB current-state shape was enough.
  - Two governance chains ran inside the sprint:
    - legacy-read: 7 or more review documents;
    - S7/X10 storage placement: five seats involved, and the destination is still not writable.
  - The CTO needed five path-grant commits.

### 1.3 The common cause, in one line

**The unit of proof is the component, and the live journey is the last thing either flow touches.** Canonical adds
pedantry on top of that: verification-heavy task orders, and rounds that repair instruments. Closer adds mail volume.
**Neither flow's first act is "make one real request travel the whole way and render."** The five changes below make
that the first act, and then keep everything after it cheap.

---

## 2. The five opportunities, ranked

### R1 -- LIVE THREAD FIRST *(light canonical edit + closer skill; highest leverage)*

**Problem.** §1.1 and §1.3: 0 journeys working after 33 canonical rounds, 0 of 2 live contacts passing in the closer
run, and in both the failures sat on seams that no fixture exercised.

**Change.** The first deliverable of any pipeline-to-product effort is **the THREAD**:
- one named person;
- one journey;
- coarse resolution: one firm, one account, the default window, no export;
- run on the **deployed** stack, **through the real browser -> API -> backend -> data/provider -> screen path**;
- proven by ONE trace artifact that records each hop's request and response and ends in the rendered screen.

Rules for the thread:
- **A fixture may stand in for a hop only while that hop is not yet reachable. A thread with any fixture-fed hop is NOT
  done.**
- **The seam is inside the thread by construction, so it always has an owner.**

Canonical edits, all text:
1. **Spine L2** (`/endpoint --forward`, Step F2 at `.claude/skills/endpoint/SKILL.md:126`). A product's first outcome is
   the THREAD outcome, with `DONE WHEN: EXERCISED -- one live trace, deployed, rendered`. The other outcomes are cut
   as today.
2. **Spine L4** (PRD template). Two new named sections:
   - **THREAD**: the hop list, `N. A -> B`, from the trace.
   - **ENRICHMENT BACKLOG**: everything off the thread, ordered, one line each.

   Both sit in the BRIEF half of the sign-off, so L4-R still covers them.
3. **Spine L5.** The round-1 rectangle is **over the thread's hops**, one cell per adapter to build or repair, instead of
   over the manifest's surfaces. Keep the manifest rectangle for later enrichment rounds, where it fits.
4. **Spine L6 and `/dispatch` Step 1.** Replace the sentence quoted in §1.1 with: *"The issuance covers every cell of
   THIS ROUND's decomposition. Round 1's decomposition is the thread; every later round's is the enrichment list the
   CTO's round-N analysis names (R2)."*
   - The L6 gate's COVERAGE limb needs **no change**: it compares the issuance to the round's decomposition, and the
     decomposition itself is now the thread.
5. **New products only: one journey = one project.** Do not split a product into frontend and backend projects again.
   Where a split already exists, the PRD pair names **one** project as the owner of each seam hop. The spine or PRD text
   *"no cell is jointly owned"* is what left IRPT's seam ownerless.
6. **`/brief-create` PART I.** Add one line: the brief names the candidate THREAD, meaning which person and which
   journey at coarse grain, so L2 has something to cut FWD-1 from.

**Lands on:**
- `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` (v3.16, L2/L4/L5/L6, one changelog line citing Andrew's record);
- `.claude/skills/endpoint/SKILL.md` Step F2;
- `.claude/skills/dispatch/SKILL.md` Step 1;
- `.claude/skills/brief-create/SKILL.md` PART I;
- the PRD template.

**Cost:** one spine amendment plus four short skill edits. No gate change.

**Non-application:** a pipeline with no product surface, where the thread is source -> served artifact; and a pure
infrastructure or governance project.

**Transition:** under spine §5 an open round finishes under its cut task orders.

**Claude + Codex:**
- The five spine/skill texts above are Claude skills. `brief-create` and `endpoint` go on the parity manifest (R5), so
  a Codex CRO or CTO seat carries them too.
- On the closer side, R1 is the first rule of `/closer` (R4) in both runtimes.

### R2 -- EVERY LATER ROUND IS AN ENRICHMENT ROUND, WITH A NAMED LIST *(light canonical edit)*

**Problem.** Rounds after the first are defined only as repair loops (§1.1), so they fill with repairs to instruments,
records and styling.
- Frontend round 15 and backend rounds 15 and 16 contain no product work.
- Six backend rounds went to one capture tool.
- 377 remediation rows each became candidate cells for the next round.

**Change.** The CTO's round-N analysis gains one mandatory section, **ENRICHMENT LIST for round N+1**:
- It names, from the PRD's ENRICHMENT BACKLOG, the capabilities round N+1 adds: next firm, next window, the selected-set
  case, export, the second tab, and so on. One item = one cell.
- It is **ordered by what a user gains**, and each item keeps the live thread green.
- Remediations ride in the same issuance, with two rules:
  - a remediation that concerns only a verification instrument, a record or a style residual is **batched into ONE cell
    per round**, never a round of its own;
  - a remediation that breaks the live thread goes first.

Andrew may re-order or replace the list at any time by his word. No limb waits on him (spine L2 autonomy stands).

**Lands on:**
- spine L10, "the round-N analysis" paragraph (one sentence on contents, one on the batching rule);
- the shape of `ledger/ROUND_ANALYSIS.round<N>.md`, which the spine names as a file and not as a template (if the CTO
  keeps a template, that too);
- `.claude/skills/canonical-drive/SKILL.md` obligation 1 (the recut reads the list);
- `/dispatch` Step 1 (R1's sentence).

**Cost:** text only.

**Non-application:** the close. A round whose every outcome grades REALIZED is CLOSED, not enriched.

**Claude + Codex:** the canonical COO loop (`/canonical-drive`, `/dispatch`) is Claude-only by construction, because
its workers are Claude subagents (R5). The CTO's analysis is prose, and a Codex CTO follows the same spine section.

### R3 -- VERIFICATION DIET ON THE TASK ORDER *(light canonical edit; prompting, not a gate)*

**Problem.** §1.1: 53.8% of frontend criteria are verification; build instruction is 3.5-20.7% of TO bytes;
`typecheck` appears in 83 of 91 TOs; a judgment criterion appears in 86 of 91.
- In rounds 11-14, anti-vacuity arms (54 in all, 31 of them in those rounds) turned a one-token style fix into an
  eight-criterion order.
- Andrew's word: *"maybe this is a function of prompting, that when we set up these task orders in the beginning, that
  the point is coarse resolution"*.

**Change.** The cut rules, written into the task-order template and `/dispatch` Step 2:
1. **At most THREE mechanical criteria per build TO:**
   - (a) the built behaviour;
   - (b) the hop's seam probe against its REAL neighbour where reachable, a fixture only where not;
   - (c) the live thread trace, re-run **once per round** by the COO at the drain, never per TO.
   A fourth needs a one-line reason on the face.
2. **Repo-wide hygiene leaves the criteria.** Typecheck, lint, the full suite and `py_compile` are **drain checks** the
   COO runs once per merge, next to `safe-merge.sh`'s row gate. They stop being acceptance criteria on each order.
3. **Judgment criteria only where the outcome needs judgment**, meaning a user-facing reading or a design conformance
   grade. They are not a default slot on every face.
4. **Battery lenses on a THREAD round are DECLARED-NOT-APPLICABLE by default**, with the reason "thread round; the lens
   runs on the enrichment round that touches its surface". `comp-iam` still RUNs whenever the thread touches IAM.
5. **Keep, unchanged:**
   - the refusal clause (spine L6);
   - v3.12's difference control, which is already scoped to criteria that assert a control;
   - the proof-of-spec instance.

   These are cheap and caught real defects. The diet removes volume, not these controls.

**Lands on:**
- `org/ref/TASK_ORDER_PROTOCOL.md` (the XML template, `:26` onward);
- `.claude/skills/dispatch/SKILL.md` Step 2;
- spine L5 (battery clause) and L6 (cut discipline, one sentence each);
- `.claude/agents/worker.md` (it runs what the face says, so no rule change there, only the smaller face).

**Cost:** text only.
- The measured payoff (INFERRED from the byte shares): a build TO shrinks by about half.
- The per-TO typecheck and suite re-runs, 137 of 788 frontend criteria, move to one run per merge.

**Not proposed:** a gate limb that refuses more than N criteria. That would be an agent-made gate (CLAUDE.md §2). It is
available only on Andrew's word, and the prompt change should be tried first.

**Claude + Codex:** the TO protocol is a file both runtimes read. `/dispatch` is Claude-only (R5).

### R4 -- `/closer`: THE CLOSER FLOW AS A SKILL *(closer skill; formalise lightly)*

**Problem.** The closer run turned six briefs into running code in under an hour (§1.2). But it exists only as one-off
files in the CTO's IRPT folder, and it carried three measured costs:
- offline-first sequencing;
- 1,544 messages including 135 ACKs;
- journal-sized STATUS files and governance side-chains.

It also has no place in the spine. Spine §5 retires *"a document that describes this process in a second shape"*, so an
unanchored closer skill would collide with the spine.

**Change: a skill with four artifacts, each templated from the IRPT originals.**
1. **TRACE brief, one per product surface** (the CRO, or any Tier-1 seat; the 09-22 shape, measured in §1.2). Sections:
   - Design finding.
   - Current measurement, **read from DEPLOYED bytes** (download the artifact and compare its digest to source).
   - Adapter map: surface x provider x existing work x gap.
   - **Numbered hop walk.** Each hop is headed `### N. A -> B -- <STATE>`, where STATE is one of `WORKS`, `INCOMPLETE`,
     `MISSING` or `MISMATCHED`. Each hop states what exists (paths) and the exact mismatch, and ends in a **`Close:`**
     line.
   - Completion sequence, **whose step 1 is the live thread (R1)**.
   - Acceptance, as one reconciled trace per case.
   - Evidence anchors and limits.
   - Andrew verbatim.

   LGIC (the D14 naming structure): any new address or name in a `Close:` line is `lib/opal_naming.py` builder output
   (CLAUDE.md Rule 30). The trace carries an LGIC subsection only when the delta adds storage or names. The Performance
   brief had 0 LGIC hits and did not need them.
2. **CONTRACT, at most two pages** (CTO; from `CONTRACT.md` v1.2, which works). It holds:
   - the outcome journeys;
   - the operating mode: implement directly, no task orders, no recuts for in-scope fixes;
   - **the one-writer-per-shared-surface table.** A more specific row wins. Consumers send pinned patches and the owner
     integrates. **The table is also the path grant, landed in the SAME commit**, where IRPT needed five grant commits;
   - the shared semantic contracts, which double as acceptance IDs;
   - the breaking-change rule: one exchange between peers, then the CTO rules;
   - the review rule: the CVO grades a pinned candidate PASS / FAIL / NOT_EVALUATED, and *"offline success cannot be
     called deployed E2E PASS"*.
3. **MANDATE per implementing seat**, one page (from `COO_P.md`). It gives the first action, *"implement one ... end to
   end"*, and the acceptance IDs.
4. **EXECUTE and REVIEW**, which is how the run already worked: pin handoff, consume-merge into an isolated worktree, a
   CVO review per pinned candidate, and CTO integration.

**The three measured fixes, written into the skill:**
- **LIVE FIRST.** The first milestone is the deployed live thread through the **shared first hop** (auth, scope,
  bootstrap), owned by one seat and proven live before any per-product offline closure counts toward an acceptance ID.
  Offline closures are allowed. They grade nothing until the thread is live.
- **FILES OVER MAIL.**
  - STATUS.md is a **fixed-shape current-state file, overwritten in place**: pins, write claims, next proof,
    dependencies with owner, limits. That is M's 5 KB shape, not a journal.
  - INTERFACES.md holds the **current** versioned schema and example, with superseded text moved to a history file.
  - Messages carry three things only: **interface published, blocker, review handoff.** **No ACK messages.**
  - CTO rulings append to one `RULINGS.md` and go out as one message per batch, not one per ruling.
- **NO SIDE-QUESTS.** A naming, registry or storage-policy question **not on the thread** is PARKED with an owner and
  the condition that un-parks it. It is not run as a review chain inside the sprint.

**Where it sits in the fabric.** Add one short spine subsection, **"Closer -- a product in flight, on Andrew's word"**,
beside the existing "Midstream" subsection:
- *when* it applies: components exist but no journey works, and Andrew names it;
- its four artifacts and the three rules above;
- how it **hands back**: once the thread and the named journeys pass, remaining work returns to canonical enrichment
  rounds (R2) or to a close.

This keeps one process document and makes `/closer` its instrument, not a second shape.

**Lands on:**
- new `.claude/skills/closer/SKILL.md` plus `templates/{TRACE_BRIEF,CONTRACT,MANDATE,STATUS}.md`;
- the spine subsection above;
- `/brief-create --midstream`: one pointer line (*"a product with pieces but no working journey -> `/closer`"*).

**Cost:** one skill, about 150 lines, plus four templates lifted from existing IRPT files; one spine subsection.

**Non-application:** greenfield work (canonical R1 already starts with the thread) and a single-surface fix.

**Claude + Codex: BOTH, from ONE source (R5).**
- In the IRPT run the implementing seats were Codex and implemented directly with no subagents. That is the Codex-native
  shape and needs nothing Claude-only.
- The skill names both send paths in one runtime block:
  - Claude: MCP `send_message`;
  - Codex: `org/mcp/codex-send.ps1`.

### R5 -- ONE SKILL SOURCE, BOTH RUNTIMES *(parity)*

**Problem (MEASURED at `a28305aefc`; the installer constants and the validator re-run by this seat).**
- **Codex coverage:** of 29 fabric skills, Codex has real ports of **2** (`log`, `open-calls`) and partial substitutes
  for 3.
  - Its `$drive` is an Anatomy loop, **not** `/canonical-drive`, and it collides by name with the Claude `/drive`
    alias.
- **The copy mechanism is hard-coded.** The one mechanism that copies skills into Codex,
  `org/mcp/install-codex-load-skill.py`, runs at every Codex seat launch. It:
  - hard-codes `CANONICAL_SKILLS = ("load", "log")` (`:21`);
  - refuses any file other than `SKILL.md` + `agents/openai.yaml` (`:20`).
- **Frontmatter fails validation:** Codex's validator (`~/.codex/skills/.system/skill-creator/scripts/quick_validate.py`)
  **fails 28 of 29** Claude skill files as written. Causes:
  - 19 have an unquoted `: ` in `description`;
  - 5 have angle brackets;
  - 4 have no frontmatter at all.

  This seat re-ran it on four files: `dispatch` fails on angle brackets, `brief-create` fails the YAML parse,
  `canonical-drive` has no frontmatter, and `log` is valid. The failure is quoting, not content.
- **Skills outside the repo:** four Codex skills (`drive`, `02check`, `opencalls`, `yolo`) exist only in `CODEX_HOME`.
  That folder is shared with the tradeops fabric.

**Change.**
1. **A manifest**, `org/mcp/codex-skills/PARITY.yaml`. One row per skill with:
   - `source` (`.claude/skills/<x>` or `org/mcp/codex-skills/<x>`);
   - `runtime` (`both` | `claude` | `codex`);
   - for a single-runtime skill, `equivalent` (what the other runtime uses instead).
2. **The installer reads the manifest** instead of `CANONICAL_SKILLS`, and admits `templates/` and `references/`. It
   keeps its sha256-verified copy and **adds a `--check` mode** that prints drift per skill. That is a read, not a gate.
3. **Quote the frontmatter** on every `both` skill so it passes `quick_validate.py`. This is mechanical.
4. **One "Runtime" block per `both` skill** where the body names a Claude-only tool:
   - Claude: MCP `send_message`, Monitor, subagent;
   - Codex: `codex-send.ps1`, the launcher's inbox bridge, direct implementation.
5. **Bring the four home-only Codex skills into the repo** under `org/mcp/codex-skills/`, and rename Codex `$drive` so
   it no longer collides with the Claude `/drive` alias. Skill names must be unique across both fabrics while
   `CODEX_HOME` is shared.

**The parity set, by the flows in this brief:**

| runtime | skills | why |
|---|---|---|
| `both` | `closer` (new, R4), `brief-create`, `endpoint`, `canonical-flow` (read-side stage measurement), `to-check`, `prd-check`, `verify`, `seams`, `handoff`, `open-calls` (Codex already has it), `next-calls`, `log` (Codex already has it) | the prose/engine class: 0 Claude-only tool hits, or engines in `.tools/` any runtime can run |
| `claude` | `dispatch`, `canonical-drive`, `watcher` | built on Claude subagents and Monitor. The Codex `equivalent` rows: direct implementation under `/closer`, and the launcher's inbox bridge |
| `codex` | `load`, `yolo`, `02check`, the renamed drive loop | runtime or fabric specific |

**⚠ A constraint the CTO carries (not this brief's to lift).** Andrew's ruling of 2026-09-02, Call 2(b), says Codex seats
issue **no comp-tool-grounded adjudication until a Codex rail exists**
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260902_230xZ_OPEN_CALLS_x2_TREE_LANES_ANY_CODEX_RAIL.md`).
- No lifting record was found, but not all 34 files that mention it were read.
- It bounds what a Codex CVO may do with `verify` and `seams`. The manifest should carry it as a note on those two rows.

**Lands on:**
- `org/mcp/install-codex-load-skill.py`;
- the new `org/mcp/codex-skills/PARITY.yaml`;
- frontmatter on about 12 skills;
- one Runtime block on each `both` skill that needs one.

**Cost:** about 30 lines in the installer, one manifest, and quoting edits.

**Non-application:** Claude-only skills keep their text. The manifest's `equivalent` column is their whole parity
obligation.

---

## 3. What NOT to change, and why

- **The L8-L10 hand-off machinery.** L10 -> next issuance is 4-72 minutes (MEASURED). The slow part is what rounds
  contain, not how they are handed off. Leave the slug, the round-N analysis and the single router alone.
- **The refusal clause, the surprise row, the proof-of-spec instance.** These are cheap, and the spine records the
  refusal clause as the only control that has caught a defect in a cut. R3 shrinks volume around them and keeps them.
- **The L4-R sign-off.** It cost real time on IRPT: frontend 10 signed and 6 refused commit subjects, backend 15 and 4.
  But it is Andrew's explicit design (2026-09-10/11), and this brief does not propose loosening it. R1's two PRD
  sections sit inside the half it already reviews.
- **The idle windows** (frontend 146.4 h; backend round 2 open 157.6 h). They ended on Andrew's re-prioritisation, not on
  any limb. No flow edit shortens a window nobody was working in.

## 4. Suggested order for `1.0.0_SA_CTO~C`

1. **R5 installer + manifest + frontmatter first.** Smallest, and every later skill edit then reaches both runtimes on
   the next Codex launch.
2. **R4 `/closer`**, from the IRPT originals, plus its spine subsection, so the active IRPT effort can adopt LIVE FIRST
   and FILES OVER MAIL immediately.
3. **Spine v3.16 carrying R1 + R2 + R3 in one amendment**, then the four skill edits and the TO template. One
   changelog line citing Andrew's 09-23 record. Rounds already cut finish under their cut orders (spine §5).

## 5. What this brief does not claim

- **The classifications are INFERRED**: VERIFY/BUILD/RECORD criteria, instrument versus product TOs, product versus
  record commits. The rules are in the scratchpad scripts, and a different rule set would move the percentages. It
  would not move the direction: frontend BUILD share by round falls to zero.
- **Codex runtime behaviour was not exercised.** No `codex` binary was run. "28 of 29 fail" is the validator script,
  and whether Codex's loader is equally strict is unmeasured. "No subagents on Codex" is an absence in config and
  records, not a tested fact.
- **The closer run is not finished.** It is judged at about 20 hours in, with its product journeys still NOT_EVALUATED.
  Its speed-to-code is measured; its speed-to-working-product is not yet measurable.
- **Author overlap in the commit counts.** A SITEZ-fabric Claude seat committed AMGT_HARVST work under the same author
  string `2.0.0_SA_COO~Y` (47 commits since 09-21 12Z). Those commits were excluded from the closer counts by subject;
  the exclusion is by content, not by device.
- **No claim that the canonical rounds produced nothing.** The closer briefs say the parsers, normalisers,
  authorisation and render libraries are reusable, and the closer contract builds on them. The defect is that none of
  it was ever proven *together*.

## 6. Evidence index

| claim | where | vintage |
|---|---|---|
| zero journeys end to end; date and field mismatches | `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_DISTANCE_AND_THREE_AGENT_ASSESSMENT_20260922.md:9,:34,:36` | `b2b2f0f4c1` |
| no cell jointly owned | `org/missions/D9/IRPT/IRPT_{FNTEND,BCKEND}/prd/*_PRD.md:16` | HEAD `7a3fd28e11` |
| round-1 horizontal rectangle; fixture adapter | `org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md:26,:83` | HEAD |
| font-weight TO | `.../task-orders/IRPT_FNTEND.TO-FE-s-87.answer-status-weights-700-400-under-c1.md:24` | `7d82ec72e5` |
| own component, own fixtures | `.../task-orders/IRPT_BCKEND.TO-IB-rtr-e.the-one-offline-actual-module-chain.md:1` | `34366c30d1` |
| round 9: 8 of 8 NOT_EVALUATED | `org/missions/D9/IRPT/IRPT_FNTEND/ledger/COMPLETION_GRADES.round9.json` | HEAD |
| the repair-loop sentence | spine L6; `.claude/skills/dispatch/SKILL.md` Step 1 | HEAD |
| closer contract / mandate | `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/{CONTRACT,COO_P}.md` | `a28ca2dd73` onward |
| closer first code | `70598ece96` (P) 21:19Z, `33e630885f` (M) 21:21Z, `e7dd1c3c6c` (Y) 21:28Z | -- |
| live failures | `b06c6cd8b6` (PROD v2.1.184, 05:07Z); `.../IRPT_MVP_COMPLETION_20260922/LOCAL_LIVE_PARTNER_SCOPE_20260923.md` | `c225382016` |
| Y integrated 14 of 14 NOT_EVALUATED | `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/ACCEPTANCE_MATRIX.md:572` | `cd59b9de6c` |
| trace brief shape | `org/tier1_exec/4.0.0_SA_CRO/deliverables/PERFORMANCE_END_TO_END_GAP_BRIEF_20260922.md` (+ SENSITIVITY_, MODEL_OVERLAY_) | `92e093a2d0` |
| installer constants | `org/mcp/install-codex-load-skill.py:20-21` | HEAD `4be8608939` |
| Codex validator | `~/.codex/skills/.system/skill-creator/scripts/quick_validate.py` (outside the repo) | run 2026-09-23 |
| Codex rail ruling | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260902_230xZ_OPEN_CALLS_x2_TREE_LANES_ANY_CODEX_RAIL.md` | -- |
