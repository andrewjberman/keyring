# GLD and VXX on the Positioning page -- what is already there, and the one-field landmine in the way

**Author:** 0.4.0_DT_ClientPlatform · **Date:** 2026-09-11 · **Requested by:** Andrew, direct
**Question asked:** what feeds Model Portfolios and the Positioning dashboard; do we technically have
GLD and VXX in there; can we fold them into the Satellites toggle with correct weights and
characteristics by adding them to the ETFS-toggle Bloomberg pull.

---

## CONCLUSION FIRST

**1. VXX is already in, and it is already folded into the Satellites toggle with correct weights and
full characteristics. There is nothing to build.** It sits in Long Term (LT) at 1.5% and Ultra-Long
Term (ULT) at 2.0%, carries `sub_asset_class: "Volatility"`, and therefore already flows through the
blend into Opal Satellite 70, 80, 90 and 98.

**2. GLD is not in -- and the reason is an allocation decision, not an engineering gap.** Every piece
of plumbing GLD needs already exists and is already correct, including its classification registry
row (`asset_class: hedge`, `sub_asset_class: Gold`, name "SPDR Gold Shares"). The only thing missing
is that GLD is not in Yang's model holdings. **Nothing in the portal or the Lambda is the blocker.**

**3. The premise of the plan does not hold, and following it would put both assets on the wrong
surface.** The Satellites toggle does not read the Bloomberg ETF pull at all. It reads the MODELS
payload and blends model books. Adding GLD/VXX to the ETFS pull would make them ETF *books* sitting
beside DIVZ/IDVZ/PFDE/PFOE -- it would not place a gram of gold inside a satellite.

**4. There IS a low-impact subtle solution, and it is ONE DYNAMODB FIELD plus a decision from Yang.**
But it must be done in that order, because of (5).

**5. ⛔ A LANDMINE SITS EXACTLY WHERE THIS CHANGE WOULD LAND. Adding GLD to the models TODAY crashes
the positioning generator with a `KeyError`, blanking the page for all four partner firms.** GLD's
registry row says `management_style: "unknown"`, and the code's default-to-passive guard **cannot
fire on it** because `"unknown"` is a non-empty string. Measured: 187 of 285 registry rows carry this
value; 0 of the 30 currently-held tickers do, which is the only reason the page works today. GLD,
IAU, SLV, USO, DBC and GSG are all in the unsafe set -- **every commodity and hedge instrument is.**

---

## HOW IT ACTUALLY WORKS -- three surfaces, not one

The Positioning page has three toggles, and they are fed by **three different data paths**. This is
the core thing the plan conflates.

| Toggle | Adapter FILE | What feeds it | Are GLD/VXX reachable here? |
|---|---|---|---|
| **Models** | (native shape) | `positioning_data.json` from Yang's PKL via the `yang-generate-positioning` Lambda | **YES -- this is the only door** |
| **ETFs** | `portal/src/pages/Positioning/shared/etfAdapter.ts` | AE's separate ETF contract artifact -- the 4 Opal ETFs (DIVZ, IDVZ, PFDE, PFOE) + the Bloomberg daily pull | No -- these are Opal's own funds |
| **Satellites** | `portal/src/pages/Positioning/shared/satelliteAdapter.ts` | **synthesised client-side from the MODELS payload** + a membership registry | Only by way of Models |

**The satellites path touches no Bloomberg pull and no ETF artifact.** From
`satelliteAdapter.ts:1-30`: *"synthesise the `satellites` payload from the ALREADY-SERVED models
payload plus the declared registry"* and *"A satellite IS the existing blend arithmetic with measured
weights."*

And a satellite's constituents are **constrained to model books by validation.**
`portal/src/pages/Positioning/shared/satelliteSet.ts` `validateSatellite()` raises `UNKNOWN_BOOK` for
any constituent not in `MODEL_BOOKS`, and the adapter **drops that whole satellite** rather than
render it. So GLD can never be named directly as a satellite leg. It has to arrive as a HOLDING
inside UST/ST/INT/LT/ULT, and then the blend carries it automatically.

### Why VXX is already done

Live satellite membership, read from `s3://opal-data-cot/platinum/satellites/registry.json`
(`as_of: 2026-09-11`, 9 books):

```
Opal Satellite 70   [LT:50.0,  INT:50.0]   -> carries VXX at 0.75%
Opal Satellite 80   [LT:100.0]             -> carries VXX at 1.50%
Opal Satellite 90   [ULT:100.0]            -> carries VXX at 2.00%
Opal Satellite 98   [ULT:100.0]            -> carries VXX at 2.00%
```

The weights are the blend arithmetic already running in production. **Your ask for VXX is complete
and has been for some time.**

---

## EVIDENCE

### Do we technically have them? Measured on the SERVED artifact

Source: `s3://opal-data-portal-v2/json/positioning/positioning_data.json`
(`data_as_of: 2026-09-09`, `generated_at: 2026-09-10T11:07:41Z`, gzip-encoded).

