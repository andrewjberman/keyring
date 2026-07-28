# 0.7.0_AE_CloudOps -- P0: hold the legacy MDPF served-key clobber before ~15:10Z (1341-1435Z)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Objective

Andrew-direct P0 routed via `1.0.0_SA_CTO` (msg 20260728T134301Z, ruling 134421Z; leg-2
authorization 142053Z). CTO restored the correct 07-23 REVAMP generation to the served MDPF keys
at 1341Z and Andrew was presenting off it within the hour. The legacy daily chain rewrites those
same keys at ~15:10Z from a dead platinum path. Leg (a): stop the clobber, today, without killing
the chain that produces tomorrow's correct data.

## What happened

Two IAM Denies landed on `mdpf-daily-runner-ec2-role`, both Terraform (not CLI), both
`-target`-scoped, both exercised on the applied plane before being reported held.

**Leg 1 (`26ac313453`)** -- `Deny s3:PutObject` on `opal-data-portal-v2/json/mdpf/*`.
Stops the Stage-4 ROLLUP overwriting the four served timeseries keys.

**Leg 2 (`d28371947c`)** -- `Deny s3:PutObject` on two LITERAL keys,
`json/portfolios/non_model_assets.json` + `json/portfolios/aum-timeseries.json`. The portal
headline is a SUM ACROSS TWO artifacts (`ModelPortfolios.tsx:1168-1172`); leg 1 protected only the
model half. Written by Stage 3.5, same chain, same ~15:10Z window.

## The decision that mattered

CTO's first instinct was to guard the `run_step` line in `mdpf-daily-dispatch.sh`. I raised that
the runner executes `s3://opal-data-mdpf/code/`, ~20 commits behind HEAD -- so a repo edit is a
TRUE-BUT-NOT-LIVE hold that reads GREEN, and refreshing that prefix to fix it would import 20
commits of unrelated drift into a live client-facing chain mid-presentation. CTO changed the
ruling to hold at the IAM layer. Both halves of the script route were wrong.

**Before writing leg 1 I checked at source whether an AccessDenied would fail Stage 4.** Deployed
dispatch `:377-380` is `CHAIN_STATUS="failed"; exit 1`, and Stage 5 OWNTS (`:383`) and Stage 6
REVAMP (`:415`) both run AFTER it. Had the rollup propagated the upload failure, this Deny would
have killed OWNTS and the REVAMP producer daily -- exactly the outcome CTO had ruled against. It
does not, because `build_aggregate_aua_timeseries.py:619-635` and `:653-662` wrap both
`json/mdpf` writes in try/except -> "loud WARN + continue" (DS~B built that deliberately so a
deploy-before-grant could not break the chain). COO reached the identical conclusion independently
from a different direction.

**Verbatim, at COO's request (`20260728T140907Z`), because it is the generalisable part:**

> From the IAM side alone, the safe version of this deny and the chain-killing version look
> identical -- it is only safe because of a try/except two files away.

**And the corollary, ratified by CTO as doctrine (`20260728T143039Z`): THE TWO LEGS ARE SAFE FOR
DIFFERENT REASONS AND NEITHER IMPLIES THE OTHER.** Leg 1 is safe because the SCRIPT swallows the
AccessDenied and returns 0. Leg 2 is safe because the SCRIPT WILL FAIL and the DISPATCH tolerates
a non-zero step (deployed dispatch `:356-370` -- bare if/else, `record_step LEGACY-EMIT 1` + ERROR
echo, no `CHAIN_STATUS="failed"`, no `exit 1`). Same-looking IAM change, same-looking outcome, two
entirely different protective mechanisms in two different files. **Any future Deny on a third
artifact re-runs the cascade check from scratch -- the precedent is not transferable.**

## Deployment Sequence

