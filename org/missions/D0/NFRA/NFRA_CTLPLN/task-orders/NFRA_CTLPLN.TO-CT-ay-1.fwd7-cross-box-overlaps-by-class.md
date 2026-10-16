# TO NFRA_CTLPLN.TO-CT-ay-1 -- workstream OUTCOME round 25 (cell CT-ay-1): FWD-7 -- classify the cross-box write overlaps into shared carriers and project paths and report the project paths alone

<to_id>NFRA_CTLPLN.TO-CT-ay-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~137</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-137 @efb0a434cd) and again in the main tree after merge 7dbffb535f: CTay1-AC1 FWD7-CLASSES total=64 carrier=40 not_same_file=15 project_same_file=9 unclassified=0 findings_line=64 ok=True (the tool's own FINDINGS count agrees); CTay1-AC2 FWD7-SELFTEST arms=9/9 ok=True; proof VALID. The 9 project-same-file lines name two shared infra files, infra/aws/lambda/ci/lambda-source-map.json (8 lines) and infra/aws/lambda/ci/record-terraform-deploy.sh (1): NON-ZERO, so per the CTO's ruling 4 it goes to him to decide whether it becomes a cell. Worker count in its tree was 62 (a sparse tree; row W137-S1: org/missions absent made placement-check under-report silently; the main-tree read is 64); W137-S2 INERT; W137-S3 (13 vs 15 directory claims classed NOT-SAME-FILE: the reused prefix rule never lets the directory-claim clause fire) is the CTO's. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ay-1` (`decompositions/NFRA_CTLPLN_DECOMP.round28.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD FWD-7 (`org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` line 87) has ACCEPT "two on different boxes change different files". `python .tools/placement-check.py` (read-only) prints one `OVERLAP <project A> (<box>) and <project B> (<box>): <path A> ~ <path B>` line per pair of projects on different boxes whose declared write surfaces overlap; at the cut it reads 64 (`FINDINGS: 0 unplaced/unreadable, 64 cross-box write overlap(s)`). The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round27.md`, ruling 4; read it) that the ACCEPT clause is read over PROJECT write surfaces: shared append-only carriers (deploy-ledger sentinels, audit logs, surprise channels, the open-calls lists) are excluded, because every box writes them by design and box-sync resolves them. This cell classifies the lines and reports the project-path overlaps alone. It changes no tool and no register.

An earlier cell classified an earlier read (56-57 lines) by rules R1-R5; its table is `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~106/FWD7_OVERLAP_CLASSES.md` (read its class legend: SHARED = a rule file, SPLIT, and NOT-SAME-FILE = one path is a strict directory-prefix parent of the other and the two are different files, decided by the path-prefix relation). Reuse its NOT-SAME-FILE relation; do not reuse its SHARED rule.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. `placement-check.py` reads every live project row and `org/devices/DEVICES.json`: if a command fails because a file or folder is missing, run `git sparse-checkout add <folder>` (likely `org/projects` and `org/missions`), retry, and name the folder, the command and the error in your final report. Run the read from the worktree root.

### BUILD

1. **The classifier**, a NEW script `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~137/fwd7_classify.py` (standard library; ASCII output; no network; it only reads). It runs `python .tools/placement-check.py` as a subprocess under `timeout 200` (never imports it), parses every `OVERLAP` line, and classes each line by exactly these rules, first match wins:
   - **CARRIER** when BOTH paths of the pair lie in the same shared append-only carrier: the path is under `org/critical_paths/.open_deploys` (deploy-ledger sentinels), or its file name matches `*audit*.log` / is under a folder named `audit`, or it lies under a `surprise-channel/` folder, or it matches `org/devices/state/*/open_calls.json`, or `org/devices/crossbox`. Print which of the five carrier kinds matched;
   - **NOT-SAME-FILE** when one path is a strict directory-prefix parent of the other (the relation of the earlier table's R5) and the two differ: the two projects change different files;
   - **PROJECT-SAME-FILE** when the two paths are the same file, or one is a directory claim over the other's directory and neither rule above fired;
   - **UNCLASSIFIED** when a line cannot be parsed. The script exits 2 if there is any.
   The last line: `FWD7-CLASSES total=<n> carrier=<c> not_same_file=<d> project_same_file=<p> unclassified=<u> findings_line=<the N from placement-check's own FINDINGS line> ok=<True|False>`; `ok` is True only when `total` equals the tool's own FINDINGS count, the four classes sum to `total` and `unclassified` is 0.
2. **The report**, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~137/FWD7_PROJECT_PATH_OVERLAPS.md`, produced by the script (write it from the script, not by hand): the denominator line, the class counts, then ONE table of every PROJECT-SAME-FILE line (project A and box, project B and box, the two paths, the shared file), then one table of the NOT-SAME-FILE lines, and the carrier counts by kind (counts only). If PROJECT-SAME-FILE is 0 the report says so in one sentence at the top; if it is non-zero the report names, per shared file, which projects touch it and does NOT propose a fix (the CTO decides whether each becomes a cell).
3. **The self-test**, `python <script> --selftest`: temporary synthetic `OVERLAP` lines fed to the classifier's own function (no subprocess): a sentinel pair is CARRIER; an `open_calls.json` pair is CARRIER; a `surprise-channel` pair is CARRIER; a directory-prefix parent of a different file is NOT-SAME-FILE; two projects naming the same ordinary source file are PROJECT-SAME-FILE; a malformed line is UNCLASSIFIED and the run's `ok` is then False. Last line `FWD7-SELFTEST arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~137/` plus the `<paths>`. NO network request, no `pip`, no install, no change to `.tools/placement-check.py`, the register, the project rows or any tool. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7. CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. Pin every artifact row of your proof instance to the commit that carried it. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W137-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTay1-AC1" cell_refs="CT-ay-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~137/fwd7_classify.py</invocation><expect>ok=True</expect></criterion>
`CTay1-AC1` -- every cross-box overlap line the placement read prints is placed in exactly one class and the total equals the tool's own FINDINGS count (base: the script does not exist); report the whole last line and the report's top sentence.

<criterion id="CTay1-AC2" cell_refs="CT-ay-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~137/fwd7_classify.py --selftest</invocation><expect>FWD7-SELFTEST arms=</expect></criterion>
`CTay1-AC2` -- the classifier puts a carrier pair, a different-files pair, a same-file project pair and a malformed line each in its class (base: the script does not exist); report the whole last line, which must end `ok=True`.
</proof_of_spec>

<expected_criteria>CTay1-AC1,CTay1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~137/NFRA_CTLPLN.TO-CT-ay-1.fwd7-cross-box-overlaps-by-class.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTay1-AC1,CTay1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round28.md</decomp_doc>
<owned_cells>CT-ay-1</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; one read of the placement tool's output.
comp-adversary: RUN -- the classifier excusing a real overlap as a carrier (the carrier rule needs BOTH paths inside one of five named kinds; the self-test plants a project file beside a carrier); a line dropped silently (the four classes must sum to the tool's own FINDINGS count, a mismatch is `ok=False`); a hand-written report (the script writes it); the worker proposing a fix (forbidden: the CTO decides whether a non-zero count becomes a cell); BLIND: the placement tool reads declared write surfaces, not what each box really writes, so a zero here says the declarations do not collide, not that no two boxes touched one file.
risk: LOCAL -- a read-only script and a report inside the cell's own deliverables folder; no tool, register or project row changes.
lane: the <paths> block IS the grant (worker RULING 1); `deliverables/<serial>/` needs no entry. The CTO ruled the reading (round-27 analysis ruling 4, msg 109661).
</preflight>

Base checks, dry-run by the issuer before the cut: CTay1-AC1 FAIL as expected (the script does not exist); CTay1-AC2 FAIL as expected (the script does not exist).
Source: CTO round-27 analysis ruling 4 and enrichment item 3; FWD-7.
