# CTO ROUND-110 ANALYSIS -- IRPT_DASHBD -- answering the round-109 L10 slug, and taking two P1 items routed today (2026-10-14 ~18:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_109_L9_GRADE_20261014.md` and
`ADJUDICATION_v69.md` @d6fee3fc43 (3.0.0_SA_CVO~DELL2 msg 7804): the first Inflection render, J1 FAIL on 4 counts. **No PRD addendum.**
Issuer: `2.0.0_SA_COO~D2`, ONE issuance. **Frame:** Andrew's P1, "the performance reporting tab functional for all clients at all firms",
internal Nov 15 (`ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md`).

## 1. Rulings

| item | ruling |
|---|---|
| **J1 counts 1-4** | Accepted. The remedy is the CVO's four lines: the account's own first-data date, or the not-spanned words, and never the household's figures; Ending Value filled from the member the overview prints; not-spanned words for a window the account did not span; one reason per cell, the account split notes deferring to the household line. |
| **Why the whole-document rule missed count 2** | The gain/loss "Ending Value" and the overview "Ending Value" are DIFFERENT contract members with the SAME meaning, and the rule compares member ids. **The contract gains an equivalence map** (members that name the same quantity for the same entity and window), and the rule compares through it. A planted mutant: one equivalent pair, absent on one side and printed on the other, FAILs. |
| **The issuer's ask: household returns from Orion's client grain** | YES, as ruled ~16:4xZ (D2-S34). The household return comes from Orion `fact_performance` at the client grain, with `source` claimed. Account returns stay `NO_SOURCE_YET` until the derivation's tie-out is ruled. |
| **W173-S9: the account label** | An ordinal that LOOKS like an account number ("ending 0001") is never printed. A client render prints the custodian account number's real last four characters as stored, alphanumeric allowed ("Account ending 4B7Q"), because that is what the client's own statements show. A private sample may use "Account 1" to "Account N". The row disarms on the builder change plus a test that an ordinal never renders after "ending". |
| **The shared as-of fix** (routed by the cluster lead, Andrew's ~18:3xZ defect: "as of 5 PM ET, October 14" shown at 2:37 PM) | **IRPT_DASHBD owns it.** A date-only value never shows an invented clock. `create5pmETDate` and `formatDataAsOfCompact` (`portal/src/lib/dateUtils.ts`, `portal/src/components/DataAsOf.tsx`) print "as of October 14, 2026". A clock prints only when the source supplies a real timestamp. Tests re-pin the 5 PM cases and add a negative case: a value dated today, read before 5 PM ET, shows no time. It is ONE shared helper, so every page of the 35 gets it. It is a client-facing candidate, so Andrew approves it. |
| **The Black Diamond date's meaning on Investor Reporting** (same route) | A READ: is the BD holdings file's date the close the holdings reflect, or the day it was pulled? If it is the pull day, the citation carries the holdings' own date. |
| **S37: Cottonwood's performance gold ends 2026-09-25 (12 trading days behind T-1), its channel unscheduled** | P1 cannot be met for Cottonwood without a scheduled producer (CLAUDE.md: production pipelines must be scheduled). The first step is a READ (below), then a packet. |

## 2. Round-110 cells (ONE issuance; LOCAL unless named)

1. **The Inflection render remedy** (J1 re-grade, the CVO's), with the equivalence map and its mutant, and the label rule (W173-S9).
2. **The shared as-of fix** in the portal helper, with the tests above, as one candidate branch `cand/dell2/<slug>`. The approval row is
   registered client-facing for Andrew.
3. **Two reads, LOCAL:**
   - (a) the BD date's meaning for Investor Reporting's holdings citation;
   - (b) Cottonwood's `holdings_performance_daily`: its producer, channel `blackdiamond_z09` (sources.json:159), why it has no schedule
     (DESIRED vs APPLIED), the input frontier, and what a scheduled fire needs. Also who writes Cottonwood's irpt holdings (ends
     2026-10-08). The packet for the schedule is the round after, under a pair.

Cottonwood's reporting-gold resume (silver stops 2026-06-23, ADVI_COTBKF's input) is unchanged.

-- 1.0.0_SA_CTO~DELL2
