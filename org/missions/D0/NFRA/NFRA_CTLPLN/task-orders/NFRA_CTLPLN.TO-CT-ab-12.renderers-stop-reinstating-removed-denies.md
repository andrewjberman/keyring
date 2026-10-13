# TO NFRA_CTLPLN.TO-CT-ab-12 -- workstream DELLADMIN round 2 (cell CT-ab-12): the identity root's renderers stop emitting the Denies CT-ab-1 removed (row W77-S2)

<to_id>NFRA_CTLPLN.TO-CT-ab-12</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~85</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>DELLADMIN</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-12` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`, Recut 1) | **outcome_ref:** FWD-10 |
**depends_on:** none (`CT-ab-1` is merged at your base)

---

## WORKER FACE

### THE CELL

`CT-ab-1` (merged) removed these Denies from the committed policy documents in `infra/aws/terraform/nfra-ctlpln-identity/`: `DenyApiKeyReads`, `DenyCutoverParameterWrites`, `DenyProtectedFunctions` (from `dell_deploy_policy.json`), `DenyIamUsersGroupsKeysAndAccount` (from `dell_iam_roles_policy.json`), `DenyShellDocuments` and `DenyStartSessionOnShellScriptDocument` (from `dell2_ssm_policy.json`); it kept `DenyCloudTrailWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes`, `DenyAuditTrailBucketWrites`, and it removed the HCL-rendered `DenyRoutesToPrivilegedRolesFunctions` policy and attachment from `routes.tf`. Read row `NFRA_CTLPLN-W77-S2` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (search the id with the Grep tool). MEASURED by the builder: under `tests/`, `derive_ssm_documents.py` (about :465-467) still renders the two shell Denies into `dell2_ssm_policy.json`, so its `--write` reverses the ruling and its `--check` reports drift; `derive_respol_actions.py` (about :104 reason c, :35) and `derive_protected_functions.py` (about :39, `DenyProtectedFunctions` add/remove logic) reason from Denies that are gone; `simulate_policy.py` carries about 23 references to them in its decision tables.

### BUILD

1. `tests/derive_ssm_documents.py`: stop emitting the two shell Denies, so `--check` agrees with the committed `dell2_ssm_policy.json` (every Allow byte-identical) and `--write` produces the committed bytes.
2. `tests/derive_protected_functions.py`: it must not add `DenyProtectedFunctions` back; make its `--check` agree with the committed `dell_deploy_policy.json` (if it exists only to maintain that Deny, make its `--write` a refusal that prints why, and keep `--check` meaningful).
3. `tests/derive_respol_actions.py`: its reason-c logic must not cite a removed Deny; make its `--check` agree with the committed `dell_respol_policy.json` (if the data's reasons change, say exactly which rows changed and why; the Allow set must not change).
4. `tests/simulate_policy.py` and `tests/render_routes_policy.py`: do NOT rewrite the decision tables. Add, at the top of each, one comment block naming that the tables still describe the pre-`CT-ab-1` Denies and that `CT-ab-2`'s apply plan, not these tables, is the authority; list in your report how many references remain.
5. Run, and report the last line of each: every renderer's `--check` that exists (`derive_ssm_documents.py`, `derive_protected_functions.py`, `derive_respol_actions.py`, plus any other `derive_*.py` that touches a changed document), `check_admin_parity.py` and `check_identity.py`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. NO terraform command that needs credentials (no init/plan/apply), no aws call, no push; nothing is applied. Do not run a `--write` unless you diff the result against the committed file first and keep it only if the intended change is the only change. `.tools/safe-commit.sh` for every commit, with explicit file paths (never a directory pathspec; a `.terraform/` folder must never be staged). Do NOT commit the `portal` gitlink. ASCII only; Python 3.11+. CLAUDE.md and org/XXX.md are LOCKED. If any gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W85-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab12-AC1" cell_refs="CT-ab-12"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py --check</invocation><expect>ok=True</expect></criterion>
`CTab12-AC1` -- the SSM renderer agrees with the committed document (report the whole last line).

<criterion id="CTab12-AC2" cell_refs="CT-ab-12"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_admin_parity.py</invocation><expect>ok=True</expect></criterion>
`CTab12-AC2` -- the admin-parity check still passes (a control that PASSES at the base).
</proof_of_spec>

<expected_criteria>CTab12-AC1,CTab12-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~85/NFRA_CTLPLN.TO-CT-ab-12.renderers-stop-reinstating-removed-denies.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab12-AC1,CTab12-AC2`, flip `<status>` to `complete` only when both pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so). Report the diff summary per file. If `derive_ssm_documents.py --check` does not print `ok=True` as its last token at the base, report the exact last line you see and adapt the expectation to what the script prints, saying so.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-12</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_respol_actions.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/render_routes_policy.py
infra/aws/terraform/nfra-ctlpln-identity/dell_respol_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell2_ssm_policy.json
org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-ab-12.renderers-stop-reinstating-removed-denies.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE at this cell (no AWS call); the apply cell CT-ab-2 runs it with its denominator.
comp-adversary: RUN -- a --write that reinstates a removed Deny (the --check arm); an Allow changed while the Denies are removed (the diff against the committed bytes); a renderer made to print ok=True without comparing (read the code path); BLIND: another consumer of the removed Sids outside tests/ (the report lists any hit).
risk: WORLD is declared because the L6 gate derives a floor from the infra path; this cell applies nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: row `NFRA_CTLPLN-W77-S2` (disarm owner this seat, the CT-ab-1 apply pair). Recut 1 of the round-12 decomposition.
