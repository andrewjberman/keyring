# Architect Attribution Decision Tree — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-13
**Project:** ADVI_MVPLVL 3a
**Data Sources:** `accounts_dimension_latest.parquet`, `nna_aua_by_advisor.parquet`, `account_performance.parquet`, `silver/transactions/*.parquet`

---

## True Architect Definition

An architect qualifies if ALL of:
- Total AUA >= $5M
- Number of relationships >= 5
- Not "49F House" or "Unassigned"
- At least 1 new account opened in trailing 12 months

**Result: 19 true architects**

---

## Decision Tree

```
ACCOUNT
  |
  v
[T1] Is architect field one of the 19 true architects?
  |-- YES --> resolve to architect                         3,191 accts  $1,039M  (65.7%)
  |-- NO
      |
      v
[T2] Is implementor field one of the 19 true architects?
  |-- YES --> resolve to implementor                       1,258 accts  $  243M  (15.4%)
  |-- NO
      |
      v
[T3] Is implementor a junior paired 80%+ with a true architect?
  |   (derived from non-49FH accounts where this implementor appears)
  |-- YES --> resolve to senior architect                    801 accts  $   79M  ( 5.0%)
  |-- NO
      |
      v
[T4] Is implementor a junior paired 60-79% with a true architect?
  |-- YES --> resolve to senior architect                    482 accts  $   48M  ( 3.0%)
  |-- NO
      |
      v
[T5] Does another account in the same relationship have a resolution?
  |   (mode of resolved siblings)
  |-- YES --> inherit from relationship                    2,796 accts  $  110M  ( 6.9%)
  |-- NO
      |
      v
[T6] Does portfolio_group match a true architect name?
  |-- YES --> resolve to that architect                       61 accts  $    3M  ( 0.2%)
  |-- NO
      |
      v
[T7] Does portfolio_group match a junior mapped 80%+ to a true architect?
  |-- YES --> resolve to senior architect                     85 accts  $   11M  ( 0.7%)
  |-- NO
      |
      v
[T8] Relationship inheritance — pass 2 (after T6-T7 added new resolutions)
  |-- YES --> inherit from relationship                       95 accts  $   13M  ( 0.8%)
  |-- NO
      |
      v
[T9] Does local_relationship ops person have 60%+ of their resolved accounts
  |   under a single true architect?
  |-- YES --> resolve to that architect                      205 accts  $    4M  ( 0.3%)
  |-- NO
      |
      v
[T10] Relationship inheritance — pass 3 (after T9)
  |-- YES --> inherit from relationship                       47 accts  $    6M  ( 0.4%)
  |-- NO
      |
      v
[T11] Is consultant field (from silver transactions) a true architect?
  |-- YES --> resolve to consultant                            5 accts  $  0.6M  ( 0.0%)
  |-- NO
      |
      v
[T12] Is consultant a junior paired 80%+ with a true architect?
  |-- YES --> resolve to senior architect                     27 accts  $    4M  ( 0.2%)
  |-- NO
      |
      v
[T13] Is consultant a junior paired 60-79% with a true architect?
  |-- YES --> resolve to senior architect                     14 accts  $    1M  ( 0.1%)
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
[T16] Relationship inheritance — pass 4 (after T11-T15)
  |-- YES --> inherit from relationship                        3 accts  $  0.3M  ( 0.0%)
  |-- NO
      |
      v
[UNRESOLVED] — no deterministic signal                       335 accts  $   21M  ( 1.3%)
```

---

## Tier Summary

