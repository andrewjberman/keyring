# ANDREW-DIRECT 2026-10-05 ~20:4xZ -- typo check 1 and swap check 2: an AI pipeline, classified in the ETFClassifier row shape

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop), ~20:4xZ (4:4x PM Eastern), mid-turn while this seat was writing
IRPT_YCDGEN PRD v0.2, following his call-2 answer of ~20:2xZ
(`ANDREW_DIRECT_20261005_202xZ_YCDGEN_INHOUSE_ENDPOINT_THREE_CALLS_ANSWERED_CLASSIFICATION_THROUGH_CANONICAL_TABLE.md`).
**Recorded by:** `1.0.0_SA_CTO`, same turn.

## Verbatim

"This goes into the "typo" check 1 and the "swap" check 2. WE need to have an AI pipeline in place to handle typos and swaps, and
when these operations happen we need to be able to classify the given security in the ETFClassifier row shape and we need to be
able to swap to comparable securities (I recommend prioritizing ETFs for equities/bonds/commodities/etc that are already in
ETFClassifier for these swaps)."

## What it states (as written)

- The classification word of ~20:2xZ "goes into" the "typo" check 1 and the "swap" check 2.
- An AI pipeline handles typos and swaps.
- When either happens, the given security is classified "in the ETFClassifier row shape".
- A swap goes "to comparable securities". His recommendation: prioritize ETFs "for equities/bonds/commodities/etc that are
  already in ETFClassifier".

## What this seat read in the code, same turn (measured, file headers only)

- `infra/aws/lambda/investor-reporting/intake/upload_suggestions.py:1-10`: the check gate offers a likely ticker for a
  `TICKER_NOT_FOUND` row, "VERIFIED by the provider", advisory until the user accepts.
- `intake/resolution_kimi.py:1-22`: two advisory kinds, `check` and `swap`, on model `kimi-k3`; "Swap refuses until provider QA
  has established actual web-search support".
- `intake/security_resolution.py:1-22`: the deterministic verification reads YCharts' `securities_info`.
- So both checks are verified against YCharts today. An in-house path needs that verification from Opal's own data.

## What this seat does with it, and what it does not decide

- IRPT_YCDGEN PRD v0.2 gains FWD-16 and contract C-RESOLVE in his terms.
- "prioritizing ETFs ... already in ETFClassifier" is carried as his recommendation, as the first place a swap looks.
- Not stated by him: which model the AI pipeline uses, and whether "the same classifier mechanism with the AI" (his ~20:2xZ
  word) and the intake's existing advisory are one mechanism or two. The PRD names both as they exist and decides neither.

-- 1.0.0_SA_CTO
