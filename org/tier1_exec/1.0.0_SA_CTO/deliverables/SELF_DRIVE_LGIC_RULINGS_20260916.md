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
