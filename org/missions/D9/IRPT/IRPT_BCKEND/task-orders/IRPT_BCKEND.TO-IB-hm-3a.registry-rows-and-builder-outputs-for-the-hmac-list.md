# TO IRPT_BCKEND.TO-IB-hm-3a -- REGISTRY rows and BUILDER outputs for the per-firm HMAC list: the three firm key addresses in the globgrph product folder, the narrow stage role and its policy name, and the secret name (CTO rulings msg 10161, 10203, 10234; rule 30 of CLAUDE.md)

<to_id>IRPT_BCKEND.TO-IB-hm-3a</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~452</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-3` (decomposition section 244) | **outcome_ref:** FWD-21 | **Ordered by:** the CTO's rulings (msg 10161: one builder-named Secrets Manager secret; msg 10203: ONE key per firm in the globgrph folder, `address()` output; msg 10234: B, a narrow role holding `secretsmanager:GetSecretValue` on the one secret and `s3:PutObject` on the three firm keys, trusted by the host's role only) and CLAUDE.md rule 30 (every S3 address is `lib/opal_naming.py address()` output and every resource name is `name()` output; a builder REFUSAL is a missing registry row to add under `infra/logic/registry/`, never a hand-typed workaround).

---

## WORKER FACE

**Cell `IB-hm-3` (inlined).** The next cells (the Terraform for the secret, the narrow role and the host profile grant; the dispatch arguments in `refresh.py`) must carry NAMES and ADDRESSES that come from the repository's naming builders, not from a person's typing. The READ cell found (see the cited lines in `deliverables/0.9.0_WK_IRPT_BCKEND~447/IBhm1_facts.json`, q4): `lib/opal_naming.py` has `address(source, scope, tier, table, partition, object=None)` (line 2515), `key(...)` (2499) and `name(system, scope, function, kind, qualifier=None, fifo=False)` (2700); the system `globgrph` exists (`infra/logic/registry/systems.json:244`) but has no bucket; `scopes.json` has no globgrph product row; `resources.json` has no `irpt` SECRET row and its existing SECRET rows are literal registered names in a slash form (for example `opalinvest/jwt-secret`, graded by `_grade_secret`, `lib/opal_naming.py:2185`). **THE HOME IS RULED (dell2 CTO msg 10259, after the first worker's STOP): a GLOBAL `scopes.json` row for the product `globgrph` whose bucket is the standing shared data bucket `opal-data-assets` (a shared home must name a `standing_shared` bucket in `org/standards/NAMING_SCHEMA.json`; `lib/opal_naming.py` lines 478 to 480 and 516), so `address(...)` emits `s3://opal-data-assets/globgrph/...`. The dedicated bucket `opal-313476888478-globgrph` is NOT used (a standards change or an R20 departure is refused).** The first worker measured that `address('globgrph', 'global', 'gold', ...)` refused for want of a scopes row, that a PRODUCT data bucket must be `opal-data-{long}`, and that `name('irpt', None, 'hmac-list-stage', 'role')` already resolves to `irpt-hmac-list-stage-role` (and `'policy'` to `irpt-hmac-list-stage-policy`) with no row; use those facts, then re-verify them. **Your job: add the registry rows so the builders emit the names and addresses below, and record each builder call and its result.** You do NOT edit `lib/opal_naming.py` or any code: a builder that refuses names a missing row.

