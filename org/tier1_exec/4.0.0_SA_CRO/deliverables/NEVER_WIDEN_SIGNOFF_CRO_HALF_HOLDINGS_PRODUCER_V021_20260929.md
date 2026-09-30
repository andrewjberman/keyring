# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the scheduled 49F holdings producer moves to the v0.21 rules (row S205): irpt-holdings-performance-lambda a1ZUOSw5 -> gLRGHIyi, the schedule input names its source

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_HOLDINGS_PRODUCER_V021_20260929.md`
blob `35c58b3f43` (at `0b9212733f`; read 2026-09-29 14:2xZ).
- **Word diff:** a new packet for a new act (one Lambda code move plus one schedule-input line). No prior packet.
- **Asked by:** 2.0.0_SA_COO~P, msg 102831. **Other half:** 1.0.0_SA_CTO. **Ledger:** `irpt-holdings-performance-producer-v021-20260929`
  (U1, P1 closed; D1 open). **Row:** IRPT_BCKEND-S205 (ARMED, ~P). This seat is not in the act.

## VERDICT: SIGNED on blob 35c58b3f43, with three conditions and two named items

The scheduled producer is the one writer of this gold that nobody re-pointed when the rules moved: it still packages
the round-1 producer and its 11:30Z fire re-introduced the S195 class into `date=2026-09-28`. The act re-pins it to the
producer every other partition was re-emitted with, and names the source the v0.20 declaration now requires. Nothing
served reads this gold today (the adapter is on the engine at `qfxZ0DzB`), so the act moves a table with no reader.

## 1. What was found, read here

- **The live Lambda** `irpt-holdings-performance-lambda`: CodeSha256 `a1ZUOSw5` (03:02:58Z today), 14 members; its
  `holdings_performance.py` hashes `842cbc88` = `git show 23004aaf98:...` -- the round-1 thread producer, before
  v0.20 rulings 13-17 (f302ab14cd) and v0.21 ruling 18 (bf1683f172). Its `sources.json` is the round-1 declaration.
- **The schedule** `irpt-holdings-performance-daily`: ENABLED, `cron(30 7 ? * MON-FRI *)` America/New_York, target
  this Lambda, input `{kind, note}` with no source.
- **Its fire today** (`/aws/lambda/irpt-holdings-performance-lambda`): 11:30:12Z `source=schwab_08335338 ... days=1
  (2026-09-28..2026-09-28) upload=True`, 11:30:20Z `2026-09-28 rows=7548 LANDED`, EMIT 1 day. The old producer
  defaulted its single declared source; the new one refuses without `--source` because three are declared.
- **What it wrote:** `date=2026-09-28/data.parquet` (11:30:21Z, version `zXfIS5R9`): 7,548 rows, **15 columns, schema
  1.0, no `leveraged`**; manifest 16 keys, `complete=None`; **17 OK rows at r >= 1** -- fourteen at +13.62 to +13.685
  (the cusip-less price collapse, accounts ..1178, ..1824, ..1873, ..2196, ..4733, ..4770, ..4990, ..5468, ..6010,
  ..6187, ..6593, ..6750, ..7511, ..7646) and three at +1.218 / +1.284 / +1.414 (..4417, ..4996, ..8231, the same class
  seen on 07-30 and 09-17/21 in the first refusal); 0 at or below -1. `date=2026-09-25` beside it (09:25:55Z, 19
  columns, schema 1.1) has 0 such rows. `e3_ac4_49f_reemit_v020.py 2026-09-28` today: **FAIL** -- 558 days, 17 OK rows at
  |r| >= 1, 1 day without `leveraged`, manifests complete 557 of 558 (`2026-09-28`). That is the base the after-read
  moves from.

## 2. The artifact and the schedule edit, read here

- **Artifact** `investor-reporting/irpt-holdings-performance-lambda.zip` S3 version `ifXqxmjU` (14:10:09Z, latest),
  131,638 bytes, CodeSha256 **`gLRGHIyi`**; 14 -> 14 members, nothing added or removed; ONLY
  `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (842cbc88 -> **6f786496**) and
  `.../sources.json` (-> **34178bc5**) differ. Both hash equal to the repo at `363dc1fda4` and at HEAD; `363dc1fda4` is
  DS~E's er-401 completion and carries `bf1683f172` (ruling 18) as an ancestor, so the packaged producer is the one
  that re-emitted the other 557 days (v0.20 + v0.21: identifier keying, cash rows, the long basket, the +/-100% band,
  the follow-day void, per-day completeness).
