# LGIC_BLANKFIX -- every broken name gets a complete fix: closing the blanks in the naming check's list

```json
{
 "project": "LGIC_BLANKFIX",
 "directive": "D14",
 "fabric": "dell1",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/d14-naming-check-blank-fixes-brief-20261007.md@af5d8b6df4",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-07. **Brief:** `docs/briefs/d14-naming-check-blank-fixes-brief-20261007.md` @af5d8b6df4
(`4.0.0_SA_CRO`). **Endpoint proposal:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_D14_NAMING_CHECK_BLANK_FIXES_20261007.md`.
**Confirmed by Andrew:** NOT CONFIRMED. The seat proceeds under its armed `/self-drive`; an amendment of his is re-cut in place.
**Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO wrote the brief.
**COO:** UNSEATED at registration.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An engineer about to clean up one part of the estate runs the naming check on it and can act
         on every line without asking anyone
         DONE WHEN  EXERCISED -- one live run on one real part of the estate, read to the end by someone
                    who did not build the check
         ACCEPT     an engineer runs the check on one real folder of infrastructure with no preparation
                    and reads one line per name; every line says the name is right, or gives the whole
                    correct name, or says plainly that this kind of name is not asked to carry the part
                    that is missing and why; no line has a hole in it; a line read from a saved example
                    instead of the live run fails the outcome
         SOURCE     brief I.0, the candidate thread

  FWD-2  Someone who runs the check over everything reads a list in which every wrong name comes with
         the complete name it should have
         DONE WHEN  EXERCISED -- the whole list read, and rows handed to someone who did not build it
         ACCEPT     pick any row of the full list and hand it to a person who did not build the check;
                    they can type the correct name from that row alone, without asking a question
         SOURCE     brief O1; Part III O1

  FWD-3  A reader is told when a kind of name is simply not asked to say which business system it
         belongs to
         DONE WHEN  EXERCISED -- a reader has told the two kinds of row apart on sight
         ACCEPT     looking at a name of a kind that carries no business system, the reader is told so
                    in plain words, and that name is not counted among the broken ones -- where today
                    it sits with the broken names with no fix anyone can apply
         SOURCE     brief O2; Part III O2; Andrew's ruling 3 and CALL 3 of 2026-09-21

  FWD-4  Someone renaming a schedule or moving a stored file reads the whole target, with nothing left
         to look up
         DONE WHEN  EXERCISED -- one schedule and one stored file each renamed from the list alone
         ACCEPT     the list gives a schedule's new name with how often it runs filled in, and a stored
                    file's new location with where it came from and whose it is filled in; a person who
                    reads the schedule itself agrees with the word the list chose
         SOURCE     brief O3; Part III O3

  FWD-5  Anyone can run the check from start to finish without writing anything for it first
         DONE WHEN  EXERCISED -- someone who has never run it runs it from the written instructions and
                    reaches the totals
         ACCEPT     a person who has never run the check follows the written instructions on a fresh
                    copy of the work, using only what that copy already holds, and it finishes -- where
                    today it stops partway, over and over, until they write it a list of names to skip
         SOURCE     brief O4; Part III O4; finding F5

  FWD-6  Whoever creates a name the check cannot place hears about it when they create it
         DONE WHEN  EXERCISED -- a deliberately unplaceable name has been tried and stopped, and a
                    placeable one let through
         ACCEPT     the person who adds something with a name nobody could place is told at that moment,
                    and told what they owe to make it placeable; the list of unplaceable names is no
                    longer than it was the last time anyone ran the check
         SOURCE     brief O5; Part III O5

  FWD-7  Whoever keeps the register says where things belong once per folder, and writes an entry by
         hand only for a real exception
         DONE WHEN  EXERCISED -- the register rebuilt from the short list and compared with what it
                    held before
         ACCEPT     Andrew asks whether the register is written by hand and the answer is: the short
                    list of folders is, everything else is produced from it, and here are the named
                    exceptions
         SOURCE     brief O6; Part III O6; Andrew 2026-09-21, "I am hoping this is a rulesbased op from
                    LGIC and none of it is handwritten aside from maybe this pass"

  FWD-8  A reader never meets a pattern from the code presented as if it were the name of a real thing
         DONE WHEN  EXERCISED -- the whole list read, and every pattern in it found shown as a pattern
         ACCEPT     a pattern with a blank meant to be filled in later is shown as a pattern, never as a
                    broken name and never as a correct one; a reader going through the full list finds
                    none presented either way
         SOURCE     brief O7; Part III O7

  FWD-9  The estate-wide naming check can be read as finished from one run that anyone can repeat
         DONE WHEN  EXERCISED -- one run, its totals read, and a second person getting the same totals
         ACCEPT     one person runs the check once and reads its totals; a different person runs it and
                    gets the same; nothing in the reading rests on a figure carried over from an older
                    report
         SOURCE     brief O8; Part III O8