**What must resolve (record each as a builder call whose result is the string you will hand to the next cells):**
1. **Three firm keys**, one per firm of `data/firm_registry.json` (`kind` client; the three firms), each an `address(...)` call whose result is an `s3://opal-data-assets/globgrph/...` URI for ONE key under the globgrph product folder of the shared data bucket, in a sub-folder named for what it holds (the account-id list), the firm token appearing only as the key's firm component. Derive the firm tokens from `data/firm_registry.json` in a loop; type none.
2. **The narrow stage role's name**, a `name(...)` call (kind IAM role) for the function `hmac-list-stage` in the irpt system, and **its inline policy's name**, a second `name(...)` call (or the repository's policy-name builder if one exists; say which).
3. **The one secret's name**: a registered SECRET row in `infra/logic/registry/resources.json` in the slash grammar `{system}/{scope}/{purpose}` that `_grade_secret` accepts (system `irpt`; read `org/standards/NAMING_SCHEMA.json:123` and the grading function first), with an `evidence` field that cites the CTO message numbers above.

**Do, in this order:**
1. Read `lib/opal_naming.py` lines 2185 to 2230, 2499 to 2560 and 2700 to 2760, the registry files `scopes.json`, `systems.json`, `resources.json`, `tiers.json`, `root_map.json` around the existing irpt and globgrph rows, `org/standards/NAMING_SCHEMA.json` near line 123, and one existing test in `lib/tests/test_opal_naming*.py` for the style of a "builder emits X" test.
2. Add the minimum registry rows. Run the builder calls; if one REFUSES, the message names the row you are missing: add it (rule 30). Do not widen any existing row's meaning.
3. Write the record `deliverables/0.9.0_WK_IRPT_BCKEND~452/IBhm3a_resolved.json`:
`{"calls":[{"label":"<what it is>","fn":"address|name|key","args":[...],"kwargs":{...},"result":"<the string returned>"}, ... ],"secret":{"name":"<slash name>","registry_file":"infra/logic/registry/resources.json"},"rows_added":["<file>: <row name>", ...],"firms":["<token>", "<token>", "<token>"],"notes":"<text>"}`. The `calls` hold the three firm key addresses, the role name and the policy name (5 calls in all). **No account id, no secret value, no key material anywhere.**
4. Run `python -m pytest lib/tests -q -k naming` and record the pass count at base (before your edit) and after: no test that passed at base may fail. Add NO new test unless a builder-emits test is the repository's norm for a new row (then one test file, under `lib/tests/`).
5. Run the three criteria below from the repository root, record each output and exit code verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~452/IBhm3a_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~452 <0.9.0_WK_IRPT_BCKEND~452@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): the registry files you changed, any test file, and your deliverables folder, plus any surprise row and the order's `<status>` flip. Report once, under 150 words. Run AC2 and AC3 only AFTER the commit (they read `HEAD~1..HEAD`).

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBHM3A-AC1" cell_refs="IB-hm-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r249/p249_cells.py" . IBHM3A-AC1</invocation><expect>IBHM3A-AC1 PASS</expect></criterion>
<criterion id="IBHM3A-AC2" cell_refs="IB-hm-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r249/p249_cells.py" . IBHM3A-AC2</invocation><expect>IBHM3A-AC2 PASS</expect></criterion>
<criterion id="IBHM3A-AC3" cell_refs="IB-hm-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r249/p249_cells.py" . IBHM3A-AC3</invocation><expect>IBHM3A-AC3 PASS</expect></criterion>

<expected_criteria>IBHM3A-AC1, IBHM3A-AC2, IBHM3A-AC3</expected_criteria>

What the checks grade: AC1 the check RE-RUNS every recorded builder call against your worktree and requires each to return exactly the recorded result with no refusal, with three address results under `s3://opal-data-assets/globgrph/` and one per firm; AC2 the naming tests pass and your ONE commit (`HEAD~1..HEAD`) touches only registry files, an optional naming test, and this order's paths; AC3 the secret row is in `resources.json` as a SECRET of system irpt in slash grammar, the role and policy names are irpt names, and the record holds no key material. Do not edit the checks.

## BOUNDS

- **Grant:** edit files under `infra/logic/registry/` (rows only); add at most one test file under `lib/tests/`; write `deliverables/0.9.0_WK_IRPT_BCKEND~452/`; the surprise channel for rows. **NO edit of `lib/opal_naming.py` or any code; NO Terraform; NO AWS call; NO secret value or key material; NO push; NO change to any existing registry row's meaning.**
- **Refusal clause:** STOP and report, writing nothing further, if a builder will not emit a name or address even with a new row (name what it refuses and why), or if adding a row needs a change to code. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
infra/logic/registry/
lib/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~452/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-3a.registry-rows-and-builder-outputs-for-the-hmac-list.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 244 (round 8, workstream ~PM), cell `IB-hm-3`.
<owned_cells>IB-hm-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM3A-AC1, IBHM3A-AC2, IBHM3A-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~452/IRPT_BCKEND.TO-IB-hm-3a.registry-rows-and-builder-outputs-for-the-hmac-list.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: registry JSON rows in a worktree; nothing is deployed and no AWS call is made; the rows only let the builders name things the next cells create.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed (the role is only NAMED here).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p249_cells.py IBHM3A dry-run at base on dell2 2026-10-17 ~04:0xZ: AC1, AC2, AC3 FAIL. Positive control (control249.py) over synthetic git repos with a stub naming module: the three positives PASS and each negative (a recorded result that differs from the re-run, a call that refuses, an address outside the globgrph bucket, fewer or more than three firm addresses, a firm address that is not per firm, a second file touched, the naming tests failing, a secret row of the wrong type or system or grammar, an irpt role name missing, key material in the record) fails its own arm. NOT measured by me: whether the real builders accept the worker's rows (the check re-runs them), the secret grammar the grader accepts, anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~452`. Class WORLD (the gate's floor for a path under infra/; the act itself is registry JSON rows in a worktree and the check re-runs the builders).
</preflight>
