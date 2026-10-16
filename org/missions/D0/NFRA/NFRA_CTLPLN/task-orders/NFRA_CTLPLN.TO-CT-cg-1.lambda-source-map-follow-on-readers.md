# TO NFRA_CTLPLN.TO-CT-cg-1.lambda-source-map-follow-on-readers -- workstream OUTCOME round 35 (cell CT-cg-1): the follow-on to the atomic source-map split: the seven still-live readers of the retired map read the function folder (graph, rcg, estate report runner, F2's p137 check)

<to_id>NFRA_CTLPLN.TO-CT-cg-1.lambda-source-map-follow-on-readers</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~151</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C by amendment in round 30 (decomposition amendment 8), the 'can follow' cell named in CT-ca-1 and the one reader that landed after its census.</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>35</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cg-1` (`decompositions/NFRA_CTLPLN_DECOMP.round30.md`) | **outcome_ref:** FWD-8 (the multi-writer file conflicts: the split's last readers) |
**depends_on:** CT-ca-1 (merged 48d660b0de)

---

## WORKER FACE

### THE CELL

Cell `CT-ca-1` (merged `48d660b0de`) split the multi-writer `infra/aws/lambda/ci/lambda-source-map.json` into one file per function, `infra/aws/lambda/ci/function-map/<function-name>.json` (240 files, plus `README.md` carrying the old map's metadata), deleted the map, and added the shared reader `lib/opal_lambda_map.py` (`load_entry(name, root=None)` raises when the file is absent; `load_all(root=None)` returns `{name: entry}` sorted by name; stdlib only). The CTO's rulings (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round29.md` rulings 1-3; READ THEM WHOLE) put a list of readers outside that atomic cell: they fail loudly now that the map is gone, which was accepted for one cell and is repaired here, before the first graph rebuild or estate report run reaches them. The census script (`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py`; `--out <path>` writes its markdown to a path you choose, so run it that way and read the table; a bare run writes nothing tracked) names every file that still names the retired path.

THIS IS A WORLD-CLASS CELL (the gate infers the class from the infrastructure path in the grant): you run NO `terraform`, NO `aws`, NO deploy, NO apply, no `build-and-upload.sh`, and you do not run the estate report runner against the real world.

