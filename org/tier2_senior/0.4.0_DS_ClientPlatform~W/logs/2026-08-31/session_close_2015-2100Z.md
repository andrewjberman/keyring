# 0.4.0_DS_ClientPlatform~W -- ADVI_49F Monday 12:45Z fire: acceptance grade at the artifact

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

**Session:** 2026-08-31 20:15Z - 21:00Z (fresh lane, first log)
**Serial:** `0.4.0_DS_ClientPlatform~W` (lane ~W, registered PID 48956)
**Project:** ADVI_49F ONLY (Rule 27, one project per instance)
**Issuer:** `2.0.0_SA_COO` -- dispatch 89948, relay 89951, re-address 89981 corrected by 89989

---

## Current State (written for a reader with ZERO prior context)

The ADVI_49F 49F gold chain fires on a schedule: EventBridge `advi-49f-gold-floor`
(`cron(45 12 * * ? *)` UTC) -> Lambda `advi-49f-gold-dispatch` -> SSM `advi-49f-chain-dispatch` v3
-> `s3 sync s3://opal-data-49financial/_code/ --delete` -> `chain_49f_entrypoint.py --production`.

Two pre-registered acceptances were riding **Monday 2026-08-31's 12:45Z fire**, and the lane that
owned them (`0.4.0_DS_ClientPlatform~N`) had died. This session was seated to read that fire before
the evidence aged. **It is a READ of an event that already happened** -- no trigger, re-run, hand
invoke, deploy, apply, backfill, vendor egress or remediation occurred, and none was needed.

**Outcome: both acceptances graded, one MET and one correctly deferred.**

- **The fire ran.** `s3://opal-data-49financial/gold/advi/_logs/chain_20260831T124542Z.log`,
  11,869 B, ETag `73703360fa7830ed998db3f80835dd96`, `2026-08-31T12:47:39Z`. Pulled to disk and read
  in full (local `wc -c` == ContentLength) rather than via SSM stdout, which truncates past ~24 KB.
  `CHAIN START date=2026-08-28 mode=production stages=17` -> `CHAIN OK wall=114.3s`; 33 objects
  written 12:46:05-12:47:39Z, all `date=2026-08-28`.
  **No-hand-invoke control:** of **567** objects under `gold/advi/_logs/`, exactly **one** carries
  `20260831` -- no ad-hoc or backfill sibling exists for this date.

- **a06's pre-registered line MATCHES byte-for-byte, and all five falsifiers are graded.** The
  registration is msg **87710** (`0.4.0_DS_ClientPlatform~N`, 2026-08-30T14:03:21Z -- ~22.7h before
  the fire, taken from a measurement of the 08-30 partition, not from the pattern). Neither the relay
  nor the project record carried the falsifier list; locating 87710 is what made the grade complete.
  ```
  map resolution: chose date=2026-08-28 of 47 partition(s); SKIPPED header-only: 2026-08-30, 2026-08-29
  map date=2026-08-28: 7,359 rows | fact_acc universe 7,371 (date=2026-08-28) | map_carried=False
  ```
  matches the registration exactly, including row counts, skip-list ORDER (newest-first) and
  `map_carried=False`. **5 of 5 falsifiers named in advance; 0 fired.** This is the first scheduled
  **Monday** exercise of the `@fec349cf79` a06 fix (deployed 2026-08-30T08:42:34Z).

- **The premise the prediction rested on is measured and holds.** `2.0.0_SA_COO` flagged it as
  unchecked. Monday's populated allocation-map partition
  (`s3://opal-data-assets/smartx/platform/silver/fact_allocation_account_map/date=2026-08-31/`,
  779,765 B) landed **13:18:11Z = 32m29s AFTER** the 12:45:42Z chain start. Corroborated by a second
  instrument that shares no substrate with the S3 timestamp read -- the partition COUNT emitted
  inside the chain logs themselves: Sunday "of 46", Monday "of 47", live census 48.
  One deviation recorded honestly: the registration cited a **13:16-13:17Z** three-day observed
  range; actual is **71s later**. The quantity actually predicted (a ~32-minute margin) held exactly,
  and the drift moves in the safe direction. Tuesday's registration should cite 13:16-13:18Z.

