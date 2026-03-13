# Architect Attribution Decision Tree — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-13
**Project:** ADVI_MVPLVL 3a
**Data Sources:** `accounts_dimension_latest.parquet`, `nna_aua_by_advisor.parquet`, `account_performance.parquet`, `silver/transactions/*.parquet`

---

## Scope: Funded Accounts Only

`accounts_dimension_latest.parquet` contains 9,407 open accounts, but 3,984 of those
are empty shells with $0 AUA — accounts opened but never funded, or fully liquidated
but not formally closed. The portal shows 5,423 accounts because it reads from
`account_performance.parquet`, which only contains accounts with actual positions.

**This analysis is scoped to the 5,423 funded accounts ($1.583B AUA) — the portal universe.**

---

## True Architect Definition

An architect qualifies if ALL of:
- Total AUA >= $5M
- Number of relationships >= 5
- Not "49F House" or "Unassigned"
- At least 1 new account opened in trailing 12 months (activity filter)

5 entries fail the activity filter: Kyle Sweeney (4 accts), Sydney Cobb (4 accts),
Jackson O'Brien (1), Olivia Shin (1, typo of Liv Shin), Trenton Milner (1). Their
accounts are reclassified through the tree.

**Result: 19 true architects**

---

## Decision Tree

```
FUNDED ACCOUNT (5,423 total)
  |
  v
[T1] Is architect field one of the 19 true architects?
  |-- YES --> resolve to architect                         2,696 accts  $1,039M  (65.7%)
  |-- NO
      |
      v
[T2] Is implementor field one of the 19 true architects?
  |-- YES --> resolve to implementor                         920 accts  $  243M  (15.4%)
  |-- NO
      |
      v
[T3] Is implementor a junior paired 80%+ with a true architect?
  |   (derived from non-49FH accounts where this implementor appears)
  |-- YES --> resolve to senior architect                    564 accts  $   79M  ( 5.0%)
  |-- NO
      |
      v
[T4] Is implementor a junior paired 60-79% with a true architect?
  |-- YES --> resolve to senior architect                    425 accts  $   48M  ( 3.0%)
  |-- NO
      |
      v
[T5] Does another account in the same relationship have a resolution?
  |   (mode of resolved siblings)
  |-- YES --> inherit from relationship                      251 accts  $  105M  ( 6.6%)
  |-- NO
      |
      v
[T6] Does portfolio_group match a true architect name?
  |-- YES --> resolve to that architect                       40 accts  $    4M  ( 0.2%)
  |-- NO
      |
      v
[T7] Does portfolio_group match a junior mapped 80%+ to a true architect?
  |-- YES --> resolve to senior architect                     71 accts  $   11M  ( 0.7%)
  |-- NO
      |
      v
[T8] Relationship inheritance -- pass 2 (after T6-T7 added new resolutions)
  |-- YES --> inherit from relationship                       74 accts  $   13M  ( 0.8%)
  |-- NO
      |
      v
[T9] Does local_relationship ops person have 60%+ of their resolved accounts
  |   under a single true architect?
  |-- YES --> resolve to that architect                       38 accts  $    4M  ( 0.3%)
  |-- NO
      |
      v
[T10] Relationship inheritance -- pass 3 (after T9)
  |-- YES --> inherit from relationship                       12 accts  $    2M  ( 0.1%)
  |-- NO
      |
      v
[T11] Is consultant field (from silver transactions, trailing 12M) a true architect?
  |-- YES --> resolve to consultant                            7 accts  $    1M  ( 0.1%)
  |-- NO
      |
      v
[T12] Is consultant a junior paired 80%+ with a true architect?
  |-- YES --> resolve to senior architect                     29 accts  $    4M  ( 0.3%)
  |-- NO
      |
      v
[T13] Is consultant a junior paired 60-79% with a true architect?
  |-- YES --> resolve to senior architect                     15 accts  $    2M  ( 0.1%)
  |-- NO
      |
      v
[T14] Is additional_advisor field a true architect?
  |-- YES --> resolve to that architect                        0 accts
  |-- NO
      |
      v
[T15] Does additional_advisor map via junior pairing?
  |-- YES --> resolve to senior architect                      2 accts  $  0.6M  ( 0.0%)
  |-- NO
      |
      v
[T16] Relationship inheritance -- pass 4 (after T11-T15)
  |-- YES --> inherit from relationship                        2 accts  $  0.3M  ( 0.0%)
  |-- NO
      |
      v
[UNRESOLVED] -- no deterministic signal                      277 accts  $   27M  ( 1.7%)
```

