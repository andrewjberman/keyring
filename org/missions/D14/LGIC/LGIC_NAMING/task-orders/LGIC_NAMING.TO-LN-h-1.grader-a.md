# TO LGIC_NAMING.TO-LN-h-1 -- hand-grader A

<to_id>LGIC_NAMING.TO-LN-h-1</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~7</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.4 @e04b802fe9 (ADMITTED @254ac1f2ab) | **Decomp cell:** `LN-h-1` | **outcome_ref:** FWD-5 | **depends_on:** LN-g-1 (merged before this slot is spawned) | **slot:** ~7, queue position 1

---

## WORKER FACE

### THE CELL

`LN-h-1` -- hand-grader A (PRD candidate N6). **You did not write the rule, and you must not see the other grader's answers.**

**Grade every name in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N6_SAMPLE.json`** -- the 85 `discriminating` names and the 3 `overlap` names -- by hand, using ONLY `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`, `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`, and what the rule itself cites (`org/standards/NAMING_SCHEMA.json`, `infra/logic/05_IDENTITY_SPINE.md`). Do NOT read the rule author's other files, any file under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/` except your own, `N3_*`, `N5_*`, the decomposition or this project's task orders.

**Write `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n6-grader-a.tsv`:** the first line `# base <sha>` (the output of `git rev-parse HEAD` in your worktree BEFORE your first commit); then one line per sample name: `<type><TAB><name><TAB><verdict><TAB><canonical_form>`, verdict one of CONFORMANT, ALIAS, OUT-OF-PATTERN, RAISE, NOT-GRADED (canonical_form empty where none). A NOT GRADED type gets NOT-GRADED. A name the rule cannot place gets RAISE -- never a guess.

**Read:** GRADING_RULE.md, LEGACY_SERVED_PATHS.json, NAMING_SCHEMA.json, 05_IDENTITY_SPINE.md, N6_SAMPLE.json.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="H1-AC1" cell_refs="LN-h-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py h1-graded</invocation><expect>VERDICT: PASS-ALL-GRADED</expect></criterion>
`H1-AC1` -- every one of the 88 sample names carries one of the five verdict values.

<criterion id="H1-AC2" cell_refs="LN-h-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py h1-base</invocation><expect>VERDICT: PASS-BASE-RECORDED</expect></criterion>
`H1-AC2` -- the file records the worktree base commit it was graded from.

<expected_criteria>H1-AC1, H1-AC2</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). Reading the live plane is done for you: the fixed inputs below are one pull, at one vintage, and you read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_ln.py` (the checker every criterion calls), `LIVE_NAMES.json` (every live AWS name by node type, vintage 2026-09-14 12:13:53 UTC, 2,531 nodes, 33 types), `N6_SAMPLE.json`, `N3_ITEMS.json`, `N3_KEY.json`, `N5_ADDRESSES.json`, `N5_KEY.json`. Read only those this order names. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n6-grader-a.tsv
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v3 @62b5c0819f, cell `LN-h-1`.
<owned_cells>LN-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `H1-AC1`, `H1-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~7/LGIC_NAMING.TO-LN-h-1.grader-a.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> H1-AC1,H1-AC2` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `grader-a.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- self-test 6/6; the 540 s view scanned 5 of 5 carriers, 25 gates armed, none on LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (LGIC_ENFORCE E9's comparison half), G-C (worker admission, checked after this issuance) and G-D (the three-writer .tf). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on the write set, not assumed: 13 markdown/TSV/JSON records under deliverables/ and one comment-only hunk in one .tf; no cell adds an operation, a policy, a principal or a resource, so the lens would receive an empty input.
comp-adversary: RUN at L5 on the PRD at v1.3 -- 6 of 6 cited commits verified; 11 cited paths, 9 stable, 2 GONE (GRADING_RULE.md and TENSION_RANKING.md, which this project mints). Not re-run at v1.4: that diff adds no cited path or commit. Blindness stated: its complement is filesystem adjacency (T11), not the dependency chain.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, or under infra/aws/, refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~7, queue position 1. Round 1 of LGIC_NAMING; issued by `2.0.0_SA_COO~G` on Andrew-direct ~13:4xZ ruling 1 (relayed 96594, record @0d3ad7d496). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: one live pull at vintage 2026-09-14 12:13:53 UTC (manifest b578e47d733f). The N6 sample is 85 + 3 by the decomposition's rule over distinct names (row LGIC_NAMING-S11).