```
DENOMINATOR: 30 distinct tickers across all 5 model books

  VXX   present = TRUE    (LT 1.5%, ULT 2.0%, AGG rollup 0.99%)
  GLD   present = FALSE
  IAU   present = FALSE   <- no gold proxy either
  GLDM  present = FALSE
  SGOL  present = FALSE
  VIXY / UVXY  present = FALSE
```

So the answer to "do we technically have GLD and VXX in there" is **VXX yes, GLD no, and no gold
substitute is standing in for it.**

### VXX's characteristics are complete -- this is the template GLD would follow

From `current_holdings.LT`, verbatim:

```
ticker          = 'VXX'
name            = 'iPath Series B S&P 500 VIX Short-Term Futures ETN'
asset_class     = 'Equity'
sub_asset_class = 'Volatility'          <- the category ALREADY EXISTS
weight          = 0.015
fee             = 0.89
aum             = 525.90694259          (millions)
yield           = None                  <- correct; a VIX-futures ETN has no yield
duration        = None                  <- correct
credit          = None
beta            = 0.9967971388223164
active          = 0
returns         = {1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y}   all 8 windows populated
```

The shape carries 13 fields on all 110 rows served. **Null yield and null duration are not a defect
here -- they are the honest answer for a non-income instrument, and the page already renders them.**
That matters for GLD, which likewise has no yield and no duration. **The positioning shape already
accommodates an asset like this. That question is settled, not open.**

### The classification registry already knows GLD

The metadata source of truth is a **DynamoDB TABLE**, `etf-classifications`
(`infra/aws/terraform/yang-pipeline/etf-classifications.tf`), read through
`ETFClassifier.get_classification()`. The inline `ETF_SUB_ASSET_CLASS_MAPPING`-style dicts were
deleted 2026-08-18 on your centralisation direction. **This is why the fix is a data row, not a
deploy.**

Live `get-item` on that table:

```
GLD   asset_class='hedge'   sub_asset_class='Gold'        name='SPDR Gold Shares'   management_style='unknown'
VXX   asset_class='equity'  sub_asset_class='Volatility'  name='iPath Series B...'  management_style='passive'
```

And `hedge` is **already one of the four allocation buckets** the Positioning shape carries
(`allocation: {cash, fixed_income, equity, hedge}`), with the Lambda already summing into it:

```python
# yang-generate-positioning/lambda_function.py:368-369
elif asset_class == 'hedge':
    hedge += weight
```

**So a gold sleeve would land in the `hedge` row correctly, with no code change.**

---

## ⛔ THE LANDMINE -- read this before anyone touches the models

`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`:

```python
:228   management_allocations = {'active': 0, 'passive': 0}     # only two keys exist
...
:242   management_style = classify_management_style(ticker)
:243   management_allocations[management_style] += weight * 100  # <-- KeyError on anything else
```

and the guard that is supposed to protect it:

```python
:81    return registry_field(ticker, 'management_style', 'passive')  # "Default to passive if unknown"
:72    return value if value else default      # <-- 'unknown' is a NON-EMPTY STRING, so it is TRUTHY
```

**The comment says "default to passive if unknown" and the code cannot do that for the literal string
`"unknown"`.** The default only fires on a null or empty value. So `classify_management_style('GLD')`
returns `"unknown"`, and line 243 does `management_allocations["unknown"] += ...` -> **`KeyError`**,
inside `calculate_allocations()`, which is called unconditionally at `:1917` and `:1926` for every
model book. The generator dies; `positioning_data.json` is not rewritten.

### Blast radius, with denominators

```
registry rows scanned                                     285
  management_style = 'unknown'  (TRUTHY -> trips KeyError) 187
  management_style = 'passive'                              76
  management_style = 'active'                               20
  management_style = NULL       (falsy -> default FIRES, SAFE)  2   [CASH_USD, XLU]

currently-held tickers                                     30
  INTERSECTION of held AND 'unknown'                         0   <- why it works today
```

**The hazard is ARMED AND LATENT.** It has never fired because all 30 held tickers happen to be
classified `active` or `passive`. The null rows are genuinely safe -- the falsy default catches them.
**It is specifically the truthy placeholder string that is dangerous, which is why this reads as
harmless in a code review.**

Every commodity/hedge instrument is in the unsafe set:

```
GLD trips=TRUE    IAU trips=TRUE    SLV trips=TRUE
USO trips=TRUE    DBC trips=TRUE    GSG trips=TRUE
VXX trips=FALSE  ('passive')  <- precisely why VXX works today
```

**VXX works and GLD would crash for the same single reason, and it is one field.**

---

## THE RECOMMENDED PATH -- low impact, in this order

