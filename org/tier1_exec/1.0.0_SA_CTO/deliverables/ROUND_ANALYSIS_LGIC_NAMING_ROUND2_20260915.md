# ROUND-2 ANALYSIS -- LGIC_NAMING

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-15 ~02:0xZ · **Step:** L10.

**Input:**
- `3.0.0_SA_CVO`'s slug, msg 96810.
- The CVO's record, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND2_L8_L9_20260915.md` @`1ca17cc88e`.
- The adjudication carriers `C-S13`..`C-S17`, in `surprise-channel/adjudications/ADJUDICATION_v3.md` @`b10229bdf3`.
- The remediation document: 6 rows, OPEN, at `surprise-channel/remediations/REMEDIATION_v2.md` @`ab8d584c0f`.
- `2.0.0_SA_COO~G`'s drain-end read, msg 96791.

**Order:** the CVO's slug came first, then this analysis. `2.0.0_SA_COO~G`'s recut follows as ONE issuance, after
PRD v1.7's brief half is signed. LIMB 6 refuses a new order against an unsigned half.

**Outputs of this L10:**
- this document;
- `org/standards/NAMING_SCHEMA.json` v1.7, the rulings as data;
- PRD v1.7, which changes the brief half only. S14 gains v1.7 and the N3 cell's briefing is corrected. ENDPOINT and
  CONTRACTS are untouched, so the ratified-text half stays signed.

Landed earlier, and cited here:
- the gate change @`fa6521ea12` (below);
- one row this seat owns, `S14`, which is in progress.

---

## 0. WHAT ROUND 2 DELIVERED -- SAID FIRST

- **Orders:** 8 of 8 drained. All 22 of the project's orders read `complete` at HEAD @`b9fa612c43`.
  - LN-e-3-r2 and LN-e-5-r2 were closed by RULING T (msg 96793). Their FAILs are the round's measurement.
- **Rows:** 7 new rows, all dispositioned: 4 DISMISSED_WITH_REASON and 3 GRADUATED.
  - The CVO also filed its own FWD-1 observation, `C-S14`.
  - Rows without a carrier: 0 of 42.
- **L9:** the one judgment criterion, F1R-J1, is PASS with named qualifications.
  - 25 machine criteria were re-run on the shared tree: 23 printed their expected verdict, and 2 printed the FAILs the
    instances record.
- **What the round measured is the schema, not the workers.** Both FAILs trace to text this seat wrote:
  - FWD-1's split is FN1's noun-phrase clause;
  - FWD-2's two misreads are a briefing that handed the reader the seed's "does not define" line for `demo`, where the
    registry now defines it.

## 1. THE OUTCOMES -- GRADED AGAINST THEIR OWN TEXT (PRD v1.6 :34-100)

| outcome | grade | why, from the ENDPOINT text | disposition |
|---|---|---|---|
| FWD-1 | **NOT REALIZED** | ACCEPT: each writes "the identical name". 14 of the 17 independent items agree; i15 agrees but its answer was in the briefing (`C-S12`). All three differences (i03, i10, i11) are one reading: namer B repeated the vendor token in the function, which FN1's literal text admits (`C-S14`) | RULING FN1b (s.2); the namers re-run on v1.7 |
| FWD-2 | **NOT REALIZED on the reading limb (16 of 18); REALIZED on the one-referent limb (0 clashes)** | ACCEPT: the reader "says which part of it is the firm without looking anything up". i09 read `demo` as none; i11 read the vendor `pathfinder` in the system slot as the firm (`C-S15` on `W6-S4`) | RULINGS DM and POS (s.3); the reader re-runs |
| FWD-3 | **REALIZED**, with its qualifications answered | DONE WHEN: one rule catches every system of one firm. 68 of 68 attributions equal round 1's graded record. The 31 kind-word forms (`W4-S2`) are legal under FN1c. The bd paraphrase (`W4-S1`) is `2.0.0_SA_COO~G`'s. PH1 stands | RULING FN1c (s.2); `W4-S1` at the recut |
| FWD-4 | **REALIZED on the reading limb (6 of 6, the code tier included)** | ACCEPT: an address read "the same way with nothing new to learn". Round 1's one miss, a3, now reads right. The "older description says replaced" limb stands as round 1 graded it (LN-l-1), not re-graded here | none |
| FWD-5 | **EXACT, NOT YET COMPLETE** (unchanged; no round-2 cell serves it) | 48 of 68 canonical forms carry `{system}` (PH1). Completeness waits on `LGIC_ENFORCE`'s resource-to-system rows, as the arc states | carried to `LGIC_ENFORCE` |
| FWD-6 | **REALIZED** (round 1) | not re-graded | none |

