# Never-widen sign-off -- gate G-B, NFRA_OPLGTW `OG-c-2` (producer deploy + controlled replay)

**Gate:** G-B (decomposition `org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md` @8768f46770, s.6).
**Governs:** `NFRA_OPLGTW.TO-OG-c-2.producer-deploy-replay` -- BOTH world acts, the deploy and the replay (order, BOUNDS "G-B").
**Halves:** `2.0.0_SA_COO~O` -- SIGNED below. `1.0.0_SA_CTO` -- **OWED.** One half present = no deploy and no replay (the order's
own stop). Law: CLAUDE.md HARD STOPS, "never move served output without never-widen sign-off" -- a half names the act's
BLAST RADIUS and the rollback for each key, reads any expected outcome from the producer's own rule, covers both branches,
and PRINTS the number of writers of the named property.

Every value below carries its instrument and vintage. "Read" = read at the cited `file:line @commit`; "measured" = a live
read at the stated UTC time.

---

## Half 1 -- `2.0.0_SA_COO~O` -- SIGNED 2026-09-15 ~12:0xZ, at CLOUD 5c51e9ff3b

### 1. The acts

| act | what it does | through |
|---|---|---|
| A1 deploy | vendors `OG-c-1`'s merged `conversion_manifest.py` / `schwab_runtime.py` into `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`, moves `silver_build_commit.schwab` (`silver.tf:78-80`), applies ONE function family | `.tools/safe-apply.sh`, ledger `nfra-oplgtw-og-c-2-producer` opened and committed first |
| A2 replay | writes ONE completion record per master (`08242234`, `08335338`) for ONE stated business date `D_r` | same ledger entry, second leg |

### 2. The named property and its writers -- N = 1

Property: the objects `s3://opal-data-assets/schwab/{master}/meta/complete/date=YYYY-MM-DD.json`.

- **Declared writers (census):** `comp-find -i 'meta/complete' --all` at 5c51e9ff3b: 448 hits across 172,311 files
  (corpus `all`; 104,760 ephemeral-floor, 17 unreadable, 4,532 binary not searched). 7 code files name the prefix: the writer
  `data/assets/scripts/silver/conversion_manifest.py` and its vendored copy
  `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py`; the declaration `silver.tf` (the
  notification) and `advi_49f_floor.tf` (comments); one test; two probes (read only). **Writers: 1 code path, in 2 copies,
  run by 1 live executor, the `opal-assets-silver-schwab` Lambda.** `OG-c-1`'s J1 record confirms every S3 write verb its
  diff touches is a marker PUT at `complete_marker_key(...)` (its result file, s.6).
- **Live corroboration (measured 12:0xZ, `s3api list-objects-v2`):** 10 marker objects per master, dates 2026-08-31 ..
  2026-09-14. LastModified clusters at 09:46Z / 21:46Z (`08335338`) and 10:16Z / 22:16Z (`08242234`), which are the
  bronze-arrival conversions. None carries the schwab sweep's slot (`silver.tf:244`, `cron(15 12 * * ? *)`). So one rule
  is read: the producer's.

### 3. Every `ObjectCreated` consumer -- 1

- **Measured by `OG-p-1`** (`deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.md`, OGP1-AC9, 2026-09-15T10:53:02Z): 11
  notification configurations on `opal-data-assets`, EventBridge disabled. **1** covers `schwab/*/meta/complete/`:
  `advi-49f-silver-complete-accelerator` -> `advi-49f-gold-dispatch`, prefix `schwab/08335338/meta/complete/`, suffix
  `.json` (`silver.tf:755-761`). **`08242234` has no consumer.** The Lambda's resource policy grants S3 invoke from
  `opal-data-assets` in this account (`get-policy`, measured 12:0xZ).
