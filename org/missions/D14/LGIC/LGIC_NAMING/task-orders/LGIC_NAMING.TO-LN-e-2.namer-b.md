# TO LGIC_NAMING.TO-LN-e-2 -- namer B

<to_id>LGIC_NAMING.TO-LN-e-2</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.4 @e04b802fe9 (ADMITTED @254ac1f2ab) | **Decomp cell:** `LN-e-2` | **outcome_ref:** FWD-1 | **depends_on:** -- (chain head, chain B; spawned from the same base as LN-e-1) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`LN-e-2` -- namer B (PRD candidate N3). **Two namers name the same NEW resources without conferring; the outcome is that they write the identical string for every one.**

**Your briefing is ONLY** `org/standards/NAMING_SCHEMA.json` (v1.4) and `infra/logic/05_IDENTITY_SPINE.md` (the registry seed), plus the item list below. Do NOT read the PRD, the decomposition, `N3_KEY.json`, any file under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/` except your own, the other namer's task order, or any grading rule. If a name cannot be derived from those two files, the answer for that item is `RAISE` and a surprise row -- never a guess.

**Name every item in `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_ITEMS.json`** (18 items; the same list is below). For a resource, the full name. For an S3 key, the key without the bucket, up to and including the partition, as the item says. For a bucket, the bucket name.

**Write `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-b.tsv`:** the first line `# base <sha>` (the output of `git rev-parse HEAD` in your worktree BEFORE your first commit); then one line per item: `<item id><TAB><name>`.

**The items** (verbatim from `N3_ITEMS.json`):

- `i01` (`LAMBDA`): The Lambda function that publishes Cottonwood's figures from the model-portfolio product (the model delivery product) every day. This is the example the outcome itself names.
- `i02` (`IAM_ROLE`): The IAM role that the Black Diamond integration assumes when it fetches 49 Financial's daily session data from Black Diamond.
- `i03` (`EVENT_RULE`): The EventBridge rule that starts the Orion ingest for Inflection once a day.
- `i04` (`SECRET`): The Secrets Manager secret holding Schwab's API credentials used for 49 Financial.
- `i05` (`S3_BUCKET`): The S3 bucket that holds Cottonwood's own data.
- `i06` (`S3Key`): The S3 key, without the bucket, of Eclipse's silver table for Inflection named account_holdings, for the day 2026-09-14. Give the key only, up to and including the partition.
- `i07` (`IAM_POLICY`): The IAM policy that lets the model-portfolio product's single shared publisher read every firm's gold data. The publisher serves all firms.
- `i08` (`SQS_QUEUE`): The dead-letter queue behind the ETF product's price-refresh queue, which is shared by every firm.
- `i09` (`CW_ALARM`): The CloudWatch alarm that fires when the daily model-portfolio publish for the demo firm fails.
- `i10` (`SCHEDULE`): The EventBridge Scheduler schedule that runs the SmartX platform export for 49 Financial once a week.
- `i11` (`ECS_TASK_DEFINITION`): The ECS task definition that runs the Pathfinder ingest for the ETF product.
- `i12` (`SSM_DOCUMENT`): The SSM document that downloads Black Diamond files for Cottonwood.
- `i13` (`S3Key`): The S3 key, without the bucket and without the file, of a NEW served family for the model-portfolio product for 49 Financial: one file per advisor, the table is advisor_books, the entity is the advisor keyed advisor_id, and the advisor id is A123. The file under it would be book.json; give the key up to and including the partition.
- `i14` (`S3Key`): The S3 key, without the bucket, of the model-portfolio product's code bundle that builds its gold tier, shared across all firms. The bundle file is named mdpf-accrual-bridge.tar.gz.
- `i15` (`INSTANCE_PROFILE`): The EC2 instance profile for the Orion runner host that builds Inflection's gold data.
- `i16` (`SECURITY_GROUP`): The security group for the model-portfolio product's exporter host that serves Cottonwood.
- `i17` (`SNS_TOPIC`): The SNS topic for the ETF product's pipeline alerts, which is shared by every firm.
- `i18` (`DYNAMODB_TABLE`): The DynamoDB table holding the model-portfolio product's delivery status for Inflection.

**Read:** NAMING_SCHEMA.json, 05_IDENTITY_SPINE.md, N3_ITEMS.json.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E2-AC1" cell_refs="LN-e-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e2-named</invocation><expect>VERDICT: PASS-ALL-NAMED</expect></criterion>
`E2-AC1` -- every one of the 18 items has a name in n3-namer-b.tsv.

<criterion id="E2-AC2" cell_refs="LN-e-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e2-base</invocation><expect>VERDICT: PASS-BASE-RECORDED</expect></criterion>
`E2-AC2` -- the file records the worktree base commit it was named from.

<expected_criteria>E2-AC1, E2-AC2</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). Reading the live plane is done for you: the fixed inputs below are one pull, at one vintage, and you read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_ln.py` (the checker every criterion calls), `LIVE_NAMES.json` (every live AWS name by node type, vintage 2026-09-14 12:13:53 UTC, 2,531 nodes, 33 types), `N6_SAMPLE.json`, `N3_ITEMS.json`, `N3_KEY.json`, `N5_ADDRESSES.json`, `N5_KEY.json`. Read only those this order names. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-b.tsv
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v3 @62b5c0819f, cell `LN-e-2`.
<owned_cells>LN-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E2-AC1`, `E2-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~3/LGIC_NAMING.TO-LN-e-2.namer-b.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E2-AC1,E2-AC2` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `namer-b.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~3, queue position 1. Round 1 of LGIC_NAMING; issued by `2.0.0_SA_COO~G` on Andrew-direct ~13:4xZ ruling 1 (relayed 96594, record @0d3ad7d496). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: one live pull at vintage 2026-09-14 12:13:53 UTC (manifest b578e47d733f). The N6 sample is 85 + 3 by the decomposition's rule over distinct names (row LGIC_NAMING-S11).
