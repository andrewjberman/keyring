# AMGT_RESAPP task order -- `AMGT-rk-59` -- the harvest root's targeted plan tolerates the absent chatter build zip: `chatter-axis-schedule.tf:124` evaluates to null when `.build/chatter-axis-producer.zip` is absent and to the same hash as today when it is present, so no unrelated resource can block a targeted plan in this root again

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-59</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~59</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- (comp-schedule 2026-09-18 ~15:55Z: scanned 5 of 5 carriers, C1=23 C2=6 C3=12 C4=21 C5=334,
  25 gates armed, 136 prose blocking fields not counted. This order edits the ONE FILE that declares the daily
  chatter schedule, aws_scheduler_schedule.chatter_axis_daily at chatter-axis-schedule.tf:172-184, and moves NONE
  of its attributes: cron(0 10 * * ? *), state ENABLED, flexible_time_window OFF -- AC5 asserts both strings occur
  exactly once in HEAD's bytes and once in the edited bytes. It arms no cron, alarm, monitor or cadence; the C2
  deploy ledger (6 open entries) gains nothing because this order names NO apply.)
comp-iam: RUN -- (comp-iam cross-reference 2026-09-18 ~15:55Z: 214 IAM roles parsed, 190 services scanned, 169
  Lambda services, 1131 operations, 328 permission gaps across 31 services; amgt-resapp-chatter-axis is NOT among
  the 31 (0 gaps). This order edits ONE expression on aws_lambda_function.chatter_axis_producer -- source_code_hash
  at chatter-axis-schedule.tf:124 -- and touches no role, no policy, no grant, no principal; it names no terraform
  apply. Its Terraform acts are plan/validate/console only, -lock=false -refresh=false, under the device's existing
  credentials against the harvest/tfstate backend.)
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~59`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~59;`. **NEVER RUN AN INSTALL** (`terraform init` in the harvest root,
which downloads the root's pinned providers into the gitignored `.terraform/`, is the one precondition and is not an
install of anything into the tree; `build_zip.py`'s pip-download of the pinned jsonschema wheels into the gitignored
`.build/` is the documented build step at AC4 and writes nothing tracked).

## 1. THE CELL, inlined in full -- `AMGT-rk-59` (R14-T5; row `AMGT_RESAPP-Z-W34-S1`; s.3.7; infra, lane CLOUD_OPS_OR_ETL)

**The analysis row, verbatim (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T5 `:145`):** *"W34-S1 (s.3.7)"*
-- serves infra; co-sign no. The ruling it implements, s.3.7 (`:100-102`), verbatim: *"The Terraform plan blocked by
a missing build zip (W34-S1, OPEN, ARMED). RULED: a build cell. `chatter-axis-schedule.tf:124` must tolerate the
absent `.build` zip, or the build step is committed, so an unrelated resource can never block a targeted plan.
Infra, `CLOUD_OPS_OR_ETL` lane. Cell R14-T5."* This order takes the FIRST arm -- tolerate the absent zip -- because it
is one expression, it changes no value when the zip is present, and it needs no apply; the second arm (a committed
build step in worktree provisioning) is NOT taken and is not this cell's.

**The row this cell closes, `AMGT_RESAPP-Z-W34-S1` (`INVESTIGATION_v1.md:8677-8699`, OBSERVATION, ARMED, disarm owner
`1.0.0_SA_CTO~Z / 2.0.0_SA_COO~Z`), verbatim in its two binding fields.** `spec_asserts` (`:8696`): *"The task
order's own procedure (step 3) assumes a targeted terraform plan against infra/aws/terraform/harvest evaluates
cleanly once the ONE list-entry change is made, naming only the role-policy resource."* `world_is` (`:8697`): *"A
targeted plan in this root also depends on every OTHER resource's static expressions evaluating without error,
regardless of -target, because Terraform builds its full configuration graph before pruning to the target; a
missing gitignored local build artifact for an entirely unrelated Lambda (chatter_axis_producer) blocked the plan
until worked around with a disposable, never-committed placeholder file at the same path."* The measured error
(`:8689`): *"Error in function call ... on chatter-axis-schedule.tf line 124 ... Call to function
"filebase64sha256" failed: open .build/chatter-axis-producer.zip: The system cannot find the path specified."*

