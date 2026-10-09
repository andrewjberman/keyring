# TO IRPT_BCKEND.TO-IB-pr-382 -- the production custody ports ~P owns for release 6: current_selection, interpret_source, validate_evidence

<to_id>IRPT_BCKEND.TO-IB-pr-382</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~190</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling msg 2128 (on ~Y2 msg 2126); port contract
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release6_custody/CUSTODY_PORT_CONTRACT.md` @859ae01405 (~Y2 msg 2132) |
**Decomp cell:** `IB-pr-382` (decomposition section 87) | **outcome_ref:** FWD-8 / IRPT_CUSTDY E2a (a real Performance client statement
submission; row IRPT_CUSTDY-W18-S1) | **depends_on:** none. ~M2 builds port 2 (`publication_for`) in parallel; ~Y2 wires all four into
`reports/generate_installed.py` as release 6.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-190` (branch `wk-IRPT_BCKEND-190`, cut from `box/dell2`). Work and commit only there.
`L` = `infra/aws/lambda/investor-reporting`. Paths below are relative to the worktree. Keep scratch outside the worktree.

**The gap.** Live `irpt-ycharts-generate` refuses every custody submission: `L/reports/generate_installed.py:172` raises
`CUSTODY_FACTORY_REQUIRED`, because no production `AcceptedCustodyReader` exists. `L/_scope/accepted_custody.py` (class
`AcceptedCustodyReader`) takes five ports, and its economic ports have "intentionally no default implementation". You build THREE of them,
the Performance client statement's own rules. Read the contract file above IN FULL first; the code at HEAD wins over its text.
- **Port 1, `current_selection(principal, owner) -> str`:** the CURRENT verified selected-account-set fingerprint (a 64-hex sha256 that
  `custody_binding.sha` accepts). It must read current state on every call and never cache, because the reader calls it up to 4 times and a
  change between calls refuses. The likely source is `L/_scope/selection_store.py` `SelectionStore`; confirm it or say why not.
- **Port 3, `interpret_source(document, manifest, *, principal, owner, publication_receipt) -> dict`:** it returns EXACTLY the keys
  `actual_custody`, `original_rows`, `source_receipts` and `revision_refs`.
  - `actual_custody` has `firm_id == owner.firm_id`, `account_ids == owner.account_ids` (same order) and
    `custody_as_of == receipt.business_date`.
  - Every value is JSON-wire (no NaN, Decimal or bytes).
  - It is deterministic for a pinned receipt.
- **Port 4, `validate_evidence(evidence, *, principal, owner, publication_receipt) -> bool`:** `True` ONLY for the complete paired
  economic/source contract under the admitted rules. Anything else, or a raise, refuses. A permissive or fake validator is not a deployed
  capability.

**Your cell. Code and tests only; nothing is built, uploaded or applied.**
1. Find the admitted rules: what a holdings publication `document` / `manifest` contains, and how custody evidence pairs economics to
   source. Read `L/_scope/accepted_custody.py`, `L/_scope/custody_binding.py`, `L/_scope/custody.py`,
   `L/ycharts/generate/custody_submission.py`, the IRPT_CUSTDY PRD (`org/missions/D9/IRPT/IRPT_CUSTDY/prd/`), and the holdings
   publication code `~M2` builds against.
   - If a rule the ports need is not written anywhere, STOP: file a row naming exactly what is undefined. Do not invent an economic rule.
2. Implement the three ports in ONE new module, `L/_scope/custody_ports.py`, with a small factory the installer can call. No new AWS
   client beyond what the source of port 1 already uses.
3. **Tests** in `L/_scope/tests/test_custody_ports.py`, with these names:
   - `custody_current_selection`, at least 2: a current fingerprint, and a change between calls observed;
   - `custody_interpret_source`, at least 3: exact key set, owner/receipt binding, and determinism for one pinned receipt;
   - `custody_validate_evidence`, at least 3: complete is True, incomplete is False, and a raise refuses;
   - `custody_ports_compose`, at least 1: a real `AcceptedCustodyReader` built with your three ports, plus in-memory fakes for the store
     and for port 2 in the contract's exact shape, reads one fixture end to end.
   The whole `L/_scope/tests` suite still passes.
4. **Read-set file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~190/IB94-1_custody_ports_read_set.json`:
   `{ports: {current_selection|interpret_source|validate_evidence: {module, function, reads: [{service, resource, action}]}},
   release6_staged: [repo paths release 6 must stage]}`. Release 6's pair carries the IAM grant from it.

<criterion id="IB94-1-AC1" cell_refs="IB-pr-382"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r94/p94_cells.py" . IB94-1-AC1</invocation><expect>IB94-1-AC1 PASS</expect></criterion>
`IB94-1-AC1` -- the `custody_current_selection` (>= 2) and `custody_interpret_source` (>= 3) tests pass. Base: FAIL.

<criterion id="IB94-1-AC2" cell_refs="IB-pr-382"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r94/p94_cells.py" . IB94-1-AC2</invocation><expect>IB94-1-AC2 PASS</expect></criterion>
`IB94-1-AC2` -- the `custody_validate_evidence` (>= 3) and `custody_ports_compose` (>= 1) tests pass, and the `_scope` suite passes whole.
Base: FAIL.

<criterion id="IB94-1-AC3" cell_refs="IB-pr-382"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r94/p94_cells.py" . IB94-1-AC3</invocation><expect>IB94-1-AC3 PASS</expect></criterion>
`IB94-1-AC3` -- the read-set file names each port's module, function and AWS reads, plus the paths release 6 must stage. Base: FAIL.

<expected_criteria>IB94-1-AC1, IB94-1-AC2, IB94-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No build, upload, apply or deploy. AWS reads only, if any.
- **No edit** to `accepted_custody.py`, `custody_binding.py`, `generate_installed.py` or the contract. If one is needed, STOP and file a row.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W190-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~190" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~190@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~190 <0.9.0_WK_IRPT_BCKEND~190@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/_scope/custody_ports.py
infra/aws/lambda/investor-reporting/_scope/tests/test_custody_ports.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-382.custody-ports-selection-interpret-validate.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~190/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 87 (round 94, workstream ~P), cell `IB-pr-382`.
<owned_cells>IB-pr-382</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB94-1-AC1, IB94-1-AC2, IB94-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~190/IRPT_BCKEND.TO-IB-pr-382.custody-ports-selection-interpret-validate.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the admitted rules you found and where, the module and factory, the commit hashes, each criterion's
last line, the read set, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- live irpt-ycharts-generate (release 5) raises CUSTODY_FACTORY_REQUIRED at generate_installed.py:172 (row IRPT_CUSTDY-W18-S1 @c562748b71); AcceptedCustodyReader ports 1/3/4 have no production implementation; new module only, no existing module edited; release 6 (~Y2) is the consumer.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change here; the read set feeds release 6's pair.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p94_cells.py dry-run at base f506a07c1a on dell2 2026-10-09 ~02:1xZ: AC1, AC2, AC3 FAIL (-k custody_current_selection and -k custody_validate_evidence select 0 of 223; no read-set file); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; _scope/custody_ports.py is new and ~P's (CTO msg 2128); port 2 is ~M2's, the installer ~Y2's.
</preflight>
