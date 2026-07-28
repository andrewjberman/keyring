# ANDREW-DIRECT — CANONICAL BASIS FOR NON-MODEL AUA

**Received:** 2026-07-28 ~14:27Z
**Channel:** Andrew direct, at the `0.2.0_DT_PortfolioAnalytics` terminal (he was working the MDPF P0 with me live)
**Recorded by:** `0.2.0_DT_PortfolioAnalytics`
**Scope:** NOT adjudicated by me. Surfaced per `org/XXX.md` "Andrew-direct instructions — RECORD + BROADCAST, same turn."

---

## VERBATIM

> "the answer is 0824 schwab total value minus 49F smartx model aggregation, that is canonical balance. if
> there is methodology difference in smartx new vs smartx legacy valuations, we can dive in there, but this
> is the structure."

**THE PHRASING IS THE RULING. Do not paraphrase this into a formula and then cite the paraphrase.**

---

## WHAT IT ANSWERS

This lands on the **basis question** Andrew had parked ~2 minutes earlier (verbatim, ~14:25Z: *"the question
then simply becomes how this cohort of assets is shifting 10%, between a few days, but that is an
investigation for another time"*). **It supersedes the park on the STRUCTURE question** — he is stating the
canonical definition, and explicitly leaving only the *methodology-difference* sub-question open.

**The open question it was answering:** two producers disagree by ~$20–30mm about non-model AUA across the
same dates, for 2+ weeks. Which is authoritative?

```
CANONICAL NON-MODEL BALANCE  =  0824 Schwab total value  −  49F SmartX model aggregation
```

**Andrew names ONE remaining sub-question and bounds it:** *"if there is methodology difference in smartx new
vs smartx legacy valuations, we can dive in there"* — i.e. a **SmartX new-vs-legacy VALUATION methodology**
difference is the sanctioned place to dig. **The STRUCTURE is settled; only the valuation methodology is open.**

---

## MEASURED CONTEXT AT THE TIME OF THE RULING (mine, not his)

The Global headline on deployed PROD renders **$1,924,186,044.47 → $1.92B** via
`portal/src/pages/ModelPortfolios.tsx:1168-1172`, which sums:

| leg | source artifact | value @2026-07-22 | vintage |
|---|---|---|---|
| model | `json/mdpf/global/aggregate-aua-timeseries.json` | 1,676,493,815.11 | restored 2026-07-28T13:41:05Z |
| non-model | `json/portfolios/non_model_assets.json` | 247,692,229.36 | last written 2026-07-27T15:10:07Z |

The REVAMP artifact's own internally-coherent figure is
`model_aua + non_model_aua == opal_aggregate_aua == 1,951,676,164.42` with non-model **275,182,349.31**.

**Delta between the two producers' non-model at the SAME date: 27,490,119.95.**

> ⚠ **I am NOT asserting which of these two satisfies Andrew's definition.** Neither producer has been traced
> to `0824 Schwab total value − 49F SmartX model aggregation`. **That trace is the work this ruling authorises,
> and it has not been done.** Recording the ruling and the measurement side by side is not the same as
> reconciling them.

---

## CAUTIONS THAT BIND ANY FOLLOW-UP

- **`0824` is the MODEL PORTFOLIOS master** (Andrew 2026-07-16). The standing 49F laws — ⛔ never **ADD**
  0824+0833, ⛔ never **SUBSTITUTE** one for the other — are **not** loosened by this ruling. This defines a
  SUBTRACTION *within* the 0824 basis; it says nothing about 0833.
- **`master_for()` is agent discipline, not a mechanical gate** (CTO retraction 2026-07-24) — it stops an
  UNKNOWN purpose, never a WRONG-but-known one.
- **LABEL THE BASIS.** 0824's ~$1,621.6mm is BLENDED-PREFERRED; the feeder serves SCHWAB-RPS ~$1,390mm+$23mm.
  Those are TWO QUANTITIES, not a shortfall. Any implementation of this formula must state which 0824 quantity
  it consumed.
- **A VERBATIM QUOTE WITHOUT ITS SCOPE IS A FUTURE CONTRADICTION WITH A CITATION.** Scope as captured: said in
  the context of resolving the non-model basis disagreement on the MDPF Global headline. He did **not** state
  a producer, a key, a schedule, or an owner.

---

## BROADCAST

MCP to `1.0.0_SA_CTO` + `2.0.0_SA_COO` + `0.0.0_AB_MSTR`, same turn as receipt, per XXX.md.
