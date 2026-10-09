# AMGT_CORPUS -- L5 decomposition v43.0 -- ROUND 43 (the served /9 read; the stale round-40 orders closed; the completion report)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-09 ~19:5xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-42 analysis `ledger/ROUND_ANALYSIS.round42.md` @`3809669299` (msg 3103) s.2; CVO slug msg 3102
(`ADJUDICATION_v49.md` @851c212ecd). PRD v0.9, no ENDPOINT change. Round 42's decomposition kept as `AMGT_CORPUS_DECOMP.round42.md`.

## 0. What this round IS

| # | item (analysis s.2) | cell | path | risk |
|---|---|---|---|---|
| 1 | the served `/9` read: on the served page, BABA US and SHOP CN management read as `/9` composed them (sentence ends, no ellipsis, no prefix), and 8766 JP management's trailing comma reads unchanged from `/7` (row D1-W1-S3) | `CRPS-as-1` | the issuer's driven read, the tick after `2.0.0_SA_COO~R1` reports AMGT_RESAPP round-87 leg p (`dossier.py` pinned at `22cb87c9d0`); never a wait on an organic visit | SERVED (read) |
| 2 | close the stale round-40 orders `TO-READ-R40-ap10b-lv` and `TO-REPIN-R40-ap10u-lr` on their graded acts | `CRPS-ap-10` (round 40's cell, carried here for this close only) | issuer amendment IN THIS ISSUANCE COMMIT: every copy (tree order and seat-home copy) reads complete at the first status tag | -- |
| 3 | when 1 grades MET, `ledger/COMPLETION_REPORT.round43.json` for the close read | `CRPS-as-2` | the issuer's act, after as-1 | -- |

**Chains:** `as-1 -> as-2`, both issuer acts. `fanout: 0 worker chains (round 43 is issuer acts only), cap 8`.

## 1. The cells

**CRPS-as-1.** Instrument: the live route the page calls (`lib/research/api/scoped_amgt.py` `read_thesis_bundle` ->
`dossier_fields.management`, through the deployed function once leg p lands), for BABA_US_Equity, SHOP_CN_Equity and 8766_JP_Equity.
Expect: BABA US management equals the `/9` NEW line in `deliverables/2.0.0_SA_COO~C1/evidence/r42_ar2_changes_whole_20261009.txt`
(opens "Eddie Wu"); SHOP CN management equals its `/9` NEW line (ends "...like Active Merchant)."); 8766 JP management equals its `/7`
value (ends with the comma). The served object's `method_version` reads `amgt-corpus-dossier/9`. Event: R1's leg-p report (deploy hash +
function LastModified).
**CRPS-as-2.** `ledger/COMPLETION_REPORT.round43.json`, written by the issuer once as-1 is MET; the CTO reads every header FWD for the close.

## 2. Not in round 43: any code change; the RESAPP deploy itself (R1's lane).