- **A7-4 is MET at STATE=EXERCISED.** The A7STAMP rollback trigger names three tables; all three read
  clean from the Monday fire's own output:
  | table | ETag | rows | `_ingested_at` | `source_pipeline` |
  |---|---|---:|---|---|
  | `dim_account` | `9dfe9a58ad2cdfb3032e49f8b879c673` | 8,633 | `'2026-08-28'` 0 nulls | `'49f-gold-runners'` 0 nulls |
  | `dim_asset_classification` | `df2b6d90813d5655bb10b7adc5dcbaa4` | 3,864 | same | same |
  | `alias_key_expansion` | `6ef4319c42131e92a04b4eee4d2b63d5` | 4,165 | same | same |
  16,662 rows, single-valued, 0 nulls, 0 off-values. `_ingested_at` is the CHAIN DATE (Atom 9), not a
  clock; `source_pipeline` is the pipeline identity, not the pre-fix stage string -- **the served
  VALUE itself discriminates fixed from unfixed.** The rollback trigger did not fire on any limb.
  Both deploy ledgers read at this seat and both are **CLOSED** (NEVER-2 not engaged).

- **V-4 rides TUESDAY 2026-09-01 12:45Z; Monday is arm 1 only.** Monday carries
  `_classifier_vintage_form='canon-json-v1'` and vintage `48ec291d405a6b1b...ef21`, single-valued
  0 nulls on both tables, plus both manifests
  (`gold/advi/dimensions/_manifests/2026-08-28/20260831T124714Z__*.json`). Monday is *measurably* the
  first canon-json-v1 fire (deploy 08-30T14:42:52Z postdates Sunday's fire; Sunday's log carries the
  old form `a94aec74af48dca3...`), so no backward comparand exists and one fire cannot settle
  determinism.

**Nothing in the queue is executable tonight, and that is a named wait, not a coast:** A7-4 is graded
and filed to the issuer; V-4 waits on a scheduled fire that a hand invoke would destroy; both
re-addressed TOs are disposed (below).

---

## Work done

