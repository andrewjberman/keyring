# TO TCKT_VNEXT.TO-R19-L3 -- BUILD the PROFILE firm scope as fail-closed with an explicit global marker (row S134 item 3; source and tests only)

<to_id>TCKT_VNEXT.TO-R19-L3</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~47</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda source path; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R19-ps-3` (`decompositions/TCKT_VNEXT_DECOMP_R19.md`) | **outcome_ref:** row `IRPT_ANLREQ-D2-S134` item 3 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~47`.
- **Worktree:** `C:/dev/wk-tckt-vnext-47` (branch `wk-TCKT_VNEXT-47`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~47 <0.9.0_WK_TCKT_VNEXT~47@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `TCKT_VNEXT-D2-W47-S<k>` (take the next free `<k>`). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before
  its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call of any kind: no AWS, no network, no
  mail, no deploy, no apply, no Terraform (`tests/conftest.py` refuses a real call). **Run NO test file by path (`python <file>`): pytest only, with `-p no:cacheprovider`.** Scratch outside the product tree.

### WHY

Row `IRPT_ANLREQ-D2-S134`: an internal PROFILE row with no `allowedFirmIds` (or an empty list) is admitted for EVERY firm (CTO ruling ADDENDUM 7, item 3: a missing list must mean NO firm). The contract every cell obeys is
`org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md`, section CONTRACT; its item 3 is this cell's. A separate staged migration writes the marker to the staff rows before this code is released: you build the code only.

### THE CELL (`R19-ps-3`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

In `infra/aws/lambda/ticket_center/lambda_function.py`, function `_profile_scope` ONLY (about lines 391-426; read it whole first, and `_resolve_scope` and `_in_profile_scope` after it, which you do not change). Today, after the status test, `val = got.get("allowedFirmIds")`: `None` returns `(None, None)` (every firm) and an empty list returns `(None, None)` too. Replace that tail with the exact rule:

1. **(a) a list.** `allowedFirmIds` a non-empty list whose members are all non-empty strings: return `(frozenset(val), None)` as today. If the attribute `scope_all_firms` is ALSO present (any value), the row is malformed: see (d).
2. **(b) the explicit global marker.** The attribute `scope_all_firms` is exactly the Python `True` (a BOOL; boto3 returns a DynamoDB BOOL as `bool`) and there is NO `allowedFirmIds` attribute: return `(None, None)` (every firm, the documented marker for Opal staff who file for any firm).
3. **(c) not configured.** Anything else with no usable scope: no `allowedFirmIds` and no `scope_all_firms`; an empty `allowedFirmIds` list; a `scope_all_firms` of any type but BOOL `True` (the string `"true"`, the number 1, `False`, `None`): print one line `FIRM-SCOPE-NONE-CONFIGURED` (no address, no row key in it) and return `(None, _resp(403, {"error": "firm scope not configured"}))`.
4. **(d) malformed.** BOTH a list and the marker present, or `allowedFirmIds` present but not a list, or a list with a non-string or empty member: return `(None, _resp(403, {"error": "firm scope malformed"}))` (the existing text; keep its log line style).
5. **Unchanged:** the lookup, the ambiguity, the no-row and the lookup-error refusals, and the status test (`status` exactly `"active"`) keep their code and answers. `_resolve_scope`, `_in_profile_scope` and every caller are NOT edited.
6. **Update the docstring** of `_profile_scope` so it states the new rule (the old text says "no scope: a row with no attribute / an empty list -- today's behaviour").
7. **Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_profile_scope_fail_closed.py` (copy the style of `tests/test_no_row_refuses.py`; a fake users table, no AWS). One named test per case: a non-empty list of firms gives that scope; `scope_all_firms` True with no list gives every firm (an INTERNAL create for any firm passes the scope test); no attribute and no marker is 403 `firm scope not configured` and the log line is printed; an empty list is 403 `firm scope not configured`; `scope_all_firms` of the string `"true"`, of 1, of False and of None each is 403 `firm scope not configured`; a list AND the marker is 403 `firm scope malformed`; a non-list `allowedFirmIds` is 403 `firm scope malformed`; a list with an empty-string member is 403 `firm scope malformed`; a row that is not active is still refused with its existing answer even with the marker; the no-row and lookup-error answers are unchanged.
8. **Re-pin** the existing assertions the new rule changes: `infra/aws/lambda/ticket_center/tests/test_no_row_refuses.py` near line 104 (a row with no list used to mean every firm) and EVERY test double in `infra/aws/lambda/ticket_center/tests/` that returns a PROFILE row without a list and relies on "every firm" (find them by running the whole folder once on your branch: each failure that is a row without a list or marker gets the marker `scope_all_firms: True` in its fixture, nothing else about it changes). List each edit, old line and new line, in your record. If a failure is NOT of that shape, STOP: file a BLOCKING row naming it.
9. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~47/mutant_check.py`** (AC2 below) and a short `R19_L3_RECORD.json`: the lines you changed, the test counts, the before-arm (the new tests on the base: the not-configured and marker-type cases FAIL), every re-pinned fixture, `not_read`.

### ACCEPTANCE

<criterion id="R19L3-AC1" cell_refs="R19-ps-3"><invocation>python -m pytest C:/dev/wk-tckt-vnext-47/infra/aws/lambda/ticket_center/tests/test_profile_scope_fail_closed.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`R19L3-AC1`: the new test file passes with every case of step 7 named in a test, no failures or errors. Also run the whole `infra/aws/lambda/ticket_center/tests/` folder and record the counts in your record, with zero failures after your re-pins (a drain check; the issuer re-runs it).

<criterion id="R19L3-AC2" cell_refs="R19-ps-3"><invocation>python C:/dev/wk-tckt-vnext-47/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~47/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R19L3-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the product tree with the old tail restored (a missing or empty `allowedFirmIds` returns `(None, None)`), runs the new test file against the copy with pytest, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R19L3-AC3J" cell_refs="R19-ps-3" judgment="true"/>
`R19L3-AC3J` (judgment, graded at L9, never by you): a PROFILE row with no list and no marker can no longer file for any firm, the global admission needs the explicit BOOL marker and nothing looser, a row with both is refused, and the other refusals of the function are unchanged.

<expected_criteria>R19L3-AC1 R19L3-AC2 R19L3-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~47/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- **Shared file:** `lambda_function.py` is also edited by `TO-R19-L1` and `TO-R19-L2` (other workers, other slots). Touch ONLY `_profile_scope`, so the three merge cleanly.
- READ only: everything else, including `infra/aws/terraform/`. The data migration that writes the marker is `TO-R19-MIG`'s; you never touch the users table.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md</decomp_doc>
<owned_cells>R19-ps-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~47/TCKT_VNEXT.TO-R19-L3.profile-firm-scope-fails-closed-with-an-explicit-global-marker.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R19-L3`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R19L3-AC1,R19L3-AC2,R19L3-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source in a worker worktree; nothing is deployed, applied or invoked. The release is `TO-R19-REL`, which runs only after `TO-R19-MIG`.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the function reads the users table it already reads.
comp-adversary: RUN -- by reading row S134, ruling ADDENDUM 7 item 3 and the contract against this cell; the lens: an active staff row locked out by the deploy (measured at the cut: 19 internal PROFILE rows are active with no list, which is why the migration runs first), a marker of a looser type (`"true"`, 1) that admits every firm, a row carrying both a list and the marker. BLIND to: the live users rows beyond the count the decomposition records and the deployed function (denominator: 1 ruling item and 1 contract item read).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ADDENDUM 7 (msg 8833) in round 19; fan-out 4 of 5 chains, cap 4 (dell2 CPU budget). The three lambda cells edit disjoint functions of one file; the issuer merges them. State coherence: an unmigrated staff row is LOCKED OUT, never widened; the release order is gated on the migration. Base: `R19L3-AC1` and `R19L3-AC2` FAIL as expected (no test file, no checker file).
