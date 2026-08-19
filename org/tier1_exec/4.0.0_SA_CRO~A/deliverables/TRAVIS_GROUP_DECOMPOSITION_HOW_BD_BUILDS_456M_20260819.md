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

---

## CLOSURE ADDENDUM (2026-08-19 ~1930Z, Andrew-direct: "go through these still open items one at a time") -- ALL FOUR CELLS CLOSED

### CELL 1 -- the +$6.9M outlier: CLOSED. It was CASH, and it corrects this document's own +2.48% claim.
Account ...8541: every SECURITY position ties to the penny between BD and our positions file; the
entire delta is ONE line -- **CASH $6,924.6K** (BD carries free cash as a position; fact_rps is a
securities file and carries ~none: 1 cash-like row in 102,797). One BD internal account, valued
identically across its 4 groups -- no multi-mapping. **The corrected tie, on the RIGHT basis (our
canonical valuation law `V(t) = dim_balance.net_mv_plus_cash`): 309 of 312 matched Travis members
tie within 0.1%; net +$146K on $420M (+0.03%); the outlier ties to $0.0K exactly.** The earlier
"+$10.4M REAL (+2.48%)" was TRUE OF THE POSITIONS TABLE and WRONG AS A BD-VS-US CLAIM -- an
instrument-domain error by this author, caught by continuing the drill-down. BD firm-wide CASH:
$35.2M across 7,201 accounts.

### CELL 2 -- the $5.64M absent member: CLOSED. It is a National Christian Foundation account (donor-advised fund), and the 23-account missing set is the HELD-AWAY class.
Custodian dimension (id 31561), read live per account: the 23 both-master-missing accounts =
Brighthouse annuities 6/$8.69M · **NCF (the $5.64M)** · Lincoln annuity 1/$3.70M · Merrill 401(k)
3/$1.09M · **Fidelity 8/$0.99M** (Mike's "recently added") · Citi 1/~$0 · Charles Schwab 3/$0.07M
(trivial strays -- new/empty, outside both masters). With the 12 non-8-digit members ($16.1M, same
class): **~$36.3M of the Travis book is held-away/other-custody -- structurally invisible to any
Schwab-only pipeline, by construction.**

### CELL 3 -- the accrual tail: CLOSED, in corrected form.
The earlier "+$1,281 median accrual-shaped tail" was CASH (it vanishes on the nmpc basis). The TRUE
accrual effect is real but surgical: on income-bearing accounts, **BD EMV minus our nmpc equals the
accrued interest to the penny, every account tested** (e.g. ...2917: EMV 814.60K, nmpc 792.13K,
Accrual 22.47K -- delta == accrual exactly). Firm-wide magnitude TODAY: **$88.0K across 155
positions** (equity-heavy book; DEBT rows: 157 firm-wide). **C5 rider specimen for CVO/CTO
(selection made, per the pre-registration ask): account ...2917** -- largest accrual, clean
single-effect separation.

### CELL 4 -- qt6 EMV semantics: CLOSED, mechanically (stronger than a doc read).
**qt1's identity `Market Value == Unaccrued Market Value + Accrual` holds on 100.0% of 120,215
rows (max residual $0.00), and qt6 EMV == qt1 Market Value on every accrual-bearing account
tested.** Therefore: **qt6 EMV = accrual-inclusive market value, cash-inclusive** (= securities MV
+ free cash + accrued income). Correspondingly: **Schwab's `net_mv_plus_cash` = cash-inclusive,
accrual-EXCLUSIVE** -- measured, not documented.

### THE ESTATE CONSEQUENCE (one line for B_02)
b00's `accrued_income = 0.0, ACCRUAL_STATUS = PENDING-RULING` means our canonical fair_value sits on
the accrual-EXCLUSIVE basis today; the accrued figure exists in BD's qt1 Accrual measure but NOT in
Schwab's dim_balance -- when Andrew+CTO rule B_02, the source question is now measured ($88K
magnitude today; BD-derivable per account; Schwab-side source TBD). The pre-registered parity band
(C5/A1) gets its signature: BD-vs-canonical on income accounts = +accrual exactly.
