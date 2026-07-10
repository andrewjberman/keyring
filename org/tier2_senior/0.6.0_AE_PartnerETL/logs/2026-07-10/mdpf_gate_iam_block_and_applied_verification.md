# 0.6.0_AE_PartnerETL -- 2026-07-10T00:05Z .. 00:41Z: the IAM block, the deploy, and the APPLIED verification

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, COORDINATE

## Window

Continues `8941f6fe8` (23:03Z-00:05Z). Zero code authored by me: I am REVIEWER on the mdpf per-partner
gate (CTO `230737Z`, designer != author). Andrew GO'd the deploy mid-window; it landed at `00:21Z` and I
verified it APPLIED. Watch ran throughout, S3-only, uninterrupted.

## 1. RE-REVIEW OF `23085840f` -- BLOCK on IAM (no `[STOP]` spent)

`0.5.0`'s revised diff carried all three of my must-fixes. **Its fix for (C) is what broke it.**

`_roll_source_exists(as_of)` -> `s3.head_object(Bucket=PLATINUM_BUCKET, ...)` with `except Exception:
return False` -> DEFER. `PLATINUM_BUCKET = "opal-data-portal-v2"` (`:88`). **The trigger's execution role
had no grant on that bucket.** Grounded three ways, one of them a falsifier hunt:

```
1. APPLIED    get-role-policy mdpf-daily-trigger-lambda-role / mdpf-trigger-scoped (full doc)
                s3:GetObject only on opal-data-inf/gold/meta/pipeline-complete.json
                                     opal-data-bd/silver/{allocations,fees}/*, schwab/silver/rps/*
                DENOMINATOR "portal-v2" occurrences in role = 0
2. FALSIFIER  get-bucket-policy opal-data-portal-v2 -> AllowCloudFrontOAI + AllowCloudFrontOAC only.
                (A same-account bucket policy CAN grant independently of the role. It does not.)
3. AUTHORITATIVE simulate-principal-policy(role, s3:GetObject, .../aggregate_aua/2026-07-06.json)
                -> Decision: implicitDeny
```
**Not drift:** `iam.tf` `:124-175` portal-v2 grants belong to `aws_iam_role_policy.mdpf_runner`;
`aws_iam_role_policy.mdpf_trigger_lambda` (`:282`) never had one. **The grant was never written.**

**Consequence on the FIRST fire:** `49financial` is stale (`behind=3`) -> `_partner_asof` = `2026-07-06`
-> `head_object` -> AccessDenied -> `except Exception` -> `False` -> `unresolvable` -> **DEFER, every day,
silently.** The exact failure the deploy exists to end, **wearing the costume of the fail-safe added to
prevent a different one.**

**Why `0.5.0` missed it:** it reported *"LIVE: `_roll_source_exists('2026-07-06')=True`"* -- exercised
under **its own credentials.** The Lambda runs as the role. **It exercised under the wrong PRINCIPAL; I had
exercised under the wrong BRANCH two hours earlier.** Same error, adjacent axis.

**MUST-FIX (adopted verbatim by CTO):** `except Exception` collapsed three worlds into one `False` --
**404** (block absent, a DATA condition, expected), **403** (the instrument is broken, a CONFIG fault that
NEVER clears), transient. *A permanent silent DEFER from a missing grant is indistinguishable from a
legitimate one.* Split into `ROLL_SOURCE_ABSENT` / `ROLL_SOURCE_UNREADABLE` / `ROLL_SOURCE_TRANSIENT`,
stamped into the `decision` dict so `mdpf-freshness-checker` alarms on UNREADABLE and never on ABSENT.
**A fail-safe that cannot say why it fired is a mute alarm.**

**No `[STOP]`.** `0.5.0` was already holding the apply pending my clearance; the interlock is not spent
where a verdict does the job. CTO confirmed the block independently **with a positive control** (`inf`
bucket -> `allowed`) -- *without which an `implicitDeny` is indistinguishable from a mis-invoked simulator.*

## 2. `comp-iam` IS A CLAUDE.md-LEVEL DEFECT (CTO ruled, both limbs)

