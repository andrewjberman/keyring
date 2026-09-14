# POSN_ASTTAX round 5 -- NEVER#1 NEVER-WIDEN SIGN-OFF, THE COO HALF

**Seat:** `2.0.0_SA_COO~Z` (L5/L6/L7 owner). **Date:** 2026-09-14 ~18:0xZ. **The other half:** `1.0.0_SA_CTO~Z`,
`ledger/NEVER_WIDEN_ROUND5_CTO_HALF.md` beside this file (msg 22884: the CTO half covers R1 as a co-signed act).
**Authority for the acts themselves:** Andrew ~17:2xZ / ~17:3xZ (*"All recs approved"*; item F widens the 2026-09-13 deploy approval
to `yang-generate-allocation-summary` under ONE sign-off), PRD v0.7 @`99cc431075` C-BENCHMARK / C-SATELLITE-SOURCE / C-RETAG-SET,
breakdown v0.5 @`0949f2d53d` s.4 step 3b. **This sign-off is two exec seats confirming what MOVES; it is not a second
authorization and must not become one** (this seat's own 0828 half, msg 13678).

> **THE RULE THIS HALF SATISFIES, and the two clauses it is written to:** *"A SIGN-OFF NAMES THE ACT'S BLAST RADIUS, NEVER THE
> PRODUCER'S DECISION ... FIRST COUNT THE WRITERS OF THE NAMED PROPERTY: a property with N writers needs N rules read, and N is a
> number the half PRINTS."* Every figure below is MEASURED on the live plane by this seat's own instruments (s3api heads, a
> filtered DynamoDB scan, `lambda get-function-configuration`, `comp-find` over `infra data integrations`), 2026-09-14
> 17:4xZ-17:5xZ UTC, never read from a document's description of it. The CTO half re-reads the census on a different instrument.

---

## 1. WHAT MOVES -- every key, its writers, its radius, its rollback

### B1 -- the two positioning generators (AT5-s-1)

| key (bucket `opal-data-portal-v2`) | writers of THIS KEY | live state before | what the deploy changes in the served bytes | rollback |
|---|---|---|---|---|
| `json/positioning/positioning_data.json` | **1** -- `yang-generate-positioning` (`lambda_function.py:2454-2459`, `:2581`) | `LastModified 2026-09-12T11:05:33Z`, 8168 B (gzip body, 73,718 B inflated; `data_as_of 2026-09-11`; allocation keys today `cash, fixed_income, equity, hedge` on all five models), VersionId `4Q1qjgD52FSKZ38EfHGqdKGHyJ_ktlka` | **FOUR source commits ride the deploy** (`git log 69b867c4eb..HEAD -- <package dir>`, read by this seat): `7f247caae0` (S6 harden), `c34eab85dc` (S1 unknown-is-not-equity), `07c046fa63` (T1 five classes through), and **`b0e1f33471` (ETFS_INGEST TO-9-DS, 2026-08-28, ETFClassifier display-name beautification -- NOT a POSN commit; it touched the vendored `etf_classifications_dynamodb.py` and ships with this deploy)**; plus B1's own labelled-zero benchmark rows. Three change classes on the served bytes: display names, the unrecognised-security label, the labelled-zero benchmark rows for the three new classes. **THE CELL PRINTS THE `69b867c4eb`-vs-HEAD LOCAL DELTA against the SAME live input BEFORE `safe-apply`** (Branch A, mirrored from the CTO half @`af667548d1`); a delta outside those three classes -- a weight, a subtotal, a holding appearing or vanishing -- is Branch B: STOP, row, no apply | artifact bucket `opal-313476888478-lambda-artifacts` is VERSIONED (`Status: Enabled`): re-point `yang-pipeline/yang-generate-positioning.zip` to VersionId `xN0rrqJbABARS6vz9NqOS1zYfjxcIsFw` (2026-08-18T18:33:23Z, `content-sha256 PRg64EGzQtLw7/HAhyN/jNP6rd01PrcLK4wKqCHAKfQ=` == the LIVE `CodeSha256`), re-apply; the served key is itself versioned (VersionId above) |
| `json/positioning/allocation_summary.json` | **1** -- `yang-generate-allocation-summary` (`lambda_function.py:34`, `:119`) | `LastModified 2026-09-12T11:05:36Z`, 969 B, VersionId `FiY95KdKcmtt5els.v44XVZciDBtUDrw` | **ZERO source commits since its live build** (`git log --since=2026-08-04 -- <dir>` returns only `89a3cca5ed`, the build itself), so this deploy ships EXACTLY ONE change: `BENCHMARK_ALLOCATIONS` (`:46`) carrying the three new classes at a labelled zero; `aggregate_by_asset_class` (`:233`, `holding.get('asset_class','Unknown')` at `:243`) groups whatever class the upstream carries -- today four values, after R1 five. Same Branch A/B delta rule before `safe-apply` | re-point `yang-pipeline/yang-generate-allocation-summary.zip` to VersionId `XLszMw8nztf6cFmPkv069UtzZGhZJ7H_` (2026-08-04T22:12:22Z, `content-sha256 o7os25TtKP9rkS9WYzCcnIsagXfKrJ7hWuGEF7/iPfM=` == the LIVE `CodeSha256`), re-apply |

