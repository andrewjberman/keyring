# CVO REVIEW -- the project-tree prerequisite set (Andrew CALL 3), reviewed ONCE, on this seat's own instrument

**Reviewer:** 3.0.0_SA_CVO base. **Delivered by:** 2.0.0_SA_COO 92797 (22:36Z) + addendum 92801 (22:40Z),
manifest `org/tier1_exec/2.0.0_SA_COO/deliverables/TREE_PREREQ_COMPLETION_MANIFEST_20260902.md` @`710edfd5e0`.
**Authority:** Andrew-direct @`a8d63f097c`, verbatim: *"Project tree prereq builds are mandatory start point
(call 3), split up work with CTO on that, and when you guys are completely done issue it to CVO for review."*
**Review window:** 22:47Z-23:20Z, 2026-09-02, HEAD @`c98904e4d4` at the last read. Every commit named below is
LOCAL until 0.0.0_AB_MSTR pushes (origin/CLOUD @`2f1ba8c604` at 22:03Z, this seat's ls-remote).

## VERDICT

**The set is COMPLETE by its own rule and the builds are REAL.** The generator's real output passes the
gate on the positive path, both halves refuse the same identity error at the control, and no commit in the
set carries this seat's author line. **Two of the four claims COO asked me to grade are PARTIAL**, and both
are the same shape: a refusal that exists as a TOOL nobody is compelled to run, or a reader that was not in
the spec's list of readers. Neither blocks REGISTERING the first tree project (that act is 0.0.0_AB_MSTR
running `check` by hand, and Andrew has said "very gingerly"). **Both should be closed before the first tree
TO is CUT** -- that is my reading of where the gates fail open; the sequencing is Andrew's.

| claim (COO 92797) | grade | one line |
|---|---|---|
| (a) the contract is ONE shape both halves built against | **PASS, with 2 named divergences** | generator-valid project -> gate PASS; but R4 and R2 bind in `check` only, and the contract carries no VALUE enum for `dep_stage`/`fabric` (the gate does) |
| (b) the refusals bind | **PARTIAL** | R1-R5 fire when `missions-tree-index check` RUNS. **No commit-time surface runs it: 0 of 56 hook/wrapper files name it; 31-file census, both pages.** A refusal is APPLIED only at MSTR's hand |
| (c) the dual-register period is honest | **PARTIAL** | the FOUR s.7 readers read both roots (CTO 27/27, 19/19, 22/22 stand). **Six more TO readers read ONE root, one of them a commit HOOK** (`to-proof-of-spec-check.sh:33`). Flat 352: untouched by the builders; one MSTR register edit in the window (below) |
| (d) certifier != author | **PASS** | 8 set commits: 4 COO, 4 CTO, 0 CVO. `surprise-watch.sh` body carries 4 CVO commits (passes 1-3); the repoint @`1655d87688` and R4-c @`f2cbab30a1` are CTO's; my core was graded by CTO GREEN 4/4 (215911Z). Stated, not claimed away |

## INSTRUMENT -- what I ran, and that it differs from the builders'

Neither half's harness was re-run (that would be repetition, not corroboration). Three instruments of my own:

1. **Shared-shape probe** (`controls/tree_shared_shape_probe_CVO_20260902.txt`, script in this session's
   scratchpad): a temp estate built with the REAL contract, a byte-copy of the LIVE `MACROS.yaml` (3
   directives, RATIFIED = D11 only), a DIRECTIVES.yaml naming the probe project; `Estate.check` /
   `Estate.derive(write=True)` from `.tools/missions-tree-index.py`, then `_project_row_rel` +
   `check_project_stage` from `.tools/to-pipeline-gate.py` on a TO under the SAME folder. The generator's
   real bytes, the gate's real functions, one temp root. **Neither builder's fixture was used.**
2. **Grain check on the manifest**: every commit's author + `--stat` file list against what its row claims;
   `git diff --stat` of `org/projects/` across the window; `git log --format=%an` over the set's files.
3. **Two censuses with printed denominators**: `comp-find 'missions-tree-index' --files` (both pages) plus a
   python read of 56 named commit-time files; and a python read of 12 named TO-enumerating tools for their
   discovery glob. Plus `missions-tree-index check` live, unscoped: tree=0, flat 352, 0 violations, rc 0.

## FINDINGS

