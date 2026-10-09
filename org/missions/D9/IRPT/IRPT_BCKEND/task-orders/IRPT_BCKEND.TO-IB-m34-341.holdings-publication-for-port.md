# TO IRPT_BCKEND.TO-IB-m34-341 -- the production publication_for port for the Performance client statement reader

<to_id>IRPT_BCKEND.TO-IB-m34-341</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~201</issued_to>
<issued_by>2.0.0_SA_COO~M2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop (seat on dell2) | **Workstream:** ~M | **Decomp cell:** `IB-mp-341`
(`decompositions/IRPT_BCKEND_DECOMP_R34_M.md`) | **outcome_ref:** CTO msg 2127 (release 6, port 2) | **depends_on:** none

---

## WORKER FACE

**The gap.** `infra/aws/lambda/investor-reporting/_scope/accepted_custody.py` `AcceptedCustodyReader` takes a `publication_for(firm_id)`
port that returns an object with `capture(*, as_of, account_ids) -> (document, manifest, receipt)` and
`load_pinned(receipt, *, account_ids) -> (document, manifest)`. `HoldingsPublication` (holdings/publication.py:122) already is that
object, and already refuses any firm outside the three canonical ones. What does not exist is the production constructor: a factory
that a release wires into the reader. The contract is port 2 of
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release6_custody/CUSTODY_PORT_CONTRACT.md`.

**What you build** (worktree `C:/dev/wk-irpt-bckend-201`, branch `wk-IRPT_BCKEND-201`):

1. In `infra/aws/lambda/investor-reporting/holdings/snapshot.py`, next to `_publication_reader`, add
   `holdings_publication_for(s3_client=None)`. It returns `publication_for(firm_id)`, which returns
   `_publication_reader(firm_id, DEFAULT_PREFIX, s3_client)` -- the production namespace only, never QA. A docstring states the
   contract in two lines (the port of AcceptedCustodyReader; firm-fenced by HoldingsPublication, never ALL). No S3 call happens until
   capture or load_pinned. Do not change `_publication_reader`, `HoldingsPublication` or any existing function.
2. Add `infra/aws/lambda/investor-reporting/holdings/tests/test_publication_port.py`: the three firms construct; "ALL", "", None
   and an unknown firm raise `PublicationRefused`; a capture -> load_pinned round trip over `test_publication.py`'s `setup()` /
   `publish()` returns equal (document, manifest), and manifest.revision equals receipt.date_row.revision.
3. In your report, state the port's S3 **read set** (bucket, key patterns, actions -- `s3:GetObject` with version ids on the
   `platinum/holdings` current index, dated manifests and parts), read from `HoldingsPublication.location` and `read_exact`, so the
   release-6 pair can carry the grant.
4. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~201 <0.9.0_WK_IRPT_BCKEND~201@opal.agent>" -F <msgfile> -- <paths>`
   (message file written with the Write tool). Run the criteria, write report + proof of spec, then flip this order and commit that.

<criterion id="IBM34-341-AC1" cell_refs="IB-mp-341"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R34_CHECKS/m34_cells.py . IBM34-341-AC1</invocation><expect>IBM34-341-AC1 PASS</expect></criterion>
`IBM34-341-AC1` -- the factory fences 3 of 3 firms in the production namespace with no S3 call at construction, refuses 5 of 5 bad
firms, and capture/load_pinned meet the reader's shape rules with an equal pinned reload. Base: FAIL.

<criterion id="IBM34-341-AC2" cell_refs="IB-mp-341"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R34_CHECKS/m34_cells.py . IBM34-341-AC2</invocation><expect>IBM34-341-AC2 PASS</expect></criterion>
`IBM34-341-AC2` -- the holdings and _scope suites pass. Base: PASS (176; 223 + 67 subtests).

<criterion id="IBM34-G-201" cell_refs="IB-mp-341"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R34_CHECKS/m34_cells.py . IBM34-G-201</invocation><expect>IBM34-G-201 PASS</expect></criterion>
`IBM34-G-201` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IBM34-341-AC1,IBM34-341-AC2,IBM34-G-201</expected_criteria>

Run every invocation from `C:/dev/wk-irpt-bckend-201`.

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **Risk WORLD by the L6 gate floor** (an infra/ path; the cell itself makes no AWS call and deploys nothing -- it ships inside ~Y2's release-6 pair).
- **No AWS call, no deploy, no bun, no downloads.** Tests use the in-memory S3 of `test_publication.py`.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A):** use 2026 dates only in any fixture.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another file.
- **Refusal clause.** An edit to any existing function, to publication.py, to accepted_custody.py, or a QA-namespace default is a
  defect: stop and file a row (id `IRPT_BCKEND-W201-S<k>`), and do not flip this order.

<paths>
infra/aws/lambda/investor-reporting/holdings/snapshot.py
infra/aws/lambda/investor-reporting/holdings/tests/test_publication_port.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-m34-341.holdings-publication-for-port.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R34_M.md</decomp_doc> (round 34, workstream ~M), cell `IB-mp-341`.
<owned_cells>IB-mp-341</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM34-341-AC1, IBM34-341-AC2, IBM34-G-201. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/IRPT_BCKEND.TO-IB-m34-341.holdings-publication-for-port.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IBM34-341-AC1,IBM34-341-AC2,IBM34-G-201` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the S3 read set, any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source factory and its test; no schedule, deploy or write.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call in this cell; the read set is reported for ~Y2's release-6 pair, which carries the grant.
comp-adversary: RUN -- AC1 dry-run at base FAIL (function absent); PASS on a positive control (the minimal factory, uncommitted, reverted); AC2 and the guard PASS at base.
lane: the <paths> block IS the grant; holdings/snapshot.py is ~M's file (prior authors 2.0.0_SA_COO~M).
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msg 2127; ~Y2 msg 2131 / contract @859ae01405; signature sent to ~Y2 01:51Z. Slot ~201 (block ~200..~219, msg 974).
Dry-run at the base 2026-10-09 ~02:0xZ on worktree `C:/dev/wk-irpt-bckend-201` (box/dell2 6066a7d5cb).