**THE PROPERTY, counted, N PRINTED: "a holding-class value on the served positioning plane" has FOUR writers.** Z-S43's floor of
three is confirmed and exceeded by one:

| # | writer | key it writes | its rule for the class value | moved by B1? |
|---|---|---|---|---|
| 1 | `yang-generate-positioning` | `json/positioning/positioning_data.json` | reads the served ETFClassifier table (`etf_classifications_dynamodb.py`, vendored by manifest); five-class normalisation at `:271-303`; unknown is NOT equity (`c34eab85dc`) | YES (re-deployed) |
| 2 | `yang-generate-allocation-summary` | `json/positioning/allocation_summary.json` | groups by the `asset_class` carried in `holdings_attribution_data.json` (`:243`); adds nothing of its own | YES (re-deployed) |
| 3 | `yang-generate-holdings-attribution` | `json/positioning/holdings_attribution_data.json` (`LastModified 2026-09-04T13:51:29Z`, 386689 B) | writes `asset_class`/`sub_asset_class` per holding from the registry (`:585-586`, `classification.get('asset_class', ...)`), Excel context as fallback (`:394`, `:410-420`); live `LastModified 2026-08-18T17:34:48Z`, source unchanged since `78ae0b583e` | **NO** -- untouched; the retag flows through it on its next scheduled fire with NO code change; it is READ by writer 2 |
| 4 | `data/etfs/scripts/gold/etf_positioning_publisher.py` | `platinum/etfs/positioning_data.json` (`:8`) -- a DIFFERENT key family, the `Z-C-S55` publisher | copies gold holding class values into a four-key book allocation (`:469-472` per PRD s.7) | **NO** -- out of POSN's write scope, IN its disclosure scope; measured ZERO candidate members at its pin, a state with an expiry (PRD s.7) |

**Both branches covered:** if the SFN regeneration after the apply produces the predicted five-class payload, the two keys move as
described; if it raises, the keys are NOT rewritten (a failed generator writes nothing -- the 2026-08-18 leg shape) and the
served bytes stay at the VersionIds above. Either branch is covered by the rollback column.

### B2 -- the satellites registry producer re-deployed + the NEW key (AT5-s-2)

