# CANONICAL LOOP REMEDIATIONS -- design + execution record

**Author:** `1.0.0_SA_CTO` · 2026-09-02 · **Status:** DESIGN + PARTIAL EXECUTION. Routed to `3.0.0_SA_CVO`
for adversarial review and adjudication per Andrew-direct.
**Source:** Andrew voice memo, `Transcript Recordings/Canonical flow remediations_4974.txt` (7,774 bytes,
1,423 words, 2026-09-02T12:04:20-04:00), read in full.
**Gating context, his words:** *"before proceeding with any kind of integration, push, or proceeding the
project in general for the ETF guardrails"* -- and site Z does not start until this functions.

⛔ **MORATORIUM CARVE-OUT, THIRD WIDENING, WIDTH STATED SO IT IS NOT INHERITED.** CLAUDE.md bans building
monitors/notifications unless Andrew explicitly asks. **He asked, repeatedly and specifically:** *"they need a
monitor to be able to see those surprises come in"*, *"COO has a monitor"*, *"there needs to be a monitor set
up on those emits. That, like, that, that has to be mechanical."*
**AUTHORIZED:** loop-internal monitors on L4->L5, L7->L8, and L10 routing, plus the gates they imply.
**NOT AUTHORIZED BY THIS:** any monitor on DATA freshness, any SNS/SES/alarm, anything outside the loop.
The ETFS_GUARDRAIL SES carve-out is a separate, narrower grant and is not widened by this one.

---

## 0. What he ruled FINE -- recorded so nobody re-opens it

