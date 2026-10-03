# TO IRPT_DASHBD.TO-DB-b-16 -- P-3: the per-client summary's own versioned contract, and the read route serving it only on full account coverage (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-16</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~3</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 197 (@7563d60e68, msg 104491), answering this seat's
round-5 ask on P-3. GATE (x) refuses a new file into round 8, so this is ROUND 9 (IRPT_BCKEND row S267). | **Decomp cell:**
`DB-b-16` (decomposition section 9) | **outcome_ref:** P-3, FWD-1 | **depends_on:** DB-b-12 (merged @eaf04fe0d1)

---

## WORKER FACE

**The ruling.**
- (a) The per-client summary gets a NEW versioned contract, `org/standards/IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json` 0.1.0. It
  sits beside its three siblings in `org/standards/` (`IRPT_DASHBD_SERIES_CONTRACT.json` is the closest model). A per-client
  summary is a different GRAIN from a per-account manifest, and rule 24 (ii) keeps one grain per schema.
- (b) The read route serves `summary.json` ONLY when the scope enforcer covers EVERY account the summary names, using the same
  per-account coverage check a manifest read uses, applied to each account.
  - A client id in a request is a claim, never a grant.
  - Partial coverage is refused with `OBJECT_NOT_COVERED`, and the page falls back to per-account manifests.
  - A client of another firm is refused.

**What exists.** `publisher.build_client_summary` (`infra/aws/lambda/investor-reporting/reporting-publish/publisher.py:323`, cell
DB-b-12) builds the document. Its address is builder output:
`naming.address("irpt", firm, "platinum", "reporting", "client=<cli_id>", "summary.json")`.
- Top-level keys: client_id, firm, as_of, windows, accounts, unpublished_account_ids, built_at, publisher_version.
- Per account: account_id, as_of, first_data_date, series_object, windows, window_status.
- `window_status` values in use include MEASURED and NOT_SPANNED. Read the builder for the full set.

The read route is `infra/aws/lambda/investor-reporting/reporting/entry.py`, which has one route today:
`GET /api/scoped/investor-reporting/reporting/{account_id}/{which}`, declared in
`infra/aws/terraform/investor-reporting/reporting-read/locals.tf:72`.

**What you build.**
1. **The contract.** Write `org/standards/IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json`:
   - `contract_version` "0.1.0";
   - a `summary` section with `required` (a list) and `fields` (each key with its one-sentence meaning), declaring EVERY
     top-level key the builder emits;
   - the per-account entry's keys, and the address as builder output.
   - `window_status` gets its own enum section with `values`, a `four_postulate_record` with keys `i`, `ii`, `iii` and `iv`
     (rule 24: MECE over a declared domain, same grain, intent coherence, state coherence), and a `token_census`. The census is a
     word-boundary count of each value's token over the repo, with its denominator.
   - Keep `unpublished_account_ids`.
2. **The read route.** Add ONE summary route to `entry.py`'s ROUTES. Suggested key:
   `GET /api/scoped/investor-reporting/reporting/client/{client_id}/summary`.
   - Map it to an operation in ENTRY.
   - The operation returns the summary's stored bytes ONLY if every account id the summary names is in the viewer's
     `permitted_account_set`. That covers `accounts[].account_id` AND `unpublished_account_ids`, and uses the same check as
     `_check_covered`.
   - Otherwise raise `AccountNotCovered` (`OBJECT_NOT_COVERED`) with no bytes.
   - The client id is validated as an id, never trusted. An absent summary is `NOT_READY`.
   - The account route is unchanged.
   - Declare the same route key in `infra/aws/terraform/investor-reporting/reporting-read/` (locals and the API route resource,
     beside the account route, on the same integration). This is text only; nothing is applied.
3. **Tests.** Write `infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_summary.py`, with stubbed S3 and scope.
   - full coverage is served;
   - partial coverage is refused `OBJECT_NOT_COVERED`;
   - another firm's client is refused;
   - a missing summary is `NOT_READY`.
   - The file names `summary`, `OBJECT_NOT_COVERED`, `partial` and `firm`.

<criterion id="DB9-1-AC1" cell_refs="DB-b-16"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r9/p9_1_ac1_summary_contract_matches_builder.py" .</invocation><expect>DB9-1-AC1 PASS</expect></criterion>
`DB9-1-AC1` -- the contract is 0.1.0 and states the address. `window_status` carries its record and census, and the builder's
document carries every required key and no undeclared one. Base: FAIL (no contract).

<criterion id="DB9-1-AC2" cell_refs="DB-b-16"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r9/p9_1_ac2_read_route_summary_tests.py" .</invocation><expect>DB9-1-AC2 PASS</expect></criterion>
`DB9-1-AC2` -- the read route suite passes with the summary arms: at least 14 tests (11 at the base), 0 failed. Base: FAIL (no
file).

<criterion id="DB9-1-AC3" cell_refs="DB-b-16"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r9/p9_1_ac3_summary_route_declared.py" .</invocation><expect>DB9-1-AC3 PASS</expect></criterion>
`DB9-1-AC3` -- one summary route is in ROUTES, mapped to an ENTRY operation and declared in the reporting-read Terraform. The
account route is unchanged. Base: FAIL (0 summary routes).

<expected_criteria>DB9-1-AC1,DB9-1-AC2,DB9-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. A second worker (DB-b-17) is building the publisher's summary writes in
  `reporting-publish/`, and a third (DB-b-15) is working on the reporting gold producer. Do not touch either surface.
- **AWS:** none. No plan, no apply, no invoke, no S3 read or write. Tests use stubs.
- **Refusal clause.** A change to the account route's behaviour, or an existing test that moves, is a defect: stop and file a row.
  No client name in any record; ids only.

<paths>
org/standards/IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json
infra/aws/lambda/investor-reporting/reporting/entry.py
infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_summary.py
infra/aws/terraform/investor-reporting/reporting-read/locals.tf
infra/aws/terraform/investor-reporting/reporting-read/api.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~3/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/investor-reporting/`,
`org/standards/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 9 (round 9, workstream B), cell `DB-b-16`.
<owned_cells>DB-b-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB9-1-AC1, DB9-1-AC2, DB9-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~3/IRPT_DASHBD.TO-DB-b-16.p3-summary-contract-and-read-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB9-1-AC1,DB9-1-AC2,DB9-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the route key and its coverage rule;
- the contract's `window_status` values with their census;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served read Lambda irpt-49f-reporting-read-lambda's source and its API route declaration, plus one new standards contract; 0 served bytes move in the cell. The deploy, the route apply and the first served summary are the issuer's P-2 packet with both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- the read role already reads the platinum reporting prefix; no policy text changes in this cell (if the worker finds the summary key outside the role's read grant, that is a row).
comp-routes: RUN -- one route is ADDED (the summary GET) on the existing reporting-read integration; the account route is unchanged (graded by AC3).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: the route answers Cache-Control private, no-cache as the account route does; no CloudFront surface is touched.
comp-adversary: RUN -- DB9-1-AC1 base FAIL (no contract), DB9-1-AC2 base FAIL (no file), DB9-1-AC3 base FAIL (0 summary routes); AC1's checker passed a synthetic valid contract and failed 4 negative controls (undeclared builder key, postulate iv empty, version 0.2.0, unpublished_account_ids dropped); dry-run at the base 2026-10-03 ~01:2xZ.
lane: the <paths> block IS the grant.
</preflight>