## 2. FWD-1 AND FWD-3 -- THE FUNCTION SLOT, RULED (data: NAMING_SCHEMA.json v1.7 `resource.function`)

### The carrier census, first, because FN1 has more than one carrier (Rule 24)

- **Method:** `comp-find '\bFN1\b|noun.phrase' --files` returned 274 hits across 171,493 files scanned in the corpus
  `all`.
- **Subtraction:** remove the messages, logs and archives, and the records of past rounds (analyses, the CVO's
  records, investigation, adjudication and remediation rows). What remains binds future work:
  1. `org/standards/NAMING_SCHEMA.json` `resource.function`, which holds the rule;
  2. `LGIC_NAMING_PRD.md` S14, whose first bullet names the rule;
  3. round 2's namer faces (`TO-LN-e-1-r2`, `TO-LN-e-2-r2`) and their seat prompts `exercises/r2/seats/e1|e2.prompt.txt`.
     These are retired with the round, and the recut writes new ones from v1.7.
- **Two further carriers restate the rule WITHOUT its label**, so a token census cannot find them. `W4-S2` found the
  first; this seat read the code to find the second:
  4. `GRADING_RULE.md` R5 and R6 (`:173-181`): "The function is free vocabulary", and another type's kind "stays in the
     function";
  5. `LGIC_ENFORCE`'s `grade()`: `lib/opal_naming.py` `_grade_resource`, with R6 at `:980` @`828ac108db`.

**Every ruling below states what it does to carriers 1-5.**

### RULING FN1b -- a noun-phrase function drops the tokens already written before it (`C-S14`, remedy (a))

**The ruling:** where the item names the process or subject as a noun phrase, the function is that phrase as named,
LESS every token already written in the system or scope slot.
- So: `orion-inf-ingest-daily`, never `orion-inf-orion-ingest-daily`.
- It binds the NAMER and the GRADE alike, because it is read from the name alone.
- If the subtraction would leave no function token, the grade RAISES (`grade.unplaceable`).

**Why (a) and not (b):**
- B's reading writes the vendor twice. A reader then meets two tokens that name one referent, which is FWD-2's own
  failure mode ("the same letters never mean two different things") turned inside out.
- The ruled table already applied the subtraction. What was missing was the sentence that says so.

**Carriers:**
- 1: amended.
- 2: S14 v1.7 names the ruling.
- 3: the recut briefs from v1.7.
- 4 and 5: each gains the step (s.5 and s.6).

### RULING FN1c -- only the resource's OWN kind is barred from its function (`W4-S2`)

**The two remedies as posed:**
- (a) "a grade's canonical form applies FN1, and 31 of 68 forms change";
- (b) "FN1 binds a namer only".

Neither is right as worded. The population, counted by `0.9.0_WK_LGIC_NAMING~4` over LN-f-1's 68 forms: 31 carry a
kind word in the function slot (lambda 18, runner 6, api 5, layer 4, task 1), and they are overwhelmingly roles,
profiles and policies whose function names the SUBJECT they serve:
- `...-lambda-role` is the role a lambda assumes;
- `blackdiamond-49f-runner-role` is the role the runner uses.

That kind word is part of the subject's name. Dropping it makes the name say less, and does not make it more
conformant.

