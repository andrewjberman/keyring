# Session Log -- 0.6.2_AE_PartnerETL~A -- 2026-07-22 1518-1815Z

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, IMPLEMENT

## Summary

Andrew-direct GO (~1615Z, relayed by CTO): ad-hoc re-pull of the missing Inflection dates into
bronze, grounding the mechanism BEFORE any write. Outcome:

- **Orion assets 07-11..07-15 REPAIRED at source** (`s3://opal-data-inf/bronze/assets/`), 5/5
  verified, pulled against each date's OWN household roster. Faithfulness proven against a
  same-day capture, not asserted.
- **Root cause named at source**: the Orion RAW producer died after 2026-07-10 while the PARQUET
  producer kept running. Not a vendor outage, not two coincident ones.
- **Eclipse: NOT re-pullable, but NOT "permanently unrecoverable"** -- my own earlier claim,
  corrected on Andrew-direct. Assignment dimension IS recoverable with a named exception set;
  the census that proves it now exists (848/848 portfolios).
- **Two gaps nobody had**: eclipse `2026-06-01`, orion `fact_positions 2026-07-01`.
- **One artifact written, then DELETED on Andrew-direct, then re-pulled correctly** -- the first
  backfill was point-in-time on prices and current-date on composition.

**ZERO repo commits this window before this log.** All work was S3 + vendor reads.

## Work Done

### 1. Startup -- LD-0290 marker missing (own reachability defect)
Came up from a `/clear`, NOT a fresh session. Inbox Monitor `bur9da1yk` was alive and proved it by
delivering mid-startup -- so the watcher was correctly NOT reaped (the 2026-07-16 MSTR
false-positive class). But `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial` did not exist: the
session UUID rotated across the clear while the Monitor task persisted. Halt gate would have
adopted the shared `.agent_context` (which reads `SERIAL=0.7.0_AE_CloudOps`), making a `[STOP]`
addressed to me invisible to my own gate. Written + read-back verified.
**Shape worth carrying: a context-clear presents to LD-0290 as a NEW session and to the Monitor as
the SAME session. I was reachable and un-haltable simultaneously, and reachable is the half that is
easy to check.**

### 2. Mechanism grounded BEFORE any write (Rule 22)
- `comp-assets` (self-test PASS 15/15) censused both channels.
- Per-feed date-set differencing: `orion fact_assets` (2,272 dates) vs `fact_positions` (2,277)
  across the FULL 6-year history -> difference is exactly 9 dates: four at the 2020 history edge
  (assets starts 04-28, positions 04-24) and **2026-07-11..07-15**. That contiguous block is
  orion assets' ONLY interior gap in six years.
- `silver/fact_assets` mirrors `bronze/assets` with **zero divergence both directions** -> the gap
  originates AT/ABOVE bronze ingest. Mirror and converter exonerated.
- Source truth: `opal-data-inf/bronze/assets/2026-07-{11..15}` exist as **`.parquet` ONLY, no
  `.jsonl.gz`**. `opal-assets-ingest-mirror/lambda_function.py:19-31` names this exact condition.
- Legacy generations (`bronze/orion-api/`, `orion-api-v2/`) carry the full gap window but hold
  DIFFERENT data types (accounts/billing/tax/transactions/dimensions). Their running cleanly
  through the window is corroboration the failure was the raw producer, not the vendor.

**An instrument failure I caught on myself:** my first bronze probe assumed `date=` partitions and
returned 0 dates for both feeds, contradicting comp-assets' 2,272/2,277. The tell was a
"silver-not-in-bronze" diff dumping all six years. Bronze is FLAT `<date>.jsonl.gz`. Discarded and
re-run with a positive control. **Reported nothing from the broken pass.**

### 3. Eclipse -- claim made, then corrected on Andrew-direct
Initially reported "permanently unrecoverable." **Andrew ~1740Z: that is wrong; rectify it.** He
was right, and CTO had carried my sentence upward.

**What survived, upgraded from doc-claim to EXERCISED:** live `GET /v1/portfolio/portfolios` with
8 candidate date params (`asOfDate, asOf, date, effectiveDate, asofdate, snapshotDate,
valuationDate, fromDate`) -> **byte-identical bodies**, same SHA-256, same 848 rows, HTTP 200 each.
It does not reject a date, it ignores one. Catalog re-scanned BY LISTING (336 GET rows): `/report/*`
is trade/block reporting, `/dashboard/*` carries no date params.