---

## Tier Summary

| Tier | Logic | Accounts | AUA | % AUA |
|------|-------|----------|-----|-------|
| T1 | Direct architect field | 2,696 | $1,039,342,240 | 65.7% |
| T2 | Implementor IS true architect | 920 | $243,344,448 | 15.4% |
| T3 | Implementor 80%+ junior pair | 564 | $79,217,290 | 5.0% |
| T4 | Implementor 60%+ junior pair | 425 | $47,509,732 | 3.0% |
| T5 | Relationship inherit (pass 1) | 251 | $105,129,609 | 6.6% |
| T6 | Portfolio group = true architect | 40 | $3,866,572 | 0.2% |
| T7 | Portfolio group = mapped junior | 71 | $10,799,046 | 0.7% |
| T8 | Relationship inherit (pass 2) | 74 | $13,153,508 | 0.8% |
| T9 | Local relationship 60%+ pairing | 38 | $4,037,293 | 0.3% |
| T10 | Relationship inherit (pass 3) | 12 | $1,837,238 | 0.1% |
| T11 | Consultant = true architect | 7 | $881,102 | 0.1% |
| T12 | Consultant 80%+ junior pair | 29 | $4,048,956 | 0.3% |
| T13 | Consultant 60%+ junior pair | 15 | $1,644,780 | 0.1% |
| T14 | Additional advisor = true arch | 0 | $0 | 0.0% |
| T15 | Additional advisor junior pair | 2 | $608,372 | 0.0% |
| T16 | Relationship inherit (pass 4) | 2 | $319,409 | 0.0% |
| | **RESOLVED** | **5,146** | **$1,555,739,595** | **98.3%** |
| | **UNRESOLVED** | **277** | **$27,412,537** | **1.7%** |

---

## Final Architect Listing

| # | Architect | Accounts | AUA | % of Total AUA |
|---|-----------|----------|-----|----------------|
| 1 | Travis Penfield | 254 | $380,923,529 | 24.1% |
| 2 | Kyle Sims | 613 | $167,188,162 | 10.6% |
| 3 | David Farrell | 274 | $113,563,194 | 7.2% |
| 4 | Josh Henson | 568 | $98,701,235 | 6.2% |
| 5 | Greg Rosner | 327 | $89,770,472 | 5.7% |
| 6 | Hunter Lloyd | 187 | $87,908,567 | 5.6% |
| 7 | Dean Dillenberg | 406 | $81,570,891 | 5.2% |
| 8 | Chase Bertrand | 406 | $78,037,026 | 4.9% |
| 9 | Ted Grant | 188 | $72,268,122 | 4.6% |
| 10 | Patrick Mundlin | 294 | $68,839,404 | 4.3% |
| 11 | Brandon Lanz | 358 | $66,755,513 | 4.2% |
| 12 | Tim Rodgers | 376 | $63,914,600 | 4.0% |
| 13 | Matt Foxhall | 157 | $46,188,657 | 2.9% |
| 14 | Zach Hawkins | 155 | $42,381,699 | 2.7% |
| 15 | Grant Boren | 169 | $32,975,372 | 2.1% |
| 16 | Lincoln Rock | 122 | $20,318,695 | 1.3% |
| 17 | Michael Ihlenfeldt | 122 | $19,442,023 | 1.2% |
| 18 | Boston Prachyl | 87 | $14,870,336 | 1.0% |
| 19 | Liv Shin | 83 | $10,122,099 | 0.6% |
| -- | **Unresolved** | **277** | **$27,412,537** | **1.7%** |
| | **TOTAL** | **5,423** | **$1,583,152,132** | **100.0%** |

