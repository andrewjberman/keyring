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
