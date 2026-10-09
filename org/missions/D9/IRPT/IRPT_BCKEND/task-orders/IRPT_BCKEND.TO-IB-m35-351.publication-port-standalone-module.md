# TO IRPT_BCKEND.TO-IB-m35-351 -- the publication_for port as a standalone module (release 6 staging collision)

<to_id>IRPT_BCKEND.TO-IB-m35-351</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~202</issued_to>
<issued_by>2.0.0_SA_COO~M2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>35</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop (seat on dell2) | **Workstream:** ~M | **Decomp cell:** `IB-mp-351`
(`decompositions/IRPT_BCKEND_DECOMP_R35_M.md`) | **outcome_ref:** ~Y2 msg 2202 (release 6, port 2) | **depends_on:** none

---

## WORKER FACE

**The problem.** Round 34 put `holdings_publication_for` in `infra/aws/lambda/investor-reporting/holdings/snapshot.py`, whose
`_publication_reader` does `from publication import HoldingsPublication`. The function that needs the port, `irpt-ycharts-generate`,
already packages a different `publication.py` (from `ycharts/extract/`), and `snapshot.py` also imports `enforce`, `ids` and a
`sys.path` walk at load. So the port moves to its own small module; `~Y2` stages `holdings/publication.py` under the name
`holdings_publication.py` beside it.

**What you build** (worktree `C:/dev/wk-irpt-bckend-202`, branch `wk-IRPT_BCKEND-202`):

1. New file `infra/aws/lambda/investor-reporting/holdings/holdings_publication_port.py`:
   - a module docstring: the production `publication_for` port of `_scope/accepted_custody.AcceptedCustodyReader`; production
     namespace only, firm-fenced by HoldingsPublication (never ALL); no S3 call until capture/load_pinned; it imports
     `holdings_publication` (the staged name in irpt-ycharts-generate) and falls back to `publication` (the holdings functions);
   - `try: from holdings_publication import HoldingsPublication` / `except ImportError: from publication import HoldingsPublication`;
   - `holdings_publication_for(s3_client=None)` returning `publication_for(firm_id)`, which builds
     `HoldingsPublication(s3, firm_id)` with `qa` left False; when `s3_client` is None it creates
     `boto3.client("s3", region_name="us-east-1")` inside `publication_for` (lazily, not at import).
2. In `holdings/snapshot.py`, delete `holdings_publication_for` (added in round 34; no consumers). Change nothing else there.
3. In `holdings/tests/test_publication_port.py`, import the port from `holdings_publication_port` instead of `snapshot`; keep every
   test's meaning.
4. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~202 <0.9.0_WK_IRPT_BCKEND~202@opal.agent>" -F <msgfile> -- <paths>`
   (message file written with the Write tool). Run the criteria, write report + proof of spec, then flip this order and commit that.

<criterion id="IBM35-351-AC1" cell_refs="IB-mp-351"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R35_CHECKS/m35_cells.py . IBM35-351-AC1</invocation><expect>IBM35-351-AC1 PASS</expect></criterion>
`IBM35-351-AC1` -- staged the way irpt-ycharts-generate stages it (beside ycharts' publication.py), the port imports, binds
holdings_publication.HoldingsPublication in the production namespace and refuses ALL; snapshot.py no longer defines it. Base: FAIL.

<criterion id="IBM35-351-AC2" cell_refs="IB-mp-351"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R35_CHECKS/m35_cells.py . IBM35-351-AC2</invocation><expect>IBM35-351-AC2 PASS</expect></criterion>
`IBM35-351-AC2` -- the holdings and _scope suites pass. Base: PASS.

<criterion id="IBM35-G-202" cell_refs="IB-mp-351"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R35_CHECKS/m35_cells.py . IBM35-G-202</invocation><expect>IBM35-G-202 PASS</expect></criterion>
`IBM35-G-202` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IBM35-351-AC1,IBM35-351-AC2,IBM35-G-202</expected_criteria>

Run every invocation from `C:/dev/wk-irpt-bckend-202`.

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **Risk WORLD by the L6 gate floor** (an infra/ path); the cell makes no AWS call and deploys nothing.
- **No AWS call, no deploy, no bun, no downloads.** 2026 dates only in any fixture.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another file.
- **Refusal clause.** An edit to publication.py, to any other snapshot.py function, to accepted_custody.py or to the source map is a
  defect: stop and file a row (id `IRPT_BCKEND-W202-S<k>`), and do not flip this order.

<paths>
infra/aws/lambda/investor-reporting/holdings/holdings_publication_port.py
infra/aws/lambda/investor-reporting/holdings/snapshot.py
infra/aws/lambda/investor-reporting/holdings/tests/test_publication_port.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~202/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-m35-351.publication-port-standalone-module.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R35_M.md</decomp_doc> (round 35, workstream ~M), cell `IB-mp-351`.
<owned_cells>IB-mp-351</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM35-351-AC1, IBM35-351-AC2, IBM35-G-202. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~202/IRPT_BCKEND.TO-IB-m35-351.publication-port-standalone-module.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IBM35-351-AC1,IBM35-351-AC2,IBM35-G-202` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source module move and its test; no schedule, deploy or write.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the read set is unchanged from round 34 (packet @36b0cbb93f).
comp-adversary: RUN -- AC1 dry-run at base FAIL (module absent); PASS on a positive control (the intended module + the snapshot removal, uncommitted, reverted); the first probe failed on ycharts' publication.py sibling import (certify) and the check now stages ycharts/extract on the path, as the function carries it.
lane: the <paths> block IS the grant; holdings/ is ~M's.
</preflight>

Source: ~Y2 msg 2202; reply to ~Y2 02:31Z naming the module. Slot ~202 (block ~200..~219, msg 974).
Dry-run at the base 2026-10-09 ~02:3xZ on worktree `C:/dev/wk-irpt-bckend-202` (box/dell2 d968ed5db5).
