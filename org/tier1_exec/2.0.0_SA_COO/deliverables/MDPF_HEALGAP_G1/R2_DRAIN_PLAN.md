# MDPF_HEALGAP round 2 -- the issuer's drain plan and rulings (2.0.0_SA_COO~G1, dell1, 2026-10-08 ~15:1xZ)

Orders drained: HG-t-4 + HG-t-5 @672800c42a, HG-t-6 @7ede39f044, HG-t-3 @c468b71b6d. HG-t-7 (FWD-6 census, LOCAL) running.
Every drain act below is WORLD and runs from dell1 under its own never-widen pair (CTO + COO) and a change-management entry.
Arming rule (CTO round-1 analysis 2.2): every timer, background task or OS task armed for an act is named here with its id
and its state is read at the act's close.

## Rulings (issuer, inside the round-2 decomposition)

**R2-1 -- row `MDPF_HEALGAP-D1-W3-S1` (the runner role holds no `s3:GetObject` on `meta/`, so `healed_at` never records live).**
FWD-2's ACCEPT is "which kind of data is missing for which day, readable without looking anywhere else" -- served by the per-feed
`status` and the `PARTIAL` verdict, which come from LISTING and work on the live role. `healed_at` is the CTO's enrichment wording,
not the outcome's test. Ruling: HG-t-3 stands complete; deploy it as built (the read fails soft, `healed_at` reads null). The fix is
one narrow grant -- `s3:GetObject` on `arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-result.json` for role
`cot-rebalancer-runner` -- which is an IAM write: the laptop's by write-in today, or dell1's once Andrew's widened grant (items 4/5,
msg 938) is applied. Carried to the round-2 drain-end read as an enrichment item; it is not a deploy blocker.

**R2-2 -- a forced repair re-lands all three feeds, not only the missing one (worker ~5 report).** FWD-3's ACCEPT: "afterwards
exactly those are present and nothing else changed ... a repair that fills days it did not name, or puts today's data under a past
date, fails." The repair is refused for any date but today, and on today the vendor serves today's state, so re-landing the two
present feeds rewrites them with the SAME day's data -- no other date is touched and nothing lands under a past date. The manifest
already names every key prefix it will write (`keys=`), so the act says beforehand exactly what it writes. Ruling: accepted as built;
the drain exercise READS the two present feeds' key sets before and after and reports any difference beyond LastModified.

**R2-3 -- the exercise rides the FIRST pull of the day.** HG-t-5 moved the daily pull to 12:45Z, so on a normal morning the 11:3xZ
re-attempt (target `cot-rebalancer-runner-reattempt` on `cot-bronze-complete`) lands the day and the 12:45Z pull skips it (guard). An
induced hole therefore goes on the RE-ATTEMPT target's input, not the daily one.

## Drain acts, in order

1. **Deploy the runner code (HG-t-3 + HG-t-6's tools are not deployed; only `lambda_function.py` ships)** -- build the zip from HEAD,
   `safe-apply` of `opal-assets` targeted to the runner module, then read the deployed CodeSha256 against the build input. Grant
   check first: dell1's deploy policy must allow `lambda:UpdateFunctionCode` on `cot-rebalancer-runner` (not in a Deny list).
2. **Apply HG-t-4 + HG-t-5 (one targeted plan/apply):** `aws_lambda_function_event_invoke_config.cot_rebalancer_runner` (age 900) and
   `aws_cloudwatch_event_rule.cot_rebalancer_runner_daily` (12:45Z). Plan must read exactly those two in-place changes. Read back
   `get-function-event-invoke-config` and `describe-rule`.
3. **The one real run of FWD-2 and FWD-3 (an induced same-day hole), ACT 1's standing word for the same-day re-run:**
   a. the evening before, set the re-attempt target's input to `{"mode":"pull","induce":"drop-feed:rebalancer_model_detail"}`
      (read back); name the restore mechanisms (session cron + an OS task) with ids;
   b. ~11:3xZ the re-attempt lands models + accounts and writes `meta/<D>-result.json` PARTIAL (model_detail missing), no stamp,
      and raises (2 async retries, same induce) -- READ the result object: that is FWD-2's exercise;
   c. restore the re-attempt input to `{"mode":"pull"}` (read back);
   d. `repair.py --date <D>` dry-run prints `MANIFEST date=<D> feeds=rebalancer_model_detail ...`; then `--execute` -- the runner
      lands the day, writes the stamp; READ `meta/<D>-result.json` COMPLETE and the two present feeds' key sets (R2-2): that is
      FWD-3's exercise;
   e. the 12:45Z daily pull SKIPs (guard); the 13:30Z floor and the 13:50Z reader read normal.
4. **The eleven marks (no vendor call):** `mark_missing.py --from 2026-08-31 --to 2026-09-10 --feed rebalancer_model_detail
   --reason "<S2 / hop-0 reason>" --execute`, then list the eleven `meta/<d>-missing.json`.
5. **FWD-4 / FWD-5 read:** the settings and schedule in place (act 2's read-backs) are the APPLIED proof; FWD-5's winter margin is
   re-read on the first EST morning (2026-11-02).
