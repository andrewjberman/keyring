# L1 BRIEF -- every broken name gets a complete fix: closing the blanks in the naming check's list

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07. **Mode:** NEW (greenfield project; no code exists).
**Commissioned by:** `1.0.0_SA_CTO` msg 106101, under Andrew-direct 2026-10-07 ~08:0xZ, VERBATIM: "Yes any new project
concept has to go through full /canonical-flow." (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_080xZ_ANY_NEW_PROJECT_CONCEPT_GOES_THROUGH_FULL_CANONICAL_FLOW.md`).
**Consumer:** `/endpoint --forward` at L2 (`1.0.0_SA_CTO`).

**Read this first.** The commission describes a residual of 1,298 rows. That figure was measured on 2026-09-19 and is no
longer the population. Measured today (Part VI): **537 rows, 242 distinct names**. Andrew's registry pass of 2026-09-21
removed most of the `{system}` rows, and three of his rulings from that day still wait on a build. The outcomes below are
cut for the population that exists today, not the one in the register.

Terms used throughout:
- **The check**: `python lib/opal_naming.py census --live --repo`, the whole-estate naming check built by LGIC_ENFORCE
  (the Platform Logic enforcement project, directive D14).
- **A blank**: a fix the check prints with a hole in it, such as `{system}-access-anomaly-scanner-lambda` or
  `advi-49f-gold-floor-{cadence}`. The check knows the name is wrong and cannot say what the right name is.
- **FWD-5**: LGIC_ENFORCE's fifth outcome, "anyone can run the check over the whole estate and get the complete ranked
  list of names and addresses that break the pattern, each with its fix". It is the one outcome of seven not realized.

---

## PART I -- THE OUTCOME TERRITORY

### I.0 The candidate thread (becomes FWD-1; round 1 builds it end to end)

**Who:** an engineer about to clean up one Terraform root (a Terraform root is one folder of infrastructure definitions).
**Journey, coarse grain:** the engineer runs the check on ONE root (`infra/aws/terraform/bd-pipeline/`, the Black
Diamond pipeline for 49 Financial), with no preparation, and reads one line per name. Every line is one of three things:
the name is right; the name is wrong and here is the complete correct name; this kind of name is not asked to carry the
part that is missing, and here is why. No line contains a blank. The engineer can act on every line without asking
anyone.

`bd-pipeline` is proposed because today's blanks include firm-led names and inline policy names that belong to it
(`bd-pipeline-task-role`, `BDPipelinePermissions`, `/ecs/bd-pipeline`). Whether it also holds a schedule with no
cadence word and a storage key with no source was not measured; if it does not, L2 should pick a root that holds all
four groups of finding F2.

### O1 -- A person reading the list can act on every row

Someone who runs the check over the whole estate reads a list in which no fix contains a blank. Each wrong name is paired
with the complete name it should have.

### O2 -- A person is told when a name is not asked to carry a system

Someone looking at an inline policy name (`CloudWatchLogs`, `S3Access`), a name led by an AWS service word
(`s3-...`, `cloudwatch-...`, `invoke-...`) or a library layer (`pandas-pyarrow-layer`) is told plainly that this kind
of name carries no business system. They are not told "broken, fix unknown". This is Andrew's ruling 3 and CALL 3 of
2026-09-21 made visible to the reader (Part IV, finding F3).

### O3 -- A person renaming a schedule or a storage key reads the whole target name

Someone renaming a schedule reads its target name with the cadence word filled in. Someone moving a storage key reads its
target address with the source and the firm filled in. They look nothing up.

### O4 -- Anyone can run the check to the end without preparing it

Someone runs the check on a clean checkout and it finishes. They do not first have to write a list of names for the check
to skip. Today the run stops twelve times (finding F5).

### O5 -- The person who creates an unplaceable name learns it when they create it

A seat that adds a resource whose name the check cannot place is told at that moment, with the registry row it owes. The
list of unplaceable names does not grow between one run of the check and the next.

