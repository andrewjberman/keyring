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
