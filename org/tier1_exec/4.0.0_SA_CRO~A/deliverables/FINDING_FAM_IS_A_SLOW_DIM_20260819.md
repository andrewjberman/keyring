# FINDING: fam is a SLOWLY-CHANGING IDENTITY DIMENSION delivered as a daily full snapshot (4.0.0_SA_CRO~A, 2026-08-19)

**Commissioned:** Andrew-direct at this terminal (~1505Z): is fam a dim or a canonical fact table;
what are the contents; hypothesis = stable identity, not transactional. **Method:** a01's
build-verified positional parse (a01_dim_relationship.py:9-22 @HEAD) + direct reads of three silver
partitions (2026-07-10 / 08-07 / 08-10, opal-data-assets schwab/08335338/silver/fact_fam/), aggregates
only, PII never printed, scratch copies deleted after measurement.

## VERDICT: the hypothesis is CONFIRMED, quantitatively

Semantically a **DIMENSION** -- the account -> advisor-firm -> rep -> holder -> household identity
registry, republished daily as a FULL SNAPSHOT. The `fact_fam` name is SILVER'S LANDING CONVENTION
ONLY (silver names every landed type fact_{type}; Rule 17 forbids silver semantic judgment). The
semantic classification happens at gold, where it already IS one: a01 consumes fact_fam as the sole
source of `dimensions/dim_relationship`, superseding the retired inferred union-find.

## CONTENTS (measured, date=2026-08-10: 7,202 rows, EXACTLY 1 row per account)

| col | meaning (a01 build-verified) | distinct |
|---|---|---|
| col_1 | master grouping id (advisor-relationship layer) | 19 |
| col_2 | master grouping / firm name | 8 |
| col_3 | rep name | 9 |
| col_4 | account number (the key; zfill(10) = account_id) | 7,202 |
| col_5 | registration / holder name | 5,084 |
| col_6 | household key (TIN-SHAPED, SENSITIVE -- grouping-only, never emitted; a01 emits a hashed account-anchor instead) | 4,246 |

## STABILITY (the number the hypothesis needed)

| horizon | identical rows | value changes on shared accounts | membership churn |
|---|---|---|---|
| consecutive publishes (08-07 -> 08-10) | **99.75%** | **0 of 7,184 on all 5 columns** | +18 / -2 accounts |
| one month (07-10 -> 08-10) | 97.86% | **2 of 7,050, col_5 only** (holder-name corrections) | +152 / -41 accounts |

Advisor/firm/rep/household assignments changed on ZERO shared accounts over a full month. The only
motion is MEMBERSHIP (new/closed accounts, ~5/business day) plus rare name corrections.

## DECISION-GRADE IMPLICATION (surfaced, not enacted -- program call above this seat)

The staleness cost of the FAM outage is UNIQUELY LOW for this file class: the 08-07 snapshot is
>=99.7% true today and its error term is almost purely "accounts opened since 08-07." The current
R-gate exists because the runners (correctly) refuse to advance vintages on a stale identity input --
a correctness DISCIPLINE cost, not a wrong-data cost. Andrew has already ruled the pattern that fits
this exact shape once (P2 INF morning floor: "ONE unified morning floor with a LABELED carry"). A
sovereign-ruled LABELED CARRY on fam (chain runs on the last-published FAM, identity plane labeled
carried-as-of-2026-08-07, new-account holes declared) would decouple the P2->P4 chain from R while
the Schwab contact proceeds. Trade stated honestly: new accounts opened after 08-07 would be absent
from advisor/household scoping until resumption (measured rate ~5/day). Whether that carry is
acceptable is HIS call, framed by CTO -- this finding supplies the measured stability numbers the
ruling would rest on.