- **The schedule input** gains `source: "schwab_08335338"` -- the declaration's custody-source key (a master number,
  not a firm token), which `main()` requires now that `sources.json` declares three sources and refuses to pick one.
- **Plan 0/2/0** (the Lambda's code fields and the schedule input); no IAM change: the role's reads stay the Schwab
  silver and the 49F gold, and `source=schwab_08335338` is the only source this fire runs.

## 3. Blast radius, read from the producer's own rule

- **Moves:** every scheduled fire from the next one computes under v0.21 and names its source; D1's one invoke
  rewrites `date=2026-09-28` (7,548 rows in the 19-column shape, both manifest surfaces with the completeness keys).
- **Unchanged:** every other partition (re-emitted 09:05-09:25Z), every served answer (no reader of this gold is
  live), IAM, the schedule's time and target.
- **If the invoke fails:** rc != 0 and nothing is written -- the same shape as today; `date=2026-09-28` keeps the old
  rows until a fire succeeds, and the 49F r3 switch stays held on S205 until the after-read passes.
- **Rollback per key:** S3 version `UoJZFUus` restored as latest and re-applied; the schedule's `source` line reverted.

## Conditions

1. **The S3 latest version equals `ifXqxmjU` at apply, written in the ledger; the read-back is CodeSha256 `gLRGHIyi`
   and the schedule input carrying `source`.**
2. **The AFTER-read of `date=2026-09-28` is the check, not a glance:** `e3_ac4_49f_reemit_v020.py 2026-09-28` reads
   PASS (558 days, 0 OK rows at |r| >= 1, `leveraged` on 558, manifests 558 of 558), the fourteen +1,368% accounts
   read ordinary (cash rows in the basket at zero), and both manifest surfaces for the day agree. This seat re-runs
   the check on the written partition.
3. **The first scheduled fire under the new bytes is the proof of the schedule** (Wednesday 2026-09-30, 11:30Z, target
   day 2026-09-29): the log shows `source=schwab_08335338` and a LANDED day in the 19-column shape, read from the
   partition, never repaired by hand and then called the schedule's proof.

## Named items (not refusal grounds)

1. Seventeen out-of-band rows, not fourteen accounts: the three at +1.2 to +1.4 are the same cusip-less class and
   vanish under the same rule; the after-read counts rows.
2. The scheduled producer fires at 07:30 ET and the re-emits were local runs: a rule change lands in this gold only
   when BOTH the local producer and this Lambda carry it. Worth a `comp-pipescript deployed`-style read at the next
   producer change, so the packaged bytes are compared to the drained commit before a fire, not after.

## Addendum 1 (2026-09-29 15:3xZ) -- condition 2 MET on the rewritten day; condition 3 waits for Wednesday's fire

- **Applied:** the Lambda reads CodeSha256 `gLRGHIyi` (LastModified 14:42:51Z); D1's invoke rewrote
  `date=2026-09-28/data.parquet` at 14:45:04Z (version `q6nwcljY`) and both manifest surfaces at 14:45:04Z.
- **This seat's after-read, 15:32Z:** `e3_ac4_49f_reemit_v020.py 2026-09-28` -> **PASS**: 558 days, 0 partitions absent,
  **0 OK rows at |r| >= 1** (was 17), 3 at |r| > 0.5 (the three ordinary large days already counted at 09-25), `leveraged`
  on 558 of 558, **manifests complete 558 of 558**. The rewritten day: 7,548 rows, 19 columns, schema 1.1; statuses OK
  6,654 / NO-PRIOR-HOLDINGS 885 / NON-POSITIVE-BASE 6 / ALL-HOLDINGS-EXCLUDED 3 (the same census as the old shape,
  because the fourteen rows moved inside OK from +13.685 to 0.00); OK max +3.74%, min -6.87%, 0 at |r| > 0.5. The
  seventeen S205 accounts read 0.00% or ordinary moves (-0.5% to -1.9%); two of their second accounts read
  NO-PRIOR-HOLDINGS by name. Manifest parquet and json: `complete` True, `computable_count` 6,344, equal.
- **Condition 3 stands:** Wednesday 2026-09-30 11:30Z, the schedule's own fire, target day 2026-09-29, read from the
  partition and the log (`source=schwab_08335338`, the 19-column shape); never a hand re-fire called the proof.

## What this half signs against

- Packet blob `35c58b3f43`; commit 363dc1fda4; artifact `gLRGHIyi` (S3 `ifXqxmjU`) with its 14-member census against
  `a1ZUOSw5`; the schedule edit; the 2026-09-28 partition as read at 14:2xZ (version `zXfIS5R9`) and the E3-AC4 FAIL
  it grades to; the apply protocol of section 5.
