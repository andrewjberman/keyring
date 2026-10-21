# TO IRPT_ANLREQ.TO-AR-y-483.resident-learns-the-ticket-table-from-a-pinned-binding-not-the-environment -- BUILD AND PROVE OFFLINE: the resident reads the ticket table from an OPTIONAL pinned binding `tickets_table` in resident_bindings.json, and no longer from the environment variable IRPT_TICKETS_TABLE; the release builder writes the binding; nothing is planned, applied, built into a release or run

<to_id>IRPT_ANLREQ.TO-AR-y-483.resident-learns-the-ticket-table-from-a-pinned-binding-not-the-environment</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~351</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ142</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-483` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** CTO ruling msg 11692 (binding, not unit environment; "valued from the core root's output, never typed")

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~351`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-351` (branch `wk-IRPT_ANLREQ-351`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~351 <0.9.0_WK_IRPT_ANLREQ~351@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W351-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy, no release build.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the selftest below) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR483-y-AC1,AR483-y-AC2,AR483-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-483`, inlined)

*The defect.* AR-y-469 made `infra/aws/lambda/investor-reporting/reports/resident_installed.py` read the ticket table for the audit ports from `os.environ` (`TICKETS_TABLE_ENV = "IRPT_TICKETS_TABLE"`, line 59; the read at line 639, `tickets_table=os.environ.get(TICKETS_TABLE_ENV)`). That variable is unset on the resident host, so the packager's audit ports are never supplied (an attach records `AUDIT_PORTS_UNWIRED`). The module's own header (lines 8-14, WHAT IS NEVER SYNTHESIZED HERE) says no table name, credential or authority comes from the environment: every table (`jobs_table`, `requests_table`) comes from ONE pinned bindings file. The CTO ruled (msg 11692): `tickets_table` is an OPTIONAL binding, valued from the core root's output, never typed; the environment read is removed.

*The change.* (1) In `infra/aws/lambda/investor-reporting/reports/resident_installed.py`: remove `TICKETS_TABLE_ENV` and the `os.environ.get` read; add `tickets_table` as an OPTIONAL binding next to `OPTIONAL_QUEUES` (absent = the pre-wiring state, as for the two queues): when present it must be a non-empty string that is a valid DynamoDB table name (3-255 chars of `[A-Za-z0-9_.-]`), else `ResidentInstallRefused("TICKETS_TABLE_INVALID")`; pass `bindings.get("tickets_table")` as `tickets_table=` to `make_packager` in `build_resident_runtime`. No other behaviour changes. (2) In `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` (the builder of the bindings file, line 108 onward): add `"tickets_table"` to the `bindings` dict. FIRST find where the table's name is DEFINED in the repository and print it in your report: the table `opal-tickets` is declared in `infra/aws/terraform/ticket-center/main.tf` (resource with `name = "opal-tickets"`, line 48) and named in `infra/aws/terraform/investor-reporting/ycharts/generate.tf` (line 424, `IRPT_TICKETS_TABLE = "opal-tickets"`), and NAMES_SRC (`data/transcripts/scripts/commentary/NAMES.json`) is the file from which the builder already reads `names["ready_queue"]` and `names["commentary_ready_queue"]`. If NAMES.json (or another JSON file the builder already reads or git-shows from the pin) holds the table name, read it from there exactly as the queue names are read. If NO such file holds it, the table name would be a typed literal in the builder (as `jobs_table` is): then STOP BEFORE editing the builder, append a BLOCKING row naming the candidate sources you checked and what each holds, still make change (1) and its tests, and report; the issuer takes the source question to the CTO. (3) Tests: new `infra/aws/lambda/investor-reporting/reports/tests/test_resident_tickets_binding.py` (hermetic; copy the construction style of the neighbouring resident bindings tests, for example `reports/tests/test_resident_r31_packager_bindings.py`): a bindings document with a valid `tickets_table` yields `tickets_table=<that value>` passed to `make_packager` (use a recording stand-in for `make_packager` the way those tests do); a document without it passes `None` (pre-wiring); the values `""`, `"ab"`, `"has space"`, 5 (an int) refuse with `TICKETS_TABLE_INVALID`; setting `IRPT_TICKETS_TABLE` in the environment changes NOTHING (a test that sets it and a document without the binding still passes `None`). Update `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py` only if it depended on the environment variable (read it; it calls `make_packager(..., tickets_table="tickets-table")` directly, so probably not). No test is deleted or skipped.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~351/`: `check_tickets_binding.py` (stdlib only, ruff clean, offline). It requires, by reading the source text at HEAD: `resident_installed.py` contains neither `IRPT_TICKETS_TABLE` nor `TICKETS_TABLE_ENV` nor `os.environ` in or near `tickets_table`; contains `tickets_table` as an optional binding with the refusal text `TICKETS_TABLE_INVALID`; and `bindings.get("tickets_table")` (or the equivalent you wrote) reaches the `make_packager` call. It prints `TICKETS-BINDING-OK env_read=no optional_binding=yes refusal=TICKETS_TABLE_INVALID reaches_make_packager=yes` or `TICKETS-BINDING-BAD <why>` (rc 1). `--selftest` mutates the text in memory three ways (the env read put back; the refusal text removed; the `make_packager` argument replaced by `None`) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the code, builder and test edits as ONE commit first, message citing AR-y-483; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR483-y-AC1" cell_refs="AR-y-483"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~351/check_tickets_binding.py</invocation><expect>^TICKETS-BINDING-OK env_read=no optional_binding=yes refusal=TICKETS_TABLE_INVALID reaches_make_packager=yes$</expect></criterion>
<criterion id="AR483-y-AC2" cell_refs="AR-y-483"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~351/check_tickets_binding.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR483-y-AC3" cell_refs="AR-y-483"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_resident_tickets_binding.py reports/tests/test_resident_r31_packager_bindings.py reports/tests/test_resident_packager_binding.py ycharts/generate/tests/test_audit_live_wiring.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~351/IRPT_ANLREQ.TO-AR-y-483.resident-learns-the-ticket-table-from-a-pinned-binding-not-the-environment.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-483.resident-learns-the-ticket-table-from-a-pinned-binding-not-the-environment`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR483-y-AC1,AR483-y-AC2,AR483-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-483</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write. NOTE: `test_audit_live_wiring.py` leaks `sys.path` at module level (row W350-S1), so keep it LAST in the AC3 list as written; report any other order problem as a row and do not fix files outside the grant.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_tickets_binding.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~351/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-483.resident-learns-the-ticket-table-from-a-pinned-binding-not-the-environment.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two source files and two test files; nothing is planned, applied, deployed, built into a release or run against AWS; the resident release r34q is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading resident_installed.py's header contract, the bindings builder and the CTO's ruling against this cell; the lens: an env read left in place, a typed table-name literal in the builder when a file holds it, a binding accepted without validation, a binding that never reaches make_packager, a test that cannot fail, a test deleted or skipped. NOT seen (blind): the release builder machinery of G2 (r34p_build.py, make_scripts_r34p.py) and whether it calls build_resident_package.py; denominator: three criteria.
</preflight>