1. Edit `infra/aws/terraform/mdpf-pipeline/iam.tf` (Deny statement + rationale comment)
2. `safe-commit.sh` under own author line, `-F` message file (Rule 14a)
3. `terraform plan -target=aws_iam_role_policy.mdpf_runner -out=<plan>` -- READ IT
4. tag-authz gate run BY HAND (see Compiler Tools), then `safe-apply.sh` with audited override
5. `aws iam get-role-policy` for APPLIED truth
6. `simulate-principal-policy` battery, ONE `--resource-arns` per call, controls SEPARATE
7. `git push origin CLOUD`

## Verification (actual output)

Applied plane, `aws iam get-role-policy --role-name mdpf-daily-runner-ec2-role --policy-name mdpf-runner-scoped`:
```
P0DenyJsonMdpfClobber20260728         | Deny | arn:aws:s3:::opal-data-portal-v2/json/mdpf/*
P0DenyLegacyPortfoliosClobber20260728 | Deny | ['.../json/portfolios/non_model_assets.json',
                                               '.../json/portfolios/aum-timeseries.json']
```

Exercised (`simulate-principal-policy`, one resource ARN per call, each control a separate invocation):
```
LEG 1
  json/mdpf/global/aggregate-aua-timeseries.json       PutObject explicitDeny
  json/mdpf/49financial/aggregate-aua-timeseries.json  PutObject explicitDeny
  platinum/mdpf/aggregate_aua_timeseries.json          PutObject allowed
  json/portfolios/non_model_assets.json (pre-leg-2)    PutObject allowed
  json/mdpf/global/... GetObject                       allowed
  opal-data-assets/gold/mdpf_revamp/global/...         PutObject allowed
LEG 2
  json/portfolios/non_model_assets.json                PutObject explicitDeny
  json/portfolios/aum-timeseries.json                  PutObject explicitDeny
  json/portfolios/<other key>                          PutObject allowed   <- over-deny control
  platinum/mdpf/etf_ownership_timeseries/DIVZ.json     PutObject allowed   <- OWNTS survives
  platinum/mdpf/aggregate_aua/2026-07-28.json          PutObject allowed   <- WS-A survives
```
`explicitDeny` WITH a named matched statement, which also rules out the Rule-22a mode-3 false-deny
(a nonexistent action name returns `implicitDeny`, indistinguishable from a missing grant).

Collateral check: enumerated all 16 `portal-v2` destinations the 07-27 run actually wrote. Exactly
6 are denied (4 json/mdpf + 2 portfolios); all 10 platinum destinations survive.

