# TO NFRA_CTLPLN.TO-CT-ci-1.estate-report-blob-prefetch -- workstream OUTCOME round 36 (cell CT-ci-1): the estate report runner fetches the blobs of every path it checks out in ONE batched fetch before the checkout

<to_id>NFRA_CTLPLN.TO-CT-ci-1.estate-report-blob-prefetch</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~152</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ci-1` (`decompositions/NFRA_CTLPLN_DECOMP.round30.md`, amendment 10) | **outcome_ref:** FWD-8 (the split's last reader, the deployed one: the daily estate report must run) |
**depends_on:** CT-cg-1 (merged bfbdc20d40)

---

## WORKER FACE

### THE CELL

`infra/aws/ec2/estate-report-runner/estate_report_runner.py` runs on a box with a BLOBLESS, NO-CHECKOUT clone of the repository (`clone_repo`: `git clone --filter=blob:none --no-checkout --branch <REPO_BRANCH>`). It then runs `git -C <repo> checkout <REPO_BRANCH> -- <path>` to materialize the files it needs. MEASURED (the CTO, 2026-10-17 ~13:30Z, read it whole: `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_PARKED_BUS_ITEMS_20261017_1350Z.md` item 1): in such a clone the FIRST `git checkout CLOUD -- <paths>` fails on every blob ("unable to read sha1 file"; rc 255 on a laptop with git 2.55, rc 128 on the runner); the same clone checks out cleanly on a retry, so the lazy per-blob fetch is what fails, not the paths. The daily run of 2026-10-17 FAILED at 13:03:55Z for exactly this reason in `load_function_map` (242 files under `infra/aws/lambda/ci/function-map` plus `lib/opal_lambda_map.py`). The EC2 manifest and the resolver checkouts in `load_attribution_maps`, and the three corpus checkouts in `capture_census`, are exposed to the same lazy-fetch failure; they degrade softly today, which hides it.

THE FIX (MEASURED by the CTO on a fresh blobless clone): list the blob ids with `git -C <repo> ls-tree -r --object-only <REPO_BRANCH> -- <paths>`, then ONE batched `git -C <repo> fetch --no-tags --filter=blob:none origin <id> <id> ...` (245 ids, 6.2 s, rc 0), then the checkout (0.2 s, rc 0, 242 files). The control (the same clone with no prefetch) fails.

BUILD (change the least that does it; keep every other behaviour and log line):
1. Add ONE helper in `estate_report_runner.py`, for example `checkout_paths(repo_dir, paths)`: it runs the `ls-tree` for all `paths`, runs ONE `git fetch --no-tags --filter=blob:none origin <ids...>` when there is at least one id, then runs the `git checkout <REPO_BRANCH> -- <paths>` with `check=True` exactly as before. A failed `ls-tree` or `fetch` logs one `WARN:` line (return code and the last stderr line) and the function STILL runs the checkout, so a site that degraded softly still degrades the same way and `load_function_map` still raises. `ls-tree` prints nothing for a path the tree lacks: that is not an error here, the checkout reports it as before.
2. Route all FIVE checkout sites through it: `capture_census` (its loop over the three `sources`: collect the three paths and prefetch them in ONE call before the loop, keeping the per-source try/except and the `degraded` list as they are), `load_function_map`, and the two entries of `load_attribution_maps`'s `wanted` loop (prefetch both in one call before the loop). After your change the string `"checkout", REPO_BRANCH` appears ONLY inside the helper.
3. A NEW test `.tools/tests/test_round30_estate_prefetch.py` (stdlib; ASCII; temporary folders for every planted case; last line `ESTATE-PREFETCH arms=<k>/<n> ok=<True|False>`). Import the runner the way `.tools/tests/test_round30_follow_readers.py` lines 150-160 do (a `boto3` stand-in when it is absent, the `ESTATE_*` environment variables set before the import). Arms: (a) SEQUENCE: with `subprocess.run` wrapped to record every argv (the wrapper still runs the command), a call of the helper over N paths of a fixture repository records exactly one `ls-tree`, exactly ONE `fetch`, then one `checkout`, in that order, and the fetch argv carries the same ids `git ls-tree -r --object-only` prints for those paths (derive the expected ids with a separate git call in the test, never from the helper); (b) REAL CLONE: build a source repository in a temporary folder with a branch named `CLOUD` holding a folder of at least 30 small files plus one more file, enable `uploadpack.allowFilter` and `uploadpack.allowAnySHA1InWant` on it, make a `--filter=blob:none --no-checkout --branch CLOUD` clone of it by `file://` URL, call the helper, and require every file present with the source's bytes; (c) CONTROL: on a second identical clone run the bare checkout with no prefetch and REPORT whether it fails (it may succeed locally, where the lazy fetch is a local read; print `control_reproduced=<True|False>` and the git version; this arm passes either way, and a False is listed in your report, not hidden); (d) SITES: no line of the runner outside the helper contains `"checkout", REPO_BRANCH`, and `load_function_map`, `load_attribution_maps` and `capture_census` each call the helper; (e) SOFT FAILURE: a helper call on a clone whose `origin` URL is pointed at a missing folder logs a `WARN:` line and still reaches the checkout (the recorded sequence shows `checkout` last), raising nothing before it; (f) MUTANT: a copy of the runner with the `fetch` call removed from the helper makes arm (a) read false (show that arm reading `ok=False`).
4. Run the test and the existing `python .tools/tests/test_round30_follow_readers.py` under `timeout 120` each and report both last lines (the second must stay `ok=True`).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~152/`. THIS IS A WORLD-CLASS CELL BY ITS PATH (the gate infers the class from `infra/aws/ec2/estate-report-runner/`): you run NO `terraform`, NO `aws`, NO deploy, NO upload of the runner, and you do NOT run the estate report runner against the real world; the real clone, the upload and the QA run are the next order's (`TO-APPLY-33`, CloudOps). No network request, no `pip`, no install; the only clones you make are `file://` clones of repositories you build in temporary folders. No push. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12 (the runner host runs Python 3.9: write the helper with no syntax newer than 3.9, and note that `list[dict]`-style annotations are already used in the file); bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after the criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~151/NFRA_CTLPLN.TO-CT-cg-1.lambda-source-map-follow-on-readers.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`); pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W152-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS SPARSE: if a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your report; run `git sparse-checkout add infra/aws/ec2/estate-report-runner lib` first.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTci1-AC1" cell_refs="CT-ci-1"><invocation>python .tools/tests/test_round30_estate_prefetch.py</invocation><expect>ok=True</expect></criterion>
`CTci1-AC1` -- the runner prefetches the blob ids of the paths it checks out in ONE fetch before the checkout, at all five sites; a real file:// blobless clone checks out with the bytes of the source; a failed prefetch still reaches the checkout; a mutant with the fetch removed fails arm (a) (base: the test does not exist, so the invocation fails); report the whole last line with its denominator and the `control_reproduced` value.

