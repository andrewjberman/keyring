# NFRA_IAMROLES202609 -- L5 decomposition (COO) -- v0.1

**Seat:** `2.0.0_SA_COO~ZI`, seated 2026-09-10 03:23Z (`0.0.0_AB_MSTR~Z` msg 20764, on Andrew-direct
2026-09-10 ~02:5xZ *"go with your recs on all six"*, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_025xZ_OPEN_CALLS_ALL_SIX_RECS_APPROVED.md`
@9382d107a3). **Directive:** D12. **Fabric:** site-z. **Consumes:** PRD v0.2 section 8 SURFACE MANIFEST
@076f37eeb2.

**The rectangle is RECEIVED, not derived here.** L4 wrote the manifest; L5 mirrors it, re-grounds each
cell at its own vintage as the manifest instructs, adds the dependency edges, the placement axis and
the battery. **This file does not re-open the manifest's MECE** -- that was run at L4 in both
directions (9 of 9 OWNS items covered, 9 rows, 0 orphans, 8 of 8 outcomes carried).

---

## 1. The rectangle -- nine cells, `IAM-s-<n>` mirroring manifest row `S<n>`

**INVARIANT THIS FILE COMMITS TO:** *every cell mirrors a manifest row, and every manifest row has at
least one cell.* ⛔ **IT IS NOT A BIJECTION AND IS NOT DECLARED AS ONE.** PRD section 8 records the
9-and-8 as a measurement at that edit and warns in terms that it is not an invariant, because
`NFRA_OPSEC202609` asserted a bijection in a heading which then went FALSE with nothing able to fail.
**MEASURED AT THIS EDIT: 9 `IAM-s-` cells over 9 manifest rows; every cell mirrors a row; every row
carries exactly one cell.** A round-2 recut giving a row a second cell breaks nothing here.

**CELL-ID CONFORMANCE, MEASURED not assumed** (`org/standards/DECOMP_CELL_ID_CONVENTION.md`): the ids
are SHAPE 1, the form the standard says to prefer for new decomps, so **no new regex branch is
requested and neither of the standard's two controls is owed.** Verified against the enforcer object
itself (`.tools/proof-of-spec-check.py` `CELL_ID_RE`, loaded and applied to this file's bytes, not
eyeballed). The run and its output are in this file's commit message.

⛔ **NO EXEMPLAR CELL ID IS WRITTEN ANYWHERE IN THIS FILE, AND THAT IS DELIBERATE.** The L6 coverage
limb indexes **every cell-shaped token in this document as a cell of this decomposition**. `NFRA_REPORT`'s
decomp quoted three known-good exemplars from the cell-id standard's shape table and they became
PHANTOM CELLS: it declared 15 cells, the issuance owned 12, and the coverage limb refused the issuance
naming a shortfall that did not exist. **A control example written inside the artifact it certifies
becomes data in that artifact.** The positive and negative exemplars live in
`org/standards/DECOMP_CELL_ID_CONVENTION.md` and in this file's commit message, which is not indexed.

**CELL STATUS VOCABULARY** (rule 24 record at section 2a). Closed set, and it HAS a not-evaluated
value by construction, because the spine requires one:
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`.
- `NOT-EVALUATED` -- this decomp did not reach the cell. **No cell carries it at this cut**, and that
  is a MEASUREMENT (9 of 9 evaluated), not a vocabulary that lacks the value.
- `OPEN` cuttable now · `IN-FLIGHT` a worker holds it · `HELD` blocked on a named owner ·
  `COMPLETE` served and proven · `CLOSED` retired without being served, with its pointer.

| cell | row | outcome | act | state | round | lane |
|---|---|---|---|---|---|---|
| `IAM-s-1` | S1 | FWD-2 | EXTEND the working `comp-iam-usage` from ROLE grain to PERMISSION grain -- which granted permissions a role has never used, over a stated lookback | OPEN | 1 | iam |
| `IAM-s-2` | S2 | FWD-1 | the POSTURE NUMBER -- one figure, carrying its denominator and its vintage, rolled up from `IAM-s-1` and nothing else | OPEN | 3 | iam |
| `IAM-s-3` | S3 | FWD-7 | the COVERAGE vocabulary at PERMISSION grain -- `unused` rendered distinctly from `unobservable` | OPEN | 2 | iam |
| `IAM-s-4` | S4 | FWD-3 | the CONDITION AXIS reader -- what a policy REQUIRES of a caller (MFA, source, tags), not only what it scopes | OPEN | 1 | iam |
| `IAM-s-5` | S5 | FWD-4 | the DECLARED-vs-LIVE RECONCILER -- which live roles exist in code and which do not. **RECONCILES ONLY; it does not dispose** | OPEN | 1 | iam |
| `IAM-s-6` | S6 | FWD-4 | the GOVERNANCE DISPOSITION of the undeclared roles -- for each, in-code or a recorded, owned exemption | OPEN | 2 | iam |
| `IAM-s-7` | S7 | FWD-6 | the HISTORICAL REMEDIATION completion evidence -- did each past clean-up actually land, on the ARTIFACT | OPEN | 1 | iam |
| `IAM-s-8` | S8 | FWD-5 | the PRE-FLIGHT BLAST RADIUS -- what a narrowing would break, known BEFORE the change, **exercised against a real narrowing** | OPEN | 2 | iam |
| `IAM-s-9` | S9 | FWD-8 | the RE-RUN HARNESS -- the whole assessment repeatable by someone who did not build it | OPEN | 4 | iam |

---

### 1a. The two re-groundings the manifest ASKED L5 to perform

PRD section 8: *"Nothing in this table was re-measured at L4; the brief's `F<n>` ids are cited so the
L5 battery re-grounds each cell at its own vintage."* Both `measured` rows were re-grounded. **One
held exactly. One held in its SET and moved in its DENOMINATOR.**

**RE-GROUNDING 1 -- `S1`/`IAM-s-1`, and it HOLDS.** `C-EXTEND-NOT-BUILD` is the constraint the whole
project leans on, so it was EXERCISED rather than inherited from the brief's document read:
`.tools/comp-iam-usage` exists (mode `-rwxr-xr-x`), is tracked, and forwards to
`org/modules/graph/comp_iam_usage.py`; `comp-iam-usage self-test` **rc=0, 9 of 9 assertions PASS**.
Among them `blind_is_unknown_NOT_unused` and `breakglass_never_used_is_stillborn_NOT_reap` -- so
**FWD-7's discipline already exists and passes AT ROLE GRAIN.** The tool's own banner states the split
the PRD claims: it answers `role-cold` on the identity plane, and the PERMISSION axis is the half that
is absent. ⛔ **`IAM-s-1` AND `IAM-s-3` ARE EXTENSIONS OF PASSING, SELF-TESTING CODE. A cell written as
greenfield re-buys it**, and the existing self-test is the regression bar any extension must keep green.

**RE-GROUNDING 2 -- `S5`/`IAM-s-5`: THE SET IS SETTLED, THE DENOMINATOR IS NOT, AND THE PRD CARRIES
TWO DENOMINATORS IN ONE SENTENCE.** Re-measured on the instrument the manifest names, at this lane's
own vintage:

```
  comp-find '.' --corpus aws IAM_ROLE
  VINTAGE      built from the estate 2026-09-10 03:31:02 UTC; manifest 5361815924ce
  DENOMINATOR  219 hit(s) across 219 aws node(s) scanned [corpus=aws types=IAM_ROLE]
  DRIFT        DECLARED=203  LIVE-no-DECLARED=16          (203 + 16 = 219, reconciles exactly)
```

| vintage | population | DECLARED | LIVE-no-DECLARED |
|---|---|---|---|
| brief `F2` (@1a90986047) | **208** | -- | 16 |
| brief `F2a`, "merged head" | **216** | 200 | 16 |
| this lane, 2026-09-10 03:31Z | **219** | 203 | **16** |

⭐ **THE UNDECLARED COUNT HAS HELD AT EXACTLY 16 ACROSS THREE VINTAGES AND TWO INSTRUMENTS. THE
POPULATION HAS MOVED TWICE.** That is the strongest possible support for the PRD's claim that the 16
are a settled SET -- and it simultaneously falsifies any cell that hardcodes `208`.
⛔ **PRD section 8's `S5` evidence cell states "16 of 208" and "`DECLARED=200 LIVE-no-DECLARED=16`" in
one sentence; those denominators are 208 and 216 and the sentence does not reconcile them.** It is not
a defect in the SET, it is a stale denominator carried beside a fresher one -- **exactly the failure
`FWD-1` exists to prevent, sitting in the PRD that commissions `FWD-1`.** Filed as a row, not a halt.

⚠ **THE COUNT MATCHING IS NOT PROOF THE MEMBERS MATCH.** A stable 16 is equally consistent with
"the same 16" and with "one left and one arrived". This lane did not measure member identity against
the brief's list and **does not claim it**; `IAM-s-5` establishes it. What this lane DID do is
enumerate the 16 at its own vintage so that `IAM-s-6` has a SET to dispose of rather than a count
(`C-TWO-REMEDIES` disposes of roles, and a count cannot be disposed of):

```
  bd-merge-daily-lambda-role          finbert-ec2-backfill-role        portfolio-management-lambda-role
  bd-pipeline-task-role               lambda-ec2-runtime-monitor-role  rds-monitoring-role
  codebuild-semantic-clustering-role  lambda-test-role                 seeking-alpha-scraper-role
  ecsTaskExecutionRole                opal-data-refresh-lambda-role    sentiment_query_api-role
                                      opal-smartx-lambda-role          vpc-flow-logs-role
  portal-auth-lambda-role             workspace-sync-lambda-role
```

⭐ **AND THE SET ITSELF ARGUES FOR `C-TWO-REMEDIES` HARDER THAN THE PRD DOES.** It is not a homogeneous
population. `ecsTaskExecutionRole`, `rds-monitoring-role` and `vpc-flow-logs-role` are AWS
service-default roles a console or service action mints -- their GOVERNANCE answer is plausibly
"recorded exemption, correctly outside our Terraform", while their PERMISSIONS answer is a wholly
separate question. `portal-auth-lambda-role` and `opal-data-refresh-lambda-role` are production
surfaces on the serving path. `lambda-test-role` reads as residue. **One cell answering both questions
across that spread would answer one of them badly for every member** -- which is precisely `D6`'s
claim, now carried on measured members rather than on the constraint's say-so.

---

### 1b. A third figure exists on the DECLARED plane, and it is NOT a contradiction

`comp-iam stats` parses **195 IAM roles from Terraform**, against `comp-find --corpus aws`'s
`DECLARED=203`. ⛔ **THESE ARE DIFFERENT PLANES AND MUST NOT BE SUBTRACTED.** `comp-iam` parses role
*resources it can resolve in the Terraform source*; `DECLARED` is the stitched graph's drift class over
LIVE nodes. `comp-iam`'s own run emits two NOTEs that its role labels `orchestrator` and `scheduler`
were reused across modules and silently mis-linked pre-fix -- so its parse is a measurement of the
PARSER's reach as much as of the estate. **No cell is cut on the 195-vs-203 delta, and no cell may
present it as an undeclared-role finding.** It is named here so a later reader does not discover a
third number and read it as drift. `IAM-s-5` states which plane its number is ABOUT, in the sentence.

---

## 2. Four-postulate record (rule 24) for what this file ADOPTS and ADDS

Rule 24 binds any schema an agent authors **or ADOPTS**. This file adopts the PRD's manifest axes and
adds the cell-status vocabulary (2a) and the round axis (section 5).

- **(i) MECE over a DECLARED domain.** Domain = PRD section 2's **OWNS** cell, NINE enumerated items.
  The uncovered-member hunt was RUN AT L4 and it FOUND TWO (`FWD-5` and `FWD-8` had no OWNS clause);
  the CRO closed it at the source @cbe45b0db4. **This lane hunted the remaining direction -- a manifest
  row serving no cell -- and found none: 9 of 9.**
- **(ii) SAME GRAIN.** Every cell is one ENGINE (the manifest's own row grain). ⛔ `IAM-s-5` and
  `IAM-s-6` are the deliberate two-rows-one-outcome case (`FWD-4`); they are the same grain as each
  other (each an engine), not one nested in the other.
- **(iii) INTENT COHERENCE.** One axis per cell: what this engine must be able to answer. WHY a cell
  is bounded lives in the `bound` column of the manifest and in section 2c, never as a cell state.
- **(iv) STATE COHERENCE -- which values one remedy does NOT move.** Extending `comp-iam-usage` to
  permission grain moves `IAM-s-1` and feeds `IAM-s-3`; it does **not** move `IAM-s-5` (declared-vs-live
  is a different plane entirely), it does **not** move `IAM-s-7` (historical completion is an archival
  read), and it does **not** move `IAM-s-4` (the condition axis is a property of policy TEXT, not of
  usage). **Naming this is only possible because the manifest kept them separate rows.**
- **TOKEN CENSUS (word-boundary), owed with any value-enum proposal:** OWED BY `IAM-s-3` AT PHASE 1,
  not run here. `IAM-s-3` authors the coverage vocabulary (`unused` vs `unobservable` vs the existing
  `UNKNOWN` band) and its census must run against the extended tool's own corpus, which does not exist
  yet. **This decomp records the debt rather than pretending the census exists.**

### 2a. Rule 24 record for the CELL STATUS vocabulary this file AUTHORS

- **(i) MECE over the declared domain** = every cell of this rectangle at any moment. Uncovered member
  hunted and found: *"evaluated, and deliberately not cut this round"* -- which is `CLOSED` **with its
  pointer**, not a seventh value. A terminal status without its pointer is the rot with a tidier label.
- **(ii) SAME GRAIN** -- every value is a property of a CELL, none of a task order or a criterion.
- **(iii) INTENT COHERENCE** -- one axis: how far this cell has travelled. ⛔ `HELD` is on that axis
  (not travelling, with a named owner); WHY it is held is section 2c's job, deliberately not a status
  value, or the axis would carry two intents.
- **(iv) STATE COHERENCE.** Spawning a worker moves `OPEN -> IN-FLIGHT`; it does **not** move `HELD`
  (that needs the named owner to act) and it does **not** move `NOT-EVALUATED` (that needs a
  re-decomposition, a COO act, never a worker's).
- **TOKEN CENSUS (word-boundary):** OWED AT L6 -- the corpus these six names must not collide with is
  the task-order and criteria text that does not exist yet. Recorded as a debt rather than claimed.

---

## 2b. BATTERY DISPOSITION PER LENS -- mandatory core, each RUN or DECLARED-NOT-APPLICABLE

Required by the spine's L5. **All three mandatory lenses were RUN. None is declared not-applicable.**

### `comp-schedule` -- RUN, COMPLETE. Denominators: C1=23 · C2=7 · C3=12 · C4=20 · C5=335

⚠ **THE DEFAULT 90 s BUDGET RETURNS A PREFIX AND SAYS SO** (`scanned 0 of 5 carriers`, C1 partial at
26131 of 33115 files, rc=3). It was re-run at `--budget 500` to completion (`scanned 5 of 5 carriers`,
used 173.8 s, rc=0). **The prefix reported `GATES ARMED: 7`; the complete compile reports 26.**
Quoting the prefix would have understated the armed set by 19.

`GATES ARMED: 26`. **NONE is owned by this project.** The partition:
- `G-1`..`G-7` SENTINEL (C1): INF gold scripts, ETFS_GUARDRAIL schedule gates, black_diamond dispatch.
  Two carry DRIFT CANDIDATE flags, both other lanes'.
- `G-8`..`G-14` DEPLOY-LEDGER (C2): advi-insure, d12-sms, freshguard, and **`G-13`/`G-14` are
  `NFRA_OPSEC202609`'s** (opsec-s10c, opsec-s15). This project is `related` to OPSEC and does **not**
  inherit its open entries.
- `G-15`..`G-26` MORATORIA (C3, 12 standing NEVER clauses): **these bind every project including this
  one.** Four bind specific cells and are carried into section 2c.
- C4 (20 scope_guards) SEMI-DECIDABLE and C5 (335 `blocking` fields, 137 non-null prose) NOT-DECIDABLE
  -- **a reading list, never gates. This decomp does not count them as such.**

### `comp-iam` -- RUN. Denominators: 195 TF roles · 188 services · 1084 operations · 304 gaps

Plus the LIVE plane via `comp-find --corpus aws IAM_ROLE`: **219 nodes, DECLARED=203,
LIVE-no-DECLARED=16, vintage 2026-09-10 03:31:02 UTC.** Both readings and their plane separation are
at sections 1a and 1b. **BLINDNESS STATED:** `comp-iam` emits `wafv2:UNMODELED` and `UNMAPPED-METHOD`
for two services -- it does not model every action namespace, so its 304-gap figure is a floor on the
DESIRED plane, not a population claim. No cell is cut against the gap count.

### `comp-adversary` -- RUN on this file; declaration at section 7

### Non-core lenses -- DECLARED-NOT-APPLICABLE, with reasons

`comp-routes`, `comp-cache`, `comp-transform`, `comp-pipescript`, `comp-blast`: **no cell of this
decomposition touches a route, a cache key, a data prop, a gold script or a deletable resource.** The
project reads IAM policy text and IAM usage telemetry and writes an assessment. ⛔ `comp-blast` becomes
applicable the moment `IAM-s-8` exercises a real narrowing -- it is named as owed AT THAT CELL in
section 2c, not run here against a change that does not exist.

---

## 2c. BOUNDS THE BATTERY ADDED TO CELLS -- carried here, and into the L6 cut

| cell | bound the battery added | lens |
|---|---|---|
| `IAM-s-2` | ⛔ **DO NOT HARDCODE `208`.** The denominator moved 208 -> 216 -> 219 across three vintages while this decomp was being written. The posture number's denominator is a LIVE quantity and must be READ at render time with its vintage printed beside it, never inherited from the brief. | comp-find aws |
| `IAM-s-9` | ⛔ **`G-21` (standing alerting/monitor moratorium) IS ARMED.** A re-run harness that acquires a schedule, an alarm or a notification becomes the thing the moratorium forbids. PRD section 4 already puts minting any alert/alarm/monitor OUT OF SCOPE; this makes the carrier explicit. **Re-runnable by a person on demand is the bar; scheduled is not.** | comp-schedule C3 |
| `IAM-s-8` | ⛔ **`G-17` + `G-23`.** `FWD-5`'s bar is EXERCISED, so a REAL narrowing WILL be applied -- a world-changing act. It opens a change-management entry in `ledger/` BEFORE the act, closes and commits it BEFORE the grading reads, and applies via `safe-apply` (never bare `terraform apply`). `comp-blast` is owed at this cell. | comp-schedule C2/C3 |
| `IAM-s-4` | ⛔ **`G-15` + `C-DESIRED-UNTIL-EXERCISED`.** The condition axis is read from policy TEXT, so every claim it makes is DESIRED until a simulate battery exercises it. PRD bounds it further: that the estate is broadly silent on this axis is an INFERENCE FROM ONE POLICY (brief Part VII item 5), **never a measured population claim.** | comp-schedule C3 |
| `IAM-s-1`, `IAM-s-3` | ⛔ **`C-ANALYZER-PRICED-FIRST` + `G-25`.** AWS Access Analyzer is the FALLBACK and **no per-role price has been read by anyone.** Taking it off the shelf is a VENDOR call requiring Andrew's explicit per-use word. **A cell may not reach for it on the grounds that it is available** -- availability is not authorization. | comp-schedule C3 |
| `IAM-s-1`, `IAM-s-3` | The existing `comp-iam-usage self-test` (9 assertions) is the REGRESSION BAR. An extension to permission grain that leaves any of the 9 red has broken working code, and `blind_is_unknown_NOT_unused` is the one that encodes `FWD-7`. | comp-iam-usage |
| `IAM-s-6` | ⛔ **`C-TWO-REMEDIES`.** Disposes GOVERNANCE only. It may not narrow a permission, and it may not read a permissions finding as a governance answer. The set spans AWS service-default roles and production serving roles (section 1a) and one disposition will not fit all 16. | comp-iam |
| `IAM-s-7` | Landed-or-not on the **ARTIFACT**, never on the plan document's own say-so. ⛔ A closed record is a snapshot, not an oracle -- a plan marked complete is a claim about the day it was written. | comp-adversary |

---

## 3. Placement axis

**Every cell executes on `site-z`** (`project.json` `fabric: site-z`; this lane is on SITEZ, branch
`SITEZ`). **Every cell is `iam` lane** -- the manifest gives all nine rows the same lane, so the
placement axis is DEGENERATE at this cut and is stated rather than omitted, because a later round
adding an `infra` cell would make it load-bearing.

⛔ **The manifest's `lane` column is a LANE, never a seat assignment** -- PRD section 8 says so in
terms. `2.0.0_SA_COO~ZI` seats workers at L6.

---

## 4. Dependency edges, keyed to OBSERVED completion, never to a status word

Read from the manifest's own `depends_on` column, not invented here.

```
  IAM-s-1  <- (none)          IAM-s-4  <- (none)          <-- FOUR INDEPENDENT ROOTS
  IAM-s-5  <- (none)          IAM-s-7  <- (none)

  IAM-s-3  <- IAM-s-1
  IAM-s-6  <- IAM-s-5
  IAM-s-8  <- IAM-s-1, IAM-s-4
  IAM-s-2  <- IAM-s-1, IAM-s-3
  IAM-s-9  <- IAM-s-2, IAM-s-3
```

⭐ **THE MANIFEST'S EDGES YIELD FOUR ROOTS; THE PRD's SEQUENCING PROSE NAMES TWO.** Section 7 says
*"`FWD-4` AND `FWD-6` ARE INDEPENDENT ROOTS and should not idle behind `FWD-2`"* -- naming `IAM-s-5`
and `IAM-s-7`. But `S4` carries `depends_on: --` in the manifest, so **`IAM-s-4` is a fourth root by
the manifest's own data.** This is not a contradiction: the prose named the two most at risk of being
wrongly sequenced, and it is prose. **The edges are the carrier and they say four.** Round 1 is four
cells wide, not two, and reading `FWD-2 IS THE ROOT` as *"nothing else may start"* would idle three
lanes for a round -- the exact failure section 7 warns against, one root further than it counted.

⛔ **`IAM-s-2` CANNOT BE GRADED BEFORE `IAM-s-1` AND `IAM-s-3` BOTH LAND** (PRD section 7: *"Nothing
that quotes a permission-level number can be graded before it"*). The posture number is a rollup of
`IAM-s-1` and nothing else, and its honesty depends on `IAM-s-3`'s coverage vocabulary --
`C-COVERAGE-OVER-COUNT` makes a number that cannot say what it could not see worse than a smaller one
that can.

---

## 5. The arc as rounds

- **ROUND 1 (4 cells):** `IAM-s-1` (the permission-grain instrument -- the critical path),
  `IAM-s-4` (condition axis), `IAM-s-5` (reconciler), `IAM-s-7` (historical completion).
- **ROUND 2 (3 cells):** `IAM-s-3` on `IAM-s-1`; `IAM-s-6` on `IAM-s-5`; `IAM-s-8` on `IAM-s-1`+`IAM-s-4`.
- **ROUND 3 (1 cell):** `IAM-s-2`.
- **ROUND 4 (1 cell):** `IAM-s-9`.

**Max round width 4, inside the default fan-out cap of 8.** ⛔ **`fanout:` data is stated in the L6
issuance commit, DERIVED from these chains, never chosen** -- this section is the input to that
derivation and is not itself the fan-out.

⚠ **THE ROUNDS ARE A READING OF THE EDGES, NOT A SECOND SOURCE OF TRUTH.** If a cell lands early the
next round's cells become cuttable early; the edges govern, the round numbers describe.

---

## 6. `<preflight>` -- what this decomp actually ran, with denominators

| act | instrument | result |
|---|---|---|
| project located on both roots | `ls`, `cat project.json`, `org/projects/NFRA_IAMROLES202609.json` | tree home + generated index, `fabric: site-z`, `dep_stage: PRD` |
| tree/index/register validated | `.tools/missions-tree-index.py check` | **0 violations**; tree=7 projects, 7 valid; DIRECTIVES.yaml 43 entries / 13 directives; MACROS 4 of 4 RATIFIED |
| task orders | `.tools/to-check.py --all --project` | **0** (scanned 2377 faces) |
| surprise channel | `comp-surprise --project` | **0 items, 0 remediation rows** (44 files scanned, both roots) |
| unfinished edits / worktrees | `git status --porcelain` on project paths, `git stash list`, `git worktree list`, `git branch --list 'worktree-*'` | **none / none / no `worktree-*` branch** |
| PRD read in full | `comp-read --for`, then all 404 lines | header + endpoint + section 8 manifest + section 9 grid present |
| lane admission | `.owned-paths.yaml` read at the lane blocks | `decompositions/**` = `TREE_COO`, `project.json` = `TREE_PROJECT_ROW`; **both auto-permit tilde lanes of `2.0.0_SA_COO`** |
| **THE MANDATORY CORE BATTERY IS AT SECTION 2b** | | **all three RUN, none declared not-applicable** |

---

## 7. comp-adversary declaration

Run ON this file; the declaration and its grid are recorded in this file's commit message rather than
inlined, for the same reason the cell-id controls are: **this document is indexed by the L6 coverage
limb, and a grid quoting cell ids in a worked example would mint phantom cells.**

**What the author's evidence context WAS:** the PRD at @076f37eeb2 read in full; the spine at
@d05c382130 read in full; the live AWS graph at vintage 2026-09-10 03:31:02 UTC; `comp-iam-usage`
exercised; `comp-schedule` compiled to completion at `--budget 500`.

**What it was NOT:** ⛔ **this lane did not read the L1 brief.** Every `F<n>` citation in this file is
the PRD's rendering of the brief, not the brief itself -- one instrument, not two. ⛔ It did not
measure member-identity of the 16 against the brief's list (section 1a states this). ⛔ It did not
read the three historical remediation plans `IAM-s-7` will grade. ⛔ The three spine amendments
v3.7/v3.8/v3.9 are LOCAL to the other fabric and reached this lane as RELAY-GRADE prose in msg 20764;
they bind this file by reading and **no line number is cited for any of them.**

---

## 8. What this decomp REFUSES to assume

- **That the 9-and-8 is an invariant.** It is a measurement at this edit; PRD section 8 says so first.
- **That the 16 undeclared roles are the SAME 16 the brief found.** The count held across three
  vintages; member identity is `IAM-s-5`'s to establish, not this lane's to assert.
- **That `195` and `203` describe one population.** Different planes, different instruments (1b).
- **That `absent` means unexamined.** Every `absent` row names what was measured about the current
  state's failure to serve it.
- **That `comp-iam`'s 304 gaps is a population claim.** It carries `UNMODELED` and `UNMAPPED-METHOD`.
- **That the L4 uncovered-member hunt discharges the L5 one.** L4 hunted OWNS-items-without-rows and
  found two. This lane hunted rows-without-cells and found none. **They are different directions and
  neither implies the other.**
- **That any cell is buildable as written.** PRD section 8 disclaims this for `S8` specifically
  (no simulate battery has been run, `D3`). `IAM-s-8` is cut with that named, not hidden.

---

## 9. Holds, and whose they are

**NONE held by this lane. All nine cells are `OPEN` and round 1 is cuttable now.**

- **`C-ANALYZER-PRICED-FIRST` is a CONDITIONAL hold at Andrew, not a standing one.** It arms only if a
  cell reaches for AWS Access Analyzer; the planned path (`EXTEND comp-iam-usage`) does not. Named so
  a worker does not discover it mid-cell.
- **`NFRA_OPSEC202609`'s open deploy-ledger entries (`G-13`, `G-14`) are NOT this project's** and do
  not gate this decomposition, notwithstanding the `related` edge in `project.json`.
- **PUSH STATE: this lane's commits are LOCAL.** `0.0.0_AB_MSTR~Z` holds the push window and opens it
  on Andrew's word only.
