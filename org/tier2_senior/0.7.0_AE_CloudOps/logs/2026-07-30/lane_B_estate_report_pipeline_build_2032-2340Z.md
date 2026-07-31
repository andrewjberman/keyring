# ~B lane: the ESTATE REPORT pipeline, built and exercised -- five defects, one family, none predicted -- 2032-2340Z

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE
**Serial:** `0.7.0_AE_CloudOps~B` (fresh session, PID 25616, Monitor `bydmt7exh`, session 339beee1)
**Task Order:** none on disk -- Andrew-direct at the CVO terminal (rulings 1-3) and at MY terminal (rulings 4/4a)

## Arc

Startup, then a two-hour build of the daily semantic-evolution pipeline Andrew ruled at ~2135Z,
then acceptance -- which is where the session actually earned its keep.

1. **Startup.** `/watcher` armed (prefix resolved `/cygdrive/c`; three `inbox-watch.sh` processes
   found for my base family, NONE mine -- base 33920 and `~A` 25432 are live peers, so I ran the PID
   discriminator instead of the "fresh session => orphan" inference and killed nothing).
   `TaskOutput(bydmt7exh)` = running. XXX.md 1b: A.2 rc=0/0 findings; **A.3 95/95 bare-resolve AND
   the mandatory EXERCISE half** (a forwarder produced its own banner); D wired; E set; F = zero crons.
2. **Held on an instruction collision, deliberately.** Andrew's word at my terminal was "await my
   further instruction, do not address any other work"; CVO relayed an Andrew-direct dispatch
   assigning me the spec. Two sovereign instructions, one later. I ACKed, started nothing, and
   surfaced the collision rather than resolving it in the direction that let me work. Ruling 3
   cleared me. **Zero work product existed at that point and I said so; consistency there is what
   made the hold worth anything.**
3. **Spec -> CVO approval (C1, C2) -> build -> apply -> acceptance -> five defects -> fixed.**

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | `gaps` | PASS (advisory) | Run as the AE role-minimum after the `iam.tf` change; 17 missing / 292 deny-present / 30 services estate-wide, none in this module. **Explicitly NOT the verification** -- `opal-estate-report` is a NEW bucket and comp-iam models `(action)`, never `(action, resource)`. Rule 22a applied instead. |
| `aws iam simulate-principal-policy` | A5 pair, x2 rounds | PASS | The real IAM instrument. ONE `--resource-arns` per call, positive control as a SEPARATE invocation. `daily/*` allowed, `adjudicated/*` implicitDeny. **The allow side doubles as the action-name oracle** -- a typo'd action denies BOTH, so one allow proves `s3:PutObject` is a real string. |
| commit-gate | 5 invocations | PASS 5/5 | py_compile + AST + ruff on every `.py` touch. |
| comp-surface-check | auto in safe-commit (x8) | PASS | No critical surface; 6 surfaces / 3 SEV1 screened each time. |
| comp-pulse risk-reflex | auto in safe-commit (x8) | PASS, and it FIRED usefully | Cited `CLAUDE.md:81` on the `iam.tf` commits -- which is what sent me to run `comp-iam gaps` as the role minimum. Denominator printed every time (1 file vs 1622 danger nodes). |
| terraform validate | x4 | 1 FAIL -> PASS | **The FAIL is the valuable one:** my comment documenting an escaping rule contained a literal percent-brace inside the heredoc, so Terraform parsed it as a directive. The note about escaping broke on escaping, and the gate caught it exactly where care could not. |
| terraform plan | x6 | PASS | Including the one that read `will be updated in-place` on a `user_data` change -- see defect table. |
| comp-which / comp-grep | not run | SKIPPED | Every search this session was a known-path `Read` or a `grep` over files I had just authored; nothing needed routing. Recorded rather than left blank. |

**What worked:** the risk-reflex citation routing me to `comp-iam gaps`, and `terraform validate`
catching a self-inflicted parser bug pre-apply.
**What failed:** nothing in the tools. Every failure this session was mine, and every one was caught
by a control or by exercise -- not one by care.
**Gap found:** none new. The `comp-iam` insufficiency for a new bucket is already law (Rule 22a) and
behaved exactly as the law describes.

## Work Completed

New module `infra/aws/terraform/estate-report/` (19 resources), orchestrator Lambda, EC2 runner job.
EventBridge Scheduler 09:00 America/New_York (DST-native, **created DISABLED**) -> fire-and-forget
orchestrator (timeout 60s: StartInstances, return) -> EC2 autostart via systemd oneshot -> scan ->
compile -> Kimi -> write S3 -> self-stop, with a boot-armed 90-minute ceiling.