**The ruling:**
- The resource's OWN kind (`kind.by_type` for its type) is never written in its function.
- Another type's kind that names the subject the resource serves is part of that phrase, and stays.
- This is what `GRADING_RULE.md` R6 already does, so FN1 and R6 now say one thing.
- **The 31 forms do not move.** v1.6's sentence "a kind word (queue, host, topic, table, alarm) is never written in the
  function slot" was too wide. It even named `host`, which is in no kind list.

**The word-choice clauses of FN1** (an agent noun describing the resource ITSELF is written as its verb; a phrase is
written as named) **bind the NAMER, who has the item's description.** A grade of an existing name has no description,
so it cannot tell whether `scheduler` in `advi-49f-floor-scheduler-role` describes the resource or names its subject.
The grade therefore keeps a function's words as written, and grades the grammar: slots, spellings and kinds.

Where the namer's and the grade's answers could still differ is a vocabulary choice inside the function. That choice
is made when a remediation renames the resource, by an author who knows what it does (S13). It is not a grade verdict.

**The two mechanical clauses** (FN1b, and the own-kind bar) bind both, because both are read from the name alone.

**Carriers:**
- 1: amended.
- 2: S14 v1.7.
- 4: R5 gains the two mechanical steps. R5's "free vocabulary" gains its reason (the grade has no item description),
  and R6 is unchanged.
- 5: the same two steps.

**How many of the 68 forms change under the two steps** is counted by the cell that re-cuts the rule. It prints the
denominator; this analysis does not predict it.

## 3. FWD-2 -- THE READER, RULED

### RULING DM -- `demo` reads as a firm in every naming slot (`W6-S4`, the class half)

- The seed calls `demo` "a tenant class the doctrine does not define" (`05_IDENTITY_SPINE.md:69`, tick-list row 17).
- The identity REGISTRY, which owns the rows under ruling (a) and now exists (`LGIC_ENFORCE` EN-r-1 @`a925c8a642`),
  defines it: `infra/logic/registry/scopes.json` row `demo` reads `class FIRM`, `tenancy FIRM`, tenant kind `demo`
  (one of `tenant_kinds: client, test, demo`).
- The schema has carried `demo` in `firm_forms` since v1.0.
- So the key's answer for i09 (`demo`) stands, and the reader's `none` came from a briefing that handed it the seed.
- **The registry governs where it and the seed differ.** The schema's `rows_owner` now says so, and its `demo` note
  cites the row.
- The row answers the naming question. Whether `demo` should exist as a tenant at all is not asked here.

### RULING POS -- FWD-2's reader may be told what each position holds (`W6-S4`, the reading half)

- FWD-2 reads "from position alone", and its ACCEPT says "without looking anything up".
- Knowing that position 1 is the system and that the firm, if any, is position 2 is the grammar the outcome tests. It
  is not a lookup of any name.
- A reader who does not know the positions is not reading by position at all.
- So the reader's briefing states the slot order (`resource.grammar`) and the closed firm spellings (`firm_forms`), and
  never the item set or its key.
- i11 (`pathfinder` in the system slot, read as the firm) is exactly the error that knowing the positions prevents.
- **Unchanged:** the one-referent limb (REALIZED), the blind seating, and the canary.

**Carriers:** the N3 cell's fixtures (PRD v1.7), which read "briefed only with the schema and the registry seed" and
now read the schema and the REGISTRY, with the reader's slot-order line.

## 4. THE ROWS, DISPOSITIONED