L2 (endpoint) · L3 (register + fabric) · L4 (PRD/arc) · **the surface manifest** (*"seems to be covered
pretty fairly"*) · L5 in principle · L6 dispatch gate on L3 registry+fabric · L7 worker execution with
`spec_asserts`/`world_is` and its gate. **RELAXED MID-DESIGN (Andrew-direct, verbatim): *"no this is ok, as
long as there is embedded json that is fine."*** -- so the memo's *"I really think all of this stuff should
be JSON... I don't really like markdowns"* is **SATISFIED BY THE EXISTING HYBRID** and there is **no
markdown-to-JSON migration.** Rows already live as fenced JSON blocks parsed by
`.tools/surprise-row-gate.py:89-104`, validated against two real schemas. **R9 CLOSED, NOT BUILT.**

---

## R1 -- "how does comp recon work at L1, at the CRO brief level" · ANSWER: IT DOES NOT EXIST

**Measured, twice, with denominators:**
- `comp-recon` **is not a tool.** Does not resolve bare; `comp-find 'comp-recon' --corpus all` returns
  **5 hits / 144,679 files**, and every hit is a *log line of someone searching for it* (mine, and
  `4.0.0_SA_CRO`'s at 15:46:36Z -- that seat asked the same question independently). **Zero definitions.**
- **L1 invokes NO comp-tool at all.** `comp-read .claude/skills/brief-create/SKILL.md --enumerate 'comp-[a-z]+'`
  -> **0 hits across 144 lines / 32 sections.** The denominator is the point: the file was scanned.

>> **SO L1 IS THE ONLY STEP IN THE LOOP WITH ZERO MECHANICAL GROUNDING, and the brief is the document every
   downstream step traces to.** His instinct (*"L1 is pretty human, I don't think there's anything we can do
   about that"*) is right about the JUDGMENT and understates the exposure: an outcome at L2 must cite a brief
   line, a manifest row must cite an outcome -- **the citation chain bottoms out in a document no instrument
   ever checked.** <<

**RECOMMENDATION (not built -- this is the answer to a question he asked, not a task he set):** the cheapest
non-invasive grounding is a *brief-side* check at L2 rather than a new L1 tool -- `/endpoint --forward`
already reads the brief and could assert that every `SOURCE` line it emits resolves to a real line range.
**That is a proposal. No tool was created, and the honest answer to his question is that the thing he was
asking about has never existed.**

---

## R2 -- the L5 lens battery: `comp-similar` readmission + `comp-adversary` INTO THE SPEC

**His words:** *"comp similar, we had an issue with before... that has since been rectified. So we want to
make sure that that is implemented in an appropriate manner. We also want to make sure that comp adversary is
implemented in an appropriate manner and is included in the spec."*

**Measured state of the battery as specified today** (`SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` s.2.2,
restated in `CANONICAL_FABRIC_WORKFLOW_20260901.md`):

```
  ADMITTED (7)   comp-blast · comp-dataflow · comp-schedule · comp-iam · comp-trigger
                 comp-pipescript · comp-denytest
  REFUSED  (1)   comp-similar -- "emits no vintage and no denominator. Not weak: UNDISCLOSED."
  comp-adversary NOT IN EITHER LIST -- it appears ONLY as a usage BOUND ("expands from CITED paths;
                 a 0-over-0 is an unrun check"). He is right: it is used and unspecified.
```

⛔ **`comp-similar`'s fix is a PRODUCER SELF-REPORT and CLAUDE.md forbids closing on one.**
`0.8.0_AE_CloudComp` reports D1/D2/D3 fixed and exercised @`b8a73cc064`. **That commit is LOCAL, and the
readmission decision belongs to `3.0.0_SA_CVO`, which authored the refusal.** The refusal was on a
DISCLOSURE property (no vintage, no denominator), so readmission is testable against exactly that property.

**PROPOSED SPEC AMENDMENT (for CVO adjudication, NOT self-applied):**
1. **`comp-adversary` -> ADMITTED (8th lens)**, carrying its existing bound as a REQUIRED disposition field:
   every run prints its **CITED-PATH DENOMINATOR**, and `0 uncited siblings over 0 cited paths` is recorded
   as **UNRUN**, never as clean.
2. **`comp-similar` -> ADMITTED (9th) ONLY on CVO re-exercise against the refusal property** -- vintage
   present AND denominator present on its own disposition line. **CVO refused it; CVO readmits it. I am not
   readmitting a lens on the word of the seat that fixed it.**

---

## R3 -- L4 -> L5 mechanization: PRD commit should trigger decomposition

**His words:** *"maybe we start putting PRDs in a dedicated folder, in a dedicated format that is
machine-readable, that COO has a monitor on. And once we effectively commit that PRD, once it's committed,
it's sent to COO immediately for decomposition... we need to discuss the mechanics around that."*

**Measured obstacle, and it is the reason this is not a five-minute build:** PRDs are **not** in a dedicated
folder and **not** machine-readable at the top. `docs/architecture/` holds **D0-D9 directive PRDs, project
PRDs, non-PRD architecture docs and templates in one flat directory.** There is no field a monitor can read
to answer *"is this a step-4 project PRD, and for which project?"* -- the PRD's own identity lives in prose.

**DESIGN -- the smallest thing that works, and it does NOT move any file:**
- **A PRD front-matter block**, one fenced JSON object at the top of a step-4 PRD, schema
  `org/standards/PRD_HEADER.schema.json`: `{project, directive, fabric, prd_version, step, brief_ref,
  endpoint_outcomes:[FWD-n], status}`. **The PRD stays where it is;** the block is what makes it
  machine-readable, which is the property he actually asked for. A dedicated folder is a second way to say
  the same thing and would break every existing citation.
- **The trigger is the COMMIT, not a file-watch.** A post-commit monitor on `docs/architecture/*_PRD.md`
  paths, reading the front-matter block, emitting one line per newly-committed-or-version-bumped PRD.
- ⛔ **DELIBERATELY NOT AN AUTO-DISPATCH.** He said *"it's sent to COO immediately for decomposition."*
  **The monitor NOTIFIES; it does not cut a task order and does not start a decomp.** Rule 27 puts the
  decomp before any TO and the step-6 gate is the only gate; an auto-dispatcher would be a second dispatch
  path that no gate covers. **This is the one place I am narrowing his words, and I am saying so rather than
  quietly implementing the narrow version.**

---

## R4 -- L7 -> L8: full indexing + a monitor on the emits. TWO MEASURED DEFECTS.

**His words:** *"the output of surprise-row-gate.py, is that output, does it include L3 registration and
fabric details? Is it attached to a given project?... it should be a JSON output that has all relevant
identification characteristics so that these can be properly grouped."*

**ANSWER: partly, implicitly, and it BREAKS at the L8->L9 boundary.**

### R4-a -- DEFECT 1 (MEASURED, and it fires the first time site Z raises a surprise)

```
  investigation id pattern   ^[A-Z0-9_]+-(Z-)?S[0-9]+$      accepts PROJ-Z-S1
  remediation   id pattern   ^[A-Z0-9_]+-S[0-9]+$           REFUSES PROJ-Z-S1
  remediation id semantics   "== the graduated investigation item's id"
```
**Exercised on both patterns:** `ETFS_GUARDRAIL-S1` ACCEPT/ACCEPT · **`ETFS_GUARDRAIL-Z-S1` ACCEPT/REFUSE**
· `ADVI_PERFRP-Z-S12` ACCEPT/REFUSE.

>> **A SITE-Z INVESTIGATION ITEM CANNOT GRADUATE INTO A REMEDIATION ROW.** The only ways past it are to drop
   the `Z-` -- **re-introducing precisely the collision the investigation schema exists to prevent** (its own
   description records 7 colliding ids over 14 distinct findings, 2026-08-21) -- or to file nothing. **This
   is the exact class Andrew is holding site Z back for, and it is in the schema today.** <<

**FIX (executed below):** remediation id pattern -> `^[A-Z0-9_]+-(Z-)?S[0-9]+$`.

### R4-b -- DEFECT 2: identity is IMPLICIT, so it is not a field a consumer can reject on

Neither schema carries a `project` or a `fabric` field. **Project is recoverable only by parsing the id
prefix; fabric only by the presence or absence of a `Z-` infix.** CLAUDE.md: *a value must carry its claim in
a field a consumer can reject on.* A monitor that must regex an id to learn which project a row belongs to
cannot reject a malformed one -- it silently mis-groups it.

**FIX (executed below):** add REQUIRED `project` and `fabric` (`laptop` | `site-z`) to both schemas, with the
gate asserting **consistency with the id** rather than replacing it -- two carriers, one quantity, checked
against each other instead of allowed to drift.

### R4-c -- the monitor
`org/surprise_channel/surprise-watch.sh` already exists and is the right shape: a **read-only watermark**
that never mutates what it watches, so an orphan of it cannot steal a row (unlike `inbox-watch.sh`, which
moves before echoing). **Extend, do not rebuild** (build ladder). Emits one line per new row carrying
`project`, `fabric`, `id`, `class`, `hazard_standing` -- which the fields above make possible for the first
time.

---

## R5/R6 -- investigations vs remediations as structure

**Already satisfied in substance and I am not building a second layout.** Per-project folders exist
(`org/surprise_channel/{PROJECT}/`); investigations and remediations are already separate FILES
(`INVESTIGATION_v{n}.md`, `REMEDIATION_v{n}.md`) with separate schemas and a gate that picks the schema by
filename. His *"folders of projects, structured JSON in each"* is the shape that exists, minus the
sub-foldering -- and sub-folders would break every existing path citation for no property gained.
⚠ **One real asymmetry, measured:** **10 project folders hold INVESTIGATION files; exactly ONE holds a
REMEDIATION file.** L9 is barely exercised -- the graduation path has run essentially once, which is worth
knowing before we call the loop deterministic.

---

## R7 -- L10 routing monitors. GOOD NEWS: the tag he asked for ALREADY EXISTS.

**His words:** *"there's like a field somewhere in there where it defines if it's a L6 issue, if it's an L5
issue."*

**It is `loop_target`, enum `[2, 5, 6]`, and it is already gate-enforced.** `.tools/surprise-row-gate.py:159-166`
refuses any row whose `loop_target` contradicts its `route` -- the mapping is LOCKED
(`SPEC_ERROR->6`, `DECOMP_INVALIDATING->5`, `SCOPE_CHANGE->2`). **No new field is needed and inventing one
would create a third carrier of a quantity that already has two checked against each other.**

**DESIGN:** one monitor process, two filters, because the routing already partitions cleanly:
```
  loop_target in (5,6)  -> 2.0.0_SA_COO     re-decompose (5) or re-cut the TO (6)
  loop_target == 2      -> 1.0.0_SA_CTO     endpoint re-alignment -- see R8
```
Per his instruction the L2 arm does not merely notify: **CTO runs a remediation analysis that rolls directly
into `/endpoint --forward` Step F0 re-entry**, which is already built for exactly this arrival
(`outcome_ref` -> read that one outcome, decide WRONG / RIGHT-BUT-INCOMPLETE / OBSOLETE, never re-derive the
whole list). **The skill the L2 arm needs already exists; only the trigger is missing.**

---

## R8 -- QUALIFYING A SCOPE CHANGE. He called this the highest risk. He is right, and there is a HOLE.

**His words:** *"we need a really defined way of qualifying what is a scope change. What are the material or
deterministic aspects of a scope change? Because that is... the highest likelihood of a wrench in the gears."*

### R8-a -- the deterministic ladder (this is the qualification he asked for)

The three routes are ONE axis -- *what does the remedy need that does not exist yet?* -- so the test is a
**containment ladder, asked in order, first hit wins.** Nothing here is a judgment call:

```
  1. Does the remedy fit inside a TASK ORDER THAT EXISTS?          yes -> SPEC_ERROR          -> 6
  2. Else: does it fit a DECOMP CELL THAT EXISTS?                  yes -> (re-cut at 6)       -> 6
  3. Else: does it need a NEW CELL under an outcome the PRD
     ALREADY NAMES?                                               yes -> DECOMP_INVALIDATING -> 5
  4. Else: does it contradict, or require, an OUTCOME?             yes -> SCOPE_CHANGE        -> 2
```
**The material discriminator between 3 and 4 is a single question: DOES THE PRD NAME AN OUTCOME THIS REMEDY
SERVES?** Rungs 1-3 are all "the endpoint is right, the plan under it is wrong." Rung 4 is "the endpoint
itself is wrong." **That is checkable against the PRD's `ENDPOINT` section, which is why that section is
load-bearing machinery and not a summary.**

### R8-b -- ⛔ THE HOLE, CONFIRMED AT SOURCE, AND IT IS THE WRENCH HE PREDICTED

`.tools/surprise-row-gate.py:175-183` **REQUIRES** `outcome_ref` matching `^FWD-[0-9]+$` when
`route=SCOPE_CHANGE`, and `outcome_ref` means *"the PRD outcome id this row CONTRADICTS."*

>> **SO EVERY SCOPE CHANGE MUST NAME AN EXISTING OUTCOME -- AND A SCOPE CHANGE THAT NEEDS AN OUTCOME THE PRD
   NAMES NOWHERE HAS NO LEGAL ROW.** There is nothing to cite. The filer's three options are all bad:
   cite a loosely-related `FWD-n` (**pollutes the one citation the step-2 re-entry depends on**), route it
   `DECOMP_INVALIDATING` (**misroutes an endpoint problem to COO as a decomp problem**), or file nothing.
   **Option 2 is the likeliest, because it is the only one that passes the gate** -- and it is the mirror
   image of the failure the workflow already documents, where scope-change collapses into spec-error.
   **The loop degrades quietly rather than failing loudly, which is the worst available mode.** <<

**This was structurally invisible until now because the SCOPE_CHANGE route has never fired: exactly one
REMEDIATION file exists estate-wide.**

**PROPOSED FIX (for CVO adjudication -- I am NOT self-applying a change to a gate's refusal logic):** permit
the sentinel `outcome_ref: "FWD-NONE"` **only** when `route=SCOPE_CHANGE`, meaning *"the PRD names no outcome
this remedy serves"* -- which is the **UNCOVERED-MEMBER case**, the strongest kind of scope change and
currently the only one that cannot be filed. It arrives at `/endpoint` F0 as *add a new `FWD-n` at the next
unused number* -- a path that skill already specifies. **The sentinel must be distinguishable from a missing
field, which is why it is a value and not an omission.**

---

## EXECUTED IN THIS TURN

1. **R4-a** remediation id pattern accepts the fabric coordinate -- site-Z items can graduate.
2. **R4-b** `project` + `fabric` REQUIRED on both schemas, gate-checked against the id.

## EXECUTION RECORD 2 -- after CVO~A's RED/HOLD @`0d272d257c`: RC1 + RC2 + RC3 landed red-first

**Verdict accepted in full.** P0-1 was this seat's: the schemas *described* a gate check that did not exist
(`comp-read --enumerate 'project|fabric'` on the gate: 1 hit / 258 lines, a comment). Acceptance: msg 92613.

```
  RED    19 controls vs the OLD gate ..... 12 DEFECTS (9 row + 3 mutation)   every named hole present
  GREEN  same 19 vs the NEW gate ......... 0 DEFECTS
  CORPUS 192 rows, HEAD schemas 4 fail / amended 4 fail / delta +0 / new-only 0
```
Harness + RED transcript: `org/tier1_exec/1.0.0_SA_CTO/deliverables/controls/` -- **not** `.tools/tests/`,
because the `TOOL_BATTERIES` lane minted on Andrew's word refuses this seat there (measured). The lane
refusing its own author is the lane working.

| RC | what landed | where |
|---|---|---|
| **1** | full Draft-07 on every new row, fail-CLOSED if `jsonschema` is absent; `project`+`fabric` gate-required and cross-checked against the id | `surprise-row-gate.py _check_row` |
| **2** | `_mutation_violations()`: every HEAD id must be byte-equivalent as data (sha256 over canonical JSON) or present; else MUTATED / DELETED. Same audited override; no second escape | `surprise-row-gate.py`, wired into `check_file` before the new-row loop |
| **3** | `FWD-NONE` rejected by name; `scope_change_kind` in {CONTRADICTS_NAMED_OUTCOME -> real `FWD-n`, REQUIRES_UNNAMED_OUTCOME -> `outcome_ref` key present with `null` + `proposed_outcome`} | gate + `remediation_row.schema.json` |

⛔ **THE VALIDATOR FOUND A BUG IN ITS OWN SCHEMA.** After RC1 the three remediation *positive* controls refused:
`/remediation/state -- 'REMEDIATED' was expected`. Both `allOf` conditionals key on `closed: true` but listed
only `hazard_standing` as required; Draft-07 `properties` constrains only *present* keys, so a row with **no
`closed` key vacuously matched** and every OPEN row was forced to REMEDIATED. **Latent for the schema's whole
life because the old gate never ran `allOf`.** Fixed by adding `closed` to both `required` lists -- a
precondition repair, not a new value or axis; disclosed to CVO as Rule 24 owner. **The corpus holds exactly
ONE remediation row estate-wide, so this harness is the only exercise those conditionals get.**

⚠ **Two self-inflicted instrument failures during this work, kept because they are the transferable half:**
(1) my "all six surfaces unclaimed" used my own fnmatch instead of the validator -- three were CVO_WORKSPACE /
ANY_EXEC; (2) a wording edit to `.owned-paths.yaml` inserted `lane: ANY` into a plain scalar and **broke the
ownership map** for ~2 minutes, with no fail-closed restore on that script. Restored from HEAD, mint verified
intact (5 REFUSE rows), re-applied with no colon and a restore path. **A file that gates every commit in the
fabric gets a fail-closed writer every time, not just the first time.**

**Still open under the hold:** RC4 (standing corpus validator, exact-tuple baseline), RC5 (CloudComp's battery
repair -- the fabric-wide step-6 critical path), RC6 (admitted catalog vs mandatory core), RC7 (delivery-ACK
tests for the monitors, gated on RC1/RC2 -- now met).

## NOT EXECUTED, AND WHY -- routed to `3.0.0_SA_CVO`

- **R2 readmissions** -- CVO authored the `comp-similar` refusal; CVO lifts it. Readmitting a lens on the
  word of the seat that fixed it is a producer self-report.
- **R8-b sentinel** -- it changes what a GATE REFUSES. That is exactly the class of change that wants an
  adversary before it lands, not after.
- **R3/R4-c/R7 monitors** -- specified above, deliberately unbuilt pending adjudication. **Building three
  monitors against a design nobody has attacked is how you get three monitors measuring the wrong thing
  precisely.** The moratorium carve-out authorizes them; it does not make them correct.

---

## EXECUTION RECORD -- R4-a and R4-b, with the baseline that proves them safe

### What landed

| | |
|---|---|
| **R4-a** | `remediation_row.schema.json` id pattern `^[A-Z0-9_]+-S[0-9]+$` -> `^[A-Z0-9_]+-(Z-)?S[0-9]+$` |
| **R4-b** | `project` + `fabric` added to BOTH schemas |

⛔ **CORRECTION TO THIS DESIGN'S OWN R4-b, MADE BEFORE IMPLEMENTING IT.** The section above says add them
as **REQUIRED**. **That would have been wrong and I did not do it.** Both schemas set
`additionalProperties: false` and ~190 rows predate these fields; a schema-level `required` would refuse
**every future append to every existing file.** The estate already has the right precedent for exactly this
-- `spec_asserts`/`world_is` are **optional in the schema and gate-required on NEW rows only**, under
Andrew-direct 2026-09-01 (*"this is a relatively new system... maintain now and prospectively"*). The new
fields follow it. **The design was edited by contact with the artifact rather than the artifact by the design.**

### Exercised, both directions, with negative controls

```
  R4-a   ETFS_GUARDRAIL-Z-S1   investigation ACCEPT · remediation ACCEPT   (was ACCEPT / REFUSE)
         ADVI_PERFRP-Z-S12     investigation ACCEPT · remediation ACCEPT
  NEGATIVE CONTROLS, all REFUSE on both patterns -- so the widened pattern did not go slack:
         etfs-S1 · ETFS_GUARDRAIL-Y-S1 · ETFS_GUARDRAIL-S · -S1
```

### Backward compatibility PROVEN AGAINST A BASELINE, not asserted

The amendment is *strictly permissive* (a widened pattern; two optional properties), so it **cannot**
introduce a failure -- but "cannot" is an argument, not a measurement. Ran every fenced row in the channel
against the schemas at `HEAD` and against the amended ones:

```
  BASELINE (schemas @HEAD)    rows=192   failures=4
  AMENDED  (worktree)         rows=192   failures=4
  DELTA                                  +0        rows failing ONLY under the amendment: 0
```

⚠ **MY FIRST RUN OF THIS TEST REPORTED 23 FAILURES AND THE TEST WAS WRONG, NOT THE SCHEMA.** It picked the
schema from the **full path**, so the project `MDPF_COTREMEDIATION` matched `"REMEDIATION"` and 19
*investigation* rows were graded against the *remediation* schema. The real gate uses **basename**
(`surprise-row-gate.py:114`). **A wrong-object error inside the very check written to prove a wrong-object
fix** -- and the tell was the failure text (`'mechanism' is a required property` on an investigation row),
which names a field that only exists in the other schema. **Recorded rather than quietly re-run.**

---

## TWO FINDINGS THE BASELINE SURFACED -- neither is in the memo, both bear on "deterministic"

### F1 -- 4 of 192 channel rows DO NOT VALIDATE, and nothing in the loop can see it

```
  D1_CATVIEWS-S8         disposition = "FALSIFIED BY EVENTS -- plausible when written..."   not in enum
  ETFS_INGEST-Z-S37      disposition = "RETIRED -- NOT FIXED, and the record should say..." not in enum
  ETFS_POSITIONING-S14   disposition = "DISARMED -- FALSIFIED BY EVENTS..."                 not in enum
  POSN_TENANCY-S3        surfaced_at = "2026-08-27T21:2xZ"                                  fails pattern
```

>> **THE GATE IS PROSPECTIVE-ONLY BY DESIGN -- it validates rows NEW IN THE COMMIT.** That was the right
   call for adoption. **The consequence nobody has stated is that the channel's EXISTING contents are
   unvalidated and no instrument reports on them.** There is no full-corpus pass, so the true answer to
   *"does the surprise channel conform to its own schemas?"* has been UNKNOWN, not YES. Cost of knowing:
   one script, ~2 s, run above. <<

### F2 -- the `disposition` enum is NOT MECE over its own domain (Rule 24 postulate i)

```
  DECLARED DOMAIN   UNDER_INVESTIGATION · GRADUATED · DISMISSED_WITH_REASON · DECOMP_INVALIDATING
  UNCOVERED MEMBER  an item THE WORLD OVERTOOK -- not graduated, not dismissed-with-reason,
                    not still under investigation. Plausible when written; falsified by events.
```

**Three seats, on three different projects, independently wrote PROSE INTO AN ENUM FIELD rather than pick a
value that was wrong.** That is the honest failure and it is the tell: **when several independent authors
all break a field the same way, the field is missing a value, not the authors discipline.** It is also the
`verdict-vocabulary-with-no-NOT-EVALUATED-value` class -- a vocabulary that cannot say *"overtaken"* forces
that state to be encoded as one of the states it is not.

⛔ **NOT SELF-APPLIED.** Adding an enum value is a Rule 24 authoring act requiring the four-postulate record
and a word-boundary token census. **Proposed to `3.0.0_SA_CVO~A`, not landed by me.** Two candidate shapes,
and the choice is not obvious: a fifth `disposition` value (e.g. `OVERTAKEN_BY_EVENTS`), or a separate
`outcome_of_record` axis -- because *"falsified by events"* and *"retired, not fixed"* may be two members,
and postulate (iii) says one axis, one intent.

---

## HANDOFF -- `3.0.0_SA_CVO~A` (base CVO is on Andrew's direct demands)

**ADJUDICATE:** R2 lens readmissions · R8-b the `FWD-NONE` sentinel (it changes what a gate REFUSES) ·
F2 the enum gap (Rule 24) · and whether F1 warrants a full-corpus validation pass as a standing act.
**REVIEW ADVERSARIALLY:** R8-a's containment ladder -- it is the piece Andrew called highest-risk, it is
the piece with no mechanism behind it yet, and it is the one I would most expect to be wrong.
