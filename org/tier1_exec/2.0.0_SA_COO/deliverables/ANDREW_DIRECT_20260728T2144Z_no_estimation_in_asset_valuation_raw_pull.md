# ANDREW-DIRECT 2026-07-28 ~2144Z -- NO INTERPOLATION OR ESTIMATION IN ASSET VALUATION. IT IS A RAW PULL.

**Recorded by:** `2.0.0_SA_COO` - **Channel:** Andrew directly at the COO terminal
**Received:** 2026-07-28T214236Z (read from `date -u`)
**Recorded + broadcast:** same turn, per `org/XXX.md`

---

## VERBATIM

> "For inflection, why would we be assessing these based on model weights as opposed to actually assessing
> off the holdings themselves? we have an entire swagger doc with all inflection endpoints, there is
> absolutely no excuse for any kind of interpolation or estimation when it comes to asset valuation; that is
> a raw pull."

**NOT A PARAPHRASE. THE PHRASING IS THE RULING.**

---

## HIS PREMISE IS CORRECT -- GROUNDED, NOT ACCEPTED

**1. INFLECTION ETF OWNERSHIP IS AN ESTIMATE.** Measured in the served platinum artifact
(`platinum/mdpf/aggregate_aua/2026-07-28.json`):
```
attribution_basis: "rps_actual:49financial ; target_weight:inflection"
```
49financial is attributed from **real Schwab-RPS holdings**; inflection from **model target weights**.

**2. WE HOLD THE ACTUAL INFLECTION POSITIONS, AND THEY ARE FRESH.**
```
s3://opal-data-assets/orion/inflection/silver/fact_positions/   newest date=2026-07-28   2,283 partitions
  (siblings: fact_assets, fact_performance, fact_transactions)
```
**T-0 fresh, 2,283 daily partitions.** DS's L1 census independently reported Orion/INF custody bronze AND
silver both at **2026-07-28 HEALTHY**. **The raw holdings exist, are current, and are already landed in the
monolith.** No vendor call is even required to stop estimating.

**3. IT WAS A DELIBERATE SCOPING DECISION, NOT AN OVERSIGHT -- and the design doc says so.**
`data/mdpf/scripts/feeders/HANDOFF_DSA_wsd2_aggregator_wire.md`:
```
:68   "WS-D.2: real Schwab-RPS held overrides the target_weight estimate"
:78   emits the basis string "rps_actual:49financial;target_weight:inflection" so the artifact discloses it
:114  "Inflection ETF stays target_weight-estimate (small: ~$8M PFOE / ~$10M PFDE; ...)"
```
**WS-D.2 gave 49financial the real-holdings override and EXPLICITLY LEFT INFLECTION ON THE ESTIMATE, on a
MATERIALITY argument.**

**4. AND THE ESTIMATE'S BIAS WAS KNOWN AND DOCUMENTED WHEN THAT CHOICE WAS MADE.**
```
:18   "model_aua x target_weight, which runs ~1-3% HIGH and OVER-ATTRIBUTES PFOE"
RUNBOOK_AE_mdpf_daily_chain.md:31  "(PFOE over-attribution via the old target_weight estimate)"
```
**A KNOWN-BIASED estimator, retained on the grounds that the exposure was small.**

**5. THE "SMALL" IS ~$58.3mm.** From today's artifact, inflection held:
`DIVZ 18,382,174.73 · IDVZ 17,367,784.99 · PFDE 14,300,934.55 · PFOE 8,215,381.40` = **$58,266,275.67**,
carried at a rate that runs 1-3% high -- **roughly $0.6mm-$1.7mm of over-attribution, every day, on a
number we could compute exactly.**

---

## WHAT THE RULING BINDS -- surfaced, NOT adjudicated

**The principle is general and is NOT scoped to inflection or to ETFs:** *no interpolation or estimation in
ASSET VALUATION -- it is a raw pull.* It reaches every place a valuation is derived from weights, ratios or
carry-forward when a holdings source exists.

>> **AND IT INVERTS THE MATERIALITY ARGUMENT THAT JUSTIFIED THE ESTIMATE.** WS-D.2 reasoned: the exposure
is small, so the estimate is acceptable. **Andrew's rule is not a materiality test -- it is a SOURCE test.
"We have the endpoints" is the whole argument; the size of the number does not enter it.** A materiality
threshold has to be re-argued every time the number moves; a source rule does not. <<

**⚠ NOT ADJUDICATED, and it is CTO's:** whether this is executed now or lands as a requirement on the
publisher/canonical rebuild. **Ruling 1 (legacy untouched, no legacy point-fixes) still stands**, and the
WS-D.2 estimator is legacy-side. **Andrew's rule and Ruling 1 are in tension exactly as the cottonwood
question was, and I am NOT resolving it a second time by attaching an implementation to his words.**

## WHAT I HAVE **NOT** ESTABLISHED

- **Whether `fact_positions` carries ticker-level detail** sufficient to attribute per-ETF. It is a
  positions table with 2,283 daily partitions, but **I have not read a row.** The whole ruling assumes it
  does; that assumption is UNVERIFIED and is the first thing to check.
- Whether the swagger surface Andrew references is already consumed by the Orion puller or is a separate,
  richer endpoint set.
- Whether any other partner/artifact carries a similar estimate. **The `attribution_basis` string is a
  disclosure mechanism -- it should be swept for every value it takes, not just this one.**

-- `2.0.0_SA_COO`, 2026-07-28T214236Z
