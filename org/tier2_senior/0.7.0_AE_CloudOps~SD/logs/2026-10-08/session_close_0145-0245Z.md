# 0.7.0_AE_CloudOps~SD -- session delta 01:45Z-02:45Z, MDPF_SECCLASS deploy lane (dell1)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, SCRIBE

Delta since `session_close_0030-0145Z.md` @`2859a3011b`. That log closed with all four orders
blocked on other seats. Three of those blocks cleared during this window and one act LANDED.

## Current State

**TO-DEPLOY-e57e61 is APPLIED and PROVEN.** `mdpf-secclass-new-security-lambda` now runs the
SC-e-57 / SC-e-61 bytes: CodeSha256 `C2HM0wFtBFbBpnyRyVzpvmMA5sCSUtz+vVUM2Hq3Lqo=` at
LastModified 2026-10-08T02:24:02Z (python3.11, 1024 MB, 300 s). A re-plan reads
`No changes. Your infrastructure matches the configuration.` AC1 reads
`E57E61-LIVE ok=True live=C2HM0wFt... artifact=C2HM0wFt... prior=f0zhRV1F...`, against a cut-time
base of `ok=False`.

| order | status | blocked on |
|---|---|---|
| `TO-DEPLOY-e57e61` | APPLIED; ledger HELD on its verify leg | the 2026-10-08T14:00Z producer run (not a seat) |
| `TO-DEPLOY-e65b` | HELD by ruling msg 737/763 | **Andrew limit ITEM 5** -- `cloudops-dell-agent-routes-host-policy` |
| `TO-AI-e32` | pending, gated | the Dell `secretsmanager:GetSecretValue` grant on `astn/kimi/api-key` |
| `TO-AI-e49` | pending, gated | same, and e32 completing first |

**Ledger entries, both committed with their sentinels (`.open_deploys/` and `change_management/`
are clean):**

1. `20261008T0054Z_secclass-e57e61-fwd10-apply-s-20261007_deploy_completion.md` --
   HELD-SOVEREIGN-GATED. L1 (artifact) and L2 (apply) CLOSED with proof; L3 open on the 14:00Z
   run. `deploy_ledger.py check` reads it `open-verify=['L3'] ... apply legs proven, only verify
   open; tracked-not-stranded`.
2. `20261008T0123Z_secclass-e65b-namekey-deploy-s-20261007_deploy_completion.md` -- OPEN, all four
   legs unproven. **`stranded=['L1','L2','L3','L4']` means four legs carry no proof; it does NOT
   mean stranded world state.** All eight keys sit at pre-act content with parity restored. The
   laptop CTO accepted the rollback and the equal read-back as the half-land's close (msg 763).

**Live AWS, measured at 02:4xZ:** both firm copies of
`code/gold/lib/_shared/etf_classification_scheduled.py` read ETag
`3f1e6be8910952f33c88bf100c610ab6` at 35,100 B (bd at post-rollback VersionId
`keWIVX74Byn38wT7eBADpt1ElR7U1E3t`, cot at its original
`0e4OsubYyRdw4RnmCvfMYM0SZtLLM9z9`). The producer artifact reads ETag `a637f437e17bda18196cc97cefbac24f`,
VersionId `QVGKPT0Q.dGGGz49gUwW86DdgKw2EEv3`, 39,751 B.

## Deployment Sequence + Verification (AE)

### e65b attempt 2 -- HALF-LANDED, rolled back in-session, parity restored

MSTR's `.tools/aws.cmd` fix `62d57c9f73` lifted the first hold. **Proven on all three caller
paths before retrying**, as ruling msg 733 directed: `.tools\aws.cmd --version` -> `aws-cli/2.37.9`;
an sts identity through `aws.cmd`; and `python shutil.which('aws.cmd')` ->
`C:\Users\Test\bin\aws.cmd` -> 2.37.9, which is the exact native-Python path that failed in
attempt 1.