```

## PROVENANCE (outside the ratified section)

- FWD-5 was tightened on `4.0.0_SA_CRO`'s read of the endpoint (msg 106131): the runner writes no skip list; the run may use the
  skip list the repository already holds.
- FWD-9 is LGIC_ENFORCE's FWD-5 seen from this project: when FWD-9 is REALIZED, `1.0.0_SA_CTO` grades LGIC_ENFORCE's FWD-5 from the
  same run.
- v0.2 (2026-10-07): FWD-8's bar raised from APPLIED to EXERCISED on `3.0.0_SA_CVO`'s note at signing (msg 106166): five pattern rows
  grade correct today, so "shown as a pattern" has to be read off the list, not taken from the change that was applied.
- Two L2 rulings, recorded in the endpoint proposal: this is a project and not an LGIC_ENFORCE round; FWD-6 is owned here.

## CONTRACTS

| Contract | Counterparty | State |
|---|---|---|
| C-CHECK: the check itself | LGIC_ENFORCE (held at stop); `lib/opal_naming.py` `census --live --repo` | This project changes what the check SAYS about four groups of names; it does not rebuild the check. A change to the grader is cut as a cell here and lands in `lib/opal_naming.py` under LGIC_ENFORCE's existing tests, which must stay green. |
| C-VERDICT: a fourth verdict value for FWD-3 | LGIC_NAMING (closed); `org/standards/NAMING_SCHEMA.json` | The schema lists three verdicts (brief F3, read at `:190`). A fourth is a schema change: its four-postulate record and word-boundary token census come first (CLAUDE.md rule 24), written by this seat at the cell's cut. **Owner of the schema edit: this project, by this seat's ruling here,** since LGIC_NAMING is closed; the edit is one row and its record, nothing else of the schema moves. |
| C-REGISTRY: registry rows and the folder map (FWD-7) | `4.0.0_SA_CRO`, the one writer of `infra/logic/**` (lane PLATFORM_LOGIC_DOCS) | Every row and the map are written by that lane. A cell that needs a row hands its content to that seat; `lib/opal_naming.validate()` reads 0 refusals before the commit. `resources.json` is NOT a list of resources (brief F7; NFRA_CTLPLN PRD v0.14); nothing here is built on that reading. |
| C-GENERATED: the generated views | LGIC_ENFORCE decision DEC-5; the portal; Lambda bundles | A registry edit moves generated files (brief F9), and some ship. Every registry batch regenerates them in the same commit. A generated view that ships is a deploy and takes its own pair; the batch that changes none that ship says so with the diff. The views are ALREADY behind the registry (F9): the first cell that touches the registry reads that gap and does not inherit it silently. |
| C-CADENCE: the cadence word for FWD-4 | each schedule's own expression | UNMEASURED whether the expression alone decides the word (brief Part V). The cell's first read is the 107 group-C rows against their expressions; a row the expression cannot decide is listed, not guessed. |
| C-CREATE: the stop at creation for FWD-6 | NFRA_CTLPLN C-NAMING (first consumer); `.tools/naming-apply-gate.py`, `.tools/naming-gate.py` | A name the check cannot place is refused where it is created, with what is owed. This is NOT the withdrawn missing-row refusal for a well-formed name. The gates are LGIC_ENFORCE's files; the change is a cell here under their tests. |

## 1. The arc

**Start.** The estate-wide naming check prints 3,519 judged rows; 537 carry a fix with a blank in it, in four groups (brief F2), and
the run stops twelve times on names it cannot read (F5). LGIC_ENFORCE reads 6 of 7 outcomes realized and has been held at stop since
2026-09-20 on this residual.

**End.** Every row of the check's list is actionable from the row alone. A kind of name that is not asked to carry a system says so.
The run finishes on a fresh copy. A new unplaceable name is stopped where it is made. The register is a short list of folders plus
named exceptions. One repeatable run reads LGIC_ENFORCE's last outcome as realized.

## 2. THREAD -- FWD-1, one folder of infrastructure end to end

1. **Pick.** One Terraform root that holds all four groups of F2. The brief proposes `infra/aws/terraform/bd-pipeline/` and did not
   measure whether it holds a schedule with no cadence word and a storage key with no source. Round 1's first cell measures that and
   picks the root that does; the pick is recorded with its counts.
2. **Run.** The check, scoped to that root, live, with no skip list written for the run.
3. **Group A** rows in that root read with their own verdict (C-VERDICT).
4. **Group B** rows in that root read with a system, from the folder map or a row (C-REGISTRY).
5. **Group C** rows in that root read with a cadence word (C-CADENCE).
6. **Group D** rows in that root read with a source and an owner, or as a legacy store, or as a pattern (FWD-8's instrument).
7. **Read.** A seat that did not build any of it reads every line of the root's output and acts on each without a question.

Round 1 builds only this thread, on the one root. Each hop is the thin version of an enrichment outcome; the whole-estate versions
are the backlog.

## 3. ENRICHMENT BACKLOG (ordered, one line each)

1. FWD-3 over the estate: all 221 group-A rows under the fourth verdict (Andrew's ruling 3 and CALL 3, decided 2026-09-21).
2. FWD-7: the folder map and the compiler; the 2026-09-21 rows are "the reference answers the compiler must reproduce" (brief F4).
3. FWD-2 for group B: the 82 rows that need a system, rule SY1 deciding the 20 firm-led ones (brief F10).
4. FWD-4 for group C, then group D (both "never characterized by anyone", brief F2).
5. FWD-8: the fifteen pattern rows, five of them graded correct today.
6. FWD-5: the twelve stops, each read: a real name that needs a row, a secret's name, or a pattern.
7. FWD-6: the stop at creation, then NFRA_CTLPLN as its first consumer.
8. FWD-9: the repeatable run, then this seat's grade of LGIC_ENFORCE's FWD-5.

## 4. WORKSTREAMS AND OWNERS

- **One workstream.** One COO lane on the laptop, asked of `0.0.0_AB_MSTR` when this PRD reads ADMITTED.
- **Write surface:** `lib/opal_naming.py` and its tests; `.tools/naming-gate.py`, `.tools/naming-apply-gate.py` and their tests; one
  row of `org/standards/NAMING_SCHEMA.json` (C-VERDICT); `org/missions/D14/LGIC/LGIC_BLANKFIX/**`.
- **Written through another lane:** every file under `infra/logic/**` (`4.0.0_SA_CRO`); every generated view that ships, under its
  own pair.
- **Not this project** (brief II.3, unchanged): the rename backlog of 1,975 rows that already have a complete fix; the 462 inherited
  skip-cards; LGIC_LGCTFM; deleting any resource.
- **Sequencing.** The brief (Part V) cites Andrew's word of 2026-09-21 placing the seating of this work after MDPF_TAXSMA and
  NFRA_MCPINDEX. Read today: MDPF_TAXSMA is closed (Andrew 2026-10-07); NFRA_MCPINDEX is seated at site Z. THIS SEAT'S READING,
  stated as a reading and without that word's verbatim text in front of it: a seat order, met. If that word meant NFRA_MCPINDEX
  complete, the COO seating waits and L1 to L4 here do not.

## 5. Rulings closed at L4 (no decide-first question enters L5)

1. A project, not a round of LGIC_ENFORCE (endpoint proposal).
2. FWD-6 is this project's; the missing-row refusal for a well-formed name stays withdrawn (NFRA_CTLPLN PRD v0.14).
3. The schema edit for the fourth verdict is owned here (C-VERDICT).
4. The thread's root is measured and picked by round 1's first cell, not typed here.
5. Nothing in this project renames, moves or deletes a resource in the cloud.

## 6. SURFACE MANIFEST (step 4 -> step 5)

| # | Outcome | Surface | State today | Contract | Act |
|---|---|---|---|---|---|
| S01 | FWD-1 | the check scoped to one Terraform root | held: the check runs estate-wide; a root scope is unmeasured | C-CHECK | measure, then wire |
| S02 | FWD-3, FWD-1 | the verdict enum in `org/standards/NAMING_SCHEMA.json` | measured by the brief: three values at `:190` | C-VERDICT | wire, after the four-postulate record |
| S03 | FWD-3 | the grader's handling of group A (170 service-led, 46 inline policy, 5 layer names) | measured by the brief (F2) | C-CHECK | wire |
| S04 | FWD-7, FWD-2 | a Terraform-root map and its compiler | absent: "a search of `lib/opal_naming.py` for a Terraform-root map finds none" (F4) | C-REGISTRY | build |
| S05 | FWD-2 | registry rows for group B's 82 | held: 465 handwritten rows exist; group B's are not among them | C-REGISTRY | wire |
| S06 | FWD-4 | the cadence word for group C's 107 | unmeasured | C-CADENCE | measure, then wire |
| S07 | FWD-4 | source and owner for group D's 127 | unmeasured: legacy store, pattern or real address | C-REGISTRY | measure, then wire |
| S08 | FWD-8 | the instrument that reads a brace pattern | measured by the brief: 15 rows, 5 graded correct | C-CHECK | wire |
| S09 | FWD-5 | the twelve names that stop the run | measured by the brief (F5), each named | C-CHECK, C-REGISTRY | wire |
| S10 | FWD-6 | the commit and apply naming gates | held: they refuse a badly formed name; an unplaceable one is unmeasured | C-CREATE | measure, then wire |
| S11 | all registry cells | the generated views | measured by the brief: already behind the registry (F9) | C-GENERATED | regenerate with each batch |
| S12 | FWD-9 | one documented command and its totals | held: the command exists; it needs 474 cards today (462 inherited plus 12) | C-CHECK | wire |

## 7. BRIEF COVERAGE -- content carried, not just cited

| Brief | What it says | Where it is carried |
|---|---|---|
| I.0 | the candidate thread: one engineer, one Terraform root, every line actionable | ENDPOINT FWD-1; section 2 |
| O1 to O8 | the eight outcomes | ENDPOINT FWD-2 to FWD-9, one each, in order |
| II.1 | owns the blanks, the stops, the mechanism that keeps them from growing back, the map | section 4 write surface; S03 to S10 |
| II.2 | relies on LGIC_ENFORCE, LGIC_NAMING, LGIC_CANON | C-CHECK, C-VERDICT |
| II.3 | not this project: the rename backlog, the 462 cards, LGIC_LGCTFM, deletion; the C-NAMING question | section 4; ruling 2 |
| Part III | the qualitative bar per outcome | each ACCEPT line |
| F1, F2 | 537 rows in four groups | section 1; section 2 hops 3 to 6; backlog 1, 3, 4 |
| F3, F4 | three rulings of Andrew's decided and not built | C-VERDICT; backlog 1 and 2; S02, S04 |
| F5 | twelve stops | S09; backlog 6 |
| F6 | LGIC_ENFORCE's register describes the old population | section 1 states today's; the register row is corrected when FWD-9 is graded |
| F7 | `resources.json` is not an index of resources | C-REGISTRY |
| F8 | the work crosses two write lanes | section 4; C-REGISTRY |
| F9 | a registry edit moves generated files | C-GENERATED; S11 |
| F10 | prior art | backlog 3 (rule SY1); S08 (the recount's section 5) |
| Part V | what must be true | C-VERDICT, C-CADENCE, C-GENERATED; section 4 sequencing |
| Part VII | what the brief does not claim | S06, S07, S10 carry "unmeasured"; ruling 1 answers project-or-round |
