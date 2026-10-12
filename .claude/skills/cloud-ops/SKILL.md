---
name: cloud-ops
description: Operational reference and permissions profile for AE_CloudOps seats -- load before AWS CLI, Terraform, EC2/SSM or any cloud-infrastructure work. Pre-approves the routine-ops wildcards in .claude/settings.json and restates the CLAUDE.md non-negotiables that pre-approval does not override. Canonical home of deployment rules 4, 5, 6, 8, 9, 11, 12, 18.
---

# cloud-ops

**Refreshed:** 2026-08-25 (1.0.0_SA_CTO~X, Andrew-direct: the DEPLOYMENT RULES now live HERE as their canonical home, not in CLAUDE.md. Prior pass 2026-05-27 -- CLAUDE.md Rules 1-19 cross-reference + LD-0034 / 0049 / 0066 / 0072 / 0082 / 0084 / 0090 / 0113 / 0115 / 0116 operating-doctrine pointers + current pipeline + bucket + secrets + KMS inventory snapshot)

You are operating in a pre-approved cloud-ops profile. The wildcards in `.claude/settings.json` cover the routine AWS / Terraform / EC2 / SSM / CloudFormation / .tools surfaces. Run them autonomously — do not pause to ask the user "should I run this?" for any pattern that already matches.

## What's pre-approved (you don't need permission)

- `aws *` — all AWS CLI commands (Bash + PowerShell)
- `terraform *` (any binary path: `.tools/terraform.exe`, `terraform`, `terraform.exe`) — plan, apply, refresh, init, import, state ops
- `.tools/*` — full canonical set (the wildcard covers all; named for reference):
  - **Compiler tools**: `comp-blast`, `comp-pipescript`, `comp-iam`, `comp-routes`, `comp-transform`, `comp-cache`, `comp-validate`, `comp-platinum`, `comp-pii`, `comp-trace`, `comp-build`, `comp-registry sync`
  - **Commit + deploy discipline**: `safe-commit.sh`, `safe-apply.sh`, `safe-deploy.sh`, `safe-ec2-deploy.sh`, `commit-gate.sh`, `halt-gate-check.sh` (and `infra/aws/lambda/ci/record-terraform-deploy.sh`, which is NOT under `.tools/`)
  - **Misc**: `jq`, `terraform.exe`, `git-hooks/install-*.sh`
- EC2 lifecycle ops via SSM (`aws ssm send-command`, `aws ssm get-command-invocation`, `aws ssm list-commands`)
- S3 list / cp / sync via Bash and PowerShell
- CloudWatch Logs queries (`aws logs filter-log-events`, `describe-log-streams`, `get-log-events`, `put-log-events`, `describe-metric-filters`)
- CloudWatch Alarms (`aws cloudwatch describe-alarms`, `get-metric-statistics`)
- EventBridge inspect (`aws events describe-rule`, `list-rules`, `list-targets-by-rule`)
- Lambda inspect (`aws lambda get-function-configuration`, `get-function`, `list-functions`)
- DynamoDB read (`aws dynamodb query`, `get-item`, `scan`)
- IAM read (`aws iam get-role`, `get-role-policy`, `list-attached-role-policies`)
- CloudTrail inspect (`aws cloudtrail describe-trails`, `get-event-selectors`)
- git workflow (status, diff, log, add, commit via safe-commit.sh, tag, push, fetch, pull)
- Standard PowerShell file ops (Test-Path, New-Item, Get-ChildItem, Out-File, Set-Content)

If your task hits a tool the user has not pre-approved, ask once briefly — don't loop on retry.

## What is NEVER pre-approved (CLAUDE.md non-negotiables, ask first)

- `aws lambda update-function-code` / `update-function-configuration` — **violates Rule 1**. Lambda code deploys ONLY via terraform apply.
- `deploy.sh` shortcut scripts for Lambdas, AWS console deploys
- Direct EC2 code writes (`aws s3 cp ... s3://opal-data-*/code/...` is fine; SCP/SSH to write code on a VM is not — see Rule 12)
- `terraform destroy` of any resource without explicit instruction
- `git reset --hard`, `git push --force` (especially to main/master), `git tag -d -r`, force-deletion ops
- `rm -rf` of anything outside `/tmp` or workspace `.runtmp/` / `.frontend-dev/`
- Stop/terminate EC2 instances unless the workflow explicitly calls for it (e.g., a known-stale runner)
- `aws s3 rm --recursive`, `aws s3api delete-bucket`, `aws dynamodb delete-table` — irreversible
- Anything that drops/empties a database table, deletes S3 objects in opal-data-* buckets, or modifies CI/CD pipelines without an authoring TO
- **Bare `terraform apply` — banned by Rule 18.** Use `.tools/safe-apply.sh` (HALT-gate checkpoint immediately pre-irreversible-apply; STOP-class inbox messages hard-block; `HALT_OVERRIDE="<reason>"` audited bypass).
- **Bare `git commit` — banned by Rule 14a.** Use `.tools/safe-commit.sh --author "..." -m "..." -- <paths>` (concurrent-agent index-contamination guard).
- **`.py` edits without `.tools/commit-gate.sh` — banned by Rule 14.** Three sub-gates must exit 0: `py_compile` + `ds-precommit-check.py` (AST + `coerce_silver_ids` enforcement + Rule-15 future-annotations check) + `ruff check --target-version py39`.
- **Silver-tier field-slimming / null-handling / business-row-filtering — banned by Rule 17.** Silver = clean shape, preserved content. Business logic belongs in gold.

