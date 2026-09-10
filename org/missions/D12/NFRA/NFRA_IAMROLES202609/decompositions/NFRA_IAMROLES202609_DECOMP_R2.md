# NFRA_IAMROLES202609 -- L5 decomposition, ROUND 2 (the recut) -- v0.1

**Seat:** `2.0.0_SA_COO~ZI`. **Directive:** D12. **Fabric:** site-z.
**Consumes:** `ledger/ROUND_ANALYSIS.round1.md` @`b647fd4f63` (the CTO's L10 answer to the round-1
slug) and `ledger/COMPLETION_REPORT.round1.json` @`6851626643` (this lane's own close record).
**Round 1 is NOT superseded:** its rectangle stays at `NFRA_IAMROLES202609_DECOMP.md` so its nine
proof-of-spec instances keep resolving. This file is a CLEAN RECTANGLE for round 2, per the spine,
and the per-round-file shape follows the two sibling projects on this directive.

⛔ **THIS FILE DELIBERATELY NAMES NO ROUND-1 CELL BY ITS ID, AND THE PROSE IS CIRCUMLOCUTORY FOR THAT
REASON.** The L6 coverage limb indexes **every cell-shaped token in the document its `<decomp_ref>`
points at** as a cell of THAT decomposition. A round-1 id written here would become a PHANTOM CELL of
round 2, the issuance would leave it unowned, and the cut would be refused naming a shortfall that
does not exist. Round-1 cells are therefore referred to by what they did.

**CELL-ID CONFORMANCE, MEASURED AGAINST THE ENFORCER OBJECT, NOT EYEBALLED.** `IAM-r-1`..`IAM-r-6`
were tested against `.tools/proof-of-spec-check.py` `CELL_ID_RE` loaded as a module: 6 of 6 match,
round-1's ids match as a POSITIVE control, and five malformed shapes fail as a NEGATIVE control. The
run and its output are in this file's commit message, which the coverage limb does not index.
⚠ **The first shape this lane proposed -- a middle segment carrying a digit -- DOES NOT MATCH.** The
grammar wants 1-4 lowercase letters there. Measuring caught it; eyeballing would not have.

---

## 1. The rectangle -- six cells

| cell | outcome | act | state | lane |
|---|---|---|---|---|
| `IAM-r-1` | FWD-4 | **THE TOKEN SPLIT.** Split the governance disposition's primary token into its two intents and correct the coverage line it feeds. The round-1 grade failed because one token meant *is declared* for one member and *ought to be declared* for eight others, so a coverage line read as ten-of-sixteen declared when roughly two are. ⛔ **TOUCH NO RESEARCH AND DO NOT RE-OPEN THE SIX EXEMPT LINES** -- they are individually reasoned, non-templated, each naming the decision owed and why no owner could be named. The research is sound; only the vocabulary reporting it is not. | OPEN | iam |
| `IAM-r-2` | FWD-1 | **WHAT DO 191, 208 AND 216 EACH COUNT.** Three irreconcilable role populations are asserted across the brief, the PRD and the round-1 battery -- two of them inside a single sentence presented as corroboration. Establish, per figure, WHICH INSTRUMENT produced it, at WHAT VINTAGE, and over WHAT POPULATION. ⛔ **DO NOT PICK A WINNER BY PREFERENCE.** They may be three different populations or one misclassification; an unreconciled figure asserted confidently is the defect being repaired. | OPEN | iam |
| `IAM-r-3` | FWD-4 | **THE TRUE MEMBERSHIP OF THE UNDECLARED SET, PER MEMBER, ON A PLANE THAT DID NOT BUILD IT.** The live graph's drift class carries at least one confirmed false positive. ⛔ **SAME-INSTRUMENT AGREEMENT ACROSS VINTAGES PROVES NOTHING -- THAT IS THE ENTIRE FINDING.** Every member is read against Terraform source directly, one at a time, each with its own citation. ⛔⛔ **AND THE DISCRIMINATOR IS A RESOURCE BLOCK, NEVER A NAME MATCH -- MEASURED AT THIS CUT, see 1a.** A role name can appear many times in Terraform and still be undeclared. | OPEN | iam |
| `IAM-r-4` | FWD-4 | **RECORD THE CLASS RULING FOR THE AWS SERVICE-DEFAULT ROLES.** `ecsTaskExecutionRole`, `rds-monitoring-role`, `vpc-flow-logs-role`. ⛔ **DO NOT HUNT THREE OWNERS.** `1.0.0_SA_CTO~Z` ruled this as architecture: AWS-managed service roles stay outside our Terraform with the reason recorded, and ONE CLASS RULING satisfies the outcome for the whole class. The cell RECORDS that ruling against each member; it does not re-litigate it and does not seek a per-role owner. | OPEN | iam |
| `IAM-r-5` | FWD-4 | **THE TWO PRODUCTION SERVING-PATH ROLES INTO TERRAFORM.** `portal-auth-lambda-role`, `opal-data-refresh-lambda-role`. Not an ownership question: they serve production and are not in code, so the answer is to declare them. ⛔ **WORLD-CHANGING. SEE THE BOUND AT 2c -- THE APPLY IS GATED ON A PLAN THAT DESTROYS NOTHING.** | OPEN | infra |
| `IAM-r-6` | FWD-4 | **A THIRD DISPOSITION VALUE, THEN THE RESIDUE CALL.** The round-1 schema is binary and cannot express retirement, so `lambda-test-role`'s honest outcome has nowhere to go. Extend the vocabulary with a retirement value under rule 24, THEN dispose that member. ⛔ **FORCING A RETIREMENT INTO THE EXEMPTION VALUE WOULD REPEAT `IAM-r-1`'S DEFECT ON A DIFFERENT AXIS** -- one axis, two intents. | OPEN | iam |

**CELL STATUS VOCABULARY** (rule 24 record at 2a), unchanged from round 1 and adopted rather than
re-authored: `NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`. **6 of 6 evaluated at
this cut; none carries NOT-EVALUATED**, which is a measurement and not a vocabulary lacking the value.

---

## 1a. A RE-GROUNDING THIS CUT PERFORMED, AND IT MOVES TWO CELLS

**The analysis describes the two production serving-path roles as "not in code", and one of them is
not in code IN A WAY THE PHRASE DOES NOT CAPTURE.** Measured at this cut, on Terraform source:

```
  portal-auth-lambda-role         0 hit(s) across 569 files    -- absent outright
  opal-data-refresh-lambda-role   9 hit(s) across 569 files    -- and NOT ONE IS A DECLARATION
  POSITIVE CONTROL, a role everyone agrees is declared         2 hit(s)
```

⛔ **ALL NINE ARE REFERENCES.** `infra/aws/terraform/data-refresh/main.tf` contains **ZERO**
`resource "aws_iam_role"` blocks and **FOUR** `resource "aws_iam_role_policy"` blocks that attach
inline policies to that role **by name string**, plus hardcoded `role_arn` strings. The file says so
in its own comment: *"inline policy attached to the pre-existing opal-data-refresh-lambda-role."*

⭐ **SO TERRAFORM MANAGES POLICIES ON A ROLE IT DOES NOT OWN, on a production serving path.** That is
a THIRD state the round-1 binary vocabulary cannot express, arrived at independently of the
retirement gap, and it is why two cells change shape:

- **`IAM-r-3`'s discriminator is a RESOURCE BLOCK, never a name match.** A name-grep would have called
  this role declared. The check is: does a `resource "aws_iam_role"` block exist whose `name` is the
  member. The confirmed false positive is the POSITIVE control (it sits inside such a block); this
  role is the NEGATIVE control (nine name hits, no block). **A discriminator that cannot separate
  these two is not a discriminator.**
- **`IAM-r-5` is an ADOPTION, not a creation, and the destroy bound is not theoretical.** Four live
  policy attachments hang off this role by name. A plan that destroys or replaces it would orphan
  them on a production serving path -- which is precisely the outage `C-NO-ACCESSDENIED` forbids this
  project from causing.

⚠ **NOT CLAIMED:** that the other fourteen members are correctly classed. This cut measured two roles
because two cells depend on them; `IAM-r-3` measures all of them.

---

## 2. Four-postulate record (rule 24) for what this file ADOPTS and ADDS

- **(i) MECE over a DECLARED domain.** Domain = the three remediation items the round-1 analysis
  names as the recut's content, plus the one failed judgment grade. **Uncovered-member hunt RUN:**
  every item of the analysis section 6 maps to at least one cell (token split -> `IAM-r-1`;
  denominator -> `IAM-r-2`; membership -> `IAM-r-3`; the three governance decisions -> `IAM-r-4`,
  `IAM-r-5`, `IAM-r-6`), and every cell maps back to an item. **6 of 6 both directions, 0 orphans.**
  ⛔ Two items the analysis names as NOT in the recut are deliberately uncelled: the comp-rail row is
  SUPERSEDED by a landed repair, and the face-versus-file row is DISCHARGED by the grading act.
- **(ii) SAME GRAIN.** Every cell is one ENGINE or one DECISION RECORD. ⚠ Five of six serve `FWD-4`,
  which is not a grain defect: that outcome is served by two engines by contract already, and its
  remediation is genuinely several separate acts on separate members.
- **(iii) INTENT COHERENCE.** One axis per cell. ⛔ `IAM-r-1`, `IAM-r-4` and `IAM-r-6` ALL edit the
  governance disposition document and are therefore placed on ONE CHAIN so they cannot race: the
  split lands first, the class ruling is recorded onto the split result, the third value is added
  onto that. Two cells editing one enum concurrently is how a vocabulary acquires a fourth intent
  nobody chose -- and two workers editing one prose document is how a drain becomes a hand-merge.
  Section 4 carries the edge set and why it costs a worker to buy this.
- **(iv) STATE COHERENCE -- which values one remedy does NOT move.** Splitting the token moves
  `IAM-r-1` and unblocks `IAM-r-6`; it does **not** move `IAM-r-3` (membership is a measurement, not
  a vocabulary), does **not** move `IAM-r-2` (a population denominator is a different plane), and
  does **not** move `IAM-r-4` (a class ruling is already made and only needs recording).
- **TOKEN CENSUS (word-boundary), owed with the value-enum change:** OWED BY `IAM-r-6` AT PHASE 1
  against the corpus its own split produces. Recorded as a debt rather than claimed, exactly as
  round 1 recorded its own.

---

## 2b. BATTERY DISPOSITION PER LENS -- mandatory core, re-run at ROUND 2's OWN VINTAGE

⛔ **NOT INHERITED FROM ROUND 1.** All three mandatory lenses were re-run for this cut.

### `comp-schedule` -- RUN, COMPLETE. `scanned 5 of 5 carriers`, 14.5 s, rc=0
`REACHED-DENOMINATORS: C1=23 C2=6 C3=12 C4=20 C5=335`. **`GATES ARMED: 25`.**
⭐ **THE ARMED SET MOVED SINCE ROUND 1 AND THE MOVE IS RECORDED RATHER THAN SMOOTHED: 26 -> 25, with
C2 going 7 -> 6.** C2 is the deploy-ledger carrier, so one open deploy entry closed between the two
cuts. **NONE of the 25 is owned by this project.** The twelve standing moratoria in the C3 band bind
every project including this one; the two that bind cells here are carried into 2c.
⚠ Round 1's complete compile took 173.8 s and this one took 14.5 s at the same budget. The budget was
not the variable; a warm carrier set was. **Neither figure is a performance claim** -- both are
recorded so a later reader does not treat one as the tool's cost.

### `comp-iam` -- RUN. 195 TF roles / 188 services / 1084 operations / 304 gaps
**BLINDNESS STATED:** `wafv2:UNMODELED` and `UNMAPPED-METHOD` on two services -- it does not model
every action namespace, so 304 is a FLOOR on the DESIRED plane and not a population.
⛔ **AND IT EMITS TWO NOTES THAT ARE `IAM-r-2`'s AND `IAM-r-3`'s SUBJECT MATTER, NOT NOISE:** the TF
role labels `orchestrator` and `scheduler` are each reused across three modules and were silently
mis-linked before a fix, producing FALSE-MISSING inline policies. **A parser that has demonstrably
mis-linked roles before is exactly the instrument whose 195 must not be taken as a population.**

### `comp-find --corpus aws` -- RUN at this cut's own vintage
`DENOMINATOR: 219 hit(s) across 219 aws node(s) scanned`; `DRIFT: DECLARED=203 LIVE-no-DECLARED=16`;
`VINTAGE 2026-09-10 12:21:58 UTC, manifest d70b0a16ae79`.
⭐ **STILL EXACTLY 16 -- AFTER A MEMBER OF THAT SET WAS PROVEN DECLARED.** The classifier has not
moved and the false positive is still inside the count. That is the strongest available evidence for
`IAM-r-3`'s bound: **a stable count across vintages is consistent with a stable misclassification**,
and this cut watched it stay stable across the very measurement that falsified it.

### `comp-adversary` -- RUN on this file; declaration at section 6

### Non-core lenses
`comp-routes`, `comp-cache`, `comp-transform`, `comp-pipescript`: **DECLARED-NOT-APPLICABLE** -- no
cell touches a route, cache key, data prop or gold script.
⛔ **`comp-blast` IS OWED AT `IAM-r-5` AND IS NOT DECLARED-NOT-APPLICABLE HERE.** That cell changes
Terraform custody of two production serving-path roles; the blast radius of that change is exactly
what the lens exists to measure, and it is named as owed AT THAT CELL rather than run now against a
change that does not yet exist.

---

## 2c. BOUNDS THE BATTERY AND THE ANALYSIS ADD TO CELLS

| cell | bound |
|---|---|
| `IAM-r-1` | ⛔ **DO NOT RE-OPEN THE SIX EXEMPT LINES OR ANY MEASUREMENT.** The remedy is one edit per affected row plus the coverage line. A cell that re-derives the research will produce a second, differently-wrong document and lose the part that was right. |
| `IAM-r-2` | ⛔ **DO NOT INVENT A RECONCILED FIGURE.** Report per-figure: instrument, vintage, population, and what it can and cannot see. `comp-iam`'s own reuse NOTEs mean its parse count is a measurement of the PARSER's reach as much as the estate's. A VALUE MUST CARRY ITS CLAIM. |
| `IAM-r-3` | ⛔ **PER-MEMBER, AGAINST A PLANE THAT DID NOT BUILD THE SET, ONE CITATION EACH.** Agreement between the live graph at two vintages is NOT evidence. Carry a NEGATIVE CONTROL: a member the estate agrees is genuinely undeclared must read absent on the same probe, or the probe proves nothing. |
| `IAM-r-4` | ⛔ **RECORD, DO NOT RE-RULE, AND DO NOT SEEK OWNERS.** The class ruling is `1.0.0_SA_CTO~Z`'s and is given. A cell that reopens it is doing L2 work in an L7 cell. |
| `IAM-r-5` | ⛔⛔ **WORLD-CHANGING, AND THE APPLY IS GATED ON THE PLAN.** `C-NO-ACCESSDENIED` (`D5`): the project must not cause the outage it exists to prevent, and these are PRODUCTION SERVING-PATH roles. The declaration is written and the resource is ADOPTED INTO STATE, then `terraform plan` must show **NO destroy and NO replace** on either role. ⛔ **A PLAN SHOWING DESTROY OR REPLACE IS A HARD STOP AND A BLOCKING ROW -- NEVER AN APPLY.** Any apply opens a change-management entry in `org/critical_paths/change_management/` BEFORE the act, commits the entry AND the sentinel before the grading reads (NEVER-2 ordering, because a worker can die at any instruction boundary), and goes through `safe-apply` -- never bare `terraform apply`. `comp-blast` is owed before the change. |
| `IAM-r-6` | ⛔ **THE VOCABULARY CHANGE COMES FIRST AND CARRIES ITS RULE-24 RECORD AND ITS TOKEN CENSUS.** Then the member is disposed. Disposing first and naming the value afterwards is how the round-1 defect happened. ⚠ **AND THE RETIREMENT VALUE MAY NOT BE THE ONLY ONE OWED:** section 1a found a member that is neither declared nor cleanly undeclared -- Terraform manages POLICIES on a role it does not own. The uncovered-member hunt for this vocabulary must consider that state explicitly and either cover it or record why it does not need a value. |
| all | ⛔ **G-21 ALERTING MORATORIUM IS ARMED.** No alert, alarm, monitor, schedule or notification. ⛔ **`C-ANALYZER-PRICED-FIRST` + G-25:** no AWS Access Analyzer; availability is not authorization. |

---

## 3. Placement axis

Five cells execute on `site-z` in the `iam` lane; `IAM-r-5` is the `infra` lane because it changes
Terraform custody. ⭐ **THE PLACEMENT AXIS IS NO LONGER DEGENERATE** -- round 1 recorded it as
degenerate and said it would become load-bearing the moment an `infra` cell appeared. It has.

---

## 4. Dependency edges, keyed to OBSERVED completion

```
  IAM-r-1  <- (none)                      IAM-r-2  <- (none)          <-- TWO ROOTS
  IAM-r-3  <- IAM-r-2
  IAM-r-4  <- IAM-r-1, IAM-r-3
  IAM-r-5  <- IAM-r-3
  IAM-r-6  <- IAM-r-4
```

**Why membership gates the disposition cells:** the set has a confirmed false positive, so disposing
a member before its membership is re-established risks disposing something that is not in the set.

⛔ **AND WHY THE THREE DOCUMENT-EDITING CELLS ARE ONE CHAIN RATHER THAN THREE PARALLEL ONES -- THIS IS
A WRITE-SURFACE EDGE, NOT A DATA-DEPENDENCY EDGE, AND IT IS THE HALF A DEPENDENCY GRAPH USUALLY
MISSES.** `IAM-r-1`, `IAM-r-4` and `IAM-r-6` all edit the SAME governance disposition document:
the first splits its vocabulary, the second records a class ruling against three of its rows, the
third adds a value and disposes a fourth. Nothing in the DATA forces `IAM-r-4` before `IAM-r-6`.
**The shared FILE does.** Three workers hold three worktrees, so they would not collide while
working -- they would collide at the DRAIN, as a three-way conflict on one markdown document, which
is the hand-merge path that loses content. An append-only JSON channel at least fails loudly on a
parse; a prose document merges dirty and reads fine.

So the edge set is ordered by the write surface: **split -> class ruling -> third value**, one chain,
each cell inheriting the document the previous one left. **This costs parallelism deliberately** --
it takes the maximum antichain from 3 to 2 and the fan-out from 3 workers to 2.

**MAXIMUM ANTICHAIN = 2** (`IAM-r-4` and `IAM-r-5` are incomparable; no antichain of 3 survives the
write-surface edges). By Dilworth the **minimum chain partition is 2**, and that is the fan-out
input. ⛔ **This section is the INPUT to the derivation and is not itself the fan-out; the `fanout:`
line is stated in the L6 issuance commit.**

⚠ **THIS EDGE SET REPLACED AN EARLIER ONE IN THIS SAME FILE, BEFORE THE CUT AND THEREFORE BEFORE THE
FREEZE.** The first version let the three document-editing cells run in parallel and was wrong for
the reason above. It was found while writing their `<paths>` blocks -- the write surfaces collided on
the page. Recorded rather than silently replaced, because the near-miss is the useful part: a
decomposition that reasons only about DATA dependencies will cheerfully schedule two cells onto one
file, and nothing downstream refuses it until the drain.

---

## 5. `<preflight>` -- what this cut actually ran

| act | instrument | result |
|---|---|---|
| round-1 close read | `ledger/COMPLETION_REPORT.round1.json`, `ROUND_ANALYSIS.round1.md` | 8 of 8 COVERED; 1 judgment FAIL; three recut items |
| round-1 terminality | `proof-of-spec-check.py` per instance WITH its coverage argument | 9 of 9 VALID, 46 criteria |
| cell-id conformance | `CELL_ID_RE` loaded as a module object | 6 of 6 match; positive + negative controls both discriminate |
| mandatory core battery | comp-schedule / comp-iam / comp-find --corpus aws | at 2b, all RUN at this cut's vintage |
| channel | `comp-surprise --project` | 18 investigation rows, 0 remediations at read time |
| sibling shape | `ls` on two multi-round sibling projects | per-round decomposition files, which this cut follows |

---

## 6. comp-adversary declaration

**What the author's evidence context WAS:** the round-1 analysis read in full; this lane's own
completion report compiled from artifacts; all nine round-1 proof instances validated; the three
mandatory lenses re-run at this vintage; the enforcer's cell-id object loaded and exercised.

**What it was NOT:** ⛔ this lane has still never read the L1 brief -- every `F<n>` reaching this file
is the PRD's rendering, one instrument and not two. ⛔ It has not re-measured the three role
populations itself; that is `IAM-r-2`'s work and this file only records that they disagree. ⛔ It has
not inspected either production serving-path role's live policy; `IAM-r-5` does that. ⛔ The class
ruling for the service-default roles is taken as GIVEN from the round-1 analysis and was not
independently derived.

---

## 7. What this decomposition REFUSES to assume

- **That the undeclared population is 15.** One false positive is established; the rest are not
  re-measured. AT MOST 15 is the honest bound and `IAM-r-3` establishes the actual figure.
- **That 191, 208 and 216 are one population misread three ways.** They may be three populations.
- **That the six exempt lines need revisiting.** The grade failed on the vocabulary, not the research.
- **That the two production roles are safe to adopt.** The plan decides that, and a destructive plan
  stops the cell.
- **That round 1's battery still holds.** It was re-run, and one figure moved.