### O6 -- The registry owner states where a resource belongs once per folder, not once per resource

The owner of the registry records "everything in this Terraform root belongs to this system" in one small map, and writes
a row by hand only for a genuine exception. This is Andrew's ruling "b" of 2026-09-21 (finding F4).

### O7 -- A reader never sees a code template presented as a resource name

Someone reading the list does not meet `bronze/positions/{snap}.parquet` as if it were a broken name, and does not meet
`orion/rate_limit_state_{dim_name}.json` graded as correct. A template in source code is shown as a template.

### O8 -- The Chief Technology Officer can read FWD-5 as realized from one run

`1.0.0_SA_CTO` runs the check once, reads its totals, and LGIC_ENFORCE reads 7 of 7 outcomes realized. Nothing about that
reading depends on a figure carried from an earlier report.

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 This project OWNS

- The blanks: every row of the check's list whose fix contains a placeholder (537 rows today).
- The stops: the names that halt the run (12 today, finding F5).
- The mechanism that keeps both from growing back (O5).
- The map behind ruling "b" (O6) and the rows compiled from it.

### II.2 This project RELIES ON and does not own

- **LGIC_ENFORCE** (`org/missions/D14/LGIC/LGIC_ENFORCE/`, active, held at stop): the check itself, the registry
  (`infra/logic/registry/`), the builders in `lib/opal_naming.py`, and the commit and apply gates. This project changes
  what the check SAYS about a class of names; it does not rebuild the check. FWD-5 stays LGIC_ENFORCE's outcome; this
  project is the named project its register asks for.
- **LGIC_NAMING** (complete, closed): the grammar in `org/standards/NAMING_SCHEMA.json`. O2 needs a new verdict value
  there. LGIC_NAMING is closed, so the owner of that edit must be named at L4 (Part V).
- **LGIC_CANON** (active): the rules a name is graded against.

### II.3 NOT this project -- named so no decomposition re-opens it

