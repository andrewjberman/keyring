# TO NFRA_CTLPLN.TO-CT-ak-3 -- workstream OUTCOME round 10 (cell CT-ak-3): one signed change deploys exactly one script, in a real push, through the CloudOps seat (FWD-5, positive arm)

<to_id>NFRA_CTLPLN.TO-CT-ak-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.7.0_AE_CloudOps~CT2</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C. Seat 0.7.0_AE_CloudOps~CT2 opened the NEVER-2 entry ctlpln-r21-fwd5-one-script-20261015 (17:55Z), and closed it at 18:07Z with all 3 legs proven (commit 35ac3c0dd0; proof instance VALID, committed 4781da8f97). Issuer's own re-read at 18:08Z: s3://opal-data-bd/code/gold/diag_sleeve_fix.py holds 2 versions (new VersionId ceImQVXASssU3IUCRXRjMkoA1XnifTf7, written 18:02:18Z) and its ETag equals the committed script md5 c204fd9be3bbfc43346a14b4c71051af (etag_equals_repo_md5=True); org/safe-deploy-bypass-audit.log shows exactly one PINNED-DEPLOY row for the path at 18:01:57Z (slug ctlpln-r21-fwd5-one-script-20261015, pin 971327859b33) and two HELD-DEPLOY rows (17:51:27Z, 17:53:05Z, reason no-open-ledger-names-it) before the entry opened. The CloudOps seat reports 0 of 190 other code/gold keys changed since the entry opened (the issuer's own count was denied by the comp rail and is not made). THE ACTOR CLAIM OF STEP 5 IS NOT MET AND IS THE ISSUER'S ERROR (row S9132, BLOCKING, ruled): the shared-branch push gate (LD-0367/0368) lets only 0.0.0_AB_MSTR push box/laptop, so the deploy was the scheduled box-sync push of 0.0.0_AB_MSTR, via the D1-S8 pinned-entry path (the script had reached CLOUD by integrate before that push, which is the D1-S8 scenario, exercised for real). The three written criteria (versions=2, other_changed=0, etag_equals_repo_md5=True) hold; the post-close re-run of the read test prints other_changed=-1 because the sentinel it reads for the open time is gone after close (carried to a round-22 cell).</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ak-3` (`decompositions/NFRA_CTLPLN_DECOMP.round21.md`) | **outcome_ref:** FWD-5 |
**depends_on:** `CT-ak-4` merged (it commits the one-line signed change and the read test, which the lane registry admits only to a worker serial; see AMENDMENT 1 below). The gate fix `D1-S8` merged at `c13fc91edb`; the round-19 negative arm is the control.

---

## WORKER FACE

### THE CELL

PRD outcome FWD-5 (`org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` line 67): pushing from any box never puts anything into production except what a signed change names for that exact build. The negative arm (an unsigned script deploys nothing, held and written down) was read in round 19 (`.tools/tests/test_round19_unsigned_push.py`). THIS CELL is the positive arm, and it is a real production write: ONE signed change that names ONE script deploys exactly that script, in a real push from `box/laptop`, and nothing else. You are the CloudOps seat that applies it; a deploy is the act being proved, so you open and close your own NEVER-2 ledger entry.

READ FIRST, whole: the research for this exact operation, `org/tier1_exec/4.0.0_SA_CRO/deliverables/NFRA_CTLPLN_R21_FWD5_ONE_SIGNED_CHANGE_ONE_SCRIPT_RESEARCH_20261015.md` (script choice, blast radius of one S3 key, the rollback VersionId, the hook path read line by line, the box-sync timing hazard, the proposed shape below). Then `.tools/git-hooks/pre-push-safe-deploy.sh` (the pinned-entry step is lines about 50-142, the box-push path about 144-230), `.tools/deploy_ledger.py --help`, and `org/critical_paths/.open_deploys/bd-gold-etf-classifier-cash-type-20261014.json` for the sentinel shape.

