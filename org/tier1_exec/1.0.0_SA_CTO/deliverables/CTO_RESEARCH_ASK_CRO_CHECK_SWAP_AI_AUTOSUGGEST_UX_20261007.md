# Research ask to 4.0.0_SA_CRO -- AI autosuggest of swaps for unrecognized securities: the check/swap operations and their UI

**From:** `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~08:0xZ. **Authority:** Andrew-direct ~08:0xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_080xZ_CRO_RESEARCH_ARM_AI_SWAP_AUTOSUGGEST_CHECK_SWAP_UX.md`
@1ea0796be2, VERBATIM: "I am more intrigued in AI functionalities for autosuggesting swaps of unrecognized securities and associated
frontend ops for that process. I will bring on 4.0.0_SA_CRO in to help assess the current check 1 swap 2 operations and how to make
them more user friendly in UI UX."

**Mode:** research and assessment only. No build, cut, deploy or vendor call. A live Kimi call needs Andrew's per-use word (CLAUDE.md).

## What exists (measured by this seat at HEAD; re-read before quoting)

| Layer | Path | Size |
|---|---|---|
| The model calls ("check" then "swap") | `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py` (model `kimi-k3`; check 16k tokens / 120 s, swap 32k / 240 s; "Swap refuses until provider QA has established actual web-search support"; "Model output remains advisory and must pass deterministic provider verification") | 225 lines |
| The broker that calls it | `intake/resolution_broker.py` | 146 |
| Deterministic verification | `intake/security_resolution.py` (`validate_symbols`, `ResolutionRefused`) | 250 |
| Turning results into suggestions | `intake/upload_suggestions.py`, `intake/upload_resolution.py` | 88 + 134 |
| Tests | `intake/tests/test_resolution_kimi.py`, `test_security_resolution.py`, `test_deferred_resolution.py`; `ycharts/generate/tests/test_resolution_retry.py` | |
| The page | portal `src/pages/InvestorReporting/tabs/analysis/InputReview.tsx` (199 lines at origin/DEV); wire contracts `contracts/wire/AnalysisUploadRequest.ts`, `AnalysisUploadResult.ts`; tests `upload-accept-suggestion.test.tsx`, `upload-review-v2-rows.test.tsx`, `iv-e-108.prospect-upload-confirm.test.tsx` | |
| History | IRPT_BCKEND `STATUS~Y.md`: Y-4 (the typo file, check gate 15.6 s), Y-5 (TIMXX named SGOV), "Y-5 packet 2 (the Kimi swap): HELD by CTO batch 218" | |
| Where it is going | IRPT_YCDGEN PRD v0.8 FWD-16 moves typo and swap verification from YCharts' data onto Opal's (surface S31) | |

## The questions, in order

1. **What the user sees today.** Walk one upload with an unrecognized symbol, a typo and a delisted fund through the page. Use
   the fixtures and tests, or `/ui-walk` on the 5174 build if one is up. For each step, give the wait, the words on the screen,
   and the choices offered. Where does a user get stuck or have to guess?
2. **What the AI does and does not do.** Check versus swap. What context the model gets. How a suggestion is verified before it is
   shown. What the user sees when the model is slow, refuses or is wrong. What Y-5 packet 2 adds that is not live today, and why
   batch 218 held it.
3. **Past patterns.** In this estate's history: earlier swap or suggestion designs, rulings and rejected options. Outside the
   estate: how comparable products present a proposed security substitution (confidence, reason, side-by-side, bulk accept,
   undo). Cite every source.
4. **Recommendations.** UI and UX changes ranked by user value against cost, and any change the backend must make to support
   them. Mark each as one of: works on today's YCharts intake; needs FWD-16's Opal data; or needs a vendor decision.

## Deliver

A brief at `docs/briefs/` (the L1 form `/brief-create` uses, so it can feed an L2 endpoint). Send the path in one line to
`1.0.0_SA_CTO~DELL2`. Questions back to this seat at any point, one per message.
