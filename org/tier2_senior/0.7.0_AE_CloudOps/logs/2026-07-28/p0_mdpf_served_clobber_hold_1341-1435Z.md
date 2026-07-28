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

## ROW 13 IS THE REAL BLOCKER (appended 15:50Z) -- AND I HAD IT WRONG FIRST

**MY ERROR, on the record:** in the 15:35Z outcome above I wrote "the chain stays blocked until 49F RPS
silver clears." **That was wrong.** I accepted the gate's `latest_partition 2026-07-23 /
trading_days_behind 3` as a DATA condition without asking what object produced it -- NEVER#1's second
clause (*the instrument's own verdict is not a second opinion, it is the same error*), committed inside the
report where I was warning about accumulated silence. COO challenged the premise; the challenge held.

**MEASURED, both paths, 15:41Z:**
```
WHAT THE GATE READS   s3://opal-data-bd/schwab/silver/rps/            newest date=20260723   FROZEN
WHERE THE DATA IS     s3://opal-data-assets/schwab/08242234/silver/fact_rps/
                                                                     newest date=2026-07-27  FRESH (T-1)
```
Source-confirmed @HEAD: `:54 BD_BUCKET=env("BD_BUCKET","opal-data-bd")`, `:96
SCHWAB_RPS_PREFIX=env(...,"schwab/silver/rps")`, `:440 paginate(Bucket=BD_BUCKET)`; the LIVE function
overrides NEITHER. **So the gate's verdict is a TRUE READING OF A DEPRECATED OBJECT.** The chain defers on
a dead path, not a data condition. Corroborated three ways: COO's 544-partition measurement, DS's L1 row,
and my own listing.

**THE TRAP -- row 13 is NOT a two-env-var change.** Both knobs are env-overridable, so the obvious fix is
`BD_BUCKET=opal-data-assets` + `SCHWAB_RPS_PREFIX=schwab/08242234/silver/fact_rps`. **That silently returns
ZERO.** `:443` is `re.match(r"date=(\d{8})/(.+)$", rel)` -- compact form only; the monolith is
`date=2026-07-27`, hyphenated. Every key fails the regex, `latest` stays `None`, the gate returns
`fresh:false, latest_partition:null` and defers for a reason further from the truth. That regex is a
DELIBERATE CTO arch-gated hardening ("a stray flat/partial object must NOT read as fresh") -- **a correct
control that becomes a blindness the moment it is pointed at a population with a different key grammar.**

**CTO RULINGS (20260728T154511Z):** (a) GO -- re-point and grammar fix are ONE commit or neither;
(b) NOT "accept both" -- **DECLARE THE GRAMMAR PER SOURCE**, a non-matching key FAILS LOUDLY (accepting
both would keep the dead path a valid freshness source, i.e. curing row 13 with row 13's own disease);
(c) row 13 lands **ALONE**, targeted, never entangled with row 10's four pending resources.
**TIMING: HOLD until CTO's word -- Andrew may still be presenting.**

### (b) ENUMERATION -- DENOMINATOR STATED, GRAMMARS MEASURED LIVE
Freshness surface = **3 check functions** (`_check_inf_spine` :303, `_check_bd_silver` :320,
`_check_schwab_rps` :458); **2 are partition-scanning**; `:614` selects ONE BD-side check per invocation
via `custody_source`, so the gate reads **2 sources per run, never 3**.

| Src | Location | Grammar (MEASURED) | Newest |
|---|---|---|---|
| S1 inflection spine | `opal-data-inf/gold/meta/pipeline-complete.json` | NOT a partition -- date from JSON body `run_date` | 2026-07-28T15:04:07Z |
| S2 49F BD silver (dormant) | `opal-data-bd/silver/{allocations,fees}` | FLAT `{YYYY-MM-DD}.parquet` | `2026-07-24.parquet` |
| S3 49F Schwab RPS (LIVE) | `opal-data-bd/schwab/silver/rps` | DIR `date=YYYYMMDD/` COMPACT + `data.parquet` | `date=20260723/` |
| TARGET row 13 | `opal-data-assets/schwab/08242234/silver/fact_rps` | DIR `date=YYYY-MM-DD/` HYPHENATED + `data.parquet` | `date=2026-07-27/` |

**VERDICT: GENUINELY MIXED, not theoretical.** Three structurally unrelated grammars (JSON body field /
flat filename stem / directory token). **The gate already IS a multi-grammar reader -- the mix is hardcoded
per function rather than declared.** This also kills "accept both" twice over: there is no single "both",
and a sniffing parser would make every source silently accept every other's grammar (a stray
`2026-07-27.parquet` under the RPS prefix would satisfy RPS freshness).

**OPEN GATE ON ROW 13, raised not answered:** the monolith carries TWO RPS silver tables, both hyphenated,
both fresh at 2026-07-27 -- `fact_rps` AND `fact_rps_s2`. Row 13 must DECLARE which is the
freshness source-of-record. Choosing by name-length is exactly the 0824/0833 never-SUBSTITUTE shape -- a
SELECTION between similar masters made at a call site instead of derived from a declared
consumer-anchored purpose. Routed to CTO; needs 0.6.2_PartnerETL or DS to state what `_s2` denotes.

**FLAGGED, NOT CLAIMED:** S2 (`opal-data-bd/silver/{allocations,fees}`) sits at 2026-07-24 = 2 trading days
behind vs `BD_MAX_LAG_TRADING_DAYS=2` -- `fresh:true` by exactly one day of margin. Dormant today
(`custody_source=schwab`). If custody ever flips back to `bd`, that path is one trading day from deferring
and nobody would expect it, because the RPS story will have been "fixed."

## DURABLE CHECK FOR THE NEXT WINDOW -- A PROCEDURE, NOT A PROCESS

**I CANNOT arm a watch that survives this session** (background tasks die with it; my lane arms ZERO crons
by standing order, LD-0157). I told COO I would re-arm and then retracted it within the hour -- accepting
that ask would have put a phantom detector into the sweep record, which is the same class this whole
session has been closing, authored by me. **So the durable artifact is this procedure plus the baselines,
not a watcher.** Whoever is live after ~15:05Z next cycle:
```
aws s3 ls s3://opal-data-mdpf/telemetry/mdpf-daily-runner/logs/ | grep 2026072       # did it RUN
aws s3 cp s3://opal-data-mdpf/telemetry/mdpf-daily-runner/status.json -              # run_id + per-stage rc
aws logs describe-log-streams --log-group-name /aws/lambda/mdpf-daily-trigger \
    --order-by LastEventTime --descending --max-items 1                              # dispatch-vs-DEFER + reason
