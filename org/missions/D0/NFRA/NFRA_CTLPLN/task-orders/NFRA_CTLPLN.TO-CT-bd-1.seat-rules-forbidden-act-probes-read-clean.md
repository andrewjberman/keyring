# TO NFRA_CTLPLN.TO-CT-bd-1.seat-rules-forbidden-act-probes-read-clean -- workstream OUTCOME round 27 (cell CT-bd-1): the seat-rules forbidden-act probes read clean: the Dell-deny row follows Andrew's 10-13 ruling and the slow probe gets its own bound (FWD-25)

<to_id>NFRA_CTLPLN.TO-CT-bd-1.seat-rules-forbidden-act-probes-read-clean</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~142</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-142 @d3e96e0354: validate, suite, proof) and again in the main tree after merge 7ba72f2e61, where the full exercise was re-run: CTbd1-AC1 `SEAT-RULES rules=47 gate=25 skill=11 launcher=11 pairs_covered=24/24 probes_pass=60 probes_pending=0 probes_fail=0 probes_unread=0 needs_andrew=2 ok=True` (base: 56 pass, 1 fail, 1 unread, 58 probes; 79 s on the main tree); CTbd1-AC2 `SEAT-RULES-VALIDATE rules=47 pairs_covered=24/24 problems=0 ok=True` (base problems=1); CTbd1-AC3 `SEAT-RULES-TEST cases=26/26 ok=True` (base 25/26); proof VALID. R-AWSDEVOPS-7 now states what the policy holds after Andrew's 2026-10-13 ruling (three Denies kept: CloudTrail writes, S3 deletes on production data, table and database deletes), as ONE row with three probes (the checker refuses split ids: W142-S1); R-WORKFLOW-19's probe has a 220 s bound (its selftest measured 107 s alone). Per-kind table: deliverables/0.9.0_WK_NFRA_CTLPLN~142/FWD25_FORBIDDEN_ACT_PROBES_BY_KIND.md (CTO 11, COO 5, CVO 7, CRO 5, CLOUDOPS 4, TIER2 5, WORKER 5, MSTR 9, no-serial 9 = 60; every kind has probes). One existing assertion moved with the retired question (the needs_andrew count 3 -> 2: W142-S3). W142-S4: test_crossbox_call.py is red at the base (the anchor `msg_path.write_text(msg_content` is absent from org/mcp/server.py): cell CT-ba-1 repairs it. The three Denies are read from the policy FILE; whether they are applied live is not read. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-bd-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** FWD-25 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-25's forbidden-act half is `python .tools/seat-rules-check.py exercise`: it runs a harmless probe of every GATE rule in `org/ref/SEAT_RULES.json` per seat kind and prints `PASS`, `FAIL`, `UNREAD` or `PENDING` for each. The issuer ran it at the cut (the CTO's round-28 ruling 4): 58 probes, 56 PASS, and the last line reads `SEAT-RULES rules=47 gate=25 skill=11 launcher=11 pairs_covered=24/24 probes_pass=56 probes_pending=0 probes_fail=1 probes_unread=1 needs_andrew=3 ok=False`. The two that are not a PASS:

- `R-AWSDEVOPS-7` FAIL: `POLICY-ABSENT sid=DenyProtectedFunctions`. The row says a Dell seat is refused updates to ten protected Lambda functions by an IAM Deny named `DenyProtectedFunctions` in `infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json`. That Deny was REMOVED on purpose at commit `0a6e65f519` (cell `CT-ab-1`, 2026-10-13) on Andrew's word recorded at `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md` (read it whole): the Dell agent users joined the administrator group and every Deny that reaches them was removed except three. `dell_deploy_policy.json` now holds exactly three Deny statements: `DenyCloudTrailWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes` (and `dell_create_policy.json` keeps `DenyAuditTrailBucketWrites`). The row and its probe describe a state Andrew replaced: the table is stale, not the world. `python .tools/seat-rules-check.py validate` also reads `problems=1 ok=False` for the same row.
- `R-WORKFLOW-19` UNREAD: its probe runs `python .tools/crossbox-call.py --selftest` (40 of 40 cases, `CROSSBOX-SELFTEST cases=40/40 ok=True`) which takes longer than the exercise's 60 s bound on this box (the exercise retried it alone and it timed out again at 60 s); the tool itself is green.

