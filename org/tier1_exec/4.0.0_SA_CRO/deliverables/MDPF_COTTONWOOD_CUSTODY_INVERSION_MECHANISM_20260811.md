# The Cottonwood custody "~24h silver-precedes-bronze inversion" — mechanism, grounded

**Author:** `4.0.0_SA_CRO~A` · **2026-08-11 ~0300-0330Z** · **archetype:** DIAGNOSE
**Scope authority:** Andrew-direct @85e51be03a ("you are on the task i put in your session regarding
MDPF and cottonwood"). Discharges the open residual named in
`MDPF_REMEDIATION_PLAN_20260810.md:48` ("real ~24h silver-precedes-bronze inversion, unexplained")
and `MDPF_PIPELINE_TRUTH.json` pipelines/5 (`latency_from_bronze_min: -1439.7`).
**Method:** read-only. Source reads at `@f72495f387`; live S3 version listings + versioned GETs;
retry-net marker reads. Nothing written to any data plane, nothing deployed, nothing repaired.

---

## THE ANSWER IN ONE PARAGRAPH

**There is no causality inversion. The instrument was reading `LastModified` on a key that is now
written more than once.** Since the 4:30p-ET retime (`ce99054e44`, first new-cadence run 2026-08-06),
the custody bronze key for date **D** is written **twice or more**: once by the primary pull the
evening of D+1 (the earliest, least-settled version) and again by the retry-net and/or weekend
lag-collapse on later nights (the settled versions). The silver converter is **first-write-wins by
design** (`skipped-idempotent`), so silver for date D is stamped at the FIRST write's conversion,
while bronze `head-object` shows the LAST rewrite — silver "precedes" its bronze by ~24h. **The real
defect the artifact-clock reading was hiding: silver `fact_holdings` permanently carries the earliest
version of every date since 08-05, and every settled re-land is silently discarded.** Measured
materiality: benign on the weekday case tested (08-05 ties to the penny), **$1.10M raw-grain
Market-Value divergence on the weekend case** (08-07: silver froze on Saturday's version; Monday's
settled version differs).

The truth JSON's hypothesis fork ("either the recorded bronze prefix is not this silver's actual
source, or silver has a second unrecorded source") is **answered: neither.** Same prefix, same
source — a multi-write key read through two instruments that each see only one write.

---

## THE MECHANISM CHAIN — five parts, each grounded

### 1 · The lag flip made the primary pull land under its TRUE as-of date
`data/cot/scripts/bronze/cot_bronze_ingest.py:100 @f72495f387` — `BD_SNAPSHOT_ASOF_LAG_BDAYS`
default **0 → 1** on 2026-08-03 (CTO ruling 20260803T225311Z item 2, recorded in the source comment
`:88-99`). Snapshot tables (holdings/allocations/unrealized) now request as-of = last complete
business day and **land under that date** (`_window_for` docstring `:310-312`, "land_to_s3 keys off
end_date").

### 2 · The retime moved the pull inside the vendor's restatement window
`ce99054e44` (Andrew-direct 4:30p-ET move): session anchor → `cron(30 16)` America/New_York =
20:30Z; mirror → `cron(30 18)` = 22:30Z. First new-cadence run **2026-08-06 20:31-20:32Z** (live:
cot-home write clocks). BD's snapshot for T-1 fetched at 16:31 ET the next day is **not final** —
BD restates it on later days (measured below). The old cadence (03:30Z, D+2) pulled data that was
already settled, which is why every pre-08-05 key has exactly ONE version.

### 3 · The retry-net double-applies the lag — its self-report is wrong by one business day
`backfill_snapshot_net` re-pulls a swept day `d` via `_window_for(table, d)`
(`cot_bronze_ingest.py:1135-1136`) — but `_window_for` applies `_as_of_for`'s lag AGAIN (`:301-303`,
`:315`), so **"re-pull day d" actually pulls and lands `d − 1bd`.** The marker then reports
`relanded: [d]`.
**Live proof (retry-net marker `forwardfill_v2/_retry_net/2026-08-07.json`):** holdings
`relanded: ["2026-08-06"]` — but the write that landed at 2026-08-07T20:31:03Z (marker stamped
20:31:21Z) was **`HOLDINGS_DAILY_2026-08-05.xlsx` v2**. Same pattern on the 08-08 marker
(`relanded: ["2026-08-07"]`, actual write = 08-06's file, mirrored 08-08T22:31:06Z).

### 4 · Sweep-before-primary makes the newest sweep day structurally absent — so the phantom heal fires EVERY night
`infra/aws/terraform/cot-pipeline/ssm.tf:143` runs `--backfill-holdings-net` **before** the primary
ingest at `:165`. Under lag-1, files exist only through run−2 at sweep time, so the sweep's newest
probe day (run−1) reads `UNKNOWN-OR-ABSENT` every night (markers 08-07/08-08: exactly one swept day,
state UNKNOWN-OR-ABSENT) → guaranteed nightly re-pull → via (3), a guaranteed nightly REWRITE of
run−2's file. **This is deterministic, not conditional on any failure.**

### 5 · Weekend lag-collapse triple-writes Friday; first-write-wins silver discards all of it
`_shift_business_days` (`:281-294`): Sat/Sun/Mon runs all resolve lag-1bd to **Friday** — live:
`HOLDINGS_DAILY_2026-08-07.xlsx` has THREE versions (08-08T22:31:07, 08-09T22:31:05,
08-10T22:31:06Z mirrored). The silver converter `data/assets/scripts/silver/mirror_conversion.py`
(deployed as `opal-assets-silver-blackdiamond`) checks `partition_exists` (`:360-364`) and returns
`skipped-idempotent` (`:474`) — **first write converts, every later write is skipped.** Live: silver
`fact_holdings/date=2026-08-05` and `date=2026-08-07` each have exactly ONE version
(2026-08-06T22:31:15Z / 2026-08-08T22:31:25Z — +10s/+18s after their bronze FIRST writes).

---

## THE VERSION EVIDENCE (live `list-object-versions`, `opal-data-assets` mirror; cot-home byte-identical)

| bronze key (date D) | writes (UTC) | silver (single version) |
|---|---|---|
| 08-03 | 08-05T03:30:27 (ONE — old cadence) | coherent |
| 08-04 | 08-06T22:31:05 (ONE — first new-cadence run) | coherent |
| 08-05 | 08-06T22:31:05 (1,164,353B) · 08-07T22:31:08 (1,166,874B) | 08-06T22:31:15 ← **v1** |
| 08-06 | 08-07T22:31:08 · 08-08T22:31:06 | 08-07T22:31:28 ← **v1** |
| 08-07 | 08-08T22:31:07 · 08-09T22:31:05 · 08-10T22:31:06 | 08-08T22:31:25 ← **v1** |

The truth JSON's "inversion began between data dates 08-04 and 08-05" is exactly the first
new-cadence run: 08-04 and earlier are single-write keys.

## MATERIALITY — measured on the discarded content

Both reads use identical method on both sides (pandas sum over Sheet1). ⚠ **Raw-grain sums**: cot BD
`fact_holdings` is Relationship×Account×Asset grain (naive sums double-count for AUA) — these are
version-vs-version deltas, **not** AUA impact numbers. AUA-grain impact needs
`collapse_relationship_grain()` — DS lane, not computed here.

- **08-05 (weekday):** v1 vs v2 — Market Value **ties to the penny** ($477,112,3xx both), Units tie;
  v2 adds **39 rows, all $0 MV / 0 units** (metadata: Last Dividend, Expense Ratio drift). Benign.
- **08-07 (weekend, the served-plane case):** Saturday v1 (what silver converted) vs Monday v3
  (settled): **Market Value $481,317,939.26 → $482,421,836.47 = +$1,103,897.21**, Units +111,165.43,
  +12 rows. **The served custody plane's Friday is Saturday's snapshot; BD's settled Friday differs
  by ~$1.1M (raw-grain).**

## WHAT THIS DISSOLVES AND WHAT IT OPENS

- **DISSOLVED:** the "~24h inversion" as a causality/ordering anomaly. It is two instruments each
  seeing one write of a multi-write key. `latency_from_bronze_min: -1439.7` should be re-read as
  "bronze rewritten ~24h after silver's first-write conversion."
- **OPENED (the real defect, three separable pieces):**
  - **C-1 · composition freeze (served-data):** first-write-wins silver × multi-write bronze =
    silver frozen on the least-settled version of every date since 08-05. Weekend dates are the
    material case (~$1.1M raw-grain on 08-07).
  - **C-2 · retry-net double-lag:** re-pull of day `d` lands `d−1bd`; marker self-report wrong by
    one day. Its heal-target arithmetic and its report disagree with its writes.
  - **C-3 · structural nightly phantom heal:** sweep-before-primary + lag-1 means the newest sweep
    day is absent by construction, every night — the sweep can never converge on it and burns a
    guaranteed re-pull rewriting the wrong (prior) day.

## ADJACENCY FLAGS — surfaced, NOT asserted

- **bd-49f-runner shares this code pattern** (`infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py:61`
  `FORWARDFILL_PREFIX = "forwardfill_v2"`; `bd-49f-interim.tf:310` `BD_SNAPSHOT_ASOF_LAG_BDAYS="1"`).
  Whether the 49F/ADVI side carries the same double-lag/first-write-wins composition is
  **UNVERIFIED** — it belongs in CTO's predicate-derived consumer census (his fact 4), not solved
  twice. Routed to CTO.
- **Why BD's T-1 snapshot at 16:31 ET differs from later reads** (settle semantics at the vendor) is
  outside our instruments — completeness of a calendar day ≠ settledness of its custody data. The
  lag-1 design assumed the two are equal; the measured versions say they are not.
- The old-cadence reconstruction (03:30Z primary systematically rejected in ET-evening, sweep
  silently compensating one day late) is **PARTIALLY INFERRED** from one data point (08-03's single
  03:30:27Z version) + the `:81-97` source comments. Marked, not load-bearing for C-1/C-2/C-3.

## REMEDY DIRECTIONS — suggested owners only; nothing dispatched, nothing held

Per the CRO charter (research names suggested owners; CTO+COO staff) and my standing sync agreement
with `1.0.0_SA_CTO` (his custody-history call at Andrew is the policy neighbor of C-1): **no fix is
proposed as final here.** The shapes, for the owning lanes:

1. **C-2/C-3 (producer arithmetic, `data/cot/scripts/bronze/` = DS commit lane, AE infra):** the
   sweep should pass an AS-OF date to a window builder that does not re-apply the lag (or probe the
   key the re-pull would actually land). One function, no schedule change, no new path.
2. **C-1 (conversion policy, `data/assets/scripts/silver/`):** on a re-delivered bronze key,
   `skipped-idempotent` is the wrong policy IFF the vendor restates — but flipping to
   latest-write-wins is a **point-in-time-vs-restate policy decision on the custody plane**, i.e.
   the same axis as Andrew's 08-10 point-in-time ruling and CTO's open custody-history call.
   **Not mine to pick; syncing with CTO before any proposal lands.**
3. The e2e class (this is one instance of the scheduling jam's general form) goes in my
   implementation-strategy deliverable, separately.

**Standing NEVER-compliance:** no alarm/monitor built or proposed; the retry-net marker (the
existing visibility artifact) already carries C-2's tell (`relanded` vs actual write) once you know
to read it.