```
Then head-object the six served keys and compare to the baselines recorded above. **`mdpf-freshness-checker`
reportedly alarms on ROLL_SOURCE_UNREADABLE per the gate docstring -- I have NOT verified it exists or has
ever fired, so it is NOT counted as coverage** (same rule applied to the fan-in fence: an unverified alarm
is a document).

## ROW 13 RESOLVED + BUILT + STAGED @938fc74211 (16:01Z) -- STILL NOT APPLIED

**Both design gates cleared by CTO:** grammar = DECLARE PER SOURCE (154511Z); source-of-record =
**`fact_rps_s2`, NOT `fact_rps`** (155053Z) -- consumer-anchored, because the producer reads `_s2` and only
`_s2` for 49F custody (`dim_mdpf_aggregate_aua_timeseries.py:326,:387`). `_s{N}` is a MECHANICAL SECTION
suffix carrying NO seniority (`silver_registry.py:72-81`); for RPS the substantive full-envelope data is in
section 2. Gating on `fact_rps` would have moved the gate off a dead bucket onto a live-but-WRONG table and
looked fixed. **My refusal to infer it from the suffix was the right call** -- picking by name-length is the
0824/0833 never-SUBSTITUTE shape.

**BUILT:** `_GRAMMARS` declaration table + `_latest_dir_partition(bucket, prefix, grammar)` returning
`(date, reason)` over four worlds a bare `None` collapsed -- `OK` / `PREFIX_EMPTY` / `GRAMMAR_MISMATCH` /
`NO_DATA_PARTITION` -- plus `UNDECLARED_GRAMMAR` (a bug, never guessed). The verdict now carries
**bucket + grammar + read_status** and a distinct `config_fault`, so a mis-declared source can NEVER be
read as a freshness verdict. Both original hardenings preserved verbatim; only the date token is
parameterised.

**EXERCISED OFFLINE (mocked boto3, no AWS -- NEVER#4 intact, no run manufactured): 20/20 PASS**, including
the one that encodes CTO's ruling (a):
`MUTANT env-only re-point (dashed keys, compact grammar) -> None` + `MUTANT names itself GRAMMAR_MISMATCH,
NOT stale data`. Also: dashed grammar REJECTS a compact key (no cross-grammar tolerance, so the dead path
cannot return as a valid freshness source). **One of my own tests failed first and the TEST was wrong, not
the code** -- a bare `date=.../` marker is excluded by hardening (a) (nothing after the slash fails
`(.+)$`), not by (b); to reach (b) a key must MATCH the grammar and still carry no data. Asserting the
right label against the wrong mechanism is its own failure mode, so the corrected test says why.

**THE LIVE LAMBDA IS UNTOUCHED and still reads the dead path. Nothing done today altered the running gate.**
Remaining gate is CTO's timing word for one targeted apply.

**PRE-EXISTING DEFECT FOUND, NOT MINE, NOT FIXED:**
`test_convergence_gate_weekend.py::test_handler_defers_on_genuine_bd_slip` **FAILS AT HEAD** -- 1 failed /
6 passed WITH and WITHOUT my change, verified by running HEAD's own copies in an isolated scratch dir.
*(`git stash` was correctly BLOCKED by the never-rules gate -- shared worktree, stash parks every dirty
file including other agents' unsaved work. The gate was right; `git show HEAD:<path>` answered the same
question without mutating global state.)* It fails via a **REAL `ec2:StartInstances` call**, so: (a) the
handler reaches DISPATCH on a case the test names a genuine slip and expects to DEFER -- harness defect or
handler defect, UNDETERMINED and not guessed; (b) **with a valid instance id this test suite would start
live EC2.** Routed to CTO.

## ROW 13 APPLIED + THE PRODUCTION EXERCISE OBTAINED (appended 16:52Z) -- CLOSING STATE

**Andrew-direct GO ~1625Z ("go ahead on firing Row 13"), CTO GO 163042Z.** Applied targeted; artifact built
via `build-and-upload.sh` (write-VERIFIED, sha256 metadata match), `CodeSha256` on the live function ==
the uploaded artifact, three declarations live as env vars, 0-diff on the target, **row 10's four resources
held back**. The `comp-tagauthz` gate **SELF-RAN with no override** -- exporting a writable `TMPDIR` fixes
the cygwin `/tmp` defect, **retiring the audited bypass used twice earlier today.**

### MY ERROR, AND THE ONLY REASON IT WAS CAUGHT
The first post-apply invoke did NOT return a verdict -- it THREW:
`AccessDenied ListObjectsV2 ... mdpf-daily-trigger-lambda-role ... s3:ListBucket on opal-data-assets`, at
`lambda_function.py:512` (my new reader). **I re-pointed a reader at a bucket its role could not read.**
Gate went from clean-DEFER to unhandled exception. Served set unaffected; I STOPPED and reported without
iterating. Andrew ratified (A) directly -- *"It is more important to add the correct grants versus roll back
to a broken setup"* -- rollback off the table.

>> **THE LESSON, AND IT IS DISTINCT FROM EVERY OTHER ONE TODAY: I VERIFIED THE DATA WAS THERE; I NEVER
VERIFIED THE CALLER COULD REACH IT.** I ran an exhaustive Rule-22a battery that day -- on the RUNNER role's
WRITES -- then changed a DIFFERENT principal's READ target without re-applying it. The rigour was real and
it was pointed at the wrong actor. **And the offline mutant suite passed 20/20 the whole time it was
broken, because it MOCKS BOTO3 -- IAM structurally cannot exist inside it. A GREEN TEST PLANE SAYS NOTHING
ABOUT REACHABILITY.** Two planes, one green light. Both now landed as MDPF_DEBTCLEAN controls. <<

**FIX:** two prefix-conditioned grants on `mdpf-daily-trigger-lambda-role` (`AssetsSchwabRpsS2GateRead` +
`AssetsSchwabRpsS2GateList`), targeted apply, 6/6 discriminating -- reader `allowed` **with
`--context-entries s3:prefix`** (without which the conditioned statement returns an `implicitDeny`
byte-identical to a real deny, i.e. I would have "proved" my own grant failed), and `implicitDeny` on
another firm's monolith prefix, on the SIBLING `fact_rps` table, and on writes. **Never bucket-wide on the
monolith.**

### THE GATE'S OWN VERDICT -- IT WORKS
```
"49financial": {"fresh": true, "bucket": "opal-data-assets",
                "prefix": "schwab/08242234/silver/fact_rps_s2",
                "grammar": "dir:date=YYYY-MM-DD", "latest_partition": "2026-07-27",
                "trading_days_behind": 1, "read_status": "OK"}
