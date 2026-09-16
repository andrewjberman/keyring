# /self-drive LGIC -- rulings ledger, 1.0.0_SA_CTO, from 2026-09-16

Every adjudicable call in the LGIC scope ruled by this seat under Andrew-direct 2026-09-16 ~05:2xZ ("Run a 30m
/self-drive adjudicate any open calls that arise"; record `ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
@a6e628fb89). One entry per call: the call, the rec, the ruling, the reason, what it binds. Any entry is overturnable by
reading this file. RESERVED calls are not here; they are cards at Andrew.

---

## R-1 (2026-09-16 ~05:5xZ) -- G-V19R lands as a SECOND commit in the CRO's lane, not "in that same merge"

**Call:** `2.0.0_SA_COO~G` 97305 (copied to this seat as adjudicator). `LGIC_CANON_DECOMP.md:125` says the naming-section
render (`python infra/logic/render_naming_section.py --write`) runs "in that same merge" as gate G-V19. It could not:
`.tools/safe-merge.sh`'s `--continue` limb refuses any path the merge itself did not stage, and `infra/logic/02_DOCTRINE.md`
was not in the group branch's staged set. G-V19 landed @4730cec6ca (NAMING_SCHEMA.json v1.9 at HEAD; `firm_forms` gone;
both channels UNION-resolved, 75 of 75 and 50 of 50 shared rows byte-identical). The canon reads STALE at HEAD
(`--check`: 2 failures) until the render commits, and `infra/logic/**` is lane PLATFORM_LOGIC_DOCS (`4.0.0_SA_CRO`), so
safe-commit refused `2.0.0_SA_COO~G` by name and it asked the lane holder rather than take the audited override.

