# TO IRPT_BCKEND.TO-IB-pr-363 -- E2: the custody release packet -- P-c1..c3 plus the custody-report-read route as ONE release pair (census at one pin, every changed member owned, both branches, rollback per function, after-reads)

<to_id>IRPT_BCKEND.TO-IB-pr-363</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~171</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 rounds 69-74 analysis @b35c7d8c73 (msg 1214), enrichment E2 | **Decomp cell:** `IB-pr-363`
(decomposition section 69) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 (the custody report export reaches PROD) | **depends_on:** IB-pr-351, 352, 355, 356, 359 (all drained).

---

## WORKER FACE

**What the CTO asks (E2).** ONE release pair for the custody path. Prepare the packet only: nothing is built, uploaded or applied
in this order.
- `infra/aws/lambda/investor-reporting/reports/custody_write.py` (IB-pr-351);
- `infra/aws/lambda/investor-reporting/export/submit_async.py` (IB-pr-352: accept by kind);
- `infra/aws/lambda/investor-reporting/export/custody_read.py` plus `infra/aws/lambda/investor-reporting/export/entry.py` ROUTES and `docs/contracts/investor-reporting/v1/routes.json` (IB-pr-355:
  the custody-report-read route);
- the print page (IB-pr-356/359, portal @63b9382a). Its DEV and PROD landings are Andrew's word, so the packet names it but does not
  move it.

**THE TRAP THAT CAUGHT TWO RELEASES TODAY.**
- `infra/aws/lambda/ci/lambda-source-map.json` stages some members from a `staged_from` row at an OLD pin, so a build ships that
  old blob, not HEAD.
- `irpt-export-render` stages `entry.py` at 34f71024a1, so IB-pr-355's two ROUTES lines would NOT ship.
- **For every changed member, compare the blob the build would package (the row's pin) with the blob at HEAD.**
- Where a named change is missing, re-pin that ONE row in that ONE function (the pin and its sha256), in one commit. That commit is
  the release pin. Never re-pin a row in another function.

**What you build** (worktree `C:/dev/wk-irpt-bckend-171`):

1. **Find every function** that packages each named file (the source map: `source_dir` + `files[]`, or `staged_from` rows), and
   each API route the routes.json row adds. The API routes are applied from `infra/aws/terraform/investor-reporting/api/` (routes.tf
   reads routes.json). If no function packages `custody_write.py`, say so: its caller is IRPT_CUSTDY's producer.
2. **Cut the re-pin commit** if needed. Then run `python infra/aws/lambda/ci/release-census.py <fn> --pin <pin>` per function.
3. **Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~171/IB76-2_custody_release_census.json`:**
   `{"pin": "...", "functions": {"<fn>": {"changed_members": [{"member":"...","owner":"IB-pr-..."}], "rollback_object_version":"...", "live_code_sha256":"..."}}}`.
   - Every changed member is owned by an IB order; a member no named order changed is a RIDER and gets an owner too.
   - The rollback object version is read-only: `s3api list-object-versions` on the artifact key, latest version.
4. **Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~171/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-363.md`.** It covers:
   - Branch A (released): what each principal class can now do -- an Opal or firm principal reads a custody report by ref within
     scope;
   - Branch B (rolled back): the per-function rollback;
   - the pin;
   - the writers of each changed property;
   - the two after-reads: a custody-report-read for ANOTHER firm's report is REFUSED (OBJECT_NOT_COVERED), and an Opal read of one
     custody report by ref returns it.
   Commit it and report its `blob <hash>`. The halves are signed against that blob.

<criterion id="IB76-2-AC1" cell_refs="IB-pr-363"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r76/p76_cells.py" . IB76-2-AC1</invocation><expect>IB76-2-AC1 PASS</expect></criterion>
`IB76-2-AC1` -- the census file carries one pin and, per function, every changed member with an IB-order owner, a rollback object version and the live CodeSha256; the census reproduces at the pin. Base: FAIL (no file).

<criterion id="IB76-2-AC2" cell_refs="IB-pr-363"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r76/p76_cells.py" . IB76-2-AC2</invocation><expect>IB76-2-AC2 PASS</expect></criterion>
`IB76-2-AC2` -- the packet names both branches, the pin, rollback, the other-firm refusal and the custody-report-read after-read. Base: FAIL (no file).

<criterion id="IB76-G-171" cell_refs="IB-pr-363"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r76/p76_cells.py" . IB76-G-171</invocation><expect>IB76-G-171 PASS</expect></criterion>
`IB76-G-171` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB76-2-AC1,IB76-2-AC2,IB76-G-171</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **Vendor egress (Andrew-direct ~18:3xZ 2026-10-07, VERBATIM: "The Dell Boxes have vendor egress as needed."):** this cell needs
  none, so it makes none. No build upload, no apply, no AWS write.
- **Web and downloads (Andrew-direct ~14:0xZ 2026-10-07, VERBATIM: "I do not mind webbrowsing if necessary for research purposes,
  however we do not do downloads."; download tiers bind EVERY box, record @875c5a9b54):** research browsing only when necessary;
  no package, script, program or file fetched from the internet onto any box (the laptop alone fetches, by the checked route);
  `bun` only as `bun --no-install` with a linked node_modules (rules 106215/106221). A vendor API call is not browsing.
- **Fence (ruling 106244, row S371):** only `opal-data-cottonwood` denies this box's identity; the legacy `opal-data-bd/-cot/-inf` are
  inside its grant. A read never widens a fence. A denied read is a row and a stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** A build, upload, terraform plan-with-apply or apply, an S3 write, a re-pin of any row outside the custody functions' named members, or a portal push is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~171/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-363.custody-release-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 69 (round 76, workstream ~P), cell `IB-pr-363`.
<owned_cells>IB-pr-363</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB76-2-AC1, IB76-2-AC2, IB76-G-171. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~171/IRPT_BCKEND.TO-IB-pr-363.custody-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB76-2-AC1,IB76-2-AC2,IB76-G-171` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base b7e16c7230 2026-10-07 ~05:5xZ 2026-10-08: build checks FAIL, guards PASS (p76_cells.py).
lane: the <paths> block IS the grant.
</preflight>