**What fell:** "the DATA cannot be had." `fact_portfolios_full` is 57 fields on two clocks --
assignment/config (slow) vs valuation/analytics (daily). The audit log carries assignment changes
with a WORKING date filter; it carries **zero value fields**.

**The census that makes it actionable (848/848 portfolios, zero failures, span 05-01..07-22):**

| gap date | portfolios changed |
|---|---|
| 2026-06-01 | 0 |
| 2026-07-01 | 2 |
| 2026-07-13 | 14 |
| 2026-07-14 | 1 |
| 2026-07-15 | 7 |

(07-10, the day before the gap, carried 67 -- the window was quiet. 578/848 have any record in
span, so the instrument is not returning trivial emptiness.)

**ARCHITECTURAL LINE STATED AND HELD: a reconstruction is NOT a bronze backfill.** Any
carry-forward + audit + derived-value artifact belongs at silver/gold WITH provenance.
`bronze/eclipse/{date}/` must stay an honest hole.

### 4. Eclipse puller fabrication hazard (surfaced, now carried by 4 records)
`data/inf/scripts/bronze/pull_eclipse_portfolios.py` `--date` is **a FILENAME, not a query**:
`:230` no date on the wire, `:270` defaults to today, every `date_iso` use is an S3 key/log/sentinel.
Running it for 07-13 today writes TODAY'S live state to `bronze/eclipse/2026-07-13/` at exit 0.
COO independently found the sharper edge: the `pull_complete.json` sentinel writes the WRONG DATE
into provenance next to `"overall": "success"` -- the lie wears a provenance stamp.
**Generalisation carried by COO to CTO: absence is the wrong control when the failure is CONTENT,
not COLLISION.** CTO's guardrail 1 (verify ABSENT, never overwrite) would not have caught it.

### 5. Orion backfill -- written, deleted, re-pulled correctly
**Pass 1 (DISCARDED).** `--start 2026-07-11 --end 2026-07-15 --upload-bronze`. Landed 5/5, exit 0,
sane sizes. **WRONG**: `_hh_universe.load_household_universe` resolves the roster via
`latest_hh_rep_map_key` -- the NEWEST snapshot. Correct for a daily run, wrong for a backfill. It
pulled 07-13 against the 07-22 roster of 323 households instead of that date's 318. Right prices,
wrong book. **Deleted on Andrew-direct** (delete markers recorded under Verification).

**Pass 2 (LANDED).** Universe pinned per-date from `silver/api_dims/household_rep_mapping/
snapshot_date={date}/data.parquet` (exists for EVERY gap date -- a READ, not a reconstruction).
Everything else reused unchanged from the stock puller: auth, fetch+retry, AdaptiveRateLimiter,
raw gzip-JSONL write, write-once resume guard, empty-pull-writes-nothing.
**Pinning validated BEFORE re-running:** as-of 07-16 universe = 319 households and the stored
same-day 07-16 capture carries exactly 319 distinct clients; as-of 07-10 = 316 vs stored 07-09 = 316.

### 6. Point-in-time proven by exercise, in two directions
- **Valuations ARE point-in-time**: same 5 clients across 4 dates returned 4 distinct MVs
  ($3,563,207 / $3,570,121 / $3,582,369 / $3,590,056). A date-ignoring endpoint returns identical
  bodies.
- **Per-client holdings ARE point-in-time**: my 07-09 control returned 677 rows for clients
  18/19/20/22/23; the stored same-day 07-09 capture has 179+102+118+204+74 = **677**. Exact.
- **The roster was the only defect** -- and I initially mis-diagnosed it as a DATA problem
  ("current-state roster") before the per-client evidence refuted it. Corrected in-session.

