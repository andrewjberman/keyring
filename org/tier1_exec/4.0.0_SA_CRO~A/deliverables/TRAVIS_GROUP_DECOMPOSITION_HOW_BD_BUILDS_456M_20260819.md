# HOW BLACK DIAMOND BUILDS $456.8M FOR THE TRAVIS PENFIELD GROUP -- the full decomposition (4.0.0_SA_CRO~A, 2026-08-19)

**Commissioned:** Andrew-direct at this terminal (~1900Z): "explore the BI and Data Mining and any
endpoints at your disposal as well as our data to figure out how Black Diamond is getting to that
number for Travis." Under the standing scanning egress (recorded ~1830Z).
**Method:** one qt6 run at GROUP x ACCOUNT grain (dims Month/Portfolio Group/Account Number/Original
Account Number, measure EMV; template OPAL_CROA_Probe_GroupAcct_qt6 id 517685, run 517686 Completed,
34,280-row export) crossed against (a) the daily allocation export, (b) role-tagging columns, (c) OUR
silver fact_rps balances. Frame VERIFIED before comparing: fact_rps partitions are CONTENT-dated
(date=2026-08-18 carries business_date=2026-08-18 on all 102,797 rows) = same content date as BD's
asOfDate 08/18 -- so deltas below are REAL, not the one-day-offset class. Two instrument errors
caught in-pass: an 8-vs-10-digit join key (clean 0-of-335 was the tell; canonical is zfill(10)) and
Decimal-vs-float arithmetic (the SILVER-DTYPE class, live specimen).

## THE DECOMPOSITION (every layer sums; BD's group EMV reproduces exactly from members)

```
$456.8M  =  BD's Travis Penfield group, Aug EMV (347 member accounts, sum ties exactly)
 |
 +-- $440.7M  335 SCHWAB-shaped accounts (8-digit Original Account Number)
 |    |
 |    +-- $420.4M  276 accounts MATCHED in our fact_rps (same content date 08-18):
 |    |             our balances = $410.0M -> BD reads +$10.4M (+2.48%) REAL delta:
 |    |               - ONE account = +$6.9M of it (the outlier -- identify its holding
 |    |                 character; BD-side pricing/manual-asset candidate)
 |    |               - the tail: 223 of 276 tie within 1%; median +$1,281/account,
 |    |                 uniformly positive -- ACCRUED-INCOME-shaped (qt6 EMV likely
 |    |                 accrual-inclusive vs our settled/unsettled market value).
 |    |                 INFERRED; confirmable per-holding.
 |    |
 |    +-- $20.2M   59 accounts in BD's group but ABSENT from our 08-18 positions file:
 |    |             mostly empty/closed (median $100, 5 at exactly $0 -- a positions
 |    |             file only carries accounts WITH holdings) BUT one $5.64M outlier
 |    |             -- the open cell (candidates: other-master delivery, held-away
 |    |             asset BD carries, recently-funded custody lag).
 |
 +-- $16.1M   12 NON-Schwab-shaped members (9/7/5/3-digit ids): other-custodian or
              manual assets -- STRUCTURALLY INVISIBLE to our Schwab-only feeds.
```

## THE ATTRIBUTION LAYERS (why $373M "role-tagged" != the $456.8M book)

| layer | accounts | value |
|---|---|---|
| role-tagged to Travis anywhere (Architect/Consultant/Implementor/Local Ops/Additional, export MV basis) | 241 | $348.7M (~ his quoted $373M at its vintage) |
| IN his group but NO Travis role tag -- the house/private-wealth-bucket class he described in the meeting | 96 | **$88.7M** |
| role-tagged but NOT in his group | 2 | (residual) |
| group members missing from the allocation export entirely (its open/grouped filters) | 28 | $42.9M |
| non-Schwab members (above) | 12 | $16.1M |

**The one-sentence answer: BD gets to $456.8M by summing EMV over the group's own member list --
347 accounts assigned to "Travis Penfield" -- of which our role-tagging sees only the ~241 tagged
accounts (~$349M), missing $88.7M of in-group-untagged Schwab assets, $16.1M of non-Schwab assets,
and carrying a real +$10.4M valuation-basis gap (one outlier account + an accrual-shaped tail).**
Role-tagging is an ATTRIBUTE view; the group is the MEMBERSHIP view; BD's number is the membership
view, and it is internally consistent (member sum ties to the group total to the dollar).

## OPEN CELLS (named, not chased tonight)
1. The +$6.9M single-account delta -- identify the holding/pricing character (one drill-down).
2. The $5.64M member absent from our positions -- which master/custodian delivers it?
3. The accrual hypothesis on the +$1.3K-median tail -- one per-holding comparison confirms.
4. qt6 EMV accrual semantics -- BD doc/measure-definition read.

PII: account-level work in scratch (deleted); only aggregates + masked shapes printed/committed.
Probe templates persisted in BD (517678, 517685) -- precedent-matched, deletable on word.