For these, surface the command + the reason + ask before running.

## THE DEPLOYMENT RULES -- canonical home (moved off CLAUDE.md 2026-08-25, Andrew-direct)

**These used to live in CLAUDE.md and were read by every agent in the fabric, most of whom never
touch a Lambda.** They now live here, where they load for the seats that actually do cloud work.
**THIS SECTION IS CANONICAL** -- it is not a refresher and not a mirror. CLAUDE.md keeps a pointer,
not a copy.

⛔ **THE NUMBERS ARE LOAD-BEARING AND DELIBERATELY UNCHANGED.** 41 files cite "CLAUDE.md Rule 4", 35
cite Rule 12, 17 cite Rule 6. Renumbering would dangle every one of those citations, so a rule keeps
its number forever even when the list has gaps. **Gaps are correct**: 1, 2, 3, 7 and 10 were deleted
2026-08-25 (Terraform-only-Lambda, commit-before-apply, layers, the EC2 wrapper mandate, and the
Docker-push ban) as unenforced restatements of rules that survive elsewhere.

### 4. UPDATE THE SOURCE MAP
Every Lambda has an entry in `infra/aws/lambda/ci/lambda-source-map.json`.
⚠ **The map PAIRS a Lambda with its repo dir. It does NOT compare deployed bytes to built-from
bytes.** It read "(CI drift detection)" until 2026-08-12 and promised a control the estate does not
have -- measured that day on a live Lambda running bytes older than its own tree, where plan 0-diff,
`get-role-policy`, `get-function-configuration` and a green scheduled run ALL passed. Code currency
is CLAUDE.md Rule 22a's CODE layer and it is the assignee's read, not this map's.
*Compliance measured 2026-08-25: 192 of 198 live functions carry an entry (97%).*

### 5. SIZE LAMBDA RESOURCES DELIBERATELY
Set `memory_size` + `timeout` explicitly. Never leave the `yang-lambda` module defaults (256MB/30s)
on a data-processing Lambda.
*Measured 2026-08-25: 14 of 198 sit at the exact default, and none of them is data-shaped.*

### 6. TAG AFTER DEPLOY
`git tag -a {pipeline}-v{X.Y.Z}` + `git push --follow-tags` after every 0-diff apply.
*Measured 2026-08-25: 864 of 927 tags match the form (93%).*

### 8. `EC2_MANIFEST.json` IS THE SOURCE OF TRUTH
`infra/aws/ec2/EC2_MANIFEST.json` -- every EC2 service registered; CI/CD depends on it.
⚠ **Its entries are SERVICES, not instances, and the two counts will never match.** Measured
2026-08-25: 27 service entries against 32 instances (4 running + 28 stopped) -- the fleet is
stopped-when-idle batch runners, so comparing those numbers directly manufactures a gap that is not
there. Name the grain before you diff.

### 9. TERRAFORM MANAGES EC2 INFRASTRUCTURE, NOT CODE
TF owns the instance, IAM and security groups. Code deploys via `infra/aws/ec2/safe-ec2-deploy.sh`
or SSM. **This boundary is the one that matters and it absorbed the old Rules 7 and 10** (the wrapper
mandate and the Docker-push ban), both of which restated it in a form nothing could check.

### 11. VERIFY PARITY BEFORE EC2 WORK
`./infra/aws/ec2/verify-ec2.sh` -- drift check between local source and deployed code, reads
`EC2_MANIFEST.json`.

### 12. S3 IS THE ARTIFACT STORE FOR ALL EC2 CODE
Never write code on a VM. Never inline Python in an SSM command. Local -> S3 -> EC2 pulls ->
execute, **even for ad-hoc diagnostics.** Spec: `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`.