<criterion id="CTci1-AC2" cell_refs="CT-ci-1"><invocation>python .tools/tests/test_round30_follow_readers.py</invocation><expect>ok=True</expect></criterion>
`CTci1-AC2` -- the neighbouring test of the cell that last changed this file stays green (base: `FOLLOW-READERS ... ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTci1-AC1,CTci1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~152/NFRA_CTLPLN.TO-CT-ci-1.estate-report-blob-prefetch.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTci1-AC1,CTci1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-ci-1</owned_cells>
</decomp_ref>

<paths>
infra/aws/ec2/estate-report-runner/
.tools/tests/test_round30_estate_prefetch.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the scheduler `estate-report-0900et` is untouched.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call: a code change and a test in temporary folders.
comp-adversary: RUN -- a prefetch that raises where the checkout used to degrade (arm e: a failed prefetch logs and proceeds); a prefetch whose ids are not the ids the checkout needs (arm a derives the expected ids from a separate git call); a fetch per path instead of one (arm a counts fetches); a fifth site left on the bare checkout (arm d); a mutant that drops the fetch passes silently (arm f); the lazy-fetch failure not reproducible on a local clone (arm c reports `control_reproduced`; the real proof of the failure and its fix is the runner host's, in `TO-APPLY-33`); a Python 3.9 incompatibility (the runner host runs 3.9: stated on the face); BLIND: nothing here touches the runner host, GitHub or S3.
risk: WORLD -- the gate infers the class from the `infra/aws/ec2/estate-report-runner/` path; nothing is deployed, uploaded or run against AWS.
lane: the <paths> block IS the grant (worker RULING 1). The CTO's ruling (item 1 of the 2026-10-17 13:50Z rulings) fixed the shape and the criteria; this order is its build leg and `TO-APPLY-33` its apply leg.
</preflight>

Base checks, dry-run by the issuer before the cut: CTci1-AC1 FAIL as expected (the test file does not exist); CTci1-AC2 PASS as expected (control, the existing test).
Source: CTO rulings `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_PARKED_BUS_ITEMS_20261017_1350Z.md` item 1; msg 109820.
