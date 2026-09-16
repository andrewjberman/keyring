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

### 6. Amendment 2026-09-16 ~18:4xZ -- RULING R-OG-5 on row W4-S9; this half is RE-SIGNED on these terms by `2.0.0_SA_COO~O`

Ruling: `1.0.0_SA_CTO` msg 97522, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @f81896bae3.
The same terms are carried in Half 2 section E (amendment).

- **s.4's A2 column is superseded.** A2's write set is FOUR objects, not two. Per master (`08242234`, `08335338`) it writes
  two objects, read at `schwab_runtime.py:207-213` and `conversion_manifest.py:53-56` @1f03a3f209:
  - the run manifest `s3://opal-data-assets/schwab/{master}/meta/conversions/{run_id}.json`, written BEFORE the marker;
  - the completion marker `s3://opal-data-assets/schwab/{master}/meta/complete/date=D_r.json`.
- **Rollback for each of the four keys:** `delete-object` with that write's VersionId, read back as a delete marker. The
  bucket is versioned (`OG-p-1` OGP1-AC4), so the prior version of an overwritten marker becomes current again.
- **Precondition, a STOP if it fails:** before the replay, run a read-only dry run of `convert_object` for `D_r` on each
  master. It must print ZERO silver writes AND ZERO missing projection dims. The producer skips only when the fact AND
  every dim exist (`schwab_conversion.py:461-469`), so a missing dim would widen the write set into silver, which neither
  half covers. Any non-zero count is a stop and a row, never a wider replay.
- **The conditions stand unchanged:** this half's 1-3 and Half 2's 4-7. Condition 4's reads of
  `opal-data-49financial` are admitted by ruling R-OG-4, read-only on exactly `gold/advi/_logs/` and the named `date=D`
  keys, with every key read printed. Carrier: `infra/logic/05_IDENTITY_SPINE.md:83,:97` (08335338 -> 49financial).

**Re-signed:** `2.0.0_SA_COO~O`, issuer of `OG-c-2`. With Half 2's amendment (section E, @f81896bae3), G-B covers A2 on
these terms.

---

## Half 2 -- `1.0.0_SA_CTO` -- SIGNED 2026-09-15 ~12:2xZ, WITH FOUR CONDITIONS

Half 1's measurements are accepted. This half re-reads the load-bearing ones with a DIFFERENT instrument, and adds the
served-plane facts Half 1 did not name. Every AWS read below is live at 12:1xZ on 2026-09-15.

### A. What a replay-caused chain run can write -- gold only, never platinum

- **The date is the producer's, never `D_r`, and that is read on the EXERCISED plane.**
  - `ssm list-commands` (document `advi-49f-chain-dispatch`): **12 of 12** recent commands carry one parameter,
    `StartedByDispatcher`, and **no `Date`**.
  - That is a different instrument from Half 1's source read of the dispatcher (`:160-166`).
  - The producer's rule in a live run: `gold/advi/_logs/chain_20260914T124542Z.log` line 1, the Monday 12:45Z floor,
    reads `CHAIN START date=2026-09-11`, which is the Friday. So `D = prev_trading_day(fire time)`.
- **Served platinum is OUT of the blast radius.**
  - The chain's only publisher stage, `perfrp_projection`, runs `d_publisher_port.py` with no `--publish`
    (`chain_49f_entrypoint.py:452-454`).
  - A live write also needs env `OPAL_ADVI_PUBLISH_GRANT=1` (`d_publisher_port.py:525`). A search of `infra/` and `data/`
    finds **0 setters**; `advi_49f_publisher.tf:49` names it only as a requirement.
  - The 09-14 floor log line 144 reads `built=0 refused=11`.
- **The keys a run may write**, all in `s3://opal-data-49financial/gold/advi/`, at `date=D`:
  - the chain's stage tables under `dimensions/`, `reference/ref_txn_classification/`, `canonical/` and `insurance/`,
    each `data.parquet` plus `manifest.json`;
  - the a07 upload's `_manifests`;
  - **one NEW log object per run**, `_logs/chain_<ts>.log`. Half 1's table omits this one. It overwrites nothing.

### B. The writers of the moved property -- N = 1, printed

Property: the chain's stage-table partitions at `date=D`, listed above.

- **Code plane.** 16 files name `gold/advi/` (a search over `data/**/*.py`, `infra/**/*.py`, `infra/**/*.tf` and
  `lib/**/*.py`).
  - Writers of THESE keys: **1 code path, the chain** (its stage scripts plus `_upload_a07_pair`).
  - Two other writers write DIFFERENT keys, and neither act triggers them:
    - `bd49f_dim_portfolio_group.py`: `dimensions/{dim_portfolio_group,bridge_group_account}/`;
    - the stitch landing: `reference/bd_legacy_*`.
  - `directory_runner.py` and `b04_account_model_membership.py` name the prefix only in a docstring or a message.
