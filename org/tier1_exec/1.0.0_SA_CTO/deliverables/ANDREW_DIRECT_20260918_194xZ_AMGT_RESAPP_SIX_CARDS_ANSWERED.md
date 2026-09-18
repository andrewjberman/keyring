# Andrew-direct 2026-09-18 ~19:4xZ -- AMGT_RESAPP: the six round-13 cards ANSWERED

**Where:** the `1.0.0_SA_CTO~Z` terminal, answering the six-card `/open-calls` frame this seat put to him after the L10
delivery @`9c8e04cd9a` (cards from `ledger/ROUND_ANALYSIS.round13.md` s.5, re-ordered BLOCKING-first in that frame).
**Recorded by:** `1.0.0_SA_CTO~Z`, before any act on it.

## His words, VERBATIM (typos his)

> 1.) Yes use SA thats fine. 2.) Yes full egress. 3.) Yes. 4.) Agreed, yes. 5.) Base. I think the upside and downside cases
> can be discussed on methodology. 6.) Yes

## The cards as put to him, and the ruling each word makes

The numbers are the FRAME's numbers (the one he answered), not s.5's.

| # in frame | the call | the REC put to him | his word | ruling |
|---|---|---|---|---|
| 1 | Seeking Alpha as a production source for Peers (and the Model forecast fallback)? | (a) YES, per security at instantiation, recorded as lifting `C-SA-VENDOR-WORD` for these paths BY NAME; (b) read SA's terms now so a scheduled refresh can follow | "Yes use SA thats fine" | **(a) and (b) ADOPTED.** `C-SA-VENDOR-WORD` is LIFTED for exactly two paths by name: `C-PEER-SET-SA` and the `SA_FALLBACK` cells of `C-MODEL-FORECASTS`, each at instantiation and in validation. A task to read SA's terms of use runs now. **Not lifted:** a RECURRING or SCHEDULED read still waits on `C-SA-TERMS-BEFORE-SCHEDULE` (his ruling on the terms, once read); every other SA route stays under `C-SA-VENDOR-WORD` as written |
| 2 | Lusha inside the three-name validation (about 6 credits)? | YES | "Yes full egress" | **ADOPTED, and wider than the REC:** Lusha calls are authorized inside the instantiation validation (Caterpillar, CSL, Keyence) with NO credit ceiling. ⚠ This seat reads "full egress" as scoped to the call it answered -- Lusha within the validation -- and NOT as a standing grant for Lusha across the covered population; a wider reading is his to state |
| 3 | International filings battery order: EDGAR ticker -> EDGAR Bloomberg CIK -> ESEF/UKSEF by LEI -> company site -> national regulator -> UNRESOLVED | YES, company site before regulator | "Yes." | **RATIFIED** as the international battery order |
| 4 | A drafted sentence with NO verbatim span: HOLD or serve LABELLED? | HOLD | "Agreed, yes." | **HOLD.** Such a sentence is held and never served; the label interim ends. Every pass count still prints its split |
| 5 | Model Upside / Base / Downside: which formula? | base = consensus EPS x the security's own trailing-median P/E; upside/downside at fixed labelled spreads he names | "Base. I think the upside and downside cases can be discussed on methodology." | **BASE ADOPTED** (consensus EPS x trailing-median P/E). **Upside and downside stay ABSENT** with the reason "methodology to be discussed with Andrew" -- no spread is chosen by any seat |
| 6 | Retire automated sign-ins to the portal's test logins, estate-wide? | YES; correct `portal/.frontend-dev/auth/README.md`; move the two plaintext passwords out of tracked `credentials.json` | "Yes" | **ADOPTED.** Outside the AMGT_RESAPP PRD: routed to `0.0.0_AB_MSTR~Z` for placement (estate-wide, portal repo) |

## What moves

- `prd/AMGT_RESAPP_PRD.md` v0.11 -> v0.12 (both halves; neither v0.11 half had been signed): `C-PEER-SET-SA`,
  `C-FILINGS-ANALYZER` (ratified-text); `C-MODEL-FORECASTS`, `C-MODEL-WINDOW-AND-ROWS`, `C-VERBATIM-GATE`, `C-SA-VENDOR-WORD`
  table, `C-VALIDATION-NAMES` (brief).
- `ledger/ROUND_ANALYSIS.round13.md` s.5: each card marked ANSWERED with this record's pin.
- Broadcast: `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z`, `0.0.0_AB_MSTR~Z`.

-- `1.0.0_SA_CTO~Z`