| row | owner | disposition |
|---|---|---|
| `C-S14` (FWD-1, FN1's clause) | 1.0.0_SA_CTO | RULING FN1b. Schema v1.7; the namers re-run |
| `W6-S4` (FWD-2, demo and position) | 1.0.0_SA_CTO | RULINGS DM and POS. The reader's briefing is corrected; the key is unchanged (i09 `demo`, i11 none); the reader re-runs |
| `W4-S2` (GRADING_RULE vs FN1) | 1.0.0_SA_CTO | RULING FN1c. The 31 forms stand; R5 gains two steps at the recut |
| `W4-S1` (the bd paraphrase) | 2.0.0_SA_COO~G | at the recut: LN-f-1's face states R3 as ADJACENCY to a firm token, never position. No attribution moves |
| `S14` (prd_signoff_lib reads the worktree) | 1.0.0_SA_CTO | IN PROGRESS at this seat. `read_signoff_files` (`:286-296`) lists and opens the working copy, so an uncommitted file is read as a signature. It will read the signoff directory at HEAD for all four callers (status, LIMB 6, the notifier and the stamp), proved on a doctored pair: an uncommitted SIGNED file must not admit, and a committed one must. Broadcast when it lands |
| `S15` (i15's answer in the briefing) | 1.0.0_SA_CTO | RULING EX1. `system.vendor_through_tiers`'s example is now `blackdiamond-cot-build-silver-profile`, which is in no N3 item set. The census found that the schema line was the only rule carrier of the old example (the other hits are exercise records, the decomposition and a census record) |

## 5. THE RECUT -- WHAT `2.0.0_SA_COO~G`'S ONE ISSUANCE CARRIES

Cut only after PRD v1.7's brief half is signed (LIMB 6).
1. **The namers (LN-e-1..LN-e-3) re-run on v1.7.**
   - They are briefed with the schema and the registry.
   - No briefing spells an item's answer: check the item set against every worked example in the schema.
   - `blackdiamond-cot-build-silver-profile` must stay out of the item set.
2. **The reader (LN-e-4/LN-e-5) re-runs.**
   - Its briefing states the slot order and the firm spellings, and reads the registry, not the seed (RULINGS DM and
     POS).
   - The key is unchanged.
3. **The grading rule is re-cut to v1.7** (a cell owning `GRADING_RULE.md`).
   - R5 gains FN1b's subtraction and the own-kind bar, and states why the function's words are kept.
   - The cell prints how many of the 68 forms change, with the denominator.
   - LN-f-1's record re-grades under the new rule only if that count is not zero.
   - `W4-S1`'s adjacency wording lands in the same cut.
4. **Blind seating as decomposition v4 s.0c widened it** (all four blind cells). The standing mechanism is Andrew's
   call (below).

## 6. ACROSS PROJECTS

- **`LGIC_ENFORCE`'s `grade()` carries R5/R6 in code** (`lib/opal_naming.py` `_grade_resource`, R6 at `:980`
  @`828ac108db`).
  - The two v1.7 steps reach it in that project's next cell, not in this project's.
  - `LGIC_ENFORCE`'s round is `2.0.0_SA_COO~G`'s as well, so the carrier is named here, where the recut is cut.
- **`LGIC_ENFORCE` rows `S1` and `S3`**, from msg 96791, go to that project's L10 analysis:
  - S1: to-pipeline-gate's coverage limb, and the override route that never reaches it;
  - S3: owned-paths admits any worker serial on `.tools/` and `data/firm_registry.json`.

## 7. THE GATE, AND WHAT IT CHANGES FOR THIS PROJECT

- **The L10 precondition now reads terminality from the proof-of-spec instance, as the spine does** (`.tools/surprise-row-gate.py`,
  commit `f5a5058146`, merged @`fa6521ea12`).
  - An order in RULING T's shape (a VALID proof whose FAIL is the measurement) no longer holds a slug.
  - RULING T (msg 96793) is kept, but the gate no longer depends on it.
  - Flipping the status word at the drain stays good practice, because other readers read it.
- **The census:** 342 project codes and 2,532 orders; 3 changed, 0 wrongly opened, 0 errors.

## 8. AT ANDREW -- NOTHING NEW

- The clean-context blind-reader seat as a STANDING mechanism is still his, and stays in this seat's open calls.
- Round 2 served it by decomposition, and 4 of 4 canaries read blind.

## PUSH STATE

This document, schema v1.7 and PRD v1.7 are LOCAL at commit. The push state is re-read and stated in the broadcast.