| Commit | What |
|---|---|
| `3acb8531c6` | Andrew rulings 4/4a recorded verbatim + broadcast same turn |
| `5192934890` | SPEC, CVO-approved with conditions C1/C2 |
| `ce3e047bda` | the build |
| `43edeabd83` | C3 ARN-pin via separate role_policy; A11; resolver seam |
| `d69df477f2` | registries + core doc, post-apply |
| `4e69b1dbc5` | contract v2 (manifest-first) |
| `afc1ccc376` | dropped my own Deny on CVO's ruling |
| `d9a7a005b3` | supervisor journal persistence |
| `ce5f0c7e45` | ROOT CAUSE: NoRegionError + systemd escape restored |
| `6d63cfe530` | EC2_MANIFEST id-churn note |

Tag `estate-report-v0.1.0`. Pushed (one rejected push -> `git pull --no-rebase` -> re-push; NEVER#7
respected).

## THE FIVE DEFECTS -- one family, every one found by EXERCISE, none by prediction

| # | Defect | Why no instrument caught it |
|---|---|---|
| 1 | dead-man's switch `enable`d but never `start`ed on the creation boot | plan/apply/0-diff all green; the box ran 10+ min with `shutdown --show` empty. **The guard was armed by the mechanism it exists to protect against.** |
| 2 | volatile journald on a self-stopping host | the record of why a run failed died with the run that failed |
| 3 | manifest written LAST -> a dead run left NO ledger entry | CVO's reader detects UN-FLIPPED days; a dead day is ABSENT, which was not a state. **The entry that would be alarming is written by the process that died.** |
| 4 | CVO's absence anchor sat inside my writable prefix | nobody edited the policy -- **a correctly-scoped grant was widened by someone else putting something valuable inside its blast radius** |
| 5 | `NoRegionError` at module import | python died one line ABOVE the first line that records anything, so contract v2 recorded nothing |

**Two more, self-inflicted, both caught before they mattered:** I halved a systemd `%%` escape after
reasoning about the wrong layer (Terraform), and systemd then ate every specifier -- and **the S3
upload SUCCEEDED, so only the garbage KEY betrayed it**. Then my comment about that escape broke
Terraform on the same character class.

**And one trap caught in a plan, not after:** `user_data_replace_on_change` defaults to FALSE in AWS
provider v5, so a `user_data` fix plans as "updated in-place" -- Terraform rewrites the attribute,
reaches a clean 0-diff, earns a green tag, and **the running box never executes the new script.**
A fix recorded as applied and never executed, behind a PASSING 0-diff.

## Verification

- **A5 boundary EXERCISED AS A DENY**, twice (post-apply and post-replacement), separate invocations.
- **A12 verified on the APPLIED policy**, because the plan rendered `policy = (known after apply)` and
  **structurally could not prove the approval condition it was asked to prove**.
- **`user_data` decoded post-apply** (`describe-instance-attribute`) -- the plan shows only a 40-char
  hash. 5/5 properties confirmed on the rendered artifact.
- **A10 with a positive control on the same file** (0/0/0/0 banned; scheduler 2, instance 2, 522 lines).
- **A11 closed BY ARTIFACT**: `manifest/2026-07-30.json` `status=FAILED`, named `SecretUnset`, window
  `13:00Z -> 13:00Z` against `started_at 23:35:14Z` -- **C1 proven inside a single document**.
- Artifact deploys md5-verified against ETag, both rounds. CVO independently re-pulled and validated.

## Current State

The chain RUNS END-TO-END on the real path: orchestrator -> boot -> autostart -> run -> record ->
self-park. A5/A6/A10/A11/A12 closed and exercised; C1 confirmed in a live artifact. Schedule
**DISABLED**. Instance `i-09fa5115b3282d6ea`, stopped. Zero crons armed.

**A2/A3/A4/A7/A8/A9 are NOT graded** -- they require a real report, which requires the PAT. Refusing
to grade them off a refusal run is the same discipline as "correctly built and unexercised."

## Blockers

**Both are human-reserved and neither is mine to clear.**
1. **GitHub PAT value** -> `estate-report/github-token` (created EMPTY on purpose: writing it through
   Terraform puts a live credential in S3-backed state, outliving every rotation). At Andrew.
2. **Retention ruling** on `opal-estate-report`. No lifecycle rule on report prefixes, deliberately --
   a rule that expires a governance record is the default nobody notices until the record is needed.

## Next Steps

1. **[Andrew]** PAT value; then the first real report completes the battery.
2. **[Andrew]** Retention ruling, or ratify "no rule" as the standing answer.
3. **[Andrew, after a human reads a real report]** Flip the schedule to ENABLED. Go-live is
   deliberate, not a 09:00 ET surprise.
4. **[me, on the PAT landing]** Run A2/A3/A4/A7/A8/A9 and hand CVO the completed battery.

## The one thing worth carrying out of this session

**MOVING A RECORD OUTWARD DOES NOT BOUND THE FAILURE, IT ONLY RELOCATES THE FRONTIER -- and the only
way to find the new frontier is to run the thing.** Five instances of one principle in one evening,
found by two agents who spent that same evening writing the principle down. Knowing a failure mode
by name demonstrably does not immunize you against building it.
