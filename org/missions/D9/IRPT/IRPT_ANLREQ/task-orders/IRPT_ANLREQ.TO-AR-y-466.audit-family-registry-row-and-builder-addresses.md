# TO IRPT_ANLREQ.TO-AR-y-466.audit-family-registry-row-and-builder-addresses -- REGISTRY ROW: add the platinum family ANALYSIS_AUDIT to reporting policy irpt-anlreq-x10-v1 and prove the naming builder addresses it for every enabled client firm; no other change

<to_id>IRPT_ANLREQ.TO-AR-y-466.audit-family-registry-row-and-builder-addresses</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~340</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ125</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD | **Decomp cell:** `AR-y-466` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.27) | **depends_on:** CTO msg 11466; the read of AR-y-462

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~340`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-340` (branch `wk-IRPT_ANLREQ-340`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~340 <0.9.0_WK_IRPT_ANLREQ~340@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W340-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR466-y-AC1,AR466-y-AC2,AR466-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-466`, inlined)

*Context.* PRD v0.27 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the row beginning `C-AUDIT-RECORD:`; CTO ruling msg 11466): one audit JSON per analysis request in a NEW PLATINUM family `ANALYSIS_AUDIT` (table `analysis_audit`, extension json, `accepted_ceiling_days` 2555, `unreferenced_days` null) of the reporting policy revision `irpt-anlreq-x10-v1`, written by the packager at attach time (the hop that holds all four linkages), the form as filed taken from the ticket answers, validated against a published schema `AnalysisAudit.v1`. The read that grounds it: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md` (read it first). Every new S3 address is `lib/opal_naming.py` `address()` output (CLAUDE.md rule 30).

*The change.* In `infra/logic/registry/reporting_policies.json`, inside the policy whose `policy_revision` is `irpt-anlreq-x10-v1`, add ONE family after `ANALYSIS_COMMENTARY`: `"ANALYSIS_AUDIT": {"tier": "platinum", "table": "analysis_audit", "extension": "json", "unreferenced_days": null, "accepted_ceiling_days": 2555}` (add the comma the previous line needs; additions only, `git diff --numstat` reads `<n> 0`, one file). Read first: the registry file, `lib/opal_naming.py` (the registry validation that rejects a platinum row with a non-null unreferenced lifetime, near lines 2600-2640; `key()` and `address()` near 2500-2530) and `infra/logic/registry/scopes.json`, `tiers.json`.

*The check.* Write `check_audit_family.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~329/` (stdlib only, ruff clean, offline). It loads `lib/opal_naming.py` BY PATH, runs the registry validation the module itself exposes on the edited registry, reads the enabled client firms (`data/firm_registry.json`, kind client, enabled true) and, for each, calls the builder `address()` with source `irpt`, that firm's scope, tier `platinum`, table `analysis_audit` and a sample partition of the shape the builder accepts (say in a comment where you read the partition grammar); it prints each resolved address (bucket and key) and ONE closing line `AUDIT-FAMILY-OK firms=<n> addresses=<n> validator=pass`, or `AUDIT-FAMILY-BAD <why>` (rc 1). `--selftest` runs the same validation on an in-memory copy where the new row carries `unreferenced_days: 30` and, separately, `tier: state` with `unreferenced_days: null`, and prints `CONTROL-FIRES` only when BOTH read BAD. `check_audit_family_bound.py` compares the registry at HEAD with HEAD~1 (commit the edit FIRST and alone, message citing AR-y-466) and prints `AUDIT-FAMILY-BOUND-OK numstat=<n>/0 files=1` only when deletions are 0 and exactly this one file changed in that commit. Commit order: the registry edit alone, then your deliverables and the instance.

*AMENDMENT 1 (issuer, 2026-10-20 ~18:2xZ, ruling on your BLOCKING row IRPT_ANLREQ-D2-W340-S1 and your S2 to S4).* S1 is the issuer's error and is taken: `lib/opal_naming.py` 2629-2636 refuses a NULL unreferenced lifetime at a non-platinum tier and caps the ceiling at 2555; it does not refuse a platinum row that carries a non-null lifetime, so the first selftest variant of this order could never read BAD. THE SELFTEST NOW READS: `--selftest` runs the same validation on two in-memory copies and prints `CONTROL-FIRES` only when BOTH read BAD: variant A = the new row with `tier: state` and `unreferenced_days: null`; variant B = the new row with `accepted_ceiling_days: 3000`. The new row itself stays as committed (platinum, null lifetime, ceiling 2555). S2 (the row sits before ANALYSIS_COMMENTARY) is accepted: the order of families inside the policy is not part of the contract and the bound stays `<n>/0`. S3 (the folder named ~329 in the cell text) was a numbering slip: ~340 is yours. S4 (the bound check reads the newest registry-touching commit) is accepted. Keep your commits; take this amended order onto your branch first (`git show <trunk commit named in the resume message>:<this order's path>` into that path, committed alone), change only `check_audit_family.py`'s selftest in a new commit, re-run all three criteria, and flip `<status>` to `complete` with the instance only on VALID.

---

## ACCEPTANCE

<criterion id="AR466-y-AC1" cell_refs="AR-y-466"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~340/check_audit_family.py</invocation><expect>^AUDIT-FAMILY-OK firms=[0-9]+ addresses=[0-9]+ validator=pass$</expect></criterion>
<criterion id="AR466-y-AC2" cell_refs="AR-y-466"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~340/check_audit_family.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR466-y-AC3" cell_refs="AR-y-466"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~340/check_audit_family_bound.py</invocation><expect>^AUDIT-FAMILY-BOUND-OK numstat=[0-9]+/0 files=1$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~340/IRPT_ANLREQ.TO-AR-y-466.audit-family-registry-row-and-builder-addresses.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-466.audit-family-registry-row-and-builder-addresses`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR466-y-AC1,AR466-y-AC2,AR466-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-466</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/logic/registry/reporting_policies.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~340/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-466.audit-family-registry-row-and-builder-addresses.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- files named in `<paths>` plus checks in the worker deliverables; nothing is planned, applied, deployed or run against AWS; the release and apply are later orders under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO ruling (msg 11466), the PRD row and the AR-y-462 read against this cell; the lens: a typed bucket or key literal (the addresses come from the builder), a platinum row that the validator would refuse, a second policy revision edited, a deletion, the control that cannot fire. NOT seen (blind): the live buckets and the resident host; denominator: three criteria.
</preflight>