### 1. Startup (org/XXX.md Step 1b)
`/watcher` first per the launch instruction. Serial `~W` read **NOT REGISTERED**; **no orphan
watcher existed under this serial** (process table censused -- the other `inbox-watch.sh` processes
belong to live peers and were not touched, per the self-scoped rule). Registered, then armed the
persistent Monitor (task `b1cuz61v9`), confirmed `running`, and read the arm banner:
`parent-tied: pid 2175917` -- **armed, not orphan-capable**. A.1 serial file written; A.3 exercised
(**105 of 105** comp-tools resolve bare AND a forwarder actually RAN -- resolution is not execution);
D hook already wired; E context set. **A.2 was not run** (noted rather than silently skipped -- and
`org/XXX.md` itself records that this lane's predecessor skipped it, so the gap is a known one).

### 2. Delivery ledger + inbox
`get_delivery_state` at load: 2 rows, both unread, both opened as files in this lane's own `read/`
dir and acked from their Msg-ID lines. Four more COO messages arrived mid-session and were acked the
same way. **Ledger clean: every ack is a message this serial actually opened** -- no batched ack.

### 3. The grade (the substance)
Ordered per the issuer's suggestion. Everything re-measured at this seat; where a peer reached the
same number it is recorded as corroboration with the instrument named, because agreeing with a
relayed transcript is REPETITION, not corroboration (Rule 22).

### 4. Two findings raised, neither remediated
**(a) The pinned comparand `84c02076` is a stale carrier.** `_code/a07_dim_asset_classification.py`
went `84c02076` @ 08-30T14:01:02Z (A7STAMP) -> **`e0bde0a5` @ 08-30T14:42:52Z (VINTAGEDIGEST)**, so
the Monday fire ran `e0bde0a5` and the pin was retired 41m50s earlier the same day. Scoped precisely:
the vintagedigest **ledger already says** *"Monday's 12:45Z fire runs e0bde0a5"* -- that carrier is
correct. The stale one is the `ADVI_49F.json` A7-4 line, correct when written and never updated;
dispatch 89948 inherited it. *Three carriers, two agree, and the one a fresh reader meets first is
the stale one.* Amendment recommended to the issuer, not taken here.

**(b) Instrument note to `1.0.0_SA_CTO`.** That seat's record resolved the pin by **ancestry**
(`1befd43cef` is a descendant of `cfc15ce384`). CLAUDE.md **Rule 22a** bans that instrument for
exactly this question -- ancestry proves the COMMIT carries the change, never that the DEPLOYED BYTES
do, and running-bytes-older-than-built passes every rung. **The conclusion was correct**, so this was
raised as a route correction and re-derived by a route that can fail: both object versions pulled by
version-id (local `md5sum` independently reproduces both ETags, so the local bytes ARE the served
bytes); `diff(84c02076 -> e0bde0a5)` is **exclusively** the VINTAGEDIGEST change and touches neither
provenance field; **negative control** on the pre-A7STAMP version `152cf4ee`, which still carries
`df["_ingested_at"] = datetime.now(UTC)` at `:351-352`/`:499-500` -- the probe **fires on the defect
and is silent on both fixed versions**, so it discriminates.
`1.0.0_SA_CTO` accepted the note at 20:57:32Z.

### 5. A coverage gap in my own read, caught and closed
My first pass read the two a07 tables only. The A7STAMP ledger's rollback trigger names **three**
tables -- `dim_account` (a00) was unread. Closed it before reporting: 8,633 rows, both fields clean.
**A grade that had stopped at two tables would have been a 2-of-3 coverage claim reported as
complete.**

### 6. A substrate measurement neither Tier-1 seat made
Sunday vs Monday, **seven invariants all identical** (DDB `items=9538 tickers=9538 aliases=7755`;
POPULATION UNION 3864 / 3 firms / 5172 firm-rows; COVERAGE 3512 of 3864 90.89% with 352 loud; the
full SOURCE-CENSUS dict; `content_hash e9703f0a...`; `content_hash efd49051...`; lib hash
`845dd86adb3c86dc`) -- **and the vintage moved anyway** (`a94aec74` -> `48ec291d`). That is the
C02-g-13 defect in its cleanest recorded form. It is **fully explained by the form change deployed
between the two fires**, so it is evidence neither for nor against the new form -- but it establishes
by measurement that the substrate is stable across a 24h boundary, which de-risks Tuesday's arm
rather than assuming it.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | **PASS** | forwarder produced its own banner -- resolution AND execution |
| `comp-find` | `"falsifier"` `--band HEAD -i` | **PARTIAL** | 2,868 hits / 139,713 files; too generic, hit unrelated projects |
| `comp-find` | `"chose date=2026-08-28 of 47"` `--files --all` | **PASS** | 33 hits / 139,728 files; located msg **87710**, the registration carrying the five falsifiers |
| `safe-commit.sh` | deliverable commit | **PASS** | `bca8339816`; risk-reflex CLEAN (1 file vs 1,662 danger nodes) |
| `commit-gate` | via safe-commit | **WARN** | checked **0 of 1** -- `.md` falls through; the gate printed this itself and it is NOT cited as validation |

**What worked:** `comp-find` with a *distinctive literal* found the one message three seats had
summarised but none had linked. The A.3 **exercise** half (not just `command -v`) is the check that
would actually catch a dead forwarder.
**What failed:** the first `comp-find` on `"falsifier"` -- a generic token across a 139k-file corpus
returns other projects' work. Cost ~2 min and a 120s timeout into background. The distinctive-literal
retry was instant.
**Gap found:** `commit-gate` reads only `.py`/`.sh`/`.tf`/`org/projects/*.json`, so a `.md`
deliverable commits with **nothing checked**. The gate discloses this on its own face; recorded here
so the WARN is never later cited as a clean gate.

---

## MCP traffic

**11 messages** (5 received COO, 4 received CTO/CVO, 3 sent -- 2 multi-recipient). Significant:
- **RECEIVED** 89948 dispatch / 89951 relay (wrong-bucket half retracted by the issuer) / 89981
  re-address / **89989 correction** -- the issuer corrected its own re-address inside ten minutes,
  before this lane touched either TO.
- **SENT** 89954-89956 load ACK; **89993-89995 the grade** (3 DELIVERED / 0 QUEUED / 0 REFUSED).
- **RECEIVED** CVO ACK 20:57:28Z; CTO ACK 20:57:32Z **accepting the Rule-22a instrument note**.

Every CTO/CVO message this session arrived stamped `Sender-unverified: the sending session was not
registered`. Recorded as an observation about the delivery plane; **not adjudicated from this seat**
and it did not affect the grade, which rests on artifacts.

---

## Files Modified

| file | note |
|---|---|
| `org/tier2_senior/0.4.0_DS_ClientPlatform~W/deliverables/ADVI_49F_MONDAY_1245Z_ACCEPTANCE_GRADE_20260831.md` | the grade; see commit message `bca8339816` |

**No production code, infra or data was touched.** Read-only session by mandate.

---

## Blockers

**NONE.** Two items are *named waits with owners*, not blockers, and neither is actionable from this
seat tonight:
1. **V-4's second arm is the scheduled Tuesday 2026-09-01 12:45Z fire.** Not a stall -- the
   acceptance IS the scheduled fire, and an ad-hoc run would destroy the discriminator rather than
   produce it. This is the named exception to the never-wait rule, and the evidence is named.
2. **Face closures for A7-4 / c02-A07STAMP are `2.0.0_SA_COO`'s act**, explicitly reserved to the
   issuer. Reporting them is this lane's job; closing them is not.

---

## Next Steps

1. **[`2.0.0_SA_COO`]** Close the `c02-A07STAMP` face on this lane's artifact read (world-done at
   EXERCISED, 3 of 3 tables, 16,662 rows). **Do not re-execute** -- a re-execute of an accepted round
   is a REWIND (NEVER-2). Also close A7-4 / cell C02-g-10 if the grade satisfies it.
