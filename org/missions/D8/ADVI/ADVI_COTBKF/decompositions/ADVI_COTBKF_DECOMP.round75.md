# ADVI_COTBKF decomposition -- ROUND 75 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T21:56Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-75 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` @cd481e59d2 (msg 5920), answering `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
Section 3 is this round's rectangle: six items, one cell each.

**Where the project stands (the analysis, sections 1 and 2).** Nothing served has moved. Round 74's return number reproduces on the
reviewer's script: equal to served on 107,316 account-days; 1,577 change (the worker's 1,575 at a coarser floor), all in 9 accounts.
33 of 270 fund series validated, 237 unreadable, 0 refuted. **A lead, treated as a lead (row D2-S127):** the large changes are trade
days: of 96 over 10 basis points, 12 purchase days all higher and 2 sale days both lower; 74 have no trade row and no cause. "The
size is not known and none is quoted." The refuting arm of the validation was never exercised. VBTLX is excluded from every count
until its cause has a name.

**Rule 24.** Domain: the six items of section 3 -> six cells. `CB-bw-6` (the list) depends on the other five; the five are
independent of one another.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED, RE-MINTED, BUILT OR FETCHED.** "Built on copies. Nothing served, no fetch beyond round 74's." Cells
   1, 2 and 5 read round 74's two local builds (`C:/dev/wk-cotbkf-83/.scratch/w129/`), which the issuer re-read with its own script at the drain (0 differing from
   served; 1,575 changed at 1e-9). No cell reads the bucket.
2. **Two floors, two counts:** 1,577 at 1e-12 (the reviewer's) and 1,575 at 1e-9 (the worker's). Each cell states both.
3. **Three cells write a rule or a closed list to a file before they look:** the purchase-day prediction (cell 1), the closed list of
   causes (cell 2), and cell 3 runs a rule already written and may not change it.
4. **No account id leaves a worker's scratch** (section 3 item 5). Cells 1, 2 and 5 work on account-days; what is committed carries
   labels `A1` to `A9` at most, and counts.
5. **The new list entry is marked a lead without a new value in the `state` field:** `state` stays `OPEN`; a key `lead: true` and the
   first words of `what` carry the marking. A new enumerated value would need its own taxonomy record; none is added.
6. **The list cell runs LAST.**
7. **Still owed by the CTO, not a cell:** the fund-basis rule as a PRD addendum, after cell 1 (it must say how a purchase is valued
   on its day); the 2022 factor's addendum.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bw-1` | the purchase-day reading, rule first: the return recomputed with the day's flow and the day's unadjusted close on every changed account-day with a trade row in a validated fund | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~132` |
| `CB-bw-2` | the 74 large changes with no trade row: a cause each from a closed list written first, or none found | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~133` |
| `CB-bw-3` | the refuting control: the validation rule, unchanged, on the adjusted column of the 33 validated funds | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~134` |
| `CB-bw-4` | VBTLX date by date until the cause has a name or is stated as not named | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~135` |
| `CB-bw-5` | the nine accounts: funds, trade days, the share of each account's served days that change; counts only | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~136` |
| `CB-bw-6` | the correction list brought current, the trade-day mechanism as its own entry marked a lead | FWD-3 | LOCAL | CB-bw-1, CB-bw-2, CB-bw-3, CB-bw-4, CB-bw-5 | `0.9.0_WK_ADVI_COTBKF~137` |

**Fan-out:** `5 of 6 chains, cap 8` now; `CB-bw-6` starts when the other five have drained. `CB-bw-3`, `CB-bw-5` and `CB-bw-6` are
DIRECT-ACT cells (LOCAL, mechanical only); the other three carry a judgment criterion and take L8 to L10.