| Tier | Logic | Accounts | AUA | % AUA |
|------|-------|----------|-----|-------|
| T1 | Direct architect field | 3,191 | $1,039,342,240 | 65.7% |
| T2 | Implementor IS true architect | 1,258 | $243,344,448 | 15.4% |
| T3 | Implementor 80%+ junior pair | 801 | $79,217,290 | 5.0% |
| T4 | Implementor 60%+ junior pair | 482 | $47,509,732 | 3.0% |
| T5 | Relationship inherit (pass 1) | 2,796 | $109,750,029 | 6.9% |
| T6 | Portfolio group = true architect | 61 | $3,377,722 | 0.2% |
| T7 | Portfolio group = mapped junior | 85 | $10,725,570 | 0.7% |
| T8 | Relationship inherit (pass 2) | 95 | $13,263,839 | 0.8% |
| T9 | Local relationship 60%+ pairing | 205 | $4,028,652 | 0.3% |
| T10 | Relationship inherit (pass 3) | 47 | $5,551,378 | 0.4% |
| T11 | Consultant = true architect | 5 | $624,314 | 0.0% |
| T12 | Consultant 80%+ junior pair | 27 | $3,882,979 | 0.2% |
| T13 | Consultant 60%+ junior pair | 14 | $918,327 | 0.1% |
| T14 | Additional advisor = true arch | 0 | $0 | 0.0% |
| T15 | Additional advisor junior pair | 2 | $608,372 | 0.0% |
| T16 | Relationship inherit (pass 4) | 3 | $319,409 | 0.0% |
| | **RESOLVED** | **9,072** | **$1,562,464,301** | **98.69%** |
| | **UNRESOLVED** | **335** | **$20,687,831** | **1.31%** |

---

## Final Architect Listing

| # | Architect | Accounts | AUA | % of Resolved AUA |
|---|-----------|----------|-----|-------------------|
| 1 | Travis Penfield | 354 | $383,081,000 | 24.5% |
| 2 | Kyle Sims | 854 | $168,668,340 | 10.8% |
| 3 | David Farrell | 429 | $113,689,617 | 7.3% |
| 4 | Josh Henson | 3,032 | $101,688,922 | 6.5% |
| 5 | Greg Rosner | 413 | $90,001,127 | 5.8% |
| 6 | Hunter Lloyd | 318 | $87,931,545 | 5.6% |
| 7 | Dean Dillenberg | 537 | $81,948,740 | 5.2% |
| 8 | Chase Bertrand | 502 | $79,577,180 | 5.1% |
| 9 | Ted Grant | 248 | $73,728,982 | 4.7% |
| 10 | Patrick Mundlin | 379 | $68,345,785 | 4.4% |
| 11 | Brandon Lanz | 430 | $67,200,040 | 4.3% |
| 12 | Tim Rodgers | 468 | $64,268,291 | 4.1% |
| 13 | Matt Foxhall | 196 | $46,459,960 | 3.0% |
| 14 | Zach Hawkins | 183 | $42,100,440 | 2.7% |
| 15 | Grant Boren | 221 | $32,598,746 | 2.1% |
| 16 | Lincoln Rock | 171 | $20,599,953 | 1.3% |
| 17 | Michael Ihlenfeldt | 153 | $19,879,200 | 1.3% |
| 18 | Boston Prachyl | 107 | $14,870,336 | 1.0% |
| 19 | Liv Shin | 92 | $10,122,099 | 0.6% |
| | **UNRESOLVED** | **335** | **$20,687,831** | — |
| | **TOTAL** | **9,407** | **$1,583,152,132** | — |

---

## Unresolved Residual (335 accounts, $20.7M)

Dominated by:
- Neil Tjon-Hing as implementor (88 accounts) — spreads evenly across architects
- Wills Crenshaw (28), Nick Bishop (27), Caleb Borders (23), Mitch Roper (30) — all below 60% pairing threshold
- 33 accounts with no implementor at all
- 295 accounts with no consultant signal in silver

These accounts have no field in the entire transaction record that points to a single
architect with confidence. They are the true operational/custodial residual.

---

## Key Findings

1. **49F House was not a real entity** — it was a data-entry catch-all. The decision
   tree recovered $523M from 49F House accounts by tracing implementor, relationship,
   portfolio_group, local_relationship, and consultant signals back to the 19 true architects.

2. **Josh Henson's book is 4x larger than the raw data shows** — $26M direct vs $102M
   attributed. His juniors (Conner Haney, Jackson O'Brien, Joseph Bolling, Jimmy Henry)
   had thousands of accounts tagged to 49F House.

3. **Consultant and additional_advisor fields exist in silver** but are dropped by the
   gold builder (`00_build_accounts_dimension.py`). They provided marginal lift (51 accounts,
   $6.4M) but should be carried through for completeness.

4. **Olivia Shin / Liv Shin** is a confirmed typo duplicate (overlapping relationship).
   Should be normalized to "Liv Shin" in the gold layer.
