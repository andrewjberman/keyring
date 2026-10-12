# Never-widen half (COO half SIGNED, CTO half owed): MDPF_HEALGAP round 3, drain act HG-t-10 -- the FWD-3 exercise, an induced same-day hole repaired by one named act

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-12 ~14:3xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half and names the restore actor.
**Orders it applies:** round-2 analysis item 4 (`ROUND_ANALYSIS.round2.md`): "FWD-3 exercise: one induced same-day hole on FWD-1's pattern, repaired by
`repair.py --date <today>`. It prints its MANIFEST before `--execute`. Read on served bronze: exactly the named feed lands and nothing else changes."
Standing conditions 2.3 (D1-S12: a restore actor on a DIFFERENT device, its ledger path, its deadline), round-1 section 2.2 (every armed
mechanism named and read at its close) and 2.4. Vendor calls need no per-use word (CLAUDE.md Agent Autonomy; Black Diamond is not Bloomberg).
**Status:** DRAFT; nothing is set. The act is the issuer's and no worker order is cut: the induce, `repair.py` and the checks all exist.

## 0. Why this half is NOT the round-2 act 3 design

The round-2 act set the induce on the 06:00Z daily target. After HG-t-5 that target no longer fires at 06:00Z, and the day's FIRST pull is the
`cot-bronze-complete` sentinel invocation (~11:32Z; read live 2026-10-12: sentinel 11:32:07Z, runner START 11:32:07Z). An induce on the 12:45Z
target would find the stamp and skip. The hole must be induced on the SENTINEL target. Round-2 act 3 also never ran its named repair: the 10-10
hole was healed by the automatic re-attempt at 11:34Z. This design keeps that automatic heal as the safety, not as the outcome.

## 1. The act, in order (UTC; first possible day 2026-10-13)

| # | when | act | read |
|---|---|---|---|
| 0 | before step 1 | the restore actor accepts (section 3); the ledger entry is opened with its legs; `0.0.0_AB_MSTR~DELL1` told (no `terraform apply` on `opal-assets` in the window) | actor's ack, ledger path |
| 1 | <= 10:30Z | `events:PutTargets` on rule `cot-bronze-complete`, target `cot-rebalancer-runner-reattempt`: input `{"mode":"pull"}` -> `{"mode":"pull","induce":"drop-feed:rebalancer_accounts"}`. The 12:45Z target is NOT touched. | `list-targets-by-rule` back |
| 2 | ~11:32-11:36Z | the sentinel invocation and its 2 async retries pull and land `rebalancer_models` and `rebalancer_model_detail`, skip `rebalancer_accounts`, write `meta/<D>-result.json` `PARTIAL`, no stamp, raise `PartialDay`; silver does not fire | result object; absence of the stamp; absence of a silver REPORT |
| 3 | ~11:37Z | restore the sentinel target input to `{"mode":"pull"}` (`PutTargets`) | `list-targets-by-rule` back; `terraform plan -target` on the target reads no change |
| 4 | ~11:38Z | `repair.py --date <D>` dry run prints `MANIFEST date=<D> feeds=rebalancer_accounts keys=...` BEFORE anything; read the key sets (names, sizes, VersionIds) of the two present feeds; then `repair.py --date <D> --execute` (one async forced invoke) | the MANIFEST line; result `COMPLETE`; stamp; silver REPORT; the two present feeds' key sets after vs before |
| 5 | 12:45Z | the scheduled fire lists the stamp and returns `SKIP-IDEMPOTENT` | runner log |
| 6 | 13:15Z, 13:25Z | unchanged: registry `as_of <D>`, `holdings_as_of` == `as_of` | as the first exercised day |

**FWD-3's exercise** is steps 2-4: the hole opens at ~11:32Z and one act closes it before 11:45Z, saying beforehand exactly which feed it will fetch.

## 2. Both branches, from each producer's own rule

