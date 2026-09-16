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
a class finding beside R-2's. Round 2 is ONE issuance by `2.0.0_SA_COO~G` over the cell table in s.3 of the
analysis; C6 stays NOT CUT.

**Binds:** `2.0.0_SA_COO~G` (the recut); `4.0.0_SA_CRO` (X8); LGIC_NAMING and LGIC_ENFORCE rounds (routes named in the
analysis). No PRD addendum: no outcome was wrong, incomplete or obsolete at this read.
