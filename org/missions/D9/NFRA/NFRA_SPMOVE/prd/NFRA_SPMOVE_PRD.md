```json
{
  "project": "NFRA_SPMOVE",
  "directive": "D9",
  "fabric": "laptop",
  "prd_version": "v0.2",
  "step": 4,
  "brief_ref": "docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md@d5e870fed2",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6"
  ],
  "status": "DRAFT"
}
```

# NFRA_SPMOVE - AWS to SharePoint file movements as a pattern; first instance: Schwab transactions as monthly workbooks

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO`. Directive D9, Opal Workflows; macro NFRA; execution fabric laptop.

Andrew commissioned it at this terminal 2026-09-16 ~19:4xZ ("a small project") on `4.0.0_SA_CRO~G`'s brief, which carries
his five inputs verbatim: an AWS folder on the main Opal SharePoint whose paths follow the AWS path structure; Schwab
masters 08242234 and 08335338 only; monthly workbooks, separate per master, all 140 columns; standing and daily, about
fifteen minutes after the Schwab pull; Menachem as recipient only after several clean days on his word. He confirmed the
six endpoint outcomes at this terminal 2026-09-17 ~19:0xZ ("3 approved"), record @57a15b2bbe.

**The product:** Andrew opens one spreadsheet per Schwab master per month on the Opal SharePoint site and reads every
transaction in it. Each morning yesterday's rows are already there. Nobody runs anything.

The header stays DRAFT until both halves are signed at L4-R. The author signs neither half.

**v0.2 (2026-09-17 ~22:0xZ)** answers the two independent L4-R brief-half refusals - `2.0.0_SA_COO~G` @c1281bfe0a and
`2.0.0_SA_COO~O` @caedbc4ecd, which measured the same denominator separately. Four additions, all below: BRIEF COVERAGE
over the brief's 22 headings; the Part V precondition map; the Part VII non-claims carried as this PRD's own open items;
and PART IV.5's measured sizes carried into C4 labelled MEASURED-vs-INFERRED so they decide something. Nothing in v0.1's
ENDPOINT or CONTRACTS text was deleted; C4 gained a paragraph, so the ratified-text half is re-opened at C4 only.

## Scope and evidence boundary

**This project owns:** the producer that rebuilds a month's workbook from silver into a builder-named S3 home; the bounded
Gateway capability that replaces that object in place under SharePoint's `AWS/` folder; the run record; the SharePoint
path rule as a naming-canon addition; the recipient switch.

**It relies on and does not change:** the Schwab silver tables and their producers; the completion markers; the Gateway's
sign-in, tiers, guard and audit; `lib/opal_naming.py`'s `address()` and `name()`; NFRA_OPLGTW's reader roles, which are
**never widened for this**.

**Explicitly NOT this project's:** de-duplication across masters (Andrew chose separate files, so the 99.98% overlap is
expected, not a defect); any change to `dim_transaction`; vendor egress (SharePoint is Opal's own tenant through the
existing Gateway); NFRA_OPLGTW's Schwab tools; a general-purpose SharePoint write tool.

**Evidence boundary.** The brief's substrate was measured 2026-09-16 against the repo and live S3 reads; the SharePoint
site choice ("the main Opal sharepoint" = `sites/OpalCapital`) is **this seat's reading and is confirmed at L5, not
assumed**; completion markers exist only from 2026-08-31, so any claim about marker behaviour before that date is
UNMEASURED. The brief's own seven non-claims are carried as open items in **BRIEF NON-CLAIMS CARRIED** below - this PRD
inherits every one of them and closes none by assertion.

## ENDPOINT (step 2, /endpoint --forward)

`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_SPMOVE_ENDPOINT_FORWARD_20260916.md` @8d5995ec46, six outcomes, confirmed
by Andrew ~19:0xZ 2026-09-17. FWD-1, FWD-2, FWD-4, FWD-5 and FWD-6 bar at EXERCISED; FWD-3 bars at APPLIED. The cards are
CARRIED here, not pointed at -- transcribed from that pin, ids permanent, none added and none dropped:

  FWD-1  Andrew opens one spreadsheet per Schwab master per month on the main Opal
         SharePoint and reads every transaction in it
         DONE WHEN  EXERCISED -- he has opened one and used it instead of asking someone
                    to pull the transactions
         ACCEPT     the month's file for a master holds every day's transactions with all
                    the columns the custodian sends; a row in it matches the same row at the
                    source field for field; he uses the file rather than asking an agent
         PROOF      one month's file opened by Andrew; one of its rows compared with its
                    source row; his word that he used it

  FWD-2  Each morning, yesterday's transactions are already in the current month's file,
         without anyone running anything
         DONE WHEN  EXERCISED -- two consecutive mornings have been observed, one of them
                    after a late custodian pull
         ACCEPT     the file updates itself about fifteen minutes after the day's Schwab pull
                    completes and never on a clock alone; a late pull means a late update,
                    not a missing one; a day never appears half-written
         PROOF      two mornings' files and their run records, one following a pull that
                    completed on its second attempt of the day

  FWD-3  Anyone who knows where a dataset lives in AWS knows where it lives in SharePoint,
         and the reverse
         DONE WHEN  APPLIED -- the rule is written into the naming canon and the first
                    folder follows it
         ACCEPT     the SharePoint location under the AWS folder repeats the naming rule's
                    address for the dataset segment for segment, and the rule is part of the
                    naming canon so the next dataset follows it without anyone deciding a path
         PROOF      the canon's rule and the first folder's path set beside the dataset's
                    AWS address

  FWD-4  Andrew can check what each run delivered and tell a short file from a quiet day
         DONE WHEN  EXERCISED -- he has read the record on a quiet day and on a day the run
                    could not read its source
         ACCEPT     every run records which days it read and how many rows it wrote, per
                    master per month, somewhere Andrew reads; a day with no transactions
                    reads differently from a day the run failed to read
         PROOF      the run record on a quiet day; the run record on a deliberately
                    withheld source; both read by Andrew

  FWD-5  Nothing reaches Menachem until Andrew says the files are clean, and then it does
         DONE WHEN  EXERCISED -- a send was refused before his word, his word was recorded,
                    and the first delivery after it arrived
         ACCEPT     while the files are being built and checked, Menachem receives nothing,
                    and an attempt to send to him is refused; after several clean days
                    Andrew says so, an operator turns delivery on, and Menachem receives the
                    file
         PROOF      one refused send before the word; the word; the first delivery after it,
                    seen by Menachem

  FWD-6  The next file that has to go from AWS to SharePoint is a change of inputs, not a
         new build
         DONE WHEN  EXERCISED -- a second dataset or the second master has been delivered by
                    changing inputs only
         ACCEPT     dataset, masters or firm, period and columns are inputs; the trigger,
                    the path mirror, the replace-in-place delivery and the run record are
                    shared; the second instance is produced without copying or rewriting the
                    first
         PROOF      the second master's monthly file produced from the same build with only
                    inputs changed; a third configuration exercised as a dry run

## CONTRACTS

**C1 -- the workbook.** One file per master per month, holding every transaction of that month with all 140 source
columns from `fact_trn`, rebuilt from silver and never hand-assembled. A row in the workbook matches its source row field
for field. Masters are never merged and nothing is de-duplicated.

**C2 -- the trigger is the MARKER, never a clock.** The rebuild fires on the completion marker
`schwab/{master}/meta/complete/date=YYYY-MM-DD.json`, about fifteen minutes after it lands. A late pull means a late
update, not a missing one. **Two measured irregularities the design must tolerate, both named in the brief: a marker that
arrives on the SECOND fire of the day (2026-09-11), and a marker REWRITTEN later the same day reporting zero tables
(2026-09-15).** A rewritten or zero-table marker never produces a half-written workbook: the run either rebuilds the whole
month or leaves the previous object in place and records why.

**C3 -- the address is builder output.** The S3 home is `address(...)` output and the resource names are `name(...)`
output, never typed (Rule 30). The SharePoint path is `AWS/` + the builder's key, then the object -- the mirror rule
Andrew confirmed. **`NAMING_SCHEMA.json` carries no SharePoint grammar today; adding it is this project's own cell,
ratified through LGIC_NAMING's schema bump, never a rider on LGIC_ENFORCE.** The tier (platinum vs gold) is a canon
question answered at L5 against `infra/logic/02_DOCTRINE.md`, not assumed here.

**C4 -- the write capability is BOUNDED, and it is sized against MEASURED bytes.** The Gateway's existing
`upload_text_to_site` writes small text and never overwrites; this export needs a binary workbook replaced daily. The new
capability is a large-file upload session that may REPLACE **only under the `AWS/` folder**, and may not write anywhere
else on the site. Rollback is SharePoint version history.

The size is not "tens of MB". The brief built the real files (s.4.5) and this contract carries its numbers with their
claims, because each one decides a design value:

| value | claim | what it decides in this contract |
|---|---|---|
| 45.4 MB, 140 columns, xlsx, 134,387 rows (August 2026, master 0824) | **MEASURED** - built by `4.0.0_SA_CRO~G` 2026-09-16 | the capability is sized for a REAL object of this order, never for a text write; a single-PUT path is out of scope on this evidence alone |
| 158 s to write that workbook | **MEASURED**, same run | the run's timeout is set from a measured build plus a measured upload leg, never from a framework default; the upload leg is MEASURED at L5 and the timeout set from the sum, with margin stated |
| ~72 MB for the largest month so far (2025-12, ~213k rows) | **INFERRED** - linear scaling from the measured August build; **never built** | the declared byte ceiling of the capability is **at least 150 MB**, so an inference wrong by a factor under two does not re-open the design; the first run that builds a month over 45.4 MB records its ACTUAL size, and the ceiling is re-read against it |

Two bounds this contract does NOT set, and names instead as L5 preconditions, because the brief measured neither: Microsoft
Graph's own size limit and chunk rules for a replace through an upload session (brief PART VII), and Excel open-time on a
real laptop at 45.4 MB (PART III makes that Andrew's judgment on real use, not a number set here). A cell CONFIRMS the
Graph limits against Graph's documentation and the Gateway's granted permissions before the capability is cut; if the
ceiling above exceeds what Graph or the site allows, that is a finding that re-opens C4, not a value to be assumed now.

**C5 -- the run record.** Every run records which days it read, how many rows it wrote per day, the source vintage and the
outcome. A short file on a quiet day and a short file from a failure are distinguishable from the record alone, without
opening the workbook.

**C6 -- the recipient switch is OFF until Andrew's word.** Menachem receives nothing while the files are being built and
checked. A send attempted before the word is REFUSED, and the refusal is recorded. His word is recorded when given, and
only then does delivery begin.

**C7 -- the pattern, not the instance.** Dataset, masters or firm, period and columns are INPUTS. The trigger, the address
rule, the write capability, the run record and the recipient switch are the pattern. The second delivery is a
configuration change with no new build, and FWD-6 is what proves it.

## BRIEF COVERAGE

Denominator: **22 headings** in `docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md` @d5e870fed2, counted as every
line matching `^#` at that pin (1 H1 + 15 H2 + 6 H3). The same 22 was measured independently by `2.0.0_SA_COO~G` and
`2.0.0_SA_COO~O` at L4-R. Each heading lands in exactly one of: CARRIED (a contract, surface, acceptance line or scope
clause holds it), CARRIED-AS-OPEN (this PRD holds it as a named L5 precondition or non-claim, not as a settled value), or
NOT CARRIED (with the reason, on this line).

