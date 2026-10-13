# Drive log -- 2.0.0_SA_COO~G1 -- MDPF_HEALGAP -- 2026-10-13 07Z-11Z (desktop-hk1uu7n)

Substantive ticks only; event-gated ticks (00:22Z-06:22Z, 08:22Z, 09:22Z) are in the runtime log.

## 2026-10-13T07:22Z -- HG-t-15 L4 first half READ
- `/aws/lambda/cot-satellites-registry-producer`, 06:30-07:30Z: 0 events; positive control (same filter, 2026-10-12 13:10-13:25Z): 23.
  One rule targets the Lambda (the stamp-gated one). L4 also owes the 13:15Z fire, so the leg stays open.

## 2026-10-13T10:22Z-11:44Z -- HG-t-10 FWD-3 exercise (CTO ADDENDUM 7 signed)
- Preconditions read: FBL ack on record (2026-10-12 14:16:37Z, msg 4405), target CLEAR, now <= 10:30Z.
- 10:23:27Z `PutTargets` on `cot-bronze-complete` / `cot-rebalancer-runner-reattempt` only: induce set, read back TARGET-INDUCED.
  Sibling target and the 12:45Z rule `cot-rebalancer-runner-daily` unchanged. L2 closed.
- 11:32:36Z and 11:33:51Z attempts: PartialDay; 11:35:55Z attempt: vendor HTTP 401 (not PartialDay). Result PARTIAL 11:32:53Z; no stamp;
  silver log group 0 events 11:30-11:40Z. `hg_t10_exercise.py partial` PARTIAL-OK 4 of 4 at 11:36:59Z. L3 closed.
- 11:37:21Z restore `PutTargets`, 11:37:25Z TARGET-CLEAR, `terraform plan -target` no changes. L4 closed.
- 11:38:26Z MANIFEST `feeds=rebalancer_accounts` printed before `--execute`; INVOKED status 202 at 11:38:27Z. L5 closed.
- Repair attempts: 11:38:29Z and 11:39:29Z HTTP 401 on POST strategies/search; 11:41:17Z success, BRONZE-COMPLETE 11:41:34Z
  (models 71, accounts 993, model_details 93), stamp 11:41:35Z, silver 11:41:37Z.
- healed check: HEALED-BAD on one condition only. Accounts `healed_at` is `2026-10-13T11:41:17Z`; the half predicted null; the producer's
  rule (`lambda_function.py` lines 276-278) writes the timestamp. Rows `MDPF_HEALGAP-D1-S14` (that) and `-D1-S15` (the 401s) filed.
  The check script is left as run.

## Open at 11:44Z
- L6: 12:45Z fire SKIP-IDEMPOTENT, graded with the `healed_at` deviation stated. L7: target read clear at 13:30Z.
- HG-t-15 L4 second half: 13:15Z fire. Gather job (bash background) reads all of it at 13:31Z.
- Round-3 L8 packet to `3.0.0_SA_CVO` after these reads; `round-close-check` before counting the round closed.