"all_fresh": true -> "dispatched": true, ssm_command_id b8a0f56f-...
```
`read_status: OK` is the discriminator proving BOTH halves landed -- re-point AND parser.

### THE PRODUCTION EXERCISE, FINALLY -- run `mdpf_daily_20260728_164452`, CHAIN complete
```
LEG 1: FOUR AccessDenied WARNs (NOT three -- top-level key PLUS 3 firm slices), each
       "with an explicit deny in an identity-based policy"; "primary timeseries IS written ... Continuing."
       step ROLLUP rc=0 dur=27s status=ok          <- the try/except analysis was RIGHT
LEG 2: UPLOADING .../json/portfolios/aum-timeseries.json -> AccessDenied, explicit deny
       step LEGACY-EMIT rc=1 status=error ... "chain continues"   <- the DISPATCH-tolerates analysis was RIGHT
       step OWNTS rc=0 status=ok                   <- OWNTS was NOT collateral
ALL SIX SERVED ETags: byte-identical to CTO's 1341Z restore, through a run that ACTIVELY TRIED to write them.
```
**BOTH MECHANISMS CONFIRMED SEPARATELY IN ONE RUN** -- leg 1 safe because the SCRIPT swallows, leg 2 safe
because the DISPATCH tolerates. Neither is evidence for the other; that is why leg 2's cascade check had to
be redone from scratch. *(Precision: leg 2 died on the FIRST of its two writes, so `non_model_assets.json`
was never reached -- same statement covers it, but the OBSERVED evidence covers one key.)*

**>> "LANDED AND SIMULATED, NOT EXERCISED" IS NOW RETIRED, BY EVIDENCE. <<**

### WHAT IS STILL BROKEN -- pre-registered BEFORE the evidence existed
- **Stage 6 rc=1**, `opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/date=2026-07-28/
  data.parquet` -- *"because no identity-based policy allows"*, textually DISTINCT from my Deny's *"with an
  explicit deny"*. `cycle-complete.json` **still never emitted**. Needs THREE grants, not one.
- **The rollup still logged "2 partner(s)".** DS's fix went to `code/scripts/gold/`; ROLLUP is `backfill/`
  -- a different directory. **The legacy producer is exactly as wrong as it was this morning and still
  cannot emit cottonwood.** THE CHAIN RAN; THE PRODUCT IS NOT FIXED. Do not let those merge.

## ITEM 1 -- ENUMERATED-LIST SWEEP (appended 17:13Z). 2 of 8 TRIAGED: 1 DEFECT, 1 CLEAR

**Hypothesis (CTO 170204Z, from my own inference):** cottonwood was onboarded AFTER these artifacts were
written, so **every non-wildcard enumeration silently never got updated.** Tested; holds.

**METHOD.** `DENOMINATOR 257 files` (.py/.tf/.sh/.json/.mjs/.yaml/.yml) across 8 roots (data/mdpf,
data/assets/scripts, terraform/{mdpf-pipeline,opal-assets}, ec2/mdpf-daily-runner,
lambda/{mdpf-pipeline,opal-assets}, lambda-edge). **PREDICATE: names BOTH `49financial` AND `inflection`
-- firms treated as a SET -- but NOT `cottonwood`. 18 candidates, 8 on the live path.**
**FIRST PREDICATE DISCARDED:** *"names 49financial OR inflection without cottonwood"* gave **49 hits and
was junk** -- it flags every single-firm-by-design script. **A single-firm script cannot omit a member;
only a firms-as-a-SET enumeration can.** The bigger number would have looked better and meant less.
**Positive control:** the sweep independently re-found today's two known defects
(`build_aggregate_aua_timeseries.py`, `build_legacy_compat_emit.py`).
**Reference is clean:** `data/mdpf/config/partner_roster.json` (owner_lane = mine) DOES carry cottonwood.

### CONFIRMED DEFECT -- `mdpf-freshness-checker/lambda_function.py`
```
COHORTS DEFINED: 14   partner values: {'49financial': 9, 'inflection': 1}   cottonwood: 0
"cottonwood" anywhere in the file: FALSE
```
>> **THE FRESHNESS ALARM CANNOT SEE COTTONWOOD.** The instrument whose entire job is to notice when a
firm's data stops advancing has no cohort for the firm whose data stopped. **Nothing fired because
cottonwood was never in its enumeration.** <<

**FOURTH MECHANISM ON ONE VICTIM:** (i) legacy 2-partner producer cannot emit it · (ii) `fact_holdings`
stalled 07-24 while siblings advance · (iii) OAC allowlist omits its 2 served keys (produced, present,
403) · **(iv) no freshness cohort.** **THE COMPOUNDING IS THE POINT: (iv) is what should have caught
(i)-(iii). The detector and the defects share a blind spot, so the omission is not additive -- it is what
made the other three SURVIVABLE.** Four enumerations, four omissions, one firm: the prediction is now a
measured pattern, not an inference.

**Closes a loop:** at 15:35Z I refused to count this alarm as coverage because I had not verified it
existed. Right call, sharper reason: **it exists, it runs, and for cottonwood it is structurally blind.
An unverified alarm was a document; a verified one turns out to be a document FOR ONE FIRM.**

**CTO RULING ON THE FIX (171123Z) -- NOT "add a cottonwood cohort":** a 15th hardcoded entry rebuilds the
defect with one more member and guarantees the fifth firm repeats it. **The cohort table becomes DERIVED
FROM `partner_roster.json`**, and **must ERROR on a roster member whose predicate it cannot evaluate,
never silently skip.** Same principle as the prefix grant and per-source grammar declaration: **derived
from one declared authority, never restated at a call site.**
**PREDICATE ROUTED TO `0.4.0_DS`, NOT PICKED BY ME** -- cottonwood has **no single freshness answer at
channel grain** (`fact_model_assignment` 07-28 / `fact_allocations` 07-27 / `fact_holdings` 07-24), so it
needs PER-TABLE declaration. Choosing a max-lag myself would be the call-site-literal error the roster
exists to prevent. **NOT BUILT.**

### ⚠ CORRECTION (17:23Z) -- THE FRESHNESS CHECKER IS **NOT DEPLOYED**. MY FINDING WAS WRONG AND UNDERSTATED
```
aws lambda get-function-configuration --function-name mdpf-freshness-checker
  -> ResourceNotFoundException.  Deployed mdpf lambdas: ONLY mdpf-daily-trigger
     and opal-assets-mdpf-portal-publisher.