| # | brief heading | disposition | where |
|---|---|---|---|
| 1 | H1 title -- Schwab transactions to SharePoint, the first AWS -> SharePoint movement | CARRIED | this PRD's title and C7 (first instance of a pattern) |
| 2 | ANDREW'S WORDS, VERBATIM | CARRIED | Authority and project arc, his five inputs restated; the verbatim text stays in the brief and is never re-typed here |
| 3 | PART I -- THE OUTCOME TERRITORY | CARRIED | ENDPOINT section; the six outcomes are FWD-1..FWD-6 |
| 4 | O1 one file per master per month, every transaction | CARRIED | C1; A1 |
| 5 | O2 yesterday's rows there each morning, nobody runs anything | CARRIED | C2; A2 |
| 6 | O3 the SharePoint path IS the S3 path | CARRIED | C3; A3 |
| 7 | O4 what each run delivered; short file vs quiet day | CARRIED | C5; A4 |
| 8 | O5 delivery to Menachem on his word, not before | CARRIED | C6; A5 |
| 9 | O6 the next movement is configuration, not a build | CARRIED | C7; A6 |
| 10 | PART II -- WHERE THE BOUNDARY SITS | CARRIED | Scope section: owns / relies-on / explicitly-out, including NFRA_OPLGTW is NOT a home for this and its reader role is never widened |
| 11 | PART III -- THE QUALITATIVE BAR | CARRIED, one item deliberately left to Andrew | A1 (uses it instead of asking for a pull), C1 (field-for-field), C5 (tells a missed morning from the record). **Open time at 45.4 MB is HIS judgment on real use** - the brief says so and this PRD sets no number for it (C4, second paragraph) |
| 12 | PART IV -- THE SUBSTRATE | CARRIED | the four subsections below; PART IV's own header carries no claim of its own |
| 13 | 4.1 The data (`fact_trn`, 140 columns, two masters, 99.98% overlap) | CARRIED | C1, and the overlap named as expected-not-a-defect in Scope |
| 14 | 4.2 The trigger (completion markers; the two irregularities) | CARRIED | C2; A7 |
| 15 | 4.3 The address -- builder output, not hand-typed | CARRIED | C3; A3; S3 |
| 16 | 4.4 The destination and the write path | CARRIED-AS-OPEN | C4 for the bounded replace; **the site choice is this seat's reading, CONFIRMED at L5** (Scope, evidence boundary) |
| 17 | 4.5 Measured file size | CARRIED | C4's table - 45.4 MB and 158 s MEASURED, ~72 MB INFERRED, each deciding a stated value |
| 18 | PART V -- WHAT MUST BE TRUE | CARRIED, item by item | the **BRIEF PRECONDITIONS** map below, all 10 |
| 19 | PART VI -- STATUS (declared NOT outcome-bearing by the brief) | NOT CARRIED, by the brief's own instruction | a status snapshot measured 2026-09-16 carries no contract; the facts inside it that DO bear on design are in 4.1-4.5 and are carried there |
| 20 | PART VII -- WHAT THIS BRIEF DOES NOT CLAIM | CARRIED-AS-OPEN, item by item | the **BRIEF NON-CLAIMS CARRIED** map below, all 7 |
| 21 | s.8 -- PROJECT OR FOLD-IN recommendation | CARRIED, and ANSWERED | Andrew commissioned it as a small project 2026-09-16 ~19:4xZ; the seat question is answered in Canonical handoff (not in his 2026-09-17 order) |
| 22 | REFS | CARRIED | `brief_ref` pin in the header; the prior-art paths are the L5 reading list, not restated here |