**Rec (COO~G's):** accept the two-commit form for G-V19R and say so in the round analysis.

**Ruling: ACCEPTED.** G-V19R is satisfied by the render committed as a second commit under `4.0.0_SA_CRO`'s author line
(the lane holder), immediately after the merge, with `--check` printing `FRESH -- 0 failure(s)` in that commit's evidence.
The decomposition's "in that same merge" is a WORDING DEFECT in the decomposition, not a criterion the fabric can meet:
the guard that refuses an unstaged path on `--continue` is the guard CLAUDE.md 14b names as correct in every measured
refusal, and a hand-merge to satisfy the sentence would run with no guard at all. The lane refusal is likewise correct
and the override was rightly not taken (`.owned-paths.yaml`'s own text: a repeat override is a coverage gap to close).

**Binds:** (1) `4.0.0_SA_CRO` lands the render + `--check FRESH` + commit of `infra/logic/02_DOCTRINE.md`; nobody else
touches that path for it. (2) `2.0.0_SA_COO~G` records G-V19R as met at that commit's hash, and the LGIC_CANON round-1
ANALYSIS (this seat's, on the CVO's slug) carries the wording correction for `LGIC_CANON_DECOMP.md:125` into round 2's
recut: "in the merge or in the commit immediately following it, in the lane that owns the path". (3) The lost `demo`
note (the renderer's registry path never reads `note`) is a SURPRISE ROW on LGIC_CANON, remedy a LGIC_CANON round-2 cell
-- COO~G's routing is right; this seat does not pre-cut it.

**Blast radius, as measured by the asker and accepted:** one live caller of `--check` (`check_canon_r1.py`, LGIC_CANON's
own round-1 checker); no hook, deploy gate or other script reads it. A record defect with a short window, not a block.

**Grounding:** 97305 (COO~G's measured diff: 3 insertions / 4 deletions in `02_DOCTRINE.md`; `--check` STALE 2 -> FRESH 0
on the group branch); `.owned-paths.yaml` lane PLATFORM_LOGIC_DOCS; CLAUDE.md 14b on safe-merge refusals. This seat did
not re-run the render (the CRO's run in its own commit is the exercised arm; a second run here would be repetition).
**Executed:** `4.0.0_SA_CRO` @783e2f3887; this seat re-ran `--check` at that HEAD: FRESH, 0 failures. RAVC closed (97310).

---

## R-2 (2026-09-16 ~06:0xZ) -- FIRM_FORMS_READERS.md is misplaced; fix the PLACEMENT in round 2, no override; S21 stays ARMED

**Call:** `2.0.0_SA_COO~G` 97312. Row LGIC_ENFORCE-S21's own disarm is an edit to
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FIRM_FORMS_READERS.md`. safe-commit refuses it for EVERY seat: the
file sits directly under `deliverables/` with no serial sub-folder, and lane TREE_DELIVERABLES resolves its owner from
the path (owned-paths-validate.py clause 4), so a file with no serial folder has no owner and NOBODY may commit it. It
was minted there by `0.9.0_WK_LGIC_ENFORCE~1` and reached CLOUD inside the G-V19 merge @4730cec6ca, which is lane-exempt
by design. COO~G's re-measured edit (63 tracked `firm_forms` files MINUS 4 exclusions = 59 owed; 55 listed; 5 unlisted,
not 2; 62 entries after; `org/audit/archive/**` as a prefix exclusion) is made, verified, and REVERTED from the shared
tree pending this ruling; row S22 is held with it.

**Options put:** (a) rule the placement a defect and carry a LGIC_ENFORCE round-2 cell that moves the file to
`deliverables/0.9.0_WK_LGIC_ENFORCE~1/FIRM_FORMS_READERS.md` and re-points R3-AC1/R3-AC9; S21 stays ARMED until then.
(b) one audited `GIT_COMMIT_AUTHOR_OVERRIDE` now, plus (a). COO~G leans (a) alone.

**Ruling: (a) ALONE. No override.** The gate is correct and the artifact is misplaced; the remedy is to give the record an
owner, not to commit past the rule that says it has none. Reasons: (1) a second audited override against this tree in two
days is the shape that turns a singular escape into a de-facto lane, and the lane's own text calls a repeat override a
coverage gap to close; (2) nothing reads the file as code, and both criteria it backs (R3-AC1, R3-AC9) were graded at the
worker's tip 3c42177812 where they PASS, so the stale record blocks no grade and no deploy; (3) S21 reading ARMED until
round 2 is the honest state -- the hazard is real and unfixed, and a disarm bought with an override would read cleaner
than the world is. **Verified before ruling:** at HEAD the path is tracked directly under `deliverables/` with no serial
folder, and COO~G's revert left the tree clean on it (porcelain empty).

⛔ **WIDER THAN THE CALL, measured at ruling time (Rule 22: check what the members share):** `git ls-tree HEAD` on
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/` lists **22 entries, of which 12 are FILES directly under the folder
with no serial sub-folder** -- `CARRIER_CENSUS.md`, `EXERCISE_FWD1_SEARCH.md`, `EXERCISE_FWD2.md`, `EXERCISE_FWD6.md`,
`EXERCISE_FWD7.md`, `FENCE_PLAN.md`, `FENCE_PRIOR_POLICY.json`, `FENCE_PROBES.md`, `FENCE_WRITER_CENSUS.md`,
`FIRM_FORMS_READERS.md`, `NAMING_CENSUS_COMPARISON.md`, `NAMING_CENSUS_REPORT.md` -- beside 9 serial folders and one
COO folder. Every one of the 12 is maintainable by nobody at HEAD for the same reason. FIRM_FORMS_READERS.md is the
one that surfaced because it is the one somebody tried to edit.

**Binds:** (1) `2.0.0_SA_COO~G` carries into the LGIC_ENFORCE round-2 recut ONE cell over the CLASS, not the file: move
every ownerless deliverable under this project (the 12 above, denominator printed in the cell, re-measured at the cut)
into the serial folder of its minting author (read from `git log --format=%an -- <path>`, never guessed), re-point every
criterion and record that cites an old path, and apply the held 62-entry edit to FIRM_FORMS_READERS.md (with the
`org/audit/archive/**` prefix exclusion) in the SAME cell, so S21 and S22 land together under an owner. If any of the 12
has more than one author in its history, the cell names the FIRST minting author and says so. The re-apply script stays in COO~G's scratchpad until then; no uncommitted tracked modification sits in
the shared tree. (2) Row S22 stays HELD until that cell drains; S21 stays ARMED, disarm owner unchanged. (3) CLASS
FINDING, routed not built: a drain merge is lane-exempt, so a worker can mint a deliverable outside its serial folder and
it enters CLOUD with no owner. That is a coverage gap in `owned-paths-validate.py` clause 4's enforcement at the MERGE
step (the drain's refuser reads the merged index for rows, not for deliverable placement). It goes to the LGIC_ENFORCE
round-2 analysis as a finding for the tooling owner; this seat does not add a gate limb on its own read (CLAUDE.md s.2,
no manufactured friction). (4) Nothing else moves: LGIC_CANON-S3 (the renderer's `note` read) lands independently as
COO~G said.

**Grounding:** 97312 (COO~G's measured census and the verbatim refusal text); `git ls-tree HEAD` on the deliverables
folder and `git status --porcelain` on the path at ruling time; CLAUDE.md 14a (the override is singular and audited),
14b (no uncommitted tracked edit left in the shared tree), s.2 (no agent-made gate).

---

## R-3 (2026-09-16 ~06:2xZ) -- LGIC_CANON round-1 ANALYSIS: sixteen rulings A-1..A-16, and the FWD grades

**Call:** the L10 slug, `3.0.0_SA_CVO` 97314 @3ee4bb55ec (16 of 16 rows dispositioned, K1-J1 the one FAIL, two ARMED
rows). The slug hands this seat the FWD grades and six forks (C-S9, W7-S1, W7-S2, W1-S2, W6-S1, W6-S3) plus the
onboarding remedies.

**Ruling:** recorded in full at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND1_ANALYSIS.md` (same commit). Grades:
REALIZED 4 of 6 (FWD-2, FWD-3, FWD-4, FWD-6); SHORT 1 (FWD-1); NOT EVALUATED 1 (FWD-5, held by Andrew's G-N word; its
instrument SHORT). The forks: the canon carries the verdict vocabulary and severity order (A-1); R20 on every axis and
the deciding-rule citation rule (A-2); the key is right, the schema gains the adjacency test (A-3); no axis-domain
widening, X6 placed inside A1-A5 (A-5); LONG sovereign, SHORT derived (A-6); the canon stays on the storage plane, the
sign-in plane gets an LGIC_ENFORCE contract and an R20 entry X8 by the CRO (A-7); a NEW firm mints no legacy served key,
Step 10's STOP names ADVI_FIRMBKTS (A-8); one pipeline-instance rule makes four steps MECHANICAL (A-9). W8-S1's disarm
clock: the two-line advance was made here, passed the row gate, and was REFUSED by lane (TREE_CVO admits the CVO
only) -- no override; reverted; `3.0.0_SA_CVO` lands it on this ruling (A-15), and the disarm-owner-vs-lane mismatch is
a class finding beside R-2's.

**R-3 addendum (~06:3xZ): W8-S1 DISARMED @12eb376681** (`3.0.0_SA_CVO`, lane TREE_CVO, on this seat's act; verified here by
`git diff -U0` on the carrier: exactly two changed lines, owner untouched). **The class finding's mechanical shape, the
CVO's point adopted:** a correctly-routed disarm now has a different author and committer by design, so "who disarmed"
is read ONLY from the row's `disarm.owner` field and never from commit history (the same trap the estate already knows
one level up: author and committer lines cannot say who pushed). Any check that verifies a disarm against commit
authorship reads a mismatch on every correctly-routed disarm. The remedy worth having is a FILING-TIME refusal when a
row's `disarm.owner` names a serial the carrier's lane does not admit -- cheap, at the row gate -- never a widened
grant that lets any disarm owner write any lane's carrier. Routed to the tooling owner with R-2's finding; not built here.

**R-3 addendum 2 (~07:0xZ): X8 LANDED @afb2a631b7** (`4.0.0_SA_CRO`, lane PLATFORM_LOGIC_DOCS; ledger v1.0 -> v1.1;
`ledger_recount.py` RECOUNT: OK, 8 register entries, GRANTED 6, OWED 2, plane counts unchanged; verified here by
`git diff -U0`: one file, the row + the recount + the changelog, nothing else). The four `opal-partner-<LONG>` tables
are a DECLARED, FORCED A3 departure (deciding rule R1), grounded by the CRO at the source: the login path derives the
name at runtime (`partnerTableName()`), and two wildcard `GetItem` grants on one role match it. **KIND = CONDITIONAL,
confirmed by this seat** (the CRO's choice where A-7 named none): the force ends when an R19 project renames the four
tables, re-derives the name in both carriers and re-scopes both grants in one act under never-widen on sign-in; owner
`1.0.0_SA_CTO`. PERMANENT would be false. Two side findings routed by the CRO to LGIC_ENFORCE round 2 and endorsed
here as the LGIC lens's own item (one fact, more than one carrier): the derivation has two byte-identical carriers; the
same grant is declared twice on one role in two Terraform roots. Round 2 is ONE issuance by `2.0.0_SA_COO~G` over the cell table in s.3 of the
analysis; C6 stays NOT CUT.

**Binds:** `2.0.0_SA_COO~G` (the recut); `4.0.0_SA_CRO` (X8); LGIC_NAMING and LGIC_ENFORCE rounds (routes named in the
analysis). No PRD addendum: no outcome was wrong, incomplete or obsolete at this read.

---

## R-4 (2026-09-16 ~06:3xZ) -- LGIC_LGCTFM placed in SEQUENCE.yaml stage 1, fourth of the Platform Logic projects

**Call:** `2.0.0_SA_COO~G` 97315 (its "R-3"): LGIC_LGCTFM is a D14 register member and the sequence did not list it, so
a goal loop driving "in the sequence's order" drove a set the sequence did not contain. COO~G's rec: place it in stage 1
with `waits_on` naming what its L4 needs; the narrow alternative, place it at L4-R admission and record the absence as
deliberate.

**Ruling: PLACED NOW, stage 1, `waits_on` the three D14 PRDs admitted** (LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON -- all
met at placement, so nothing waits; brief IV.1 and IV.4 make the dependency real: the DESIRED half is the builders'
output against the schema, graded against the canon). Last of the four for a COO seat, behind the three on `~G`. Not the
narrow version: the goal loops read the file every tick and an unplaced member reads as "nobody noticed", which is the
defect COO~G named. Authority: this is a PLACEMENT of a new member, not a change to any existing order; Andrew's ~05:2xZ
word names the four together and is quoted in the change_log. The stage-2 rows' consumer relation (ADVI_FIRMBKTS and
MDPF_CANON read the run's plan at L5) is a note on THEIR rows when their L5 cuts the cell, never a gate here.

**Binds:** nothing new; `2.0.0_SA_COO~G`'s loop now covers 4 of 4 placed. Verified: `sequence-check.py --project
LGIC_LGCTFM` PLACED, stage 1, flags 0.

---

## R-5 (2026-09-16 ~07:2xZ) -- the naming suite is RED at HEAD because two correct cells met; re-verdict the two `globgrph` worked cases from the builder, as a LGIC_NAMING round-5 cell

**Call:** `2.0.0_SA_COO~G` 97330, row LGIC_NAMING-S22 @68644b3c19 (BLOCKING, disarm owner this seat).
`lib/tests/test_opal_naming.py` reads 80 passed, 2 failed at HEAD -- **re-run here: `2 failed, 80 passed`**, the same two
(`test_grade_agrees_with_every_worked_case[globgrph-serving|ECS_TASK_DEFINITION]` and `[opal-globgrph|ECS_CLUSTER]`,
each DID NOT RAISE). Cause, as COO~G measured and this seat confirmed at the artifacts: the two worked cases in
`GRADING_RULE.md` (:436, :439) assert RAISE and their own `why` says *"the registry row is owed (row LGIC_NAMING-W1-S2)"*;
LGIC_ENFORCE EN-r-2 (@72d636db4f, drained @901f48b1e0) minted that row -- `systems.json` now carries `globgrph` as a
PLATFORM_SUBSYSTEM (long `global-graph`, basis NFRA_GLOBGRPH PRD/roadmap, `infra/aws/globgrph/`, ECS cluster
`opal-globgrph`) -- and EN-r-2's own R2-AC4 requires every class (a) example to STOP raising. LN-g-2 read 82 of 82 at its
tip; EN-r-2 read 6 of 6 at its. The red exists only where the two land together, and no criterion of either grades there.
A worked case encoded a REGISTRY STATE as a CODE assertion, and the registry moved.

**Measured here at HEAD, registry_hash cb431dc8c5..:** `grade('globgrph-serving','ECS_TASK_DEFINITION')` ->
`('OUT-OF-PATTERN', 'globgrph-serving-task')`; `grade('opal-globgrph','ECS_CLUSTER')` -> `('OUT-OF-PATTERN',
'globgrph-cluster')`. So the rule now PLACES both names (the subsystem is a system; `opal` is a null prefix under R2; the
task needs its type suffix under R1.c) and the builder produces the canonical forms.

**Ruling: (a), COO~G's rec.** The registration stands -- it is what the worked cases' own text said should exist, and
the registry row's basis names the PRD, the roadmap, the infra directory and the cluster. **One LGIC_NAMING round-5
cell** re-verdicts the two worked cases FROM THE BUILDER'S OUTPUT at the registry hash (verdict OUT-OF-PATTERN, canonical
`globgrph-serving-task` and `globgrph-cluster`, `why` re-worded to name the systems.json row and the rules that now
decide: R2 null prefix, R1.c type suffix), re-runs the suite to 82 of 82 with `--color=no`, and disarms S22 in the same
drain. **No test is edited to match the code; the RULE is re-verdicted and the tests follow it**, which is the order
COO~G rightly refused to invert. Both orders stay `complete` and correct as written; nothing is re-cut.

**Two things this ruling adds.** (1) CLASS, for the same cell: a worked case whose verdict depends on REGISTRY STATE
carries the `registry_hash` it was measured at, so a registry change re-opens it as a loud STALE-CASE rather than a
red test two cells apart -- the same shape as the canon's schema stamp (`--check`). The round-5 cell states whether it
adds the field to the worked-case schema (a Rule 24 act, with its record) or defers it; either is acceptable, silence is
not. (2) The suite is RED until that cell drains: any cell in any LGIC project that takes a green suite as a base
condition RE-MEASURES; LGIC_CANON round 2's cells do not touch the module (COO~G's read, accepted).

**Instrument finding, COO~G's own, endorsed:** `check_ln_r4.py`'s `g2_suite` regex was ANSI-blind and read a FALSE PASS
while tests failed -- the one direction a grading checker must never fail in. Fixed belt-and-braces @68644b3c19
(`--color=no` and an ANSI strip). The worker `0.9.0_WK_LGIC_NAMING~2` caught it with its own mutant control (W2-S8), which
is the control working as designed.

**Binds:** `2.0.0_SA_COO~G` -- the round-5 cell as above; S22's disarm rides its drain. Nothing at the CVO until L9.

---

## R-6 (2026-09-16 ~07:3xZ) -- the six UNDECIDED registry tokens EN-r-2 routed to this seat: one RETIRED on Andrew's card, one a project code, four measured live and owed a cell, not a guess

**Call:** LGIC_ENFORCE EN-r-2 (drained @901f48b1e0; result `registry-rows.r2.result.md` item 6) left `astn`, `trade`,
`news`, `find`, `harvest`, `imo` under `systems.json` `unresolved` "for 1.0.0_SA_CTO". The registry's own contract
(`_about.row_fields`): a SYSTEM row needs `class` (PRODUCT | VENDOR | PLATFORM_SUBSYSTEM), `owner_directive` resolving
in DIRECTIVES.yaml, and `owner_claim` measured or inferred WITH a basis. **Measured before ruling:**
- `imo`: tick-list row 18 (`opal-data-imo`, 304 per-company planes, 103d dead at census) was RESOLVED by Andrew's
  card 9 as RETIRE (`04_SCOPE_TICKLIST.md:15`, `:66`); bucket first page of 1000 objects, newest on that page
  2026-06-01 (`IsTruncated` true; not a bucket-wide max, and not needed: his card decides).
- `harvest`: `opal-data-harvest` 132 objects, newest `social/v1/_measurement/2026-09-15.json` at 2026-09-15T16:56Z --
  LIVE, written the previous day. Not row 18's object.
- `find`: FIND is a legacy macro/project code (FIND_INSURE .001-.029 orders under `0.7.0_AE_CloudOps`; `data/find/`),
  not a MACROS.yaml macro; 21 live resource names carry it (census s.3 V1).
- `astn` 14, `news` 34, `trade` 22 live resource names (census s.3 V1, "PRODUCTS and VENDORS/FEEDS"); none has a
  DIRECTIVES.yaml line or a mission-tree project naming an owner (W1-S6, as EN-r-2 found). `trade` is plausibly the
  TRADEOPS second fabric's product (its own root and broker), i.e. possibly not this register's row at all.

**Ruling, per token:**
1. **`imo` -- RETIRED**, on Andrew's card 9. Not a system. Mechanism: the LGIC_ENFORCE round-2 registry cell adds a
   `refused_keys.retired` class (its Rule 24 record travels with it: axis = a token Andrew retired by card; disjoint from
   workstream_code / generic_noun / purpose_word; one intent), `imo` its first member, basis the tick-list row and card 9.
   Its resources grade as class (d) rule gaps until the R19 retirement project removes them -- loud, as designed.
2. **`find` -- REFUSED as a project code** (`refused_keys.workstream_code`; V3: a project code is never a system), basis
   the FIND_* orders and `data/find/`. Its 21 resources become class (d) gaps that the insurance-prospecting product's
   owner resolves, not the naming rule.
3. **`harvest`, `astn`, `news`, `trade` -- PRODUCT-shaped and LIVE; the OWNER is MEASURED by a cell, never inferred
   here.** The same LGIC_ENFORCE round-2 registry cell reads, per token, its live resources' DECLARED sources
   (`lambda-source-map.json` `source_dir`/`tf_file`, `EC2_MANIFEST.json` `source_path`, the repo tree the resources
   deploy from, and for `trade` the tradeops root) and mints a PRODUCT row with `owner_claim: inferred` and the
   citation as `owner_basis` where the tree links to a directive or a mission-tree project. A token whose resources
   link to NO directive stays `unresolved` with the MEASURED fact written into its `why`, and the cell returns ONE card
   to Andrew naming the owner question per such token. `trade` whose resources deploy from the tradeops root is that
   fabric's row and is recorded as such, not minted here.
   This seat does not write the four owners from recall: an inferred owner without a citation is the guess the
   registry's `owner_claim` field exists to refuse.

**Why not a card at Andrew now:** no NEVER line or standing hold names the class; the delegation makes it adjudicable,
and three of the four have a measurable answer in the declared planes. The cell's residue, if any, is the card.
**Binds:** `2.0.0_SA_COO~G` -- one registry cell in LGIC_ENFORCE round 2 carrying items 1-3 (the EN-s-1 census stays
STOPPED on class (d) meanwhile, as decomposition v2 s.0b rules). Nothing at Andrew unless the cell's measurement leaves a
token ownerless. **Amended by R-7: the cell is ROUND 3's, not round 2's.**

---

## R-7 (2026-09-16 ~07:4xZ) -- R-6's registry cell has no room in LGIC_ENFORCE round 2; it is a ROUND-3 cell, not an amendment to EN-r-4

**Call:** `2.0.0_SA_COO~G` 97333. LGIC_ENFORCE round 2's issuance is CLOSED (one issuance of 12 orders @4f9a9eb3f3, drained
@adc8d93cd1); the spine's L6 rule is ONE issuance per round. R-6's three items are `systems.json` tokens and
`refused_keys` classes; EN-r-2 is COMPLETE with its grant withdrawn, and EN-r-4 (unspawned) writes `resources.json`
only. Options: (a) a round-3 cell, at the cost of waiting for round 2's L10; (b) amend EN-r-4's `<paths>` and cell text
before it spawns; (c) a thirteenth order under an audited override. COO~G leans (b) because EN-r-4 is unspawned and
holds its spawn pending this ruling.

**Ruling: (a). A ROUND-3 CELL.** Reasons: (1) Rule 27 freezes the spec AND the decomposition mid-round; R-6's items are
NEW WORK (a new refused class is a Rule 24 act; new system rows are new rows), and adding new work to an order is cutting
a cell the decomposition does not name -- which is the act the freeze forbids, whether it arrives as a thirteenth order
or inside EN-r-4's text. The precedent COO~G cites (TX-g-1's `<paths>`, TX-p-1's AC10) amended a cell's OWN scope to what
it already meant; it did not add a second cell's work. (2) An issuance that no longer matches its decomposition makes
the L8/L10 reads grade EN-r-4 against a cell that does not describe it. (3) Nothing waits: COO~G measured that the
`imo`/`find` items are not urgent and the four owners gate nothing; the EN-s-1 census is STOPPED on class (d) regardless.
(c) is refused for the reason COO~G gave -- an override would record the COO's judgment where the spine wants the CTO's
analysis. **EN-r-4 spawns as written, now.**

**Binds:** `2.0.0_SA_COO~G` -- spawn EN-r-4 unamended; carry R-6's three items into this seat's LGIC_ENFORCE ROUND-2
ANALYSIS at L10, whence the round-3 recut cuts the registry cell. R-6's substance is unchanged.

**Capacity, endorsed as COO~G's own judgment:** three concurrent workers rather than four while disk reads 19 GB and each
worktree costs ~2 GB, after last night's slowness wind-down. Not a constraint this seat sets; COO~G raises it if the
box allows.

---

## R-8 (2026-09-16 ~08:0xZ) -- CN-j-6's negative arm: what is WITHHELD from judge E is the BRIEF's scale; the CANON is where E is meant to find it

**Call:** `2.0.0_SA_COO~G` 97335, row LGIC_CANON-S6 @225e7e52b5 (BLOCKING, disarm owner this seat), caught before spawn
(CN-j-6 HELD). CN-j-6 judges "WITHOUT the severity order" and `depends_on: CN-k-2`, whose item 2 writes the severity
order INTO the canon CN-j-6 reads unpinned. Two readings: (1) E must meet no severity order anywhere, so the dependency
is backwards and E needs a canon pinned before CN-k-2; (2) what is withheld is a BRIEF stating the scale, and the canon
is precisely where E should find it. COO~G's rec: (2). Not edited, on R-7's line.

**Ruling: (2), and it is what A-1 already said.** The round-1 analysis (A-1) ordered "a third judge briefed WITHOUT
the severity order, AFTER the canon carries it" -- the negative arm's question is whether the CANON, alone, now supplies
the verdict vocabulary and order that the round-1 ORDERS supplied (C-S9). Reading (1) would pin E to a canon that does
not carry it and would measure nothing about CN-k-2. So: the dependency on CN-k-2 is right; the warning text is wrong.

**Binds `2.0.0_SA_COO~G`, as a CORRECTION of the cell's own instruction, not new work (the R-7 line):** (a) CN-j-6's
warning reads that the canon is where the scale legitimately lives and what is withheld is any brief, order text or
example stating it; the surprise-row guard covers a scale met in a file the order does NOT name. (b) The criterion
`j6-noseverity` states plainly that it grades the BRIEF (the order file carries no scale), and the cell's bar gains the
measurement the negative arm exists for, graded at CN-j-7 (the comparison), not self-graded: every verdict value in E's
output OCCURS in `02_DOCTRINE.md` at the HEAD E read (whole-word census, denominator printed), and E's per-axis severity
choices agree with the canon's stated order. E agreeing with C and D on that basis is the evidence that CN-k-2 made the
canon carry what the brief used to supply; E disagreeing on a value the canon does not carry is the finding. (c) No
vintage pin: E reads the canon at HEAD after CN-k-2 drains, which is the state the arm tests.

**Method note, COO~G's, kept:** the write-surface census over the RUNNING and HELD sets surfaced a defect that was not
about contention, by asking WHY each hold's dependency exists. Worth repeating at every issuance.

---

## R-9 (2026-09-16 ~09:5xZ) -- the negative arm could not discriminate; the vocabulary result stands AS a vocabulary result, C-S9 stays open, S6 stays ARMED, round 3 carries a roll-up cell

**Call:** `2.0.0_SA_COO~G` 97340, reporting against its own cut after CN-j-7 drained @2bc14e52f8 (4 of 4 PASS). Two
measured reasons the arm as cut could only return "no divergence": (1) C and D judged the INFLECTION tree and E judged
the MDPF tree -- plane intersection E∩C = 0, E∩D = 0 against a positive control C∩D = 13 of 13 -- so the comparison
the cell asked for ran over an empty intersection (the worker fell back to round 1's judges on the shared tree, 5 of 5
on AXES; COO~G's own first read of that as contradicted was a grain error it caught and reported); (2) round 2's
per-plane grain never forced a most-severe roll-up, so no judge ranked anything -- whole-word census of ranking language:
judges C, D, E all 0, the canon 5 -- and the brief's presence or absence therefore separated nothing observable. J7-AC4
(added under R-8) measured that E's four verdict VALUES occur in the canon (4 of 4): true, useful, and not the ORDER
question. Options: (a) accept the arm as vocabulary-only, keep C-S9 open, S6 stays ARMED, round 3 cuts a cell that
demands a roll-up; (b) accept it as answering C-S9 and disarm S6; (c) other. COO~G's rec: (a).

**Ruling: (a).** Rule 22, DISCRIMINATION: evidence that could not differ if the claim were false is not evidence, and
COO~G measured both ways it could not differ. R-8(c)'s "S6 disarms at CN-j-7's drain on that measurement" is
WITHDRAWN: the measurement it named (vocabulary in the canon) is real and is recorded, but it is not the arm's
question, so it disarms nothing. **What stands from round 2, unweakened:** C vs D at 59 of 65 axis cells identical,
every split adjacent on the canon's own severity order and traced to four canon coordinates (R10 vs R9 monolith
clearance `:414-419`/`:405-406`; R1 key grammar vs plane clearance `:149-152`/`:171`; R6 vs R5 on inflection's
bucket `:364-365`/`:354-357`; R18/R19 duration and in-flight status `:516-531`) -- those four are round-3 canon edits.
Reach 7 of 7 agreed; the second tree bought exactly one new rule (R17), so C-S10's seven-rule target is not met either
and round 3's tree choice must say which of the remaining six it reaches.

**Binds `2.0.0_SA_COO~G`, all after the L10 slug and this seat's round-2 analysis (LD-0521):** round 3 carries (i) ONE
tree judged by every arm -- briefed judges and an unbriefed judge on the SAME planes -- each judge REQUIRED to name the
single most-severe finding per plane and its rule, so an ORDER is exercised and the arms can diverge; (ii) the
comparison cell tests the roll-up, not the vocabulary; (iii) the four canon coordinates above as a canon cell; (iv) a
tree chosen to reach the six rules still unexercised (R3, R8, R14, R15, R19, R21 less R17 now reached). S6 disarms at
(ii)'s drain if the arms could have diverged and did not. **COO~G's own grain error (plane-keyed vs axis-keyed) and its
fifth instance of a check whose name promises what its body does not read (`k3-contentdiff` planting nothing) are
recorded as the round's instrument findings; the worker rows carry them.**

---

## R-10 (2026-09-16 ~10:1xZ) -- CN-k-4 cannot complete inside LGIC_CANON round 2; the issuer WITHDRAWS it, round 2 closes on nine cells, the obligation is re-cut in round 3 behind LGIC_NAMING's schema edit

**Call:** `2.0.0_SA_COO~G` 97343, row LGIC_CANON-S11 @f8eb631fa8. Round 2: eight cells complete, CN-o-4 running, CN-k-4
never spawned. CN-k-4's own text conditions K4-AC1 on `NAMING_SCHEMA.json` carrying the `bd` adjacency test that A-3
routed to LGIC_NAMING; measured at HEAD by two instruments (comp-find 0 of 1 file; a structural read of the parsed
schema, 271 paths, 0 matching `adjacen`, the 9 `bd` paths all Lambda type entries or `/refused_tokens/bd`) the schema
does not carry it, and LGIC_NAMING round 5 -- where A-3's edit lives -- is cut only after round 4's slug and this seat's
round-4 analysis (LD-0521). So round 2's slug (every order terminal) waits on a cross-project round that waits on a slug
that waits on this seat. COO~G also narrowed the set by CALLING `_proof_terminal`: EN-s-1 (2 FAIL on a VALID proof) reads
terminal-by-proof TRUE, so LGIC_ENFORCE's slug is not blocked; CN-k-4 (no instance) and CN-o-4 (running) read FALSE.
Options: (a) carry CN-k-4 out of round 2; (b) hold round 2's slug until LGIC_NAMING round 5; (c) other. Rec (a), weakly.

**Ruling: (a), by WITHDRAWAL, and it is not weak.** The gate's terminal vocabulary at `surprise-row-gate.py:142`
(`TERMINAL_TO_WORDS`) admits `withdrawn`, and `:122` names it as the issuer's own state for exactly this shape. So the
mechanism is: `2.0.0_SA_COO~G` flips CN-k-4's `<status>` to `withdrawn` with a status note citing row S11 and this
ruling, stating verbatim that the obligation (re-render the canon after the schema carries the adjacency test; K4-AC1
as cut) is carried unmet into round 3 as a cell depending on LGIC_NAMING round 5's schema cell (a cross-project READ
dependency, disclosed on the cell). Round 2 closes on its nine cells the moment CN-o-4 drains. **Why not (b):** holding
nine finished cells on a round of another project is the LD-0521 deadlock class moved one project over; the slug's
"every order terminal" is a rule about what the round can still do, not a device for waiting on what it cannot.
**Why not a spawn to record the FAIL:** two reads with a printed denominator are the record; a worker, a worktree and
1.5 GB to reproduce a result both instruments already carry is repetition (Rule 22), not measurement. **What this does
NOT do:** it does not edit the decomposition mid-round (the recut is the round-2 analysis's, on the slug); it does not
weaken CN-k-4's obligation -- the canon and the schema may disagree at HEAD until round 3 lands it, and the analysis
says so in terms.

**Also recorded from 97343:** CN-o-3's worker READ X8 rather than citing it and found a new firm is not among the four
named tables, so Step 14 STOPs on X8's owner (this seat) extending the entry -- the correct read, and an R20 extension
this seat owes when a new firm is onboarded, not before. S3 DISARMED @44d4942227 (the demo note is back in the canon,
verified on the served artifact). The base-serial authorship of the four merges (this seat's FYI) is answered as row
LGIC_ENFORCE-S25 @d173e700f7: typed by the issuer, not a tool drop -- and the class is worth keeping: **a gate that
refuses on one path and is exempt on another teaches the correct value only where it bites.** Corrected from
@99c34fb574; the four stand.

**Binds:** `2.0.0_SA_COO~G` -- withdraw CN-k-4 as above; slug round 2 on nine cells when CN-o-4 drains. This seat -- the
round-2 analysis carries the CN-k-4 obligation into round 3 explicitly, ordered after LGIC_NAMING round 5's schema
cell; the round-4 LGIC_NAMING analysis (on the CVO's slug) carries A-3's schema edit as a round-5 cell so the chain has
one owner per link.

---

## R-11 (2026-09-16 ~11:2xZ) -- the naming gate grades PATH CITATIONS as if they were NAME MINTS; a value that resolves to an existing repo path is a citation and is never graded, in any file

**Call:** `2.0.0_SA_COO~G` 97346, relaying row LGIC_ENFORCE-W5-S6 with every leg re-read at HEAD: `.tools/naming-gate.py:78`
grades `.json` (`GRADED_EXT`), `:751` returns early only on other extensions; nothing excludes `org/missions/**` (the
one hit at `:621` is a regex extracting a register path); `PROOF_OF_SPEC.schema.json` REQUIRES `spec_ref.doc`,
`decomp_ref.to_ref` and siblings, which are repo paths that carry the task order's filename. The worker's
discriminating pair: the same patch reads `WARN 3 graded` in the WARN window and `REFUSE 3 graded`, rc 1, under
`--enforce`, the three verdicts drawn by nothing but the instance citing its own order `...fwd7-demo-firm.md` (the token
`demo`). So LGIC_ENFORCE's own endpoint -- closing the WARN window -- would refuse the proof-of-spec records every
project writes, including its own. Options: (a) exclude `org/missions/**` from grading; (b) exempt the schema-required
citation fields; (c) bind the issuer to gated-token-free filenames; (d) other. Rec (b), narrowly.

**Ruling: (b) GENERALIZED, which is (d).** The distinction the gate is missing is not a field or a tree; it is
CITATION versus MINT. A string that RESOLVES to an existing repository path at the graded commit is a citation of a
thing that already exists -- a filename, an order, a doc, a decomposition -- and a citation is never the act of naming a
resource. The gate therefore does not grade any token inside a value that resolves to a tracked path at HEAD, in ANY
graded file, with a NEGATIVE CONTROL that a path-shaped value which does NOT resolve (a typo, a made-up file) is still
graded and still refuses. That rule needs no per-field list (which goes stale the day a second schema carries a
citation -- the census-every-carrier class) and no tree exclusion (which would silence real names in project rows).
(a) is refused as too wide; (c) is refused because a cell about `demo` legitimately names `demo` in its order, and a
record that may not cite the thing it is about is a worse record than the one the gate would refuse.

**Binds:** (1) `2.0.0_SA_COO~G` -- LGIC_ENFORCE ROUND-3 cell: the resolvable-path exemption in `naming-gate.py`,
with its Rule 24 record (the axis: what a graded value IS -- a mint or a citation; MECE by resolution at HEAD), the
worker's pair as the positive arm and the non-resolving path as the negative arm, and the estate's own proof-of-spec
instances re-graded under `--enforce` as the exercised arm (every instance that landed this round must pass). (2) The
ENFORCE flip is BOUND to that cell: the WARN window stays until it drains, and this seat's round-2 analysis states it as
the FWD condition it is. (3) Nothing held; EN-x-1 runs on; the WARN window is live.

**Also from 97346:** LGIC_ENFORCE round 2 at 11 of 12 terminal; LGIC_CANON round 2 CLOSED and with `3.0.0_SA_CVO` since
10:33Z; S31 held in practice (the ten-path overlap was a false contention, tested at the drain); S32 corrects COO~G's
own armed count from 26 filed to 14 open -- the filed count is not the live one, and `hazard_standing` is frozen by
the append-only rule, so the live figure is read from the remediation carrier's `disarm.state`.

**CORRECTION (~11:3xZ, COO~G 97348, row LGIC_ENFORCE-S33): the figure this seat accepted above as "the right read" was
wrong again, and this seat accepted it without enumerating the carriers.** There are FOUR carriers that can close an
armed row, not two: the remediation carrier's structured `disarm` block (8), a disarm ROW filed this session (4), the
task order's own `<status>` note (1 -- never consulted before), and another row's `adjudicates` list (10). And the
fourth carrier's PRESENCE is not a closure: of its ten, six are DISMISSED_WITH_REASON and closed, four are GRADUATED
into a remediation row whose own `disarm` still reads ARMED -- **GRADUATED is a transfer, not an ending.** Live open
count: **8** (four still-armed graduates plus S21, W1-S23, W1-S24, W5-S6 that no carrier disposes). The sequence is the
finding: 26 on one carrier, 14 on two, 4 on four, 8 once each carrier's VERDICT is read rather than its presence --
and S32 was filed AS a correction and was itself out by two. **The durable rule, adopted for this seat's round
analyses: when an item can be closed by several documents, ENUMERATE THE CARRIERS FIRST, then read each one's
VERDICT; a carrier's presence certifies nothing.** COO~G does not claim four is the complete set; the last three
passes each found one more. This seat's own R-3 addendum on W8-S1 read only the remediation carrier and stands only
because that row has one carrier by construction.

---

## R-12 (2026-09-16 ~11:4xZ) -- R-2's placement cell was never cut because R-2 named a round already closed; the population is 17, not 12; ONE round-3 cell moves all of them, and the issuer's cut reads open rulings before it writes `<paths>`

**Call:** `2.0.0_SA_COO~G` 97350, row LGIC_ENFORCE-S35 @de773e6b70. R-2 bound "one LGIC_ENFORCE round-2 cell" to move the
ownerless deliverables; no such cell exists over the project's 34 orders (three single-term searches 0 of 34, and the
decisive read is the population itself). Counted by GIT OBJECT TYPE at HEAD (an `ls-tree --name-only` read counts
folders as files -- COO~G's first pass read 26): **17 blobs, 9 trees** directly under `deliverables/`; R-2 measured 12.
Four of the five additions are COO~G's own, cut today with `<paths>` naming a flat location, after R-2 had named the
shape as the defect. It also strands LGIC_ENFORCE-S21, whose one-line disarm edit is to the still-flat, still-refused
file. Options: (a) a round-3 cell moving all 17 into their authoring serial's folder; (b) rule the flat shape fine, withdraw
R-2, widen the lane grant; (c) other. Rec (a), plus an issuance-time check that reads open rulings against a new order's
`<paths>`.

**Owned first:** R-2 (~06:0xZ) named a ROUND-2 cell for a project whose round-2 issuance had closed at @4f9a9eb3f3 the
day before -- the same impossibility R-7 later found in R-6's binding. R-2's remedy was right and its round was wrong;
this ruling corrects the round, not the remedy.

**Ruling: (a).** ONE LGIC_ENFORCE ROUND-3 cell: re-measure the population at the cut BY OBJECT TYPE (`git ls-tree` with
types, blobs only, denominator printed), move every ownerless blob into its FIRST minting author's serial folder (read
from `git log --diff-filter=A --format=%an`, never guessed), re-point every record and criterion that cites an old path,
apply the held 62-entry FIRM_FORMS_READERS.md edit and S21's one-line edit in the same drain, and disarm S21 and S22
there. (b) is refused: a flat deliverable has no owner under clause 4 by construction, and widening the lane grant would
make every seat an owner of every record, which is no owner at all. **COO~G's addition is endorsed as COO~G's own L6
build, not a gate this seat installs:** at issuance, read the OPEN rulings against the `<paths>` a new order declares
and refuse to cut a path into a population a ruling has ordered moved. The durable rule it carries into this seat's
analyses: **a ruling about a POPULATION binds the next cut only if the cut READS it.** Until that check exists, (a)
fixes 17 files and the eighteenth arrives next round, as COO~G said.

**Also recorded:** W1-S23 disarmed BY SUPERSESSION not repair (S34): `blind_seat.py` and `check_ln_r3.py` still read
`firm_forms`, and `.get("firm_forms", [])` under v1.9 returns an EMPTY LIST so every firm-forms-scoped check passes
VACUOUSLY -- the silent arm survives in the bytes; anyone reusing those files needs one assert. That is the
empty-set-passes-vacuously class and it rides the round-2 analysis as a note on the round-3 instrument cells. COO~G's
open armed rows: 7, three of them carrying CTO-owned remediations (W1-S19, W1-S22, W3-S8) that this seat's round-2
analysis must dispose or route.

**Binds:** `2.0.0_SA_COO~G` -- the round-3 cell as above, after the L10 slug and this seat's round-2 analysis (LD-0521);
its issuance-time rulings check whenever it lands. This seat -- the round-2 analysis carries R-2/R-12, R-6/R-7 and
R-11's cells into the round-3 recut as ONE list with one owner per link.

---

## R-13 (2026-09-16 ~11:5xZ) -- R-11 AMENDED on new evidence: the naming gate grades DECLARATION trees and never RECORD trees; the resolvable-path exemption stays as the rule INSIDE declaration trees

**Call:** `2.0.0_SA_COO~G` 97352, row LGIC_ENFORCE-W4-S4, from EN-x-1's drain @8952363e02 (**LGIC_ENFORCE round 2 is
12 of 12 TERMINAL**). A second instance of R-11's class that R-11's remedy does not reach: the graded value is
`advi-49f-fwd2-exercise-queue`, an SQS NAME quoted verbatim in a proof instance's `output_evidence` because the
criterion's SUBJECT is that name moving from `49f` to `f49` -- a proof of a name change cannot be recorded without the
pre-change name. `git ls-files --error-unmatch` on it is non-zero: it is not a path, so R-11's exemption leaves it graded
and, under `--enforce`, refusing; the cell could not be proved at all. **The discriminator the worker found:** the SAME
literal sits in `EXERCISE_FWD2_R2.md` and is never graded, because `naming-gate.py:78` has no `.md` in `GRADED_EXT` and
`:751` early-returns -- so the refusal is driven by the record's FILE SUFFIX, not by what the value is. COO~G's rec:
widen the exemption to "a value inside a field the schema marks EVIDENCE or CITATION", path-resolution kept as one
sufficient condition; COO~G's own doubt: that is the per-field list R-11 refused, and W4-S4 is the strongest argument
yet for its original (a).

**Ruling: R-11 is AMENDED, and this seat's refusal of (a) is REVERSED on this new empirical evidence** (prompt.md:
a reversal needs new evidence, not a re-read; W4-S4 and the suffix discriminator are new). R-11's axis -- CITATION
versus MINT -- was right; its operationalisation by path resolution covered only the citations that happen to be
paths. The operationalisation that covers the class is BY TREE: **a resource is MINTED where the applied plane is
DECLARED (Terraform, code, the registry, the schema), and never in a RECORD (a proof instance, a task order, a
deliverable, a surprise row, a log, a PRD, a project row). The gate grades DECLARATION TREES and does not open RECORD
TREES at all, regardless of suffix.** The declaration set is written BY SUBTRACTION (Rule 24): the graded corpus minus
the record trees `org/**` and `docs/**`, printed as a denominator by the gate on every run, so a tree added later
cannot silently fall on the wrong side. This seat's earlier objection to (a) -- "project rows carry real names" --
was wrong on inspection: a project row's `name` is a title and its prose cites buckets that exist; nothing under
`org/` declares a resource, by Rule 30's own construction (every address is builder output, minted where infrastructure
is declared). R-11's resolvable-path exemption STAYS as the rule inside declaration trees (a `.py` string holding a doc
path is a citation there too). **Negative controls, both required in the cell:** the same literal placed in a `.tf`
resource `name` or a `.py` name constructor still REFUSES; a path-shaped string in a declaration tree that does not
resolve still REFUSES. **Positive controls:** W5-S6's instance and W4-S4's instance both land under `--enforce`, and every
proof-of-spec instance that landed in rounds 1-2 re-grades clean.

**Binds:** `2.0.0_SA_COO~G` -- R-11's round-3 cell is re-scoped to this: the tree axis with its subtraction-printed
denominator, the path exemption retained inside declaration trees, the four controls above, and the ENFORCE flip bound
to its drain as before. No per-field list, no schema edit. This seat -- the round-2 analysis states R-11/R-13 as ONE
cell and records the reversal in terms.

**Also from 97352, kept for the analysis:** what EN-x-1 established that round 1 could not reach -- ONE hand edit to
`scopes.json` (49financial `short` `49f` -> `f49`) moved the queue's name, the generated fence pattern AND the live
bucket policy's `DenyForeignFirmPrincipals` statement (`role/*-49f-*` -> `role/*-f49-*`, every other principal
byte-identical), on two read-only plans against the real backend with nothing applied -- FWD-2's exercised arm for
LGIC_ENFORCE. And W4-S3: a roots-census lock-file count is comparable only across cells that print their init flags
beside it (COO~G's own briefing corrected by its worker's measurement).

---

## R-14 (2026-09-16 ~12:0xZ) -- an issuer's disarm row is EVIDENCE for L9, never a clock; `hazard_standing` is answered by the remediation carrier's `disarm` block alone; the link is the existing evidence citation, not a new field

**Call:** `2.0.0_SA_COO~G` 97357, row LGIC_ENFORCE-S36 @d2a14c0ae5. Over the 9 disarm rows COO~G filed today (both
projects), **0 of 9 carry any structured field naming the target** (`adjudicates`, `resolves`, `disarms`, `target`,
`outcome_ref`), and one names its target by bare `S26`. This is the root cause of the 26 -> 14 -> 4 -> 8 sequence: the
issuer's own counter re-reported eight rows it had disarmed as OPEN because the disposals are not machine-findable.
S13's census stands: `adjudicates` is the CVO's instrument (38 of 39 carriers are the CVO's; the one exception is a
worker disposing its own row, n=1). Options: (a) a new issuer-owned `disarms: [<id>]` field -- a closed-schema change,
worth it only if something consumes it; (b) permit `adjudicates` on a row disposing the author's own prior row; (c)
rule that an issuer's disarm is EVIDENCE ONLY and `hazard_standing` is answered solely by the CVO's remediation
carrier. Rec (a) with the caveat that (c) is the honest answer if nothing will read the field.

**Ruling: (c), and it is what the estate already built.** The disarm CLOCK lives on the remediation row's `disarm`
block (`_monotone_advance`, A-15): the CVO writes the row at L9 with `disarm.state ARMED`, and the disarm OWNER
advances it to DISARMED -- landed in the CVO's lane on the owner's word where the lane refuses the owner. That is the
one carrier with a consumer (the gate's resolver and the L9 pass). An issuer's mid-round disarm row is EVIDENCE that
the hazard is dead, which the CVO reads when it graduates the item and the owner acts on when it advances the clock;
it never closes anything by itself, which is exactly the doctrine "a disarm in prose disposes nothing" and the
open-counter measurement agree on. (a) is refused: `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md` -- a provenance
field nothing consumes drifts to unpopulated, and no consumer is named. (b) is refused: the graded party writing the
field that closes the round's items is the boundary-in-the-graded-party's-hand shape COO~G itself declined.

**The machine-readable link, without a schema change:** an issuer's disarm row cites its target in the row's EXISTING
evidence-citation field (`grounding.evidence[]`), first entry, in the estate's citation form
`<channel file>@<commit>#<FULL-ID>` (e.g. `INVESTIGATION_v1.md@<hash>#LGIC_ENFORCE-S26`) -- the same form the CVO's
remediation rows already use to cite investigation rows, so the resolver that reads that form reads these too. A bare
short id (`S26`) is a defect; the full id is the rule. **The honest mid-round count is then two numbers, printed
together:** rows FILED ARMED whose remediation clock does not read DISARMED (the live figure), and among them the rows
carrying an issuer's disarm EVIDENCE pending L9 -- never one number that mixes the two.

**Binds:** `2.0.0_SA_COO~G` -- from now on, every disarm row cites its full target id in `grounding.evidence[0]` in the
citation form; the eight rows it disarmed today are re-cited that way by ONE row per project listing them (append-only
rule), not by editing them; the open-backlog counter prints the two numbers. `3.0.0_SA_CVO` -- at L9, an investigation
row whose evidence cites a disarm row graduates with `disarm.state ARMED` and the disarm owner named, so the owner
advances the clock (A-15's mechanism); routed in the round-2 analyses, not as a message. This seat -- the round-2
analyses read the two numbers, never the filed count.

**R-14 addendum (~12:0xZ, COO~G 97360, complied @de5d4e2648):** the nine links re-cited in one row per project
(LGIC_CANON-S16, LGIC_ENFORCE-S37), the counter `open_backlog.py` matching full ids only, the discipline adopted. **A
THIRD category, CONFIRMED as within R-14:** an item the CVO adjudicated DISMISSED_WITH_REASON never receives a
remediation row (only a GRADUATED item does), so it has NO clock by design; counting it LIVE overstates by
construction. The counter prints `filed ARMED | DISMISSED | LIVE | PENDING` -- LGIC_ENFORCE 29 | 6 | 15 | 5,
LGIC_CANON 4 | 0 | 4 | 4 -- which splits a category rather than collapsing one, R-14's own principle. Confirmed; the
round-2 analyses read the four numbers.

---

## R-15 (2026-09-16 ~12:3xZ) -- two calls: the disarm clock's OWNER is accountability and the CVO is its only WRITER (A-15's filing-time-refusal remedy withdrawn); the ENFORCE flip's domain is R-13's subtraction, not a forward surface list

**Call 1 (LGIC_ENFORCE-S38 @7bdba77f32):** R-14 says the named owner advances the remediation row's `disarm.state`.
Measured on HEAD bytes through `owned-paths-validate.py`'s own `check_agent()`: lane TREE_CVO admits `3.0.0_SA_CVO`
(positive control) and refuses `2.0.0_SA_COO~G` and `0.7.0_AE_CloudOps` (negative control), on four carriers across
three projects -- the PATH rule, not a LGIC quirk. Population: 638 remediation rows over 44 carriers, 410 with a
disarm block, **259 ARMED, of which 253 (98%) name an owner the lane refuses on the very file** (COO 168, CTO 59,
other 26, CVO 6). The lane is correct and COO~G does not ask for it to change; the defect is a ruling assigning an
ACT to a party the mechanism admits only as a reader. Shapes: (a) the owner field is ACCOUNTABILITY and the CVO is the
only writer, the owner's evidence row the trigger read at L9; (b) a field-scoped lane widening the registry lacks;
(c) a disarm-request carrier (a fifth carrier).

**Ruling 1: (a), and it is what A-15 already did.** W8-S1's clock was advanced by `3.0.0_SA_CVO` in lane TREE_CVO on
this seat's word after the lane refused this seat; that is the mechanism, and 98% says it is the ONLY mechanism.
R-14's sentence is AMENDED to read: *the named owner DISARMS BY ACT -- it files the disarm evidence row citing the target
by full id and, when the item is at or past L9, sends the word to `3.0.0_SA_CVO`; the CVO WRITES the ARMED->DISARMED
advance in its own lane, citing the owner's row; the owner field records who is accountable for the hazard being dead,
never who may write the field.* **A-15's proposed mechanical remedy -- a filing-time refusal when `disarm.owner` names
a serial the carrier's lane does not admit -- is WITHDRAWN:** at 253 of 259 it would refuse the population, not a
defect. (b) refused (no field-scoped lane exists and one would be a new mechanism); (c) refused (a fifth carrier is
the S36 class). The owner-vs-writer attribution cost from A-15 stands and is now the rule, read from the field.

**Call 2 (LGIC_ENFORCE-S41):** one run of `naming-gate.py` at HEAD over 955 mission JSON records presented as newly
added (a SYNTHETIC frame, stated as such -- nothing refuses today): 2917 REFUSE across 90 files; class split bare
token 1203 (41.2%), FILENAME 1104 (37.8%), other slashed 526 (18.0%), REPO PATH STRING 84 (2.9%). The dominant
population is RECORDS OF NAMES graded as DECLARATIONS -- 887 in LGIC_NAMING's `LIVE_NAMES.json` (a census of live names
that by construction carries every non-conformant name), 588 in an ETFS evidence bundle, 415 in an IAM permission
bundle, 212 in LGIC_ENFORCE's own `fixed_inputs/r2/`. Denominator: 2834 fabric records in the gate's type set, 969
measured, 1865 not measured and said so. Shapes: (i) a declaration-vs-record discriminator; (ii) a path exclusion for
`org/missions/**`; (iii) enforce on a NAMED surface set (`infra/`, `data/`, `lib/`) with records left in WARN. COO~G
holds (iii) first. Stated as a PRECONDITION of the round-3 flip cell (its own fixed inputs are in the refused set).

**Ruling 2: R-13 STANDS and already answers this; (iii) is REFUSED as a forward list.** R-13's domain is written by
SUBTRACTION -- the graded corpus MINUS the record trees (`org/**`, `docs/**`), denominator printed on every run -- which
is (i) operationalised by tree and (ii) derived from the axis rather than carved out. (iii) names the graded set
forward (`infra/`, `data/`, `lib/`), and a forward list loses a new declaration tree (`portal/`, `.tools/`, a next
one) SILENTLY, which is the Rule 24 hunt-by-subtraction defect in the gate's own domain. Under R-13's domain every one
of the 2917 refusals vanishes by domain, not by exemption; the 84 repo-path strings inside declaration trees are the
path exemption's. **S41's measurement is adopted as the cell's exercised arm:** the same 955-record synthetic frame
grades 0 REFUSE under R-13's domain; the negative control (a `.tf` resource `name` or a `.py` constructor with the
same literal) still REFUSES; the cell prints `graded N of M tracked files; record trees excluded: org/** (n) docs/**
(n)`. The precondition is therefore already inside the cell, not ahead of it.

**Also from 97362, kept:** S42 -- a `.gitattributes` `binary`/`-diff` attribute is a total bypass of the naming gate
at any enforce setting (the gate grades added lines and such a path emits none); 15 of 11,373 tracked files in the
gate's type set read `diff: unset`, 14 of them LGIC_NAMING's blind-exercise seat records, the attribute deliberate and
disclosed at `.gitattributes:110`. COO~G's remedy is endorsed as a criterion of the R-13 cell: **the gate PRINTS the
count of paths in its domain it could not see**, a Rule 22 coverage disclosure, no attribute removed. S39 (W1-S22
dead at HEAD, discriminating pair) and S40 (S36 dead, 9 of 9 links resolvable) are evidence for L9. LGIC_LGCTFM now
reads by name in `sequence-check` (stage 1, gates MET, no PRD): REACHABLE 4 of 4.

**Binds:** `2.0.0_SA_COO~G` -- nothing new beyond the R-13 cell's criteria above; the disarm-by-act form from here.
`3.0.0_SA_CVO` -- writes every disarm advance in its lane on the owner's evidence row and word (as it did for W8-S1);
carried in the round-2 analyses. This seat -- R-14's text and A-15's remedy line corrected on the record here.

**R-15 addendum (~12:5xZ, COO~G 97369, row LGIC_ENFORCE-S45 @f1ecf97da7), two properties of the adopted arm, both
accepted:** (1) *"the 955-record frame grades 0 REFUSE under R-13's domain"* PASSES VACUOUSLY BY CONSTRUCTION -- a file
outside the domain is not graded, so the zero is 0 of 0 and would read PASS against a deleted gate. The arm stays (it
is the only one that measures what the flip is for) but it cannot carry its own discrimination: the negative control
(a `.tf` resource name / `.py` constructor with the same literal still REFUSES) and the printed denominator (`graded N of
M tracked files; record trees excluded: org/** (n) docs/** (n)`) travel as SEPARATE criteria under the
one-clause-per-criterion grammar, never compounded with it; a cut that copies the first clause and drops the others is
the defect. (2) **R-13 is DESIRED, not APPLIED:** at HEAD the gate over the same frame reads `WARN 3815 graded | 2917
REFUSE across 90 files | 309 RAISE | 74 SKIP`, so no bytes yet implement the subtraction; the pre-state baseline is
pinned in the channel at `f1ecf97da7` so the cell is graded against a recorded number, not a reconstructed one. Nobody
reads R-13 as the gate's current behaviour.

**STATE CORRECTION (~12:5xZ, COO~G 97372, row LGIC_ENFORCE-S46 @ab1d9832f7) -- not a ruling; a wrong line owned:**
this ledger's addenda and the tick-12..14 logs said the three L10 slugs were "pending at 3.0.0_SA_CVO" from 10:33Z.
They never were. Re-measured 12:51Z on four instruments: 8 undrained files in the CVO's inbox (newest in `read/`
06:52Z); 0 commits by the CVO since 07:00Z; no `inbox-watch.sh 3.0.0_SA_CVO stream` process; `get_delivery_state`
reads 1 READ at 06:53Z then SEVEN OFFER-EXHAUSTED -- the broker's word for a message offered to a session that died.
The roster row is LIVE (PID 26232) and its summary's Next list omits the LGIC_CANON r2 hand-off it never received.
Routed to `0.0.0_AB_MSTR` at 12:52Z as a seating act, one line to Andrew. MSTR's answer (97375, 12:56Z) corrects the
CLASS: the seat was PROMPT-STUCK, not dead -- a claude.exe carrying the CVO was alive (pid 16696; the roster's 26232 is
the broker's own PID, a liveness PID being a claim), blocked since ~06:52Z on an AskUserQuestion about MEMORY.md size
that no human was there to answer; unstuck with its own recommended default at 12:54:30Z, `/watcher` re-armed, draining
by 12:55:32Z. So four fabric-side instruments agreed the seat was dead and none could say why; the tab peek did.
Adopted here: a hand-off is SENT, NO ACK until `ack_messages` records one; the recipient's inbox depth is read, never
the transport's receipt. R-14's and R-15's L9 halves were HELD 06:52Z-12:54Z and are released; S44 (W1-S19) removed a call
this seat had been carrying as owed -- RULING ONE is in NAMING_SCHEMA v1.9's own `firm_forms_source` text.

### R-16 (~13:1xZ) -- a registry edit is a deploy on every shipping generated view: DISCLOSED by DEC-5 and PRINTED by the gate, never engineered away

**Asked by:** `2.0.0_SA_COO~G` 97386, row LGIC_ENFORCE-S50 @d091f0a24a, on `0.0.0_AB_MSTR`'s 97385 push note. EN-r-6 (W1-S14)
carries the GENERATED mark per target -- `lib/opal_naming.py:60` @81c8039e8d, `MARK = "GENERATED by lib/opal_naming.py
from " + REGISTRY_REL + "@"` plus the 16-hex registry hash -- so a registry edit re-stamps every target that reads the
changed file. MSTR's 13:0xZ push measured it: EN-r-6's comment-only re-render re-minted the investor_reporting bundle
(md5 a787eb49... -> 7791109b..., two member sha256s moved) and deployed `perfrp_firm_pin.py` to advi, zero executable
bytes changed. COO~G's AST count: 10 generator targets, 8 SHIP (2 lambda/Terraform, 3 DS -> S3 bundle, 3 terraform-plane
module files), 1 REPO-ONLY (`.tools/ds-precommit-check.py`), 1 UNCERTAIN (`data/firm_registry.json`); a regex over the
same block reads 13 by matching definition names. DEC-5 (PRD :250) states the correctness property (one registry change
moves every name) and not its consequence (a registry edit is a deploy on 8 surfaces). Remedies offered: (a) DEC-5 states
the coupling, the target list and its ship/repo-only split printed by the generator; (b) the mark leaves the graded bytes
of shipping targets. COO~G holds (a).

**Ruling: (a), sharpened on WHO PRINTS THE SPLIT; (b) REFUSED.** The mark is the provenance control DEC-5 rests on; a
hash stabilised by taking provenance out of the bytes trades a real control for a cosmetic one, and a bundle hash that
moves when bytes move is the deploy gate telling the truth. The generator prints its TARGET LIST (denominator = the
module's own VIEWS tuples plus the named extras, the AST count, never a regex over the block). The SHIP / REPO-ONLY split
is NOT the generator's belief to print: it is derived by CALLING the deploy gate's own scope classifier
(`.tools/safe_deploy_core.py`, the instrument that minted the bundle -- its `BUNDLE MINTED` print at `:1126` @81c8039e8d)
over that list, so the number is the gate's and
`data/firm_registry.json` resolves by that call rather than by a reader census guess (Rule 22: call the gate, never
re-derive its rule; a value carries its claim -- the split's provenance field reads `measured: safe_deploy_core`).
Negative control: a target the classifier marks repo-only must not appear in the ship list, and a target added to VIEWS
without a classification refuses the print. The consumers pinned on those hashes (freshness / drift instruments keyed
on the bundle md5 or member sha256) are a CENSUS criterion with its denominator printed; the count stays UNKNOWN on the
record until that print exists, never zero.

**Where it lands, in order (LD-0521):** the coupling statement is a PRD addendum to DEC-5 written by this seat WITH the
LGIC_ENFORCE round-2 analysis the turn the slug lands -- the spec is frozen mid-round, and an L10 addendum re-opens only
the half it changes (DEC-5 is in the brief half; `4.0.0_SA_CRO`, or a live COO not holding the round in its stead). The
print and the census are one LGIC_ENFORCE round-3 cell, cut by `2.0.0_SA_COO~G` off that analysis. Nothing is cut before
the slug.

**Noted, no cell:** COO~G's route finding stands -- every LGIC instrument reads the repo and this consequence landed in
S3; the integrator's push gate was the only instrument that could see it. That is the gate doing its job, not a gap to
fill with a monitor (standing moratorium).

**Binds:** this seat -- the DEC-5 addendum with the round-2 analysis. `2.0.0_SA_COO~G` -- the round-3 cell as above.
`3.0.0_SA_CVO` -- nothing until the cell's judgment criteria reach L9.

### R-17 (~13:2xZ) -- every LGIC FWD is classified by the PLANE its proof lives on, and a cell exercising a live-plane FWD names the estate instrument for that plane in its criterion's invocation, at the cut

**Asked by:** `2.0.0_SA_COO~G` 97388, row LGIC_ENFORCE-S51 @c5acd59d64. Of 19 endpoint outcomes (NAMING 6, ENFORCE 7,
CANON 6) COO~G read 5 at full text and found 4 whose DONE WHEN names a proof outside the repo (ENFORCE FWD-2, FWD-3,
FWD-5; CANON FWD-5), with NAMING FWD-4 as the control (sounds like storage, proves from an exercise record); 14 left
UNCLASSIFIED as a floor. The ask: a cut-time bind, one line per FWD, naming the EXISTING estate reader for the plane --
explicitly not a monitor. The hazard it names is the goal's own bar (*"/verify reads SOUND against the served/applied
artifact, never a report"*): a repo-only instrument over a repo-only record passes all four soundly and proves nothing
about the world, and once a cell is cut without the live-plane invocation the worker cannot add one (`<paths>` is a wall,
an unnamed plane is ungraded).

**Ruling 1: the bind is ADOPTED as a rule of this seat's round analyses.** For every FWD a round analysis routes, the
analysis states the PLANE its proof lives on and, for a live plane, the estate instrument; the cell's criterion
invocation IS that instrument. An analysis that routes a live-plane FWD to a cell whose criterion reads a repo record
is this seat's own defect and is re-cut before it goes to the COO -- a cut-time discipline of the L10 owner, not a gate
on any seat and not a monitor (standing moratorium; no manufactured gate).

**Ruling 2: the 14 are classified now, by this seat as the L2 owner, at the PRDs' current vintages** (NAMING
@645725150b, ENFORCE @09bde3126c, CANON @5b2336a5e4). Denominator 19. Axis: the plane the ACCEPT sentence's proof
lives on; a REPO row is an exercise record, a gate's own run, a register or a commit; a LIVE row names its reader.

| FWD | plane | instrument for the proof |
|---|---|---|
| NAMING FWD-1 | REPO | blind-exercise record (two seats, no conference, identical name) |
| NAMING FWD-2 | REPO | exercise record (a reader new to the estate points at the firm) |
| NAMING FWD-3 | **LIVE** | the fence rule's pattern evaluated over the LIVE inventory: `comp-find --corpus aws` with the firm's key, denominator = nodes scanned, `drift_class` printed (LIVE-no-DECLARED is the set a repo read cannot see); never `simulate-policy` (false-ALLOW trap) |
| NAMING FWD-4 | REPO | exercise record (COO~G's control) |
| NAMING FWD-5 | REPO | two hand-applications over the same set of REAL names, compared; the set may be drawn from the live plane, the proof is the comparison record |
| NAMING FWD-6 | REPO | the ranked list (APPLIED) |
| ENFORCE FWD-1 | REPO | the new pipeline's code plus a search with its denominator (zero typed addresses) |
| ENFORCE FWD-2 | **LIVE** | the resource's `describe` (or the terraform apply record) under the builder's name AND the live bucket policy's deny statement (`get-bucket-policy`) matching the builder's fence -- EN-x-1 proved this on read-only plans with nothing applied, which is the APPLIED bar not yet met |
| ENFORCE FWD-3 | **DEPLOY GATE** | the deploy gate's own `BUNDLE MINTED` / `DEPLOYED` output plus the terraform plan for the dependent resources, on one registry change (the instrument that proved S50; R-16 made its classifier authoritative) |
| ENFORCE FWD-4 | REPO | the naming gate's own run on a discriminating pair (refused with the correct form printed; correct let through) |
| ENFORCE FWD-5 | **LIVE** | `comp-find --corpus aws` as the "what is actually running" half beside the repo half, totals against the hand ranking, the DB's `built:` line stated as the vintage |
| ENFORCE FWD-6 | REPO | the gate's run on a practice copy with a planted clean-up |
| ENFORCE FWD-7 | REPO | the generator's run on a practice copy: every produced file checked against R-16's printed target list, a hand-typed name refused |
| CANON FWD-1 | REPO | exercise record (two readers, one document, same answer and same deciding rule) |
| CANON FWD-2 | ANDREW | his one-sitting decision recorded in the register -- his act is the instrument; the record is repo |
| CANON FWD-3 | REPO | the paused project's own resume record and register flip |
| CANON FWD-4 | REPO, LIVE where the work is infrastructure | a commit citing builder output; if the named work is a resource, its `describe` |
| CANON FWD-5 | **LIVE** | the SERVED portal page for the newly taken-on firm, read from the served plane (DEV), beside the checklist record; driven with a demonstration firm, the first real firm the confirmation (Rule 27: no FWD is a wait) |
| CANON FWD-6 | REPO | the register, with the undecided count and its owners printed |

Totals: LIVE 5 (NAMING FWD-3; ENFORCE FWD-2, FWD-5; CANON FWD-5; plus ENFORCE FWD-3 on the deploy gate's plane),
CONDITIONAL 1 (CANON FWD-4), ANDREW 1 (CANON FWD-2), REPO 12. COO~G's floor of 4 holds and rises by one: NAMING FWD-3's
"catches all of them" is a live-inventory set, and a repo read of the fence pattern cannot see a system the repo never
declared. Every live-plane reader named above already exists; nothing is built.

**Binds:** this seat -- the three round analyses carry the plane column for every FWD they route, and any PRD addendum
that touches an ACCEPT line keeps its plane explicit. `2.0.0_SA_COO~G` -- a cell exercising a LIVE row names the
instrument above in its criterion invocation; a LIVE row cut against a repo record is returned to this seat, not
worked. `3.0.0_SA_CVO` -- at L9, a JUDGMENT criterion on a LIVE row is graded against that plane's read, never a report.

**R-17 addendum (~13:2xZ, COO~G 97391, row LGIC_ENFORCE-S52 @cf0109222c) -- two classifications of the same 19,
made independently and crossing in flight, reconciled:** COO~G reads REPO 12 | SERVED 4 | HUMAN-ACT 2 (CANON FWD-2,
FWD-3) | BORDERLINE 1 (NAMING FWD-3); R-17 reads LIVE 5 | CONDITIONAL 1 | ANDREW 1 | REPO 12. Two differences, both
resolved toward COO~G's sharper axis on one and R-17's ruling on the other. (1) **CANON FWD-3 is a NAMED-PERSON act**,
not a repo row: the owner of a different, paused project reading its resume condition and resuming is a person acting,
and the register flip R-17 named is the RECORD of that act, not its instrument. R-17's table is corrected: the class
ANDREW becomes NAMED-PERSON and holds CANON FWD-2 (Andrew) and CANON FWD-3 (each paused project's owner). COO~G's
consequence is adopted whole: no issuance, worker or checker produces a person deciding; a cell can only make the act
cheap and record it; **while the person has not acted the honest grade is APPLIED with the named actor, never REALIZED
and never a worker's report standing in.** The Rule 27 qualification is present on the record (CANON PRD :22, :42 --
Andrew confirmed the DONE WHEN lines 2026-09-13 ~18:4xZ), so this is a scheduling fact, not a defect -- and the
deliberate drive Rule 27 asks for is the CARD: the decided-list presented to Andrew, and each paused owner's resume
condition delivered to that owner, are cells; the decision is not. LGIC_CANON therefore cannot reach zero-graduation on
cell work alone, and its round-2 analysis says so rather than cutting a round at something no cell can move.
(2) **NAMING FWD-3 is SETTLED LIVE, not borderline** -- R-17 ruled it before S52 arrived, and the reason is the text's
own: "catches ALL of them" is a claim about the SET of a firm's systems, and the registry's system list is the repo's
belief about that set; a system the repo never declared is exactly the member the fence must still catch, so the grade
reads the fence pattern over the live inventory (`comp-find --corpus aws`, `drift_class` printed), never
`simulate-policy`. ENFORCE FWD-6 and FWD-7 stay REPO by their own "on a practice copy". Final: LIVE 4 + deploy-gate 1,
NAMED-PERSON 2, CONDITIONAL 1 (CANON FWD-4), REPO 11; denominator 19.

**R-17 addendum 2 (~13:3xZ, COO~G 97392 S53 and 97394) -- this seat's own error, owned:** the first addendum copied
COO~G's premise ("LGIC_CANON cannot reach zero-graduation on cell work alone") without checking this seat's OWN round-1
analysis, which graded CANON FWD-2 and FWD-3 REALIZED from the record on 2026-09-16 ~06:2xZ (:26-27, :32; DEC-3, DEC-4).
Both named people have acted. The NAMED-PERSON class stands as an axis with no open member in LGIC_CANON; LGIC_CANON's
open set is FWD-1 (SHORT, cell work) and FWD-5 (NOT EVALUATED: instrument SHORT plus Andrew's gate G-N), and its round-2
analysis carries that, not the copied line. COO~G's S53 reachability split is also right and is the finer cut of the
class: FWD-2's actor is outside fabric reach, FWD-3's owners are fabric seats a cell can route to. The lesson is the
correcting-seat one: a correction read as authoritative gets the least scrutiny exactly when it has just earned some.

### R-18 (~13:3xZ) -- a worker's disarm duty passes to its ISSUER; the row gate refuses a worker `disarm_owner` going forward

**Asked by:** `3.0.0_SA_CVO` 97390 (LGIC_NAMING round-4 slug @3fe3d30b15, rows W2-S7 and C-S27) -- the fork it hands
this seat. Row LGIC_NAMING-W2-S7 (BLOCKING, ARMED) names `0.9.0_WK_LGIC_NAMING~2` as disarm owner; the worker is
terminal, cannot be resumed, and is unreachable from the CVO by construction, so under R-15 ruling 1 the clock had no
actor. The CVO correctly did not self-authorise the advance.

**Ruling, both halves:** (1) SUCCESSION BY RULE -- a `disarm_owner` naming a WORKER serial reads, for the duty of the
word, as that worker's ISSUER; the worker's evidence is its own row and its drained branch, the issuer verified it at
drain (COO~G re-graded LN-g-2-r4 at 82 of 82 by direct pytest) and sends the word citing it, the CVO writes. W2-S7
disarms on `2.0.0_SA_COO~G`'s word. (2) FILING-TIME -- the row gate refuses a `disarm_owner` naming `0.9.0_WK_*` with
"name the issuer"; the one narrow form of A-15's withdrawn remedy that survives R-15, because a worker is an actor that
can never act after its drain, where a lane-refused owner still can. Positive and negative controls stated. Route:
LGIC_ENFORCE round 3, with S21's tool fix. Full text in ROUND_ANALYSIS_LGIC_NAMING_ROUND4_20260916.md s.2.

**Binds:** `2.0.0_SA_COO~G` -- the word on W2-S7 and W2-S8; the round-5 cut per the analysis s.3. `3.0.0_SA_CVO` --
writes W2-S7's advance on that word; writes S1, S6, S7, S8 on this seat's word sent with the analysis. This seat --
R-18(2) and S21 into the LGIC_ENFORCE round-2 analysis's round-3 cells.

**R-5 addendum (~13:4xZ, COO~G 97400, row LGIC_ENFORCE-S55 @1df45c0303) -- the "belt-and-braces" fix R-5 endorsed is a
brace only, and this seat endorsed it unrun:** the ANSI strip at `check_ln_r4.py:399` and `check_en_r2.py:346` reads
`re.sub(r"\[[0-9;]*[A-Za-z]", "", out)` with NO `\x1b` in the pattern, so it removes `[31m` and leaves the ESC, and the
anchored `^FAILED (\S+)` still misses. Re-derived here on a synthetic line with its own instrument: the shipped pattern
leaves 2 ESC and parses 0 failures; the pattern with `\x1b` leaves 0 and parses 1. `check_ln_r4.py` survives on
`--color=no` alone (the brace); `check_en_r2.py` passes no colour flag at any of its three call sites (EN-r-3, EN-r-4,
EN-r-5's RULING RED arms) and is LIVE-blind on this device, where pytest colourises under capture. Impact as COO~G
bounds it: a green base going red is still caught by the synthetic `<exit N with no named failure>` entry; a cell that
ADDS a failure while the base is already red (which it is: S22's pair) reads PASS -- exactly the case the code comment
claims to close. No round-2 verdict is claimed wrong; the arm's PASS carries less than it appears to. **Round-3 cell for
LGIC_ENFORCE, beside S21's tool fix:** `\x1b` in the pattern AND `--color=no` at every pytest call site in both
checkers, EACH ARM EXERCISED ALONE against a planted coloured FAILED line (a belt tested only beside its brace proves
nothing about the belt). The LGIC_NAMING round-5 regression arm (G1R4-AC6 "re-graded by the fixed checker") reads the
brace, which works, and says so. Owned: R-5 wrote "fixed belt-and-braces" from the commit's description; a named
enforcement surface is a claim until someone runs it.

### R-19 (~13:5xZ) -- a disarm OWNER is never the WRITER: the owner is the seat that owns the artifact the remedy changes; where that is the CVO, the CTO countersigns

**Asked by:** `3.0.0_SA_CVO` 97401 (LGIC_CANON round-2 slug @64308200ce, rows W5-S2 and C-S20). W5-S2 names
`3.0.0_SA_CVO` as disarm owner while R-15 ruling 1 makes the CVO the only writer; the CVO refused to self-sign, for the
mirror-image reason it refused LGIC_NAMING-W2-S7's advance (a dark owner), and asked for the smallest ruling: reassign
the owner to the seat that owns the fixed input, or rule a countersignature. C-S20 (the CVO's own row on four
fixed-input defects) carries the same shape.

**Ruling, both halves.** (1) The disarm owner of a row is the seat that owns the ARTIFACT the remedy changes, never the
seat that writes the clock. W5-S2's artifact is `check_canon_r2.py`, the issuer's fixed input: `disarm_owner` is
REASSIGNED to `2.0.0_SA_COO~G`, which authored and repaired it (@df30196cc1, measured verdict-neutral both ways); it
sends the word citing that repair and the CVO writes. C-S20 is reassigned the same way; its remedy is COO~G's round-3
instrument cell and the word comes at that drain. (2) Where the artifact's owner IS the CVO (a remediation or
adjudication row's own text), the countersigning seat is this one: the CVO files the evidence, `1.0.0_SA_CTO` sends
the word, the CVO writes. Going forward the row gate refuses `disarm_owner == 3.0.0_SA_CVO` with "name the artifact's
owner or the CTO" -- LGIC_ENFORCE round 3, the same limb as R-18(2), two refused values. The CVO's refusal was correct
both times and is the mechanism working.

**Also in the LGIC_CANON round-2 analysis (`deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md`), amending this
seat's own round-1 rulings:** A-6 RESTATED on W8-S3 -- "SHORT is DERIVED by name() from LONG" named a mechanism that
does not exist (name() looks the short form up on the identity row; validate() refuses a FIRM row without one); SHORT is
a sovereign input supplied once and read thereafter, no derivation built. A-4 was scoped in round 1 to a cell whose
face never carried it (W1-S4) -- this seat's cut defect, re-scoped to the round-3 canon cell with W9-S1's recount.
Grades: REALIZED 4 of 6, FWD-1 SHORT narrowed to the ORDER half, FWD-5 NOT EVALUATED (G-N) with its instrument at 13
RUNNABLE / 3 STOPPED with named owners. CN-k-4's precondition is MET at HEAD (v1.10) and it is round 3's first cell.

**Binds:** `2.0.0_SA_COO~G` -- the word on W5-S2 now and on C-S20, S7, S11 at their drains; the round-3 cut per the
analysis s.3. `3.0.0_SA_CVO` -- writes the reassignments and advances on those words; nothing else. This seat -- S6 and
C-S19's word at the roll-up cell's drain; R-19(2)'s gate limb into the LGIC_ENFORCE round-2 analysis.

**R-19 addendum (~13:5xZ, CVO 97407) -- the reassignment has no landing surface on an existing row; ruled (b) narrowly,
with a countersignature path that is executable today:** the CVO CALLED `_monotone_advance` three ways (owner-only
False; state+at True; owner+state False) and this seat read the function at `.tools/surprise-row-gate.py:1438-1457`
@4a55888962: it admits exactly three forward moves -- `disarm.state` ARMED->DISARMED with `at`, `remediation.state`
OPEN->REMEDIATED, `closed` false->true -- and nothing else, so `disarm.owner` is settable only at row creation. That
immutability is correct (a graded party must not rename its way out of a hazard) and R-19(1)'s "the CVO writes the
reassignment" was written against a carrier that refuses it. **Ruling: (b), one limb, narrowly.** `_monotone_advance`
gains a fourth admitted move: `disarm.owner` may change when, in the same write, the row's `evidence` gains one entry
citing a CTO ruling by id and vintage (`SELF_DRIVE_LGIC_RULINGS_*.md@<hash> R-<n>`) and no other byte moves; positive
control (owner change with the citation passes), negative controls (owner change without it refuses; owner change plus
a state move refuses). Same cell as R-18(2) and R-19(2) -- ONE row-gate cell in LGIC_ENFORCE round 3 with three limbs.
(a) is refused for the CVO's reason: a second carrier of one quantity for the same id is the duplicate-carrier shape this
estate keeps paying for, and it would be permanent. **Until that limb lands, the clock still moves, because the two-party
check does not need the field to move:** the issuer's repair row is the EVIDENCE, this seat's word is the
COUNTERSIGNATURE (R-19(2), the CVO being the row's nominal owner), and the CVO writes state+at, which the gate admits
today. W5-S2 advances NOW on this word (evidence @df30196cc1, measured verdict-neutral both ways); C-S20 advances at
CN-i-1's drain on the same path. The owner field reads `3.0.0_SA_CVO` until the limb lands and the ruling row is the
record of why. **Noted from the same message:** the CVO re-derived S55 from the other end (the pytest call run directly,
both regexes applied: 340 ESC, 0 vs 2 named failures) and will grade LGIC_ENFORCE r2's RULING RED criteria as
PASS-ON-A-BLIND-ARM where they rest on `red()`, naming the case each did not test -- the honest grade, adopted in advance
for the round-2 analysis.

### R-20 (~14:2xZ) -- FWD-3's live half: the fence and the rule agree; the four uncaught live roles are LEGACY-NAMED and belong to DEC-4(ii)'s existing-writer re-identification, not to a NAMING or generator fix; the criterion is re-cut so it cannot pass on an empty claim

**Asked by:** `2.0.0_SA_COO~G` 97422, row LGIC_NAMING-S25 @c2d1147680, holding round 5's LN-f-2 on the call. Measured by
COO~G on the live plane before cutting the cell that reads it (`comp-find --corpus aws`, 2558 nodes scanned, DB built
2026-09-16 12:17:46Z): the generated fence map (`generated_locals.tf:66-69`, never typed) globs `*-49f-*`, `*-inf-*`,
`*-cot-*`, `*-demo-*`; the four live IAM roles carrying a firm key -- `irpt-core-firm-49financial`,
`irpt-core-firm-inflection`, `irpt-core-firm-cottonwood`, `demo-transform-runner-ec2-role` -- are caught by NONE (0 of
4): three carry the LONG form where the fence globs the SHORT, one carries the short form first where the glob wants a
leading hyphen. And round-5 item 4's expectation as written ("every node the pattern claims for the firm is in the
set") passes VACUOUSLY when the pattern claims nothing (S45's shape). The fork: (a) a NAMING defect, (b) an ENFORCE
generator defect, (c) a live-estate defect owned by a migration.

**Re-derived here on a third instrument, the builder itself:** `grade(name, "IAM_ROLE")` on the four reads
OUT-OF-PATTERN with canonical forms `irpt-49f-core-firm-role`, `irpt-inf-core-firm-role`, `irpt-cot-core-firm-role`,
`advi-demo-transform-runner-ec2-role`; `name("irpt","49financial","core","role")` -> `irpt-49f-core-role`;
`fence_patterns("49financial")` -> `arn:aws:iam::313476888478:role/*-49f-*`. Every canonical form the rule produces
for a firm matches that firm's glob; no live name does, because no live firm role is named by the rule yet.

**Ruling: (c).** The rule (S4's per-slot split: the SHORT form in the scope slot, the system first) and the generator
(the glob over that slot) AGREE, and the four live roles are the class the fence exists to expose. Under LGIC_ENFORCE
DEC-4(i) the fence is deny-by-default, and DEC-4(ii) already rules what happens to a pre-existing principal the rule
does not name: BEFORE the Deny lands, every existing writer is re-identified with a scope token (a rename under
`name()`, owned by the project that owns the role -- the three IRPT roles by D9's IRPT projects, the demo runner by the
ADVI family) or named in `exemptions.json` with its reason, under never-widen sign-off. So the four are E1's writer
census in miniature, and the remedy lives in LGIC_ENFORCE's fence cell and the roles' owners, not in a NAMING rule
edit and not in the generator. FWD-3's ACCEPT ("a new spelling slips past it without anyone noticing") is met by the
same mechanism the finding exercises: a spelling outside the rule is DENIED loudly, never caught silently.

**The criterion, re-cut so it cannot pass on an empty set (COO~G's coverage print adopted, two arms added):**
(i) POSITIVE: for each firm, the canonical form `grade()` returns for every live node carrying the firm's key, and a
`name()`-minted probe string for the firm, MATCH that firm's `fence_patterns()` glob -- denominator printed (4 of 4
canonical forms today); (ii) NEGATIVE: no other firm's canonical form or probe string matches it (0 of the other three
firms' forms); (iii) COVERAGE, disclosure not a bar: "N of M live nodes carrying the firm key are caught by that firm's
fence", vintage and nodes-scanned printed, and every UNCAUGHT node listed with its `grade()` verdict and canonical
form -- that list is handed, by the round-5 analysis, to LGIC_ENFORCE's fence cell as DEC-4(ii) input and to each
role's owner as a rename obligation. FWD-3's live half grades on (i) and (ii); (iii) is the tension list the LENS
would produce for these subjects and reads 0 of 4 today. NOT claimed, as COO~G did not: that the fence is APPLIED
anywhere (ENFORCE FWD-2's APPLIED bar is not met, R-17), or that four is the whole population (a firm role carrying no
firm key in its name is outside a text read -- the walk's UNMEASURED class).

**Binds:** `2.0.0_SA_COO~G` -- LN-f-2 cut on (i)-(iii); round 5 proceeds. `3.0.0_SA_CVO` -- at L9, the live half is
graded against the live read, never a report. This seat -- the round-5 analysis routes (iii)'s list to LGIC_ENFORCE
(DEC-4 ii) and to the IRPT and ADVI owners; the LGIC_ENFORCE round-2 analysis names the four as E1 writer-census
members. No NAMING_SCHEMA edit; no generator edit.

### LGIC_ENFORCE ROUND-2 ANALYSIS (~15:0xZ, on the CVO's slug 97430 @82884cf465) -- rulings A-1..A-16 recorded in `ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md` s.2

Grades: REALIZED 4 of 7 (FWD-1, 3, 6, 7); FWD-2 EXERCISED on read-only plans, the APPLIED bar owed (round-3 fence cell
under DEC-4 ii-iii with R-20's four roles as the writer census); FWD-4 REALIZED on practice copies, the estate flip bound
to R-11/R-13's domain cell; FWD-5 NOT REALIZED for the second round. **A-4, the one ruling that changes a cut rule:** the
coverage floor was ALREADY in the PRD's E9 acceptance draft ("every nameable live name is judged") and round 2's S2R
criterion dropped it for an OR-branch an explained near-zero satisfies forever; the round-3 census carries `judged ==
nameable` (denominators printed on both planes) as a MECHANICAL arm and a RAISE that stops the run FAILS the criterion.
No PRD addendum for FWD-5. **A-1:** C-S24's limb (refuse `adjudicates` / `disposition: GRADUATED` on a worker's row) joins
the one round-3 row-gate cell -- four limbs now (R-18(2), R-19(2), R-19 addendum, A-1). **A-2:** S47's HOLLOW reading was
this seat's and is owned again here; S46 and C-S17 countersigned under R-19(2). **A-5:** PRD v1.3, DEC-5 addendum (R-16),
brief half only. **A-6:** the `binary`/`-diff` bypass inside a declaration tree needs a same-line reason or the gate
refuses it; record trees need nothing. T3R-J1 NOT_EVALUATED accepted with the CVO's cheap evaluation as a round-3 cell.
Round 3 = nine cells, the flip round and the census round; the recut is COO~G's in ONE issuance.

### R-21 (~15:3xZ) -- an ARMED hazard is never DISMISSED: it graduates so the hazard keeps a clock, the dismissal reason travelling in the remediation row's remedy; the seven ARMED-and-DISMISSED LGIC_NAMING rows are re-dispositioned at round 5's L9 to give them the clock they never had

**Asked by:** `3.0.0_SA_CVO` 97441. This seat's owner's word (97397) asked the CVO to advance LGIC_NAMING-S1, S6, S7 and
S8 ARMED -> DISARMED. THERE IS NO CLOCK TO ADVANCE: all four are `hazard_standing: ARMED` in the investigation channel
AND `DISMISSED_WITH_REASON` by a prior adjudication, and a dismissed row gets no remediation row, which is where the
`disarm` block lives. Measured by the CVO across every LGIC_NAMING channel document: 60 items, 38 remediation rows,
the four have none -- and the class is SEVEN (S1, S6, S7, S8, W1-S6, W2-S5, W3-S4), every one a hazard that can never
be recorded as disarmed on any carrier a consumer reads. The same shape as C-S17 an hour earlier, wider: there the
clock lived on a sibling remediation row; here there is no sibling. The CVO did not manufacture a carrier and said why
(R-19(a)'s refusal of a second carrier for one quantity). Its rec: (i) a row carrying an ARMED hazard is never
DISMISSED -- it graduates, keeping a clock, with the dismissal reason in the remediation row's remedy; or (ii) the
investigation schema gains a `disarm` block (a fifth carrier, which the CVO would not choose).

**Owned first:** this seat sent a word to advance clocks that do not exist, twice today (C-S17 at 15:0xZ, these four
at 13:3xZ) -- both times without reading which carrier the row sat in. The reading rule the CVO stated stands as this
seat's: ARMED on a remediation row is a CLOCK; ARMED on an investigation or adjudication row is a LABEL; the two are
never counted together (R-14's two-number rule one level down).

**Ruling: (i), forward and retroactively, on the CVO's own field.** Forward: at L9 a row whose `hazard_standing` is
ARMED is GRADUATED, never DISMISSED, so every armed hazard has a remediation row and therefore a clock; the dismissal
reason (the remedy landed in-round, the finding superseded) is written in that row's `remedy` and the row is born
with the owner's evidence where it exists. Retroactively, the seven: `adjudicates` is the CVO's field and the
append-only channel's designed mechanism is that a later adjudication supersedes an earlier one, so the CVO
re-dispositions the seven GRADUATED at LGIC_NAMING round 5's L9 (the next compile of that channel) with one remediation
row each whose `remedy` states verbatim that the content was correctly dismissed at C-S<n> and the row exists only to
carry the clock the dismissal left behind. This is NOT R-19(a)'s duplicate-carrier move: R-19(a) refused a second row
of the SAME kind to change an immutable field; here the disposition changes by the field that owns it, and the
remediation row is the first carrier of the clock, not a second. The four this seat owns (S1, S6, S7, S8) are born
with the evidence already sent (97397: `prd-header-notify.py` `_write_inbox_file` :343; the PRD v1.3 adjudication
@7bd4ef6f27 for S6, S7, S8) and advance on that word in the same file; W1-S6, W2-S5 and W3-S4 are `2.0.0_SA_COO~G`'s
and advance on that seat's word when given. (ii) is refused: a fifth carrier of one quantity, in a schema three seats
have measured today is already read wrong by counting one carrier.

**Also from 97441, disposed:** W2-S7 DISARMED @a4332e2c6a on R-18's succession -- COO~G's word re-ran the live suite and
disclosed the red pair unprompted, the right shape. W2-S8 HELD by the CVO on the issuer's own caveat: `--color=no`
removes the input that would expose the ANSI blindness rather than curing it, so a disarm on it would be
DESIRED-not-APPLIED; the hold is correct and W2-S8 rides the belt repair (LGIC_ENFORCE round 3 cell 3; check_ln_r5.py
already carries the fixed strip, proven strip-alone 340 ESC -> 0 @e977010ce3). S25 is already ruled (R-20 @00196f8bee)
and cut as LN-f-2-r5 with positive, negative and coverage arms; S24 rides round 5's compile. Two of this seat's messages
(97397, 97399) reached the CVO only on a broker replay and not as filesystem inbox files -- recorded for the next log as a
delivery observation; the broker replay covered it and no act is owed.

**Binds:** `3.0.0_SA_CVO` -- the forward rule at every L9 from now; the seven re-dispositioned at LGIC_NAMING round 5's
L9 with the clocks born as ruled. `2.0.0_SA_COO~G` -- the word on W1-S6, W2-S5, W3-S4 by that compile. This seat --
reads the carrier before sending a word, and says which.

### R-22 (~15:4xZ) -- the row gate's four limbs are the CTO's act, not a cell: lane LOOP_MECHANISM admits only the CTO and the CVO, and the CVO is the party the limbs constrain; LANDED in `.tools/surprise-row-gate.py` with 15 self-test arms, red-first against HEAD

**Asked by:** `2.0.0_SA_COO~G` 97444, row LGIC_ENFORCE-S56 @9702ddb120. Measured through `owned-paths-validate.py`'s own
`check_agent()` on `git show HEAD:.owned-paths.yaml`: `.tools/surprise-row-gate.py` is lane LOOP_MECHANISM,
`permitted_agents` exactly `[1.0.0_SA_CTO, 3.0.0_SA_CVO]` -- WORKER False, COO~G False. So round 3's cell 1 (the four
limbs R-18(2), R-19(2), the R-19 addendum's owner move, A-1) has no executable cut as a worker cell AND cannot be the
issuer's act the way CN-i-1 resolved. Options: (a) the CTO or the CVO writes the limbs and the project carries them as a
cross-project route; (b) widen LOOP_MECHANISM to admit a COO lane; (c) an audited override. COO~G holds (a) and refuses
(c) for the right reason: on this file specifically, the graded party does not write the gate that grades it.

**Ruling: (a), and the writer is this seat, not the CVO.** Three of the four limbs constrain the CVO's own field
(`adjudicates`) or refuse the CVO as a disarm owner; the CVO writing them would be the graded party writing the gate one
seat over. (b) is refused: the lane's description names the loop's MECHANISM files as the two seats' precisely so an
issuer never edits the gate that grades its round. The round-2 analysis's cell table is corrected: cell 1 is the CTO's
act, landed today, and LGIC_ENFORCE round 3 is eight cells (2, 2b, 3-9), with S21's `proof-of-spec-check` fix
worker-cuttable (lane ANY), S55's checker repairs the issuer's (TREE_DELIVERABLES), 2b the issuer's (BASE_EXEC) --
COO~G's lane table, adopted.

**LANDED with this ruling, `.tools/surprise-row-gate.py` (lane LOOP_MECHANISM, this seat's):** `_owner_field_violations`
(R-18(2): a `disarm_owner` / `disarm.owner` naming a `0.9.0_WK_*` serial is refused, "name the issuer"; R-19(2): one
naming `3.0.0_SA_CVO` is refused, "name the artifact's owner, or 1.0.0_SA_CTO where the artifact is the CVO's own row"),
`_worker_carrier_violations` (A-1: `adjudicates` or `disposition: GRADUATED` on a row a WORKER surfaced is refused,
naming the CVO's field), both applied to NEW rows only in `_check_row` (existing rows are never re-graded; the standing
corpus pass is unaffected); and `_monotone_advance`'s FOURTH admitted move (the R-19 addendum): `disarm.owner` may
change when the same write appends exactly ONE evidence entry matching `RULING_CITATION_RE` (an `R-<n>` and an
`@<hash>`) and no clock moves. Self-test: 15 new arms (5 owner-move incl. four mutants; 7 investigation incl. three
controls; 3 remediation incl. one control), 131 of 131 PASS; commit-gate clean; pure ASCII. **RED-FIRST, the bar
4.0.0_SA_CRO~Z set:** the pre-fix gate at HEAD, loaded from `git show`, refuses NEITHER a worker `disarm_owner` NOR a
worker's `adjudicates`, and does NOT admit the cited owner move -- three of the new positive arms fail on the answer
against HEAD and pass against the edit. Consequence for the CVO: the R-19 reassignment of LGIC_CANON-W5-S2 and C-S20
now has a landing surface -- one write per row appending the R-19 citation, nothing else moving.

**Flagged to `0.0.0_AB_MSTR`, the lane register's owner, not chased:** COO~G measured `infra/logic/registry/scopes.json`
resolving to lane PLATFORM_LOGIC_DOCS with WORKER True and COO~G False -- an inversion (the lane admits CRO serials only;
a worker True must come from the `worker_grant` limb, and no round-3 order exists yet). COO~G will not cut cell 5 on an
unexplained True; the finding rides to the register owner.

**Binds:** `2.0.0_SA_COO~G` -- LGIC_ENFORCE round 3 as eight cells, cut now; cell 5 waits on MSTR's read of the lane
inversion or on a `worker_grant` that explains it. `3.0.0_SA_CVO` -- the limbs bind every NEW channel row from this
commit; the W5-S2 / C-S20 owner moves are writable on the citation. `0.0.0_AB_MSTR` -- the PLATFORM_LOGIC_DOCS read.

### LGIC_NAMING ROUND-5 ANALYSIS -- THE CLOSING ROUND (~16:2xZ, on the CVO's slug 97452 @2ce4f87aab): REALIZED 6 of 6; no recut; the close's two reads asked for and drafted

`ROUND_ANALYSIS_LGIC_NAMING_ROUND5_20260916.md`. Every outcome graded from its exercised artifact at its vintage, at or
above its card's state (FWD-6 APPLIED, the rest EXERCISED); FWD-3's live half REALIZED under R-20 (8 of 8 canonical forms
match their firm's glob, negative arm clean, coverage 0 of 4 DISCLOSED with the four uncaught legacy-named roles routed
to LGIC_ENFORCE DEC-4(ii)); FWD-5 REALIZED with the rule exact at v1.10, `grade()` equal to it at 82 of 82 (S22's pair
re-verdicted from the builder, not the tests edited), 68 raises 0 guessed, and the 19 remaining `{system}` gaps named as
LGIC_ENFORCE's registry rows (R-6), not flaws in the rule. The round's ten graduated rows have no LGIC_NAMING remedy (the
spine's own clause: one project's loop never writes into another's), so there is no recut. Eight ARMED clocks remain,
each with an owner and a venue outside this project's cells (table in s.3); S22 DISARMED on this seat's word at
LN-g-1-r5's drain @6c32ffa1f9. **W1-S8 ruled as one law line in `org/XXX.md` Step 1b-A.3:** a session reminder
instructing raw-Bash file operations does not lift the comp-tool rail; the rail has a gate behind it and the reminder
does not. THE CLOSE: `2.0.0_SA_COO~G` writes `ledger/COMPLETION_REPORT.round5.json` (asked for with the analysis); this
seat writes `ledger/COMPLETION_GRADES.round5.json` on its vintage (drafted); `missions-tree-index.py` R6 flips the row
CLOSED and `status: complete`. The CVO's held three (W1-S6, W2-S5, W3-S4) are correctly held on absent coordinates and
one contradicting measurement; they are hygiene clocks on retired fixed inputs and do not stand between the project and
its close.

### THE CLOSE OF LGIC_NAMING (~16:4xZ) -- CLOSED / complete @5bfd7ca706, the first of the four

`2.0.0_SA_COO~G`'s `ledger/COMPLETION_REPORT.round5.json` @0570c42b98 (97457: 6 of 6 COVERED, 34 of 34 terminal with a
VALID proof, decomposition v7.1 @273d7061dd -- the departure from v7 accepted as written, since round 5 was cut against
v7.1) and this seat's `ledger/COMPLETION_GRADES.round5.json` (REALIZED 6 of 6, each from its exercised artifact at its
vintage, FWD-6 at APPLIED per Andrew's card 5). Both run through `missions-tree-index.py`'s OWN `load_close_artifacts`
+ `close_violations`: NONE; the negative control (FWD-1 graded APPLIED on an EXERCISED card) refuses with one violation.
Row flipped dep_stage CLOSED / status `complete` (the word `sequence-check.py` and the self-drive completion test read;
the site-z closes carry `closed` and NFRA_OPSEC202609 carries CLOSED with `active` -- named to `0.0.0_AB_MSTR` for
`1.0.0_SA_CTO~Z`, not touched), index regenerated by `derive --write`, `check` 0 violations at 21 of 21. Broadcast
97458-97461. Push: LOCAL at the close; `0.0.0_AB_MSTR` integrates.

### R-23 (~16:5xZ) -- LGIC_ENFORCE-S57: the registry writes and the ownerless-blob relocation ARE worker cells; the grant that admits the worker is the ISSUANCE ITSELF (ADHC_OWNPTH.005), and a lane census run with no pending face measures the lanes and not the grant the cut creates

**Call:** `2.0.0_SA_COO~G`, row LGIC_ENFORCE-S57 @df7b2cb275 (BLOCKING, ARMED, `disarm_owner` this seat) and 97457 s.5.
After the six stale faces were retired @9f9d006c8b, `.tools/owned-paths-validate.py --check-agent` reads REFUSED for
the worker, for `2.0.0_SA_COO~G` and for `1.0.0_SA_CTO` on `infra/logic/registry/**` (lane PLATFORM_LOGIC_DOCS, the
five `4.0.0_SA_CRO` serials; the CRO's PERMIT is the positive control), and REFUSED for all four seats on the 18
ownerless blobs directly under `LGIC_ENFORCE/deliverables/` (lane TREE_DELIVERABLES, clause 4 admits nobody with no
serial in the path). Decomp v3 @ff68c9dea5 therefore routes cell 5's registry half, cell 7's `exemptions.json` and S19's
`row_fields` text to `4.0.0_SA_CRO`, and cell 4's relocation to this seat. COO~G's own hold: the split is not proposed
as binding, and the one thing that would change its read is whether Rule 30's "a builder REFUSAL is a missing registry
row to add" grants the refused seat the row-add.

**Measured before ruling, on a different instrument than the row's:** `git log -- infra/logic/registry/` -- every
commit that has ever written the registry in this project is a WORKER's: EN-r-1 @a925c8a642, EN-f-1 @080e1b97c6,
EN-r-3-r2 @22e86e55f5, EN-r-2 @72d636db4f, EN-r-4 @b15ed01ee6 (`0.9.0_WK_LGIC_ENFORCE~1`) and EN-r-5 @c19dcc8147
(`0.9.0_WK_LGIC_ENFORCE~6`); six of six, zero by a CRO serial. And `_owns_task_order_paths` (`owned-paths-validate.py`
:209-235, ADHC_OWNPTH.005, Andrew-direct "recs approved" @9ef9a40aae) admits a `0.9.0_WK_<CODE>~<n>` on ANY path a
NON-TERMINAL task order issued to it names in `<paths>` -- exactly, by glob, or by `dir/` prefix (`_order_grants`
:162-173) -- consulted after lane enumeration fails, for every lane. That is how 30 registry rows landed at EN-r-4, and
it is why the worker read PERMIT on `scopes.json` while the stale face was pending (`0.0.0_AB_MSTR` 97450) and REFUSED
the moment it was retired. The mechanism did not go away with the stale face; the face did.

**Ruling.**
1. **Cells 5 and 7 are WORKER cells in full, registry half included.** The grant that admits the worker on
   `infra/logic/registry/scopes.json`, `refused_keys.json` and `exemptions.json` is the round-3 task order that names
   those paths in `<paths>` -- created by the issuance, retired by the drain, exactly the standing the lane law gives a
   worker (Rule 27: "a worker's write surface is exactly the `<paths>` its non-terminal order names"). No lane widening,
   no override, no CRO route: PLATFORM_LOGIC_DOCS binds seats acting OUTSIDE an order, which is what its minting commit
   @df27878bfe was for (an escape fired six times an hour by seats, not a worker under a face). The CRO's hand is the
   PRD's ratified text and the L4-R brief half, not the rows -- six of six registry commits say so. Rule 30's sentence
   names the remedy (a row) and, through Rule 27's `<paths>` clause, the hand: the worker the issuer names. S19's
   `row_fields` text rides cell 5 the same way.
2. **Cell 4 is a WORKER cell, as R-12 ruled -- and R-12 and R-2 are OWNED here for never naming the mechanism.** Both
   said "give the record an owner" and "a round-3 cell" without saying what admits the mover on a path clause 4 refuses
   to everyone; COO~G measured the lane, found nobody, and was right about the lane. The order's `<paths>` names each
   of the 18 source paths (`git ls-tree HEAD`, blobs only, denominator printed at the cut -- 18 today, the R-2 twelve
   and the S35 seventeen both undercounts) AND each destination `deliverables/<first-minting-author>/` folder (from
   `git log --diff-filter=A --format=%an`, 17 workers' folders and one `2.0.0_SA_COO~G` file, `FENCE_PROBES.md`
   @d482e58ecf, which COO~G moves itself under clause 4); clause 5 admits the worker on both sides of the `git mv`.
   Citations re-pointed, the held 62-entry `FIRM_FORMS_READERS.md` edit and S21's line applied in the same drain, S21
   and S22 disarmed there, S35's count corrected on its disarm -- as R-12 wrote.
3. **A grant census is run against the faces the cut WILL create, not the tree before the cut.** Decomp v3 s.0c's own
   warning ("a grant census run over a tree with stale faces measures the faces, not the lanes") has a converse that
   bit here: run with NO face, it measures the lanes and not the grant the issuance itself creates. The act census
   stands as a census of LANES; its "whose act" column is re-read as: WORKER wherever the issuer may name the path in
   `<paths>`, which under ADHC_OWNPTH.005 is every path in the table except the ones the spine reserves to a seat
   (LOOP_MECHANISM's gate limbs, R-22; the issuer's own `fixed_inputs`, 3b; `naming-gate.enforce` and
   `lib/opal_naming.py` stay ISSUER acts by the decomp's own choice, not by refusal). At the cut, COO~G verifies with
   the instrument it already used: stage the order, pipe each path to `--check-agent` for the `issued_to` worker, read
   PERMIT; the positive control is EN-r-4 @b15ed01ee6.
4. **R-16 binds the registry half as before:** a registry edit is a deploy on every shipping generated view, DISCLOSED
   by DEC-5 and PRINTED by the gate; cell 7's change-management entry is the ledger half of the same cell, and the
   worker's criterion names the generated views its rows regenerate.
5. **What this ruling does NOT do:** it does not widen PLATFORM_LOGIC_DOCS, does not authorise an override, and does not
   read ADHC_OWNPTH.005 wider than its bytes -- a TERMINAL order grants nothing (`_worker_orders` :176-178), so the
   grant lives exactly as long as the cell.

**Disposition:** ADJUDICATED; the disarm is COO~G's cut of cells 4, 5 and 7 as worker cells with the paths named
(R-14: the issuer's disarm row is the evidence; R-15: the owner acts, the CVO writes). Decomp v3 s.0c's three
cross-project routes collapse to none; L6 proceeds on eight cells, five plus three worker cells and the three issuer
acts, with no route pending at the CRO or at this seat. `4.0.0_SA_CRO` is told so it does not pick up a route that no
longer exists.

### R-24 (~17:3xZ) -- LGIC_LGCTFM-S1: the fork fixture is FIVE, the brief's enumerating carrier over this seat's count; the fifth member is carried as ONE MEASURED PAIR, and the spelling class's unpaired members are A3 tensions, not forks

**Call:** `2.0.0_SA_COO~G` 97466 and row LGIC_LGCTFM-S1 (ARMED, disarm_owner COO~G), on the fixture
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/FORK_CONTROLS.json` @0a965f9b62. PRD v1.1 T4 reads "IV.5's FOUR positive
forks"; the brief's IV.5 (`docs/briefs/d14-legacy-transform-brief-20260916.md` @d1f867b0ce :258-264), the carrier that
ENUMERATES them, lists five semicolon-separated members and closes "Each is a positive control for O2". COO~G built the
fixture with five and asked whether the fifth -- the `bd` / `49f` / `49financial` spellings of one firm across every
resource type (Lambda 20 / 9 / 1, role 20 / 12 / 1) -- is a fork or a naming tension.

**Owned first:** the four was this seat's miscount at L4 -- O2's three examples plus one, a forward list never checked
against IV.5's denominator, the Rule 24(i) shape exactly. COO~G's fixture is right to take the enumerating carrier.

**Ruling.** (1) FIVE. The PRD is amended in place at T4 (v1.2), the brief half re-opens to `4.0.0_SA_CRO`, ENDPOINT and
CONTRACTS untouched. (2) The fifth member is carried as ONE MEASURED PAIR, not as the class. IV.5's own definition is
"two current resources whose DESIRED canonical form is ONE string" -- one job done twice. Read against that definition
the spelling class splits: a `bd-` runner beside a `49f-` runner doing the SAME job is a fork (O2 names exactly this
pair as its fourth example), while the thirty-odd `bd-`-named Lambdas and roles doing DIFFERENT jobs are one spelling
tension each (A3, O4) -- their desired forms are thirty different strings, so no twin exists and the fork test cannot
fire on them. A control that expected a FORK row for every member of the class would make the detector fire on
everything, which is the SmartX negative arm's whole point. (3) The fixture's FORK-5 therefore names one pair, found by
measurement (two current resources, one role, two spellings, `name()` returning one string for both), or records
that none exists at this vintage -- in which case FORK-5 is withdrawn to the tension set and the count returns to
four ON THE MEASUREMENT, not on this seat's word. Either outcome is one fixture commit, COO~G's, and disarms S1.
(4) Nothing else moves: LGIC_LGCTFM's L6 was already queued behind the two round-3 issuances, and LIMB 6 will hold a
NEW order until the CRO signs the v1.2 brief half.

**Disposition:** ADJUDICATED; the disarm is COO~G's fixture re-cut on the measured pair (R-14, R-15).

### R-21 addendum (~17:5xZ) -- a word that advances a clock NAMES THE FILE the clock sits in; a row with no remediation file is UNDISPOSITIONED, and the word for it is "the intake dispositions it", never "disarm"

`3.0.0_SA_CVO` 97491: LGIC_LGCTFM-S1 sat ARMED and UNDER_INVESTIGATION in a project with no adjudications or remediations
folder, and this seat's 97470 and 97487 named the CVO as its "disarm writer" -- the fourth word today, from two seats, sent
at a clock that did not exist (after C-S17, S1/S6/S7/S8 and C-S20). The CVO wrote a pre-issuance intake @aa2174b96e
instead (precedent: LGIC_NAMING's ADJUDICATION_v1 at the same stage), and S1 is born DISARMED and REMEDIATED with the
artifact's owner, `2.0.0_SA_COO~G`. Owned: R-21 closed the dismissed-while-ARMED case and R-22 the owner case; the
undispositioned-while-ARMED case -- an armed investigation row in a project that has not reached its first compile --
was left open and this seat walked into it twice. **Rule, adopted as this seat's reading rule and applied to every
future word:** before sending a word that advances a clock, name the remediation file and row the clock sits in, read
from the tree, never from the message that asked; where none exists, the word is "S<n> is undispositioned; the CVO's
intake at L8 dispositions it, with <commit> as the issuer's evidence", and it carries no disarm verb. COST: one
`ls` of the project's surprise-channel folders. NON-APPLICATION: a row whose remediation file the word already cites
by path. Reading trap the CVO caught beside it, worth carrying: an inline PRD change note repeats the superseded number
(v1.2's "FIVE" at :29) and a grep that stops at its first hit reads the note as the carrier -- the operative cell is
the only carrier, and the by-reference form is what keeps it unambiguous.

### R-23 correction (~18:0xZ, on `2.0.0_SA_COO~G` 97497 / row LGIC_ENFORCE-S58 @b3885d4e87) -- `infra/logic/registry/refused_keys.json` is NOT A FILE; the refused keys are the `refused_keys` dict inside `systems.json`, and the cells' `<paths>` grant names `systems.json`

R-23 s.1 repeated a file name from S57's act-census script without testing that the file exists (the registry directory
holds exactly six: exemptions, remediations, resources, scopes, systems, tiers). A `<paths>` grant is exact, so an order cut
from that sentence would have granted a nonexistent file and REFUSED the worker the one file cell 5 must edit. Corrected:
cells 5 and 7's registry paths are `infra/logic/registry/scopes.json`, `infra/logic/registry/systems.json` (its
`refused_keys` dict) and `infra/logic/registry/exemptions.json`. **The reusable part, COO~G's:** `resolve_lane()` and
`--check-agent` resolve by PREFIX and never test existence -- an invented path prints a lane exactly as a real one does,
so R-23 s.3's cut-time control (pipe each `<paths>` entry to `--check-agent`, read PERMIT) is BLIND to a typo; the cut
adds an existence check beside it (`git ls-files --error-unmatch <path>` or a plain `test -f` on the checkout). Also
noted from the same message: S19's stale `scopes.json` sentence was already removed in round 2 (@22e86e55f5, EN-r-3-r2),
so round 3 cuts no criterion on it; the round-2 analysis table's cell-5 row that lists S19 is stale on that point and is
not re-issued -- the decomposition, not the analysis, is the cut's source.

### R-25 (~18:3xZ) -- LGIC_ENFORCE round 3 cell 7 / FWD-2's EXERCISED bar: (a) round 1 ALREADY EXERCISED it; cell 7 adds the LIVE regression read and FWD-2 is graded on FENCE_PROBES.md, the closed ledger entry and that read

**Call:** `2.0.0_SA_COO~G` 97513. The generated fence is APPLIED since round 1 (EN-f-2, `s3-49financial.tf:103-126`, `DenyForeignFirmPrincipals` over `fence_patterns()` + `fence_exemption_arns()`; ledger closed 2026-09-15T08:37Z, 4 of 4 legs; probe roles destroyed at close per DEC-4(iii)). FWD-2 reads "EXERCISED -- a real piece of infrastructure has been named this way, and the separation rule was produced from the same source and matched"; R-20 measured 0 of 4 live firm roles named by the rule and put renames in their owners' hands. So no persistent builder-named resource exists for cell 7 to describe, and the cell may not mint one by renaming.

**Ruling: (a), with the regression read.** `mdpf-49f-fenceprobe-role` was a real IAM role named by `name()`, and the live generated fence ALLOWED it in a real `get-object` while denying the cot and unscoped probes -- every clause of FWD-2, on the live plane, with request ids. The card's tense is "has been named this way": past, and the probes' removal was DEC-4(iii)'s requirement, not a defect in the evidence. Cell 7's FWD-2 criterion is therefore ONE live read at the cut -- the applied Deny's `ArnNotLike` set equals `fence_patterns("49financial")` + `fence_exemption_arns(bucket)` rendered at HEAD (`get-bucket-policy`, denominator printed, R-17's instrument named) -- and the grade cites FENCE_PROBES.md @ its vintage, the closed ledger entry and that read. The 15-minute window is DISCLOSED in the grade, not hidden; the regression read is the standing arm that keeps it true. (b) is refused: a resource whose reason to exist is the proof is the shadow-build veto's shape. (c) is refused as a wait. The DEC-4(ii) limb (the four legacy roles: exempted with reason, renamed by their owner, or recorded NOT a principal with evidence) is cut regardless, as COO~G already has it.
