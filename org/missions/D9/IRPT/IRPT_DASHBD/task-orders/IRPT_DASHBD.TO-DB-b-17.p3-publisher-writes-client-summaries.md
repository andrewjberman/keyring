# TO IRPT_DASHBD.TO-DB-b-17 -- P-3: the publisher WRITES every directory client's summary.json at the builder's address, from all of the client's published accounts (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-17</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~4</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer, inside its decomposition, on CTO RULINGS batch 197
(@7563d60e68). DB-b-12 built `build_client_summary`, but no served code calls it. Nothing writes `summary.json`, so P-3 cannot be
served until the publisher writes it. Cut beside DB-b-16 in ROUND 9 (GATE (x), IRPT_BCKEND row S267). | **Decomp cell:**
`DB-b-17` (decomposition section 9) | **outcome_ref:** P-3, P-1 | **depends_on:** DB-b-12 (merged @eaf04fe0d1), DB-b-14 (merged
@f26fa5fb4d)

---

## WORKER FACE

**What exists.**
- `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py:323` `build_client_summary(client, accounts, built_at)`
  builds ONE client's summary. `client` is `{"client_id", "account_ids"}`; `accounts` maps an account id to
  `{"series", "manifest"}`. Its address helper (`:320`) gives
  `naming.address("irpt", firm, "platinum", "reporting", "client=<cli_id>", "summary.json")`.
- The publisher handler (`handler.py`) publishes per-account `series.json.gz` and `manifest.json`.
  - Above `SHARD_ACCOUNTS` it fans out to 8 shards by `shard_of(account)` (a crc32 of the ACCOUNT).
  - A client's accounts can therefore land in different shards, so no single shard holds a whole client.
- DB-b-12's local dry run read the directory and built 6 summaries:
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/client_summary_dryrun_r5.py` and `CLIENT_SUMMARY_R5.json`.
  - The directory: 4,620 clients, 7,576 account ids, through the `latest.json` pointer the directory handler loads.
  - Row W1-S15 records how opaque `cli_`/`acc_` ids map to custodian-keyed series (mint through `_ids`, as `reporting/entry.py` does).

**What you build.**
1. **A summaries pass.** Every directory client with at least one published account gets its `summary.json` written at the builder
   address, built by `build_client_summary` from ALL of that client's published accounts. Accounts not yet published are listed in
   `unpublished_account_ids`.
   - Suggested shape: an explicit event mode, `{"summaries": true}`, with `dry_run` honoured. It reads the directory and each
     covered account's published series and manifest, and builds and writes one client at a time.
   - It must fit the 900 s Lambda limit at 4,620 clients and 7,570 accounts. Measure the per-account read cost on what is
     published today (reads only) and state the projection with its basis. If it does not fit, shard it BY CLIENT (a stable
     hash), reusing the existing fan-out and its own-function invoke grant.
   - A client with no published account gets no summary and is counted.
   - When the pass runs (a schedule after the shards, or a packet invoke) is the issuer's P-2 packet, not this cell.
2. **The scheduled publish fire is unchanged.** Without the new event key it does exactly what it did at @f26fa5fb4d.
3. **IAM, only if needed.** If the publish role cannot read the directory objects, grant `s3:GetObject` on exactly those objects
   in `infra/aws/terraform/investor-reporting/reporting-publish/iam.tf`, never `*`. Text only; nothing is applied.
4. **Tests.** Write `reporting-publish/tests/test_publisher_summaries.py`, with stubbed S3 and directory, at least 4 tests:
   - a client with two published accounts gets one summary naming both;
   - a client with one published and one unpublished account lists the unpublished one;
   - a client with no published account gets no summary and is counted;
   - the write lands at the builder's `address`;
   - `dry_run` writes nothing;
   - a fire without the new key behaves as before.
   - The file names `summary`, `directory`, `unpublished` and `address`.

<criterion id="DB9-2-AC1" cell_refs="DB-b-17"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r9/p9_2_ac1_publisher_writes_summaries_tests.py" .</invocation><expect>DB9-2-AC1 PASS</expect></criterion>
`DB9-2-AC1` -- the summaries pass tests pass (at least 4). Base: FAIL (no file).

<criterion id="DB9-2-AC2" cell_refs="DB-b-17"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB9-2-AC2</invocation><expect>DB9-2-AC2 PASS</expect></criterion>
`DB9-2-AC2` -- reporting-gold and reporting-publish suites pass with nothing removed (floors 24 and 25). Base: PASS (a regression
guard).

<expected_criteria>DB9-2-AC1,DB9-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. DB-b-16 (another worker) owns the read route, `reporting/entry.py`, and the new standards
  contract. DB-b-15 owns the reporting gold producer. Do not touch either.
- **AWS:** S3 READS only, to measure the per-account read cost. No write, no upload, no plan, no apply, no invoke.
- **Refusal clause.** A change to the scheduled publish fire's behaviour, or an existing test that moves, is a defect: stop and
  file a row. No client name in any record; ids only.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_summaries.py
infra/aws/terraform/investor-reporting/reporting-publish/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~4/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/investor-reporting/`, `lib/`,
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 9 (round 9, workstream B), cell `DB-b-17`.
<owned_cells>DB-b-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB9-2-AC1, DB9-2-AC2. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~4/IRPT_DASHBD.TO-DB-b-17.p3-publisher-writes-client-summaries.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB9-2-AC1,DB9-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the summaries event shape and its refusals;
- the measured per-account read cost and the 900 s projection with its basis;
- whether it shards by client;
- any IAM statement added;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served publisher irpt-49f-reporting-publish-lambda's source and possibly its role's policy text; 0 served bytes move in the cell. The deploy, the first summaries pass and its schedule are the issuer's P-2 packet with both halves.
comp-iam: RUN -- only if the role cannot read the directory objects: s3:GetObject on exactly those objects, applied only under the packet.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed (the summary route is DB-b-16's).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 08:15 ET publish schedule is not moved; the summaries pass is an explicit event in this cell, and its trigger is the packet's.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB9-2-AC1 base FAIL (no file), DB9-2-AC2 base PASS (regression guard, floors 24 and 25), dry-run at the base 2026-10-03 ~01:2xZ.
lane: the <paths> block IS the grant.
</preflight>