AMENDMENT 1 (issuer, 2026-10-15 ~17:0xZ, after row S9130 and the STOP at step 3): the registry lanes admit only a `0.9.0_WK_NFRA_CTLPLN~<n>` worker serial to the script (lane POD4) and to the read test (lane TOOL_BATTERIES), so the commits of steps 3 and 7 are made by worker cell `CT-ak-4` and merged into `box/laptop` BEFORE you start. This order is re-pointed from `0.7.0_AE_CloudOps~U7` (which also holds an unrelated IRPT_ANLREQ order) to the lane `0.7.0_AE_CloudOps~CT2`, and its `<paths>` are cut to the files a CloudOps seat is admitted to. No override is used. Row id form: `NFRA_CTLPLN-S<next free number>` (the row gate refuses `U7-S<k>` and `CT2-S<k>`). Your steps 3 and 7 below read: VERIFY the commit and the test are in `box/laptop`.

THE SCRIPT: `data/black_diamond/scripts/gold/diag_sleeve_fix.py` (first choice; fallback `validate_sl_nightly_gate.py` if the first no longer matches S3 byte for byte). A hand diagnostic that no schedule runs and nothing imports; its S3 object `s3://opal-data-bd/code/gold/diag_sleeve_fix.py` equals the repository byte for byte today (1 version, VersionId `3.yZFEuxxfxUOEMd.NRY7bZucaDccGX.`, ETag `56cb170f95c0b112a36a0ee3973d5473`; re-read both at the start, they are the rollback record). Blast radius: one S3 key and, at the runner's next 04:00Z sync, one more file on the gold runner's disk; nothing executes it. A never-widen pair is NOT owed (no served data output moves; CLAUDE.md NEVER-1, DELTA=0).

### BUILD (the steps, in this order; each step reads its own result before the next)