### 18. `terraform apply` GOES THROUGH `.tools/safe-apply.sh`
HALTGT inbox checkpoint at the last reversible moment (routine pending msg -> `HALT_ACK=1`; override
audited via `HALT_OVERRIDE="reason"`).
⚠ **A HALTGT PASS IS NOT EVIDENCE YOU WERE NOT HALTED, and `[STOP]` does NOT reliably hard-block.**
The checkpoint sees only unread files directly under `inbox/<serial>/`, so a live Monitor (which
moves the message first) guarantees a silent empty-inbox `exit 0`, and a `~lane` agent is unhaltable
regardless. **NOBODY CITES A HALTGT PASS.** `docs/architecture/ADHC_HALTGT.md`, `org/tier0/ledger/LD-0267.md`.

### 18a. THE PRE-APPLY INBOX CHECK -- it must not be able to read CLEAN (row NFRA_IAMROLES202609-Z-S42)

Rule 18's caveat says a `~lane` agent is **unhaltable**, so HALTGT cannot be cited and such a seat must read its
own inbox before an irreversible apply. **That direct read is the only pre-apply mail guard a `~lane` seat has,
and the obvious form of it fails toward CLEAN.** Measured 2026-10-11 (`0.7.0_AE_CloudOps~IR`, round 7): the
expression below was cited in THREE apply records and could not have detected mail in any of them.

```bash
# DO NOT USE -- all three defects measured:
ls -1 org/mcp/inbox/<base>/~<lane>/ 2>/dev/null | grep -vc '^read$'
```
1. **From a LINKED WORKTREE it prints `0` because the inbox path is not checked out there** -- identical to an
   empty inbox. Rule 14b is what sends a seat to a worktree to commit, so this is the normal case, not the edge.
2. **From the main tree it over-counts by one:** `ls -1` renders the subdirectory as `read/`, which `^read$`
   never matches, so the directory itself is counted. Against an empty inbox it prints `1`.
3. **`ls -1` hides dotfiles**, and the only regular files directly in that directory are `.unread-deliveries`
   and `.watcher.owner`. The denominator is not what it appears to be.

**THE FORM TO USE, two limbs:**

- **(a) PRIMARY -- the broker read.** `get_delivery_state(<your FULL lane serial>)` and count **every row not
  `READ`**. This is sound from any tree because it does not depend on a checkout, and it is the only limb that
  survives a **live Monitor**: the watcher `mv`s an arriving message into `read/` before any agent sees it, so a
  file-based check goes quiet exactly when mail has arrived. `READ` is also the only state that claims an AGENT
  saw a message -- `SENT` and `EMITTED` are transport, not readership.