**THE MEASURED STATE, at HEAD (`chatter-axis-schedule.tf` last moved @a30a75d74a 2026-09-15; cite these lines):**
- `infra/aws/terraform/harvest/chatter-axis-schedule.tf:44`: `chatter_axis_zip = "${path.module}/.build/chatter-axis-producer.zip"`;
  `:118-124`: `resource "aws_lambda_function" "chatter_axis_producer"` with `filename = local.chatter_axis_zip` (`:123`)
  and `source_code_hash = filebase64sha256(local.chatter_axis_zip)` (`:124`). The file's own comment `:33-42` documents
  the precondition (*"Run it BEFORE terraform init/plan: filebase64sha256() reads the file during evaluation"*) --
  a KNOWN precondition, not a defect in the source, that nothing in worktree provisioning runs.
- The zip is gitignored (`.gitignore:95` `*.zip`; confirmed by the row via `git check-ignore -v`) and is built by
  `infra/aws/terraform/harvest/lambda_src/build_zip.py` (`_OUTPUT` `:69` = `.build/chatter-axis-producer.zip`;
  `main()` `:333`). A fresh linked worktree carries no `.build/` directory -- that is the state your worktree is in
  at spawn, and AC2 asserts it before anything else.
- `filebase64sha256()` is a Terraform built-in read at EVALUATION time for every resource in the root, and `-target`
  does not prune evaluation (the row's measurement, `:8689`, `:8697`). `fileexists()` is the built-in that answers
  whether the path exists without reading it. `source_code_hash` on `aws_lambda_function` is Optional; a `null`
  value declares nothing and leaves the attribute to the provider, so an absent zip yields no evaluation error and
  the resource cannot be APPLIED without the zip (`filename` is read at apply) -- fail-closed on the right resource.
- The other evaluation-time read in this root, `module.scoped_amgt_api.data.aws_s3_object.artifact`
  (`build-and-upload-scoped-amgt.sh:5-11`, `scoped-amgt-api.tf:225-226`), reads an S3 key that exists permanently;
  it does not block a fresh worktree and is NOT this cell's.
- Lane: `infra/aws/**` resolves to `CLOUD_OPS_OR_ETL` (`.owned-paths.yaml:1906-1907`); this worker is admitted to
  the one file by THIS order's `<paths>` (ADHC_OWNPTH.005, `.tools/owned-paths-validate.py:114-122`). Read before
  any apply was named: none is named.
- `.tools/safe-apply.sh` (`:1-27`, `:52-66`) gates `apply` ONLY and says so: *"`plan` and other subcommands are
  non-destructive -- call terraform.exe directly for those"*; on site Z terraform resolves on PATH (`:32-33`).

**RULED, what you build (one expression, one comment block):**
1. `chatter-axis-schedule.tf:124` becomes
   `source_code_hash = fileexists(local.chatter_axis_zip) ? filebase64sha256(local.chatter_axis_zip) : null`
   -- ONE line; `filename` (`:123`) and every other attribute of the resource are untouched.
2. The comment block `:33-42` is amended in place (no line outside `:33-44` and `:124` moves): state that an
   ABSENT zip evaluates to `null` (no error; a targeted plan on any other resource proceeds; the function itself
   cannot be applied without the zip because `filename` is read at apply), that a PRESENT zip computes exactly the
   hash it computes today, and that `build_zip.py` is therefore a precondition of a plan or apply that TARGETS this
   function, not of every plan in the root (row `AMGT_RESAPP-Z-W34-S1`, cell `AMGT-rk-59`).
3. `terraform fmt` on the file; `terraform validate` on the root.

**NO APPLY IS NAMED BY THIS ORDER.** A Terraform expression whose value is identical when the zip is present is
applied by nothing: with the zip built, the plan for `chatter_axis_producer` reads exactly what it read before this
edit. If AC4's targeted plan on that function reports a change, it is the PRE-EXISTING delta between a freshly built
zip and the function deployed 2026-09-15 (the packaged sources have moved since; `AMGT-rk-53` moves
`lib/research/metrics/chatter_axis.py` again this round) -- that delta is a DEPLOY, it belongs to the COO's
consolidated redeploy under its own never-widen pair, and you RECORD it and do not apply it. Never `terraform apply`
of any shape, never `safe-apply.sh`, never `aws lambda update-function-code`.

**What this cell does NOT change:** `lambda_src/build_zip.py`; `lambda_src/lambda_function.py`; the schedule
`:172-184`; the role and policy `:58-116`; `scoped-amgt-api.tf`; the live function; the live schedule; the state
file; worktree provisioning (`AMGT-rk-60` is the provisioning cell and does not run `build_zip.py` either).

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** an infra cell with no security
population; proven on a DRY RUN -- `terraform validate`, `terraform plan -refresh=false -lock=false` (evaluation and
diff, no state lock, no write), `terraform console`, and one local build into the gitignored `.build/`. Nothing is
written to any pool, table, function or state. `C-PRODUCTION-HOME` (`:1643-1650`): no worker's folder is read; the
zip is built from the repository's own sources.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.3.7 (`:100-102`), s.4 row R14-T5
(`:145`) and s.6 (`:207`); the row `AMGT_RESAPP-Z-W34-S1` (`surprise-channel/investigations/INVESTIGATION_v1.md:8677-8699`,
filed 2026-09-18T02:10Z by `0.9.0_WK_AMGT_RESAPP~34`). PRD v0.13 @1699960261: `C-PRODUCTION-HOME` (`:1643-1650`),
`C-VALIDATION-NAMES` (`:1652-1658`); s.10's stage table names the chatter Lambda as *"the ONLY scheduled stage"*
(`:1633`) and this order leaves its schedule exactly as declared (`:1660-1661`: *"the chatter schedule; any cadence,
which stays Andrew's"*).

## 3. SURFACES -- what you may read and write

<paths>
infra/aws/terraform/harvest/chatter-axis-schedule.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~59/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-59.plan-tolerates-absent-zip.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `lambda_src/build_zip.py`,
  `scoped-amgt-api.tf`, `main.tf`, `.tools/safe-apply.sh` and `.gitignore` freely); this block governs WRITES.
  `org/critical_paths/change_management/` and `org/critical_paths/.open_deploys/` are granted because every infra
  order carries them; this order names NO apply, so you open NO entry -- if you find yourself opening one, STOP: an
  apply is outside this order. Scratch is `<your worktree>/.scratch/` only; the gitignored `.build/` and `.terraform/`
  under the harvest root are build outputs, not surfaces, and are never committed (`git status --short` after AC4 must
  show only the one `.tf` as modified).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~59 <0.9.0_WK_AMGT_RESAPP~59@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. The `.tf`
  passes `.tools/commit-gate.sh` inside safe-commit.
- **TERRAFORM:** `terraform` from PATH (site Z; `.tools/safe-apply.sh:32-33`). `terraform -chdir=infra/aws/terraform/harvest init -input=false`
  once, first; every plan carries `-input=false -lock=false -refresh=false` (evaluation and diff, never a state lock
  held against a peer, never a refresh write). **NEVER `apply`.**

## 4. BOUNDS

**NO APPLY, NO DEPLOY, NO LIVE WRITE, NO VENDOR CALL.** PORTAL FROZEN (not your surface). **COLLECTION STAYS
OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker** -- and the schedule this file declares
is neither armed, disarmed nor edited. Secrets through `comp-secrets` only. No non-ASCII in anything you write.
**PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular, never by a placeholder zip (the
workaround the row used and removed) and never by editing `build_zip.py`.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the plan summary counts AC3 and
AC4 print are whatever the backend state and the built zip say at spawn; the bar is the ABSENCE of the evaluation
error and the CONFINEMENT of any function diff to `source_code_hash`, not a particular count.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W59-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-59"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, subprocess
f = 'infra/aws/terraform/harvest/chatter-axis-schedule.tf'
t = io.open(f, encoding='utf-8').read()
new = 'source_code_hash = fileexists(local.chatter_axis_zip) ? filebase64sha256(local.chatter_axis_zip) : null'
print('tolerant_expression', t.count(new), 'of 1 expected')
print('bare_filebase64sha256_calls', t.count('filebase64sha256(local.chatter_axis_zip)') - t.count(new), 'of 0 expected')
r = subprocess.run(['terraform', 'fmt', '-check', '-diff', 'chatter-axis-schedule.tf'], cwd='infra/aws/terraform/harvest', capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
print('fmt_rc', r.returncode, (r.stdout + r.stderr).strip()[-400:])
v = subprocess.run(['terraform', '-chdir=infra/aws/terraform/harvest', 'validate', '-no-color'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
print('validate_rc', v.returncode, (v.stdout + v.stderr).strip()[-400:])
"</invocation><expect>tolerant_expression 1 of 1 expected and bare_filebase64sha256_calls 0 of 0 expected (at HEAD the two figures read 0 and 1); fmt_rc 0 with no diff; validate_rc 0 printing "Success! The configuration is valid." (terraform init has been run once in the harvest root before this criterion) ISSUER REPAIR (2.0.0_SA_COO~Z, on row W59-S1): fmt_rc may be non-zero ONLY when the fmt diff is confined to lines OUTSIDE this cell's hunks (33-44 and 124) AND reproduces identically on HEAD's own bytes (pre-existing drift, printed with its line range) -- that branch is PASS; a fmt diff touching this cell's hunks is FAIL; validate_rc 0 is required in every branch; fixing drift outside the hunks is forbidden by AC5</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-59"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, os, shutil, subprocess
root = 'infra/aws/terraform/harvest'
f = root + '/chatter-axis-schedule.tf'
zipp = root + '/.build/chatter-axis-producer.zip'
print('zip_absent_before', not os.path.exists(zipp), '(the fresh worktree carries no .build/)')
assert not os.path.exists(zipp), 'this criterion is only meaningful with the zip ABSENT; remove .build/ first'
edited = io.open(f, 'rb').read()
head = subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True, timeout=30).stdout
def plan():
    r = subprocess.run(['terraform', '-chdir=' + root, 'plan', '-input=false', '-lock=false', '-refresh=false', '-no-color', '-target=aws_iam_role.chatter_axis_scheduler'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
    out = r.stdout + r.stderr
    return r.returncode, out
try:
    io.open(f, 'wb').write(head)
    rc0, out0 = plan()
    print('CONTROL (HEAD bytes): rc', rc0, 'filebase64sha256_error', out0.count('Call to function \"filebase64sha256\" failed'), 'of 1 expected')
finally:
    io.open(f, 'wb').write(edited)
rc1, out1 = plan()
print('EDITED bytes: rc', rc1, 'filebase64sha256_error', out1.count('Call to function \"filebase64sha256\" failed'), 'of 0 expected')
print(out1.strip()[-900:])
print('bytes_restored', io.open(f, 'rb').read() == edited)
"</invocation><expect>zip_absent_before True; CONTROL (HEAD bytes): rc 1 with filebase64sha256_error 1 of 1 expected -- the planted negative reproduces row W34-S1's exact failure on the unedited bytes in this same worktree; EDITED bytes: rc 0 with filebase64sha256_error 0 of 0 expected and a plan tail reading "No changes." or a summary that names ONLY aws_iam_role.chatter_axis_scheduler (never chatter_axis_producer); bytes_restored True -- the file ends the invocation carrying the edited bytes</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-59"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os, re, subprocess
root = 'infra/aws/terraform/harvest'
zipp = root + '/.build/chatter-axis-producer.zip'
print('zip_absent', not os.path.exists(zipp))
r = subprocess.run(['terraform', '-chdir=' + root, 'plan', '-input=false', '-lock=false', '-refresh=false', '-no-color'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
out = r.stdout + r.stderr
print('rc', r.returncode, 'filebase64sha256_error', out.count('Call to function \"filebase64sha256\" failed'), 'of 0 expected')
summ = re.findall(r'Plan: \d+ to add, \d+ to change, \d+ to destroy\.|No changes\.', out)
print('summary', summ)
blocks = re.findall(r'# aws_lambda_function\.chatter_axis_producer will be (\w+)', out)
print('chatter_axis_producer_action', blocks, 'of 0 blocks expected when the state hash is kept')
attrs = re.findall(r'^\s*[~+-]\s+(\w+)\s*=', out.split('# aws_lambda_function.chatter_axis_producer', 1)[1].split('\n\n', 1)[0], re.M) if '# aws_lambda_function.chatter_axis_producer' in out else []
print('chatter_axis_producer_changed_attrs', attrs)
"</invocation><expect>zip_absent True; rc 0 and filebase64sha256_error 0 of 0 expected -- the UNTARGETED plan evaluates with the zip absent, which it could not at HEAD; summary printed (re-measure: "No changes." is the expected reading when the provider keeps the state's hash for a null source_code_hash; if a change block for chatter_axis_producer appears, chatter_axis_producer_changed_attrs must list source_code_hash and nothing else, and that block is RECORDED, never applied); any other resource's diff in this untargeted plan is pre-existing root drift, recorded verbatim in your report and left alone</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-59"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import base64, hashlib, io, os, re, subprocess, sys
root = 'infra/aws/terraform/harvest'
zipp = root + '/.build/chatter-axis-producer.zip'
b = subprocess.run([sys.executable, root + '/lambda_src/build_zip.py'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
print('build_rc', b.returncode, (b.stdout + b.stderr).strip()[-600:])
print('zip_present', os.path.exists(zipp), 'bytes', os.path.getsize(zipp) if os.path.exists(zipp) else None)
py = base64.b64encode(hashlib.sha256(io.open(zipp, 'rb').read()).digest()).decode('ascii')
c = subprocess.run(['terraform', '-chdir=' + root, 'console', '-no-color'], input='fileexists(local.chatter_axis_zip) ? filebase64sha256(local.chatter_axis_zip) : null\n', capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
tf = (c.stdout or '').strip().strip('\"')
print('console_rc', c.returncode, 'hash_equal', tf == py, 'python', py, 'terraform', tf)
r = subprocess.run(['terraform', '-chdir=' + root, 'plan', '-input=false', '-lock=false', '-refresh=false', '-no-color', '-target=aws_lambda_function.chatter_axis_producer'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
out = r.stdout + r.stderr
print('targeted_plan_rc', r.returncode, re.findall(r'Plan: \d+ to add, \d+ to change, \d+ to destroy\.|No changes\.', out))
seg = out.split('# aws_lambda_function.chatter_axis_producer', 1)[1].split('\n\n', 1)[0] if '# aws_lambda_function.chatter_axis_producer' in out else ''
print('changed_attrs', re.findall(r'^\s*[~+-]\s+(\w+)\s*=', seg, re.M))
st = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout
print('tracked_changes', [l for l in st.splitlines() if not l.startswith('??')])
"</invocation><expect>build_rc 0 and zip_present True (the documented precondition, run here as the POSITIVE control); console_rc 0 and hash_equal True -- with the zip PRESENT the tolerant expression computes byte-for-byte the value the bare filebase64sha256() computed before this order; targeted_plan_rc 0; the plan summary and changed_attrs are RECORDED: "No changes." means the built zip matches the deployed function, and a single source_code_hash change means the pre-existing build/live delta (a deploy that is NOT this order's and is NOT applied); tracked_changes lists exactly one entry, the modified chatter-axis-schedule.tf (the build wrote only gitignored paths)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-59"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, re, subprocess
f = 'infra/aws/terraform/harvest/chatter-axis-schedule.tf'
head = subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True, timeout=30).stdout
now = io.open(f, 'rb').read()
print('non_ascii_now', len(now) - len(now.decode('utf-8')), 'crlf_now', now.count(b'\r\n'))
for label, b in (('HEAD', head), ('EDITED', now)):
    t = b.decode('utf-8')
    print(label, 'cron', t.count('cron(0 10 * * ? *)'), 'of 1; state_enabled', t.count('state                        = \"ENABLED\"'), 'of 1; lines', len(t.splitlines()))
d = subprocess.run(['git', 'diff', '-U0', 'HEAD', '--', f], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout
hunks = re.findall(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', d, re.M)
print('hunks', hunks)
ok = all(int(h[0]) >= 33 and int(h[0]) + (int(h[1]) if h[1] else 1) - 1 <= 44 or int(h[0]) == 124 for h in hunks)
print('hunks_confined_to_33-44_and_124', ok, 'of', len(hunks), 'hunks')
ns = subprocess.run(['git', 'diff', '--numstat', 'HEAD'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip().splitlines()
print('files_changed', len(ns), 'of 1 expected', ns)
"</invocation><expect>non_ascii_now 0 and crlf_now 0; HEAD and EDITED both print cron 1 of 1 and state_enabled 1 of 1 (the schedule is untouched); every diff hunk's OLD-side range sits inside lines 33-44 (the comment) or starts at line 124 (the expression) -- hunks_confined_to_33-44_and_124 True of N hunks with N at least 1; files_changed 1 of 1 expected, the one .tf</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Order of execution matters and is fixed: `terraform init` once, then AC1, AC2 and AC3 with the zip ABSENT,
then AC4 (which builds it), then AC5. AC2's CONTROL arm rewrites the `.tf` to HEAD's bytes for one plan and restores
your edit in `finally`; snapshot your edited bytes to `.scratch/` before running it.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~59/AMGT_RESAPP.TO-AMGT-rk-59.plan-tolerates-absent-zip.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, quoting AC3's and AC4's plan summaries verbatim so the
COO's consolidated chatter redeploy (under `AMGT-rk-53`'s pair) knows whether the built zip already differs from the
live function.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~59</slot>
<fabric>site-z</fabric>