THE SEVEN FILES (read each whole at HEAD before you change it; change the least that makes it read the folder through `lib/opal_lambda_map.py` and keep its behaviour and output shape otherwise):
1. `org/modules/graph/comp_closure.py` and 2. `org/modules/graph/extract_lambda_routes.py` (graph readers: the graph build and the closure tool read the map's function entries).
3. `rcg/bin/lexicon.py` and 4. `rcg/bin/mark.py` (the ratified-terms lexicon and its marker read entries of the map).
5. `infra/aws/ec2/estate-report-runner/estate_report_runner.py` (reads the map to enumerate functions; it runs on a box that has this repository checked out: the folder travels with the checkout; do not add a network or AWS read).
6. `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py` (IRPT_DASHBD round 137's closure check, landed on the target after the atomic cell's census; it reads the map's entry `irpt-49f-reporting-gold-lambda`, the staged members and pins, and compares to a base entry file `sourcemap_entry_r137_base.json` beside it). The same ruling as for `p136_sourcemap.py` and `p170` in `CT-ca-1`: read the entry through `lib/opal_lambda_map.py`, keep its `<id> PASS|FAIL` output shape, its last line and its `--selftest`; where an assertion cannot be kept without the map file, pin it to the map as of its own base commit (a `git show <commit>:<path>` of the retired path, built by parts so the census does not grade it as a live reader) and SAY SO in your report.
7. Any other file the census names as reading or WRITING the retired path that is NOT under `org/missions/`, `org/tier1_exec/`, `org/tier2_senior/`, `org/tier0_exec/`, `docs/` (closed-round deliverables, history and documents stay stale on purpose: they are the accepted loud failures). If the census names such a file outside your paths, file a BLOCKING row naming it and STOP on that file.

For each of the seven: if the file has a `--selftest`, a documented invocation or a test (`org/modules/graph/tests/`, `rcg/tests/`, the estate report runner's folder), run it at the base and after under `timeout 120` and report both last lines; a suite red at the base stays red and is listed, not repaired. A reader that needs a function the map had and `lib/opal_lambda_map.py` does not offer is a BLOCKING row (the issuer widens the reader), never a copy of the map into your file.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero. Your worktree is sparse: run `git sparse-checkout add rcg infra/aws/ec2/estate-report-runner org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks` first (the files above live there) and name any further folder you add with the command and the error.

### BUILD

1. Switch the seven files as above, one commit per file or per pair, committed as soon as each works.
2. **A NEW test** `.tools/tests/test_round30_follow_readers.py` (stdlib; ASCII; temporary folders for any planted case; last line `FOLLOW-READERS arms=<k>/<n> ok=<True|False>`): (a) for each of the files 1-6, no line names the retired path literally (a path built by parts is allowed only in `p137_repin.py` and only for its history pin) and the file imports or loads `opal_lambda_map` or the folder; (b) for each of the files 1-5, ONE behaviour arm against a 5-entry fixture folder built in a temporary directory (the reader's own function, called with the fixture root, returns what the same entries gave before: derive the expected value from the entries, never from the reader); where a reader cannot take a root, test it through the environment or its documented hook, and say so; (c) a planted EMPTY folder and a planted MISSING folder make each of files 1-5 FAIL LOUD (non-zero exit or a raised error naming the folder), never an empty result; (d) `p137_repin.py --selftest` still ends in a pass line; (e) a mutant that restores a read of the retired path in one reader makes arm (a) fail (show it reading ok=False).
3. The census: run it with `--out <scratch path>` and report its last line; the bar is `other:0` and `ok=True`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~151/`. Every experiment runs in a temporary folder; NEVER write the function folder `infra/aws/lambda/ci/function-map/` (read it). NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W151-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge. A WORLD-class order carries no deploy: any command that would reach AWS or a box other than this one is out of bounds and a BLOCKING row if you think you need it. The `portal` gitlink in your worktree may show modified: do not commit it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcg1-AC1" cell_refs="CT-cg-1"><invocation>python .tools/tests/test_round30_follow_readers.py</invocation><expect>ok=True</expect></criterion>
`CTcg1-AC1` -- the six named readers read the function folder (none names the retired path), five of them behave as before on a fixture and fail loud on an empty or missing folder, and p137's selftest still passes (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTcg1-AC2" cell_refs="CT-cg-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~145/atomic_check.py</invocation><expect>census_other=0 live_old_path_users=0 ok=True</expect></criterion>
`CTcg1-AC2` -- the census reads `other=0` and no live reader or writer outside the closed-round set still names the retired path (base: `ATOMIC-SPLIT functions=240 equal=240 map_present=False census_other=1 live_old_path_users=0 ok=False`: the one file is `p137_repin.py`); report the whole last line.

<criterion id="CTcg1-AC3" cell_refs="CT-cg-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py --selftest</invocation><expect>SOURCEMAP-SELFTEST arms=10/10 ok=True</expect></criterion>
`CTcg1-AC3` -- the census instrument itself is unchanged and green (base: `SOURCEMAP-SELFTEST arms=10/10 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTcg1-AC1,CTcg1-AC2,CTcg1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~151/NFRA_CTLPLN.TO-CT-cg-1.lambda-source-map-follow-on-readers.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTcg1-AC1,CTcg1-AC2,CTcg1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cg-1</owned_cells>
</decomp_ref>

<paths>
org/modules/graph/comp_closure.py
org/modules/graph/extract_lambda_routes.py
org/modules/graph/tests/
rcg/bin/lexicon.py
rcg/bin/mark.py
rcg/tests/
infra/aws/ec2/estate-report-runner/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py
.tools/tests/test_round30_follow_readers.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call: reads of the function folder and tests in temporary folders; the estate report runner is not run against the world.
comp-adversary: RUN -- a reader that silently returns empty on a missing or empty folder (arm c: fail loud, the CT-ca-1 rule); a reader that still names the retired path (arm a, mutant arm e); a behaviour change in a graph or lexicon reader (arm b: expected value derived from the fixture entries, not from the reader); a copy of the old map pasted into a file (forbidden; a missing reader function is a BLOCKING row); the F2 closure check weakened silently (history pin named in the report, its selftest kept, its output shape kept); a closed-round deliverable edited (forbidden: they stay stale on purpose); BLIND: the graph rebuild and the estate report runner are unproven against the live estate until their next scheduled run; the first real Lambda deploy after the split is the live proof of the deploy path.
risk: WORLD -- the gate infers the class from the infrastructure path (`infra/aws/ec2/estate-report-runner/`); nothing is deployed, applied, run against AWS or moved.
lane: the <paths> block IS the grant (worker RULING 1). The seven files are read-only consumers of the map `CT-ca-1` retired; the IRPT_DASHBD check file joins on the same ruling as p170, p172 and p136_sourcemap.
</preflight>

Base checks, dry-run by the issuer before the cut: CTcg1-AC1 FAIL as expected (the test does not exist); CTcg1-AC2 FAIL as expected (`census_other=1`); CTcg1-AC3 PASS as expected (control: `SOURCEMAP-SELFTEST arms=10/10 ok=True`).
Source: `CT-ca-1`'s "can follow" list (round-29 ruling 1) and the census read at the merge (`census_other=1`: `p137_repin.py`).