### 7. Concurrency finding (outlives this ticket)
The assets endpoint is PER-CLIENT (`/Portfolio/Clients/{cid}/Assets/{date}`), so one date = 318
sequential round-trips at ~1.22s. The limiter was PERMITTING 5.34 rps; we achieved **0.82**.
**We were never throttled -- we were blocking.** Measured proof: my eclipse audit sweep ran
**848 vendor calls in 6 seconds = 138.3 calls/s**, same vendor, same JWT, 429/503 backoff still
honoured -- ~170x purely from fanning out.
Andrew's instinct was "stop rate-limiting them"; the correction is that removing the limiter buys
NOTHING (never the binding constraint) and deletes the thing that caught their 503 mid-run.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | "enumerate every date partition ... find gaps" | PARTIAL | No curated rule matched; correctly flagged its own hits as fuzzy. Top hit `comp-assets` WAS right -- the rail earned its keep |
| comp-assets | `--self-test` | PASS | 15 checks; gated before trusting any output |
| comp-assets | `--channel eclipse` / `--channel orion` | PASS | Correct counts/frontiers -- AND surfaced the defect below |
| comp-grep | orion/eclipse bronze paths, `opal-assets-ingest-mirror`, `schedule_expression`, `pull_inflection_assets_v2`, `bronze/positions/` | PASS | Located producer, mirror, and mirror cadence with systems context |
| comp-glob | `**/*swagger*`, `**/*openapi*`, `**/INFLEC_API*` | NO MATCH | Correctly stated NO MATCH is not proof of absence; pointed me to content search, which found the catalog |
| pipescript | `inflection` | FAIL | Not a known named thread; printed the 27 known threads. `inflection` is a candidate registration |

**What worked:** `comp-which` -> `comp-assets` was the whole rail working as designed -- I would
have hand-rolled a listing and missed the channel census. `comp-glob`'s NO-MATCH copy explicitly
prevented an absence claim.

**What failed:** `pipescript inflection` -- the inflection chain has no named thread despite being
a live 2-vendor bronze->silver pipeline under active repair.

**GAP FOUND (report to CTO/0.8.0):** `comp-assets` renders each channel's own
`backfill-status.json`, and **BOTH eclipse and orion declared `complete: True | holes: 0 named`
while eclipse carried 4 July holes and orion assets 5.** Declared completeness is computed at
CHANNEL/DATE level -- a date counts present if ANY feed wrote it -- so `fact_positions(2,277)`
masked `fact_assets(2,272)` inside a channel calling itself complete. **Structurally blind to
per-feed gaps, which is the only kind we have had.** Also: no comp-tool exposes per-feed date-set
differencing; I used `# rail-checked:` overrides for it (4 calls, logged). A repeat override for
one intent = a coverage gap -> tool candidate.

## Deployment Sequence

**NO Lambda/TF/EC2 deploy this session.** Work was vendor pulls + S3 object writes/deletes in
`opal-data-inf` (source bronze), plus read-only vendor probes. No code committed, no artifact
deployed, no scheduler touched. The mirror was NOT fired manually.

## Verification (ACTUAL output)

**Final landings -- `s3api head-object`, explicit Z:**
```
  2026-07-11  Wed, 22 Jul 2026 18:04:41 GMT 2176938
  2026-07-12  Wed, 22 Jul 2026 17:58:07 GMT 2175913
  2026-07-13  Wed, 22 Jul 2026 17:51:35 GMT 2172954
  2026-07-14  Wed, 22 Jul 2026 17:45:01 GMT 2176843
  2026-07-15  Wed, 22 Jul 2026 17:38:51 GMT 2180491
  POSITIVE CONTROL 07-16 (pre-existing): 2166565
  NEGATIVE CONTROL 07-99 (must 404):     (404)
```

**Per-date content (pass 2, as-of rosters):**
```
  2026-07-15: roster 319  rows=34,942  mv=$202,880,787
  2026-07-14: roster 319  rows=34,942  mv=$202,375,855
  2026-07-13: roster 318  rows=34,935  mv=$201,601,607
  2026-07-12: roster 318  rows=34,935  mv=$202,843,646
  2026-07-11: roster 318  rows=34,935  mv=$202,843,646
```

**FAITHFULNESS -- my 07-15 vs the SAME-DAY 07-16 capture:**
```
  client sets: in15-not16=[]  in16-not15=[]   (319 == 319, byte-identical)
  shared clients=319  identical row counts=309  differing=10
  net row delta: +103, localised to 10 named clients (178 +47, 1406 +29, 1344 +13, 1408 +6, ...)
```
That is real position movement Wed->Thu, not a methodology difference.