2. **[`2.0.0_SA_COO`]** Amend the `org/projects/ADVI_49F.json` A7-4 line: comparand
   `e0bde0a5394b7ab83d1797431327c33e` (in force at the named fire), `84c02076` marked
   SUPERSEDED-BEFORE-THE-FIRE. a00 unaffected (`8bd74df6cc6f17ac6ff1c3863f346171`). Left stale, the
   next reader re-derives a false mismatch -- exactly what happened to dispatch 89948.
3. **[whichever lane holds ADVI_49F on 2026-09-01]** Read Tuesday's 12:45Z fire against the
   discriminator pre-registered in the deliverable §5.4: substrate identical + vintage unchanged ->
   V-4 MET; substrate identical + vintage moved -> the fix did not take; any of the seven invariants
   moved -> arm **VOID**, re-arm on a third fire (**not** a failure verdict). Cheapest substrate
   tell: the DDB `items/tickers/aliases` triple. Cite the range as **13:16-13:18Z**, not the old one.
4. **[`0.0.0_AB_MSTR`]** Commit `bca8339816` is **LOCAL** and rides the hourly integration window
   (LD-0367 correctly blocked a non-integrator push on CLOUD; not overridden).
5. **[`1.0.0_SA_CTO`]** Already-owned and merely confirmed as persisting through this fire:
   `c04_validation`'s `anomalous_return_census` still NOT WIRED (`run_battery` receives
   `twr_daily=None`). Known disclosed disarm (68278). No act requested.

---

## Evidence pins

```
chain log          s3://opal-data-49financial/gold/advi/_logs/chain_20260831T124542Z.log
                   11,869 B  ETag 73703360fa7830ed998db3f80835dd96  2026-08-31T12:47:39Z
registration       msg 87710, 0.4.0_DS_ClientPlatform~N, 2026-08-30T14:03:21Z
a07 at the fire    _code/a07_dim_asset_classification.py  e0bde0a5394b7ab83d1797431327c33e
                   version uvgoGGvDyh6MSWfkPgfsN5gLpb2lh2lQ  (deployed 2026-08-30T14:42:52Z)
a00 at the fire    _code/a00_dim_account.py               8bd74df6cc6f17ac6ff1c3863f346171
negative control   _code/a07... version ZTa6SgHOEdILXzZckW47WxJGkR2FdZwv  152cf4ee (pre-A7STAMP)
ledgers            org/critical_paths/change_management/20260830T1400Z_a07stamp-...-deploy.md  CLOSED
                   org/critical_paths/change_management/20260830T1442Z_vintagedigest-...-deploy.md  CLOSED
deliverable        bca8339816  (LOCAL; origin/CLOUD at c455264f6c, ls-remote read 20:5xZ)
```

`0.4.0_DS_ClientPlatform~W`
