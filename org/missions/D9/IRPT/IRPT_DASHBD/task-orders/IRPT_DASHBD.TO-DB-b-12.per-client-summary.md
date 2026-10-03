# TO IRPT_DASHBD.TO-DB-b-12 -- P-3, one precomputed per-client summary built by the publisher, its address from the naming builder (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-12</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 178 (@2a537cbad4, msg 104324), fold-in section 1, P-3: "The
picker reads ONE precomputed per-client summary, not one PATH A request per account (`ReportingTab.tsx:614-640`). Every new address is
`lib/opal_naming.py address()` output, cited in the cell (rule 30). Backend summary at `~P`; the page at `~D`" | **Decomp cell:**
`DB-b-12` (decomposition section 5) | **outcome_ref:** P-1 (under 2 s; a window change computes nothing on the backend) |
**depends_on:** none (queued on the shared DIR after DB-b-11)

---

## WORKER FACE

**The cell.** The Performance picker (`portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx:614-640`) issues one
`GET /performance` per account per window. P-3 replaces that with ONE precomputed summary per client, which the publisher writes
beside the per-account series. This cell builds the producer and proves it locally. The contract file, the read route and the
deploy are the issuer's next step; the page is `2.0.0_SA_COO~D`'s.

**What you build** (in `reporting-publish/publisher.py`, pure functions, beside `build_series` and `build_manifest`):
- `build_client_summary(client, accounts)`. `client` is one directory client: its id and its account ids, from the 49 Financial
  directory the `directory/` function serves; name the exact source you read. `accounts` holds each account's built series and
  manifest.
- The summary carries the client id, the firm, `as_of`, and per account: `account_id`, `as_of`, `first_data_date`, the series
  object's name, and the standard windows YTD, QTD, 1Y, 3Y and SI as precomputed TWRs. A window is null when the series does not
  span it, never a partial.
- The page then paints every account's figure from one object, and draws any custom window from the per-account series it already
  fetches. No backend compute.
- **The address:** `opal_naming.address("irpt", "49financial", "platinum", "reporting", "client=<id>", "summary.json")` or the
  builder's own form of it. If the builder refuses, that is a missing registry row: file a row and stop the address part, never
  hand-type a key (rule 30).

**Prove it.**
- `reporting-publish/tests/test_client_summary.py`, at least 4 tests, naming `client`, `YTD` and `series`:
  - each window equals the geometric link of the series over it;
  - a window the series does not span is null;
  - a client with no published account refuses by name;
  - the address is the builder's.
- `CLIENT_SUMMARY_R5.json` in your deliverables folder, from a LOCAL dry run (reads only, nothing uploaded) over the 49 Financial
  directory and today's published 6-account series: `builder_call` (the literal `address(...)` call), `address_example`,
  `clients`, `accounts_covered`, `seconds`, `shape` (one example summary with account ids only, no names) and `directory_source`.

<criterion id="DB5-2-AC1" cell_refs="DB-b-12"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_2_ac1_client_summary_tests.py" .</invocation><expect>DB5-2-AC1 PASS</expect></criterion>
`DB5-2-AC1` -- the summary tests pass (at least 4). Base: FAIL (no file).

<criterion id="DB5-2-AC2" cell_refs="DB-b-12"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_2_ac2_summary_record.py" .</invocation><expect>DB5-2-AC2 PASS</expect></criterion>
`DB5-2-AC2` -- the record's address is the builder's (the check re-runs the call), and the dry run built summaries for real clients.
Base: FAIL (no record).

<criterion id="DB5-2-AC3" cell_refs="DB-b-12"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB5-2-AC3</invocation><expect>DB5-2-AC3 PASS</expect></criterion>
`DB5-2-AC3` -- reporting-gold and reporting-publish suites pass unchanged. Base: PASS (a regression guard).

<expected_criteria>DB5-2-AC1,DB5-2-AC2,DB5-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only. No S3 write, no upload, no Terraform, no invoke. No client or account NAME in any record: ids only.
- **Refusal clause.** A builder refusal is a row (rule 30), never a typed key. A directory you cannot read is a row, never a guess.
  An existing test that moves is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_client_summary.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `portal/src/pages/InvestorReporting/`, `lib/`, `infra/logic/registry/`, `docs/contracts/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 5 (round 5, workstream B), cell `DB-b-12`.
<owned_cells>DB-b-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB5-2-AC1, DB5-2-AC2, DB5-2-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-12.per-client-summary.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB5-2-AC1,DB5-2-AC2,DB5-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the builder address;
- the client and account counts of the dry run;
- the directory source;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a pure producer function in the served publisher's module and its tests; 0 served bytes move (the summary's contract, route and deploy follow under the issuer's packet).
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes in the cell.
comp-routes: DECLARED-NOT-APPLICABLE in the cell -- the read route for the summary is the issuer's next step.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 08:15 ET publisher schedule is not moved; the summary rides that fire later.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB5-2-AC1 base FAIL (no file), DB5-2-AC2 base FAIL (no record), DB5-2-AC3 base PASS (regression guard), dry-run at the base 2026-10-02 ~18:2xZ.
lane: the <paths> block IS the grant.
</preflight>
