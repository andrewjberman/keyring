# Never-widen half, MDPF_HEALGAP round 1 -- the Rebalancer runner re-runs after the Cottonwood login chain succeeds (cell HG-t-2)

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-07 ~14:1xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half (laptop CTO rulings
@31e91d2d1e section 2: dell1 signs both halves; the laptop applies). **Status: COO half SIGNED; CTO half owed.** No apply happens
before both halves are signed AND `HG-t-2` is drained to CLOUD AND the R20 entry for `cot-bronze-complete` is on CLOUD.

**Andrew's word:** `ANDREW_DIRECT_20261007_135xZ_HEALGAP_ACT1_YES_R20_YES_ACT2_NO_WORKTREE_DELETE_YES.md` @e5fb41862f, VERBATIM:
"1.) Yes, rec approved. 2.) Yes this is fine. Calls 3 and 4 both approved." -- ACT 1 (standing vendor word for this runner's
same-day re-run) and the R20 naming exception.

## The act

Apply `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf` (cell `HG-t-2`, built and checked by
`0.9.0_WK_MDPF_HEALGAP~2`: TF-OK, SEAM-OK) with `-target` on its two resources: an `aws_cloudwatch_event_target` on the EXISTING
rule `cot-bronze-complete` invoking `cot-rebalancer-runner` with `{"mode":"pull"}`, and an `aws_lambda_permission` for
`events.amazonaws.com` scoped to that rule. No new rule, schedule, function, role grant or output path (C-ONE-PIPELINE).

## What changes, read from the producers' own rules

**The trigger.** `cot-bronze-complete` fires on `s3://opal-data-cot/bronze/<date>/_BRONZE_COMPLETE.json` Object Created. Measured
2026-10-01..10-06: once a day, 11:31-11:32Z, on the same UTC date as the 06:00Z pull, after either leg of the session chain. Its
existing target (`CotSilverOnBronzeComplete`, the cot silver run) is untouched.

**The runner** (live code = the HG-t-1 build, CodeSha256 `QxLvPLTM...OMvk=`, verified 10:4xZ): invoked with `{"mode":"pull"}`,
date = today UTC.

**Writers counted.** Bronze `blackdiamond/cottonwood/bronze/rebalancer_{models,accounts,model_detail}/<date>/` and the stamp
`meta/<date>-complete.json`: N = 1 rule (`ingest`), now reachable from 2 triggers (06:00Z and ~11:32Z). Silver for the date: N = 1
rule, the `opal-assets-silver-blackdiamond` converter via `on_success`, converting `responsePayload.as_of` on BOTH verdicts
(`mirror_conversion.py` `date_from_destination`).

**Both branches, per day:**
- (A) The 06:00Z pull completed (every day measured 10-01..10-07). At ~11:32Z the re-run lists the stamp and returns
  `SKIP-IDEMPOTENT`: no secret read, no Black Diamond call, no bronze write. `on_success` fires and silver re-converts the SAME date
  from the SAME bronze: the served values are unchanged; one extra conversion run a day.
- (B) The 06:00Z pull failed (lapsed login, or any raise). No stamp exists. At ~11:32Z the re-run pulls the three feeds for that UTC
  date (ONE Black Diamond pull, under ACT 1), lands them, writes the stamp, and `on_success` drives silver then gold. The served
  Cottonwood day appears the same day instead of staying empty. A partial morning landing (some pages written, then a raise) is
  overwritten key-for-key; a key the morning wrote that the re-run does not enumerate would trip the set-identity guard (raise, no
  stamp, no silver) -- the same fail-closed outcome as today, not a wider one.
- (C) The session chain fails all day (no sentinel): nothing fires; identical to today.

## Blast radius

Keys the act may cause to be written: on branch (B) days only, that UTC date's bronze keys under
`opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_*/` and `meta/<date>-complete.json`, `meta/pulls/<date>/`, and the silver
and gold partitions the existing `on_success` chain writes for that date. On branch (A) days: no bronze key; one silver re-conversion
of the same date. No other firm, bucket or prefix (the runner's write policy is `blackdiamond/cottonwood/` only, with an explicit
49f Deny).

## Rollback

Remove the two resources: `terraform destroy -target` on them in `opal-assets` (or revert the file and apply), then read
`list-targets-by-rule cot-bronze-complete` = `[CotSilverOnBronzeComplete]` only and the runner's policy without the
`rule/cot-bronze-complete` statement. Data: a branch (B) day's bronze is the vendor's real data for that date, landed by the same
rule that lands it at 06:00Z; nothing to undo.

## Acceptance (the order's criteria, read from the live plane)

1. HG1-d2-AC1 `hg_d2_applied.py --wired` -> `WIRED-OK` (FAILS at the base today: 0 runner targets).
2. HG1-d2-AC2 `hg_d2_applied.py --unchanged` -> `UNCHANGED-OK` (PASSES at the base today: a control).
3. The next ~11:32Z fire on a normal day shows `SKIP-IDEMPOTENT` in the runner's log and no new bronze key (branch A, read by
   the issuer).

## COO half -- SIGNED

`2.0.0_SA_COO~G1`, 2026-10-07, after reading the worker's file and checks in `/c/tmp/wk-healgap-2`, the live rule pattern and
targets, the live runner sha and resource policy, the stamp census, and the converter's `date_from_destination`.
- **Blast radius, writers counted, rollback:** as above.
- **Not signed here:** the FWD-1 exercise (setting the 06:00Z target's input to `{"mode":"pull","induce":"auth-lapse"}` for one
  morning), which is a separate act with its own half; FWD-3 (no refill, per Andrew's ACT 2 answer).
