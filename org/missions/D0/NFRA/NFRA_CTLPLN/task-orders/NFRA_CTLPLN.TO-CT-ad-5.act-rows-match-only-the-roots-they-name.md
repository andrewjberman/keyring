# TO NFRA_CTLPLN.TO-CT-ad-5 -- workstream CROSSBOX round 1 (cell CT-ad-5): in `crossbox-deploy-check.py` an open-calls row of `kind` `act` matches only the roots its own `roots` field names, and a row with no roots matches none (row D2-S3, CTO round-13 ADDENDUM 1)

<to_id>NFRA_CTLPLN.TO-CT-ad-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~96</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run: OPEN-CALL-ACT-ROOTS arms=8/8 ok=True (the worker's control: 2/8 at the base) and APPLY-GATES-TEST cases=100/100 ok=True; proof instance VALID on the committed state. Accepted: files mode treats a roots-named act row through roots_field_hit while a fork row skips it there (the cell's wording, literal). The real f61b read against irpt-status is the issuer's, after the merge.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>CROSSBOX</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ad-5` (`decompositions/NFRA_CTLPLN_DECOMP.round14.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-D2-S3` (Grep `"id": "NFRA_CTLPLN-D2-S3"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). `.tools/crossbox-deploy-check.py` `measure_open_call(...)` (about :189-253) scans every live open-calls row. For each row it takes a hit when the row's own `roots` field names the root (`roots_field_hit`), or the row's `project` field is one of the covering projects (`project_field_hit`), or the root's name appears as text in the row (`mentions`). A row of `kind` `act` is an act ONLY Andrew can do (for example "send the execution ID of your own PROD submission"): it is not a decision about a deploy. Yet one such row, dell2 `f61b` with project `IRPT_BCKEND` and no `roots` field, draws a hit on every root of that project's write set, so under ENFORCE it would STOP applies (`irpt-status`, `opal-ticket-api`) that do not depend on the act. The CTO ruled the rule: a row with `kind` `act` matches ONLY the roots its own `roots` field names; a row with `kind` `act` and no roots matches none. Today the OPEN-CALL limb prints WARN; arming ENFORCE before this lands is refused.

### BUILD

1. In `.tools/crossbox-deploy-check.py` `measure_open_call`, in the loop over open-calls rows (about :240-248), when the row's `kind` equals `act` (compare case-insensitively on the stripped value; a row with no `kind`, or `fork`, is untouched): its hit reason is `roots_field_hit(row, rel)` ONLY, in both the Terraform and the narrow (files-mode, non-Terraform) cases; skip `project_field_hit` and `mentions` for it. The line for such a hit still names the row id and says `act row names the root in its roots field (<entry>)`. An act row that is skipped for having no matching roots prints nothing new but is still counted in `calls_scanned`. Crossbox call FILES (the first loop) and `fork` rows are untouched.
2. Update the module docstring (the OPEN-CALL paragraph about :13-16) with one sentence stating the act-row rule.
3. A NEW test `.tools/tests/test_open_call_act_roots.py` (standard library; temporary directories only; builds a temporary repo root holding `org/devices/state/<box>/open_calls.json` fixtures; calls `measure_open_call` by importing the module from its path, or runs the tool with `--repo-root` if it has that option; read the module to decide) with arms: (a) an OPEN `act` row with project `IRPT_BCKEND`, no `roots`, against the root `infra/aws/terraform/irpt-status` -> `matched=0`; (b) the same row with `roots` naming `infra/aws/terraform/irpt-status` -> `matched=1` and the hit line names the row; (c) the same row with `roots` naming ANOTHER root -> `matched=0` against `irpt-status`; (d) an OPEN `fork` row with the same project and no roots against the same root -> `matched=1` (unchanged); (e) an `act` row whose subject text names `irpt-status` but whose `roots` is empty -> `matched=0`; (f) a CLOSED `act` row naming the root -> `matched=0` (closed rows stay ignored); (g) the narrow files-mode case: an `act` row with no roots against a non-Terraform root with carried files -> `matched=0`. Final line `OPEN-CALL-ACT-ROOTS arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no network, no push, no change to any real open-calls file (the test reads fixtures only). `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W96-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTad5-AC1" cell_refs="CT-ad-5"><invocation>python .tools/tests/test_open_call_act_roots.py</invocation><expect>ok=True</expect></criterion>
`CTad5-AC1` -- every arm passes, the unchanged `fork` arm and the closed-row arm included (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTad5-AC2" cell_refs="CT-ad-5"><invocation>python .tools/tests/test_apply_who_and_crossbox.py</invocation><expect>ok=True</expect></criterion>
`CTad5-AC2` -- the existing apply-gates suite still passes (base: `cases=100/100 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTad5-AC1,CTad5-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~96/NFRA_CTLPLN.TO-CT-ad-5.act-rows-match-only-the-roots-they-name.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTad5-AC1,CTad5-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round14.md</decomp_doc>
<owned_cells>CT-ad-5</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-deploy-check.py
.tools/tests/test_open_call_act_roots.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- an act row dropped from `calls_scanned` (the denominator must still count it); a `fork` row narrowed by mistake (arm d); a closed row revived (arm f); a decision row mislabelled `act` hiding a real upset (the worker lists in its report which `kind` values the open-calls tool can write, from `open-calls.py add --help`); BLIND: a row whose `kind` carries a different case or whitespace (the comparison is case-insensitive on the stripped value, and the worker adds an arm for `" Act "`).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base checks, dry-run by the issuer before the cut: CTad5-AC1 base: FAIL as expected (the file does not exist); CTad5-AC2 base: see the issuer's dry-run note in the issuance commit. The issuer reads the real `f61b` row against `irpt-status` after the merge (the criterion of the CTO's ADDENDUM 1: `matched=0`, and a root the row names still matches).
Source: CTO round-13 ADDENDUM 1 @ad8da57abc (`ledger/ROUND_ANALYSIS.round13.md`), row NFRA_CTLPLN-D2-S3 (from 1.0.0_SA_CTO~DELL2).