Detector at 14:28Z -- all four json/mdpf ETags still at CTO's 1341Z baseline; both portfolios keys
still at `a453f372` / `9a455976`, 27 Jul 15:10:07Z.

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-tagauthz check --from-plan` | mdpf-pipeline, both legs | PASS (rc=0) | Run BY HAND -- `safe-apply` could not self-run it |
| `comp-which` rail (HUD) | attempted `infra/*.tf` grep | BLOCKED (correct) | Rail denied the blind .tf grep; used live `get-account-authorization-details` instead, which is strictly better (applied plane, and TF cannot see a non-TF principal) |
| `comp-iam` | NOT used, deliberately | n/a | Models `(action)` never `(action, resource)` and fails GREEN -- cannot settle an `(action, resource)` question. Grounded on `simulate-principal-policy` + `get-role-policy` instead (Rule 22a) |

**What worked:** `simulate-principal-policy` with one resource ARN per call and separate controls
produced a genuinely discriminating battery both times (6/6, both verdicts represented).

**What failed -- FABRIC DEFECT, routed to CTO:** `safe-apply`'s `comp-tagauthz` gate CANNOT
SELF-RUN in this shell. It builds its plan via `mktemp`/`$TMPDIR` (`safe-apply.sh:157`) and `/tmp`
is unwritable here (probed: `touch /tmp/... -> Permission denied`), so it fails closed with "could
not produce a plan JSON" -- an ENVIRONMENT defect wearing the costume of a gate refusal. I did not
bypass blind: ran the gate by hand on the identical plan (`terraform show -json <plan>` ->
`comp-tagauthz check --default-tags-tree . --from-plan`), got rc=0 PASSED scoped to 0 candidate
instances (plan carries zero `aws_instance`), and only then set `TAGAUTHZ_OVERRIDE` with that
evidence as the audited reason (INTENT `20260728T135941Z-2325965`, `20260728T142624Z-2380717`,
both OUTCOME SUCCESS). **The cost is that it trains agents to reflex-override a security gate** --
and then the once it fails for a real reason, nobody notices. CTO filed it; fix is honour `TMPDIR`
or fall back to a tree-local temp path.

**Gap found:** `.tools/aws` is unreliable in this Bash (resolves via `~/bin/aws` into a
Python-executed forwarder -> `SyntaxError`). PowerShell's `aws` works. Also the harness rc is
corrupted in this shell (`claude-*-cwd: No such file or directory` on every call) -- captured
TRUE_RC in-stdout throughout.

## Findings routed (not acted on)

1. **`mdpf-pipeline` carries 4 committed-but-unapplied resources** -- the row-10 scheduled floor
   (`aws_cloudwatch_event_rule`/`event_target`/`lambda_permission` `mdpf_scheduled_floor`) plus
   `aws_sqs_queue_policy mdpf_trigger_dlq`. A plain `apply` attaches a NEW EventBridge schedule to
   `mdpf-daily-trigger`. Used `-target` to keep them out. **CTO ruling: tree FROZEN to targeted
   applies until he sequences row 10.** COO adds: that floor targets `mdpf-daily-trigger`, which
   may NOT be the publisher Andrew's P0 names (`opal-assets-mdpf-portal-publisher`) -- applying it
   could close the P0 on paper while the real publisher stays unscheduled.
2. **Stage 6 REVAMP has been failing rc=1 on a MISSING IAM GRANT, not on code.** 07-27 log:
   `AccessDenied PutObject arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/date=2026-07-27/data.parquet`.
   Source-grounded (`data/assets/scripts/gold/build_dim_model_portfolio.py:378-383`) the stage
   needs THREE grants it lacks, not one: `PutObject` on the gold key (`:382`), **`GetObject` on
   the same key for the `head_object` verify at `:383`** (HeadObject IS `s3:GetObject` -- granting
   only PutObject would just move the failure), and `ListBucket` on `opal-data-assets` (`:116`
   paginate, latent -- only fires when `--date` is absent). Consequence: `cycle-complete.json` has
   NEVER been emitted, so anything gated on that marker is dark. **NOT granted** -- the prefix is
   `blackdiamond/cottonwood/*`, a firm-scoped write, so it is an authority call under NEVER#2, and
   the better question (COO concurring) is whether this stage should write cottonwood gold at all.
   CTO holds disposition.
3. **My own guard is PRINCIPAL-scoped, not prefix-scoped.** Live sweep
   (`get-account-authorization-details`; DENOMINATOR 206 roles + 30 default managed-policy
   versions): SEVEN other roles retain `PutObject` reaching `portal-v2/json/mdpf/*` --
   `bd-pipeline-task-role`, `opal-portal-lambda-role`, `smartx-exporter-role`,
   `smartx-ingestion-lambda-role`, `yang-pipeline-lambda-role` (all `portal-v2/*` bucket-wide),
   `news-ingestion-lambda-role` and managed policy `opal-data-refresh-lambda-policy`
   (`portal-v2/json/*`). No evidence any writes that prefix. CTO's "nobody writes it except me" is
   a CONVENTION, honoured, NOT an enforced control. A real fence is a bucket-policy Deny with one
   allowlisted publisher -- same question as "who owns the serve", i.e. leg (b).
4. **ROLLUP is `:375` DEPLOYED vs `:391` in the repo** (deployed dispatch 32,077 B @07-23T06:55 vs
   34,751 B repo). CTO had been citing `:391` all session. Same deployed-vs-repo class as the
   producer freeze, one layer up.
5. **The served set was never one generation.** The deployed 2-firm code CANNOT emit cottonwood --
   three keys refreshed daily off the dead path, one frozen at 07-23. The non-atomicity is not a
   race; it is one writer structurally incapable of producing a member of the set it publishes.
   COO folded this into L3's requirements.

## Blockers

**None of mine.** Gated at others, evidence-cited:
- **[1.0.0_SA_CTO]** disposition on the Stage-6 cottonwood IAM grant (3 grants, not 1); row-10
  sequencing + whether the floor targets the right lambda; the bucket-policy fence decision.
- **[0.4.0_DS]** trace of both non-model producers to Andrew's canonical basis (~1427Z verbatim:
  *"0824 schwab total value minus 49F smartx model aggregation, that is canonical balance"*) --
  routed by CTO as L2, sequenced after the 15:10Z run.

## Current State

Both Denies LIVE and exercised on `mdpf-daily-runner-ec2-role` (`26ac313453`, `d28371947c`, both
pushed to CLOUD). Six served keys frozen against the runner; all 10 platinum destinations and the
`opal-data-assets/gold/mdpf_revamp/*` REVAMP writes unaffected, so tomorrow's correct data still
produces. `mdpf-pipeline` FROZEN to targeted applies. Two background ETag watches armed to 15:25Z.

**CTO ruling (`143039Z`): option (a) -- LEAVE IT FROZEN, do NOT write a corrected artifact.**
`0.2.0_DT` WITHDREW the claim that $1.95B is correct; the two producers disagree ~$20-30mm on the
SAME DATES for 2+ weeks, which is a persistent BASIS disagreement, not staleness. The rendered
$1,924,186,044.47 is internally incoherent (model leg one basis, non-model leg another) -- that is
the defect, independent of which producer is authoritative. A wrong-but-stable number beats an
unverified new one on a live screen. The Deny binds the runner role ONLY, so CTO remains the
authorised writer of `portal-v2/json/*` and is deliberately not exercising it.

**Expected at ~15:10Z, pre-registered:** three ROLLUP AccessDenied WARNs with Stage 4 rc=0; a
Stage 3.5 LEGACY-EMIT FAILURE (that is leg 2 working, NOT a regression); OWNTS complete; Stage 6
rc=1 on the pre-existing cottonwood IAM gap (NOT a DS regression); all six ETags unmoved. If chain
rc goes to 1, or OWNTS/Stage 6 do not run, the try/except analysis was wrong -- escalate to CTO
immediately.

## OUTCOME OF THE ~15:10Z WINDOW (appended 15:36Z) -- THE PRE-REGISTRATION ABOVE DID NOT HAPPEN

**NO RUN OCCURRED. Every expectation pre-registered above is UNTESTED, not confirmed.** Leaving the
prediction standing without this would make a stale record say something false with authority.

Measured 15:26Z: all six served keys intact, byte-identical to baseline (four json/mdpf at CTO's 1341Z
restore, both json/portfolios still 27 Jul 15:10:07Z). **But the Denies did not cause that** -- nothing
executed. No `mdpf_daily_20260728_*` log key exists (independently re-confirmed by a watch to 15:35:33Z);
`status.json` still reads `run_id mdpf_daily_20260727_150800` / `updated_at 2026-07-27T15:11:34Z`; runner
`i-02448edb624a7a7cf` is `stopped`.

**BOTH DENIES REMAIN VERIFIED ONLY BY `simulate-principal-policy`. THE PRODUCTION EXERCISE DID NOT HAPPEN,
AND NEITHER DID DS's PRODUCER DEPLOY.** A clean detector over a chain that never ran is not the same result
as a clean detector over a chain that degraded as designed (COO's framing, and it is the whole point).

**WHY:** `mdpf-daily-trigger` fired once at 15:04:00Z with 0 errors (CloudWatch: exactly 2 invocations in
26h, 07-27 and 07-28 both at 15:04:00Z) and the INF event source DID land
(`opal-data-inf/gold/meta/pipeline-complete.json` 15:04:07Z). The gate returned
`"dispatched": false, "deferred": true` -- 49financial RPS silver at `latest_partition 2026-07-23`,
`trading_days_behind 3` vs `max_lag_trading_days 2`. **The DEFER is CORRECT**, and the gate counted in
TRADING DAYS itself, so NEVER#1 is satisfied.

**THE DEFECT FOUND -- THE GATE NAMED THE WRONG FAILURE.** It logged
`ROLL_SOURCE_UNREADABLE 2026-07-23.json (403) -- a CONFIG/IAM fault that will NOT clear on its own`.
Measured: that object **does not exist** (my head_object -> 404; the prefix runs 07-17, 07-18, then 07-25,
07-26, 07-27 -- no 07-19..07-24, the six-day freeze still legible). The trigger role HOLDS `GetObject` on
the key (`allowed`) but LACKS `s3:ListBucket` (`implicitDeny`) -- and **without ListBucket, S3 returns 403
instead of 404 for an absent key.** So `_roll_source_exists()` (`lambda_function.py:351-382`), which was
built specifically to separate "cannot read it" from "it does not exist", **has that discrimination
defeated by a missing grant on a DIFFERENT ACTION than the one it tests** -- and it fails in the expensive
direction, reporting a DATA condition as a permanent CONFIG fault. Per its own docstring
`mdpf-freshness-checker` alarms on UNREADABLE and never on ABSENT (alarm existence NOT verified -- flagged,
not claimed).

**NOT MY DENY, proven four ways, not asserted:** different principal
(`mdpf-daily-trigger-lambda-role` vs `mdpf-daily-runner-ec2-role`; isolated control shows my statements are
not even in the trigger's evaluation -> `implicitDeny`); different action (`head_object` = `s3:GetObject`
vs my `PutObject`); different prefix (`platinum/mdpf/aggregate_aua/*` vs `json/*`); and the trigger role's
GetObject on that exact key simulates `allowed`.

**RECOMMENDED, NOT EXECUTED (tree frozen, CTO's gate):** `s3:ListBucket` on `opal-data-portal-v2` for
`mdpf-daily-trigger-lambda-role`, prefix-conditioned to `platinum/mdpf/*`, mirroring the runner's existing
`PlatinumMdpfListScoped`. **IT FIXES ONLY THE LABEL -- ABSENT and UNREADABLE both DEFER, so it unblocks
nothing.** The chain stays blocked until 49F RPS silver clears. Stated explicitly because "add the grant"
is exactly the shape that gets reported as a resolution.

**STANDING RISK TO CARRY:** the next production exercise requires a dispatched run, and the gate will keep
deferring while 49F is stale. **The Denies may sit unexercised for days, and accumulated silence reads as
confirmation.** Recorded here so "the hold is proven" cannot become the remembered state. It is landed and
simulated, not proven.

## Next Steps

1. **[0.7.0_AE_CloudOps]** Report the ~15:10Z run from its OWN log: Stage 4 rc, the WARN naming
   the AccessDenied, Stage 3.5 run/failed with `non_model_assets.json` ETag+size+LastModified both
   sides, OWNTS, Stage 6. Clean or not, unprompted.
2. **[0.7.0_AE_CloudOps]** After the meeting + on CTO's word: tidy-up commit deleting the
   `JsonMdpfServingRW` Allow (Andrew ~1351Z makes this a DECOMMISSION, not a liftable hold) and
   fix the leg-1 commit message's "TO LIFT" frame -- a decommission described as liftable is a
   stale record that reads as an invitation.
3. **[1.0.0_SA_CTO]** Stage-6 cottonwood grant disposition; row-10 sequencing; fence decision.
4. **[0.7.0_AE_CloudOps]** Queued, yielding to the P0: `~Z` EC2 `i-06376c11d8b3c3443` no instance
   profile; `INF_GOLD_RELEASE_PROVENANCE` set-but-unread disposition; 3 Rule-4
   `lambda-source-map.json` MISSING_ENTRY + 3 WRONG_SOURCE_DIR.
