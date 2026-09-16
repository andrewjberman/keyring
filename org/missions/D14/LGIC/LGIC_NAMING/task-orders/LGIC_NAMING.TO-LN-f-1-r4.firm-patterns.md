# TO LGIC_NAMING.TO-LN-f-1-r4 -- the firm patterns re-graded, every gap raised

<to_id>LGIC_NAMING.TO-LN-f-1-r4</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete -- 0.9.0_WK_LGIC_NAMING~4 @6ed5fe6493 (deliverable), proof-of-spec instance at org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~4/LGIC_NAMING.TO-LN-f-1-r4.firm-patterns.proof_of_spec.json validated rc=0; F1R4-AC1..AC5 PASS-by-output, F1R4-J1 RECORDED for 3.0.0_SA_CVO at L9; row LGIC_NAMING-W4-S3 filed (OBSERVATION, INERT)</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.8 @2f554182b6 (ADMITTED; brief half signed @b136cdc308, review @02529e1bce) | **Decomp cell:** `LN-f-1` (round 4) | **outcome_ref:** FWD-5, FWD-3 | **depends_on:** LGIC_ENFORCE EN-r-2 (the registry rows for the 115 tokens) merged to CLOUD, AND the G-V19 group (LN-g-1, LN-g-2, EN-r-3, NAMING_SCHEMA v1.9) merged to CLOUD | **slot:** ~4, queue position 1

---

## WORKER FACE

### THE CELL

`LN-f-1` -- one pattern per firm, round 4: the canonical forms re-graded at the registry and rule of your base, and every gap raised (round-3 analysis s.1 FWD-5 and s.3 items 3 and 4; row W4-S1). Round 2 attributed 68 live roles to their firms; 48 of their canonical forms carry `{system}`, because the name does not carry its system. FWD-5 grades REALIZED when no placeholder remains except where the registry has no row, and there the grade RAISES the missing row (CLAUDE.md Rule 30: a missing row is a row to add, never a guess).

**What you build: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r4/n4-firm-patterns.md`**, prose plus ONE fenced ```json block:

```
{"patterns": {"49financial": "<glob>", "inflection": "<glob>", "cottonwood": "<glob>", "demo": "<glob>"},
 "attributed": {"<firm>": [{"name": "<live role name>", "canonical": "<its canonical form by the rule>"}]},
 "excluded": [{"name": "<live role name>", "reason": "<why it is no firm's principal>"}],
 "raise": [{"name": "<live role name>", "step": "<the GRADING_RULE.md step>", "why": "<what cannot be placed>", "missing_row": "<the registry row that would place it>"}],
 "denominator": {"iam_roles_live": <n>, "with_a_firm_alias_token": <n>, "attributed": <n>, "excluded": <n>, "raise": <n>, "placeholders_filled": <n>, "placeholders_raised": <n>}}
```

