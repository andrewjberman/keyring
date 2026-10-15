# TO NFRA_CTLPLN.TO-CT-ai-6 -- workstream OUTCOME round 5 (cell CT-ai-6): the package request, decision and downloads-today records that do not exist yet (FWD-16, FWD-19)

<to_id>NFRA_CTLPLN.TO-CT-ai-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~111</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ai-6` (`decompositions/NFRA_CTLPLN_DECOMP.round19.md`) | **outcome_ref:** FWD-16, FWD-19 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcomes FWD-16 (`prd/NFRA_CTLPLN_PRD.md` line 175: anyone can tell whether a package is approved, ask for one that is not, and later read who said yes or no and why) and FWD-19 (line 214: Andrew can ask what a box downloaded today and get an answer from a record). What exists, found by the issuer's survey: the intake tools in `org/devices/intake/` (`intake_fetch.py`, `intake_check.py`, `intake_receive.py`; read its `README.md`), the repository's generated `requirements.txt`, per-batch CTO approval files such as `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_BATCH_20261008_A.md`, the CRO's `org/tier1_exec/4.0.0_SA_CRO/deliverables/PACKAGE_INTAKE_ASSESSMENT_PYARROW_VERSION_CHANGE_20261007.md`, and each fetch's `*.fetch.json`. What does not exist: a request filing tool, a decision record, a status query that answers from records, and a downloads-today reader.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. A NEW tool `org/devices/intake/intake_request.py` (standard library; ASCII; one file, under 250 lines), with subcommands and a `--root <folder>` (default the intake folder) so tests run in a temporary folder:
   - `file --name N --version V --needed-by "<lane or tool>" --why-no-approved "<why nothing approved will do>" --by <serial>` writes `<root>/requests/REQ-<UTC stamp>-<name>.json`.
   - `decide --id REQ-... --verdict APPROVED|REFUSED --by <serial> --reason "<text>" --evidence <path>` appends the decision to that request's file (who, when, why, on what evidence); a second decision on the same request is refused.
   - `status --name N --version V` prints one line `PACKAGE <name>==<version> <APPROVED|REFUSED|REQUESTED|UNKNOWN> by=<serial|-> at=<UTC|-> reason=<text|->`, answered from the request records and `requirements.txt` (a line there reads APPROVED with `by=requirements.txt`); the answer does not depend on which box or serial asks (a `--device` flag, or `AGENTBUS_DEVICE`, changes nothing in the answer).
   - `show --id REQ-...` prints the request and its decision in plain lines (what, which exact version, what needs it, why nothing approved will do, who decided, when, why), a refusal as clearly as an approval.
   - `downloads --device D --day YYYYMMDD` prints `DOWNLOADS-TODAY device=<D> day=<day> requests=<n> files=<k>` counted from the `*.fetch.json` records under the intake folder whose stamp is that day and whose device is D (read one real `*.fetch.json` first for its fields); zero is printed from the record folder, with `files=<k>` the number of fetch records read, never from a missing folder (a missing folder is `REFUSED`).
2. A NEW test `.tools/tests/test_round19_intake_requests.py` with `--downloads` for the last subcommand. Default arms (temporary folder): one request filed; one approved and one refused (two decisions); `status` for the approved, the refused, a still-requested and an unknown package, asked as two different devices with identical output; `show` for both decisions read back by a second process that did not file or decide; a second decision refused. Last line: `INTAKE-REQUESTS arms=<k>/<n> ok=<True|False>`. With `--downloads`: a fixture folder with two fetch records on the day and one on another day, then the day for the device, and a missing folder; last line `INTAKE-DOWNLOADS arms=<k>/<n> ok=<True|False>`.
3. Do NOT file any real request, make any real decision or write under the real `org/devices/intake/requests/`; the real requests are the CRO's and the CTO's acts, which the issuer drives next round with this tool.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~111/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W111-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTai6-AC1" cell_refs="CT-ai-6"><invocation>python .tools/tests/test_round19_intake_requests.py</invocation><expect>ok=True</expect></criterion>
`CTai6-AC1` -- a request is filed, one approved and one refused, status answers alike for two devices, and both decisions read back (base: the file does not exist); report the whole last line.

<criterion id="CTai6-AC2" cell_refs="CT-ai-6"><invocation>python .tools/tests/test_round19_intake_requests.py --downloads</invocation><expect>ok=True</expect></criterion>
`CTai6-AC2` -- the downloads-today line is counted from fetch records, zero from a record folder, and a missing folder refused (base: the file does not exist); report the whole last line.
</proof_of_spec>

<expected_criteria>CTai6-AC1,CTai6-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~111/NFRA_CTLPLN.TO-CT-ai-6.intake-request-decision-record-and-downloads-today.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTai6-AC1,CTai6-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round19.md</decomp_doc>
<owned_cells>CT-ai-6</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_request.py
.tools/tests/test_round19_intake_requests.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no network; the tool reads local record files.
comp-adversary: RUN -- the tool writing into the real intake folder from a test (every arm uses a temporary `--root`, asserted); a `status` that answers differently by serial; a zero downloads count printed from a missing folder (the missing-folder arm refuses); a decision that overwrites an earlier one; BLIND: no real request or decision is made here (the CRO and CTO make them next round); the Dell-side download count (a Dell box's fetch records) needs that box's seat.
risk: LOCAL -- a new local tool and tests in temporary folders.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is a laptop-side intake folder (NFRA_CTLPLN's own, C-INTAKE); the new file is added, no existing tool edited.
</preflight>

Base checks, dry-run by the issuer before the cut: CTai6-AC1 and CTai6-AC2 FAIL as expected (the files do not exist).
Source: CTO round-18 analysis section 3 (`ledger/ROUND_ANALYSIS.round18.md` @721e05298f), msg 109398; FWD-16, FWD-19.