---

## Unresolved Residual (277 accounts, $27.4M)

Dominated by:
- Neil Tjon-Hing as implementor (58 accounts) -- spreads evenly across architects
- No implementor at all (40 accounts)
- Wills Crenshaw (25), Nick Bishop (25), Mitch Roper (25) -- all below 60% pairing threshold
- Caleb Borders (14), Trenton Milner (13) -- sub-threshold juniors
- Centralized Client Ops (11 accounts) -- institutional operations

These accounts have no field in the entire transaction record that points to a single
architect with confidence. They are the true operational/custodial residual.

---

## Key Findings

1. **49F House was not a real entity** -- it was a data-entry catch-all. The decision
   tree recovered ~$517M across 2,450 funded 49F House accounts by tracing implementor,
   relationship, portfolio_group, local_relationship, and consultant signals back to
   the 19 true architects. Only 229 funded 49F House accounts ($22M) remain unresolved.

2. **Scoping matters** -- `accounts_dimension` has 9,407 open accounts but 3,984 are
   empty shells with $0 AUA. The portal universe is 5,423 funded accounts from
   `account_performance`. All analysis must use this as the denominator to match
   what the portal displays.

3. **Josh Henson's book is 4x larger than the raw data shows** -- $26M direct (T1)
   vs $99M attributed (all tiers). His juniors (Conner Haney, Jackson O'Brien,
   Joseph Bolling, Jimmy Henry) had hundreds of accounts tagged to 49F House.

4. **Consultant and additional_advisor fields exist in silver** but are dropped by the
   gold builder (`00_build_accounts_dimension.py`). They provided marginal lift
   (54 accounts, $7.5M) but should be carried through for completeness.

5. **Olivia Shin / Liv Shin** is a confirmed typo duplicate (overlapping relationship).
   Should be normalized to "Liv Shin" in the gold layer.

6. **portfolio_group is unusable as an organizational hierarchy** -- 176 distinct
   values, 83.5% many-to-many with architect. It is an operations-assignment field
   (which support person services the account), not a team or office grouping.

7. **local_relationship** (18 values) is also operations staff, not organizational
   structure. Useful as a last-resort attribution signal (T9) but not a group-by
   dimension.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Scope to 5,423 funded accounts | Portal reads from `account_performance`; 3,984 $0-AUA shells inflate counts misleadingly |
| 19 true architects via $5M + 5 rels + 12M activity | Captures 96.7% of non-institutional AUA; excludes noise |
| Reclassify stale architects through tree | 5 stale entries (11 funded accounts) have no activity in 12M |
| Flat architect list for MVP | No clean grouping dimension exists; portfolio_group and local_relationship are ops fields |
| 16-tier deterministic tree | First-match-wins; 4 relationship inheritance passes; consultant/addl_advisor from silver as late tiers |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

Research deliverable complete. The decision tree logic is validated against the
portal universe of 5,423 funded accounts and explains 98.3% of AUA ($1.556B) across
19 true architects. The remaining 277 accounts ($27.4M) are genuine operational
residual with no deterministic attribution signal.

---

## Next Steps

1. **[1.0.0_SA_CTO] Review attribution tree** -- confirm the 19-architect list and
   tree logic for implementation in the gold layer
2. **[0.4.0_DS_ClientPlatform] If approved** -- implement the attribution logic in a
   new gold script (or extend `08_build_nna_aua_by_advisor.py`) to produce a
   `resolved_architect` column in the advisor-level views
3. **[0.4.0_DS_ClientPlatform] Add consultant + additional_advisor** to
   `00_build_accounts_dimension.py` so these fields are available in the gold layer
4. **[0.4.0_DS_ClientPlatform] Normalize Olivia Shin -> Liv Shin** in the architect
   field during gold build
5. **[0.4.0_DE_ClientPlatform] Update Advisors Tab** -- once resolved_architect is
   available, the leaderboard, Top 3, and rolling flows should read from the
   attributed view instead of raw architect field