- **(A) The repair lands (~11:40Z).** The day's silver builds from repaired bronze ~1h50m before the 13:30Z floor. Served delta 0: the same day's
  state is served at the same served times. Vendor pulls that day: 3 induced attempts (two feeds each) + 1 forced repair (all three feeds) = 4,
  against 1 on a normal day; the session is valid at 11:32Z.
- **(B) The repair fails (vendor error or the seat is absent).** The day stays PARTIAL, silver is withheld, and the 12:45Z scheduled fire (not
  induced) finds no stamp and pulls all three feeds clean: FWD-1's own path. If that also fails, the 13:30Z floor serves the prior day, exactly as
  on any failed day before this project. The induce on the sentinel target outlives step 3 only in (C).
- **(C) The step-3 restore fails.** Tomorrow's sentinel invocation would induce again. The act reads the input back at step 3 and, if the restore
  did not take, re-applies `terraform apply -target` to that target the same hour; the ledger leg stays open until the read-back reads
  `{"mode":"pull"}`. If this seat is down, section 3's actor owns it.

## 3. D1-S12: the restore actor, off this box, with a path and a deadline

- **Setting seat:** `2.0.0_SA_COO~G1` on dell1.
- **Restore actor (the CTO names it; proposed):** `1.0.0_SA_CTO` on the LAPTOP, reached by `0.0.0_AB_MSTR~DELL1` relaying to `0.0.0_AB_MSTR`
  (a cross-fabric call goes MSTR to MSTR). It is on a different device from the setting seat and from `0.0.0_AB_MSTR~DELL1`, which is
  also on dell1 (round-2 act 3's second actor shared the failing box; this one does not).
- **Ledger path it reads:** `org/critical_paths/.open_deploys/healgap-r3-act-ht10-fwd3-exercise-<D>.json` on `origin` after the next `box-sync`,
  and the live read `events list-targets-by-rule --rule cot-bronze-complete` (target `cot-rebalancer-runner-reattempt`, input).
- **Deadline:** read the target at 12:30Z `<D>`; restore by 13:30Z `<D>` if its input still carries `induce`. Hard backstop: before the next
  sentinel, 10:30Z on `<D>+1`. The restore command is one `PutTargets` of the original input (the original input is printed in the ledger).
- **Armed mechanisms named (round-1 2.2):** the induce itself (step 1, read at step 3); no timer, background task or OS task is armed by this
  act. A wait-for-the-artifact poll may be run from this session at steps 2-4 and dies with the session.

## 4. Writers counted

| property | writers | notes |
|---|---|---|
| the sentinel target's input | 2 | Terraform (`cot_rebalancer_reattempt.tf`, `aws_cloudwatch_event_target.cot_rebalancer_reattempt`), and this act's `PutTargets`. Terraform is not applied on `opal-assets` in the window; the plan reads drift while the induce is set. |
| the day's bronze, result, stamp | 1 | the runner |
| silver for the day | 1 trigger | `on_success` of a successful runner invoke; withheld while PARTIAL |

## 5. What the exercise must show (acceptance)

1. Step 2: `meta/<D>-result.json` `PARTIAL`, `rebalancer_accounts` `missing`, models and detail `arrived`; no `meta/<D>-complete.json`; no silver REPORT.
2. Step 3: the sentinel target input reads `{"mode":"pull"}`.
3. Step 4: the MANIFEST names exactly `rebalancer_accounts` before `--execute`; after it the result reads `COMPLETE`, the stamp exists, accounts
   keys are present, and the key sets of models and model_detail equal their step-4 pre-read except LastModified/VersionId (any other difference is
   reported, not hidden); `healed_at` on accounts reads null live (the R2-1 rule).
4. Step 5: the 12:45Z fire is `SKIP-IDEMPOTENT`.

## 6. Rollback

Input: `{"mode":"pull"}` via `PutTargets`, or `terraform apply -target=aws_cloudwatch_event_target.cot_rebalancer_reattempt`. Result object: inert.
Bronze: same-day state, no rollback needed.
