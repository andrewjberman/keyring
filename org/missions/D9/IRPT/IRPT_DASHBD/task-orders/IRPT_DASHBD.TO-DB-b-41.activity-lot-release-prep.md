# TO IRPT_DASHBD.TO-DB-b-41 -- E1: prepare the release of account_activity_daily, account_lot_realized and account_lot_unrealized_daily in the served reporting-gold function, with W20-S1, W20-S3 and W22-S3 folded in (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-41</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~23</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Risk WORLD:** its `<paths>` name infrastructure (the gate's floor; the
analysis classes the item SERVED); the cell itself applies nothing. **Ordered by:** 1.0.0_SA_CTO~DELL2 round-25 analysis @3543da2f4d
item E1 ("Release packet for the activity and lot tables (FWD-4), with the release-bound rows folded in: W20-S1 (typed source names into
`sources.json`), W20-S3 (composite keys in the contracts), W22-S3 (`basis_source` and its members ... in the lot contracts)"; criteria
"(1) the contracts under `org/standards/` name every served column and key, with a diff-check against the built tables' schemas reading
0 unnamed; (2) every new address and name is builder output, printed; (3) the packet names the root, a targeted plan, and both
branches; COO half signed") | **Decomp cell:** `DB-b-41` (decomposition section 26) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-40
(merged @5ffd7b740d).

This order PREPARES the release and proves it locally. It applies nothing. The COO half is the issuer's act at the drain; the plan, the
apply and the after-read are the issuer's once the dell2 terraform kit lands and both halves are signed.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-23`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/`.