| key (bucket `opal-data-cot`) | writers | live state before | change | rollback |
|---|---|---|---|---|
| `platinum/satellites/registry.json` | **1** -- `data/assets/scripts/gold/build_satellites_registry.py:230` via the `cot-satellites-registry-producer` trigger, scheduled `cron(0 7 * * ? *)` UTC | `LastModified 2026-09-14T07:00:19Z`, 2196 B, VersionId `sDM2rbJ.m2yyArr8utwAaleSJyntdVbj` | the PAYLOAD is unchanged (B2 adds a sibling key; `registry.json`'s contract `{books, as_of}` and its reader stay as they are); the FUNCTION is re-deployed so its package carries the holdings builder and the ETFClassifier read | re-point `cot-pipeline/cot-satellites-registry-producer.zip` to VersionId `qXzZE63fhPXwG2dXU86eLbTh48cFn0vQ` (2026-08-28T02:44:19Z, `content-sha256 WfuD8gLfKN2W9U3DUmk6pxfUDn3QW3tOuopTecNRCv0=`), re-apply; the served key is versioned |
| `platinum/satellites/holdings.json` | **0 today** (s3api HeadObject 404 NotFound, 2026-09-14 ~17:5xZ); **1 after** -- the same producer | absent | a NEW key: per satellite one total weight per ticker (BD, summed across sleeves; Yang never added) + `asset_class` / `sub_asset_class` from the served table + per-sleeve breakdown + coverage counts | delete-on-rollback is NOT the shape (publish-the-empty, never delete the key -- the producer's own rule); the rollback is the function re-point above, after which the key is simply no longer refreshed and its `as_of` says so |

**Grants that widen (DESIRED plane, in the `.tf`, graded by `comp-iam gaps` inside the cell):** a second pinned `s3:PutObject`
resource (`platinum/satellites/holdings.json` ONLY, never the prefix) and `dynamodb:GetItem`/`BatchGetItem` on the
`etf-classifications` table ARN. The cross-firm deny is mirrored, not widened (a gate edit is its own act).

### R1 -- THE RETAG (AT5-s-8) -- the served-output move NEVER#1 names

**Store 1, the served DynamoDB table `etf-classifications`:** 285 rows (ScannedCount, filtered scan, no LastEvaluatedKey);
**13 rows move** (12 at the ~18:0xZ signing; JEPI added at PRD v0.8, R1 AMENDMENT 2 below), each at BOTH levels where the target
differs, plus one `management_style`. **Prior values, printed so the
rollback is one script and not a memory:**

```
ticker  asset_class    sub_asset_class   management_style
DBC     hedge          Commodities       passive
GLD     hedge          Gold              passive
GSG     hedge          Commodities       passive
IAU     hedge          Gold              passive
SLV     hedge          Silver            passive
USO     hedge          Oil               passive
PDBC    equity         Commodities       active
VXX     equity         Volatility        passive
VIXY    hedge          Volatility        passive
UVXY    equity         Volatility        passive
QBER    fixed_income   Volatility        active
VNQ     equity         US Large Cap      unknown
JEPI    equity         US Large Cap      active      (added ~20:4xZ; CTO batch-get 2026-09-14T20:03:01Z; PRD v0.8 @709d7b4221)
```
Targets (C-RETAG-SET + C-SUB-ASSET): Commodities for DBC/GLD/GSG/IAU/SLV/USO/PDBC with sub Metals for GLD/IAU/SLV and their current
sub kept for DBC/GSG/USO/PDBC; Structured / Hedge for VXX/VIXY/UVXY/QBER; Alternatives / Real Estate for VNQ, `management_style`
set from `unknown`; Structured / Options Income for JEPI (management_style active, unchanged). **Radius = 13 of 285 rows (4.6%)**; `hedge` as a top-level value goes to ZERO rows (7 today, all in the set).
**Store 2, `infra/aws/lambda/v2_portal/_shared/etf_classification.py` `ETF_CLASSIFICATIONS`:** the same 13 rows; the seeder's
`merge_item()` (`seed-etf-classifications.py:72-120`) reports 0 conflicts after, so the two stores agree and a later seed changes
nothing. **Downstream, on their next scheduled fires and with NO code change:** the four property writers above and the B2
producer read the new labels; `bd-securities` (the second table, C-CUTS) is NOT written and keeps disagreeing on purpose. **Rollback:**
the 13 prior rows restored by one `update-item` script from the table above, both levels + VNQ's style; the dict reverted by one
commit. **Both branches:** a partial write (k of 13) is detectable by the same scan and reverted by the same script. **Order of
writes (matching the CTO half):** VNQ's `management_style` is set BEFORE its class write, so `C-RETAG-SAFETY`'s guard is never armed
mid-retag. **Writers of the property AFTER R1: N = 6** (the four positioning-plane writers above + the B2 producer + the B4 lambda),
each reading the same served table on its next scheduled fire. The CTO half point-read the same 12 rows by `batch-get-item` at
2026-09-14T17:53:44Z (13 of 13 with a negative-control key not returned); this half's filtered scan and that point read agree on
all 12 x 3 values -- two instruments, one table.

### R1 AMENDMENT 2026-09-14 ~20:3xZ -- the served refresh after the retag is DRIVEN, not waited on (matching the CTO half @3311955ebf)

**Why:** as cut, `TO-V8-1` left the served refresh to the producers' next scheduled fires and said the render might show pre-retag
labels until then -- a wait (Rule 27). The mechanism is driven on demand; the scheduled fire stays as the organic confirmation leg.
**NEVER#1 names the new reachable state (an off-clock producer run), and this half now covers it, line for line with the CTO half:**

- **The act, in dependency order, once each (amended ~21:1xZ on W19-S8):** (1) the three yang generators invoked DIRECTLY --
  `yang-generate-positioning`, `yang-generate-holdings-attribution`, `yang-generate-allocation-summary` -- each with the event the
  state machine passed it on the last execution that ran it (`get-execution-history`), never a hand-written event; the STATE MACHINE
  IS NEVER STARTED: it consumes its own input (`MoveToProcessed`, `CleanupUploads`), so the last input is 3 of 3 absent, and its
  write set of 28 Task states, an S3 delete and a CDN invalidation exceeds the signed keys; then `yang-invalidate-cloudfront`
  invoked with its recorded event -- the pipeline's own step, whose write set is the WHOLE CACHE (`/*`) of the two distribution ids it hardcodes (one of them,
  `E2LPCXXBLDGWXY`, exists in no distribution -- W19-S10 / Z-S103; the live one, `EVTSA9VEHNZVH`, fronts the bucket that holds the
  signed keys) and NO key -- so the render bars read the new bytes (the CTO half names the generators and the keys; this invalidation moves no key
  and is stated here so the halves describe the same act);
  (2) `cot-satellites-registry-producer` invoked directly (`{}`, the trigger passes no date); (3) `cot-satellites-characteristics-producer`
  invoked directly (`{}`), after (2) because it reads holdings.json.
- **The keys, and nothing else:** `json/positioning/positioning_data.json`, `json/positioning/allocation_summary.json`,
  `json/positioning/holdings_attribution_data.json` on `opal-data-portal-v2`; `platinum/satellites/registry.json` (content-identical
  by design -- the registry carries no labels), `platinum/satellites/holdings.json` (relabelled), `platinum/satellites/characteristics.json`
  on `opal-data-cot`. The ETF publisher (`etf_positioning_publisher.py`, `platinum/etfs/positioning_data.json`) is NOT invoked and
  stays on its own schedule, disclosed.
- **Writers of the property: N = 6, UNCHANGED** -- the off-clock run is the same six writers' own code on the same inputs; no new
  writer, no new key, no code change. The state machine's other steps (manifest, cleanup, capture-output-versions) do NOT run --
  only the generators and the invalidation, which are the fire's own steps on the same inputs.
- **Expected outcome, both branches.** **A:** every invocation returns success; each key's `generated`/`as_of` stamp and S3
  LastModified move past the retag time; `registry.json`'s body is byte-identical to its prior version; the per-ticker per-level
  target comparison reads the REFRESHED artifacts; the next scheduled fire is recorded as the organic leg, not waited on.
  **B:** any invocation fails, or a key's content differs beyond the retagged labels and the weights they regroup (a holding
  appearing or vanishing, a total moving, a non-set ticker relabelled): STOP; the 13 prior values are written back to BOTH stores by
  `r1_rollback.py`; the same invocations are re-issued so every served key returns to pre-retag labels; the row is filed.