### F-A1. (a) POSITIVE PATH AGREES. One control expectation of mine was set wrong.
Probe case 1: `D11/NFRA/NFRA_COMPEFFICACY` planted per the contract -> `check` = `[INDEX-MISSING]` (the
remedy path) -> `derive --write` wrote `org/projects/NFRA_COMPEFFICACY.json` (11 fields, `home` set) ->
re-`check` 0 violations, generated=1 -> gate resolved `.../NFRA_COMPEFFICACY/project.json` from the PATH and
`check_project_stage` PASS. The transcript prints DISAGREE for this row because my script demanded 0
violations BEFORE derive; INDEX-MISSING before derive is the contract's own remedy sequence. **AGREE, my
label wrong, stated.**

### F-A2. (a) THE GATE NEVER READS `project_code`, SO R4 BINDS IN `check` ONLY.
Probe case 2: row `project_code=NFRA_COMPEFFICAC` under folder `NFRA_COMPEFFICACY` -> generator `[R4]`;
gate PASS (it derives the code from the path and never compares it to the row). Case 4: a project under
`D0/NFRA` (D0 PROPOSED) -> generator `[R2]`; gate PASS. **Both halves are correct for their own question;
the tree's identity and ratification rules are enforced by one of them.** Combined with F-B1 below, a
mis-coded or unratified project.json can be committed, indexed by nobody, and have TOs admitted against it.

### F-A3. (a) THE CONTRACT HAS NO VALUE ENUM; THE GATE DOES.
Probe case 3: `dep_stage=BOGUS fabric=moon` -> generator VALID (`row_required_fields` is presence-only),
`derive --write` INDEXED it; gate REFUSED every TO. Rule 24(iv): two verdict vocabularies over one row --
"valid tree project" and "TO-admissible project" -- with no shared enum. CTO's fixture used `status:
"ACTIVE"`, the generator's `"active"`, live rows `"active"`; nothing validates `status` at all.
**Contract amendment (COO): reference `DEP_STAGE_ENUM` / `FABRIC_ENUM` (the gate's, to-pipeline-gate.py)
as value constraints, and the generator validates them.** One shape, or two documents.

### F-B1. (b) `check` IS A TOOL, NOT A GATE. 0 of 56.
`comp-find 'missions-tree-index' --files` (corpus=all, 145,577 files scanned): 31 files, both pages read.
Code files among them: `.tools/missions-tree-index.py` and `.tools/tests/test_missions_tree_index_selftest.py`
(CloudComp's wrapper @`6eac560149`). Named commit-time surfaces read line by line (`safe-commit.sh`,
`commit-gate.sh`, `ds-precommit-check.py`, every `.tools/hooks/*.sh` and `.tools/git-hooks/*.sh`; 56 files):
**0 lines name the generator.** So "the tree refuses every registration today, by design" (manifest) is true
of `check`'s OUTPUT and false of any commit: a folder under `org/missions/D8/ETFS/...` with a project.json
commits today under lane TIER0_MSTR / TREE_PROJECT_ROW with no refusal fired. DESIRED != APPLIED.
**Proposal (CTO gate + COO tool, not this seat's build): `commit-gate`/`safe-commit` runs
`missions-tree-index check` when a staged path is under `org/missions/D*/` or `org/projects/`, refusing on
rc 1.** Cost: one python run (~0.4 s measured by CloudComp) on those commits only.

### F-C1. (c) SIX TO READERS SEE ONE ROOT; ONE IS A COMMIT HOOK.
The contract lists four repointed readers and names `to-check`/`registry-check`/`fabric-check` as
"readers_of_the_index_unchanged" -- correct for the INDEX. But these tools DISCOVER TASK ORDERS by glob,
and each globs `task_orders/` only (exact lines, read 23:1xZ):
```
  .tools/to-check.py:350                     org/**/task_orders/*.md
  .tools/proof-of-spec-check.py:404, :486    */task_orders/*.md  (ls-files + rglob)
  .tools/to-decomp-ref-lint.py:215           task_orders/*.md
  .tools/to-liveness-join.py:76              org/**/task_orders/*.md
  .tools/loop-quiescence:159                 */task_orders/{macro}.*.md
  .tools/git-hooks/to-proof-of-spec-check.sh:33   grep -E '(^|/)task_orders/[^/]+\.(md|xml)$'  <-- HOOK
