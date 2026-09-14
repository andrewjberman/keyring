# TO LGIC_ENFORCE.TO-EN-c-1 -- the carrier census

<to_id>LGIC_ENFORCE.TO-EN-c-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-c-1` | **outcome_ref:** FWD-3 | **depends_on:** -- (level 0; chain head) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`EN-c-1` -- the carrier census (PRD candidate E1, its first half). **The population of hand-kept firm carriers, re-derived by an UNSCOPED read** (DEC-5: *"Cell E1 first re-derives the whole carrier population by an unscoped read"*).

Read the repo for every firm long form (`49financial`, `inflection`, `cottonwood`, `demo`), short form (`49f`, `inf`, `cot`), refused or legacy token (`bd`) and legacy bucket name (`opal-data-bd`, `opal-data-inf`, `opal-data-cot`, `opal-data-49financial`) as a WHOLE segment (split on `-`, `_`, `/`, `.`, quotes), with `comp-find` (the estate's instrument; print its denominator line). Classify every hit as a CARRIER, meaning a hand-kept copy of a registry row (a map, list, constant or config value the firm's name keys or fills), or EXCLUDED with a reason (prose, a comment, a test fixture, a generated file, a log).

The eight DEC-5 definitions, re-measured at L5 by definition-pattern, must appear among your carriers:
- `data/firm_registry.json`
- `infra/aws/lambda-edge/_shared/firm-config.mjs:65` `FIRM_CONFIG`
- `firm_bucket_map()` at `data/assets/scripts/gold/investor_reporting/directory_runner.py:170`
- `firm_bucket_map()` at `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:145`
- `infra/aws/lambda/investor-reporting/_authz/loaders.py:43` `bucket_for`
- `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py:57` `resolve_firm`
- `.tools/ds-precommit-check.py:68` `_CROSS_FIRM_FOREIGN_BUCKETS`
- `.tools/ds-precommit-check.py:110` `_CROSS_FIRM_FOREIGN_KEY_PREFIXES`

A carrier OUTSIDE those eight is listed AND filed as one surprise row. The generated views of this round cover only the eight, so an extra one is a finding, never a silent extension.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md`:** prose, then ONE fenced ```json block:
```
{"instrument": "<the comp-find command and its denominator line>", "vintage": "<HEAD you read>",
 "denominator": {"files_scanned": <n>, "hits": <n>},
 "carriers": [{"path": "...", "line": <n>, "token": "<the literal string>", "kind": "<map|list|constant|config|function>"}],
 "excluded": [{"path": "...", "line": <n>, "reason": "..."}],
 "outside_dec5_rows": {"<path>:<line>": "<the surprise row id>"}}
```
`hits` equals the carriers plus the excluded.

**Read:** comp-find over the repo; the files it finds; the channel (to mint a row id).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C1-AC1" cell_refs="EN-c-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py c1-denominator</invocation><expect>VERDICT: PASS-DENOMINATOR</expect></criterion>
`C1-AC1` -- the census names its instrument and prints a non-zero denominator.

<criterion id="C1-AC2" cell_refs="EN-c-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py c1-dec5</invocation><expect>VERDICT: PASS-DEC5-PRESENT</expect></criterion>
`C1-AC2` -- all eight DEC-5 definitions are among the carriers.

<criterion id="C1-AC3" cell_refs="EN-c-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py c1-partition</invocation><expect>VERDICT: PASS-PARTITIONED</expect></criterion>
`C1-AC3` -- every hit is a carrier or excluded with a reason, and the two add up to the hits.

<criterion id="C1-AC4" cell_refs="EN-c-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py c1-extra-filed</invocation><expect>VERDICT: PASS-EXTRA-FILED</expect></criterion>
`C1-AC4` -- every carrier outside the eight is filed as a row that exists in the channel.

<criterion id="C1-J1" cell_refs="EN-c-1" judgment="true"/>
`C1-J1` -- graded at L9 by 3.0.0_SA_CVO: every exclusion's reason holds. RECORD; NO VERDICT.

<expected_criteria>C1-AC1, C1-AC2, C1-AC3, C1-AC4, C1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform apply. Any live read is read-only through the `aws` shim.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-c-1`.
<owned_cells>EN-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C1-AC1`, `C1-AC2`, `C1-AC3`, `C1-AC4`, `C1-J1`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-c-1.carrier-census.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C1-AC1,C1-AC2,C1-AC3,C1-AC4,C1-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `carrier-census.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This project registered G-B (first half DISCHARGED @ce7349b7cc; EN-s-2 waits on the second), G-C (worker admission, checked after this issuance), G-E (the never-widen sign-off before EN-f-2), G-F (the live REFUSE flip, outside this round), G-S (the ADVI_FIRMBKTS manual gate) and G-W (write logging; EN-c-2 takes writers from grants). None is owed by this cell.
comp-iam: RUN at L5 -- stats 209 roles, 189 services, 1,091 operations, 310 gaps; APPLICABLE (EN-f-2 applies a bucket policy and three roles; EN-c-2 is a grant census); blind to bucket policies, so the fence is proved by real probes (DEC-4). This cell adds no operation, policy, principal or resource.
comp-adversary: RUN at L5 on the PRD at v1.1 -- 15 of 15 cited commits verified; 19 cited paths, 12 stable, 3 MOVED (s3-49financial.tf, SEQUENCE.yaml, NAMING_SCHEMA.json now v1.4), 4 GONE (this project mints them). Blindness stated: T11, its complement is filesystem adjacency.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 1. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