- **The rename backlog.** 1,975 rows are wrong names that ALREADY have a complete fix. Renaming them is the work of the
  clean-up projects (`ADVI_FIRMBKTS`, `MDPF_CANON`, `ETFS_CANON` in `infra/logic/registry/remediations.json`, and each
  pipeline's own migration under doctrine rule R19). This project renames nothing in the cloud.
- **The 462 inherited skip-cards.** Names LGIC_ENFORCE carded as not-judged under its ruling R-29 before today. Whether
  those are judged is LGIC_ENFORCE's question. This project owns only the stops that are new (finding F5).
- **LGIC_LGCTFM** (the Legacy Transform, active): it walks one product and renders its canonical form. It consumes the
  check; it is not changed here.
- **NFRA_CTLPLN contract C-NAMING**: its next issuance carries a cell that proposes a missing-row refusal to
  LGIC_ENFORCE. O5 and that cell describe the same thing from two projects. One of them must own it; this brief
  recommends this project, with NFRA_CTLPLN as the first consumer. That is a call for `1.0.0_SA_CTO` at L2.
- **Deleting resources.** Andrew approved in principle deleting `unknown-alarm`, `unknown-topic`, `test-alarm` and
  `/aws/lambda/test-yfinance-simple`, routed to CloudOps under a change record. Some of those names are still in
  today's population (`/aws/lambda/test-yfinance-simple` and two `unknown-` rows were seen). This project lists them;
  it deletes nothing.

---

## PART III -- THE QUALITATIVE BAR

No number in this part is a target. Counts appear only in Part VI, as status.

- **O1.** A person handed any one row of the list can type the correct name from that row alone. The test is disputable:
  pick a row, hand it to a seat that did not build the check, and see whether it has to ask a question.
- **O2.** The reader can tell "this name is wrong" apart from "this kind of name is not asked for a system" from the row
  itself, and the second kind is not counted among the names that break the pattern. It displaces today's reading, where
  an inline policy name is filed with the broken names and sits there with no fix anyone can apply.
- **O3.** The cadence word printed for a schedule is the one its own schedule expression implies, and a person who reads
  the expression agrees with it.
- **O4.** A seat that has never run the check runs it from the documented command and reaches the totals. The
  alternative it displaces is today's: stop, read the refusal, write a skip-card, run again, twelve times.
- **O5.** The seat that created the name is the one who hears about it, at creation, and not a later seat at the next
  whole-estate run.
- **O6.** Andrew can ask "is this registry handwritten?" and the answer is "the map is; the rows are compiled; here are
  the named exceptions". That is his own question of 2026-09-21, VERBATIM: "I am hoping this is a rulesbased op from
  LGIC and none of it is handwritten aside from maybe this pass."
- **O7.** A template is recognizable as a template in the list, and no name containing a brace is graded as correct.
- **O8.** The run that realizes FWD-5 is one a different seat can repeat and get the same totals.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Each finding states what was measured. All were measured 2026-10-07 between 09:27Z and 09:40Z at the laptop, working
tree at `e7ac51a04c`.

**F1. The population is 537 rows, not 1,298.** The check, run to completion, prints 3,519 judged rows; 537 carry a
placeholder in the fix (242 distinct name-and-type pairs). On 2026-09-21 the same count was 1,303.

**F2. The 537 are four different problems, not one.**

| group | rows | what is missing | what would fill it |
|---|---|---|---|
| A. names not asked for a system | 221 | `{system}` | a verdict of their own (ruling 3, CALL 3) -- a grader and schema change |
| B. names that need a system named | 82 | `{system}` | registry rows or the folder map (O6) |
| C. schedules and event rules with no cadence word | 107 | `{cadence}` | never characterized by anyone |
| D. storage keys and buckets with no source or firm | 127 | `{scope}`, `{source}`, others | never characterized by anyone |

Group A is 170 rows led by an AWS service or verb word, 46 inline policy names in PascalCase, 5 library layers. Group B
is 58 rows led by a refused generic word, 20 led by a firm token (`bd`, `cot`, `inf`; 16 distinct names, log groups
included), and 4 others. 251 of the 303 `{system}` rows are IAM policies.

**F3. Three of Andrew's rulings on this population are decided and not built.** Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260921_163xZ_FOUR_OPEN_CALLS_ALL_RECS_APPROVED.md`.
- Ruling 3: "an AWS service name is never a `{system}`"; the check gives these their own verdict.
- CALL 3: ruling 3 extends to inline policy names and library layers.
- Measured: `org/standards/NAMING_SCHEMA.json:190` lists three verdicts, `CONFORMANT`, `ALIAS`, `OUT-OF-PATTERN`. No
  fourth verdict exists. Group A is exactly the population those rulings cover.

**F4. Ruling "b" (a compiled registry) is decided and not built.** `infra/logic/registry/resources.json` holds 465
handwritten rows. A search of `lib/opal_naming.py` for a Terraform-root map finds none. The 2026-09-21 rows were
committed as "the reference answers the compiler must reproduce" (`b282500581`).

**F5. The check does not finish on a clean run.** It stopped 12 times, each on a name it cannot read. Each was skipped
with a scratch card (outside the repository) so the run could complete:
`ldo001-360ca30f109a-expire`, `ldo001-617eec392d89-expire`, `ldo001-d77c7b300917-expire` (live schedules);
`dowjones/barrons/session`, `dowjones/wsj/session`, `ocilar/credentials` (live secrets);
`restricted-prefix-get-put-list`, `calculated-group`, `astn/kimi/api-key` (repository);
`%s%s/`, `firms/{firm}/generations/{export_id}/receipt.json`, `bbg/` (repository storage keys).
One of the twelve was already seen on 2026-09-21. The stop is the designed behaviour (FWD-5: "a name the check cannot
read stops the run loudly"). The finding is that new unreadable names keep arriving and nothing tells their creator.

**F6. The register describes the old population.** `org/missions/D14/LGIC/LGIC_ENFORCE/project.json` fields `phase`
and `blocking` were last amended 2026-09-20 and state 1,298 rows, 1,119 with `{system}`, 243 firm-as-system. Today the
same measures read 537, 303 and 20. The registry pass of 2026-09-21 is not in that register.

**F7. `resources.json` is not an index of resources.** Its own `_about` says each row fills a `{system}` blank for a
name whose words resolve no system, and the validator refuses a row for a conformant name. `1.0.0_SA_CTO` recorded the
same correction today in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_081xZ_LGIC_NAMING_DILIGENCE_AND_REGISTRATION_FOR_EVERY_NEW_RESOURCE.md`.
O5 and O6 must not be built on the reading that it lists what exists.

**F8. The work crosses two write lanes.** Registry rows under `infra/logic/**` are written by `4.0.0_SA_CRO` only
(`.owned-paths.yaml`, lane `PLATFORM_LOGIC_DOCS`). The grader `lib/opal_naming.py`, the schema and the Terraform naming
module are outside that lane. Groups A, C and D cannot be closed by registry rows alone.

**F9. A registry edit moves generated files.** `python lib/opal_naming.py generate` into a scratch folder, compared
with the repository: `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `tests/vectors.json` differ in
their registry mark, and `portal/src/pages/InvestorReporting/header/vendorDisplayNames.generated.ts` lacks the
`commonwealth` row. The generated copies are already behind the registry before this project writes anything.

**F10. Prior art, so the specification does not re-buy it.**
- The recount and the 21 families: `org/tier1_exec/4.0.0_SA_CRO/deliverables/LGIC_PLACEHOLDER_RECOUNT_AND_A5_FAMILIES_20260921.md`
  (its section 5 covers O7's fifteen template rows and names the instrument fix; its section 6 names the grader lines).
- The operator task specification: `docs/briefs/lgic-enforce-registry-assigning-brief-20260921.md` (states itself that it
  is not an L1 brief).
- Rule SY1 in `NAMING_SCHEMA.json` already decides the 20 firm-led rows: one vendor's integration takes the vendor and
  the firm; a resource that combines feeds takes the owning product and the firm.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not ordered.

- A new verdict value is a schema change. CLAUDE.md rule 24 requires its four-postulate record and a word-boundary token
  census before it is a proposal.
- An owner for edits to `org/standards/NAMING_SCHEMA.json`, since LGIC_NAMING is closed.
- A source of truth for a schedule's cadence word (group C). Whether the schedule's own expression is enough is
  unmeasured.
- A reading of group D: whether those keys are legacy stores that belong in
  `infra/logic/registry/legacy_addresses.json`, templates of the O7 kind, or real addresses missing a source.
- The decision named in II.3 on O5 against NFRA_CTLPLN C-NAMING.
- Regeneration of the generated files with every registry batch (F9), including the ones that ship to the portal and
  to Lambda bundles (LGIC_ENFORCE decision DEC-5: a registry edit is a deploy on every generated view that ships).
- Andrew's sequencing word of 2026-09-21 ~00:55Z placed the project seating this work after MDPF_TAXSMA and
  NFRA_MCPINDEX. Whether that condition is met today is for `1.0.0_SA_CTO` to read.
- Directive D14 is placed on the laptop.

---

## PART VI -- STATUS -- NOT OUTCOME-BEARING

Do not cut outcomes from this part. Every figure: measured 2026-10-07 09:27Z to 09:40Z, laptop, working tree at
`e7ac51a04c`, registry mark `0f9890d68b7d50a8`, estate graph "as of 2026-10-07 06:16:58 UTC".

Command: `python lib/opal_naming.py census --live --repo --budget 600 --not-judged <cards> --report <file>`, with
`<cards>` = `NOT_JUDGED_R13.json` (462 cards) plus the 12 scratch cards of F5.

| measure | 2026-09-19 (register) | 2026-09-21 (recount) | 2026-10-07 (this run) |
|---|---|---|---|
| judged rows | 3,264 | 3,286 | 3,519 |
| skipped by card | -- | -- | 477 |
| rows with a blank | 1,298 | 1,303 | 537 |
| -- `{system}` | 1,119 | 1,119 | 303 (116 distinct names) |
| -- no `{system}` | 179 | 184 | 234 |
| firm-led `{system}` rows | 243 | 217 | 20 |
| wrong names with a complete fix | not read | not read | 1,975 |
| names carrying a literal brace | -- | 15 | 15 (5 graded correct) |

Coverage of the run: live plane 1,902 judged plus 137 carded of 2,039 nameable; repository plane 1,617 judged plus 340
carded of 1,957. Verdicts over the 3,519: 2,507 out of pattern, 854 conformant, 152 alias, 6 not graded.

LGIC_ENFORCE: 6 of 7 outcomes realized, held at stop since 2026-09-20 (its register, as read). LGIC_NAMING: complete.
LGIC_CANON and LGIC_LGCTFM: active.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **A decision count.** Rows and distinct names are counted; how many decisions they need is not. Group A may be one
  decision; group B's 82 rows may be a handful of folder-map entries. Neither is measured.
- **That groups C and D are small.** Nobody has classified the 234 rows without `{system}` since they were first counted.
  They did not move between 2026-09-19 and today. They may be the larger part of the work.
- **That the 2026-09-21 rows are all correct.** That pass recorded seven self-corrections. The compiler of O6 is their
  first independent check.
- **Whether the commit-time naming gate is enforcing.** `org/mcp/naming-gate.enforce` exists (dated 2026-09-17, "remove
  this file to return the naming limbs to WARN"); CLAUDE.md rule 30 says the gate is "WARN today". Not resolved here.
- **The Dell boxes and site Z.** Every figure is the laptop's tree and the shared estate graph. Whether the other
  boxes' registries agree was not read.
- **The scratch artifacts are not in the repository.** The full report (692 KB) and the card file are in the session
  scratch folder and will not survive the session. Every figure is re-derivable from the command above and the twelve
  names in F5.
- **Agreement with the hand ranking** (FWD-5's other clause, served at LGIC_ENFORCE round 19) was not re-read.
- **Whether this should be a project or a round.** `1.0.0_SA_CTO` ruled it a project when it was 1,298 rows. At 537
  rows in four groups, two of which are builds already decided by Andrew, that ruling may or may not still hold. This
  brief supplies the measurement and takes no position.

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/d14-naming-check-blank-fixes-brief-20261007.md
PROJECT           NONE-YET (directive D14, macro LGIC; code to be minted at L3)
EXISTING PRD      NONE for this project. Parent outcome: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md FWD-5 (:132)
SIBLING PROJECTS  LGIC_ENFORCE, LGIC_NAMING, LGIC_CANON, LGIC_LGCTFM (D14); NFRA_CTLPLN C-NAMING (D0);
                  ADVI_FIRMBKTS, MDPF_CANON, ETFS_CANON (the clean-up projects, remediations.json)
PRIOR ART         org/tier1_exec/4.0.0_SA_CRO/deliverables/LGIC_PLACEHOLDER_RECOUNT_AND_A5_FAMILIES_20260921.md
                  org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260921_163xZ_FOUR_OPEN_CALLS_ALL_RECS_APPROVED.md
                  docs/briefs/lgic-enforce-registry-assigning-brief-20260921.md
                  docs/briefs/d14-executable-layer-brief-20260913.md (LGIC_ENFORCE's own L1 brief)
                  infra/logic/registry/ (8 files); lib/opal_naming.py; org/standards/NAMING_SCHEMA.json
                  org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json
MEASURED AT       2026-10-07 09:27Z-09:40Z, laptop, working tree e7ac51a04c, registry mark 0f9890d68b7d50a8
```
