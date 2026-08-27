# ANDREW-DIRECT 2026-08-26 ~17:56Z — the "Opal" name-scan is NOT ENOUGH: build a comparable constituent-level discovery mechanism for SMAs and Opal ETFs, variant-tolerant

**Channel:** Andrew, live at the `1.0.0_SA_CTO` terminal, immediately after his DIVZ-SMA bucketing
ruling (~17:45Z) — the incident that exposed the gap: the partner was SUPPOSED to label every Opal
model/SMA and did not reliably, so the DIVZ SMA sleeve read as "non-Opal" to the blend-based scan.

## VERBATIM

> Yeah this means whatever system we have for scanning for "Opal" clearly is not enough for these
> guys, who were SUPPOSED to label every opal model/sma/etc in their accounts. I think we need to
> create a comparable mechanism that scans for SMAs as well, like any constituent-level name
> including "DIVZ" "DIVZ SMA" for DIVZ SMA, maybe "Tax SMA" and "Tax" disambiguated as a
> single-word name,  "Opal Tax SMA" would be potential too, as we do not know how these fuckers
> name these things. Same for "Muni" "Muni SMA" "Opal Muni" "Opal Muni SMA". same for really any
> opal ETF, and associated conjunctions, the etfs including PFOE PFDE IDVZ DIVZ.

## The directive, structured (recorder's rendering; the phrasing above is the ruling)

1. **A discovery mechanism COMPARABLE to the Opal-model name scan, aimed at SMAs and Opal ETFs, at
   CONSTITUENT level** (position/sleeve names inside accounts), because partner labeling is
   unreliable by measurement ("we do not know how these fuckers name these things").
2. **The token set:** strategies/ETFs **DIVZ · PFOE · PFDE · IDVZ · Tax · Muni** — with a VARIANT
   GRAMMAR per token: bare token ("DIVZ") · "<token> SMA" ("DIVZ SMA", "Tax SMA", "Muni SMA") ·
   "Opal <token>" ("Opal Muni") · "Opal <token> SMA" ("Opal Tax SMA", "Opal Muni SMA") — and the
   ETF conjunction forms for the four tickers.
3. **Disambiguation is REQUIRED for the common-noun tokens:** "Tax" and "Muni" as single-word
   NAMES, never substrings — the estate has measured the common-noun-token trap repeatedly (a
   census over "Tax" as free text counts something else). Name-field exact/token-boundary
   matching, with the estate's word-boundary census discipline.
4. **Discovery surfaces, never silently classifies:** the existing candidate-NEW-Opal WARN pattern
   (registry F5 crosswalk review) is the shape — a matched-but-unregistered name is a surfaced
   candidate for review, not an auto-classification into a served bucket (the canonical-key guard
   discipline is unchanged; today's `opal_div_sma`-not-"DIVZ" catch is the standing example of why
   the served key stays deliberate).

## VERBATIM 2 (~17:58Z — confirmation of the structured reading)

> Yeah just saw your reponse, youre exactly correct, we need to be on the lookout on a fuzzy basis
> for these things

**"On the lookout on a FUZZY basis" is the standing posture, in his words:** the mechanism matches
fuzzily to CATCH candidates (variant grammar, token-boundary tolerance), then surfaces them for
deliberate classification — fuzzy at DISCOVERY, exact at the served key. The two-stage split (wide
net, deliberate gate) is ratified by this confirmation.

## Immediate context it lands in

- Tonight's DIVZ fix is HAND-RULED by his word; this mechanism is the durable fix so the next
  unlabeled Opal SMA does not repeat the incident.
- An immediate SWEEP is dispatched alongside (read-only): scan the current cottonwood constituent
  names for the full token/variant set — are there MORE mislabeled Opal SMA/ETF sleeves in the book
  right now? A "Muni SMA" sitting unclassified would mis-bucket in tomorrow's artifact identically.
- Register home: COO routes per Rule 27 (likely D1-family — the taxonomy/registry owns
  classification — with D8 as the pipeline surface); the strategy_id registry
  (divz/pfoe/muni/tax confirmed; idvz/pfde = Q1 per PRD :57) is the existing anchor the mechanism
  extends.

Broadcast same-turn: `2.0.0_SA_COO` (routing/decomp), `3.0.0_SA_CVO`, `0.6.2_AE_PartnerETL~A`
(the sweep), `0.4.0_DS_ClientPlatform~T` (awareness — the fix in flight does not wait on this),
`0.0.0_AB_MSTR` (register).