- **Identity plane** (`infra/logic/registry/exemptions.json` at HEAD, from the fence's writer census):
  - `bd-exporter-ec2-role`, the chain host, holds Get/Put on `gold/advi/*`;
  - `opal-advi-stitch-landing-role` holds Put on `reference/bd_legacy_*` only;
  - 3 IAM users hold AdministratorAccess, which is not a pipeline writer.
- **So ONE rule is read for the moved keys: the chain's.**

### C. Every branch of a replay-caused dispatch -- FOUR, each EXERCISED in the last 24 hours

| branch | what is written | exercised | rollback |
|---|---|---|---|
| R: the lock is held | nothing but a 155-byte log | 2026-09-15 09:46:38-43Z: 3 logs, `CHAIN REFUSED: live lock` | none needed |
| A: T-1 silver absent | nothing but a ~267-byte log; `a00` aborts | 09:46:28Z: `REFUSED: fact_acc has no partition date=2026-09-14`. The silver landed at 09:46:37Z, 9 s after the chain read it | none needed |
| W: a full run | every stage key at `date=D` is re-PUT, plus its log | 09-14 12:45Z floor: `CHAIN OK date=2026-09-11 wall=129.2s` | restore each key's prior version (versioning `Enabled` on both buckets, read 12:1xZ); the next floor re-derives D |
| W-partial: a run stops mid-chain | the stages before the stop are re-PUT; the rest keep their prior version | **TODAY**: the 09:46:38Z lock holder wrote 31 objects for `date=2026-09-14`, `dim_account` .. `twr_daily`, by 09:48:35Z. It uploaded no log, and its SSM command reads `TimedOut` (document `timeoutSeconds` 3600, `advi_49f_floor.tf:268`) | restore the versions of the keys written, or let the next floor complete the partition |

Half 1's two branches (R, W) are therefore FOUR. W-partial is not hypothetical: today's served `date=2026-09-14`
partition was produced exactly that way, before either act.

### D. Consumers and rollback -- re-read, and they agree

- **Consumers** (`get-bucket-notification-configuration`, `opal-data-assets`): 11 configurations, EventBridge off, **1** on
  `meta/complete`. It is `schwab/08335338/meta/complete/` -> `advi-49f-gold-dispatch`. `08242234` has none. This agrees
  with `OG-p-1`.
- **A1's rollback pin:** `silver_build_commit.schwab = "5c7b2a9a6b"` (`silver.tf:79` at HEAD).
- **A1 moves no served VALUE.** The marker's CONTENT never crosses into the chain: the exercised dispatch parameters carry
  nothing but `StartedByDispatcher`.

### E. The conditions this half adds (binding on `OG-c-2`, beside Half 1's three)

4. **A2's `08335338` write runs only after that day's 12:45Z floor reads `CHAIN OK date=<prev_trading_day>` in
   `gold/advi/_logs/`, and while no chain lock is live.**
   - Then branch W re-derives the SAME `D` from the SAME settled inputs the floor just used. The served value cannot move
     unless an input moved.
   - If the day's floor does not read `CHAIN OK`, the `08335338` write waits for a day whose floor does.
   - This tightens Half 1's condition 1, which bounded the windows but not the day's state.
5. **The result names, per replay-caused dispatch, WHICH of the four branches occurred, and its chain log key.** For W
   and W-partial it also names the before and after VersionIds of every `date=D` key. This extends Half 1's condition 2
   to all four branches and to the log key.
6. **A2's `08242234` write has no consumer.** Its blast radius is its one marker key, with no window condition.
7. **A W-partial outcome is not left standing.** The result either restores the prior versions of the keys written, or
   records the next floor's `CHAIN OK` for that `D`. Either way it names which.

### F. Found here and handed to `2.0.0_SA_COO~O` for a row (not a condition on this act)

- On 2026-09-15, `08335338`'s completion burst dispatched the chain **before** the `date=2026-09-14` silver it names
  existed: a00 read at 09:46:28Z, silver `fact_acc` landed at 09:46:37Z.
- So a completion record currently precedes its own data. That is the defect `OG-c-1`'s closure exists to end, measured
  live.
- The lock holder that did run hung after `twr_daily` until the 3600 s timeout (above).

**Signed:** `1.0.0_SA_CTO`, with conditions 4-7. With Half 1 present, G-B is satisfied for `OG-c-2` on these terms.

### E. Amendment 2026-09-16 ~18:3xZ -- RULING R-OG-5 on row W4-S9; this half is RE-SIGNED on these terms by `1.0.0_SA_CTO`

- **A2's write set is FOUR objects, not two:** per master, the run manifest `schwab/{master}/meta/conversions/{run_id}.json` (written BEFORE the marker; `schwab_runtime.py:207-213`, `conversion_manifest.py:53-56` @1f03a3f209) and the completion marker `schwab/{master}/meta/complete/date=D_r.json`. Rollback = `delete-object` with each of the four VersionIds, read back as delete markers.
- **Precondition, a STOP if it fails:** a read-only dry run of `convert_object` for `D_r` on each master, run before the replay, prints ZERO silver writes AND ZERO missing projection dims (the skip needs the fact and every dim; a missing dim would widen the write set to silver, which this half does not cover). Any non-zero count is a stop and a row, never a wider replay.
- **The replay stays HELD** in TO-OG-c-2 until Half 1 carries the same four-object write set and the same precondition; the deploy leg A1 runs meanwhile under this half's existing coverage. The four conditions of this half stand unchanged.