**BRIEF PRECONDITIONS (PART V, 10 of 10).** The brief states these without scoping them; this PRD says who holds each and
where it lands. None is assumed true.

| V | precondition | held by | this PRD |
|---|---|---|---|
| V.1 | a SharePoint path rule admitted into the naming canon | LGIC_NAMING (`2.0.0_SA_COO~G`) | C3 - this project's own cell, ratified through LGIC_NAMING's schema bump, never a rider on LGIC_ENFORCE |
| V.2 | delivery tier (gold vs platinum) under Doctrine R1-R21, and the `table`/function words from builder output | this project at L5 | C3 - a canon question answered at L5 against `infra/logic/02_DOCTRINE.md`, not assumed here |
| V.3 | the Gateway can replace a large binary file inside `AWS/` and only there | this project (S2) | C4; A8 is the refusal outside `AWS/` |
| V.4 | the producer rebuilds the whole month on each trigger (the brief RECOMMENDS rebuild as the mechanism for Andrew's word "append") | **the CTO, here** | **RULED: rebuild.** C1 says rebuilt from silver and never hand-assembled; C2 says the run rebuilds the whole month or leaves the object in place. Andrew's word "append new rows" names the EFFECT and is satisfied by a rebuild, which also heals a late or corrected day |
| V.5 | the trigger fires off the marker plus ~15 minutes and tolerates a second-fire or rewritten marker | this project (S1) | C2; A7 |
| V.6 | a read role scoped to exactly the two masters' `fact_trn` and the output prefix, never a widening of an existing role | this project (S7) | Scope ("never widened for this") and S7 |
| V.7 | a run record per run where Andrew can read it | this project (S4) | C5; A4 |
| V.8 | the Menachem recipient switch exists and is OFF | this project (S5) | C6; A5 |
| V.9 | a backfill decision -- which past months get built on first run (history from 2024) | **Andrew** | OPEN, and it is a card at him, not a value set here. The first run builds the CURRENT month only unless he says otherwise; C7 makes a backfill a configuration change, so his answer costs no rebuild |
| V.10 | rollback: SharePoint version history restores the prior workbook; S3 is the source; silver is never touched | this project (S2) | C4 names version history as the rollback; Scope says silver is not changed |

**BRIEF NON-CLAIMS CARRIED (PART VII, 7 of 7).** Each is inherited as an open item. A cell closes it by MEASURING it;
none is closed here by assertion.

| VII | the brief does not claim | this PRD's disposition |
|---|---|---|
| VII.1 | whether the 12:15 UTC silver sweep ever writes TRN after the fire | OPEN - L5 measures it; C2 is marker-triggered precisely so a sweep's timing is not load-bearing |
| VII.2 | who rewrote the 09-15 markers | OPEN and NOT this project's to answer; C2 tolerates the rewrite either way (A7) |
| VII.3 | the ~72 MB largest-month figure is extrapolated; only August was built; Excel open-time unmeasured | CARRIED EXPLICITLY - C4's table labels it INFERRED and sets the ceiling so the inference can be wrong by a factor under two; open-time stays Andrew's judgment (PART III) |
| VII.4 | the Gateway's Graph permissions for a replace or an upload session, and Graph's size limits, unchecked | OPEN and it GATES C4 - named in C4's second paragraph as an L5 precondition that can re-open this contract |
| VII.5 | NFRA_OPLGTW's OG-z-1 entitlement guard was not read for an Andrew-only file | OPEN - L5 reads it before S2 is cut; NFRA_OPLGTW's roles are not widened either way (Scope) |
| VII.6 | "main Opal sharepoint" is the CRO seat's reading; Andrew has not named the site | OPEN - the evidence boundary says the site is CONFIRMED at L5, not assumed, and it is one line to ask him |
| VII.7 | `.claude/skills/49-schwab-conv/SKILL.md:30` points at a silver prefix that is not where current silver lives | OPEN and OUT of this project's write surface - raised to LGIC_NAMING as a stale-pointer finding, never repaired as a rider here |

## SURFACE MANIFEST

| id | surface | what it is | outcomes |
|---|---|---|---|
| S1 | the producer | marker-triggered rebuild of a month's workbook from `fact_trn` into the builder-named S3 home | FWD-1, FWD-2 |
| S2 | the delivery capability | the bounded large-file replace under SharePoint `AWS/`, through the Gateway | FWD-1, FWD-3 |
| S3 | the address rule | `address()`/`name()` output plus the `AWS/` mirror, and its NAMING_SCHEMA addition | FWD-3 |
| S4 | the run record | per-run days read, rows written, vintage, outcome | FWD-4 |
| S5 | the recipient switch | off by default; refusal before the word; recorded enablement | FWD-5 |
| S6 | the configuration surface | dataset, masters, period and columns as inputs | FWD-6 |
| S7 | the read role | scoped to exactly the two masters' `fact_trn` and this project's output prefix | all |

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A1 | one month's workbook opened by Andrew; one row compared field-for-field with its source row; his word that he used it instead of asking for a pull | FWD-1 |
| A2 | two consecutive mornings' files and run records, one of them following a pull that completed on its second fire | FWD-2 |
| A3 | the SharePoint path of a delivered object equals `AWS/` + the builder's key, shown for two different inputs; the rule is IN the naming schema | FWD-3 |
| A4 | two run records read side by side -- a quiet day and a failed/short day -- distinguishable without opening the workbook | FWD-4 |
| A5 | one refused send before the word, the word recorded, then one delivered send | FWD-5 |
| A6 | a second dataset or the second master delivered by changing inputs only; the diff shows no new build | FWD-6 |
| A7 | a rewritten or zero-table marker produces either a whole-month rebuild or no change plus a recorded reason -- never a half-written workbook | C2 |
| A8 | the write capability refuses a path outside `AWS/`, and the refusal is recorded | C4 |
| A9 | the delivered object's MEASURED byte size and the run's MEASURED wall time are printed in the run record for the largest month built, and read against C4's ceiling; a size over the ceiling is a finding that re-opens C4, never a silent pass | C4, FWD-4 |

## Canonical handoff

L5 is `2.0.0_SA_COO`'s on a lane `0.0.0_AB_MSTR` seats. **This project is NOT in Andrew's 2026-09-17 seat order** (IRPT_BCKEND,
NFRA_MCPINDEX, MDPF_TAXSMA), so it takes a lane only when he places it or one frees past those three. First cells: confirm
the SharePoint site and the tier (C3) and read Graph's replace limits against the Gateway's granted permissions (C4's open
precondition, VII.4), then the producer (S1), because the delivery capability (S2) is only worth building once the object
it delivers exists.