- **Rollback per key:** the prior values table above re-written, then the same invocations; where the bucket versions the key
  (`opal-data-portal-v2` does; the VersionIds are printed by the worker before the retag), the prior object version is the
  second, independent restore.

COO half for this amendment: `2.0.0_SA_COO~Z`, GIVEN, 2026-09-14 ~20:3xZ.

### R1 AMENDMENT 2 2026-09-14 ~20:4xZ -- JEPI, the thirteenth member (matching the CTO half @d3f0c3b79c; PRD v0.8 @709d7b4221)

Andrew ~20:0xZ *"Also JEPI I would put in Structured, yes."* and ~20:2xZ *"b, Options Income"*. **Prior values** (CTO batch-get
2026-09-14T20:03:01Z, one instrument for this row; this half adopts the CTO's point read and names it as such): JEPI `equity` /
`US Large Cap` / `active`. **Target:** `structured` / `Options Income` (a NEW sub_asset_class value under Structured), `management_style`
UNCHANGED. **Radius:** 13 of 285 rows (4.6%). **Served effect:** JEPI is held by no satellite component (holdings.json, 9 satellites,
177 rows at as_of 2026-09-14) and no Yang served book, so no served Positioning figure moves on its account; the writers of the
property (N = 6) read the new row on their driven run and their next fires. **Rollback:** the same script, the JEPI row restored
to the three prior values above. **Store 2:** the JEPI dict entries at `etf_classification.py:180` and `:495`; the 'US Dividend' map
at `:633` untouched. **Both branches** as above; `C-RETAG-SAFETY`'s guard is not armed (management_style is already a real value).
COO half for this amendment: `2.0.0_SA_COO~Z`, GIVEN, 2026-09-14 ~20:4xZ.

### B4 -- the additional characteristics lambda (AT5-s-4) -- NEVER-WIDEN NON-APPLICATION, stated

`platinum/satellites/characteristics.json` has **0 writers today** (s3api HeadObject 404 NotFound) and B4 is its ONLY writer after;
no existing served output moves. NEVER#1's own non-application clause -- *"an act whose write set is a literal key list the actor
controls"* -- applies. What still binds and is NOT waived: the change-management ledger entry opened at deploy start, `safe-apply`
only, `comp-iam gaps` on the new `.tf`, the cross-firm deny mirrored, its OWN schedule (never success-of-upstream), no monitor.

### B5 -- the edge router leaf allowlist (AT5-s-9) -- NOT COVERED HERE

Pending Andrew's word (msg 22884). If adopted it gets its own pair of halves: radius = the `/api/scoped/satellites/*` path class on
distribution `EVTSA9VEHNZVH`; rollback = re-associate the previous published edge version (artifact VersionId
`N3w_OHAikHzTkuf.iIGPCXPM8_4ygJlL`, `content-sha256 qrL3PFqRnq5RUyQ4SDJvZQWDreLnl7rmNWZ25IF8cx0=`).

## 2. WHAT DOES NOT MOVE -- named, so the radius is bounded rather than implied

The portal gitlink `e85f6eb84f`; any DEV/PROD branch or promote; Yang's PKL and the Models mode's data (Andrew: *"models do not get
updated"*); `holdings_attribution_data.json`'s producer code; `bd-securities`; the Bloomberg pull's `FUNDS` list; the Attribution
page; every served key outside the six named in the decomposition's (iv); the ETFS publisher's `platinum/etfs/positioning_data.json`.

## 3. SIGNED -- COO HALF GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACTS      B1 (two functions, two keys, one sign-off -- Andrew item F)  B2 (one function, one existing key + one new key)
          R1 (13 of 285 rows -- 12 signed ~18:0xZ + JEPI ~20:4xZ -- two levels, one style field; the dict)
DELTA     NOT 0 -- moving the labels and carrying five classes IS the purpose
N         positioning-plane class property: 4 writers, 4 rules read above (2 re-deployed, 2 untouched)
          registry.json: 1 writer;  holdings.json: 0 -> 1;  characteristics.json: 0 -> 1 (non-application)
COO half  2.0.0_SA_COO~Z, GIVEN. SIGNED 2026-09-14 ~18:0xZ.
CTO half  1.0.0_SA_CTO~Z -- ledger/NEVER_WIDEN_ROUND5_CTO_HALF.md (being written against this write set, msg 22884)
```
Every order for B1, B2 and R1 cites BOTH halves by path and commit; a worker reaching a deploy leg without both citations REFUSES
the leg and files a row (the refusal clause).

-- `2.0.0_SA_COO~Z`