1. **Step one (W113-S1, read only):** compare the hook's bucket and key mapping with `safe_deploy_core.py` (`CODE_TREES` and `PIPELINE_MAP`, line about 68 and 576; that file is IRPT_BCKEND's, READ it, never edit it): for `black_diamond`, `inf`, `cot` the hook's bucket and `code/<layer>/<name>` key equal the core's; `mdpf` is gated in the core and absent from the hook's map (the hook then HOLDS it, safe). Print the comparison as a table in your report. If `black_diamond` gold does NOT agree, STOP and file a BLOCKING row; do not push.
2. **Pre-state:** record `s3api head-object` ETag and VersionId of the key, the md5 of the repository file, the output of `python .tools/deploy-ledger-names.py --rev HEAD data/black_diamond/scripts/gold/diag_sleeve_fix.py` (expect not LEDGERED), and `git log -1` of the file. Confirm 0 other OPEN sentinels pin a top-level deploy-scope script (`python .tools/deploy_ledger.py list`; the CRO read 0 LEDGERED of 357 at HEAD).
3. **The signed change, committed by `CT-ak-4` (verify, do not edit):** `git log -1 -- data/black_diamond/scripts/gold/diag_sleeve_fix.py` shows the worker's commit on `box/laptop` (comment-only: `# noqa` comments on the six lines ruff names, AST identical; the file fails ruff at the previous commit, which is why the change is lint comments, row W118-S1); record the new blob id (10+ hex), its sha256 and md5, and confirm with `python .tools/tests/test_round21_fwd5_positive_read.py --pre` that exactly this script differs from S3. If the commit is not there, STOP and say so; do not edit the script yourself.
4. **Open the NEVER-2 entry** with `python .tools/deploy_ledger.py open --slug ctlpln-r21-fwd5-one-script-20261015 ... --window-hours 2` (read `--help` for the exact flags): legs L1 git (the commit, the blob pin, the sha256), L2 s3-prefix (`s3://opal-data-bd/code/gold/diag_sleeve_fix.py`, proof: ETag equals the new md5 AND a new VersionId), L3 verify (the audit log shows exactly one deploy row for this path and no `PINNED-DEPLOY` row for any other path; `list-object-versions` shows 2 versions). Put the prior VersionId in the entry title. The entry text carries the repo path and the pin so the hook's ledger gate admits it. Commit the entry files through `safe-commit.sh` (as the entry's own open step instructs; the sentinel and change_management paths are lane ANY and admit you), with `--author "0.7.0_AE_CloudOps~CT2 <0.7.0_AE_CloudOps~CT2@opal.agent>"`.
5. **Push, in the SAME minute as steps 3-4, uninterrupted:** the scheduled `Opal box-sync` runs every 10 minutes and pushes `box/laptop` through the same hook, so do steps 3, 4 and this push back to back (check the clock first: start just after a :x0 slot passes) with `AGENTBUS_DEVICE=laptop` and `OPAL_AGENT_SERIAL=0.7.0_AE_CloudOps~U7` set so the audit row names you. `git push origin box/laptop` (a pull-merge, never a rebase, if rejected). The hook deploys the one ledgered script through `.tools/safe-deploy.sh --no-pipescript`.
6. **Prove it, then close:** `s3api head-object` ETag equals the new md5; `list-object-versions` for the key shows 2 versions; `org/safe-deploy-bypass-audit.log` shows one deploy row for this path naming YOUR serial (row S9131: a ledgered box-diff deploy writes NO audit row, so the actor is proven by the push's own stderr `deploying 1 ledgered file(s)` and the S3 version time inside your push window; if the box-sync slot pushed first, say so) and zero `PINNED-DEPLOY` rows for any other path; no other key of `s3://opal-data-bd/code/gold/` changed since the push (count client-side in the read test below, never `--query length()` on a paginated list). Close L1-L3 and the entry (`deploy_ledger.py close-leg`, `close`). The 04:00Z runner sync is NOT part of the cell.
7. **The read test** `.tools/tests/test_round21_fwd5_positive_read.py` is committed by `CT-ak-4` (you run it, you do not edit it; read-only AWS `get`/`head`/`list` calls only): it reads the key's ETag, the version count, the repository file's md5, the keys of `code/gold/` modified since the entry's open time (paginate client-side and count), the last audit row for the path; prints `FWD5-POSITIVE versions=<n> etag_equals_repo_md5=<True|False> other_changed=<n> audit_actor=<serial|UNKNOWN> ok=<True|False>`.

### ROLLBACK (per key)

`opal-data-bd` versioning is Enabled. If any proof fails: copy the recorded prior VersionId back to the key (`s3api copy-object` from `?versionId=...`, no delete), or pin the prior blob `0e4aec8d80` in a second signed entry; close the entry with the failure named. Never leave the entry half-landed: finish in this session or roll back and escalate loud (CLAUDE.md NEVER-2).

### RULES FOR THIS CELL

Write surface = the `<paths>` (the entry's own files under `org/critical_paths/`, the surprise channel, your proof instance). The script and the read test are NOT yours to write (CT-ak-4). ONE S3 key may be written, and only by the hook's deploy of that script; do not run `aws s3 cp`, `sync` or any AWS write yourself, and do not run `safe-deploy.sh` by hand (the push is the act under test). No terraform, no Lambda, no IAM. Use `.tools/safe-commit.sh` for every commit, with explicit paths. ASCII only. CLAUDE.md and org/XXX.md are LOCKED. If a gate REFUSES, STOP and file a BLOCKING row. If the hook HOLDS the script (HELD-DEPLOY row) the finding is the result: report it, roll nothing back (nothing was written), and close the entry as not-landed. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-S<next free number>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. COPY the proof instance's field names from a VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTak3-AC1" cell_refs="CT-ak-3"><invocation>python .tools/tests/test_round21_fwd5_positive_read.py</invocation><expect>versions=2</expect></criterion>
`CTak3-AC1` -- the script's S3 key holds exactly two versions after the push (base: 1); report the whole `FWD5-POSITIVE` line.

<criterion id="CTak3-AC2" cell_refs="CT-ak-3"><invocation>python .tools/tests/test_round21_fwd5_positive_read.py</invocation><expect>other_changed=0</expect></criterion>
`CTak3-AC2` -- no other key under `s3://opal-data-bd/code/gold/` changed since the entry opened (base: the test does not exist); report the whole line.

<criterion id="CTak3-AC3" cell_refs="CT-ak-3"><invocation>python .tools/tests/test_round21_fwd5_positive_read.py</invocation><expect>etag_equals_repo_md5=True</expect></criterion>
`CTak3-AC3` -- the deployed object's ETag equals the md5 of the committed script (base: the test does not exist); report the whole line, the actor evidence (the push's stderr line and the S3 VersionId time), and the ledger entry's final state.
</proof_of_spec>

<expected_criteria>CTak3-AC1,CTak3-AC2,CTak3-AC3</expected_criteria>

Each invocation runs from the repository root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.7.0_AE_CloudOps~CT2/NFRA_CTLPLN.TO-CT-ak-3.signed-change-deploys-exactly-one-script.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTak3-AC1,CTak3-AC2,CTak3-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round21.md</decomp_doc>
<owned_cells>CT-ak-3</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/.open_deploys/ctlpln-r21-fwd5-one-script-20261015.json
org/critical_paths/change_management/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the 10-minute `Opal box-sync` task exists already and its push through the hook is the named timing hazard, handled by order of steps.
comp-iam: DECLARED-NOT-APPLICABLE no policy or role is changed; the deploy is the box's existing deploy path (safe-deploy.sh) writing one object.
comp-adversary: RUN -- the push deploying more than the named script (the pinned-entry step runs on every push: 0 other pins measured at HEAD, the read test counts changed keys client-side); the script chosen being executed by a schedule (research: not in `gold_dispatch.sh`'s 24, imported by nothing); the actor attribution lost to the 10-minute box-sync slot (steps 4-5 back to back; the ledgered box-diff path writes no audit row, S9131, so the actor is proven by the push's own stderr); a half-landed deploy (NEVER-2 entry opened first, closed last, rollback VersionId recorded); the hook's pre-read key being wrong (step one compares it with the core; bd gold agrees per the issuer's read-only check); the first live pass of the pinned-entry code path (its S3 read of a present object is exercised for the first time; a no-op today); BLIND: the runner's 04:00Z sync of `code/gold/` and the mdpf tree (absent from the hook's map, held).
research: org/tier1_exec/4.0.0_SA_CRO/deliverables/NFRA_CTLPLN_R21_FWD5_ONE_SIGNED_CHANGE_ONE_SCRIPT_RESEARCH_20261015.md (4.0.0_SA_CRO, WORLD research owed and delivered before the cut).
risk: WORLD -- one real S3 write to a production code prefix (`s3://opal-data-bd/code/gold/diag_sleeve_fix.py`); the blast radius above is the whole write set.
lane: the <paths> block IS the grant (worker RULING 1). `0.7.0_AE_CloudOps~CT2` is the NFRA_CTLPLN laptop deploy seat (re-pointed from ~U7 by AMENDMENT 1); an application by a CloudOps seat is the standing route for a deploy. The commits of the script and of the read test are the worker cell CT-ak-4's.
</preflight>

Base checks, dry-run by the issuer before the cut: CTak3-AC1, AC2 and AC3 FAIL as expected (the read test does not exist). Pre-state read by the issuer 2026-10-15 ~16:3xZ: `list-object-versions` for the key prints 1 version. `deploy_ledger.py list` shows 5 OPEN or HELD entries, none pinning a top-level gold script.
Source: CTO round-20 analysis ruling 4 (`ledger/ROUND_ANALYSIS.round20.md` @5df0b0af31), msg 109441; CRO research (above); rows D1-S8, W113-S1.
