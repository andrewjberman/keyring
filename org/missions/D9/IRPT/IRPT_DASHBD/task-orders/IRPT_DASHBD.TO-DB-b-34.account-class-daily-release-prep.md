# TO IRPT_DASHBD.TO-DB-b-34 -- E1: prepare the release of `account_class_daily` -- the reporting-gold Lambda also emits it, its role writes the one new prefix, and the never-widen packet is written; proven locally, applied later (FWD-3)

<to_id>IRPT_DASHBD.TO-DB-b-34</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~19</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Risk WORLD:** its `<paths>` name infrastructure (the gate's floor); the cell itself applies nothing. **Ordered by:** 1.0.0_SA_CTO~DELL2 round-21 analysis @214a0ef324 item E1 ("Release
`account_class_daily` with the unclassified-share line ... (1) a release packet with both never-widen halves ... (2) the after-read shows
the per-class sum equal to the account return within 1e-9 on one account-day, and the unclassified share printed; (3) the share's value is
printed with its denominator"; "The release waits on the terraform kit") | **Decomp cell:** `DB-b-34` (decomposition section 22) |
**outcome_ref:** FWD-3 | **depends_on:** DB-b-33 (merged @75717e8580).

This order PREPARES the release and proves it locally. It applies nothing: no `terraform apply`, no Lambda update, no S3 write. The
apply and the after-read (the CTO's criteria 2 and 3 on the served table) are the issuer's act once the dell2 terraform kit lands and both
halves are signed.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-19`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~19/`.

**The cell (`DB-b-34`).** `account_class_daily` is built and proven locally (`data/assets/scripts/gold/irpt_reporting/account_class_daily.py`,
its tests, `org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`; record
`deliverables/0.9.0_WK_IRPT_DASHBD~18/CLASS_DAILY_LOCAL_RUN.json`). The CTO ruled it released AS IS, with the unclassified share of value
shown beside the class breakdown (row W18-S2: about 16% of value, single stocks and money-market funds the module does not name).
**CORRECTION FIRST (1.0.0_SA_CTO~DELL2 msg 463, on 1.0.0_SA_CTO~DELL1 and 2.0.0_SA_COO~M1):** the classes must come from the
`etf-classifications` DynamoDB TABLE, not from `_shared/etf_classification.py`. The module is MDPF_SECCLASS's seed source and carries
ETFs and funds only by design; single stocks (equity) and money-market funds (cash) land in the TABLE (MDPF_SECCLASS cell SC-e-49, in
flight), never in the module, so a module reader stays about 16% unclassified forever.

The smallest release is to EXTEND the existing function, not to add one:
0. **Classes from the table** `data/assets/scripts/gold/irpt_reporting/account_class_daily.py`: read each holding's class from the
   `etf-classifications` table through `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (`ETFClassifier`, one
   `GetItem` per ticker, the client `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` already imports), never a
   Scan and never the module. A ticker the table does not hold is `unclassified`; a cash position is `cash`; a table `asset_class`
   outside the six is `unclassified` with the table's value kept in the record. Update the tests and the contract's class source and pin
   (the table, its key `ticker`, the read). Re-run the round-21 sample's 61 accounts and print the unclassified share against round
   21's module-based share, in `RELEASE_LOCAL_RUN.md`.
1. **Handler** `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`: after it emits a day of `account_return_daily`, it emits
   the same day of `account_class_daily` through `account_class_daily.py`'s own functions, in the scheduled path and in backfill mode.
   The `account_return_daily` output must not change by a byte (DELTA=0). A day the class producer cannot emit is logged by name and
   does not stop the returns table.
2. **Packaging** `infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf`: the bundle gains `account_class_daily.py` and
   `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (read how the current bundle pins `account_return_daily.py`,
   and pin the same way). It does NOT gain `_shared/etf_classification.py`.
3. **Role** `iam.tf` and `locals.tf`: add the class table's name ONCE in `locals.tf` (as `irpt_rg_gold_table_class`, mirroring the
   producer's constant, with the same "cited where it lives" comment), a class prefix local, and make `irpt_rg_gold_write_arns` the
   returns AND class prefixes, nothing else. Read access to the class prefix (the handler lists it for the newest landed day), and
   `dynamodb:GetItem` on `table/etf-classifications` only (no Scan, no index, no write; `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf`
   shows the same grant). No Delete, no other bucket. The schedule does not change.
4. **Declaration** `data/assets/scripts/gold/irpt_reporting/sources.json`: move the trade-leg tokens (`tr_cd` TR, `trade_typcd`
   BUY/SELL) from the producer's `TRADE_LEG_DECLARATION` block into the declaration, and have the producer read them there (row
   W18-S1). `account_return_daily.py` is not edited.
5. **Tests** in `infra/aws/lambda/investor-reporting/reporting-gold/tests/`: the handler emits both tables for a day; a class failure
   leaves the returns table written.
6. **The local release run.** Run the extended handler's `--local` mode for ONE trading day (2026-10-05) over 20 sample accounts (the
   round-21 sample's first 20), and the unextended handler (at base `git show 954983d543:<handler>`) over the same day and accounts.
   Write `RELEASE_LOCAL_RUN.json`: `returns_sha256_before` and `returns_sha256_after` (sha256 of the two returns parquet outputs),
   `account_days` and `class_rows` (as in the round-21 record), and `unclassified_share` `{value, denominator, basis: "market value on
   2026-10-05 over the sample's accounts"}`. Write a summary `RELEASE_LOCAL_RUN.md`, COUNTS ONLY.
7. **The never-widen packet** `NEVER_WIDEN_PACKET_ACCOUNT_CLASS_DAILY_RELEASE.md` in your folder, in the shape of
   `deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_REPORTING_PUBLISH_SCHEDULE_20261002.md`. Sections: **Blast radius** (the one
   new prefix written; the returns prefix rewritten byte-identically; what the act may not touch), **Rollback** per key (the prior Lambda
   version and role; the class prefix's objects deleted under the issuer's word), **Branch A / Branch B** of the expected outcome (the
   first fire writes the class table for T-1 with the identity holding; or it refuses a day by name and the returns table is still
   written), the **After-read** the apply will run (the CTO's criteria 2 and 3: one account-day's class sum against the account return
   within 1e-9, and the unclassified share with its denominator), and a **CTO half** and a **COO half**, unsigned, each naming what it
   signs. Cite every name and address as builder output (`lib/opal_naming.py name()` / `address()`), printed.

<criterion id="DB22-1-AC1" cell_refs="DB-b-34"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r22/p22_release_prep.py" . DB22-1-AC1</invocation><expect>DB22-1-AC1 PASS</expect></criterion>
`DB22-1-AC1` -- the returns table is byte-identical before and after the extension; the classes sum to the account within 1e-9 on every
measured account-day; the unclassified share is printed with its denominator; the reporting-gold tests pass. Base: FAIL.

<criterion id="DB22-1-AC2" cell_refs="DB-b-34"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r22/p22_release_prep.py" . DB22-1-AC2</invocation><expect>DB22-1-AC2 PASS</expect></criterion>
`DB22-1-AC2` -- the role writes the returns and class prefixes only, never dim_return_method, with no Delete. Base: FAIL.

<criterion id="DB22-1-AC3" cell_refs="DB-b-34"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r22/p22_release_prep.py" . DB22-1-AC3</invocation><expect>DB22-1-AC3 PASS</expect></criterion>
`DB22-1-AC3` -- the never-widen packet carries the blast radius, rollback, both branches, the after-read and both halves. Base: FAIL.

<expected_criteria>DB22-1-AC1,DB22-1-AC2,DB22-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. `account_return_daily.py` and `_shared/etf_classification.py` are read, never edited.
- **AWS:** S3 reads only (the producers' sources). NO `terraform init/plan/apply`, no `aws lambda`, no S3 write, no vendor call.
- **Refusal clause.** An apply, a deploy, an S3 write, a byte of change in the returns table, a write grant beyond the two prefixes, or a
  client figure in a committed `.md` is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf
infra/aws/terraform/investor-reporting/reporting-gold/iam.tf
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/gold/irpt_reporting/account_class_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_class_daily.py
org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~19/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-34.account-class-daily-release-prep.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 22 (round 22, workstream B), cell `DB-b-34`.
<owned_cells>DB-b-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB22-1-AC1, DB22-1-AC2, DB22-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~19/IRPT_DASHBD.TO-DB-b-34.account-class-daily-release-prep.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB22-1-AC1,DB22-1-AC2,DB22-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the two returns sha256 values, the unclassified share and its denominator, the
files changed, the builder output printed, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED -- the served reporting-gold function's handler, bundle and role change in source only; nothing is applied in this cell; the apply's blast radius is the packet's.
comp-iam: RUN -- `comp-iam service irpt-49f-reporting-gold-lambda` at 2026-10-07 ~12:0xZ returned 'No service matching' (196 Lambda services indexed; this role is built through the naming module, which the tool does not index), so the tool cannot see this role; the role's write and read set is graded by DB22-1-AC2 instead, and applied later under the halves.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the existing schedule is unchanged; the extended function rides it.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB22-1-AC1, AC2 and AC3 base FAIL (no record; locals.tf names the class table 0 times; no packet), dry-run at base 954983d543 2026-10-07 ~12:1xZ.
lane: the <paths> block IS the grant; rule 13 binds the apply (DS owns gold-script deploys; the issuer routes it).
</preflight>
