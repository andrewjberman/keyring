# MDPF_HEALGAP decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~G1, dell1; cut 2026-10-07 ~08:5xZ)

**Status: ISSUED** in one issuance. Seat: `0.0.0_AB_MSTR~DELL1` msg 29 (SPAWN-DIRECT), on laptop `1.0.0_SA_CTO` placement msg 106053;
Andrew-direct ~07:15Z relayed there: "the COOs should be running /canonical-drive on their projects".

**Cut on:** PRD v0.1 @78db344481 (L4-R ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO` @53596a3131; brief half admitted because the
CRO wrote the brief). Brief `docs/briefs/mdpf-healgap-midstream-brief-20261007.md` @a8c67a424e.

## The thread (PRD section 2, FWD-1) and its hops, measured at the base 2026-10-07 ~08:3xZ

| hop | what | today | cell |
|---|---|---|---|
| 0 read | why model_detail stopped 2026-09-01..09-10; the guard's state | measured here, no cell (below) | none |
| 1 fail | the 06:00Z pull fails on a lapsed login | `cot-rebalancer-runner-daily` ENABLED `cron(0 6 * * ? *)`; a lapse raises at `mint_rebalancer_bearer` (`lambda_function.py:145-152`), two async retries, no `on_success`. No way to make it fail on purpose without touching the login | `HG-t-1` (the induced lapse) |
| 2 heal | the session chain mints or re-uses a login | `cot-bd-session-daily-et` 07:30 America/New_York; both legs (Lever-A skip and mint) end in `opal-cot-bronze-run`, which writes `s3://opal-data-cot/bronze/<date>/_BRONZE_COMPLETE.json` LAST. Measured 10-01..10-06: one sentinel a day at 11:31-11:32Z, same UTC date as the 06:00Z pull | none: works, relied on (C-SESSION) |
| 3 re-attempt | the runner re-runs for the date only if incomplete | NOTHING re-runs. And the guard is dead: `_already_landed` (`lambda_function.py:211-218`) reads the stamp with `s3:GetObject`, which the role does not hold (`comp-iam service cot-rebalancer-runner`: `s3:GetObject [UNGRANTED]`, 2026-10-07), so it falls open and re-pulls on every invocation | `HG-t-1` (guard), `HG-t-2` (wire) |
| 4 chain | three feeds land; `on_success` carries them to silver, then gold | live: `MaximumRetryAttempts 2`, `MaximumEventAge 21600`, OnSuccess `opal-assets-silver-blackdiamond` (`get-function-event-invoke-config`, 2026-10-07) | none: works |
| 5 page | the reader sees the day's Cottonwood figures | unchanged | none: the COO's one real run at close |

**Hop 0, measured at the base (no vendor call):**
- **Cause of 2026-08-31..09-10:** the count-reconcile self-gate RAISED after `rebalancer_models` and `rebalancer_accounts` landed and before
  `rebalancer_model_detail` (account 26725961 left `/api/accounts/search` while BD kept `accountCount`). Carried at HEAD in the docstring of
  `_reconcile_counts` (`lambda_function.py:334-394`) and fixed by `c53e48f7fb` (committed 2026-09-11T02:17Z); deployed bytes LastModified
  2026-09-11T03:26:00Z. Claim: **held** (the fix commit's own measurement), corroborated by the stamp census: `meta/2026-09-0*-complete.json`
  ABSENT, `meta/2026-10-01..07-complete.json` PRESENT (each ~06:01Z). The runner's own log line for those days is unrecoverable: the log group's
  retention is 14 days (`describe-log-groups`). So the cause is a SECOND cause class (a vendor-counter gate), not session death, and it is closed.
- **Guard:** dead on the DESIRED plane (above). The APPLIED plane is unread: `iam:SimulatePrincipalPolicy` is denied to the dell1 agent user.
- **For FWD-3 (enrichment 2):** the runner sends NO as-of to Black Diamond (`date` only keys the landing, `lambda_function.py:400-458`). Row
  `MDPF_HEALGAP-S2`.

## Rule 24

Domain: the FWD-1 thread, hops 0-5. Hop 0 is measured above; hops 2, 4 and 5 work today. The remainder is two write sets with one intent each:
the runner's own code (`HG-t-1`: the guard that makes a second attempt safe, and the induced lapse that makes hop 1 exercisable, both inside
`ingest()`'s entry), and the wiring that makes the second attempt happen (`HG-t-2`: Terraform in the runner's root). No remainder. Same grain:
each cell is one adapter of the thread. State coherence: neither cell moves the per-feed run result (enrichment 1, FWD-2), the repair of old
dates (FWD-3), the retry/age settings (FWD-4), the 06:00Z fire time (FWD-5) or the class census (FWD-6).

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `HG-t-1` | The runner's guard reads the complete-stamp by LISTING (the role holds `s3:ListBucket` on `blackdiamond/cottonwood/*`), not `GetObject`, so a complete date skips before the session secret is read; and an event key `"induce": "auth-lapse"` raises the same HTTP 401 error a lapsed login raises, after the guard and before the session read, so hop 1 can be made to fail without touching the login | FWD-1 | NOT-EVALUATED | dell1 (code); deployed by the issuer at the drain | WORLD | A, `0.9.0_WK_MDPF_HEALGAP~1` |
| `HG-t-2` | The re-attempt: a second target on the existing `cot-bronze-complete` rule invoking `cot-rebalancer-runner` with `{"mode":"pull"}`, plus the invoke permission scoped to that rule, in a new file in the runner's Terraform root (opal-assets); a step of the existing chain (C-ONE-PIPELINE), no new schedule, rule or output path | FWD-1 | NOT-EVALUATED | dell1 (code); applied by the issuer at the drain | WORLD | B, `0.9.0_WK_MDPF_HEALGAP~2` |

## Write sets (disjoint)

- **HG-t-1:** `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py`,
  `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/test_healgap_guard.py` (new), the surprise channel.
- **HG-t-2:** `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf` (new), the surprise channel.
- Checks (issuer's, dry-run at the base, all FAIL as expected; the seam instrument's own controls PASS on `cot-bronze-complete` and REFUSE
  `cot-silver-complete`): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/`.

## Edges and fan-out

No data edge: `HG-t-2` declares a target and consumes no output of `HG-t-1`. The ORDER of the two at the drain (guard deployed before the
target is applied, C-IDEMPOTENT) is a drain act, not an edge. `fanout: 2 of 2 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round; no schedule changes (the re-attempt is an event target on an existing rule).
- `comp-iam`: RUN (`comp-iam service cot-rebalancer-runner`, 2026-10-07): 4 call sites; `s3:ListBucket` GRANTED, `s3:GetObject` UNGRANTED,
  2 UNRESOLVABLE-RESOURCE (`PutObject`, `GetSecretValue`). The guard's repair uses the GRANTED call, so the round needs no IAM write. The new
  `aws_lambda_permission` is a resource policy on the runner (principal `events.amazonaws.com`), not a role grant. Blindness, as the tool states
  it: 10 Deny statements unparsed, and DESIRED plane only (simulate is denied to the dell1 user).
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface.
- C-NAMES: the round mints no resource name. `target_id` and `statement_id` are sub-resource ids; `lib/opal_naming.py`'s schema maps neither
  `aws_cloudwatch_event_target` nor `aws_lambda_permission` (`tf_type_map`, `tf_unmapped_own_name`, `not_covered`, read 2026-10-07).

## The issuer's acts at the drain (not cells)

1. **Deploy `HG-t-1` (WORLD):** build-and-upload of the runner zip and `safe-apply` of opal-assets for the code only, under a change-management
   entry. It adds no vendor call (the guard removes calls). Then read the deployed code against the build input.
2. **Before applying `HG-t-2`:** read how `opal-assets-silver-blackdiamond` treats an `on_success` envelope whose `responsePayload.verdict` is
   `SKIP-IDEMPOTENT`, because once the re-attempt exists the runner returns cleanly TWICE on a normal day and the destination fires twice.
3. **Apply `HG-t-2` (WORLD), held on ACT 1:** the target makes a second Rebalancer call on any day the morning failed. That is the standing
   vendor word the PRD's ACT 1 names, so the apply waits for it. A never-widen half (CTO + COO) names the blast radius: bronze keys for that UTC
   date under `blackdiamond/cottonwood/bronze/`, the stamp, and the silver/gold chain the existing `on_success` drives; rollback = remove the
   target.
4. **The one real run of FWD-1, held on ACT 1:** for one morning set the 06:00Z target's input to `{"mode":"pull","induce":"auth-lapse"}`,
   restore it the same day, then read that UTC date's three feeds and the reader's Cottonwood page by end of day. The next natural failure is the
   negative arm.


---

# ROUND 2 -- the ENRICHMENT (issuer 2.0.0_SA_COO~G1, dell1; cut 2026-10-08 ~15:xxZ)

**Status: ISSUED** in one issuance. Round 1 above is FROZEN (FWD-1 REALIZED, CTO round-1 analysis @475c742f71).

**Cut on:** PRD v0.2 (L4-R ADMITTED 2026-10-08 ~14:4xZ: ratified-text half re-SIGNED by `3.0.0_SA_CVO` at the current ENDPOINT
hash; brief half admitted because the CRO wrote the brief; FWD-3 wording finding @4d5c4ef70e). The rectangle is the CTO's round-2
ENRICHMENT LIST (`CTO_ROUND_ANALYSIS_MDPF_HEALGAP_ROUND_1_20261008.md` section 3), five items, plus msg 994 (FWD-3 joins). Seats: dell1
only (laptop CTO 106882).

## Measured at the base, 2026-10-08 ~14:5xZ

- **Runner async settings (FWD-4):** `get-function-event-invoke-config cot-rebalancer-runner` = `MaximumRetryAttempts 2`,
  `MaximumEventAgeInSeconds 21600`, OnSuccess `opal-assets-silver-blackdiamond`. Declared at
  `cot_rebalancer_runner.tf:222-239`, with a comment calling them "the AWS defaults". On a function error the async engine retries at most
  twice, ~1 and ~2 minutes apart; the age only bounds queue wait. The 6-hour age is a window no failed pull ever gets.
- **Schedules (FWD-5):** `cot-rebalancer-runner-daily` = `cron(0 6 * * ? *)` UTC, ENABLED (declared `:168-173` with "PLACEHOLDER 06:00Z").
  `cot-bd-session-daily-et` (EventBridge Scheduler) = `cron(30 7 * * ? *)` America/New_York, ENABLED -> 11:30Z in summer, 12:30Z in winter.
  Session sentinel `opal-data-cot/bronze/<date>/_BRONZE_COMPLETE.json`, 10-01..10-08: 11:31:34Z-11:34:15Z (1.5-4.3 min after the fire).
  The 13:30Z gold floor run reads silver at 13:30Z. A UTC pull at 12:45Z sits 75 min (summer) / 15 min (winter) after the session fire
  and 45 min before the floor; the cell re-derives this first (C-SESSION).
- **Per-feed result (FWD-2):** the runner prints a verdict line and writes `meta/<date>-complete.json` LAST on a clean day; a day missing
  a feed (2026-08-31..09-10) wrote no stamp and NO record of which feed was missing -- the cause had to be reconstructed from a
  docstring (round 1 hop 0). Nothing per-feed is readable without logs, and the log group keeps 14 days.
- **FWD-3:** the vendor serves current state only (row S2; `lambda_function.py:400-458` sends no as-of). So a hole is repairable only on
  the day it opened, and the eleven days 2026-08-31..09-10 can only be MARKED missing. The CTO's FWD-3 DONE WHEN: one hole repaired by
  one act on the day it opened, the hole induced on purpose as FWD-1's was, and the eleven days read as marked-missing.
- **FWD-6:** the PRD names the 49F login chain first; the population (every scheduled pull whose login is kept alive elsewhere) is unread.

## Rule 24

Domain: the five enrichment items, one cell each. FWD-4 and FWD-5 both edit `cot_rebalancer_runner.tf`, so they are ONE chain (t-4 then
t-5, one worker), two cells because they have two intents. Same grain: each cell is one adapter. State coherence: t-3 does not move the
settings, the schedule or old dates; t-4 does not move the fire time; t-5 does not move retry behaviour; t-6 never fetches a past date and
never writes a feed key for the eleven days; t-7 writes nothing outside its document.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-3` | The runner records, on EVERY run, a per-date result `meta/<date>-result.json`: per feed `arrived` / `missing`, `landed_at`, and `healed_at` when a later run fills it; verdict `COMPLETE` only when all three arrived. A run missing a feed writes `PARTIAL`, writes no complete-stamp, and RAISES (so the async engine does not call it a success). New induce `"drop-feed:<feed>"` skips writing exactly that feed, so FWD-2 (and FWD-3's same-day hole) can be made on purpose | FWD-2 | dell1 code; deployed by the issuer at the drain | WORLD | A, `0.9.0_WK_MDPF_HEALGAP~3` |
| `HG-t-4` | The runner's async settings made true: `maximum_event_age_in_seconds` set to cover the 3-minute retry chain and no more (900), the comment corrected, and `retry_schedule.py` `predict(retries, age)` returning the attempts and last-attempt offset the engine actually uses | FWD-4 | dell1 code; applied at the drain | WORLD | B, `0.9.0_WK_MDPF_HEALGAP~4` |
| `HG-t-5` | The daily pull moved after the session refresh in both summer and winter, with the 13:30Z floor margin re-derived first: `schedule_expression` of `cot_rebalancer_runner_daily` to a UTC time that passes `hg_t5_schedule.py` (12:45Z proposed), PLACEHOLDER comment replaced by the derivation | FWD-5 | dell1 code; applied at the drain under its own never-widen pair | WORLD | B (after t-4), `~4` |
| `HG-t-6` | FWD-3's two acts: `repair.py --date D` prints a MANIFEST (date, the feeds missing, the keys it will write) BEFORE any fetch, refuses any D other than today UTC with the reason, and invokes the runner for D; `mark_missing.py --from --to --feed --reason` writes `meta/<date>-missing.json` (feed, reason, marked_at) and never a feed key; both dry-run by default | FWD-3 | dell1 code; the marks and the induced-hole repair are the issuer's drain acts | WORLD | C, `0.9.0_WK_MDPF_HEALGAP~5` |
| `HG-t-7` | READ-ONLY census: every scheduled data pull whose success depends on a vendor login kept alive by something else, 49F first, each answered `RECOVERS` or `NOT-EXPOSED because ...`, with grounding and the denominator swept | FWD-6 | dell1, document only | LOCAL | D, `0.9.0_WK_MDPF_HEALGAP~6` |

## Write sets (disjoint)

- **HG-t-3:** `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py`, `.../test_healgap_result.py` (new), the channel.
- **HG-t-4 then HG-t-5:** `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf`, `.../cot-rebalancer-runner/retry_schedule.py` (new),
  the channel.
- **HG-t-6:** `.../cot-rebalancer-runner/repair.py` (new), `.../mark_missing.py` (new), `.../test_healgap_repair.py` (new), the channel.
- **HG-t-7:** `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md`, the channel.
- Checks (issuer's, dry-run at the base 2026-10-08 ~14:5xZ, each BAD as expected; `hg_t3_legacy.py` and `hg_tf_fmt.py` are regression
  guards and read OK at the base): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/`.

## Edges and fan-out

`HG-t-5 depends_on HG-t-4` (same file; one worker in order). No other data edge. `HG-t-6`'s exercise uses `HG-t-3`'s `drop-feed` induce,
but that is a DRAIN act, not a build edge: t-6 builds and tests against a stub. `fanout: 4 of 4 chains, cap 8`.

## Battery

- `comp-schedule`: RUN at the base (above) -- the runner's rule and the session schedule read live; t-5 moves one schedule under its own pair.
- `comp-iam`: the round needs no role grant. t-3 writes a new key under `blackdiamond/cottonwood/meta/`, inside the runner's existing
  PutObject grant (`cot_rebalancer_runner.tf:73-112`); t-6's marks are written by the issuer at the drain with the same prefix.
- `comp-adversary`: t-3's raise on PARTIAL changes what the async engine sees (retries x2 on a partial day, then no `on_success`): the cell's
  tests pin that the retry re-reads the result and records `healed_at`, never double-lands a feed (C-IDEMPOTENT).
- C-NAMES: no new resource name. The new S3 keys sit under the existing runner prefix (rule 30 non-application: existing pipeline).
- C-FIX-NOT-NOTIFY: FWD-2 is the run's own result read on demand; nothing notifies.

## The issuer's acts at the drain (not cells)

1. **Deploy HG-t-3 + HG-t-6's runner-side code (WORLD)** under a change-management entry, then read the deployed bytes against the build
   input. A deploy grant enumerates every tool's writes (S5).
2. **Apply HG-t-4 (WORLD):** the age change; no vendor call. Wiring-only orders omit the code-deploy recorder (S9).
3. **Apply HG-t-5 (WORLD) under its own never-widen pair:** the fire-time move. Any amendment that moves a step's time re-reads every half
   bounding that step (D1-S1). The restore-mechanism rule (CTO analysis 2.2) binds any timer armed for it.
4. **FWD-2's one real run + FWD-3's induced same-day hole (WORLD, ACT 1's standing word for the same-day re-run):** one morning the daily
   input carries `"induce": "drop-feed:rebalancer_model_detail"`; read the day's `meta/<date>-result.json` (PARTIAL, model_detail missing);
   then `repair.py --date <that day>` prints its manifest and fills it; read the result again (`healed_at`). Restore the input the same
   morning; every armed restore mechanism named and read at close.
5. **The eleven marks (WORLD, no vendor call):** `mark_missing.py --from 2026-08-31 --to 2026-09-10 --feed rebalancer_model_detail
   --reason <S2/hop-0 reason>` without `--dry-run`, then read the eleven `meta/<date>-missing.json`.
6. The 13:30Z condition's successor wording names its plane (row S11) -- in this round's never-widen halves.

## ROUND 2 AMENDMENT A1 -- cell HG-t-8 (issuer 2.0.0_SA_COO~G1, 2026-10-09 ~05:4xZ)

Ruling R2-1 (row D1-W3-S1) first carried the grant to the round-2 drain-end read. Re-ruled by the issuer on the operator's word
("If there's things you're already expecting to do downstream, why not just do them now?" ... "go ahead", 2026-10-09 ~05:3xZ, at the
`2.0.0_SA_COO~G1` terminal): nothing blocks it, and landing it before act 3 lets FWD-3's exercise read a non-null `healed_at`.

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-8` | One statement added to `aws_iam_role_policy.cot_rebalancer_runner_write`: Allow `s3:GetObject` on `arn:aws:s3:::${local.monolith_bucket}/blackdiamond/cottonwood/meta/*-result.json`, nothing else | FWD-3 (`healed_at`) | dell1 code; applied by `0.7.0_AE_CloudOps~DELL1` after act 1 L4 is read (2026-10-09 07:07Z) | WORLD | E, carried by `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/ADHOC.healgap-r2-1-runner-reads-own-result.md` (edit + apply in one lane) |

- **Write set:** `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` (no other cell of round 2 is open on it: t-4/t-5 drained @672800c42a), the channel.
- **Check:** `R2_CHECKS/hg_t8_iam.py`, dry-run at the base 2026-10-09 ~05:4xZ: base IAM-BAD (0 GetObject statements); a correct edit
  IAM-OK; a `meta/*` resource IAM-BAD; an added `s3:DeleteObject` IAM-BAD. `hg_tf_fmt.py` is the regression guard.
- **comp-iam:** the role is used by 1 of 232 us-east-1 Lambda functions (`cot-rebalancer-runner`), read 2026-10-09 01:2xZ, so the Step F
  before-rule (msgs 1249/1255) does not bind; the change is reported after the apply to `0.0.0_AB_MSTR~DELL1` (msgs 1245/1255).
- **Rule 30:** no new name or address; the resource is inside the existing runner prefix (existing pipeline, R19 non-application).
- **Edge:** none to t-3..t-7; the apply waits only on the act-1 L4 read so today's read is not confounded. `fanout: 1 of 1 chains, cap 8`.
- **Carrier:** `to-pipeline-gate.py` refused a sixth round-2 order file (ONE ISSUER PER ROUND: the round-2 issuance is closed). The cell is
  carried as one CloudOps order (one-statement edit + targeted apply), under an audited `# pipeline-override`, as the partner_roster deploy was.
- Gate limb that graded this modification: none (a decomposition amendment); the carrier order is graded at its cut.

## ROUND 3 -- the enrichment (issuer 2.0.0_SA_COO~G1, 2026-10-11 ~03:2xZ; PRD v0.3 @4dd05f99ec; CTO L10 answer @1974b85f4e)

Input: `ledger/ROUND_ANALYSIS.round2.md` section 3 (six items) and rulings 3411 (HG-t-11 guard in the SSM document), D, E, K.
The CTO's item numbers map to cells: item 1 = `HG-t-9`, item 2 = `HG-t-5` apply (drain act), item 3 = `HG-t-11`,
item 4 = `HG-t-10` (drain act), item 5 = `HG-t-12`, item 6 = `HG-t-13`.

### Measured at the base, 2026-10-11 ~03:1xZ

- **Satellites producer (FWD-5 prerequisite):** `satellites-registry-producer.tf` has one rule, `cot_satellites_registry_producer_daily`
  `cron(0 7 * * ? *)`, one target, one permission. The handler (`infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py`)
  passes no event field to `producer.main` and reads no stamp. The role's S3 policy (`cot_satellites_registry_producer_s3`) reads only
  `bronze/rebalancer_models/*` and `bronze/rebalancer_model_detail/*`, and has **no `s3:ListBucket` anywhere, by design** (the file's own
  comment). Consequence found at the cut: a stamp read without `ListBucket` returns 403 for an ABSENT key, indistinguishable from a
  missing grant. The cell therefore adds one prefix-conditioned `ListBucket` so absent reads 404 and a grant fault stays loud.
- **Asset-dim re-attempt (FWD-6):** `bd_asset_dim_pipeline` `cron(10 22 ? * MON-FRI *)`; the trigger Lambda has no guard; its role
  `bd_daily_trigger` is shared by 7 triggers and holds no S3 or `ssm:ListCommands` read. The pull is now the REST path (no Playwright):
  it mints from the 49F session secret and writes `bronze/assets_dim_rest/<UTC date>/assets_dim_rest.parquet` (key from the generated
  pin `_asset_dim_rest_pin.py`), then rebuilds `silver/bd_assets_dim.parquet`. **Ruling 3411 named `silver/assets/<D>.parquet`, which is the
  Playwright-era artifact; the guard keys on today's bronze partition instead** (issuer's ruling inside this decomposition, same intent:
  today's pull has landed). Accepted residual: bronze present and the dim rebuild failed reads "complete" until the next day's run.
- **FWD-6 population:** 164 scheduled pulls live (CVO read) against the census's 162 (row D1-C-S15).
- **Row S1:** `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:548-556` runs the builder, pair and slice only when
  `build_cottonwood_mdpf_slice.py` is staged in the runner's `assets_gold`; whether it is staged is unread.

## Rule 24

Domain: the six items, one adapter per cell. Same grain: `HG-t-9` is one producer (rule + handler + its grant); `HG-t-11` is one
re-attempt (rule + document guard). State coherence: t-9 does not move the 07:00Z fire or the runner's fire time; t-11 does not move
the 22:10Z fire; t-12 and t-13 write only their documents. The two drain acts change a schedule or the world and are not cells.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-9` | The producer's second scheduled fire `cron(15 13 * * ? *)` with target input `{"require_stamp": true}`; the handler, on that input only, heads `meta/<UTC date>-complete.json` and rebuilds only if present (404 -> one `STAMP-ABSENT` line, nothing served; any other error raises); the role gains `GetObject` on `meta/*-complete.json` and one prefix-conditioned `ListBucket`. The 07:00Z fire and its event are unchanged | FWD-5 (prerequisite), D1-S7 | dell1 code; applied at the drain under its own never-widen pair | WORLD | A, `0.9.0_WK_MDPF_HEALGAP~7` |
| `HG-t-11` | The asset-dim re-attempt: a second rule on the same trigger at `cron(40 22 ? * MON-FRI *)` (after the 22:20Z mint), and a guard in `opal-bd-asset-dim-download`: exit 0 with the shutdown armed when today's bronze partition exists; a failed read is not "exists" | FWD-6 | dell1 code; Terraform and the document applied at the drain, document under `safe-apply` with its own pair; rollback = prior document version | WORLD | B, `0.9.0_WK_MDPF_HEALGAP~8` |
| `HG-t-12` | READ-ONLY re-sweep of every scheduled pull against a fresh count (CVO read 164), answering `schwab-canonical-si2-08403355-pull-daily` and `teams-global-transcripts-pull-hourly`, and marking the SI2 and FT pulls with v0.3's third answer, each naming the person's act and where it is listed | FWD-6 | dell1, document only | LOCAL | C, `0.9.0_WK_MDPF_HEALGAP~9` |
| `HG-t-13` | READ-ONLY: does `mdpf-daily-dispatch.sh` run the slice script on the staged runner, and is that run a no-op | row S1 | dell1, document only | LOCAL | D, `0.9.0_WK_MDPF_HEALGAP~10` |

## Write sets (disjoint)

- **HG-t-9:** `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`,
  `infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py`, the channel.
- **HG-t-11:** `infra/aws/terraform/bd-pipeline/eventbridge.tf`, `infra/aws/ssm/opal-bd-asset-dim-download.json`, the channel.
  Neighbouring project: NFRA_MCPINDEX owns the BD pipeline's history; the order's drain act re-reads its open cells before the apply.
- **HG-t-12:** `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~9/FWD6_CENSUS_RESWEEP_R3.md`, the channel.
- **HG-t-13:** `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~10/MDAILY_RUNNER_SLICE_READ.md`, the channel.
- Checks (issuer's, dry-run at the base 2026-10-11 ~03:2xZ, each BAD as expected with a GREEN control):
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/` -- `hg_r3_rules.py --t9 | --t9-iam | --t11`,
  `hg_t9_stamp_gate.py`, `hg_t11_assetdim.py --ssm`, `hg_t12_census.py`, `hg_t13_read.py`.

## Edges and fan-out

No data edge between the four cells. `HG-t-5` apply (drain) depends on `HG-t-9` APPLIED and one 13:15Z fire read back (CTO item 2).
`fanout: 4 of 4 chains, cap 8`.

## Battery

- `comp-schedule`: t-9 adds one fire at 13:15Z (after a 12:45Z landing and before the 13:30Z floor, ruling K); t-11 adds one at 22:40Z
  after the 22:20Z mint; each carries its margin in the order. The runner's fire time does not move in this round until the HG-t-5 apply.
- `comp-iam`: t-9 adds `GetObject` on one stamp pattern and one prefix-conditioned `ListBucket` to a firm-scoped role (a widening: the
  never-widen half names both statements and the rollback); t-11 adds NO grant (ruling 3411).
- `comp-adversary`: t-9's 403-vs-404 distinction is the whole difference between "stamp absent" and "grant missing"; the stub test pins
  both. t-11's guard cannot read a vendor or write a firm bucket; its only new act is a HEAD on a key the instance already reads.
- C-NAMES: t-9 adds a rule, target and permission; every name is `lib/opal_naming.py` output printed in the order. t-11 adds one rule
  name likewise. A builder REFUSAL is a registry row to add, never a typed name (CLAUDE.md rule 30).
- C-FIX-NOT-NOTIFY: no alarm, topic, send or monitor in any cell.

## The issuer's acts at the drain (not cells)

1. **Apply HG-t-9 (WORLD):** count the writers of `registry.json`/`holdings.json` first (N printed in the half); then plan, apply, read the
   deployed code against the build input, read the second rule back. The 13:15Z fire is read on the next day's artifacts.
2. **HG-t-5 apply (WORLD, own pair):** the fire time to `cron(45 12 * * ? *)`, only after act 1 and one 13:15Z fire read; every half
   that bounds the 06:00Z step is re-read (round-1 rule D1-S1).
3. **Apply HG-t-11 (WORLD, 49F leg):** the CloudOps msg-1814 conditions verbatim; the laptop told FIRST of a send that writes a firm
   data bucket; the document change under `safe-apply` with its own pair; the first guarded fire read.
4. **`HG-t-10` -- FWD-3's exercise (WORLD, own pair):** one induced same-day hole on FWD-1's pattern, repaired by
   `repair.py --date <today>`, which prints its MANIFEST before `--execute`; read on served bronze that exactly the named feed lands.
   Ruling 3410: the vendor call needs no per-use word. **Condition D1-S12:** the half names the restore actor on a DIFFERENT device
   than the seat that sets the induce, the ledger path it reads and the deadline. Condition D1-S11: any IAM verification splits C5a/C5b.
5. Every armed restore mechanism is named in the entry and read at its close (round-1 section 2.2).

## AMENDMENT 1 (issuer `2.0.0_SA_COO~G1`, 2026-10-11 ~13:3xZ) -- cell `HG-t-14`, the characteristics producer re-time

**Why, and who ruled it:** reading every same-day reader of the runner's bronze for the HG-t-5 apply found
`cot-satellites-characteristics-producer` (`cron(30 12 * * ? *)`, reads `holdings.json`). Once the runner fires at 12:45Z, `holdings.json`
is final only at the stamp-gated 13:15Z fire, so `characteristics.json` would sit one calendar day behind by construction, silently. CTO
`1.0.0_SA_CTO~DELL1` ruled (B), msg 3655, ADDENDUM 3 `c3cc34f2d0`: re-time it past 13:15Z first, as its own pair, before HG-t-5. The
issuer rules inside its own decomposition; the new cell is recorded here and not as a recut (the round's cells are otherwise unchanged).
The time input the ruling asks for was read from the first 13:15Z fire (REPORT Duration 3281.22 ms, END 13:15:48Z).

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-14` | The characteristics rule's `schedule_expression` `cron(30 12 * * ? *)` -> `cron(25 13 * * ? *)` (and its `description` and derivation comment). Nothing else. | FWD-5 (consequence of the runner move; CTO ADDENDUM 3) | dell1 code; applied at the drain under its own never-widen pair, BEFORE the HG-t-5 apply | WORLD | E, `0.9.0_WK_MDPF_HEALGAP~11` |

- **Write set:** `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`, the channel. Disjoint from t-9, t-11, t-12, t-13.
- **Workstream:** the order carries `<workstream>CHARRETIME</workstream>` beside `<round>3</round>`. The order gate refuses a second issuance
  into a round (Rule 27, row AMGT_RESAPP-Z-S154) and reads no override; the workstream key is its sanctioned lever for a scope with a disjoint
  write surface. Same issuer, one file, no shared write path with the first issuance. It is not a `pipeline-override`; none was used.
- **Check (issuer's, dry-run at the base):** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t14_schedule.py` -- BAD at the
  base (`TIME ... 12:30Z`), OK on a good copy (margin 600 s over a 270 s declared worst case), BAD on four mutants. No `terraform fmt` criterion:
  the file's fmt drift predates this cell (`FMT-BAD rc=3` at the base).
- **Edges:** none into the cell. The apply order is the CTO's: first 13:15Z fire read (done, ledger `healgap-r3-act1-...` CLOSED), then
  this cell's pair, then HG-t-5. `fanout: 5 of 5 chains, cap 8`.
- **Readers and writers (the pair prints N):** census `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/CHARACTERISTICS_JSON_CENSUS_20261011.md`
  @61d007d22c: 3 runtime readers, one producer; the by-grant writer count is read live at the pair.

## AMENDMENT 2 (issuer `2.0.0_SA_COO~G1`, 2026-10-12 ~13:4xZ) -- cell `HG-t-15`, retire the 07:00Z registry rule

**Why, and who ruled it:** HG-t-5 is applied and its first exercised day read (ledger `healgap-r3-act-ht5-runner-fire-1245z-20261011`
CLOSED `f3afa83d59`). With the runner's scheduled fire off 06:00Z, no roster partition for today exists at 07:00Z, so the 07:00Z registry
invocation raises `RegistryProducerError: BLOCKED` three times a day and writes nothing (read 2026-10-12: 07:00:15, 07:01:11, 07:03:16Z).
CTO ADDENDUM 5 `0c9f67d92d` (msg 3898) accepted that effect and ruled its retirement "its own pair, cut the day the first 12:45Z fire is
read and applied within one trading day". The issuer rules inside its own decomposition; the new cell is recorded here.

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-15` | Remove `cot_satellites_registry_producer_daily` (rule `cot-satellites-registry-producer-daily` `cron(0 7 * * ? *)`), its target and its permission from `satellites-registry-producer.tf`. Nothing added. | FWD-5 (consequence of the runner move; CTO ADDENDUM 5) | dell1 code; applied at the drain under its own never-widen pair | WORLD | F, `0.9.0_WK_MDPF_HEALGAP~12` |

- **Write set:** `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`, the channel. Disjoint from t-9, t-11, t-12, t-13, t-14
  (t-9 wrote the same file earlier and is complete; no open order holds it).
- **Workstream:** `<workstream>RULERETIRE</workstream>` beside `<round>3</round>`, the order gate's lever for a disjoint write surface under
  one issuer (the same reading as AMENDMENT 1's `CHARRETIME`); no `pipeline-override`.
- **Check (issuer's, dry-run at the base):** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t15_retire.py` -- BAD at the
  base (`GONE`), OK on a good copy, BAD on four mutants (rule-only removal, stamp-gated removed, stamp-gated cron altered, 07:00Z cron relocated).
  **Known and accepted:** HG-t-9's check `hg_r3_rules.py --t9` asserts the 07:00Z rule and will read T9-BAD on the new tree; HG-t-9 is complete.
- **Edges:** none into the cell. `fanout: 6 of 6 chains, cap 8`.
- **Rollback coupling (for the half):** rolling HG-t-5 back to 06:00Z requires restoring this rule in the same act.

## ROUND 4 -- the enrichment (issuer 2.0.0_SA_COO~G1, 2026-10-13 ~14:1xZ; PRD v0.3 @1c25ac7a85; CTO round-3 analysis @1f5f44b861 and its ADDENDUM 1, msg 4866)

Input: `ledger/ROUND_ANALYSIS.round3.md` section 3 (four items) and ADDENDUM 1. The CTO's item numbers map to cells: item 1 = `HG-t-16`,
item 3 = `HG-t-17`. **Item 2 (the HG-t-5 apply) is WITHDRAWN by ADDENDUM 1**: it was applied in round 3 (ledger
`healgap-r3-act-ht5-runner-fire-1245z-20261011` CLOSED `f3afa83d59`; live rule `cot-rebalancer-runner-daily` `cron(45 12 * * ? *)` ENABLED, read
2026-10-13T10:23:42Z; the 12:45Z fire read `SKIP-IDEMPOTENT` on 2026-10-12 and 2026-10-13), and FWD-5 grades REALIZED. **Item 4 is a carried
obligation, not a cell** (below): nothing is built for it.

### Measured at the base, 2026-10-13 ~14:0xZ

- **Characteristics producer (FWD-1's pattern for D1-S16):** `satellites-characteristics-producer.tf` has one rule
  `cot_satellites_characteristics_producer_daily` `cron(25 13 * * ? *)`, one target, one permission. The handler passes no event field to
  `producer.main`. The role (`cot_satellites_characteristics_producer_s3`) holds one `s3:ListBucket`, on `opal-data-etfs` conditioned to
  `bbg/*` and `bbg-testpull/tickers/*`, **no ListBucket on the cot bucket and, by design (CTO PRD ruling 13c), no GetObject on its own output**.
  2026-10-13 13:25:14Z, 13:26:29Z and 13:28:23Z: `NoSuchKey` on `bbg/2026-10-12/characteristics.parquet` (404 at 13:33Z; last partition present
  2026-10-09, landed 2026-10-12T11:03:03Z). The cause is upstream (site Z, weekly limit until 2026-10-14 06:00Z; the CTO's section 2).
- **Consequence found at the cut (the HG-t-9 lesson again):** the output's own freshness cannot be read by GetObject (no grant, ruled) and a HEAD
  under a prefix-conditioned ListBucket reads 403 for an absent key. The cell reads it by a LISTING of the exact key: the listing returns the key and
  its LastModified, never its bytes, and an absent key is an empty listing while a missing grant is a 403 that stays loud. "Complete day" is
  therefore defined as `characteristics.json` LastModified (UTC date) == today (UTC). The Bloomberg partition is also read by listing; the role's
  existing `bbg/*` ListBucket already covers it, so the only new grant is one `ListBucket` on the cot bucket for the exact output key.
- **FWD-6 census (HG-t-12, 164 scheduled pulls):** 7 EXPOSED-MANUAL rows. The census already carries, per row, the person's act and where it is listed
  (`deliverables/0.9.0_WK_MDPF_HEALGAP~9/FWD6_CENSUS_RESWEEP_R3.md` section 3, last two columns). For `bd-asset-dim-pipeline-trigger` the machine
  re-attempt exists since round 3 (HG-t-11: `blackdiamond-49f-asset-dim-reattempt-daily` `cron(40 22 ? * MON-FRI *)`, first guarded pair read
  2026-10-12 22:10Z and 22:40Z). The other six are person-renewed logins.

## Rule 24

Domain: the two live items, one adapter per cell. Same grain: `HG-t-16` is one producer (a second rule + the handler's skip decision + one listing
grant); `HG-t-17` is one document. State coherence: `HG-t-16` does not move the 13:25Z fire, does not change what that fire does on an absent
partition (it still raises, loud), and does not touch holdings or the registry; `HG-t-17` writes only its document and the channel.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-16` | A second rule on the characteristics producer, `cron(25 14-23 * * ? *)`, target input `{"require_partition": true}`, named by the `opal_name` builder (`etfs-cot-satellites-characteristics-producer-reattempt-hourly`). The handler, on that input only: lists `characteristics.json` and returns `SKIP-COMPLETE` when its LastModified (UTC) is today; else lists the T-1 `characteristics.parquet` and `run_manifest.json` and returns `PARTITION-ABSENT` if either is missing; else runs the producer as the scheduled fire does. AccessDenied on a listing raises. The role gains ONE `ListBucket` on the cot bucket, `StringEquals s3:prefix` the exact output key. The 13:25Z fire is unchanged. | D1-S16; FWD-1's pattern on the characteristics producer; FWD-6 (a new re-attempt in the census) | dell1 code; applied at the drain under its own never-widen pair | WORLD | A, `0.9.0_WK_MDPF_HEALGAP~13` |
| `HG-t-17` | READ-ONLY: each of the seven EXPOSED-MANUAL pulls gets one disposition row, `RE-ATTEMPT-BUILT` (only the asset-dim row), `RE-ATTEMPT-DESIGNED` (a machine re-attempt that no cell builds: the rule time and the guard are written) or `NAMED-REASON` (none needed, because the renewal is a person's act: that act and the list it is queued on are named), each citing code `path:line` that resolves | FWD-6 | dell1, document only | LOCAL | B, `0.9.0_WK_MDPF_HEALGAP~14` |

## Write sets (disjoint)

- **HG-t-16:** `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`,
  `infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py`, the channel.
- **HG-t-17:** `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md`, the channel.
- Checks (issuer's, dry-run at the base 2026-10-13 ~14:0xZ, each BAD as expected with a GREEN control; 17 mutants of the HG-t-16 reference change and 8 of
  the HG-t-17 document discriminated): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_CHECKS/` -- `hg_r4_rules.py --t16 | --t16-iam`,
  `hg_t16_gate.py`, `hg_t17_dispositions.py`. Reference patches that pass every `HG-t-16` check on a pristine HEAD:
  `R4_PATCHES/t16_characteristics_tf.patch`, `R4_PATCHES/t16_handler.patch`.

## Edges and fan-out

No data edge between the two cells. `fanout: 2 of 2 chains, cap 8`.

## Battery

- `comp-schedule`: `HG-t-16` adds ten fires a day at :25 past 14Z-23Z. The first is 60 minutes after the scheduled 13:25Z fire, whose own
  worst case (a 120 s timeout and two async retries) is about 8 minutes, so no re-attempt overlaps the fire it backs up. Each re-attempt that does
  nothing costs one or two S3 listings.
- `comp-iam`: `HG-t-16` adds one `s3:ListBucket` on `opal-data-cot`, exact-key `StringEquals`. A widening: the never-widen half names the statement,
  the rollback (revert the policy) and the writer count of `characteristics.json` (one function, now two triggers).
- `comp-adversary`: the empty-listing versus 403 distinction is the whole difference between "partition absent" and "grant missing"; the stub test
  pins both on both buckets, and a sibling key (a `.bak`, a `.tmp`) is never read as the key.
- C-NAMES: the one new rule name is `lib/opal_naming.py` output (`etfs-cot-satellites-characteristics-producer-reattempt-hourly`, kind `hourly`),
  built by the `opal_name` module; the handler derives its buckets and keys from the producer module's constants and types none.
- C-FIX-NOT-NOTIFY: no alarm, topic, send or monitor in either cell. The `SKIP-COMPLETE` and `PARTITION-ABSENT` lines are the whole record.

## The issuer's acts at the drain (not cells)

1. **Apply HG-t-16 (WORLD, own never-widen pair):** count the writers of `characteristics.json` first (N printed in the half); build and upload the
   package (`build_package.py --pin`, deployed bytes read against the build input); then plan (exactly the rule, target, permission and one IAM
   statement), apply, read the rule and the role back. The first organic read is the next day the T-1 partition arrives after 13:25Z; the driven
   arm is a QA invoke of `{"require_partition": true}` on a day the output is complete (`SKIP-COMPLETE`) and, once a partition is missing, the
   `PARTITION-ABSENT` line. A hand re-run to produce 2026-10-12's object is NOT an act of this round (CTO section 2).
2. Every armed mechanism is named in the entry and read at its close (round-1 section 2.2): the new rule is the only one this round arms.

## Carried obligations (not cells)

- **D1-W8-S1's remediation** closes on the first live failed guard read, read when it occurs, as the organic negative arm (CTO item 4). Owner:
  the issuer. Trigger: an asset-dim run whose `hg_guard.py` step reads rc 1 or 2 (the pull then runs). Read: that day's
  `s3://opal-data-bd/logs/asset-dim-download-<D>.log` and the instance's result. Until it occurs the row stays OPEN and the positive arms stand
  (round-3 act-3 L4: 22:10Z downloaded, 22:40Z `SKIP-COMPLETE`).
- **Item 2 withdrawn** (above); nothing carried.

## AMENDMENT 1 (round 4; issuer `2.0.0_SA_COO~G1`, 2026-10-13 ~14:4xZ) -- cell `HG-t-16`, the re-attempt's schedule and guard

**Why, and who ruled it:** worker `0.9.0_WK_MDPF_HEALGAP~13` applied the reference patches and stopped on its refusal clause with BLOCKING row
`MDPF_HEALGAP-D1-W13-S1`. The naming limb refused the code commit: `NAMING REFUSE infra/aws/terraform/cot-pipeline:0 <hole-count-ratchet> -> -`,
because the new rule's schedule `cron(25 14-23 * * ? *)` has no cadence word (`lib/opal_naming_cadence.word_for` returns `None`: "hour field 14-23:
more than once a day, not a list of single hours"), so the name ending in `hourly` would add one hole. `word_for("cron(55 * * * ? *)")` returns
`hourly`. The defect was the issuer's: the order's checks graded the rule's schedule against the intent and never ran the cadence reader.
The issuer rules inside its own decomposition (CLAUDE.md rule 27, no CTO ruling); this amendment is recorded here, not as a recut.

**What changes in the cell (and what does not):**

| | first cut | amended |
|---|---|---|
| schedule | `cron(25 14-23 * * ? *)`, ten fires 14:25Z-23:25Z | `cron(55 * * * ? *)`, 24 fires a day, at :55 |
| "after the registry's 13:15Z fire" | carried by the window | carried by the handler's FIRST test: `holdings.json` listed with LastModified (UTC) == today, else `HOLDINGS-NOT-FINAL` |
| "complete day" | `characteristics.json` LastModified (UTC date) == today | the output is listed and its LastModified >= `holdings.json`'s (a day is complete only when the output is no older than its input) |
| grant | one `ListBucket`, exact key `characteristics.json` | one `ListBucket`, `StringEquals` the two exact keys `characteristics.json` and `holdings.json` |
| name | `etfs-cot-satellites-characteristics-producer-reattempt-hourly` | unchanged |
| the 13:25Z fire | unchanged | unchanged |

**Reasons the guard moved from the clock to the fact:** a window assumed holdings final after 14:25Z by arithmetic; the handler now reads it. The
:55 minute keeps every re-attempt out of the scheduled :25 minute and out of the registry's :15 fire, so two producers never share a minute.
Cost: 24 invocations a day, each at most four listings; before 13:15Z each ends at the first test.

**Residual named:** a day on which the registry producer's stamp-gated 13:15Z fire did not write `holdings.json` (the runner left no stamp) draws
`HOLDINGS-NOT-FINAL` all day; the scheduled 13:25Z fire alone serves it, exactly as before this cell.

**Check and patches (issuer's, dry-run again at the base 2026-10-13 ~14:3xZ):** `R4_CHECKS/hg_r4_rules.py --t16` now also reads the naming
limb's cadence reader and is BAD at the base, OK on the reference change, and BAD on 6 rule mutants (the window cron among them) and 7 grant
mutants; `hg_t16_gate.py` has fifteen arms (A-N plus E2) and is BAD at the base, OK on the reference handler and BAD on 11 handler mutants.
24 of 24 mutants discriminated. Reference patches `R4_PATCHES/t16_*.patch` are regenerated and apply cleanly to a pristine HEAD.

**Gate limb that graded this amendment:** none of `to-pipeline-gate` limb 6 fires on a modified order (it grades newly added orders); GATE (viii)
reads `<placeholders>NONE</placeholders>` unchanged. The graded refusal was the naming limb at the worker's commit (the limb that found the defect).
**Worker:** the finished slot is re-seated, naming its prior commits (the surprise row and an INVALID proof instance) as inherited state; the
row stayed on the worker's branch (the row gate refuses a seat-authored W-coordinate row) and reached the channel with the worker's merge `8cc7e0458e`.

## ROUND 5 -- the enrichment (issuer 2.0.0_SA_COO~G1, 2026-10-13 ~17:2xZ; PRD v0.3 @1c25ac7a85; CTO round-4 analysis @c36a37275f, msgs 4962 and 4966)

Input: `ledger/ROUND_ANALYSIS.round4.md` section 3 (four items) and the CTO's ruling (A) on the schedule's name (msg 4966). The CTO's item numbers map to cells:
item 1 = `HG-t-18` (the code half), item 2 = `HG-t-19`, item 3 = `HG-t-20`; item 4 is a carried obligation, not a cell. FWD-6 grades PARTIAL on the
analysis: all seven pulls are dispositioned and the characteristics re-attempt is live, but D1-W14-S3 regrades ASTN to RE-ATTEMPT-DESIGNED, and a design
is not a build. FWD-6 grades REALIZED on item 1's re-attempt (the CTO's text).

### Measured at the base, 2026-10-13 ~17:2xZ

- **ASTN FT leg:** `tools/astn_wsjft/scripts/run.py` degrades to WSJ-only when the FT fetch raises (the warning `FT fetch failed ...`), never refills the day;
  `_fresh` keeps 12 h. The orchestrator Lambda (`infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py`) has modes `run` and `absence_check`;
  the schedule `astn-wsjft-3am-run` (`aws_scheduler_schedule.astn_run`, `cron(0 3 * * ? *)` America/New_York) is the only trigger; no 4 AM absence-check
  schedule exists in Terraform. The code reaches the scraper from `s3://opal-313476888478-lambda-artifacts/ec2/astn-wsjft/code/` by `deploy.sh`.
- **The naming obstacle, found at the cut and raised the same hour:** `lib/opal_naming.grade(<any astn name>, 'SCHEDULE')` raises `R1.c: 'astn' is an
  unresolved token` (the registry holds `astn` unresolved; ruling R10-2 keeps its existing names). A new hand-named astn schedule would add a hole and the
  naming limb refuses the commit (the HG-t-16 failure). CTO ruling (A), msg 4966: astn gets a registry row with owner AMGT_HARVST, routed through MSTR to
  the laptop CRO's lane; the schedule resource is cut when the row is on CLOUD and `grade()` returns the name clean. **The cell therefore builds only the code.**
- **SDD session:** the puller reads Credential Manager `SDDSecure` (`sdd-daily-pull.ps1:229`); the capture writes Secrets Manager `schwab/sdd/session`;
  no in-repo writer of `SDDSecure` was found (row D1-W14-S2; the CTO ruled the census row WRONG as written).
- **Transcripts header:** `infra/aws/terraform/transcripts/pull.tf:1-3` says DESIRED ONLY, never applied; both transcripts rules are live and ENABLED
  (read 2026-10-13). Its non-comment bytes are blob `ebabe8dad470cfb6a4ed0e865c13172bef05e12a`.

## Rule 24

Domain: the three live items, one adapter per cell. Same grain: `HG-t-18` is one behaviour (an FT-only refill) across the code that runs it and the
Lambda that starts it; `HG-t-19` is one document; `HG-t-20` is three comment lines. State coherence: `HG-t-18` does not change what the 3 AM run does
(the gate pins `run()` and the `run` command line byte-for-byte), adds no schedule, no grant and no SES identity; `HG-t-19` and `HG-t-20` change no
code and no resource.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `HG-t-18` | The code half of the ASTN FT same-day re-attempt: `run.ft_reattempt` (complete-day no-op, FT-only fetch, window since the last successful run, de-dup by article id across the window's digests, one `FT supplement` send, `-ftsup` digest as the done-marker), `store.try_load_digest`, the `--ft-reattempt` / `--dry-run` CLI switch, and the orchestrator Lambda's mode `ft_reattempt`. NO Terraform; the schedule resource waits on the registry row | FWD-6 (D1-W14-S3) | dell1 code; the S3 code upload and the Lambda deploy are the issuer's drain acts under their own never-widen pair | WORLD | A, `0.9.0_WK_MDPF_HEALGAP~15` |
| `HG-t-19` | READ-ONLY: what `SDDSecure` holds, who writes it, whether the capture's store is the same, and ONE decision: `NAMED-ACT` (person and trigger), `REPOINT` (a pair named) or `BOX-READ-OWED` (the exact read and the identity) | FWD-6 (D1-W14-S2) | dell1, document only | LOCAL | B, `0.9.0_WK_MDPF_HEALGAP~16` |
| `HG-t-20` | The `pull.tf` header's first three comment lines corrected: both live rules named, `live`, read 2026-10-13; no non-comment line changes | FWD-6 (D1-W14-S4) | dell1 code; the proof is a `terraform plan` reading no change, run by the issuer | WORLD | C, `0.9.0_WK_MDPF_HEALGAP~17` |

## Write sets (disjoint)

- **HG-t-18:** `tools/astn_wsjft/scripts/run.py`, `tools/astn_wsjft/scripts/store.py`, `infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py`, the channel.
- **HG-t-19:** `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~16/SDD_SESSION_RESTORE_DETERMINATION_R5.md`, the channel.
- **HG-t-20:** `infra/aws/terraform/transcripts/pull.tf`, the channel.
- Checks (issuer's, dry-run at the base 2026-10-13 ~17:2xZ, each BAD as expected with a GREEN control and mutants discriminated: 20 of 20 for HG-t-18, 6 of 6
  for HG-t-20, 9 of 9 for HG-t-19): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_CHECKS/` -- `hg_t18_run_gate.py`, `hg_t18_orch_gate.py`,
  `hg_t19_sdd.py`, `hg_t20_comment_only.py`. Reference patches that pass both HG-t-18 gates on a pristine HEAD: `R5_PATCHES/t18_tools.patch`,
  `R5_PATCHES/t18_orchestrator.patch`.

## Edges and fan-out

No data edge between the three cells. `fanout: 3 of 3 chains, cap 8`. The schedule resource (round-5 item 1's second half) depends on the registry row, an
act outside this project; it is cut as a later cell, or an amendment, when `grade()` returns its name clean.

## Battery

- `comp-schedule`: HG-t-18 adds no schedule in this round. The refill's own schedule is chosen when its resource is cut: it must fall after the 3 AM ET run's
  worst case (the orchestrator's 900 s Lambda and the box's 600 s SSM timeout), and be a fixed cadence the cadence reader decides (the HG-t-16 lesson).
- `comp-iam`: none changed. The scraper role already writes `digest/` and `email/`; the supplement writes `digest/<date>-ftsup/` and `email/<date>-ftsup/`,
  inside those prefixes. Read at the drain by `get-role-policy`, not assumed.
- `comp-adversary`: the two failures the gates pin are a re-send of an already-sent article and a refill that fires on a complete day; the residual is a day
  whose FT cookie is still dead at the re-attempt (the fetch raises: loud, nothing sent).
- C-NAMES: no new resource name in this round's code half (the schedule's name is the open registry row).
- C-FIX-NOT-NOTIFY: no alarm, topic, SES identity or monitor in any cell; the supplement uses the brief's own `send_ses.send` to its own recipients.

## The issuer's acts at the drain (not cells)

1. **Deploy HG-t-18 (WORLD, own never-widen pair):** count the writers of `digest/<date>-ftsup/`, `email/<date>-ftsup/` and the brief's recipients first (N
   printed in the half); read the scraper role and the orchestrator role; upload the `tools/astn_wsjft` tree to the box's code prefix and the Lambda
   (Terraform `archive_file` update, targeted at the function) with a plan reading ONE changed attribute (the function's source hash); read the deployed bytes
   against the build input. The first driven arm is `{"mode":"ft_reattempt","dry_run":true}`: fetch, analyse, compile, send and write nothing.
2. **HG-t-20:** a `terraform plan` in `infra/aws/terraform/transcripts` reads no change; the transcripts project's owner is copied on the commit.
3. **HG-t-19:** if the decision is `BOX-READ-OWED`, the read is a separate act with its own half and an executor on the box's identity; if `REPOINT`, a pair;
   if `NAMED-ACT`, the person and trigger go to the CTO's open-calls list.

## Carried obligations (not cells)

- **The schedule resource** for the refill: cut when the registry row is on CLOUD and `grade()` returns the name clean (CTO msg 4966). Owner: the issuer.
- **HG-t-16 ledger L6:** the `HOLDINGS-NOT-FINAL` read from 00:55Z 2026-10-14 (recorded, not waited on; CTO round-4 section 1).
- **D1-W8-S1's remediation:** the first live failed guard read of the asset-dim pull (recorded, not waited on).
