# TO LGIC_NAMING.TO-LN-f-1 -- one pattern per firm

<to_id>LGIC_NAMING.TO-LN-f-1</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.4 @e04b802fe9 (ADMITTED @254ac1f2ab) | **Decomp cell:** `LN-f-1` | **outcome_ref:** FWD-3 | **depends_on:** LN-g-1 (its rule, merged before you start) | **slot:** ~1, queue position 2

---

## WORKER FACE

### THE CELL

`LN-f-1` -- one pattern per firm (PRD candidate N4). **You start after LN-g-1 is merged; `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` is at HEAD in your worktree.**

**What you build: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n4-firm-patterns.md`**, prose plus ONE fenced ```json block:

```
{"patterns": {"49financial": "<glob>", "inflection": "<glob>", "cottonwood": "<glob>", "demo": "<glob>"},
 "attributed": {"<firm>": [{"name": "<live role name>", "canonical": "<its canonical form by the rule>"}]},
 "excluded": [{"name": "<live role name>", "reason": "<why it is no firm's principal>"}],
 "denominator": {"iam_roles_live": <n>, "with_a_firm_alias_token": <n>, "attributed": <n>, "excluded": <n>}}
```

- **The population** is every live `IAM_ROLE` in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json` whose name carries a firm alias token (`bd`, `49f`, `49financial`, `inf`, `inflection`, `cot`, `cottonwood`, `demo`, split on `-` and `_`). Grade each by `GRADING_RULE.md` to its canonical form and its firm. `bd` is the vendor Black Diamond in a system or source position, and the firm 49 Financial otherwise -- as the rule says. A role that is no firm's principal goes to `excluded`, with its reason.
- **One pattern per firm**, written from S3-S5: an fnmatch-style glob, the shape an IAM `ArnLike` condition takes, over the CANONICAL role names. Each firm's pattern catches every one of its attributed canonical forms and none of another firm's.
- Print the denominators.

**Read:** GRADING_RULE.md (at HEAD after LN-g-1), NAMING_SCHEMA.json, 05_IDENTITY_SPINE.md, LIVE_NAMES.json.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F1-AC1" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py f1-one</invocation><expect>VERDICT: PASS-ONE-EACH</expect></criterion>
`F1-AC1` -- exactly one non-empty pattern for each of the four firm keys.

<criterion id="F1-AC2" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py f1-catch</invocation><expect>VERDICT: PASS-CATCHES-ALL</expect></criterion>
`F1-AC2` -- each firm's pattern matches every canonical form attributed to that firm.

<criterion id="F1-AC3" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py f1-cross</invocation><expect>VERDICT: PASS-NO-CROSS</expect></criterion>
`F1-AC3` -- no firm's pattern matches a canonical form attributed to another firm.

<criterion id="F1-AC4" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py f1-covered</invocation><expect>VERDICT: PASS-COVERED</expect></criterion>
`F1-AC4` -- every live IAM_ROLE carrying a firm alias token is attributed or excluded with a reason.

<criterion id="F1-J1" cell_refs="LN-f-1" judgment="true"/>
`F1-J1` -- graded at L9 by 3.0.0_SA_CVO: each attribution and canonical form follows GRADING_RULE.md, and each exclusion's reason holds. RECORD; NO VERDICT.

<expected_criteria>F1-AC1, F1-AC2, F1-AC3, F1-AC4, F1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). Reading the live plane is done for you: the fixed inputs below are one pull, at one vintage, and you read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_ln.py` (the checker every criterion calls), `LIVE_NAMES.json` (every live AWS name by node type, vintage 2026-09-14 12:13:53 UTC, 2,531 nodes, 33 types), `N6_SAMPLE.json`, `N3_ITEMS.json`, `N3_KEY.json`, `N5_ADDRESSES.json`, `N5_KEY.json`. Read only those this order names. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n4-firm-patterns.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v3 @62b5c0819f, cell `LN-f-1`.
<owned_cells>LN-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F1-AC1`, `F1-AC2`, `F1-AC3`, `F1-AC4`, `F1-J1`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-f-1.firm-patterns.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F1-AC1,F1-AC2,F1-AC3,F1-AC4,F1-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `firm-patterns.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 2. Round 1 of LGIC_NAMING; issued by `2.0.0_SA_COO~G` on Andrew-direct ~13:4xZ ruling 1 (relayed 96594, record @0d3ad7d496). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: one live pull at vintage 2026-09-14 12:13:53 UTC (manifest b578e47d733f). The N6 sample is 85 + 3 by the decomposition's rule over distinct names (row LGIC_NAMING-S11).