- **The population** is every live `IAM_ROLE` in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json` whose name carries a firm alias token (`bd`, `49f`, `49financial`, `inf`, `inflection`, `cot`, `cottonwood`, `demo`, split on `-` and `_`).
- **Grade each BY HAND** from `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` at your base, to its canonical form and its firm. Fill `{system}` from the identity registry at your base (`infra/logic/registry/`: `systems.json`, and any resource-to-system rows present). `gateway` is a registered system there (PLATFORM_SUBSYSTEM, owner D9; the issuer's gateway commit, landed ahead of round 4). `bd` is governed by R3, quoted here from the rule at the cut and never paraphrased (row W4-S1):

  > **R3 `bd`** is refused in every slot (S10). It is the VENDOR `blackdiamond` when a V4 firm token is next to it,
  > before or after, and the FIRM `49financial` otherwise. CENSUS s.1 item 4 gives both readings: in
  > `bd-49f-session-trigger` it is the vendor, in `bd-allocations` the firm. Either way it is an alias, and the canonical
  > form spells `blackdiamond`, or the firm's form for the slot. The test is ADJACENCY to a V4 firm token, never position:
  > `bd` first with no firm token next to it (`bd-allocations`) is the firm, and `bd` next to a firm token wherever it sits
  > (`bd-49f-...` first, `cot-bd-session-trigger-lambda-role` second) is the vendor (row `LGIC_NAMING-W4-S1`).

  If R3 at your base reads differently, your base governs, and your result names the difference.
- **Three dispositions.** A role the rule places goes to `attributed` under its firm. A role that is no firm's principal goes to `excluded`, with its reason. A role whose grade is a RAISE goes to `raise`, with its step and why.
- **Every gap is raised.** An attributed form that still carries a placeholder after the registry fill is ALSO a `raise` entry for the same name, with its `step`, its `why`, and a `missing_row` naming the row that would fill it. Print how many placeholders the registry filled and how many you raised.
- **One pattern per firm**, written from S3-S5: an fnmatch-style glob over the CANONICAL role names, the shape an IAM `ArnLike` condition takes. Each firm's pattern catches every one of its attributed canonical forms and none of another firm's.
- Round 2's `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md` is your starting point. Print the denominators.

**Read:** GRADING_RULE.md and `NAMING_SCHEMA.json` at your base; `infra/logic/registry/*.json` at your base; LIVE_NAMES.json; round 2's n4-firm-patterns.md.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F1R4-AC1" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py f1-covered</invocation><expect>VERDICT: PASS-POPULATION-COVERED</expect></criterion>
`F1R4-AC1` -- every live IAM_ROLE carrying a firm alias token is attributed, excluded with a reason, or raised with a step.

<criterion id="F1R4-AC2" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py f1-regrade</invocation><expect>VERDICT: PASS-FORMS-EQUAL-GRADE</expect></criterion>
`F1R4-AC2` -- every attributed canonical form equals what `grade()` returns at your tree.

<criterion id="F1R4-AC3" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py f1-gaps</invocation><expect>VERDICT: PASS-EVERY-GAP-RAISED</expect></criterion>
`F1R4-AC3` -- every attributed form still carrying a placeholder is raised with its step and its missing row.

<criterion id="F1R4-AC4" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py f1-catch</invocation><expect>VERDICT: PASS-CATCHES-EVERY-OWN</expect></criterion>
`F1R4-AC4` -- each firm's pattern matches every canonical form attributed to that firm.

<criterion id="F1R4-AC5" cell_refs="LN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py f1-cross</invocation><expect>VERDICT: PASS-NO-FIRM-CROSSES</expect></criterion>
`F1R4-AC5` -- no firm's pattern matches a canonical form attributed to another firm.

<criterion id="F1R4-J1" cell_refs="LN-f-1" judgment="true"/>
`F1R4-J1` -- graded at L9 by 3.0.0_SA_CVO: each attribution follows R3 as quoted and the rest of GRADING_RULE.md; each exclusion's reason holds; each `missing_row` names a real registry gap, never a guessed system. RECORD; NO VERDICT.

<expected_criteria>F1R4-AC1, F1R4-AC2, F1R4-AC3, F1R4-AC4, F1R4-AC5, F1R4-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. The registry and the rule are NOT yours: a missing row is a `raise` entry, never an edit. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). The fixed inputs are one live pull, at one vintage; read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds rounds 1-3's inputs (`LIVE_NAMES.json` and the rest; `r2/`, `r3/`), and `fixed_inputs/r4/check_ln_r4.py` is round 4's checker, which every criterion calls. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r4/n4-firm-patterns.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v6, cell `LN-f-1`, round 4 (section 0e).
<owned_cells>LN-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F1R4-AC1`, `F1R4-AC2`, `F1R4-AC3`, `F1R4-AC4`, `F1R4-AC5`, `F1R4-J1`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~4/LGIC_NAMING.TO-LN-f-1-r4.firm-patterns.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F1R4-AC1,F1R4-AC2,F1R4-AC3,F1R4-AC4,F1R4-AC5,F1R4-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `firm-patterns.r4.result.md` beside it -- the round is in the name, so no earlier round's result is replaced (row S18). **Pin every artifact in the instance by the commit that carries it: commit the artifact first, then pin it; never PENDING-THIS-COMMIT** (rows S18, W1-S7, W2-S6). **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut -- --budget 540, 5 of 5 carriers (C1 23, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 naming LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (met by round 1's LN-h-3 @d292bca3ba), G-C (worker admission, checked at each spawn), G-D (round 1's .tf; no round-4 cell touches it) and G-V19 (decomposition v6 s.0e, the cross-project landing). This cell waits on G-V19's merge to CLOUD and on LGIC_ENFORCE EN-r-2.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 4's write set, not assumed: GRADING_RULE.md, lib/opal_naming.py and its test file, and records under deliverables/exercises/r4/; no cell adds an operation, a policy, a principal or a resource.
comp-adversary: RUN at the recut on the PRD at v1.8 (@2f554182b6) -- 7 of 7 cited commits verified; 15 cited paths, 15 stable, 0 flagged. Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood; 1624 of 1636 uncited siblings not digested (budget).
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~4, queue position 1, spawned from CLOUD after EN-r-2 and the G-V19 group have merged; not LN-g-2's worker (decomposition v6 s.0e: the hand grade is compared with grade(), which discriminates only if the hand is not the code's author). Measured at the cut: all 68 round-2 forms equal `grade()`'s output, and the first non-scope token of each of the 48 `{system}` forms is a function word, so EN-r-2's token rows are expected to fill none; the raises carry FWD-5. Round 4 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-3 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND3_20260915.md` @2f554182b6); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Decomposition v6, section 0e.