**17a + never-overwrite:**
```
  gap-date .parquet surviving (expect 5): 5      <- never used as a backfill source
  07-10 raw LastModified: Fri, 10 Jul 2026 13:38:31 GMT   <- untouched, original
```

**Pass-1 deletions (recoverable -- versioned delete markers):**
```
  2026-07-11.jsonl.gz  DeleteMarker=True  Rrqw719qtCwXkPN1EdUYgK82yLKpjsYA
  2026-07-12.jsonl.gz  DeleteMarker=True  Af4fLQ_khEAgWtIRinBMattjNNVcmS._
  2026-07-13.jsonl.gz  DeleteMarker=True  Gl0ZDfaU7HFJNBBGjHHherCyVmHtPXm.
  2026-07-14.jsonl.gz  DeleteMarker=True  xS8Dmn3u4cxShiAF9_1Pc04Z.vaJwXjR
  2026-07-15.jsonl.gz  DeleteMarker=True  XfKbiTiTwf6YsaRHsj925ahtUP6eMpmJ
```

**PROPAGATION -- NOT DONE, and this is not a defect:**
```
  monolith bronze orion/inflection/bronze/assets/2026-07-13.jsonl.gz : ABSENT
  monolith silver orion/inflection/silver/fact_assets/date=2026-07-13/ : ABSENT
  CONTROL monolith silver date=2026-07-16 : 1
```
The mirror is POLLING: `mirror_inf` `cron(15 14 * * ? *)`, `mirror_cot` `cron(30 3 * * ? *)`, ONE
Lambda walking all three map rows, idempotent skip-if-landed. Today's 14:15Z pass ran BEFORE my
landings, so propagation is the next pass (03:30Z 2026-07-23). **Nothing to fire; I did not fire it.**

## Blockers

**NONE.** No BLOCKED items. Two decisions sit at Andrew by his own deferral (see Next Steps) --
those are AWAITING-DECISION, not blocked work.

## Current State

**Serial:** `0.6.2_AE_PartnerETL~A`. Zero repo commits this session prior to this log.

**REPAIRED (source layer only):** `s3://opal-data-inf/bronze/assets/2026-07-{11,12,13,14,15}.jsonl.gz`
-- raw gzip-JSONL, AES256, pulled per-date against that date's household roster. Verified above.
**These have NOT reached the monolith or silver.** Anyone reading
`s3://opal-data-assets/orion/inflection/silver/fact_assets/` before ~03:30Z 2026-07-23 will still
see the gap and must NOT conclude the repair failed.

**STILL EMPTY, correctly:** `bronze/eclipse/2026-{06-01,07-01,07-13,07-14,07-15}/` -- unfillable
from the vendor. Do not run `pull_eclipse_portfolios.py --date <past date>`; it fabricates.

**Producer/mechanism facts a zero-context reader needs:**
- Puller: `data/inf/manual_api/pull_inflection_assets_v2.py`; writes `bronze/assets/{date}.jsonl.gz`
  to `opal-data-inf`; endpoint `GET {BASE}/api/v1/Portfolio/Clients/{cid}/Assets/{MM-DD-YYYY}`,
  `BASE=https://api.cloud.orionadvisor.com`. Accepts arbitrary historical dates (VERDICT A,
  `ADVI_INFSHIP_A2.md:60`; independently exercised this session).
- **The backfill defect lives in `data/inf/manual_api/_hh_universe.py`:**
  `load_household_universe()` -> `latest_hh_rep_map_key()` returns the NEWEST snapshot. Correct for
  daily, wrong for backfill. The as-of roster exists at
  `silver/api_dims/household_rep_mapping/snapshot_date={date}/data.parquet` for every gap date.
- Mirror: `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py`, TF at
  `infra/aws/terraform/opal-assets/mirror.tf:95-106`.
- Eclipse puller: `data/inf/scripts/bronze/pull_eclipse_portfolios.py`; `ECLIPSE_BASE=
  https://www.orioneclipse.com`; JWT via SM `orion/eclipse_jwt/current`.