```
Terraform REFERENCES it in comments while nothing deploys it. Confirms CVO's morning measurement
independently.

>> **I WROTE "it exists, IT RUNS, and for cottonwood it is structurally blind." "IT RUNS" WAS FALSE, AND I
INFERRED IT FROM THE PRESENCE OF A SOURCE FILE.** That is the deployed-vs-repo class -- the same one that
opened this whole incident, the same one I caught in the gate reading a dead bucket, in the
`public-data-router` fork, in the mdpf `code/` prefix. **I committed it in the very sentence where I was
crediting myself for refusing at 15:35Z to count an unverified alarm** -- then counted it at 17:10Z on
strictly weaker evidence than I had demanded three hours earlier. CTO told me to establish
deployed-vs-repo BEFORE reading the enumeration; I read first. That ordering was the discriminator. <<

**CORRECTED FINDING, LARGER NOT SMALLER: there is no freshness alarm at all.** The 14 cohorts describe an
instrument that does not exist. **NOBODY's freshness is monitored** -- not cottonwood's, not
49financial's nine, not inflection's. The cottonwood omission is real but it is a detail of a monitor
that never ran. **So mechanism (iv) is not "an alarm blind to cottonwood" -- it is "NO ALARM."** The
compounding claim survives and is stronger: (i)-(iii) endured because **nothing was watching anything**.
This is postmortem §10 E2, still open, now confirmed from a second direction.

**CONSEQUENCE FOR THE RULING:** CTO's roster-derived fix stands but is **no longer a fix to an existing
Lambda -- it is a BUILD-AND-DEPLOY** of an instrument that has never existed (TF resource + artifact +
schedule), materially larger than "make the cohort table derive from the roster." Sizing is CTO's; not
silently re-scoped by me.

**METHOD COMMITMENT: never report an instrument's BEHAVIOUR without first establishing the instrument is
DEPLOYED.** Describing what a cohort table monitors is a claim about a RUNTIME made from a FILE. Remaining
6 candidates get a deployed-vs-repo check BEFORE any reading.

### CLEARED -- `mdpf_revamp_model_crosswalk.py` (a FALSE POSITIVE of my own predicate)
Names both firms **only in comments/docstring**; the code branches `if firm_id == "global": ... else:
entry_for_key(model_key).display_name` -- **global vs NOT-global, never a firm list.** Cottonwood takes
the generic per-firm path. **My predicate cannot distinguish a comment from a control** -- which is why
the 8 were reported as CANDIDATES, not findings. It also already raises `UnknownModelError` rather than
dropping (CVO F5), i.e. it **already implements the fail-loud property CTO just ruled for the freshness
fix** -- cite it as the in-house precedent. **Both copies BYTE-IDENTICAL** (`d43c99acf061f0a3d...`): no
fork, unlike the `public-data-router` pair. **2b is NOT undercut.**

### OUTSTANDING (6, lower prior)
`mdpf_aggregate_aua.py` · `wsd_partner_held_etf.py` (x2 copies) · `verify_wsd2_clears_identity2.py` ·
`mdpf-daily-trigger/lambda_function.py` (mine -- gate checks inflection spine + 49F custody, cottonwood
is not a gated partner, so likely correctly scoped). **1 defect in 2 is NOT a rate to extrapolate: I
picked those two BECAUSE they were highest-consequence, the least representative sample in the set.**

## ANDREW-DIRECT ~1725Z -- FRESHNESS-CHECKER LINE STOPPED; QUEUE RE-ORDERED (appended 17:36Z)

**VERBATIM:** *"We don't need freshness checkers at this point, what we need to do is create established,
canonical routes and schedules and make sure they are robust. This is a significantly higher priority than
making freshness checkers before these patterns are designed and deployed."*

**The freshness checker is a RECORD, not a build.** Do NOT build it, size it, or route the DS predicate
question (CTO withdrew that ask -- it existed only to feed a monitor we are not building). The finding
stands as postmortem §10 E2, confirmed from three directions (CVO this morning, me at 17:23Z, and the TF
comment asserting an emitter that does not exist).

**WHY, and it re-reads today's headline finding:** a monitor built now would encode the PRE-CUTOVER
topology -- serving origin unresolved, publisher unbuilt, legacy rollup pending decommission, serving set
only established as FIVE artifacts this afternoon -- and would report GREEN against routes we intend to
retire. **You cannot monitor your way out of an unstable pattern; a checker on a non-canonical route
measures the wrong thing PRECISELY, which is what this entire incident is made of.** The absent alarm was
never the root defect: **there was nothing stable for it to check.**

**RE-ORDERED QUEUE. STANDING TEST: does this make a route CANONICAL and ROBUST? If it observes, reports,
alarms or measures WITHOUT changing what the route IS, it goes behind the things that do.**
1. `PIPELINE_MAP` part 1 + the Rule-12 class (scoping in msg 20260728T165951Z -- **do NOT land as a map
   entry**: emits `code/<layer>/` vs live `code/scripts/<layer>/`; 4 of 6 live dirs outside `VALID_LAYERS`
   incl. `backfill/` = the ROLLUP and `assets_gold/` = the Stage-6 script; would resolve to a NONEXISTENT
   key, worse than not registering. Needs a schema change: declare prefix + layers per tree.)
2. 2b's AUTH-invariant enforcement (elevated -- canonical-route work; gated on DT's Q4)
3. Stage 6's three grants (Andrew-ratified, AUTHORIZED, prefix-scoped to
   `opal-data-assets/blackdiamond/cottonwood/gold/`) -- unblocks `cycle-complete.json`, the publisher's
   precondition
4. The stale `public-data-router` fork (two artifacts, one live, ON the serving path)
5. Sweep's 6 outstanding -- **RE-SCOPED: hunting enumerations that will silently omit a firm from a
   CANONICAL ROUTE**, not monitoring gaps. **Deployed-vs-repo FIRST on every one.**

**Nothing already landed is affected** -- the two Denies, row 13, and the decommission all stand.

## ⛔ STAND DOWN (appended 19:45Z) -- 2b, THE OAC PREFIX GRANT, AND THE AUTH-INVARIANT ARE ALL **DEAD**

**Andrew ~1858Z:** *"`/json` should not even be there, the serving side is in `opal-data-portal-v2`, we
dont need a serving duplicate in `opal-data-assets`."* **`opal-data-assets/json/mdpf/` and
`json/portfolios/` are being DELETED -- that was 2b's ORIGIN.** So, DEAD, do not spend a minute:
- ❌ **2b** narrow CloudFront behavior `/api/general/mdpf/*` -> `opal-data-assets`
  (design `MDPF_LEGB_2B_DESIGN_20260728.md` is now HISTORICAL -- do NOT build from it)
- ❌ **The OAC prefix-grant ruling** (`json/mdpf/*` + `json/portfolios/*`, SourceArn pinned) -- **do NOT
  land it**; the objects it would cover are going away
- ❌ **The AUTH-invariant enforcement** -- dead with its parent

**THE FINDINGS OUTLIVED THE DESIGN and stay in the PRD as doctrine:** the nine-key hand-enumerated
allowlist + its two cottonwood omissions · *"an enumerated allowlist is a control that silently narrows as
the estate grows"* · the origin defined-and-unreferenced. **The ground moved; the costing was correct when
made.**

**NEW, ANDREW-APPROVED -- a SEPARATE EGRESS PRINCIPAL for the publisher** (serving is now
`opal-data-portal-v2` only, and `opal-assets-mdpf-portal-publisher-role` is fence-denied):
```
NEW ROLE   read   opal-data-assets/portal/gold/mdpf/*   prefix-scoped
           write  opal-data-portal-v2/platinum/mdpf/*   prefix-scoped
           on NEITHER fence
```
**RATIONALE MUST GO IN THE TF DESCRIPTION VERBATIM** or the next reader sees a fence bypass: **11 of the
12 `one-way-fan-in-fence` members are INGEST roles; the publisher is the ONLY EGRESS component on the
list, swept in because it is named `opal-assets-*`.** A new egress principal leaves the fence enforcing
exactly what it was built for. **Removing the publisher from the fence reaches the same place by
WEAKENING the guardrail -- we are not doing that.**
⚠ **Read path is `portal/gold/mdpf/*`, NOT `gold/mdpf_revamp/*`** -- locked layout
`opal-data-assets/portal/{layer}/{product}/{scope}/{artifact-type}/{YYYY-MM-DD}.json` (PRD §16).
**Scope to the TARGET tree, not today's.**
⚠ **This grants a NEW principal read on a bucket it has never touched -- the EXACT shape that bit me at
16:39Z. Simulate the caller (with `--context-entries` for conditioned statements) BEFORE relying on it,
separately-invoked negative control for prefix-scope, targeted apply, verify on the live primitive.**

**QUEUE NOW:** 1. `PIPELINE_MAP` + the Rule-12 class (**the class matters more than the instance**) ·
2. this egress principal · 3. Stage 6's three grants · 4. the stale `public-data-router` fork ·
5. the sweep's 6 outstanding (re-scoped to canonical-route omissions, deployed-vs-repo first).

## 🔴 STAGE 6 GRANTS ARE NOW #1 -- AND THE `|| return 1` FINDING (appended 19:47Z)

**They are NOT housekeeping.** `0.4.0_DS` source-confirmed in `mdpf-daily-dispatch.sh`:
```
:523  build_dim_model_portfolio.py   --date $cot_date --upload || return 1   <- the AccessDenied
:524  build_cottonwood_mdpf_pair.py  --date $cot_date --upload || return 1   <- NEVER EXECUTED
:525  build_cottonwood_mdpf_slice.py --upload                  || return 1   <- NEVER EXECUTED
```
`:525` is what writes `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json`. **`:523`'s AccessDenied
short-circuited the block before either cottonwood emitter ran.**

>> **STAGE 6 rc=1 AND THE MISSING COTTONWOOD ARTIFACT ARE ONE DEFECT, NOT TWO. Three of us tracked them
separately all day. NEITHER SYMPTOM, READ ALONE, POINTS AT THE OTHER** -- an IAM gap presented as a missing
artifact three steps downstream, with nothing in either signal naming the link. **This is a FIFTH mechanism
on cottonwood and unlike the other four it was INVISIBLE TO ENUMERATION -- it lived in shell control
flow.** Worth more than the fix. <<

**I DECLINED TO START IT, deliberately: NEVER#6** (a begun deploy FINISHES in-session). I could not
guarantee edit -> apply -> 6-control verification, and **a half-landed IAM change on the role carrying both
live Denies is worse than a 10-minute delay.** *(Noted for accuracy: this is NOT the 16:39Z shape -- that
was a NEW principal on an untouched bucket; this is an EXISTING role already measured against this exact
prefix today. Lower risk; the binding constraint was finishing the verification, not the grant.)*

### PRE-COMPUTED SPEC -- next session lands it in ~10 min
`infra/aws/terraform/mdpf-pipeline/iam.tf`, on `aws_iam_role_policy.mdpf_runner`, mirroring the
`AssetsSchwabRpsS2GateRead`/`GateList` pair landed 16:44Z:
```
Sid AssetsCottonwoodGoldWrite  Allow s3:PutObject, s3:GetObject
    arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/gold/*
    ** GetObject is NOT redundant: build_dim_model_portfolio.py:383 head_objects AFTER the put,
       and HeadObject IS s3:GetObject. PutObject alone moves the failure one line down. **
Sid AssetsCottonwoodGoldList   Allow s3:ListBucket
    arn:aws:s3:::opal-data-assets  Condition StringLike
      s3:prefix = ["blackdiamond/cottonwood/gold/*"]      ** NEVER bucket-wide -- firm separation **
```
`TMPDIR=<writable> .tools/safe-apply.sh -chdir=infra/aws/terraform/mdpf-pipeline apply
-target=aws_iam_role_policy.mdpf_runner` (TMPDIR makes comp-tagauthz self-run: 4 clean applies today,
zero overrides). **Tree frozen; row 10 must not ride along.**
**6 controls, isolated calls, one `--resource-arns` each:** T1 PutObject cottonwood gold key -> allowed ·
T2 GetObject same key (the `:383` verify) -> allowed · T3 ListBucket +context
`s3:prefix=blackdiamond/cottonwood/gold/` -> allowed · C1 ListBucket +context `schwab/08242234/silver/`
-> deny · C2 PutObject cottonwood **SILVER** -> deny · C3 PutObject `json/mdpf/global/...` -> explicitDeny
(leg-1 still holds).
**REAL TEST = the next scheduled run:** `:523` passes -> `:524`/`:525` execute -> cottonwood's
`aggregate_aua_timeseries.json` appears -> Stage 6 rc=0 -> **`cycle-complete.json` emitted for the FIRST
TIME EVER.**

## MY OWN ERRORS TODAY, CONSOLIDATED (so they are not scattered across comms)
1. **"Blocked until 49F clears"** -- inherited the gate's own verdict without asking what object produced
   it (NEVER#1 clause 2). Corrected in ~20 min on COO's challenge.
2. **"7 other roles"** -- was 6 roles + 1 managed policy; imprecise in the direction that understates.
3. **Broke the gate** -- re-pointed a reader at a bucket its role could not read. Verified the data was
   there; never verified the caller could reach it. **The Rule-22a battery was real and aimed at the wrong
   principal.**
4. **"Three allowlist omissions"** -- was TWO; inflated in the direction that made my own finding bigger.
   Caught by a precondition aimed at something else.
5. **JSON round-trip mojibake'd six unrelated manifest entries** -- caught pre-commit because a pure
   deletion must have zero added lines.
6. **"It exists, IT RUNS"** -- inferred a RUNTIME claim from a SOURCE FILE, in the sentence crediting
   myself for refusing an unverified alarm 3h earlier. **BOUND AS A RULE: a claim about what an instrument
   DOES is a claim about a RUNTIME -- establish deployment first, or say INFERRED-FROM-SOURCE in the same
   sentence.**
7. **"Routed to DS"** -- I stated it as done at the moment I decided to do it, and never sent it. Harmless
   only because CTO withdrew the ask. **"I will route it" and "it is routed" are different claims.**

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
