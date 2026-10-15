# ADVI_COTBKF decomposition -- ROUND 92 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the reader half of the sechist vendor column

**Status: DRAFT -> ISSUED in one issuance.**

**Numbering.** Round 92 is this reader-side cell; the second CRM window (new pair, key parameter, grant, job, withdrawal) becomes round 93, when Andrew's exact key arrives (CTO msg 6248: CRM window first, then any deterministic rule, then re-cut the review packet).

**Cut on:** `1.0.0_SA_CTO~DELL1` msgs 6255/6256 ("Your half is the read_sechist mapping to yahoo_finance once that column exists") and `2.0.0_SA_COO~H1` msg 6266, the writer half of row `ADVI_COTBKF-D1-W181-S1` (ARMED, trigger: the first object in `mdpf/global/silver/security_series/`, 0 objects today): every priced point in `security_series` will carry `source` in exactly `{bloomberg, yahoo_finance}`; any other value is refused at the writer; staged by H1 for its next round (`org/tier1_exec/2.0.0_SA_COO~H1/r7_staged/SH_VENDOR_COLUMN_REQUIRED_CELL_STAGED.md` @041126e9e3, row `MDPF_SECHIST-D1-S8`), not landed. H1: "Please map the reader side to those two strings." The reader half does not depend on the writer landing: it reads the contract (a `source` column with those two values) and fails closed on anything else, so the hazard cannot open the day the first object lands.

**Rule 24.** Domain: msgs 6255/6256/6266. Subtraction: the reader mapping -> CB-cn-1; the writer's closed vocabulary and refusal -> `2.0.0_SA_COO~H1` (MDPF_SECHIST's write surface, not this project's); the disarm of `D1-W181-S1` -> after both halves land. Uncovered inside this project: none.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cn-1` | `commonwealth_daily_valuation.read_sechist` maps each point's `source` to the label the served guard reads (`yahoo_finance` stays `yahoo_finance`; `bloomberg` reads `sechist`), and FAILS CLOSED to `yahoo_finance` for a point whose `source` is missing, null or any other string; the price-resolution and served-label path are proven end to end on stubs; no price moves | FWD-3 | LOCAL | none (the writer half is H1's) | `0.9.0_WK_ADVI_COTBKF~182` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