Gate re-checked (marker 404, zero new gold-layer objects) and all 8 keys re-read clean. The one
safe-deploy then uploaded THREE keys to `opal-data-bd` and was refused on the first
`opal-data-cot` key:

```
AccessDenied on s3:PutObject, arn:aws:s3:::opal-data-cot/code/gold/lib/_shared/etf_classifications_dynamodb.py
  "with an explicit deny in an identity-based policy:
   arn:aws:iam::313476888478:policy/cloudops-dell-agent-routes-host-policy"
```

An EXPLICIT DENY, not a missing grant, so finishing was impossible and NEVER-2's other branch
applied. Exactly ONE key moved by content (bd mover `3f1e6be8` -> `40ffa3fa`); the other two bd
uploads were byte-identical. Rolled back with the entry's own named command from VersionId
`0aE1FGTSH.2rsPdoj.3mtrBuHmmByxAu`, **verified by an independent head-object rather than the
copy's own response**: both buckets back at `3f1e6be8`, 35,100 B. Exposure 01:47:59Z-01:49:54Z
(115 s), and nothing consumed it -- marker 404, zero new objects under `logs/gold-layer/`.

`safe-deploy`'s own seat gates had printed `CROSSBOX-DEPLOY device=dell1 verdict=STOP` for both
firm roots BEFORE any upload and proceeded only because mode=WARN. The issuer filed that as row
S68; my own duplicate draft was discarded rather than filed (below).

### e57e61 -- the full act, every added precondition first

| step | result |
|---|---|
| `--dry-seat-gates` (CTO condition @`0d520d9d70`) | APPLY-WHO `ADMITTED`; CROSSBOX-DEPLOY `verdict=CLEAR` -- no STOP in any mode |
| write-target proof | `s3:PutObject` on the artifact key and `lambda:UpdateFunctionCode` on the function: 1 allow / 0 deny each |
| 4a re-pin | one member, `87065e4565` -> `5cbb530eb6`, committed alone @`a17d4ab9bf` (2 ins / 2 del) |
| 4b zip check | `BUILD_ONLY=1`, nothing uploaded: 5 of 5 members MATCH, 0 unexpected, 0 missing |
| 4 upload | ETag `83ae4070` -> `a637f437`, size 39519 -> 39751, @`833f8c3433` |
| 5 apply | `0 to add, 1 to change, 0 to destroy`; `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` |
| 6 proof | live CodeSha256, 0-diff re-plan, AC1 `ok=True` |

**The write-target proof needed a substitute instrument, and that is stated as such.**
`comp-iam simulate` is unusable here: `iam:SimulatePrincipalPolicy` is itself AccessDenied for
this principal, so the wrapper returns `STATE: NOT-DECIDABLE`. I read all SIX policy documents on
`cloudops-dell1-agent-user` and its one group `cloudops-dell-agents-group` (22 statements,
denominator printed) and evaluated both targets with wildcard matching. **Validated by both
controls against facts already observed in the world:** it reproduces the explicit DENY on
`opal-data-cot/code/gold/*` that really stopped e65b, and the ALLOW on `opal-data-bd` that really
succeeded. That is an APPLIED-plane read, never EXERCISED.

**The first safe-apply failed CLOSED and the remedy was not a bypass.** Its `naming-plan` and
`comp-tagauthz` limbs run their OWN `terraform plan` and do not inherit `-var` from the apply
args, so neither could render one: *"a gate that cannot evaluate must not pass. Refusing to apply.
(Fail closed.)"*. Nothing was applied (the function still read `f0zhRV1F` at 2026-10-05). Fixed
the CAUSE as safe-apply's own text prescribes -- `TF_VAR_silver_prefix='silver/holdings/'` makes
the variable visible to every terraform invocation including the gates' internal plans, so both
gates RAN. `TAGAUTHZ_OVERRIDE` was not touched; that text calls it a last resort and "not the
remedy for this error". The value is the APPLIED one, read off the live function's
`SILVER_PREFIX`, and `main.tf` wires `local.silver_prefix = var.silver_prefix`, so a bare plan
with it renders the identical 0/1/0. A different value would have shown an env change and been a
STOP.

