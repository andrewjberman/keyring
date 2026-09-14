# TO LGIC_NAMING.TO-LN-f-1-r2 -- one pattern per firm, with a RAISE disposition

<to_id>LGIC_NAMING.TO-LN-f-1-r2</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.6 @2706014705 (ADMITTED @8e08704fb0) | **Decomp cell:** `LN-f-1` (round 2) | **outcome_ref:** FWD-3 | **depends_on:** -- (level 0; LN-g-1's GRADING_RULE.md is at HEAD since round 1) | **slot:** ~4, queue position 1

---

## WORKER FACE

### THE CELL

`LN-f-1` -- one pattern per firm, round 2 (PRD candidate N4; round-1 analysis s.1 FWD-3 and s.7 item 6; row LGIC_NAMING-W1-S5). Round 1 met FWD-3 with one qualification: the output shape had no place for a role whose grade is a RAISE, so `wp5-49f-feeder-scheduler-role` was filed under `excluded`. Round 2 adds the third disposition (the row's option b) before LGIC_ENFORCE's census reads the list.

**What you build: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md`**, prose plus ONE fenced ```json block:

```
{"patterns": {"49financial": "<glob>", "inflection": "<glob>", "cottonwood": "<glob>", "demo": "<glob>"},
 "attributed": {"<firm>": [{"name": "<live role name>", "canonical": "<its canonical form by the rule>"}]},
 "excluded": [{"name": "<live role name>", "reason": "<why it is no firm's principal>"}],
 "raise": [{"name": "<live role name>", "step": "<the GRADING_RULE.md step that raised, for example R1.f>", "why": "<what the rule cannot place>"}],
 "denominator": {"iam_roles_live": <n>, "with_a_firm_alias_token": <n>, "attributed": <n>, "excluded": <n>, "raise": <n>}}
```

- **The population** is every live `IAM_ROLE` in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json` whose name carries a firm alias token (`bd`, `49f`, `49financial`, `inf`, `inflection`, `cot`, `cottonwood`, `demo`, split on `-` and `_`). Grade each by `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` to its canonical form and its firm. `bd` is the vendor Black Diamond in a system or source position, and the firm 49 Financial otherwise -- as the rule says.
- **Three dispositions.** A role the rule places goes to `attributed` under its firm. A role that is no firm's principal goes to `excluded`, with its reason. A role whose grade is a RAISE goes to `raise`, with the step that raised and why -- never to `excluded`.
- **One pattern per firm**, written from S3-S5: an fnmatch-style glob, the shape an IAM `ArnLike` condition takes, over the CANONICAL role names. Each firm's pattern catches every one of its attributed canonical forms and none of another firm's.
- Round 1's `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n4-firm-patterns.md` is your starting point; re-grade under NAMING_SCHEMA.json v1.6. Print the denominators.

**Read:** GRADING_RULE.md, NAMING_SCHEMA.json (v1.6), 05_IDENTITY_SPINE.md, LIVE_NAMES.json, round 1's n4-firm-patterns.md.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F1R-AC1" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py f1-one</invocation><expect>VERDICT: PASS-ONE-EACH</expect></criterion>
`F1R-AC1` -- exactly one non-empty pattern for each of the four firm keys.

<criterion id="F1R-AC2" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py f1-catch</invocation><expect>VERDICT: PASS-CATCHES-ALL</expect></criterion>
`F1R-AC2` -- each firm's pattern matches every canonical form attributed to that firm.

<criterion id="F1R-AC3" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py f1-cross</invocation><expect>VERDICT: PASS-NO-CROSS</expect></criterion>
`F1R-AC3` -- no firm's pattern matches a canonical form attributed to another firm.

<criterion id="F1R-AC4" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py f1-covered</invocation><expect>VERDICT: PASS-COVERED</expect></criterion>
`F1R-AC4` -- every live IAM_ROLE carrying a firm alias token is attributed, excluded with a reason, or raised with a step.

<criterion id="F1R-AC5" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py f1-raise</invocation><expect>VERDICT: PASS-RAISE-DISPOSED</expect></criterion>
`F1R-AC5` -- the shape carries a raise list; every RAISE names its step and why, and no exclusion's reason is a RAISE.

<criterion id="F1R-J1" cell_refs="LN-f-1" judgment="true"/>
`F1R-J1` -- graded at L9 by 3.0.0_SA_CVO: each attribution and canonical form follows GRADING_RULE.md, each exclusion's reason holds, and each RAISE names the step that raised. RECORD; NO VERDICT.

<expected_criteria>F1R-AC1, F1R-AC2, F1R-AC3, F1R-AC4, F1R-AC5, F1R-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). The fixed inputs are one live pull, at one vintage; read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's (`check_ln.py`, `LIVE_NAMES.json`, `N6_SAMPLE.json`, `N3_ITEMS.json`, `N3_KEY.json`, `N5_ADDRESSES.json`, `N5_KEY.json`), and `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's (`check_ln_r2.py`, the checker every criterion calls; `blind_seat.py`, the clean-context seat; `N3_KEY_R2.json`; `N5_R2.json`). Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v4 @32795c348c, cell `LN-f-1`, round 2 (section 0c).
<owned_cells>LN-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F1R-AC1`, `F1R-AC2`, `F1R-AC3`, `F1R-AC4`, `F1R-AC5`, `F1R-J1`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~4/LGIC_NAMING.TO-LN-f-1-r2.firm-patterns.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F1R-AC1,F1R-AC2,F1R-AC3,F1R-AC4,F1R-AC5,F1R-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `firm-patterns.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut -- --budget 540, 5 of 5 carriers (C1 207, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (LGIC_ENFORCE E9's comparison half; met by round 1's LN-h-3 @d292bca3ba), G-C (worker admission, checked after this issuance) and G-D (the three-writer .tf; round 1's, and no round-2 cell touches the .tf). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set, not assumed: TSV, JSON and markdown records under deliverables/exercises/r2/ and the seat records beside them; no cell adds an operation, a policy, a principal or a resource, and the seat is a local claude process with no tools, so the lens would receive an empty input.
comp-adversary: RUN at the recut on the PRD at v1.6 (@2706014705) -- 7 of 7 cited commits verified; 13 cited paths, 13 stable, 0 flagged. Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~4, queue position 1. Round 2 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md` @de52d3db04 (SC1 corrected @2706014705)); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v4 @32795c348c, section 0c.
