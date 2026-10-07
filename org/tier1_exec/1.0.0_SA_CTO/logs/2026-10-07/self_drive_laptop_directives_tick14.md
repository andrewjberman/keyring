# /self-drive laptop directives -- tick 14 (2026-10-07 20:4xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`.
**Cadence:** 60m, cron `77f028d5`. **paired_with:** solo. **state: ARMED**. Covers the event-driven acts since the tick 13 log (author
time by `git log`: 2026-10-07T15:35 -04:00) and the cron's fourteenth fire.

## Measurements (20:41Z)

- Trunk (fetch): origin CLOUD `f797fc2df1`; the shared laptop tree 1 ahead, 645 behind; site Z pushed.
- Sequence: no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 3 of 3 COO lanes (`~C`, `~G`, `~R`): the laptop is at its cap.
- Inbox: 0 unread files. Live on the laptop broker: 12.
- Laptop memory: 5.9 GB free of 31.7 GB (one read). At ~20:2xZ the harness killed a seat's background timers for low memory.
- `cot-rebalancer-runner-daily` target input, read by this seat: `{"mode":"pull","induce":"auth-lapse"}`. Still induced, as
  intended until 06:05Z.
- Stale summaries not read as state: `0.7.0_AE_CloudOps~S` (a question answered at 17:30Z and 18:22Z), `0.0.0_AB_MSTR` (e66,
  pushed 19:40Z), `2.0.0_SA_COO~G` and `3.0.0_SA_CVO` (items closed), `4.0.0_SA_CRO`.

## Calls ruled since tick 13 (the driver's own REC, each; event-driven)

| # | Call | Ruling | Carrier |
|---|---|---|---|
| 1 | Check 7 of the intake, with Defender off (106548) | the active managed antivirus, read on-access; no test-virus control | msg 19:51Z |
| 2 | The scope of `2.0.0_SA_COO~R` | the seat-roles workstream only; its first cut named; read by that seat (its summary) | msg 19:54Z |
| 3 | An untargeted apply of the opal-assets root before 06:20Z (106553) | a cross-box deploy notice to all four boxes, expiring by itself | msg 106554 |
| 4 | The seat for dell1's two vendor runs (106558) | `0.7.0_AE_CloudOps~SC`, as dell1's seating check asked; this seat's choice of `~I` was wrong | acked |
| 5 | LGIC_BLANKFIX round 3 (slug 106559) | FWD-1 at 138 of 140; the Cottonwood-named file ruled from two live reads; six cells | @f0e6411e53 |
| 6 | The restore after `~F` lost its timers (106563) | dell1's `2.0.0_SA_COO~G1` at 06:10Z is the first timed owner; this seat at 06:17Z with the payload in hand | msgs 20:34Z |
| 7 | Nine audit records present only in a snapshot (106561) | `0.0.0_AB_MSTR` restores and commits them | msg 20:36Z |

## Held by this seat for 06:17Z on 2026-10-08

- Read: `.tools/aws events list-targets-by-rule --rule cot-rebalancer-runner-daily --query 'Targets[0].Input' --output text`.
- If it still prints the induce: `.tools/aws events put-targets --rule cot-rebalancer-runner-daily --targets file://<payload>`,
  payload `[{"Id":"cot-rebalancer-runner-daily","Arn":"arn:aws:lambda:us-east-1:313476888478:function:cot-rebalancer-runner","Input":"{\"mode\":\"pull\"}"}]`
  (the order's own second put, from `0.7.0_AE_CloudOps~F` msg 106570; Id and Arn equal the live target's, read 20:38Z). Expect
  FailedEntryCount 0, then re-read. If it already prints `{"mode":"pull"}`: nothing.
- This is the one act this loop holds that touches AWS. It is the restore of a signed order's own state, under dell1's CTO half
  @b05cdf04c1 condition 2, as owner (3) of ruling 106485; it is not an apply of this seat's choosing.

## Acts only Andrew can do (unchanged from tick 13)

- The Python 3.12 installer, elevated, on each Dell when delivered. The naming exception for MDPF_HEALGAP HG-t-2. The
  walk-through of the two Dell reports. LGIC_BLANKFIX's DONE WHEN lines.

## Completion test

NOT DONE, read from the register: 18 parked; 3 UNREACHABLE (LGIC_CANON, LGIC_LGCTFM, LGIC_ENFORCE); D10 UNMEASURABLE.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `Get-CimInstance Win32_OperatingSystem` | the laptop's free memory | PASS | one read, not a trend |
| `.tools/aws events list-targets-by-rule` | the induced setting | PASS | still induced |
| `sequence-check.py` | capacity | PASS | 3 of 3 |

- **What worked:** asking the seat that lost its timers for the payload and the read as two lines, so the fallback does the
  order's own put and nothing else.
- **Gap found:** an overnight safeguard held in a session's memory on the box with the least of it.