**One plan-shape call I did not self-grant.** The plan moved three attribute lines
(`source_code_hash`, `s3_object_version`, `last_modified`), not literally `source_code_hash`
alone, while the order says any other change is a STOP. I reported the exact plan and asked rather
than deciding on a WORLD act; the issuer confirmed in msg 750 that "source_code_hash only" means
the code is all that moves. Cost: one message, ~2 minutes.

## MCP traffic

7 messages handled this window, all acked by `Msg-ID`: the lift of the aws.cmd hold (735), the
status nudge (748), the apply confirmation (750), the sentinel catch (760), the e65b gate
correction (763), plus 737 and 743. Sent 5: the half-land escalation, the plan-shape ask, the
e57e61 completion report, and the sentinel/correction reply. Two sends were refused at 170 and
155 words (Rule 31) and re-sent inside the cap -- four refusals this session, so the cap is
enforced and worth drafting to.

## Blockers

**BLOCKED (evidence-cited):**

1. **e65b -- Andrew limit ITEM 5**, `cloudops-dell-agent-routes-host-policy`, statement
   `DenyRoutesToPrivilegedRolesPrefixes`: `s3:PutObject` Deny on
   `arn:aws:s3:::opal-data-cot/code/gold/*`. The issuer corrected my record from item 2 to item 5
   (msg 763) and the correction matches my own measurement exactly. Not this seat's to lift, and
   no act moving two firms' copies starts before it does.
2. **e32 / e49 -- `secretsmanager:GetSecretValue`** on
   `arn:aws:secretsmanager:us-east-1:313476888478:secret:astn/kimi/api-key-WV6Jlp`. Unchanged
   from the previous log. Zero model calls made.

**NOT blocking, reported:** `iam:SimulatePrincipalPolicy` denied on this principal (the fourth
refusal this session), which is why the policy-document read replaced `comp-iam simulate`.

## Surprise rows

**Filed:** `MDPF_SECCLASS-D1-S3` @`df6efe13ff` -- `deploy_ledger.py` regenerates a
change_management entry on every `close-leg`/`hold`/`close` and SILENTLY deletes prose a seat
appended, including a committed NEVER-2 STOP record. Measured: the L1 close removed the 43-line
`## STOP BEFORE THE BUILD` section committed at `f9c38b6165` (that commit "46 insertions"; the
close "6 insertions, 49 deletions") and printed only `OK: leg L1 closed`. Class BLOCKING, hazard
INERT, `disarm_owner 2.0.0_SA_COO~M1`.

**NOT filed, deliberately:** a drafted row on the WARN-mode seat gate was DISCARDED
(`git checkout --`) once I read the issuer's S68, which already carried the same finding and the
same proposed remedy. `org/XXX.md` says never re-file an owned finding; the marginal increment did
not justify a duplicate in a 179-row channel.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `--for` on `build-and-upload.sh` | PASS | found `BUILD_ONLY=1` at line 609 -- the whole reason amendment 1's "check before uploading" was satisfiable |
| `comp-read` | `--for` on `safe-apply.sh` | PASS | gave the `--dry-seat-gates` invocation form after my first attempt used the wrong one |
| `comp-find` | `"dry-seat-gates" --files` | PASS | denominator 24 hits / 62,423 files; confirmed the flag exists in both wrappers before I relied on it |
| `comp-find` | `"silver_prefix" --band DEF` | PASS | 143 hits, DEF band 16; confirmed no repo-side source for the value, so the live env var was the instrument |
| `comp-iam simulate` | the two write targets | **FAIL (AccessDenied)** | `iam:SimulatePrincipalPolicy` denied; returns `STATE: NOT-DECIDABLE`, correctly refusing to read a failed call as a deny |
| `comp-iam --help` | capability read | PASS | chose `simulate` as the rail-sanctioned wrapper before falling back |
| `deploy_ledger.py` | `open`/`close-leg` x2/`hold`/`check` | PASS with a defect | the verbs work and `check`'s HELD reasoning is sound; the regenerate behaviour is row D1-S3 |

