# AMGT_RESAPP -- ROUND 104 (`~R1` keys bk-1..bk-7), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~02:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 5348, `surprise-channel/adjudications/ADJUDICATION_v128.md` and `REMEDIATION_v41.md` @bebc25e482. MAY-CLOSE: 20 orders, judgment 1 of 1.
13 rows dispositioned, 4 graduated ARMED to `~R1`. The AIFILL workstream has its own analysis (`ROUND_ANALYSIS.round104.AIFILL.md`).

## 1. Graded (FWD-40, V1)

| arm | verdict | read |
|---|---|---|
| (b) the first load under 3 s | **MET** | 2,910.88 ms handler, from the log's REPORT line, one driven request (down from 20 s in round 102). The margin is thin (89 ms), so the first organic request of a trading day is read as the corroborating arm the PRD names, not as a gate |
| (c) the per-security pull census | MET (round 103) | |
| (d) the 10-name walk | EXERCISED | |
| (a) complete and clean | **NOT MET** | 2 confirmed broken values: PBR US prints "$" on BRL team-model figures; BATS LN shows an empty "Period 4" column. The Key Figures dashes still carry no reason. Round 103's defects are fixed (USD/"$", header dashes, forward P/E on 9 names; header live on PROD 7d5cb34d) |

**FWD-40 is one arm from REALIZED.**

## 2. ENRICHMENT LIST (round 105 for `~R1`, ONE issuance), then FWD-40 grades

1. **The currency symbol follows the figure's own currency.** "$" prints ONLY for USD. A BRL figure prints its code (or "R$" if the page already maps it), from the served currency
   field, never a default. This is a page fix that reuses the round-104 formatter; its arm is PBR US.
2. **BATS LN's empty "Period 4" column:** read why the model block serves a column with no values. Either serve the period's values or drop the empty column with a stated reason;
   never an empty header.
3. **Key Figures dashes carry their reasons,** as the header tiles now do: the same component, extended.
4. **Then:** the 93 census and the 10-name walk re-run on PROD. FWD-40 (a) reads MET with 0 confirmed broken values, and FWD-40 is graded REALIZED at that L10.

Items 1 and 3 are portal changes (Security Analysis, Opal-internal) and land as one feature cut from PROD, approved by this seat. Item 2 moves a served value only if the
column is filled, and then needs its pair.

## 3. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
