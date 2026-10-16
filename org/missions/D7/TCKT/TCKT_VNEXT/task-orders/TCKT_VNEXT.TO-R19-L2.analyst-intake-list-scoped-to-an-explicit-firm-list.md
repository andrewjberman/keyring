# TO TCKT_VNEXT.TO-R19-L2 -- BUILD the svc-analyst-intake LIST scope as an explicit firm list from configuration (row S134 item 2; source and tests only)

<to_id>TCKT_VNEXT.TO-R19-L2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~46</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda source path; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R19-ai-2` (`decompositions/TCKT_VNEXT_DECOMP_R19.md`) | **outcome_ref:** row `IRPT_ANLREQ-D2-S134` item 2 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~46`.
- **Worktree:** `C:/dev/wk-tckt-vnext-46` (branch `wk-TCKT_VNEXT-46`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~46 <0.9.0_WK_TCKT_VNEXT~46@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `TCKT_VNEXT-D2-W46-S<k>` (take the next free `<k>`). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before
  its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call of any kind: no AWS, no network, no
  mail, no deploy, no apply, no Terraform (`tests/conftest.py` refuses a real call). **Run NO test file by path (`python <file>`): pytest only, with `-p no:cacheprovider`.** Scratch outside the product tree.

### WHY

Row `IRPT_ANLREQ-D2-S134`: `svc-analyst-intake`'s ticket LIST returns every firm's tickets (CTO ruling ADDENDUM 7, item 2). The contract every cell obeys is
`org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md`, section CONTRACT; its item 2 is this cell's.

### THE CELL (`R19-ai-2`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

In `infra/aws/lambda/ticket_center/lambda_function.py` (read first: the `COMMENTARY_ALLOWED_FIRMS` constant about lines 81-83, which is the pattern to copy; `authorize` and the `MATRIX` about line 188 where `LIST` admits `INTERNAL`, `SVC_ANALYST_INTAKE` and `CLIENT`; `list_tickets` about line 1387, whose item filter `_in_profile_scope(...)` runs at line 1413; `_resolve_scope` about line 429, which scopes only the INTERNAL class):

1. **The config.** A module-level frozenset `ANALYST_INTAKE_ALLOWED_FIRMS`, built from the env var `ANALYST_INTAKE_ALLOWED_FIRMS` (comma-separated firm ids, each stripped, empties dropped, the literal `ALL` dropped as a wildcard) exactly as `COMMENTARY_ALLOWED_FIRMS` is built. Unset or empty means NO firm.
2. **The scope.** In `list_tickets`, when the caller's principal class is `SVC_ANALYST_INTAKE`, keep only the items whose `requester.firm` is in that set (a missing firm is dropped). The filter runs on the fetched items, together with the existing filters; no change to how `limit` is applied. An empty set returns `{"tickets": [], "count": 0, ...}` with 200, never an error and never every firm.
3. **Nothing else changes.** INTERNAL and CLIENT callers' LIST, every other route's behaviour for `svc-analyst-intake`, `_resolve_scope`, and `MATRIX` stay as they are.
4. **Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_analyst_intake_scoped.py` (copy the style of `tests/test_list_scoped_firm.py`; a fake table, no AWS). The module reads its config at import: set the env var and reload the module the way the neighbouring tests do for `COMMENTARY_ALLOWED_FIRMS`. One named test per case:
   - the intake principal lists with the set `49financial,inflection`: only tickets of those two firms come back and a third firm's ticket is absent;
   - the set is unset or empty: zero tickets, status 200;
   - the value `ALL` or `49financial,ALL`: `ALL` admits nothing by itself (only `49financial` does);
   - a ticket with no requester firm is dropped;
   - an INTERNAL caller is unchanged by the set (its own profile scope still decides);
   - the `status`, `assignee` and `ticket_type` filters still work for the intake principal inside the set;
   - the response still carries `cutoff_et` and `count` equal to the length of the list.
5. **Re-pin** the one existing assertion that pins the intake principal as unscoped: `infra/aws/lambda/ticket_center/tests/test_list_scoped_firm.py` near line 240. Change it to the new rule (the intake principal sees only the configured set; give its fixture the set it needs) and list the old and the new lines in your record. No other existing assertion may change; edit another existing test only where a fixture needs the new env var, and list that too.
6. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~46/mutant_check.py`** (AC2 below) and a short `R19_L2_RECORD.json`: the lines you changed, the test counts, the before-arm (the new tests on the base: every case FAILS), the re-pinned lines, `not_read`.

### ACCEPTANCE

<criterion id="R19L2-AC1" cell_refs="R19-ai-2"><invocation>python -m pytest C:/dev/wk-tckt-vnext-46/infra/aws/lambda/ticket_center/tests/test_analyst_intake_scoped.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`R19L2-AC1`: the new test file passes with every case of step 4 named in a test, no failures or errors. Also run the whole `infra/aws/lambda/ticket_center/tests/` folder once and record the counts in your record (a drain check; the issuer re-runs it).

<criterion id="R19L2-AC2" cell_refs="R19-ai-2"><invocation>python C:/dev/wk-tckt-vnext-46/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~46/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R19L2-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the product tree with the intake principal's firm filter removed (every firm returned), runs the new test file against the copy with pytest, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R19L2-AC3J" cell_refs="R19-ai-2" judgment="true"/>
`R19L2-AC3J` (judgment, graded at L9, never by you): `svc-analyst-intake` can list only the tickets of the firms named in its configuration, an unset or empty configuration shows it nothing, `ALL` is never a wildcard, and no other principal's LIST changed.

<expected_criteria>R19L2-AC1 R19L2-AC2 R19L2-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~46/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- **Shared file:** `lambda_function.py` is also edited by `TO-R19-L1` and `TO-R19-L3` (other workers, other slots). Touch ONLY the config constant and `list_tickets`, so the three merge cleanly.
- READ only: everything else, including `infra/aws/terraform/` (the environment value is `TO-R19-TR`'s).

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md</decomp_doc>
<owned_cells>R19-ai-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~46/TCKT_VNEXT.TO-R19-L2.analyst-intake-list-scoped-to-an-explicit-firm-list.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R19-L2`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R19L2-AC1,R19L2-AC2,R19L2-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source in a worker worktree; nothing is deployed, applied or invoked. The release is `TO-R19-REL`.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler reads the table it already reads.
comp-adversary: RUN -- by reading row S134, ruling ADDENDUM 7 item 2 and the contract against this cell; the lens: an intake poller that loses a firm it needs (the three served firms are `49financial`, `inflection`, `cottonwood`, set in `TO-R19-TR`), a wildcard that opens every firm, an INTERNAL caller whose scope changed by accident. BLIND to: the live poller's firm needs and the deployed function (denominator: 1 ruling item and 1 contract item read).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ADDENDUM 7 (msg 8833) in round 19; fan-out 4 of 5 chains, cap 4 (dell2 CPU budget). The three lambda cells edit disjoint functions of one file; the issuer merges them. Base: `R19L2-AC1` and `R19L2-AC2` FAIL as expected (no test file, no checker file).