**Step 1 (engineering, ~1 minute, reversible, no deploy).** Set GLD's `management_style` from
`"unknown"` to `"passive"` in the `etf-classifications` DynamoDB table. GLD is a passively-held
bullion trust, so this is the factually correct value, not a workaround. Do the same for IAU/SLV/
USO/DBC/GSG if a commodity sleeve is at all likely. **This is the whole "subtle solution" you were
looking for -- one field on a data row.**

**Step 2 (yours and Yang's, the actual decision).** GLD has to appear in Yang's model holdings with a
target weight, the same way VXX does. **This is an allocation call, not an engineering task, and it
is the only real work in the whole question.** Once it is in the PKL, the registry row, the `hedge`
bucket, the blend, the Satellites toggle and the characteristics table all pick it up with no code
change.

**Step 3 (durable, recommended separately).** Fix the class rather than the instance: either treat
`"unknown"` as falsy in `registry_field()`, or make `management_allocations` tolerate an unexpected
key instead of raising. **Step 1 unblocks GLD; step 3 is what stops the next 186 rows from being a
trap.** I would not ship step 2 without at least step 1, and I would not call this closed without
step 3.

**What is explicitly NOT needed:** no new Bloomberg pull, no change to the ETFS toggle, no change to
`etfAdapter.ts`, no satellite-registry edit, no portal deploy, and no new API route.

---

## UNRESOLVED -- stated rather than smoothed

1. **Where GLD's `fee` / `aum` / `beta` / `returns` come from is Yang's surface, and I have not
   verified it carries GLD.** Those five fields do NOT come from the DynamoDB registry -- they are
   read from the `etf_characteristics` DataFrame in Yang's PKL (`lambda_function.py:1327-1350`). So
   GLD must be in **both** the holdings and that characteristics frame. If it lands in holdings only,
   the row renders with nulls across fee/aum/beta and no returns series. **This is the one genuine
   open dependency and it should be put to Yang with step 2.**
2. **Geography will be blank for GLD.** `ETF_GEOGRAPHY_MAPPING` is still an inline dict (the registry
   carries no geography field, deliberately -- widening that schema is a separate taxonomy act), and
   neither GLD nor VXX is in it. Not a blocker: **VXX is already absent from it today and renders
   fine.** Gold arguably has no meaningful country anyway.
3. **`management_style: "unknown"` on 187 rows is a data-quality question I did not chase.** Many are
   single stocks (AAPL, MSFT, NVDA), where "management style" is not a meaningful property at all --
   so the right fix may be a vocabulary change rather than 187 backfills. Flagged, not solved.
4. **Beta 0.9968 for VXX looks wrong on its face** and I did not verify it. A long-VIX instrument is
   strongly NEGATIVELY correlated to the S&P 500; a beta of ~+1.00 is the value you would expect from
   a defaulted or mis-signed calculation, not a measurement of VXX. It is also suspiciously close to
   SPYM's 1.0008. **Not in scope here, but it is on a client-facing page, and if a gold sleeve gets
   the same treatment the number will be equally wrong.** Worth a separate look.

---

## SEPARATE DEFECT FOUND IN PASSING -- duplicate SPYM in INT

Not related to your question; surfaced because the census printed it.

```
INT: holdings_len = 19, distinct tickers = 18, num_holdings served = 19
     DUPLICATE: SPYM appears TWICE
```

`num_holdings` is served as 19 while only 18 distinct securities are held, so the Intermediate book
**overstates its holdings count by one on the page**. It also interacts with the satellite blend:
`satelliteAdapter.ts` accumulates holdings into a `Map` keyed by ticker, so the two SPYM rows are
summed into one entry and `num_holdings` there becomes the union count (18), **disagreeing with the
19 the Models toggle shows for the same book.** Worth routing to whoever owns the PKL-to-JSON step.

---

## CITATIONS

- Served artifact: `s3://opal-data-portal-v2/json/positioning/positioning_data.json` @ `data_as_of 2026-09-09`
- Satellite membership: `s3://opal-data-cot/platinum/satellites/registry.json` @ `as_of 2026-09-11`
- Registry table: `etf-classifications` (DynamoDB, us-east-1), 285 rows scanned 2026-09-11
- Producer: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`
  (lines 72, 81, 228, 242-243, 368-369, 1327-1350, 1917, 1926)
- Satellites: `portal/src/pages/Positioning/shared/satelliteAdapter.ts`, `shared/satelliteSet.ts`
- ETFs toggle: `portal/src/pages/Positioning/shared/etfAdapter.ts`
- Table contract: `infra/aws/terraform/yang-pipeline/etf-classifications.tf`
- Bloomberg scope/limits: `integrations/bloomberg/READ_HERE.md` sections 4-5

**Method note:** every factual claim above is read from the SERVED artifact or the LIVE table, not
from the code's intent or from documentation. `portal/src/pages/Positioning/README.md` is
known-stale and says so at its own head -- it still cites a producer FILE
(`generate_positioning_json.py`) that does not exist. I did not rely on it.
