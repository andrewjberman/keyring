# ETFS / inflection: from "dedup the silver" to the Orion forward-label — and three specs falsified on the way (08-01 2300Z -> 08-03 1315Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE, COORDINATE

Continues `etfs_rebate_basis_lineage_and_producer_repoint_1330-2300Z.md` @`2b1193e7da`.
One subject throughout: **the ETFS_AVGCAP partner-rebate basis — the numbers that decide what a
partner is paid.**

## What landed

| commit | what |
|---|---|
| `10ae33b724` | **FALSIFY** my own §1 layer table — the monolith is NOT clean for inflection |
| `3c7c759386` | spec: INFLECTION_SILVER_RETRO_DEDUP (**later superseded — wrong approach**) |
| `4a66353f38` | fix: AC2/AC7 contradiction + my 92.3% figure skipped an existing partition |
| `14ff9164c0` | ci: vendored-copy parity — 4 unguarded copies of `lib/trading_calendar.py` |
| `8f0e32a642` | spec: **ETFS_ORION_LABEL_NORMALIZATION** (the correct approach) |
| `5f27b84c0f` | memorialize: the July figures + corrected CSVs |

## The arc, and it inverted twice

**1. I specced a repoint to the monolith on a layer table that said bronze/silver clean, gold
defective. `0.7.0_AE_CloudOps~E` verified it before implementing and FALSIFIED it.**

My detector dropped date columns named `('date','snapshot_date','as_of','as_of_date')` — snake_case.
The schema is **camelCase**: `asOfDate`, plus `_source_file`, `_source_as_of`. All three sat INSIDE
my hash and all three differ solely because they encode the partition date. **My "DISTINCT" was
manufactured by the columns I believed I had dropped.** Correcting the drop list did not save it —
a whole-body hash also trips on two unrelated `assetClass` reclassifications. **Both failure modes
pointed toward "clean."**

Root cause is VERIFICATION_LAW #6, which I wrote the same day: **I measured "is the FILE different"
when the question was "is the ETF VALUE different."**

**2. I then specced a retroactive DEDUP. Also wrong.** `~E` caught two defects in it before writing
code: AC2 and AC7 could not both hold (strict trading-day pairing makes 07-20 classify SUSPECT at
70.88%, not DUPLICATE), and my cited 92.3% was computed by **skipping an existing partition**
(`date=2026-07-15` exists; correct adjacent figure is 81.80%). Cause: an earlier instrument (the ETF
vector) flagged a PAIR, and I carried that pair into a different instrument without re-checking
adjacency was valid on the new axis.

**3. Then I found the actual mechanism, already SEALED in the estate 2026-07-02.**
`data/inf/scripts/silver/_orion_vendor_asof.py`: Orion returns the latest **SETTLED** close — the
prior trading day — while `asOfDate` **echoes the run date**. Offset is exactly one NYSE trading day.

**Refinement:** the docstring attributes this to a *pre-open* pull at 09:00 ET. The positions puller
now fires **09:37 ET, POST-open** (`cron(37 13)`), moved by **Andrew-direct `b2f61bed83`
(2026-07-01)** *"to avoid pulling before Orion settles prior-day close."* So the operative mechanism
is **the pull deliberately targets the prior settled close** — not pre-open timing. The docstring's
stated precondition is now STALE.

**So dedup was wrong for a second reason: it treats a LABELLING defect as a CONTENT defect.** The
07-20 partition holds real settled 07-17 data, correctly pulled, wrongly labelled. Suppressing it
would discard a genuine observation and encode the vendor's label as truth.

## The oracle — RUN AND TESTED (Andrew-direct "run the oracle and test it")

| published | → true settled | outcome |
|---|---|---|
| 07-18 **and** 07-20 | both → 07-17 | values identical → **collapse CORRECT** |
| 07-25, 07-26, 07-27 | all → 07-24 | identical → **CORRECT** |
| CONTROL 07-14 / 07-16 | → 07-13 / 07-15 | **different** → genuinely different books |

The control normalizes to different dates, so the instrument discriminates.

## THE FIGURES (memorialized `5f27b84c0f`)

Like-for-like, **22 trading-day observations per basis, zero gaps**:

| ticker | published avg | true-settled avg | delta | % |
|---|---|---|---|---|
| DIVZ | 17,213,181.28 | 17,372,480.95 | +159,299.67 | 0.925% |
| IDVZ | 13,303,299.68 | 13,425,779.03 | +122,479.35 | 0.921% |
| PFDE | 10,855,741.97 | 10,949,981.15 | +94,239.18 | 0.868% |
| PFOE | 6,236,133.97 | 6,284,178.68 | +48,044.71 | 0.770% |
| **TOTAL** | **47,608,356.91** | **48,032,419.82** | **+424,062.91** | **0.891%** |

Re-labelled, the July file spans **2026-06-30 → 2026-07-30**: one **June** settled day in, true
**07-31** out (it lands in August). ⚠ **BASIS, not payment**; simple-mean assumption; AVGCAP
aggregation unconfirmed.

## ⛔ The larger defect — three partners, one file, TWO DATE BASES

Schwab and Black Diamond carry **accurate settled-date labels and must NOT be normalized**; only
Orion forward-labels. So one monthly rebate file has **inflection on T-1 while 49financial and
cottonwood are on T** — **not comparable in the artifact that decides what each is paid.** This is
the defect to fix regardless of any restatement decision.