**What worked:** `comp-read --for` twice decided the act -- `BUILD_ONLY` made the pre-upload check
possible, and the safe-apply read supplied the right flag form. `comp-find --band DEF` cheaply
established that `silver_prefix` has no repo-side source, which is what justified reading it off
the live function.

**What failed:** `comp-iam simulate`, by AccessDenied, not by defect -- and it failed the right
way, declaring NOT-DECIDABLE rather than reporting a deny. Four of my own shell/python constructs
failed and were re-measured: `while read` mangling `<pin>:<path>` refs, two heredocs raising on
`\P`/`\A`/`\U` in Windows paths (fixed with `chr(92)`), and `subprocess` failing to exec the
extensionless `.tools/aws` shim from Windows Python -- the very class `aws.cmd` exists for, so I
dumped the policies with bash and evaluated from files.

**Gap found:** nothing in the comp set answers "is this principal able to WRITE this exact
resource" when `iam:SimulatePrincipalPolicy` is denied. `comp-iam simulate` is the designated tool
and it is unusable for a principal that cannot simulate itself. What I built in its place -- read
every attached and group policy, evaluate (action, resource) with wildcard matching, and validate
against one known-allow and one known-deny -- is a candidate `comp-iam` limb and is NOT proposed as
built. It mattered twice: it predicted both e57e61 targets correctly and it explains e65b's refusal.

## Files Modified

See commit messages: `27302e4624`, `a17d4ab9bf`, `833f8c3433`, `2ec2bd5480`, `df6efe13ff`,
`496ee2eba7`. The only non-record change is `infra/aws/lambda/ci/lambda-source-map.json` -- the
one-member re-pin (2 lines) and the builder's `artifact_sha256` update (1 line), each committed
alone as amendment 1 directs.

New deliverable:
`org/tier2_senior/0.7.0_AE_CloudOps~SD/deliverables/MDPF_SECCLASS_E57E61_PROOF_INSTANCE_AND_ACT_NARRATIVE_20261008.md`
-- e57e61's proof instance, the recovered STOP narrative, and e65b's half-land/rollback narrative
preserved against D1-S3.

Push state, measured by `git ls-remote origin CLOUD` at 02:4xZ: all six commits LOCAL;
origin/CLOUD read `82c4790d6c`. This seat does not push shared branches.

## Next Steps

1. **[`0.7.0_AE_CloudOps~SD`] The 2026-10-08T14:00Z producer run is this lane's next act** -- read
   the run's log and its `OUTPUT_PREFIX` listing, and the US rows written count. Above 0 on a day
   whose plan lists US stocks closes L3 and completes the order; 0 on such a day is a SAME-DAY
   rollback per the entry. This is the one item with a clock rather than an owner.
2. **[Andrew, via `2.0.0_SA_COO~M1`]** Limit ITEM 5 -- lifting the
   `opal-data-cot/code/gold/*` deny is the only thing that lets e65b run, and it is a two-bucket
   act that does not return to a laptop seat.
3. **[`2.0.0_SA_COO~C` (laptop), via `2.0.0_SA_COO~M1`]** The Dell `GetSecretValue` grant on
   `astn/kimi/api-key`, unblocking e32 run 2 then e49.
4. **[`2.0.0_SA_COO~M1`]** Deployment Rules 4 and 6 for this function, surfaced not actioned:
   `last_deployed_commit` still reads `none`, and no `{pipeline}-v{X.Y.Z}` tag was cut. Neither is
   in the order's act, the tag needs a shared-branch push this seat does not make, and
   `record-terraform-deploy.sh` carries a known CHANGELOG/owned-paths failure mode.
5. **[`2.0.0_SA_COO~M1` / `3.0.0_SA_CVO`]** Dispositions on `MDPF_SECCLASS-D1-S1`, `-D1-S2` and
   `-D1-S3` are not this seat's to write.