- **What the consumer does (read, `infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py` @e9b070d842):**
  - It reads the object KEY only (`:104-128`), never the body, and ignores the date in the key.
  - It starts the `bd-gold-layer-runner` host if the host is stopped (`:147-154`).
  - It sends `advi-49f-chain-dispatch` with an EMPTY `Date` (`:160-166`). The document then runs
    `chain_49f_entrypoint.py --production` (`advi_49f_floor.tf:282-283`).
  - The chain derives `D = prev_trading_day(now)` (`chain_49f_entrypoint.py:534`).
  - It PUTs each stage's output unconditionally to `s3://opal-data-49financial/gold/advi/<table>/date=D/{data.parquet,
    manifest.json}` (`runner_common.py:34,39,103-104,124-125`).
  - A live `mkdir` lock refuses a second run with `CHAIN REFUSED`, rc 3 (`chain_49f_entrypoint.py:549-563`).
  - A dispatcher-started host halts itself 2 minutes after the run (`advi_49f_floor.tf:291`).
- **What it does today (measured 12:0xZ, `logs filter-log-events`, 14 days, 249 events, no nextToken):**
  - 108 dispatches: 14 floor, 94 accelerator.
  - Every `08335338` marker date is PUT about 10 times within ~40 s, and each PUT dispatches the chain.
  - 61 dispatches were REFUSED by the lock, and 33 dispatches started the host.
  - Chain logs under `gold/advi/_logs/` show one run per burst lasting beyond seconds, plus the 12:45Z floor.
  - **So the served chain already re-derives and re-PUTs the same `D` at least twice on every Schwab day. That is row
    `NFRA_OPLGTW-S4`.**

### 4. What each act MAY touch, both branches, and the rollback for each key

| key / resource | A1 deploy | A2 replay | rollback |
|---|---|---|---|
| `opal-data-assets` `schwab/{m}/meta/complete/date=*.json` | from the first post-deploy conversion, the same keys as today gain one field `closure`; the 9 v1 fields are unchanged (`OG-c-1` AC2/AC13). **Branch a:** the runtime's botocore sends `If-None-Match`/`If-Match`, so an identical qualified closure writes nothing (W4-S4) and the PUT count per date is at most today's. **Branch b:** it cannot send them, so the v1 PUT lands as today and the closure records `write_guard: unconditional` / `incomplete` (W4-S2). | 2 keys for `D_r`, one per master | bucket versioning Enabled (`OG-p-1` OGP1-AC4): restore the prior version of each key written |
| `opal-assets-silver-schwab` Lambda code | new artifact, 1 of 6 families (`OG-c-2` AC3 refuses any other row) | -- | re-apply the prior pin `5c7b2a9a6b` through safe-apply |
| bronze / silver objects | none | none (OGC2-AC10 proves it by VersionId) | -- |
| dispatcher invocations (via `08335338` keys only) | at most today's count per date, in today's windows (the same producer triggers) | at least 1, at replay time | none needed: an invocation writes nothing itself |
| `bd-gold-layer-runner` EC2 host | as today | may be STARTED by the dispatcher; it halts itself through the document's existing branch. No act of this order stops it | -- |
| `opal-data-49financial` `gold/advi/<table>/date=D/{data.parquet,manifest.json}`, D = prev_trading_day(time of the fire) | as today: the marker CONTENT reaches neither the dispatcher nor the chain, so A1 changes no served VALUE; it can change only the NUMBER of fires (branch a: fewer) | **Branch R (refused):** a sibling run holds the lock and nothing is written. **Branch W (runs):** every stage table's `date=D` partition is re-PUT from the inputs present at the fire. That is the same act the 12:45Z floor and the morning burst already perform for the same `D`. | bucket versioning Enabled (measured 12:0xZ `get-bucket-versioning`): restore each re-PUT key's prior version; the next floor re-derives the same `D` |

Expected outcome, read from the producer's rule and not predicted: the replay-caused chain run's `D` is
`prev_trading_day` of the fire time, **not `D_r`**. So the replay never writes a historical 49F partition.

### 5. Conditions this half attaches (binding on `OG-c-2` by the order's "Read: ... the sign-off record")

1. Run A2's `08335338` write **outside** the producer's burst windows (09:30-10:30Z, 21:30-22:30Z) and the floor window
   (12:40-13:00Z). The triggered run then reads the day's settled inputs.
2. Record, in the result file, **every dispatcher invocation A2 caused**: its time, its outcome (REFUSED, or the
   `command_id` and chain log key) and, for branch W, the `date=D` object VersionIds of each stage table before and after.
   The served plane is then measured, not assumed.
3. Before A1, record the deployed runtime's botocore version and whether it accepts `IfNoneMatch` (W4-S2). This decides
   branch a or b in the record, not in prose.

**Signed:** `2.0.0_SA_COO~O`, issuer of `OG-c-2`.

---

## Half 2 -- `1.0.0_SA_CTO` -- OWED

(The CTO's half is written here, in this file, in its own commit.)
