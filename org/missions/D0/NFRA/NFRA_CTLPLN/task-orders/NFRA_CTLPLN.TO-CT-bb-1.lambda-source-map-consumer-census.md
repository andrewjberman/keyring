# TO NFRA_CTLPLN.TO-CT-bb-1.lambda-source-map-consumer-census -- workstream OUTCOME round 27 (cell CT-bb-1): lambda-source-map.json: the consumer census and the per-function layout proposal (stage 1 of the split), and who edited record-terraform-deploy.sh (FWD-7)

<to_id>NFRA_CTLPLN.TO-CT-bb-1.lambda-source-map-consumer-census</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~140</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C in the round-29 issuance, per the CTO's round-28 analysis (ROUND_ANALYSIS.round28.md @3894648aa3, msg 109677).</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-bb-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` (7577 lines) is a JSON map that several boxes edit in place; it is the 8 of 9 project-same-file overlaps of FWD-7 and the same multi-writer shape that causes FWD-8's conflicts. The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round28.md`, ruling 2; read it): split it into one file per function under a folder; any consumer that needs the whole map reads the folder; NO aggregate file is stored. And `infra/aws/lambda/ci/record-terraform-deploy.sh` (923 lines) is code with ONE owner, `0.7.0_AE_CloudOps`: projects do not edit it; if a project's edit carried data, that data moves into the per-function files; "the cell lists each past project edit and where its data now lives".

A `git grep` at the cut finds the string `lambda-source-map` in about 106 files under `infra/` alone (Terraform `locals`, build and deploy scripts, tests, docs). The migration is therefore cut in TWO STAGES by the issuer: THIS cell is stage 1, READ-ONLY on the repository: it measures the map, classifies every consumer, lists every past non-owner edit of the deploy script, and proposes the folder layout and each consumer's migration. The issuer cuts the migration cells from your census (stage 2). You change NO file under `infra/`, no Terraform, no script, and not the map.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **The census script**, a NEW file `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py` (standard library; ASCII output; it only reads; no network). It writes `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/LAMBDA_SOURCE_MAP_CONSUMER_CENSUS.md` and prints a last line `SOURCEMAP-CENSUS files=<n> grep_files=<g> reconciled=<True|False> map_functions=<f> classes=<read_whole:a,read_one:b,write:c,test:d,doc:e,other:o> ok=<True|False>` where `reconciled` is True only when `n` (the files the census classed) equals `g` (the count of files `git grep -l --fixed-strings lambda-source-map` finds over the WHOLE repository, run from the script by `subprocess`), and `ok` is True only when `reconciled` is True and `other` is 0 (every file lands in exactly one class). Scope: the whole repository, not only `infra/` (print the per-top-level-folder counts).
   The classes, by what the file DOES with the map: READ_WHOLE (a program or Terraform expression loads the whole JSON: `jsondecode(file(...))`, `json.load`, `jq` over the whole file, `fromjson`), READ_ONE (looks up one function's entry by key), WRITE (adds, edits or regenerates entries: `record-terraform-deploy.sh`, build scripts, backfill tools), TEST (a test file), DOC (a doc, comment, log or ledger that only names the file). The script classes by line patterns around each match; then YOU read EVERY file the patterns put in READ_WHOLE or WRITE and every file they could not decide, and record your reading in a table `file | class | the line that loads or writes it | what a per-function folder changes for it`. A file the patterns and your reading disagree on is reported, with your reading winning.
2. **The map's own shape** (printed into the census): the top-level keys (how many; which are functions, which are metadata), the key set and one example of a function entry, the min/median/max entry size in bytes, and the count of functions. The census counts the functions two ways (the map's keys and the Terraform functions that name it) and reports any difference.
3. **The deploy script's past edits.** List every commit that changed `infra/aws/lambda/ci/record-terraform-deploy.sh` (`git log --follow --format=...`), its author and committer serial (the commit's `--author` carries the serial), and mark each commit whose author is NOT `0.7.0_AE_CloudOps*` (any suffix). For each non-owner commit read the diff and class it: CODE (logic), or DATA (a function list, a name, a path, a count) and say where that data would live as a per-function file. Print `owner_commits=<a> non_owner_commits=<b> non_owner_data=<c> non_owner_code=<d>` in the census.
4. **The proposal**, a NEW file `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/PROPOSED_LAYOUT_AND_MIGRATION.md` (under 150 lines, written by you): (a) the folder and file names, one file per function, the exact JSON each holds (derived from the map's real entries; show one real one); (b) how a Terraform consumer reads the folder without an aggregate file (`fileset` + `for_each`, or `file()` per function: say which of the consumers in your census need which, and whether any Terraform consumer CANNOT work without an aggregate), and how a script or Python consumer reads it (one small shared reader function: say where it would live); (c) the migration order by consumer class and the risk of each step (which steps change a Terraform plan: say that a plan, not an apply, is the check and that nothing here applies anything); (d) the list of consumers that must change in the SAME commit as the split so that nothing reads a missing file (the atomic set), against those that can follow; (e) what a deploy does while the map is half-split.
5. **The self-test**, `python <script> --selftest`: temporary files only; the line classifier puts a planted `jsondecode(file("x/lambda-source-map.json"))` in READ_WHOLE, a planted `m["fn"]` lookup in READ_ONE, a planted write in WRITE, a planted `test_` path in TEST, and a planted prose mention in DOC; a planted unknown shape reads OTHER and makes `ok` False. Last line `SOURCEMAP-SELFTEST arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/`. You write ONLY inside your own deliverables folder (and a row, if needed); the repository outside it is read-only for this cell. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W140-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTbb1-AC1" cell_refs="CT-bb-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py</invocation><expect>reconciled=True</expect></criterion>
`CTbb1-AC1` -- every file that names the map lands in exactly one class and the count equals the repository's own `git grep` count (base: the script does not exist); report the whole last line with its denominator, the per-class counts and the per-folder counts.

<criterion id="CTbb1-AC2" cell_refs="CT-bb-1"><invocation>python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/source_map_census.py --selftest</invocation><expect>SOURCEMAP-SELFTEST arms=</expect></criterion>
`CTbb1-AC2` -- the classifier puts a planted example of each class in its class and refuses an unknown shape (base: the script does not exist); report the whole last line, which must end `ok=True`.
</proof_of_spec>

<expected_criteria>CTbb1-AC1,CTbb1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280` (the repository-wide `git grep` inside the script is bounded by its own `timeout 200`); record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~140/NFRA_CTLPLN.TO-CT-bb-1.lambda-source-map-consumer-census.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTbb1-AC1,CTbb1-AC2` on the COMMITTED state. NOTE for the reader of your own tree: the worktree is SPARSE, so `git grep` over the whole repository works on the committed tree (not on the sparse working copy): that is what the census wants; read a file's lines with `git show HEAD:<path>` when it is not checked out, and say so in the census.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round29.md</decomp_doc>
<owned_cells>CT-bb-1</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; a read-only census over the committed repository.
comp-adversary: RUN -- the census missing consumers (the count must equal `git grep -l` over the whole repository; the script prints both); a consumer misclassed READ_ONE when it reads the whole map (the worker reads every READ_WHOLE and WRITE file and every undecided one and its reading wins); the worker editing an infra file or the map (forbidden: the repository outside the cell's deliverables folder is read-only, and the cell's only `<paths>` entry is the surprise channel); the proposal hiding an atomic set (item 4d names it); BLIND: a consumer outside this repository (a Lambda that reads the map at runtime from S3, a CI system, another repo such as the portal) is not seen by a repository census; the proposal says so and lists each such candidate it finds named in the repository's docs; also the Terraform plan effect of reading a folder is reasoned here, never run.
risk: LOCAL -- read-only reading of the repository and two files written into the cell's own deliverables folder; no infra, Terraform, script or map change.
lane: the <paths> block IS the grant (worker RULING 1); `deliverables/<serial>/` needs no entry. The CTO ruled the split (round-28 analysis ruling 2, msg 109677); the issuer staged it.
</preflight>

Base checks, dry-run by the issuer before the cut: CTbb1-AC1 FAIL as expected (the script does not exist); CTbb1-AC2 FAIL as expected (the script does not exist).
Source: CTO round-28 analysis ruling 2 and enrichment item 2; FWD-7 report `FWD7_PROJECT_PATH_OVERLAPS.md`; FWD-8.
