# TO-IB-yr-293 -- allowedFirmIds is READ, not merely recorded: the projection carries it and decide() refuses a data_firm outside it by a named code

<to_id>IRPT_BCKEND.TO-IB-yr-293</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~96</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-293` (`decompositions/IRPT_BCKEND_DECOMP_R29_Y.md`)

---

## WORKER FACE

### THE CELL

A durable service principal `svc-irpt-analysis@opalinvest.com` is about to be created in `opal-users-v2` with
`firmId opal-capital`, `role admin`, `userType service`, `status active` and `allowedFirmIds cottonwood`. Two
readings measured at HEAD say that last attribute restricts NOTHING today:

1. `infra/aws/lambda/investor-reporting/_scope/canonical_profile_reads.py` projects the profile row through two
   tuples, `_USER_FIELDS` (the DynamoDB projection, eleven names ending `"role", "userType"`) and
   `_USER_RETURN_FIELDS` (the seven names returned). Neither names `allowedFirmIds`, so the consumer never sees it.
2. `infra/aws/lambda/investor-reporting/ycharts/generate/current_authority.py` `decide(user, record, *,
   data_firm, now, phase)` grades that projected row. Scope is `OPAL_GLOBAL` when `firmId == "opal-capital"` or
   `userType == "Dev"`, else `OWN_FIRM`; an OPAL_GLOBAL actor passes ANY `data_firm`. The word `allowedFirmIds`
   does not occur in the file.

**Your cell, part 1 -- the projection carries the attribute.** Append `"allowedFirmIds"` as the LAST name of both
`_USER_FIELDS` and `_USER_RETURN_FIELDS` (order matters: the projection expression is built from the tuple, and
the check's stub expects it twelfth, after `userType`). A row without the attribute returns a dict without the key
(the existing `{field: row[field] for field in _USER_RETURN_FIELDS if field in row}` already does this). The test
pin `USER_FIELDS` in `_scope/tests/test_canonical_profile_reads.py` (around line 29) moves to match, and you add
one test there: a row carrying `allowedFirmIds` (DynamoDB `S`, value `cottonwood`) returns it verbatim; a row
without it returns no such key; `passwordHash` still never returns.

**Your cell, part 2 -- decide() reads it.** In `current_authority.py` add a helper (for example
`allowed_firm_ids(user)`) that returns `None` when the attribute is absent or is the string `ALL` (case-sensitive,
exactly the estate's own unrestricted marker), else the list of firm ids: a comma-separated string is split and
each token stripped, empty tokens dropped; a list is taken as-is (each item stripped). In `decide()`, AFTER the
scope is computed and the existing `OWN_FIRM` refusal, and BEFORE `evidence["decision"] = "ALLOWED"`: if the
helper returns a list and `data_firm` is not in it, `refuse("ACTOR_FIRM_NOT_ALLOWED")`. The evidence dict gains two
keys, initialised with the others at the top: `allowed_firm_ids` (the list, or `None`) and
`allowed_firm_ids_absent` (`True` when the attribute is absent, `False` otherwise -- `ALL` is present, not absent).
Update the module docstring's scope sentence with one line naming the new refusal. Nothing else in `decide()`
moves; every existing refusal keeps its order and code.

**Part 3 -- the test.** `ycharts/generate/tests/test_allowed_firms.py` (pytest, import `decide` and
`CurrentAuthorityRefused` from `current_authority` exactly as `test_resident_worker.py:32` does) with the five
cases the check runs, plus one: an `OWN_FIRM` actor (`firmId 49financial`, `allowedFirmIds "49financial"`) on its
own firm is ALLOWED and on `inflection` refuses `ACTOR_SCOPE_REFUSED` (the EXISTING code, which fires first).

**Do NOT** touch `resident_worker.py`, `resident_installed.py`, `_scope/resolve.py` or any handler: the resident
already retains a `CurrentAuthorityRefused` for retry and journals its code, and that behaviour is a separate
question (row S231) that this cell does not decide. **Do NOT** add a fixture or a stub for DynamoDB beyond the
botocore Stubber the existing test file already uses.

**Why:** CTO 103221 limit (3) and the W27 CTO half condition 5; the W27 CRO half condition 1 requires this proven
BEFORE the window opens: *"a job submitted under this principal for a firm other than cottonwood is REFUSED by a
named code."* The name is `ACTOR_FIRM_NOT_ALLOWED`.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y29-3-AC1" cell_refs="IB-yr-293"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_293_allowed_firms.py</invocation><expect>PASS: all five allowed-firm cases hold</expect></criterion>

<criterion id="Y29-3-AC2" cell_refs="IB-yr-293"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_293_projection.py</invocation><expect>PASS: projection carries allowedFirmIds verbatim, absent stays absent, passwordHash never returned</expect></criterion>

<criterion id="Y29-3-AC3" cell_refs="IB-yr-293"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider ycharts/generate/tests/test_resident_worker.py _scope/tests/test_canonical_profile_reads.py ycharts/generate/tests/test_allowed_firms.py</invocation><expect>0 failed and not fewer than 88 passed (87 at base on the two existing files plus at least one new node; 8 skipped unchanged)</expect></criterion>

<expected_criteria>Y29-3-AC1,Y29-3-AC2,Y29-3-AC3</expected_criteria>

**Issuer's base run at CLOUD HEAD a7a6d286f2 (CTO 103159: the base reading beside every criterion):**

- **AC1 -- FAIL as expected:** `2 of 5 cases hold`. Case 1 (restricted row, foreign firm) reads **`ALLOWED`** --
  that is the recorded-not-enforced state; cases 2 and 4 fail only on the evidence keys not existing yet; cases 3
  and 5 already pass because today nothing is refused.
- **AC2 -- FAIL as expected:** `FAIL: reader did not project allowedFirmIds -- Error getting response stub for
  operation GetItem: Expected parameters ...` -- the stub demands the twelve-field projection; the reader sends
  eleven.
- **AC3 -- FAIL as expected on the new file (absent).** The two existing files read **87 passed, 8 skipped, 0
  failed in 44.9 s** and that is the control inside this criterion: it must not lose a node. If your change turns
  any existing node red, that node's message is your finding, not a test to edit.

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~96/` and
  this order's file. **`_scope/canonical_profile_reads.py` is a shared surface whose writer is `~P` under the
  closer contract; you are granted the ONE-FIELD patch described above and nothing else in that file or directory.**
  `test_resident_worker.py` is READ-ONLY (read it for the import shape; add nothing to it).