Read first: `org/ref/SEAT_RULES.json` (the two rows; read how a row's `probe` carries a `bound` key), `.tools/seat-rules-check.py` (625 lines: the `exercise`, the `_policy_deny` helper and `validate`), `.tools/tests/test_seat_rules_check.py` (26 cases; it reads `cases=25/26 ok=False` at the base: find which case fails and why), the two policy files above, and the Andrew-direct record.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **`R-AWSDEVOPS-7` follows the ruling.** Replace the row's rule text, `mechanism.entry` and probe so the row states what the policy NOW refuses: updates stay allowed; the three Denies that remain are the refusals (CloudTrail writes, S3 deletes on production data, table and database deletes). Keep the row's shape: one row can carry ONE probe per the table's schema, so if the schema allows one probe per row, split into THREE rows `R-AWSDEVOPS-7a`, `-7b`, `-7c` (one per kept Deny, each probing `_policy_deny` for its own `Sid` and a representative action: read the Deny statements' `Action` lists in the policy file and pick an action each really names) and keep the kinds list (`CLOUDOPS`, `TIER2`), `holder` GATE, `built_by` `existing`. Retire the old question: set `needs_andrew` to `false` on the new rows and quote the Andrew-direct record as the `source`. Do not edit any policy file: the rows follow the files, never the other way round. Say in your report that the old protected-functions refusal is gone by Andrew's ruling, with the commit and the record.
2. **`R-WORKFLOW-19` gets its own bound.** Give that probe a `bound` key large enough for the selftest on this box (read how the table spells a probe's `bound`; measure `python .tools/crossbox-call.py --selftest` once on the loaded box and set the bound to about twice the measured time, at most 280 s) so it reads PASS, not UNREAD. Do not change the tool.
3. **The one red case.** Find why `test_seat_rules_check.py` reads 25/26 at the base. If it is the stale `R-AWSDEVOPS-7` row, the table change cures it. If another cause, repair THAT case to the tool's intended behaviour, change no other existing case, and quote the old and new assertion.
4. **Run and report the whole exercise.** After the change run `python .tools/seat-rules-check.py exercise` (about two minutes) and report every `PROBE` line grouped by seat kind (CTO, COO, CVO, CRO, CLOUDOPS, TIER2, WORKER, MSTR) with PASS/FAIL/UNREAD, as a table in `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~142/FWD25_FORBIDDEN_ACT_PROBES_BY_KIND.md` (written by you from the tool's output, with the tool's whole last line quoted and the count of probe lines per kind printed so no kind is missing: MSTR and WORKER included even if a kind has only `stands_for_all_kinds` probes: say so).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~142/`. Every experiment runs in a temporary folder unless the cell says otherwise; the exercise runs probes the tool itself defines as harmless (it never pushes, commits, merges, applies or sends). NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W142-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTbd1-AC1" cell_refs="CT-bd-1"><invocation>python .tools/seat-rules-check.py exercise</invocation><expect>probes_fail=0 probes_unread=0</expect></criterion>
`CTbd1-AC1` -- every probe reads PASS: none fails and none is unread (base: `probes_pass=56 probes_pending=0 probes_fail=1 probes_unread=1 ... ok=False`); report the whole last line with its denominator.

<criterion id="CTbd1-AC2" cell_refs="CT-bd-1"><invocation>python .tools/seat-rules-check.py validate</invocation><expect>problems=0 ok=True</expect></criterion>
`CTbd1-AC2` -- the table validates against the files it points at (base: `SEAT-RULES-VALIDATE rules=47 pairs_covered=24/24 problems=1 ok=False`); report the whole last line.

<criterion id="CTbd1-AC3" cell_refs="CT-bd-1"><invocation>python .tools/tests/test_seat_rules_check.py</invocation><expect>ok=True</expect></criterion>
`CTbd1-AC3` -- the tool's suite passes (base: `SEAT-RULES-TEST cases=25/26 ok=False`, a red base); report the whole last line.
</proof_of_spec>

<expected_criteria>CTbd1-AC1,CTbd1-AC2,CTbd1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280` (the exercise takes about two minutes: if it hits the bound, run it once more alone and say so); record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~142/NFRA_CTLPLN.TO-CT-bd-1.seat-rules-forbidden-act-probes-read-clean.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTbd1-AC1,CTbd1-AC2,CTbd1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round29.md</decomp_doc>
<owned_cells>CT-bd-1</owned_cells>
</decomp_ref>

<paths>
org/ref/SEAT_RULES.json
.tools/seat-rules-check.py
.tools/tests/test_seat_rules_check.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request: the row's probe reads a policy FILE and does not call AWS.
comp-adversary: RUN -- the row rewritten to pass without matching the files (each new row's `Sid` and action must occur in the policy file the probe reads; validate checks the entry occurs); a probe passing because it is bypassed (the exercise prints the matched text per probe); the worker editing a policy file to make the old row true (forbidden: the rows follow the files, and Andrew's 10-13 ruling removed the Deny); the bound raised so far that a hung probe hides (at most 280 s, and the exercise still kills a probe at its bound); BLIND: whether the three kept Denies are APPLIED live is not read here (the row says it reads the policy file, as the old row did).
risk: LOCAL -- the seat-rules table, its checker and test; no policy, Terraform or AWS change.
lane: the <paths> block IS the grant (worker RULING 1). `org/ref/SEAT_RULES.json` is the table built by cell `CT-s-2` of this project; the change follows Andrew-direct 2026-10-13 ~16:5xZ (record named in the face).
</preflight>

Base checks, dry-run by the issuer before the cut: CTbd1-AC1 FAIL as expected (`probes_fail=1 probes_unread=1`, run 2026-10-16 ~11:5xZ); CTbd1-AC2 FAIL as expected (`problems=1 ok=False`); CTbd1-AC3 FAIL as expected (`SEAT-RULES-TEST cases=25/26 ok=False`).
Source: CTO round-28 analysis ruling 4 and enrichment item 4; the issuer's run of `seat-rules-check.py exercise` at 2026-10-16 ~11:5xZ; FWD-25.