```
Consequence: a tree TO under `task-orders/` is invisible to `/to-check` and the dashboard, to the
decomp-ref lint, to the liveness join, to loop-quiescence -- and **the ISSUANCE LINT hook does not fire on
it**, so a NEW tree TO without `<proof_of_spec>` is admitted. `to-pipeline-gate.py` (repointed) still runs
its limbs on it, so the tree TO is not ungated; it is un-LINTED and un-LISTED. Denominator: 12 named tools
read; 1 (`to-pipeline-gate.py`) reads both roots; 6 read one root; 5 do not discover TOs by glob.
**Proposal (CTO): repoint the six to the contract's `task_orders_glob` alongside `task_orders/`.** Whether
the spec's s.7 list SHOULD have contained them is COO's to say; the estate's behaviour on the first tree TO
does not care which list they were on.

### F-C2. (c) FLAT 352 UNTOUCHED BY THE BUILDERS; ONE MSTR EDIT IN THE WINDOW; THE D8 CENSUS PREDATES IT.
`git diff --stat cb6e93e7f8~1 HEAD -- org/projects/` = **1 file, 17/17 lines**: `GLOBALALARM.json`
`directive: D10 -> D8` by 0.0.0_AB_MSTR @`2fa0e0b29f` (22:13Z), a register move, not tree work. None of
the 8 set commits touch `org/projects/`. OBSERVATION for 2.0.0_SA_COO (not a defect: flat rows are not
tree-bound, `prospective_only: true`): the D8 macro census in `MACRO_ENUM_RULE24_D0_D8_D11_20260902.md`
(@`cb6e93e7f8`, ~21:1xZ) now has a D8 member whose `macro_code` (`GLOBALALARM`) is not in D8's proposed
enum `[ETFS, MDPF, AUTH]` and fails the macro regex `^[A-Z]{4}$`. The proposal Andrew will ratify for D8
is one row stale. The macro layer for GLOBALALARM is a naming act at MSTR (4-letter macro), flagged.

### F-C3. (c) GENERATED INDEX ENTRIES CARRY 11 FIELDS; HAND-WRITTEN ROWS CARRY 18.
A generated entry lacks `blocking, created, leads, phase, pipeline, pods, related`. Read against the
unchanged readers: `registry-check.py` uses `d.get` throughout (build_rows :239-274) and surfaces malformed
rows rather than failing; `to-check.py get_hot_prd_project_codes` reads `project_code` only. **Unread:**
`fabric-check.py`, `/drive step 2`, and any `registry-check` consumer that prints `phase`/`blocking` -- the
first generated entry will print empty there. Not a refusal anywhere I read; stated as the unread remainder.

### F-D1. (d) HOLDS, WITH THE DEPENDENCY NAMED.
Authors of the 8 set commits: COO x4 (`cb6e93e7f8`, `1223c343fe`, `5f8b774a5d`, `db8fc37e45`,
`710edfd5e0`), CTO x3 (`20d1c60866`, `1655d87688`, `fa44d04e2c`); CVO 0. `--stat` of each matches its
manifest row. `surprise-watch.sh` is the one file with CVO bytes (passes 1-3); CTO repointed and extended
it and graded my core GREEN 4/4 on real bytes. The certifier of the SET authored none of the SET.

## RESIDUALS I ADD TO THE MANIFEST'S (owners named; none is this seat's build)

| # | what | owner | when |
|---|---|---|---|
| R-i | wire `missions-tree-index check` into the commit path for `org/missions/D*/**` + `org/projects/` (F-B1) | 1.0.0_SA_CTO (gate) + 2.0.0_SA_COO (tool) | before the first tree TO is cut |
| R-ii | repoint the six one-root TO readers, the issuance hook first (F-C1) | 1.0.0_SA_CTO | before the first tree TO is cut |
| R-iii | contract v0.1.1: value enums for `dep_stage`/`fabric` by reference to the gate's; generator validates (F-A3) | 2.0.0_SA_COO | with the first registration |
| R-iv | gate reads `row.project_code` and refuses on mismatch with the folder (F-A2) -- ~3 lines in `check_project_stage` | 1.0.0_SA_CTO | with R-i |
| R-v | D8 census one row stale after GLOBALALARM's move (F-C2) | 2.0.0_SA_COO / 0.0.0_AB_MSTR | before Andrew ratifies D8 |

## WHAT THIS VERDICT IS NOT
Not a GO for registration (Andrew's, "when the time comes", @`a258e3060f`). Not a re-grade of CTO's 27/27,
19/19, 22/22 or COO's 18/18 -- those stand on their transcripts and I did not repeat them. Not a claim that
`fabric-check.py` or `/drive step 2` accept a generated entry -- unread, named above.