## Residual normalization does NOT explain

`true 2026-07-13 (Mon)` and `true 2026-07-15 (Wed)` share an IDENTICAL ETF vector to the cent
(17,221,032.09 / 13,502,102.90 / 11,079,105.25 / 6,300,737.41). Two different settled trading days.
**Andrew-direct: "holdings should be a raw fact."** OPEN.

## Collateral finding: the ONE frontier definition had FIVE copies

`lib/trading_calendar.py` + **4 unguarded vendored byte-copies** — `inf-etf-ownership-daily`,
`bd-served-vintage-alarm`, `opal-assets-absence-check`, `schwab-bronze-freshness`. All identical
today; **none had a parity check.** **THREE OF THE FOUR ARE FRESHNESS INSTRUMENTS** — a drifted copy
makes a staleness checker read a market holiday as a trading day and report a HEALTHY pipeline STALE:
the NEVER#1 false-outage class. Header says refresh before 2028.

Also reproduced: with `pandas_market_calendars` absent (**the default — none of the four ships a
`requirements.txt`**), `is_trading_day()` has **no coverage guard** and returns TRUE for every
holiday outside 2024-2027, including **2028**. Caught before drift; parity CI landed `14ff9164c0`.
⚠ **My first probe of this PASSED and proved nothing** — my environment HAS pmc; I had to force
`_USE_PMC=False` to exercise the failing path.

## Seats — who worked what (see the companion BRIEF for the full roster)

| serial | thread |
|---|---|
| `0.7.0_AE_CloudOps~E` | inflection producer + repoint + dedup + parity CI + correction email |
| `0.7.0_AE_CloudOps~C` | rollback CDN invalidation fix + the 7/27 portal repair |
| `0.7.0_AE_CloudOps` (base) | Aug-1 ETFS month-end fire watch |
| `0.0.0_AB_MSTR` | spawns, integration, INF-canon cluster ownership |
| `1.0.0_SA_CTO` (me) | specs, arch-gates, validation, the oracle |

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-grep` | PASS | located `_orion_vendor_asof`, the 4 vendored copies, the puller sources |
| `comp-estate data-refresh` / `etf-reports` | PASS | gave the per-firm producer split |
| `comp-routes behaviors` | PASS | api/public=0 vs api/general=6 — the control behind the CDN finding |
| `lib/trading_calendar.py` | **PARTIAL — defect found** | no out-of-window guard; silent wrong answers pre-2024 / post-2027 on the fallback path |
| `_orion_vendor_asof.orion_normalize_as_of` | PASS | **the oracle**; discriminating control held |
| `comp-aws <fn>` | FAIL (my error) | takes subcommands, not a function name |
| `/registry-check -all`, `/to-check` | PASS | 98 projects (23 hot), 30 active TOs, 0 malformed, 0 parse errors |

**Gap found:** `lib/trading_calendar.py` degrades silently in two ways — no signal when pmc is
absent, and no coverage guard outside the fallback window. Both fail toward "market open."

## Current State

- **Nothing deployed on inflection.** `inf-etf-ownership-daily` still reads
  `opal-data-inf/gold/canonical/holdings_`; repoint code never committed/built/applied
  (`~E` verified env vars + CodeSha256 unchanged). `meta/dedup/` EMPTY — dry-runs only.
- **CLOSED + verified:** rollback CDN invalidation (`~C`); portal serving the 7/27 vintage
  (etag `a8cb00d8…`/19221, Andrew visually confirmed); inflection scheduled floor + catch-up (`~E`,
  0 trading-day gaps remain); 49F + cottonwood repointed to `opal-data-assets` (cottonwood 07-20
  corrected 48,391,202.69 → 50,292,778.58).
- **Email SENT + DELIVERED** to andrew@opalinvest.com from noreply@opalinvest.dev — SES `Send=1`,
  `Delivery=1`, 0 bounce/reject, 3 attachments. Moratorium-exempt on Andrew's explicit ask.
- **SUPERSEDED, do not implement:** `INFLECTION_SILVER_RETRO_DEDUP.md` @`4a66353f38`.
- **AWAITING ANDREW:** build `ETFS_ORION_LABEL_NORMALIZATION.md` @`8f0e32a642`? restate any partner
  figure? fix the cross-partner date-basis inconsistency?

## Next Steps

- [ANDREW] the three decisions above. Nothing proceeds on the rebate basis without them.
- [`1.0.0_SA_CTO`] confirm the real ETFS_AVGCAP aggregation before any dollar figure reaches a partner.
- [`0.0.0_AB_MSTR`] cot-pipeline has ~3d of committed-but-never-applied Terraform (07-29, Andrew-direct);
  routed, surfacing to Andrew.
- [`0.7.0_AE_CloudOps~E`] STOOD DOWN. Do not start the normalization spec.
- **OPEN, unowned:** the true-07-13/07-15 residual; the `dev@test.com` attribution gap on the
  data-refresh handler (any direct invoker can self-assert an arbitrary identity string).

## The line worth carrying

**Three specs of mine were falsified in one arc, and every one was caught by the implementing seat
verifying a premise I handed them rather than building against it.** The instrument that lied
loudest was my own, and it lied toward the comfortable answer both times it failed.