**The cell (`DB-b-41`).** The three tables are built and graded locally by
`data/assets/scripts/gold/irpt_reporting/account_activity_lots.py` (its `SCHEMAS`, `TABLES`, `builder_output()`, `compute_local()`;
record `deliverables/0.9.0_WK_IRPT_DASHBD~22/WINDOWS_E1.json`: 58 of 91 account-windows tie within one cent, the other 33 within the 0.05
rounding tolerance). The served function is `irpt-49f-reporting-gold-lambda`: handler
`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, root `infra/aws/terraform/investor-reporting/reporting-gold/`. That
handler ALREADY carries an UNAPPLIED release of `account_class_daily` (round 22, packet
`deliverables/0.9.0_WK_IRPT_DASHBD~19/NEVER_WIDEN_PACKET_ACCOUNT_CLASS_DAILY_RELEASE.md`); the next apply of the root ships both. Read
that packet first: this release follows its shape and extends it.

1. **Contracts** (`org/standards/IRPT_DASHBD_ACCOUNT_ACTIVITY_DAILY_CONTRACT.json`, `..._ACCOUNT_LOT_REALIZED_...`,
   `..._ACCOUNT_LOT_UNREALIZED_DAILY_...`): name every column the producer's `SCHEMAS` carry (the activity contract lacks
   `income_gross`, `income_fee_admin`, `income_withheld_tax` and `inkind_departure_gain` today), each with type, nullability and meaning.
   Add `primary_key` (a list of column names: the composite key each table is unique on, row W20-S3) and prove uniqueness on your local
   run's rows. In both lot contracts add `enums.basis_source` with every member the producer writes, `WASH_SALE_EXCLUDED_BASIS` and
   `IN_KIND_TRANSFER_VALUE` included (row W22-S3). Recompute `schema_hash` by the contract's stated `schema_hash_basis`, and bump
   `contract_version`. State the 0.05 per-account-window rounding tolerance in the activity contract where a reader meets it.
2. **Declaration** (row W20-S1): move the producer's `LOT_SOURCE` block (custodian table and column names) into
   `data/assets/scripts/gold/irpt_reporting/sources.json`, and have the producer read it there; also any other custodian table name the
   producer types (`fact_trn` included). After this, the producer names no custodian table as a literal. The served
   `account_return_daily.py` is not edited, and its output must not change.
3. **Handler** `handler.py`: after it emits a day of `account_return_daily` and `account_class_daily`, it emits the same day of the
   three tables through `account_activity_lots.py`'s own functions, in the scheduled path and in backfill mode. A day this producer
   cannot emit is logged by name and does not stop the returns or class tables. The returns output must not change by a byte (DELTA=0).
4. **Packaging and role** (`lambda.tf`, `iam.tf`, `locals.tf`): the bundle gains `account_activity_lots.py` (pinned as the current
   bundle pins its producers). Name the three tables ONCE each in `locals.tf`, mirroring the producer's constants with the same "cited
   where it lives" comment; the write ARNs become the returns, class and these three prefixes, nothing else; read on the three prefixes
   for the newest-landed-day listing. No Delete, no other bucket. The schedule does not change. Name every file the build must carry in
   the packet, with its sha256 at your HEAD; the issuer writes `infra/aws/lambda/ci/lambda-source-map.json` at the apply.
5. **Tests** in `infra/aws/lambda/investor-reporting/reporting-gold/tests/` (the handler emits all five tables for a day; a failure of
   this producer leaves returns and class written) and in `data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py`
   (the producer reads its source names from the declaration).
6. **Local release run.** The extended handler's `--local` mode for ONE trading day (2026-10-05) over the round-24 sample's first 20
   accounts, and the round-25 handler (`git show 5ffd7b740d:<handler>`) over the same day and accounts. Write `RELEASE_LOCAL_RUN.json`:
   `returns_sha256_before` / `_after`, `class_sha256_before` / `_after`, rows per table, the primary-key uniqueness per table, and the
   run's wall time and peak memory. Write `RELEASE_LOCAL_RUN.md`, COUNTS ONLY.
7. **The never-widen packet** `NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE.md` in your folder, in the round-22 packet's shape, and covering
   the WHOLE next apply of the root (the class release it carries, and these three tables). Sections: **Root**
   (`infra/aws/terraform/investor-reporting/reporting-gold`); **Plan**, a TARGETED plan command (`terraform plan` with one `-target=`
   per resource the apply may change; it must not name any resource outside this root) and the expected counts written as
   `N to add, N to change, N to destroy`; **Blast radius** (the new prefixes written, the returns prefix rewritten byte-identically,
   what the act may not touch); **Rollback** per key; **## BRANCH A** and **## BRANCH B** of the first fire (the tables written for T-1
   with the identity graded; or a day refused by name with returns and class still written); the **After-read** the apply will run; the
   build's file list with sha256s; and a **CTO half** and a **COO half**, unsigned, each naming what it signs, with a line that the
   round-22 class pair is superseded by this packet once both halves here are signed. Print every new address and name as builder output
   (`lib/opal_naming.py address()` / `name()`, through the producer's `builder_output()`), verbatim.

<criterion id="DB26-1-AC1" cell_refs="DB-b-41"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_release.py" . DB26-1-AC1</invocation><expect>DB26-1-AC1 PASS</expect></criterion>
`DB26-1-AC1` -- the three contracts name every built column (0 unnamed either way), each with a primary key; both lot contracts carry
`basis_source` with WASH_SALE_EXCLUDED_BASIS. Base: FAIL (the activity contract lacks 4 columns).

<criterion id="DB26-1-AC2" cell_refs="DB-b-41"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_release.py" . DB26-1-AC2</invocation><expect>DB26-1-AC2 PASS</expect></criterion>
`DB26-1-AC2` -- the packet prints every new address as builder output; the producer types no custodian table name; sources.json
carries them. Base: FAIL.

<criterion id="DB26-1-AC3" cell_refs="DB-b-41"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_release.py" . DB26-1-AC3</invocation><expect>DB26-1-AC3 PASS</expect></criterion>
`DB26-1-AC3` -- the packet names the root, a targeted plan with its expected counts, both branches, the rollback and the class release it
carries. Base: FAIL.

<expected_criteria>DB26-1-AC1,DB26-1-AC2,DB26-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. `account_return_daily.py` is read, never edited.
- **AWS:** S3 reads only (the producers' sources). NO `terraform init/plan/apply`, no `aws lambda`, no S3 write, no vendor call, no bun,
  no download of any package, script or program.
- **Refusal clause.** An apply, a deploy, an S3 write, a byte of change in the returns or class tables, a write grant beyond the five
  prefixes, a hand-typed address or name, or a client figure in a committed `.md` is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf
infra/aws/terraform/investor-reporting/reporting-gold/iam.tf
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/standards/IRPT_DASHBD_ACCOUNT_ACTIVITY_DAILY_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_LOT_UNREALIZED_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-41.activity-lot-release-prep.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 26 (round 26, workstream B), cell `DB-b-41`.
<owned_cells>DB-b-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB26-1-AC1, DB26-1-AC2, DB26-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/IRPT_DASHBD.TO-DB-b-41.activity-lot-release-prep.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB26-1-AC1,DB26-1-AC2,DB26-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what you changed per file, the before/after hashes, the run's time and memory,
the plan counts you expect and why, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED -- the served reporting-gold function's handler, bundle and role change in source only; nothing is applied in this cell; the apply's blast radius is the packet's, and the next apply of this root also carries the unapplied round-22 class release.
comp-iam: RUN -- the role is built through the naming module, which comp-iam does not index (round 22: `comp-iam service irpt-49f-reporting-gold-lambda` returned 'No service matching' over 196 indexed services); the write and read set is graded in the packet and applied later under both halves.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the existing schedule is unchanged; the extended function rides it.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB26-1-AC1 base FAIL (the activity contract lacks income_fee_admin, income_gross, income_withheld_tax, inkind_departure_gain); AC2 and AC3 base FAIL (no packet); dry-run at base c246d6a180 2026-10-07 ~20:5xZ.
lane: the <paths> block IS the grant; rule 13 binds the apply (DS owns gold-script deploys; the issuer routes it). Cross-box notice (MSTR msg 1060/1062): the opal-assets root is untouched; this root is investor-reporting/reporting-gold.
</preflight>
