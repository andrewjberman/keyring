# TO IRPT_ANLREQ.TO-AR-y-485.audit-policy-row-flips-to-active-with-the-applied-audit-policy-commit -- EDIT AND PROVE OFFLINE: flip the registry row irpt-anlreq-audit-x10-v1 from PENDING_ENFORCEMENT to ACTIVE with enforcement_ref = the commit that records the applied audit policy; nothing else in the registry changes; nothing is planned, applied, built into a release or run

<to_id>IRPT_ANLREQ.TO-AR-y-485.audit-policy-row-flips-to-active-with-the-applied-audit-policy-commit</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~353</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ144</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-485` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** CTO ruling msg 11646 (flip to ACTIVE with the commit recording the applied audit policy, before any row is reserved under it, never edit it after) and the applied policy: IB2 receipt `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_auditpolicy/A_AFTER_AUDITPOLICY.txt`, ledger irpt-resident-audit-policy-20261021 CLOSED, IB2 msg 11802

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~353`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-353` (branch `wk-IRPT_ANLREQ-353`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~353 <0.9.0_WK_IRPT_ANLREQ~353@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W353-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy, no release build.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; its controls kind is `script`), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR485-y-AC1,AR485-y-AC2,AR485-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID. The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it).

### THE CELL (`AR-y-485`, inlined)

*What and why.* `infra/logic/registry/reporting_policies.json` holds the row `irpt-anlreq-audit-x10-v1` (family ANALYSIS_AUDIT), registered by AR-y-481 as `state` `PENDING_ENFORCEMENT` with `enforcement_ref` null (CTO msg 11646). The audit managed policy is now applied (IB2, ledger irpt-resident-audit-policy-20261021 CLOSED; the receipt commit is `e3788d3f8a359b0253f45137f8ff3b1cfa075c2d`, on this branch). The CTO's rule: flip the row to ACTIVE with the commit that records the applied audit policy, before any record is reserved under it, and never edit it afterwards. `reports/retention.py` (`_policy`, lines 66-88) requires an ACTIVE row with a 40-hex `enforcement_ref`.

*The change (the only edit).* In `infra/logic/registry/reporting_policies.json`, in the row whose `policy_revision` is `irpt-anlreq-audit-x10-v1` set `"state": "ACTIVE"` and `"enforcement_ref": "e3788d3f8a359b0253f45137f8ff3b1cfa075c2d"`. Keep every other key, every other row and the file's formatting byte for byte (a two-line diff; do not re-serialise the file: edit the two lines). First run `git cat-file -t e3788d3f8a359b0253f45137f8ff3b1cfa075c2d` and `git show --stat e3788d3f8a359b0253f45137f8ff3b1cfa075c2d -- org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_auditpolicy/A_AFTER_AUDITPOLICY.txt` and print both in your report (the commit must exist and must contain that receipt); if either fails, STOP with a BLOCKING row and change nothing.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~353/`: `check_audit_active.py` (stdlib only, ruff clean, offline). It reads the registry at HEAD and at the base commit `382ebe4a5a9a` (use `git show 382ebe4a5a9a:infra/logic/registry/reporting_policies.json`), and requires: every row other than `irpt-anlreq-audit-x10-v1` is dict-equal to the base; the audit row differs from the base in exactly the two keys `state` and `enforcement_ref`; `state` == `ACTIVE`; `enforcement_ref` == `e3788d3f8a359b0253f45137f8ff3b1cfa075c2d` and matches `[0-9a-f]{40}`; `git cat-file -t` of it prints `commit`; and the row's `register_commit` (705dae3202cac873a133825bee9d0381c7dd6b7f) and `ruling_commit` (88ae0673276c9c9b0ce068c0273c6ebf25de5a48) are unchanged. It also loads `lib/opal_naming.py` BY PATH and calls `reporting_policy('irpt-anlreq-audit-x10-v1')` and requires a returned dict with `state` ACTIVE and a 64-hex `policy_sha256` (if that function's name or signature differs, read `lib/opal_naming.py` and use the real one, and say so in your report). It prints `AUDIT-ACTIVE-OK state=ACTIVE enforcement_ref=e3788d3f8a other_rows_unchanged=yes audit_row_keys_changed=2 builder_accepts=yes` or `AUDIT-ACTIVE-BAD <why>` (rc 1). `--selftest` mutates in memory three ways (the audit row ACTIVE with enforcement_ref null; the enforcement_ref cut to 39 hex; another row's `state` changed) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the registry edit as ONE commit first, message citing AR-y-485; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR485-y-AC1" cell_refs="AR-y-485"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~353/check_audit_active.py</invocation><expect>^AUDIT-ACTIVE-OK state=ACTIVE enforcement_ref=e3788d3f8a other_rows_unchanged=yes audit_row_keys_changed=2 builder_accepts=yes$</expect></criterion>
<criterion id="AR485-y-AC2" cell_refs="AR-y-485"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~353/check_audit_active.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR485-y-AC3" cell_refs="AR-y-485"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_generate_installed.py ycharts/generate/tests/test_audit_live_wiring.py reports/tests/test_analysis_audit.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~353/IRPT_ANLREQ.TO-AR-y-485.audit-policy-row-flips-to-active-with-the-applied-audit-policy-commit.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-485.audit-policy-row-flips-to-active-with-the-applied-audit-policy-commit`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR485-y-AC1,AR485-y-AC2,AR485-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-485</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write. Keep `test_audit_live_wiring.py` LAST-but-one as listed in AC3 (it leaks `sys.path`; row W350-S1); report any other order problem as a row and do not fix files outside the grant. The older checkers of AR-y-481 (`check_audit_row.py`, which reads PENDING_ENFORCEMENT) stay as history and are expected to read BAD after this flip; do not edit them.

<paths>
infra/logic/registry/reporting_policies.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~353/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-485.audit-policy-row-flips-to-active-with-the-applied-audit-policy-commit.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one registry row, two keys; nothing is planned, applied, deployed, built into a release or run against AWS; r34q is built by 2.0.0_SA_COO~G2 from this file and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO's rule, the retention module and the applied-policy receipt against this cell; the lens: a file re-serialised so other rows move (their policy_sha256 changes and live retention refuses), an enforcement_ref that is not a real commit or not the receipt's commit, ACTIVE with a null ref, a second key changed, a control that cannot fire. NOT seen (blind): the live retention rows; denominator: three criteria.
</preflight>