```
comp-iam service mdpf-daily-trigger  ->  s3:GetObject [GRANTED]  via s3.head_object at lambda_function.py:345
                                                                      ^^^ the call that returns AccessDenied
```
**It matches the ACTION NAME and never compares the RESOURCE ARN.** The role holds `s3:GetObject` -- on
three *other* buckets. **A new call against a fourth reports GREEN.** CLAUDE.md's AE minimum (*"`comp-iam
gaps` after adding any new boto3 call"*) **would have cleared this bug.** The file warns comp-iam DESIRED
cannot tell landed-from-planned; **it does not warn that it cannot tell bucket-from-bucket.**

`existence` for `rows` | `filename` for `content` | `coherence` for `correctness` | `delivered` for
`channel push` | **`action` for `resource`.**

**CTO ruled:** (1) amend the AE minimum -- a new boto3 call against a **new bucket/ARN** is verified with
`simulate-principal-policy` **plus a positive control**; comp-iam is necessary and not sufficient.
(2) `comp-iam` must resolve each call's resource ARN against the statement `Resource` and report
`GRANTED-ACTION / UNGRANTED-RESOURCE` distinctly -- routed to `0.8.0` with a **negative-control fixture**:
a call to a bucket the role does not hold **must RED**. *An assertion that has never failed has never been
tested.*

## 3. DEPLOYMENT SEQUENCE + VERIFICATION (AE role requirement -- actual output)

**Deployed by `0.5.0` at ~00:21Z** (Andrew-direct GO via CTO `001053Z`): IAM + Lambda code + the 403/404
split, ONE plan, ONE ledger. Tag `mdpf-pipeline-v1.4.0` -> `ed67e1b02`, **present on origin**. Ledger
`org/critical_paths/change_management/20260710T0013Z_mdpf-per-partner-gate-deploy_deploy_completion.md`
opened at deploy-start, closed at completion (NEVER#6).

**Baseline PINNED PRE-APPLY** (so "changed" is provable, not asserted):
`CodeSha256 = Cei1TsbP27C2g1wAVRWroBZro+JrmB/SeL5xHqHMGHg=`, `LastModified 2026-07-01T21:14:05Z`,
`portal-v2` statements in role = 0, `simulate -> implicitDeny`.

**My independent verification (`scratchpad/verify_applied.sh`), actual output:**
```
1. IAM APPLIED
   Sid "PlatinumRollSourceRead"  Resource arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/aggregate_aua/*
   DENOMINATOR portal-v2 statements = 1
   GUARD bucket-wide ('portal-v2/*' | bare bucket ARN) = 0            <- NOT widened

2. IAM EFFECTIVE  (simulate-principal-policy, mdpf-daily-trigger-lambda-role, s3:GetObject)
   TARGET   platinum/mdpf/aggregate_aua/2026-07-06.json   -> allowed
   CONTROL+ opal-data-inf/gold/meta/pipeline-complete.json -> allowed        (simulator is sane)
   CONTROL- opal-data-portal-v2/json/market-overview.json  -> implicitDeny   (grant is NOT bucket-wide)

3. CODE APPLIED
   CodeSha256  Cei1TsbP... -> Y5py4xQ3Ar4CoIy13LuGpt1gF0Oa1qQRS1jjFCKVzMU=   CHANGED
   DEPLOYED zip (get-function -> Code.Location -> unzip), NOT the repo:
     MDPF_STALE_PARTNERS 3 | spine_fresh 2 | _roll_source_exists 2
     ROLL_SOURCE_ABSENT 5 | ROLL_SOURCE_UNREADABLE 4 | head_object wrapped in `except ClientError`

4. THE OTHER TWO ARTIFACTS (a Lambda is one third of this deploy)
   data/mdpf/scripts/gold/mdpf_aggregate_aua.py -> comp-pipescript deployed = MATCH
   s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh -> written 00:18:56Z, CONTENT-checked:
       is_stale_partner() present, MDPF_STALE_PARTNERS x4, IDENTICAL to the committed revision
   git status on all three deployed paths -> clean (deployed content == committed content)
```
**The negative control is the check that matters.** An `allowed` on the target is also consistent with
someone granting `portal-v2/*`. It isn't bucket-wide. **I checked the dispatch script by CONTENT, not
mtime** -- a fresh timestamp is an existence proxy, the very thing under indictment.

### VERDICT: `APPLIED-VERIFIED, NOT-EXERCISED`
Stated in those words on purpose. The next INF spine sentinel is **~15:03Z**; there has been no fire since
the apply. **A config read is not a behavioral claim** (22a). Nothing has run and nothing serves.

## 4. ONE LATENT FINDING SHIPPED (accepted by `0.5.0`, queued -- NOT a rollback)

```python
if not as_of:
    return (False, "ROLL_SOURCE_ABSENT")   # runs BEFORE any S3 call
```
`ROLL_SOURCE_ABSENT` is defined as *"404: the block is genuinely not there. A DATA condition, expected"* --
the one reason `mdpf-freshness-checker` is told never to alarm on. But `not as_of` means **`_partner_asof`
could not RESOLVE the vintage** -- a config/upstream fault that may never clear -- and it lands in the
branch that fires **when RPS stops landing**, which is the sovereign-frozen state we are in.
**It re-creates the exact conflation the 403/404 split just removed, one branch earlier.**

**Fix:** a fourth reason `PARTNER_ASOF_UNRESOLVED` (config-class, loud). `ROLL_SOURCE_ABSENT` reserved for
*"as_of resolved AND head_object returned 404."*

**Not re-blocked:** it DEFERs -- never skips, never rolls a wrong block, never serves a wrong number -- and
is **unreachable today** (the schwab scalar `2026-07-06` resolves). **Blocking a correct deploy over an
unreachable branch would be my `[STOP]` error of two hours ago with the sign flipped, and Andrew's
deliverable would pay for it.** `0.5.0` additionally declined to land it tonight because committing without
a same-session apply would create **committed-but-not-deployed drift** -- the exact "landed != applied" lie
we spent the night convicting. Queued to ride the 15:03Z cycle.

## 5. Corrections I made to my own record this window
1. **Predicted `comp-pipescript deployed` would report UNCOVERED for mdpf and that a MATCH would be
   suspicious. WRONG** -- it covers the mdpf gold tree and correctly reported `mdpf_aggregate_aua.py MATCH`.
   It covers **neither the Lambda nor the EC2 dispatch shell script**; I verified those separately.
   **Nobody should cite `comp-pipescript deployed MATCH` as evidence the Lambda deployed.**
2. CTO credited my *"blocking is free"* withdrawal with saving Andrew's fix. **Recorded as his, not mine:**
   I did not find that claim false by re-reading my own work -- I found it because he refuted the premise
   (`custody_source="schwab"`) underneath it. **Two of three retractions were self-initiated; that one was
   not.**

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-iam service` | `mdpf-daily-trigger` | **FAIL (false-GREEN)** | Reported `s3:GetObject [GRANTED]` for the `head_object` at `:345` -- **the call that returns AccessDenied.** Binds the ACTION name, never the RESOURCE ARN. CTO ruled it a CLAUDE.md-level defect; routed to `0.8.0` with a negative-control fixture. |
| `comp-pipescript deployed` | `data/mdpf/scripts/gold/mdpf_aggregate_aua.py` | **PASS** | `[mdpf:gold] MATCH`, 1 MATCH / 0 STALE. Confirmed the gold half of the deploy landed on `s3://opal-data-mdpf`. |
| `comp-pipescript deployed` | no-arg sweep (inside verify harness) | **PASS** | 59 MATCH / 0 STALE / 12 UNCOVERED across bd/inf/cot/mdpf trees. **Does not cover Lambdas or EC2 shell artifacts** -- stated so it is never cited as such. |
| `simulate-principal-policy` | role x action x exact key, **+ pos & neg controls** | **PASS** | Not a comp tool, and it is the ONLY instrument that answered the question. This is the gap. |

**What worked:** `simulate-principal-policy` with a positive **and** negative control settled in one call
what `comp-iam` got backwards. `comp-pipescript deployed` cleanly proved the gold artifact landed.

**What failed:** `comp-iam service` -- a **false GREEN on a served-money deploy.** It is the instrument
CLAUDE.md obliges AE to run after a new boto3 call, and on this call it cleared the bug.

**GAP FOUND (routed, and it subsumes the `comp-path` gap I filed in `8941f6fe8`):** nothing in the estate
answers **"does this call, on this BRANCH, as this PRINCIPAL, against this RESOURCE, actually succeed in
production?"** Tonight's three exercise failures -- my branch, `0.5.0`'s principal, `comp-iam`'s resource --
are **one missing tool, not three findings** (CTO's framing). Banked to memory as
`feedback_exercise_is_evidence_only_for_its_identity_branch_environment`.

## Blockers

**None.** The IAM blocker I raised is **CLOSED** (grant applied, verified `allowed` with controls). The
latent `PARTNER_ASOF_UNRESOLVED` bug is queued, unreachable, and fails safe -- an open follow-up, not a
blocker. The watch is read-only and unimpeded.

## Current State

- **`mdpf-pipeline-v1.4.0` DEPLOYED + APPLIED-VERIFIED, NOT-EXERCISED.** `mdpf-daily-trigger`
  `CodeSha256 = Y5py4xQ3Ar4CoIy13LuGpt1gF0Oa1qQRS1jjFCKVzMU=`. IAM `PlatinumRollSourceRead` applied,
  key-prefix scoped, `simulate -> allowed` with pos+neg controls. Aggregate + dispatch script on S3,
  content-verified. Tag on origin. Ledger closed. Nothing half-landed.
- **Nothing serves until the ~15:03Z INF spine sentinel.** Inflection has not advanced since
  `2026-07-08T14:58Z`; the whole `$1,860,979.88` gap is the DEFER (RPS `behind=3 > max_lag=2`), not a feeder
  bug. **The deployed-before-tonight code would have DEFERred again at 15:03Z** -- the deploy is Andrew's
  deliverable, not an improvement on it.
- **Watch RUNNING, S3-only, no vendor call.** curve **pt5 00:30:53Z CLEAN, no delta vs pt3/pt4**;
  `[FREEZE-RISK]` not entered; 07-09 NOT POSTED. Timer armed for **pt6 + txnwatch pt3 at 01:00Z**;
  then pt7 01:30Z, txnwatch 01:40Z, **02:30Z primary = cot half ONLY** (bd half sovereign-cancelled).
  Harnesses: `scratchpad/{curve_pt3_readonly,txnwatch_pt,exercise_gate_predicate,verify_applied}.{py,sh}`.
- **Memory banked (survives session):** `feedback_curve_watch_is_a_live_vendor_call_killed`,
  `feedback_exercise_is_evidence_only_for_its_identity_branch_environment`,
  `project_pending_trigger_mdpf_gate_first_fire_verify` (+ `MEMORY.md` ACTIVE TIME-TRIGGER for 15:10Z).
- **49F / Schwab / RPS / bd-custody: sovereign out-of-scope, honored.** No file under those trees opened,
  no bd write, neither `bd-49f` ledger touched, no vendor call on either plane.

## Next Steps

1. **[0.6.0_AE_PartnerETL]** curve pt6 + txnwatch pt3 (01:00Z), pt7 (01:30Z), txnwatch (01:40Z);
   **02:30Z primary, cot half only** -- read `s3://opal-data-cot/logs/cot-exporter/bronze-run/<ts>.log` for
   the `REJECT:` line, re-confirm cot silver row counts unchanged. S3-only.
2. **[0.6.0_AE_PartnerETL, act on/after 2026-07-10T15:10Z]** The **behavioral** verdict on the gate's first
   production fire. Read the SERVED `platinum/mdpf/aggregate_aua/2026-07-10.json`: `dispatched:true`,
   `stale_partners:["49financial"]`, 49F rolled VERBATIM from 07-06 (`non_model_aua = 196,913,158.63`,
   **not** 07-08's fabricated `207,293,583.56`), `as_of_by_partner['49financial']='2026-07-06'`,
   `source_vintage.overall = BEHIND`, Sentinel 3 naming its carried fraction, **Inflection's row ADVANCING
   on the same run.** Read it off the artifact, not the log line that says it worked.
3. **[0.5.0_AE_OpalETL]** Land `PARTNER_ASOF_UNRESOLVED` (config-class, loud, alarm-able) on the same cycle;
   `safe-apply` + my re-review. Reserve `ROLL_SOURCE_ABSENT` for "as_of resolved AND 404."
4. **[0.8.0]** `comp-iam` resource-ARN resolution + `GRANTED-ACTION / UNGRANTED-RESOURCE`, with a
   negative-control fixture that must RED. Also: port the content assertion to `bd-cot-freshness-probe`
   (until then cot's `-stale-allocations`/`-unrealized` alarms read GREEN on a dead table).
5. **[1.0.0_SA_CTO]** Land the AE-minimum amendment in CLAUDE.md (new boto3 call against a NEW bucket/ARN ->
   `simulate-principal-policy` with a positive control; comp-iam necessary, not sufficient).