- Scratchpad tooling written this session (NOT committed, reproducible):
  `eclipse_asof_probe.py` (8-param as-of probe), `eclipse_audit_probe.py` (windowed audit w/
  controls), `eclipse_audit_sweep.py` (concurrent 848-portfolio census, 16 workers),
  `backfill_asof_universe.py` (per-date roster-pinned backfill driver).

**WS-5 (prior thread, unchanged):** converter half COMPLETE @6d1a15ef2, NOT DEPLOYED. 0.7.0_AE_CloudOps
holds apply -> artifact -> exercise. **The exercise must assert the conversion manifest's
`mode == "event"`; parquet-landed is NOT sufficient** (my sweep backstop converts either way).

**MCP traffic:** 8 messages handled, 6 sent. Significant: COO 152158Z (hold binds fabric-wide;
"answer anything asked, initiate nothing new"); CTO 161501Z (Step-1 GO, Andrew-direct); DS 161922Z
(pre-emptive eclipse grounding + the two-date-lists-opposite-polarity trap -- prevented a real
error); COO 164916Z + 170102Z (pathspec hazard, then a downward severity correction); CTO 174554Z
(Andrew says my eclipse line is wrong, rectify). Sent: ACKs + the rectification + final matrix.

## Next Steps

1. **[0.6.2_AE_PartnerETL~A] `orion fact_positions` 2026-07-01 backfill -- NOT STARTED, awaiting
   Andrew.** Deferred by Andrew this session ("we'll handle those two points when you're
   instantiated next"). Source is `.parquet`-only; same endpoint, same corrected per-date-roster
   mechanism; ~6 minutes sequential (or seconds threaded). Missing from CTO's list entirely.
2. **[Andrew / 1.0.0_SA_CTO] Eclipse disposition for 5 dates** (06-01, 07-01, 07-13, 07-14, 07-15)
   -- deferred by Andrew this session. Now a COSTED choice, not a flat "never": (a) record as
   permanent holes; or (b) reconstruct assignment via 07-10 carry-forward + the 848/848 audit
   census (0/2/14/1/7 changed) and DERIVE valuations from Orion holdings. **(b) is a silver/gold
   artifact with provenance -- never a `bronze/eclipse/` key.** Residual unknown: Eclipse-computed
   analytics (`percentDeviations`, `cashNeedPercentage`, `needAnalyticsStatus`) may be derivable in
   principle and not faithfully reproducible in practice.
3. **[0.6.2_AE_PartnerETL~A] Verify propagation after 03:30Z 2026-07-23** -- monolith bronze then
   silver `fact_assets/date=2026-07-{11..15}`. Listing-based with a positive control. Do NOT fire
   the mirror to accelerate it.
4. **[0.4.0_DS_ClientPlatform] TWO fixes to your files, both "the backfill path needs what the
   daily path does not":** (a) `_hh_universe.load_household_universe()` should take an as-of date
   (default latest) so a backfill cannot silently borrow today's roster; (b) thread the per-client
   fan-out in `pull_inflection_assets_v2.py` -- measured 138 calls/s concurrent vs 0.82 sequential.
   Also one stale docstring: the header still says output/resume are `.parquet`; the code does
   `.jsonl.gz` in both places.
5. **[1.0.0_SA_CTO / 0.8.0_AE_CloudComp] `comp-assets` declared-completeness is channel/date-level
   and blind to per-feed gaps** -- both channels reported `complete: True | holes: 0 named` over
   real holes. Gate/tool candidate; also no comp-tool covers per-feed date-set differencing.
6. **[1.0.0_SA_CTO] Register `inflection` as a named pipescript thread** -- `pipescript inflection`
   FAILs today for a live 2-vendor pipeline under active repair.
7. **[0.6.2_AE_PartnerETL~A / 4.0.0_SA_CRO] Coordinate on the lookback question** -- CTO flagged
   that eclipse/inflection and CRO's Cottonwood Black Diamond question are the SAME SHAPE:
   live-state vendor, short assignment history, and whether a change-log can honestly stand in for
   a snapshot. Report once if the answers converge.
8. **[0.7.0_AE_CloudOps] WS-5 unchanged** -- apply -> blackdiamond-only artifact -> exercise; the
   exercise must assert manifest `mode == "event"`.
