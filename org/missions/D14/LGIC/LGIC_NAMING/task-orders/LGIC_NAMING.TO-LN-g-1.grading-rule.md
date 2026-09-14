# TO LGIC_NAMING.TO-LN-g-1 -- the written grading rule, its worked cases, and the legacy served list

<to_id>LGIC_NAMING.TO-LN-g-1</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.4 @e04b802fe9 (ADMITTED @254ac1f2ab) | **Decomp cell:** `LN-g-1` | **outcome_ref:** FWD-5 | **depends_on:** -- (chain head, chain A) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`LN-g-1` -- the written grading rule (PRD candidate N2), and since PRD v1.4 the legacy served list.

**What you build.** A rule a person can apply BY HAND, with no machine: `grade(name, type) -> (verdict, canonical_form)`. Three verdicts, `CONFORMANT`, `ALIAS` and `OUT-OF-PATTERN`, and no fourth. A name the rule cannot place, or a token no registry row resolves, `RAISE`s as a defect in the rule or the registry. A type the data file marks NOT GRADED returns `NOT-GRADED`: it is outside the grade's domain, not a fourth verdict.

**Your inputs, all at HEAD in your worktree:** `org/standards/NAMING_SCHEMA.json` v1.4 (the closed lists: the key grammar and its forms, buckets, the resource grammar, kinds by node type, cadences, secrets, log groups, policies, firm long and short forms, refused tokens, the grade's signature); `infra/logic/05_IDENTITY_SPINE.md` (the registry seed: firms, products, vendors, masters, and their aliases); `infra/logic/09_NAMING_CENSUS.md` (the residue classes); and S1-S13 of `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md` v1.4.

**Deliverable 1: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`.** The rule in prose -- how a name is tokenised, then slot by slot: the per-slot form (S4), a shared resource's missing scope (S5), the system slot (S6), kinds (S7), cadences (S8), secrets, log groups and policies (S9), refused tokens (S10), keys and buckets (S1, S2, including the v1.3 entity partition, code tier and legacy served path, and v1.4's membership rule). It cites `LEGACY_SERVED_PATHS.json` for membership and carries NO second copy of that list. Then ONE fenced ```json block:

```
{"vintage": "<LIVE_NAMES.json vintage>", "worked_cases": [ {"name": ..., "type": <node_type>, "verdict": ..., "canonical_form": ..., "why": <the rule lines applied>, ...} ]}
```

Each worked case carries `name`, `type`, `verdict` and `why`; `canonical_form` is required for ALIAS and OUT-OF-PATTERN. Tag a case where it applies: `residue_class` (one of `camel-iam`, `purpose-first-policy`, `library-first-layer`, `default-sg`, `workstream-schedule`); `form` (one of `entity-partition`, `legacy-served`, `code-tier`, `legacy-root-code`); `pair` (`on-list` or `off-list`); and `specimen: true` ONLY for a form or pair path that has no live name.

**Coverage of the worked cases.**
- at least one for EACH of the 25 graded node types: the 18 of `kind.by_type` plus EVENT_RULE, SCHEDULE, LOG_GROUP, S3_BUCKET, S3_BUCKET_POLICY, S3Key and SECRET;
- at least one per verdict (CONFORMANT, ALIAS, OUT-OF-PATTERN), per residue class (5), and per key form (4);
- the legacy root `code/` case is graded as RULED at v1.4: OUT-OF-PATTERN, with the code-tier key as its canonical form;
- a DISCRIMINATING PAIR: two same-shaped platinum paths, one ON the list graded CONFORMANT, one OFF it graded OUT-OF-PATTERN -- so the list is proved to CHANGE a verdict, not merely to exist;
- every non-specimen case is a name in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json` under its type -- never from a later pull;
- NO worked case may be one of the 85 discriminating names in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N6_SAMPLE.json` (the graders are tested on those). Its 3 OVERLAP names -- the single live ECS_CLUSTER, LOAD_BALANCER and STATE_MACHINE -- are allowed.

**Deliverable 2: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`** (PRD v1.4, S10 ruled). The CLOSED list of every served path below `{source}/{scope}/platinum/` that the frozen portal requests:

```
{"portal_vintage": "<the portal commit you read>", "source": "<the files you read>", "paths": ["<key template>", ...], "denominator": <len(paths)>}
```

Each entry is a key template below the bucket, with `{placeholders}` for variable segments (for example `advi/{scope}/platinum/advisors/{id}/summary.json`). **Read the portal at the commit the workspace pins:** `git ls-tree HEAD portal` in your worktree prints it (`e85f6eb84f` at issuance). Read it READ-ONLY with `git -C /c/Users/AndrewBerman/Desktop/ajb_workspace/portal show <sha>:<path>`. The portal is frozen and is not yours to change. `src/api/endpoints/adviKeyRepoint.ts` is the known request site (the CTO's ruling cites line 37); census the rest with `git -C /c/Users/AndrewBerman/Desktop/ajb_workspace/portal grep -n platinum <sha> -- src` and print the denominator.

**Read:** NAMING_SCHEMA.json, 05_IDENTITY_SPINE.md, 09_NAMING_CENSUS.md, the PRD, LIVE_NAMES.json, N6_SAMPLE.json, the portal at its pinned commit (read-only).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G1-AC1" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-wellformed</invocation><expect>VERDICT: PASS-WELL-FORMED</expect></criterion>
`G1-AC1` -- every worked case carries a name, a type and one of the five verdict values, and a canonical form where the verdict is ALIAS or OUT-OF-PATTERN.

<criterion id="G1-AC2" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-types</invocation><expect>VERDICT: PASS-ALL-25-TYPES</expect></criterion>
`G1-AC2` -- a worked case for each of the 25 graded node types, counted from the data file itself.

<criterion id="G1-AC3" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-verdicts</invocation><expect>VERDICT: PASS-ALL-3-VERDICTS</expect></criterion>
`G1-AC3` -- each of CONFORMANT, ALIAS and OUT-OF-PATTERN appears.

<criterion id="G1-AC4" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-residue</invocation><expect>VERDICT: PASS-ALL-5-RESIDUE</expect></criterion>
`G1-AC4` -- each of the five census residue classes has a worked case.

<criterion id="G1-AC5" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-live</invocation><expect>VERDICT: PASS-ALL-LIVE</expect></criterion>
`G1-AC5` -- every non-specimen worked case is a live name under its type in LIVE_NAMES.json.

<criterion id="G1-AC6" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-disjoint</invocation><expect>VERDICT: PASS-DISJOINT</expect></criterion>
`G1-AC6` -- no worked case is a discriminating sample name.

<criterion id="G1-AC7" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-forms</invocation><expect>VERDICT: PASS-ALL-4-FORMS</expect></criterion>
`G1-AC7` -- each of the four v1.3 key forms has a worked case.

<criterion id="G1-AC8" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-legacyroot</invocation><expect>VERDICT: PASS-RULED-VERDICT</expect></criterion>
`G1-AC8` -- the legacy root code/ case is OUT-OF-PATTERN with a code-tier canonical form, as ruled.

<criterion id="G1-AC9" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-list</invocation><expect>VERDICT: PASS-LISTED</expect></criterion>
`G1-AC9` -- LEGACY_SERVED_PATHS.json exists with its portal vintage, and its denominator equals its length.

<criterion id="G1-AC10" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-pair</invocation><expect>VERDICT: PASS-DISCRIMINATES</expect></criterion>
`G1-AC10` -- the on-list case is CONFORMANT and matches a list entry; the off-list case is OUT-OF-PATTERN and matches none.

<criterion id="G1-AC11" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py g1-cites</invocation><expect>VERDICT: PASS-CITES-NO-COPY</expect></criterion>
`G1-AC11` -- the rule cites LEGACY_SERVED_PATHS.json and repeats at most three of its entries.

<criterion id="G1-J1" cell_refs="LN-g-1" judgment="true"/>
`G1-J1` -- graded at L9 by 3.0.0_SA_CVO: the rule is exact enough for a person who did not write it to apply by hand -- LN-h-1 and LN-h-2 are that test. RECORD; NO VERDICT.

<expected_criteria>G1-AC1, G1-AC2, G1-AC3, G1-AC4, G1-AC5, G1-AC6, G1-AC7, G1-AC8, G1-AC9, G1-AC10, G1-AC11, G1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). Reading the live plane is done for you: the fixed inputs below are one pull, at one vintage, and you read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_ln.py` (the checker every criterion calls), `LIVE_NAMES.json` (every live AWS name by node type, vintage 2026-09-14 12:13:53 UTC, 2,531 nodes, 33 types), `N6_SAMPLE.json`, `N3_ITEMS.json`, `N3_KEY.json`, `N5_ADDRESSES.json`, `N5_KEY.json`. Read only those this order names. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md
org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v3 @62b5c0819f, cell `LN-g-1`.
<owned_cells>LN-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G1-AC1`, `G1-AC2`, `G1-AC3`, `G1-AC4`, `G1-AC5`, `G1-AC6`, `G1-AC7`, `G1-AC8`, `G1-AC9`, `G1-AC10`, `G1-AC11`, `G1-J1`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-g-1.grading-rule.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G1-AC1,G1-AC2,G1-AC3,G1-AC4,G1-AC5,G1-AC6,G1-AC7,G1-AC8,G1-AC9,G1-AC10,G1-AC11,G1-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `grading-rule.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 1. Round 1 of LGIC_NAMING; issued by `2.0.0_SA_COO~G` on Andrew-direct ~13:4xZ ruling 1 (relayed 96594, record @0d3ad7d496). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: one live pull at vintage 2026-09-14 12:13:53 UTC (manifest b578e47d733f). The N6 sample is 85 + 3 by the decomposition's rule over distinct names (row LGIC_NAMING-S11).
