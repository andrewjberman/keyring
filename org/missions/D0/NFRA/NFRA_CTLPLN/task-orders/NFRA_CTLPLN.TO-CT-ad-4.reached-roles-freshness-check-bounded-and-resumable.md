# TO NFRA_CTLPLN.TO-CT-ad-4 -- workstream CENSUS round 1 (cell CT-ad-4): `derive_reached_roles.py --check-fresh` becomes bounded and resumable, so it finishes inside a call's time bound instead of running about eight minutes in one piece (round-13 analysis section 3 ruling 4)

<to_id>NFRA_CTLPLN.TO-CT-ad-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~95</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run: CHECK-FRESH-BOUNDED arms=5/5 ok=True and the offline ROLE-CENSUS line unchanged (175 of 175 roles, ok=True); proof instance VALID on the committed state. Tested only with an injected fake; no AWS call, and the real --check-fresh was not run against the account. Slices run sequentially, so a full check takes longer than the parallel take(); the bound is the point. Rows W95-S1 (the checkpoint file name is covered by no ignore rule, INERT: a stray checkpoint could be staged; a round-15 item with the ignore files) and W95-S2 (Python 3.11 not installed, 3.12.10 used) accepted. The UNREAD-role path in the checkpoint is read from code, no arm exercises it (declared).</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>CENSUS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ad-4` (`decompositions/NFRA_CTLPLN_DECOMP.round14.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py` `check_fresh(saved_path)` (about :368) re-takes the WHOLE census with `take()` (about :251: several hundred read-only AWS calls, about eight minutes), then compares it with the saved file. A caller with a two-minute bound never sees an answer. The CTO ruled: fix the check so it is BOUNDED and RESUMABLE, never just raise a timeout. Read the file's docstring (lines 1-28) and `take()` first.

### BUILD

1. Make the live read of `check_fresh` resumable in slices. Add `--budget <seconds>` (default 90) and `--checkpoint <json>` (default a file next to the saved census named `reached_roles_census.fresh_checkpoint.json`, gitignored if the folder's ignore rules do not already cover it: say what you found). The check reads units of the census (a role, a function region, a task family, a host: whatever unit `take()` already iterates; reuse its loop, do not rewrite its logic) and after each unit appends the unit's result to the checkpoint. When the budget is spent it stops BETWEEN units, saves the checkpoint and prints `CENSUS-FRESH-PARTIAL read=<n> of <total> resume=<the exact command>` and returns exit code 2. A later call with the same checkpoint continues where it stopped. When the last unit is read it compares as today and prints the existing `CENSUS-FRESH ... fresh=<True|False>` line with its existing exit codes (0 fresh, 1 not fresh); a checkpoint that is complete is deleted after that line. A checkpoint taken against a DIFFERENT saved census (compare the saved file's `taken_at` and sha256, stored in the checkpoint) is refused with `ERROR: checkpoint belongs to another census` and exit code 1.
2. Behaviour with NO new flag must stay the same for every other mode (`--live`, `--from-file`, `--refresh-routes`, `--stamp-header`). `--check-fresh` without `--budget` uses the default 90 seconds, which is the change.
3. Update the docstring text for `--check-fresh` (it says "about 8 minutes") to say it runs in slices of `--budget` seconds and resumes.
4. A NEW test `infra/aws/terraform/nfra-ctlpln-identity/tests/test_check_fresh_bounded.py` (standard library; temporary directories only; NO AWS: replace the module's AWS-calling function by an injected fake, and put a stub `aws` first on PATH that fails the arm if it is ever called) with arms: (a) a fake of 12 units and a budget that allows 5 per call: call 1 prints PARTIAL read=5 of 12 and returns 2, call 2 PARTIAL read=10 of 12, call 3 reads the rest and prints `CENSUS-FRESH ... fresh=True` and returns 0, and the checkpoint file is gone; (b) the same with one unit changed in the fake: the final call prints one `VERDICT-CHANGE` line and `fresh=False`, returns 1; (c) a checkpoint from another saved census is refused; (d) a budget of 0 still reads at least ONE unit per call (it never loops forever without progress); (e) the units read across calls equal the units a single uninterrupted pass reads (same set, no unit read twice). Final line `CHECK-FRESH-BOUNDED arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. NO AWS call at all (the injected fake and the PATH stub enforce it), no network, no push. Do NOT run `--live` or `--check-fresh` against the real account. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W95-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTad4-AC1" cell_refs="CT-ad-4"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/test_check_fresh_bounded.py</invocation><expect>ok=True</expect></criterion>
`CTad4-AC1` -- every arm passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTad4-AC2" cell_refs="CT-ad-4"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py --from-file infra/aws/terraform/nfra-ctlpln-identity/tests/reached_roles_census.json</invocation><expect>ok=True</expect></criterion>
`CTad4-AC2` -- the offline re-derivation still prints the same LAST line (base: `ROLE-CENSUS functions=233 tasks=9 hosts=33 roles=175 read=175 unread=0 yes_iam=1 yes_trail=0 yes_delete=9 yes_any=10 no=165 resident_host_role=NO ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTad4-AC1,CTad4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~95/NFRA_CTLPLN.TO-CT-ad-4.reached-roles-freshness-check-bounded-and-resumable.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTad4-AC1,CTad4-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round14.md</decomp_doc>
<owned_cells>CT-ad-4</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py
infra/aws/terraform/nfra-ctlpln-identity/tests/test_check_fresh_bounded.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call in the cell; the real `--check-fresh` read-only run is the applier's, not this worker's.
comp-adversary: RUN -- a partial run reported as fresh (arm a checks the PARTIAL exit code 2 and the absence of a CENSUS-FRESH line until the last slice); a unit read twice or skipped across slices (arm e); a stale checkpoint of another census accepted (arm c); a zero budget that loops without progress (arm d); BLIND: a unit whose read fails midway (the worker says how `take()` records a listing error and whether the checkpoint keeps it as UNREAD rather than dropping it).
lane: the <paths> block IS the grant (worker RULING 1). The tests folder is inside the identity root whose lane lists the CTO and the COO~C; the order's own grant applies, as in round 13's CT-ac-3.
</preflight>

risk: WORLD is declared because the L6 gate derives a floor from the infra path (derive_reached_roles.py); this cell makes no AWS call and applies nothing.

Base checks, dry-run by the issuer before the cut: CTad4-AC1 base: FAIL as expected (the file does not exist); CTad4-AC2 base: PASS as expected (`ROLE-CENSUS functions=233 tasks=9 hosts=33 roles=175 read=175 unread=0 yes_iam=1 yes_trail=0 yes_delete=9 yes_any=10 no=165 resident_host_role=NO ok=True`).
Source: CTO round-13 analysis section 3 ruling 4 (`ledger/ROUND_ANALYSIS.round13.md` @7d271cb57b); the issuer's round-13 close note on `TO-CT-ac-4` (`--check-fresh` did not finish within 200 s).
