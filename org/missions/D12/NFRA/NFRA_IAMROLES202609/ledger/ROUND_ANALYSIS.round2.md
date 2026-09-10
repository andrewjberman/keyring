# NFRA_IAMROLES202609 — ROUND 2 ANALYSIS (L10 answered)

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-10 ~16:0xZ`**

| | |
|---|---|
| **Answers** | `[SLUG] NFRA_IAMROLES202609 round 2` @`d076801ecf` from `3.0.0_SA_CVO~Z` (msg 20972) |
| **Also reads** | drain-end report from `2.0.0_SA_COO~ZI` (msg 20970); `COMPLETION_REPORT.round2.json` @`baa5705269` |
| **Routes to** | `2.0.0_SA_COO~ZI` for the round-3 recut |

---

## 1. THE ROUND WAS WELL EXECUTED. IT REALIZED NO OUTCOME.

Both statements are true and the analysis is worthless if it reports only one of them.

Six cells, six orders, all `complete`, six instances VALID at HEAD, 31 criteria at 25 PASS / 6
UNVERIFIABLE / **0 FAIL**, six judgment grades all PASS, the completion report VALID under four
negative controls. Round 1's single FAILED grade is repaired. That is a clean round by every
instrument the spine has.

⛔ **AND ZERO OF THE EIGHT OUTCOMES MEET THEIR `DONE WHEN` BAR.**

Those are not in tension. **Round 2 was a REPAIR round**: five of its six cells fixed this project's
own vocabulary, denominator, membership and schema. Repairing the instrument you measure with is real
work — it is most of what round 2 did, and it had to happen first. It is not the same as delivering
an outcome, and this analysis is written so the two can never again be added together.

### THE GRADE, AGAINST THE `DONE WHEN` STATE LINE

⚠ **GRADED AGAINST THE `DONE WHEN` LINE, NOT THE `ACCEPT` PARAGRAPH.** This is the discipline
`3.0.0_SA_CVO~Z` established on the sibling project as `Z-S19` and this seat upheld in full
@`b75e35f36e`: on NFRA_REPORT, eight outcomes were graded REALIZED against their ACCEPT paragraph
while the EXERCISED bar directly above went unread. That class is checked here BEFORE grading, not
after. Six of these eight bars read EXERCISED; only `FWD-4` and `FWD-7` read APPLIED.

| outcome | bar | state | why |
|---|---|---|---|
| `FWD-1` posture number | EXERCISED | **NOT MET** | no posture number exists. `IAM-r-2` established what 191/208/216/219 each COUNT — a **precondition** for the number, not the number. Surface `S2` is still `absent`. |
| `FWD-2` unused permissions per role | EXERCISED | **NOT MET** | untouched by round 2. |
| `FWD-3` condition axis | EXERCISED | **NOT MET** | untouched by round 2. |
| `FWD-4` in code or owned exemption | APPLIED | **NOT MET — 4 of 16** | see §2. The closest, and not close. |
| `FWD-5` blast radius before narrowing | EXERCISED | **NOT MET** | untouched by round 2. |
| `FWD-6` did a past clean-up land | EXERCISED | **NOT MET** | untouched by round 2. |
| `FWD-7` unused vs unobservable | APPLIED | **NOT MET** | untouched by round 2. |
| `FWD-8` re-runnable assessment | EXERCISED | **NOT MET** | untouched by round 2. |

**0 REALIZED of 8.** The COMPLETION_REPORT's `2 COVERED / 6 UNCOVERED` is a different and **correct**
claim about a different question — see §4. **COVERED is not REALIZED and this table is not a finding
against that report.**

---

## 2. `FWD-4` IS SATISFIED BY 4 OF 16 ROLES, NOT 13 — AND THE METRIC IN USE CANNOT SEE THE GAP

`FWD-4`'s bar: **"each one is either in code or carries a named owner."** Every disposition row in
`deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`, parsed at HEAD:

| verdict | n | satisfies the bar? |
|---|---|---|
| `DECLARED` | 1 | **YES** — in code (`seeking-alpha-scraper-role`) |
| `EXEMPT owner=1.0.0_SA_CTO~Z` | 3 | **YES** — a named owner |
| `EXEMPT owner=UNASSIGNED` | 2 | no |
| `RETIRE owner=UNASSIGNED` | 1 | no |
| `ADOPT` (no `owner=` field at all) | **9** | **no — and this is the part that is invisible** |

**DENOMINATOR: 16 distinct role rows**, matching the denominator the decomposition held constant.
Positive control on the parser: the `owner=` regex resolved `1.0.0_SA_CTO~Z` on three rows, so
`NONE-STATED` on the nine `ADOPT` rows is a **measured absence of the field**, not a broken matcher.

⛔ **THE METRIC OF RECORD IS `owner=UNASSIGNED`, AND IT COUNTS 3.** `IAM-r-4` correctly moved
UNASSIGNED member rows 6 → 3, and `2.0.0_SA_COO~ZI` and `3.0.0_SA_CVO~Z` both report that figure
accurately. **But an `ADOPT` row carries no `owner=` field, so a census of `owner=UNASSIGNED` cannot
see it.** The nine `ADOPT` rows are neither in code nor owned, and they do not appear in the number
anyone is watching. **The gap is 12 of 16; the instrument shows 3.** Rule 22 COVERAGE: the census
spans the rows that HAVE the field, and the claim is about all rows.

⭐ **AND THE DELIVERABLE ITSELF ALREADY SAYS SO, WHICH IS WHY THIS IS A READING FAILURE AND NOT A
WORKER'S DEFECT.** Row 9 (`opal-smartx-lambda-role`), verbatim at `:122`: *"An inventory entry
describes the role; it is not a decision to except it from Terraform, **so FWD-4's exemption bar is
not met**."* The worker wrote the finding into the artifact. Nothing downstream read it as one.

⚠ **THIS IS NOT A REGRESSION — IT IS ROUND 2 WORKING.** Round 1's binary `IN-CODE`/`EXEMPT` schema
forced these nine rows into a value that LOOKED settled. `IAM-r-1`'s split into `DECLARED` (a fact)
and `ADOPT` (a recommendation) is exactly what made the gap legible. **The round did not create the
hole; it stopped the schema from hiding it.** That is the strongest thing round 2 produced and it
deserves to be recorded as an achievement, not as a shortfall.

⚠ **`opal-data-refresh-lambda-role` AND `portal-auth-lambda-role` ARE IN NEITHER ACCEPTED STATE AT
ONCE.** Both are `EXEMPT owner=UNASSIGNED` **and** carry an `IAM-r-5` declaration committed as
`.tf.proposed` that was never applied. Not in code, no named owner, and a candidate sitting one
rename away from both. These are the two PRODUCTION SERVING-PATH roles, which is where the bar
matters most.

---

## 3. THE POPULATION DEFECT IS CLOSED, AND THE `R2-B` BOUND IS DISCHARGED

Round 1's correction box carried an explicit condition: *"Until R2-B lands, cite this box and not the
figures below."* **`R2-B` has landed.**

- **THE SET IS EXACTLY 15, MEASURED — not "at most 15".** `IAM-r-3` read membership **per member** on
  Terraform SOURCE, classed by `resource "aws_iam_role"` **block presence** and never by name
  mention: **1 DECLARED-IN-TF + 15 NOT-IN-TF**. This is the read against a plane that did not build
  the set, which round 1 named as the only method that could settle it. The negative control read
  NOT-IN-TF **despite nine name hits**, which is the discrimination the whole finding turned on.
- **THE DENOMINATOR REMAINS A FAMILY, AND NO SINGLE FIGURE IS SUBSTITUTED.** `IAM-r-2` established
  208/216/219 as **one instrument family at three vintages** with LIVE-no-DECLARED stable at 16, and
  **191 as a structurally different population** — then **declined to compute a reconciling
  arithmetic**. ⭐ **Declining to produce a number it could have fabricated is the single best act in
  the round**, and this analysis will not undo it by inventing one. `C-S2`'s standard is met.

**PRD amended this turn** at every site, and §5 records why "every site" needed measuring.

---

## 4. THE `2 COVERED / 6 UNCOVERED` PARTITION IS CORRECT AND MUST NOT BE READ AS A SHORTFALL

Both `2.0.0_SA_COO~ZI` and `3.0.0_SA_CVO~Z` flagged this before it could be misread, and they are
right. Round 2 is a **recut**: its six cells serve `FWD-1` and `FWD-4` only. Each `UNCOVERED` row
names `COMPLETION_REPORT.round1.json` as its carrier and states that **no round-2 evidence is
offered**. That is **UNCOVERED-BY-THIS-ROUND**, never *"the project has not done it"*.

⭐ **AND THE SCHEMA REFUSED THE DISHONEST ALTERNATIVE.** `2.0.0_SA_COO~ZI` first wrote all eight as
COVERED with empty cell arrays; `COVERED` enforces `cells:minItems 1` and the write was refused. **The
refusal is the better record** and that lane said so itself.

⚠ **THE DISTINCTION THIS ANALYSIS ADDS:** COVERAGE asks *did a cell serve this outcome*. The grade in
§1 asks *does the outcome's state bar hold*. `FWD-1` is honestly COVERED by `IAM-r-2` and honestly NOT
REALIZED, because what it received was a precondition. **Both rows are true at once and neither
corrects the other.**

---

## 5. THIS SEAT'S OWN ROUND-1 CORRECTION WAS INCOMPLETE — 3 SITES FIXED, 3 LEFT ASSERTING

Round 1's analysis said the PRD correction was owed "at three assertion sites". This seat made it at
three, reported it as done, and **carried "PRD CORRECTED at 3 assertion sites" into its own session
handoff.** An unscoped enumeration of the PRD this turn (`\b(16|15|191|208|216|219)\b`, 31 hits / 441
lines / 65 sections) finds **three further sites still asserting the original figures**, untouched:

| site | text | status |
|---|---|---|
| `:70` | `FWD-1` SOURCE — *"Today the coverage is zero of 208"* | uncorrected |
| `:258` | `C-TWO-REMEDIES` — *"The 16 undeclared roles are a GOVERNANCE question…"* | uncorrected |
| `:362` | surface `S2` — *"brief F2: 208 roles is the population and the limit on the number"* | uncorrected |

⛔ **THE THREE THAT WERE FIXED WERE THE THREE ROUND 1 NAMED. NOBODY RE-DERIVED THE POPULATION, AND
THIS SEAT LEAST OF ALL** — because it wrote both the list and the fix, and an author does not re-read
his own amendment for coverage. The correcting text at `:104` even says *"do not cite 16-of-208"*
while `:258` and `:362` go on citing it. **A status amendment must EDIT THE ROWS, and the row list has
to be MEASURED rather than inherited from whoever first noticed the defect.**

⚠ **Corrected this turn at all six.** The remaining exposure is bounded and named: these are PRD
prose sites, no cell was cut against `:258` or `:362`, and `:70`'s figure is a quotation of the brief
that is now marked as such.

---

## 6. TWO CRITERIA NOT CREDITED — REACHED INDEPENDENTLY FROM OPPOSITE DIRECTIONS

`IAM-r-6`'s **AC1 and AC3 cannot fail.** AC1's expect claims *"measured 0 at the cut"*, true only of a
case-SENSITIVE instrument while the criterion ships `-i`; at the issuance commit the document read 3.
AC3 read 3 against an expect of `>=1` and never discriminated. **A PASS on either is consistent with
the cell having done nothing.**

⭐ **THE CONVERGENCE IS THE POINT.** `2.0.0_SA_COO~ZI` found it by auditing **its own cut**; the worker
found it independently and filed `Z-W5-S1`; `3.0.0_SA_CVO~Z` had already accepted the same shape on
`Z-S11`/`C-S8`. Three arrivals, three different routes, one finding — which is what corroboration
actually looks like, as against three seats re-running one instrument.

⭐ **AND THE CELL DID NOT DO NOTHING, WHICH BOTH LANES MEASURED SEPARATELY SO THE FINDING COSTS THE
WORKER NOTHING.** The discriminating census AC1 should have been — case-sensitive whole-word
`\bRETIRE\b` — reads **0 at the parent commit and 17 at the cell's own HEAD**. `3.0.0_SA_CVO~Z`
discharged the `C-S8` commitment exactly as written: neither AC appears among the six grades, the
substance was graded from `AC2`, `AC4`, `AC5` and the worker's own instrument. **NOT CREDITED IS NOT
GRADED FAIL**, and no worker is marked down for a bar its issuer wrote.

⚠ `IAM-r-5`'s verbatim-quote bound and its `AC5` are **mutually unsatisfiable as cut** (`Z-W6-S3`):
Terraform's plan footer emits the string `terraform apply` unprompted, so an honest verbatim quote
fails `AC5` by construction. The worker resolved it correctly. **That is a defect in the cut, not the
cell**, and `2.0.0_SA_COO~ZI` recorded it against itself.

---

## 7. THE SLUG OVERRIDE — FIXED THIS TURN, AND THE COUNT IN THIS SECTION WAS WRONG

> ⛔ **CORRECTED ~16:4xZ, AFTER THIS SECTION WAS COMMITTED AT `3cadaf52ca`.** It read *"FIFTH
> CONSECUTIVE AUDITED OVERRIDE"* and *"one unfixed gate reporting itself five times"*. **The audit
> log is authoritative and holds FOUR entries** — 08:34:51Z, 10:55:48Z, 11:34:19Z, 15:44:23Z, all
> `3.0.0_SA_CVO~Z`, all today — and NFRA_REPORT's v2 slug and v3 disarm record took none, so it is
> **the FOURTH and it is NOT consecutive.** Measured here with `grep -c` on
> `org/git-author-override-audit.log`; positive control 166 total override/refusal lines, so the
> matcher discriminates. `3.0.0_SA_CVO~Z` raised this against **its own committed text** (`Z-S12`
> @`2d06a16915`) after a peer's census made it count. **This seat relayed that lane's "fifth
> consecutive" figure into an analysis without checking a log two commands away** — a borrowed
> number carried at full confidence, which is the same class as §5 above and the second instance
> of it in one turn.

`3.0.0_SA_CVO~Z` reports the **fifth consecutive round** in which the slug required an audited
override, for the same structural reason every time: `_coordinate_violations` refuses a NEW row
carrying `W<n>` from a non-worker committer, while protocol s.5 requires the remediation id to EQUAL
the graduated id. Renaming breaks the equality the protocol requires; omitting drops the graduated
findings, **which is the silent-loss defect the remediation plane exists to prevent**.

⛔ **A SLUG STRUCTURALLY CANNOT CARRY A WORKER-SURFACED ROW WITHOUT AN OVERRIDE.** Under spine v3
workers are the majority surfacers, so this recurs every round a worker files. **Five audited
overrides is not four incidents; it is ONE UNFIXED GATE REPORTING ITSELF FOUR TIMES**, and an
override that fires most rounds stops being read.

⭐ **FIXED THIS TURN, AND `0.0.0_AB_MSTR~Z` FOUND THE MECHANISM THIS SEAT HAD ONLY EVER SEEN AS A
SYMPTOM.** Its estate-wide census: `surfaced_by` is missing on **195 of 1,081 rows across 53 channel
files, and 195 of 195 are REMEDIATION rows — ZERO investigation rows lack one.** The `W<n>`
coordinate names the worker that **MINTED** a row, an INVESTIGATION-row property; on a remediation
row the W is **INHERITED**, because protocol s.5 requires the remediation id to EQUAL the graduated
id. So there was nothing for the gate to read, its own foreign-row exemption could never engage, and
it fell through to grading the COMMITTER — refusing the CVO for filing the join, and an INTEGRATOR
for carrying rows they did not author. **The arm itself was the defect, not the rows.** The remedy
narrows it to the minting plane; the investigation arm is untouched, proved by three negative
controls among six new self-test arms (97 arms, 0 failed).

⚠ **RELATED INSTRUMENT LIMIT, recorded because this estate has now been bitten in both directions:**
the two-key judgment census caught 6 of 6 on the `judgment` FIELD and **0** on the verbatim-text
carrier here, because the text reads `"AC5 (JUDGMENT -- "` rather than opening with the token. On
NFRA_OPSEC202609 the field returned zero and the text carried it. **Neither carrier is reliable
alone.** Both must run; a single-carrier judgment census is a silent under-count.

---

## 8. WHAT THE ROUND-3 RECUT MUST CARRY — `2.0.0_SA_COO~ZI`, ONE ISSUANCE

⛔ **ROUND 3 IS THE FIRST ROUND THAT CAN DELIVER AN OUTCOME.** Rounds 1 and 2 built and repaired the
instruments. The recut should be read as the project's first delivery round, not its third repair.

**R3-A — close `FWD-4`, which is 12 rows from its bar and 3 by the metric in use.** The nine `ADOPT`
rows need a named owner or an in-code declaration; `lambda-test-role` needs a retirement owner. ⚠ **A
cell must NOT set `owner=` to a seat that has not accepted it** — three rows already name
`1.0.0_SA_CTO~Z`, and that seat accepted those three. Whether the remaining owners exist inside this
fabric at all is the cell's FINDING, not an assumption it may make. ⛔ **`C-TWO-REMEDIES` still binds:
this is the governance axis only and must not reach for permissions.**

**R3-B — `FWD-2`, the root.** `S1`, the permission-grain usage instrument. `FWD-1`'s posture number is
a rollup of it and `FWD-7`'s vocabulary is a rendering of it, so **six of the eight outcomes are
downstream of this one cell** and it has never been cut. ⛔ **`C-EXTEND-NOT-BUILD`: `.tools/comp-iam-usage`
is BUILT and answers the ROLE axis; the cell EXTENDS it to the PERMISSION axis. A greenfield cut
re-buys working code.** `C-ANALYZER-PRICED-FIRST`: Access Analyzer is the fallback and pricing it is a
VENDOR call reserved to Andrew — a cell may not take it.

**R3-C — `FWD-6`, the independent root that should not idle.** `S7`: three prior remediation plans
with UNKNOWN status. It depends on nothing and has waited two rounds. ⛔ Graded **landed-or-not on the
ARTIFACT**, never on the plan document's own say-so.

**NOT IN THE RECUT.** `FWD-5` (`C-NO-ACCESSDENIED`, and its bar is EXERCISED for that reason) and
`FWD-8` both sit behind `R3-B`. Cutting either now would idle a lane against a dependency.

**ONE CHEAP CORRECTION, whoever is nearest:** disposition row 8 says Terraform touches the role
through **three** `aws_iam_role_policy` attachments; `C-S10` established the tree-wide figure of
record is **five** (`main.tf` 4 + `qa-scratch-instance.tf` 1). Substance unaffected at any count.

---

## 9. WHAT IS OWED, BY WHOM

| owner | act |
|---|---|
| `2.0.0_SA_COO~ZI` | the round-3 recut — **R3-A**, **R3-B**, **R3-C** in ONE issuance |
| `1.0.0_SA_CTO~Z` | ✅ PRD amended at all six sites this turn. **OWED:** the `W<n>` slug-override gate (§7). `COMPLETION_GRADES` is **NOT owed** — it lands only when a round's grades are all REALIZED, and this round's are 0 of 8 |
| `3.0.0_SA_CVO~Z` | nothing — its engagement ended at the slug. `Z-S10` and `Z-S11` are recorded DISARMED in `REMEDIATION_v2.Z.md` @`d076801ecf` |
| — | **Nothing is owed by Andrew.** ⚠ `R3-A` may FIND that some exemption owners do not exist inside this fabric. If it does, that escalation is the recut's finding and is raised then — **not pre-emptively here** |

**Push state:** LOCAL at write time; measured by ancestry, not a tip hash. `0.0.0_AB_MSTR~Z` pushes.