- **No AWS call, no deploy, no Terraform, no vendor/external network call.** The DynamoDB reads in the tests are
  botocore Stubber responses.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass. If a file you need is not in `<paths>`, that is a REFUSAL AND A ROW.
- **Row ids** are `IRPT_BCKEND-W96-S<k>`, appended to the project surprise channel with a
  `## <ID> -- <one line>` markdown heading. Other seats append concurrently: re-read immediately before writing and
  re-check your `<k>`. `hazard_standing` is `ARMED` or `INERT`, nothing else. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~96 <0.9.0_WK_IRPT_BCKEND~96@opal.agent>" -F <msgfile> -- <paths>`; do NOT pre-`git add`; the message file is written by the Write tool or python, never a shell heredoc and never a `python -c "..."` containing double quotes.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty).
- **MSYS trap (row S215):** a unix path inside a `python -c` SOURCE BODY is not converted. Pass paths as argv.
- **Search discipline:** raw recursive `grep`/`find` in Bash is gated; use `comp-find` or the native Grep/Glob/Read
  tools, and never pipe `comp-find` into `head`.
- **ASCII only** in every file you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/current_authority.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_allowed_firms.py
infra/aws/lambda/investor-reporting/_scope/canonical_profile_reads.py
infra/aws/lambda/investor-reporting/_scope/tests/test_canonical_profile_reads.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_293_allowed_firms.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_293_projection.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R29_Y.md</decomp_doc> round 29, workstream ~Y, cell `IB-yr-293`.
<owned_cells>IB-yr-293</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y29-3-AC1, Y29-3-AC2, Y29-3-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~96/IRPT_BCKEND.TO-IB-yr-293.allowed-firm-ids-enforced-at-decide.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y29-3-AC1,Y29-3-AC2,Y29-3-AC3` BEFORE the flip. Copy
the shape from `deliverables/0.9.0_WK_IRPT_BCKEND~92/IRPT_BCKEND.TO-IB-yr-282.served-answers-tell-the-truth.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line; the exact diff of the two tuples in
`canonical_profile_reads.py`; the position of the new refusal relative to the existing ones (line numbers); the
passed/skipped counts of AC3; the diff summary; and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-blast: RUN -- WORLD (an authorization decision on the resident's path, and a one-field projection change on a P-lane file). Reach measured from the code: decide() is called by reports/resident_installed.py make_principal_for (the resident) and by ycharts/generate/resident_worker.py; every existing profile row has NO allowedFirmIds attribute in the projection today, and the cell's helper returns None for absent and for ALL, so every existing principal's decision is byte-identical (AC1 case 4, AC3's 87 existing nodes). The only rows that gain a refusal are rows that carry a restricting list, of which the first will be svc-irpt-analysis. The projection change adds one attribute to a DynamoDB ProjectionExpression; no IAM change is needed to read an attribute the role already reads the item of.
comp-iam: DECLARED-NOT-APPLICABLE for the cell (no role or policy moves); the window act's own census of who can read the secret is a separate half.
comp-adversary: RUN -- three risks. (1) The worker enforces at the wrong layer (a header, resolve.py) where a forged value could reach it: the face pins the READ to the projected DynamoDB row and forbids resolve.py. (2) ALL or absent gets treated as a restriction and every existing principal is refused: AC1 cases 3 and 4 and AC3's 87 existing nodes. (3) The tuple order is changed so the projection expression drifts and every profile read fails: AC2's stub pins the twelve-field order and AC3's existing reads stay green. Blind to rows whose allowedFirmIds is a DynamoDB type other than S or L (for example SS): the helper's list branch takes any iterable of strings, and a genuinely foreign type raises in decide() as a ValueError the resident journals -- stated, not hidden.
lane: the <paths> block IS the grant. Measured: no non-terminal ~P or ~M order names canonical_profile_reads.py, its test, or current_authority.py (11 non-terminal orders of 155 scanned, 0 hits). The _scope delta is the exact one-field patch CONTRACT.md row 21 has Y supply; the drain records its hash in STATUS~Y.md for ~P.
</preflight>