- **(b) FALLBACK, only if the broker is unreachable.** `test -d` the **REAL** inbox path
  (`org/mcp/inbox/<base>/~<lane>/` under the **MAIN workspace root**, never a linked worktree's copy), then
  `ls -A` and count entries other than `read/`. **A MISSING PATH IS AN ERROR** -- print it and exit non-zero.
  **It is NEVER a `0`.** That rule is the whole disarm: defect 1 above was a missing path silently becoming a
  clean reading.

```bash
# (b) fallback -- ROOT is the main workspace, resolved, never the cwd
ROOT=$(git -C "$(git rev-parse --show-toplevel)" rev-parse --path-format=absolute --git-common-dir)/..
INBOX="$ROOT/org/mcp/inbox/<base>/~<lane>"
test -d "$INBOX" || { echo "ERROR: inbox path absent: $INBOX -- this is NOT an empty inbox"; exit 2; }
# -type f excludes read/ regardless of how ls renders it; the name pattern (the message filename grammar YYYYMMDDT...,
# never a pinned year) excludes state dotfiles. Control: a planted message named by that grammar counts 1.
echo "unread=$(find "$INBOX" -maxdepth 1 -type f -name '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]T*.md' | wc -l)       state_markers=$(find "$INBOX" -maxdepth 1 -type f ! -name '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]T*.md' | wc -l)"
```

> **DO NOT FILTER `read/` BY NAME WITH `ls`, IN ANY FORM. `ls` IS ALIASED TO `ls -F` HERE**
> (`ls -F --color=auto --show-control-chars`), and `-F` appends `/` to a directory, so `ls -A` emits
> **`read/`** and `grep -v '^read$'` never matches it. Measured 2026-10-11: that alias is the actual mechanism
> behind Z-S42's over-count, and it defeats `ls -1` and `ls -A` alike. `find -maxdepth 1 -type f` cannot be
> fooled by the rendering. **Both counts are printed** because the two state dotfiles
> (`.unread-deliveries`, `.watcher.owner`) are always present: a bare entry count reads 3 against an empty
> inbox, which is a tripwire that is always tripped and therefore gets ignored -- as useless as one that reads
> clean.

**COST:** one broker call. **NON-APPLICATION:** a seat that is not `~lane`-scoped can be halted and has HALTGT;
this is for the seats that cannot.

### IAM INSTRUMENT TRAPS -- moved from CLAUDE.md Rule 22a, 2026-08-25

⛔ **`comp-iam` IS NOT SUFFICIENT FOR A NEW RESOURCE, AND IT FAILS *GREEN*.** It models `(action)`,
never `(action, resource)` -- **a role holding `s3:GetObject` on ANY bucket reports `[GRANTED]` for a
call to EVERY other.** It also cannot see returned-buffer calls (`batch_writer`) or
`generate_presigned_url`'s action-at-REDEMPTION.

>> **AN UNDER-REPORTING IAM INSTRUMENT DOES NOT CAUSE AccessDenied -- IT CAUSES A FUTURE ENGINEER
DOING LEAST-PRIVILEGE CLEANUP TO DELETE A NEEDED GRANT AS "UNUSED". SILENCE IS THE DEFECT; THE TRACE
IS A BONUS. NEVER read a comp-iam operation list as a deletion warrant.** << Treat it as a FLOOR.

For a NEW bucket/table/ARN, verify on the live primitive:
```
aws iam simulate-principal-policy --policy-source-arn <role> --action-names <action> \
    --resource-arns <exact key>
```
⛔ **THAT INSTRUMENT HAS FOUR INDEPENDENT FALSE-DENY MODES:**
1. **2+ `--resource-arns` in one call flips the HELD ones to `implicitDeny`.**
2. **It EVALUATES `Condition` blocks** -- with no `--context-entries`, a conditioned statement returns
   `implicitDeny` **byte-identical to a real deny**.
3. **It does NOT validate action names** -- a nonexistent action returns `implicitDeny` too, so **a
   TYPO is indistinguishable from a missing grant** (exercised: `s3:ZzzNoSuchActionName9999` ->
   `implicitDeny`).
4. **A resource ARN at the WRONG GRAIN for the action returns `implicitDeny` even for an
   `AdministratorAccess` (`*`/`*`) principal** -- no error, no hint the resource failed to match the
   action's resource type. Measured 2026-09-04 (NFRA_OUTSET-S3, `0.7.0_AE_CloudOps~W`):
   `logs:GetLogEvents` against `...:log-group:/ecs/globgrph/trino:log-stream:*` -> `implicitDeny`;
   the same principal and action against the log-GROUP-grain ARN -> `allowed`. **It fails in the
   UNDER-granted direction and is INVISIBLE against a narrowly scoped principal** -- the normal
   subject of an IAM audit -- where it reads as a correct negative. Modes 1-3's mitigations were all
   in force and none prevents it.

⛔ **AND ONE FALSE-ALLOW MODE: IT MATCHES THE ARN AGAINST THE POLICY'S `Resource` PATTERNS AND NEVER
ASKS WHETHER THE ARN NAMES ANYTHING.** It returns `allowed` for a resource nothing has created. The
four modes above all fail toward DENY, which trains a reader to trust an `allowed`; for a
not-yet-created resource that is the unsafe direction. Measured 2026-10-07 (NFRA_CTLPLN-TO-DELL-1,
`0.7.0_AE_CloudOps~RV`): both Dell principals simulated 10 of 10 `allowed` against
`agentbus-global-dellN-queue.fifo` while ZERO `agentbus-global*` queues existed (`list-queues` empty,
denominator printed). **So an `allowed` proves the PATTERN matches the string you typed -- it does not
prove the resource exists, or that its real name is the one you typed.** Pair every simulation of a
new resource with an existence read of that exact ARN (`get-queue-url`, `head-bucket`,
`describe-table`), and run the simulation AFTER the resource is created, never as its pre-apply proof.
Cost: one read per resource. Non-application: a resource whose existence the same run already printed.

**THEREFORE: ONE `--resource-arns` PER CALL - run the positive control as a SEPARATE INVOCATION -
pass `--context-entries` for any conditioned statement - pass the resource ARN AT THE GRAIN THE
ACTION IS AUTHORIZED ON (`log-group` for `logs:GetLogEvents`, `task-definition` for `ecs:RunTask`)
and run a `*`/`*`-principal positive control beside any deny you intend to act on (a deny you cannot
reproduce against an admin principal is the instrument, not the world) - and NEVER use it to check
whether an action name is REAL** (use `aws accessanalyzer validate-policy`: bogus -> `INVALID_ACTION`
naming the right one; real -> 0 findings).

*A POSITIVE CONTROL IS ONLY A CONTROL IF IT IS RUN IN ISOLATION FROM THE TARGET* -- mode (1) silently
disarms the very control this rule leans on.

### FOUR APPLY-SIDE TRAPS, MEASURED 2026-10-12 (NFRA_IAMROLES202609 round 9, 0.7.0_AE_CloudOps~IR)

Each of these cost a real round-trip or produced a wrong-looking record on a WORLD-risk act. All four are
reads or writes you cannot re-derive at the call site.

**(1) `terraform fmt` WRITES BY DEFAULT.** `-write=false` disables it; **`-check` is what makes it
read-only**, and `-diff` does NOT imply read-only. `terraform fmt -diff <file>`, run only to *inspect*
whether a flagged deviation was mine, silently rewrote the file in the worktree AND the shared tree -- so
three realigned lines sat inside a never-widen act's diff as "added lines" in an act claiming to add
nothing. To decide whether a deviation is PRE-EXISTING: run `-check` at HEAD in the shared tree, compare
the flagged FILE LIST, then compare the flagged HUNK (identical content shifted by your own edit =
pre-existing). Never fix a pre-existing fmt deviation inside an unrelated signed act.
COST: one extra `-check` run. NON-APPLICATION: a commit whose declared purpose IS reformatting.

**(2) A ROLLBACK MUST BE VALIDATED AGAINST ITS CONSUMER, NOT ITS PRODUCER.** `get-role-policy` returns
`{RoleName, PolicyName, PolicyDocument}`; `put-role-policy --policy-document` takes **only** the inner
document. **2 of 13** rollbacks in one round were saved as the envelope -- unreplayable, on acts whose
pairs cited them as the rollback path. The control I had run (*each file equal to a fresh re-fetch*, 7 of
7, canonical `sort_keys`) is satisfied **perfectly** by the wrong shape, because the envelope is exactly
what the API returns. Capture with `--query PolicyDocument`, and guard every read: refuse a dict carrying
`PolicyDocument` with no top-level `Statement`, and refuse zero statements in a policy just read live --
that same shape once made a script print *"the document would be empty -> delete-role-policy"* from a
vacuous read. COST: one `--query` and a two-line guard. NON-APPLICATION: an artifact no command will
replay.

**(3) `RoleLastUsed` ANSWERS "WAS THIS ROLE USED", NEVER "DID A JOB COMPLETE".** On a PERSISTENT EC2
instance the two come apart entirely: the box touches the role continuously between runs. After a
`delete-role-policy` whose pair required a real post-change run, `RoleLastUsed` advanced past the delete
floor within two minutes **while 0 run-record objects had been written** (`gold/.checkpoints/<date>/`,
`gold/meta/`, `watermarks.json`, `silver/` all 0 after the floor). A grader handed only the advancing
timestamp would have called the branch satisfied. Grade a run by **the record it writes**, and read
`RoleLastUsed` only as a liveness floor. It also lags up to 4h, so it is weak in both directions.
COST: one server-side `list-objects-v2 --query "length(Contents[?LastModified>'<floor>'])"`.
NON-APPLICATION: a role whose only consumer is an ephemeral runner that exits per run.

**(4) A SPARSE WORKTREE THAT WILL RUN AN APPLY NEEDS `lib` AND ITS OWN AGENT HOME FOLDER IN THE CONE.**
`safe-apply`'s HALT-gate refuses with `unknown-base` / `SERIAL RESOLVES TO NO KNOWN AGENT` when no
`org/tier*_*/<base>*` matches your serial, and the LGIC naming limb then **BLOCKS** (`LGIC_ENFORCE DEC-6`)
on an absent `lib/opal_naming.py`; `crossbox-deploy-check` WARNs on an absent `lib/devices.py`. All three
fail **CLOSED** and name what they need. **Neither is a verdict about your change** -- and the HALT-gate's
own message is why it behaves this way: *scanning a nonexistent inbox would PASS while a real `[STOP]` to
the real you sits unread.* Fix by widening the cone (`sparse-checkout add lib org/<tier>/<base>`), NEVER
by writing a different serial to make the gate pass.
COST: one `sparse-checkout add` at worktree creation. NON-APPLICATION: a full (non-sparse) checkout.

### THE ON-BOX WRAPPER SET -- moved from CLAUDE.md Rule 26, 2026-08-25

CLAUDE.md Rule 26 still carries the ruling (**the apply runs on the device that owns the work; never
ferry an apply across fabrics**). The tooling it names lives here:

| purpose | path |
|---|---|
| Terraform apply (HALTGT checkpoint) | `.tools/safe-apply.sh` |
| EC2 code deploy | `infra/aws/ec2/safe-ec2-deploy.sh` — **NOT** `.tools/` |
| data-script deploy (DS lane) | `.tools/safe-deploy.sh` |
| EC2 parity check | `infra/aws/ec2/verify-ec2.sh` |
| deploy-completion ledger | `org/critical_paths/change_management/` |

⚠ **Terraform is NOT at the same path on every device.** CLAUDE.md's Git section names
`.tools/terraform.exe`; that file **does not exist on site Z**, where `terraform` resolves on PATH.
**Resolve the binary; never assume the baked path** -- same device-agnosticism rule as every other
hardcoded path.

### WHAT STAYED IN CLAUDE.md, AND WHY
These bind every agent, not just cloud seats, so they did not move: **13** (DS lane ownership of
gold/silver/bronze), **14 / 14a** (the universal commit gate and `safe-commit.sh`), **15**
(`from __future__ import annotations`), **16** (Git Bash utility limits), **17 / 17a / 17b** (the
medallion architecture), **19** (portal worktree stays on DEV). The NEVER block also still carries
the bare-`terraform apply`, bare-`git commit` and `aws lambda update-function-code` prohibitions --
⛔ **and only the first of those three is actually gated** (`never-rules-gate.sh:422`); the other two
are imperatives enforced by nobody. Measured 2026-08-25.

## Pre-flight checklist (before any cloud apply)

For Terraform applies on `infra/aws/terraform/{pipeline}/`:

1. `git tag -l "{pipeline}-v*" | sort -V | tail -5` — find the actual latest tag (CRITICAL: don't assume next version).
2. `terraform plan` — read the diff before applying. If a `-target` is needed because of P3 module S3 artifact gaps, target the specific resource. Note targeting in the RAVC.
3. RAVC1 to CTO + COO with the plan diff for any non-trivial change. For trivial in-place attribute updates (state flips, env var bumps), surface plan + apply in one RAVC if pre-authorized by a TO; otherwise wait for GO.
4. **`.tools/safe-apply.sh` (Rule 18) — NOT bare `terraform apply`.** The HALT-gate checkpoint fires immediately before the irreversible apply: empty inbox passes silently; routine pending message surfaces (sender/subject/age) and requires `HALT_ACK=1` on re-invocation; **STOP-class** message (`[STOP]` or `[HALT]` subject prefix) hard-blocks. Override only via `HALT_OVERRIDE="<reason>"` (audited to `org/halt-gate-override-audit.log`). If the checkpoint library is missing, safe-apply fails closed.
5. After apply, `terraform plan` again for 0-diff verification.
6. Tag `{pipeline}-v{X.Y.Z}`, push `--follow-tags`.
7. RAVC2 with apply confirmation + AWS state check (e.g., `aws events describe-rule`, `aws lambda get-function-configuration`).

**For EC2 code deploys (Rule 12):** write locally → upload to `s3://opal-data-{firm}/code/...` → EC2 pulls from S3 → execute. Never write code directly on a VM. Even ad-hoc diagnostic scripts go through S3. Use `.tools/safe-ec2-deploy.sh` (Rule 7) — never service-specific deploy scripts directly.

**For DS-owned scripts (Rule 13):** `.tools/safe-deploy.sh` runs the commit→push→S3-upload→deployed-MATCH→SSM-dispatch cycle atomically. Pre-push hook auto-fires on `git push` for `data/*/scripts/{gold,silver,bronze}/*.py` paths. Bypass via `--allow-stale --reason "..."` (audited). AE coordinates with DS but DS owns the cycle.

## Compiler tools (run when the situation matches — full table in CLAUDE.md)

CLAUDE.md `## Compiler Tools (comp-*)` table is canonical — read it. AE 0.7-relevant high-frequency subset:

- `comp-pipescript io <script>` — column-gap audit before editing gold/silver scripts
- `comp-pipescript deployed <script>` — verify EC2/Lambda runner has your code (MATCH/STALE/MISSING)
- `comp-pipescript postdeps <script>` — show required post-steps before ad-hoc runs
- `comp-blast <node>` — blast-radius before TO authoring or risky changes
- `comp-iam service <lambda>` — flag missing IAM permissions before deploy (catches s3/secrets/dynamodb/sns/kms gaps)
- `comp-iam gaps` — full cross-reference of all Lambda/EC2 ops vs Terraform policies (run after iam.tf changes)
- `comp-validate <script> --artifact /tmp/<file>` — gold script post-run validation. **READ THE VERDICT, NOT THE EXIT CODE** (CLAUDE.md's own form): `PASS`/`WAIVED` = safe; `ADVISORY` = read the WARNs; **`NO_CONFIG`/`ZERO_CHECKS` = UNVALIDATED — NEVER signal SAFE** (absence is not a pass). *Corrected 2026-08-11: this line read "exit 0 all-pass = SAFE to signal", and **rc IS NOT A DISCRIMINATING ORACLE HERE** — `--lenient` converts both UNVALIDATED verdicts into `return`, i.e. **rc=0**, so an rc-only consumer reads SAFE on an artifact where zero checks ran (`validate_cli.py:593` NO_CONFIG, `:630` ZERO_CHECKS; exercised live: `comp-validate INF_B_01 --artifact <f> --lenient` → **rc=0** while stdout says `ZERO_CHECKS: UNVALIDATED`; same call strict → rc=2). A skill that teaches rc-reading defeats the tool's own fail-closed design — the flag does not have to be malicious, only present. Found at site-Z's certified-instruments rectangle (exercise E3), relayed by `0.0.0_AB_MSTR` 201818Z, re-exercised here before landing.* Protocol: `docs/architecture/COMP_VALIDATE_PROTOCOL.md`
- `comp-routes behaviors` / `comp-routes trace <fn>` — CloudFront / Lambda@Edge debugging
- `comp-registry sync ROW=N` / `--project CODE` / `--all` — REGISTRY-vs-JSON narrative drift detection (read-only default; `--apply` writes under CVO author line)
- `comp-pii audit` — pseudonymized vs cleartext field audit

After ANY `iam.tf` change → `comp-iam gaps`. After any new boto3 call → `comp-iam service <lambda>`.

## Commit + deploy hygiene

**Every commit via `.tools/safe-commit.sh` (Rule 14a):**
```bash
.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" -- <pathspec>
```
Wrapper aborts if staged index contains files outside declared pathspec (concurrent-agent contamination guard). `--force` bypasses but audits to `org/git-author-override-audit.log`. Never use bare `git commit -a`. Three CLASS-C sweep incidents 2026-04-27 prove the structural guard is required. **Concurrent-agent contamination is common during multi-agent MCP windows** — when safe-commit aborts on contamination, run `git reset HEAD -- <extras>` to unstage strays, then retry. Feature, not bug.

**Every `.py` edit via `.tools/commit-gate.sh <files>` BEFORE `git add` (Rule 14):**
- `python -m py_compile`
- `.tools/ds-precommit-check.py` — AST undefined-name scanner + silver `coerce_silver_ids()` enforcement + Rule-15 `from __future__ import annotations` check
- `ruff check --target-version py39` (pin 0.15.11)

All three must exit 0. Catches Class A latent bugs at commit time vs SSM dispatch.

**Every DS-owned gold/silver/bronze deploy via `.tools/safe-deploy.sh` (Rule 13):**
Commit→push→S3-upload→`comp-pipescript deployed` MATCH→SSM dispatch (or RAVC2 ACK to AE for PROD). Pre-push hook auto-fires on `git push` for `data/*/scripts/{gold,silver,bronze}/*.py`. Bypass via `--allow-stale --reason "..."` audits to `org/safe-deploy-bypass-audit.log`. AE coordinates with DS but DS owns the cycle.

**Every Terraform apply via `.tools/safe-apply.sh` (Rule 18):**
HALT-gate checkpoint immediately pre-irreversible-apply (see Pre-flight §4). Bare `terraform apply` is BANNED.

**Every EC2 deploy via `.tools/safe-ec2-deploy.sh` (Rule 7):**
Tracks deployments in `EC2_MANIFEST.json`. Never run service-specific deploy scripts directly.

## Failure handling

- TF state drift: investigate with `terraform refresh` first; never `terraform state rm` without surfacing.
- Apply error mid-run: capture full stderr, RAVC2 to CTO + COO, do not retry blindly.
- Pre-commit gate fails on a Python edit: read the gate output, fix the issue, re-stage, NEW commit (never `git commit --amend` after a hook failure).
- `record-terraform-deploy.sh` tooling failure: known issue (CHANGELOG.json writer + owned-paths-hook on Andrew identity); reset the spurious source-map.json changes and surface in RAVC.
- **HALT-gate `STOP`-class blocks `safe-apply`**: read the inbox message in full, route the requested action (or coord with CTO if unclear), then `HALT_OVERRIDE="<reason>"` only if Andrew/CTO/MSTR explicitly clears.
- **`safe-commit.sh` aborts on contamination**: `git reset HEAD -- <extras>` to unstage the concurrent-agent files (DS/COO/CVO commonly stage own session logs in the shared index during multi-agent MCP windows), then retry. NOT `--force` unless wrapper bypass is genuinely needed (audited).
- **Inbox watcher `AUTO-RESPAWN-INTERRUPT-LOST` VERDICT**: run **`/watcher rearm`**. It `TaskStop`s the Monitor, then kills the surviving bash **CHILD** (`TaskStop` does NOT reap it — arming on top of the survivor makes two streams race the same `mv` and splits your inbox at random), then re-arms under the **Monitor tool**.
  **⛔ DO NOT relaunch `inbox-watch.sh ... stream` under Bash `run_in_background` — `org/XXX.md` Step 1b C BANS it: the Bash tool only notifies on EXIT, stream mode NEVER exits, so YOU GO SILENT FOR THE SESSION.** *(This line instructed exactly that until 2026-07-31. It was the most dangerous kind of wrong — scoped, specific, and it even warned you off a worse variant (`&`), so it read as authoritative. An AE following it landed in the deaf state while every reachability probe still read REACHABLE: the remedy MANUFACTURED the fault it was curing, the same anti-correlated shape as the orphan watcher. Caught by `0.7.0_AE_CloudOps~B`, who declined to absorb it.)*

## Operating doctrine pointers (LD cycle binding)

These ledger decisions bind AE 0.7 operating discipline. Cite in commit messages where relevant.

- **LD-0034** — unified `opal-agent-comms` broker + ws-rooted `inbox-watch` PATH wrapper for all serials (ws + CL). Legacy `feature_clb/org/mcp/cl-inbox-watch.sh` retired.
- **LD-0049** — Concurrency cap 8→16 raise; ceiling-not-target + reallocation-before-spawn discipline.
- **LD-0066** — 3-way /charter split: /ws-charter (ws CTO) + /cl-charter (CL CTO) + /mstr-charter (MSTR rare-use). Workers `/work` per LD-0072.
- **LD-0072** — `/work` skill body as universal Tier-2/3 worker-loop body; 20m cron cadence; workers self-classify blockers + MCP lane COO with `[BLOCKED-ASK]`.
- **LD-0082** — Deterministic loop arming at session start; primary cron arming per role-class.
- **LD-0084 §2** — Sibling-PRD pattern for deferred sub-deliverables (e.g., `.003` comp-graph deferred to Phase 1 first-Lambda land).
- **LD-0090** — ALWAYS-PROCEED operating principle (Constitution Art. XVI): ALWAYS proceed / NEVER delay / 1-turn-no-response = proceed. Sovereign-class reservation (S3/S4) preserved.
- **LD-0113** — Workspace-shared skills sync via `sync-skills-to-worktree.sh` (ws → CL idempotent + sha256 drift detection).
- **LD-0115** — Concurrency cap 16→20 raise (2026-05-27); cross-fabric combined counting per Constitution Art. XV.
- **LD-0116** — Chain-of-command edict (2026-05-27): **Tier-2/3 workers shall NOT MCP MSTR directly**. Workers route to lane COO; T1 routes upward. MSTR bounces violations + CCs responsible T1. Enforced structurally via `/work` SKILL.md §4a.1 ladder.

## Current pipeline + bucket inventory (snapshot 2026-05-27)

**Buckets AE 0.7 owns / operates:**
- `opal-data-bd` — Black Diamond (49 Financial); SSE-S3
- `opal-data-inf` — Inflection; SSE-S3
- `opal-data-demo` — Demo tenant; SSE-S3
- `opal-data-cottonwood` — Cottonwood firm (post-LD-0049 mid-May onboard)
- `opal-data-imo` — FIND_INSURE IMO research (2026-05-27 today; `imo-pipeline-v0.1.0`); SSE-S3 baseline + SSE-KMS upgrade pending `imo-pipeline-v0.X.0` per PRD v0.4 §3.1 (PII-scope prefixes)
- `opal-data-mdpf` — Partner ETF Ownership
- `opal-data-etfs` / `opal-data-aaii-v2` / `opal-data-pm` — sibling pipelines
- `opal-313476888478-lambda-artifacts` — Lambda packaging bucket (root)

**Terraform pipelines AE 0.7 owns:**
- `infra/aws/terraform/inf-pipeline/` — Inflection
- `infra/aws/terraform/bd-pipeline/` — Black Diamond
- `infra/aws/terraform/mdpf-pipeline/` — MDPF
- `infra/aws/terraform/imo-pipeline/` — FIND_INSURE (today)
- `infra/aws/terraform/shared-infra/` — KMS / OAI / cross-pipeline shared
- `infra/aws/terraform/portal-auth/` — Portal auth + Lambda@Edge. **⛔ NOT Cognito — Opal does NOT use Cognito.** Auth is custom RS256-signed JWTs issued at login, held client-side as `accessToken`, sent as `Authorization:` on every API call (`0.7.0_AE_CloudOps/prompt.md:112`). *Corrected 2026-07-31: this line read "Portal Cognito + L@E" and contradicted the AE prompt's flat prohibition on writing Cognito into a portal/trade auth context — a launch-loaded skill asserting the wrong auth primitive.*
- `infra/aws/terraform/orion-pipeline/` — Orion JWT pattern
- `infra/aws/terraform/smartx-pipeline/` — SmartX REST integration

**Secrets Manager namespaces AE 0.7 operates:**
- `orion/jwt/*`, `orion/credentials/*`
- `smartx/jwt/*`, `smartx/credentials/*`
- `find-insure/bright-data/*`, `find-insure/lusha-ai/*`, `find-insure/job-board/*` (today)
- `brightdata-api-key` (root; copied to find-insure/bright-data/ per Andrew AskUserQuestion choice (a) 2026-05-27)

**KMS keys (post-LD upgrade):**
- `find-insure-data-key` (PRD v0.4 binding; AE provisions in `imo-pipeline-v0.X.0`; key-policy = `find-insure-lambda-role` decrypt-grant only at v0.1; annual rotation enabled)

You're cleared. Move fast within the rails.
