# Never-widen sign-off packet -- the Performance adapter reads 49F from the holdings-basis gold (engine read retires)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~04:2xZ.
**Ordered by:** PRD ADDENDUM v0.19 @82e1700237 rulings 10 and 12 (the adapter switches to the gold; the engine read
retires in the same act, no fallback); CTO ruling 102520 (serves only after ~E round 2's manifest reads complete --
MET: TO-IB-er-202, 557 of 557 days, every manifest complete=True, issuer re-run PASS); Andrew-direct "yesterdays closing
weights, yes" (CTO 102548: FWD-3 gradable for 49F when this lands). **Orders:** TO-IB-pr-201/202 drained @a595a14264
(P20-1-AC1, P20-1-AC2, P20-2-AC1 PASS, issuer re-run on CLOUD). **Ledger:** `irpt-adapter-holdings-gold-49f-20260929`
(U1 and P1 closed; prep @ae20e904e6). **Applies:** only after window 21 closes (W21 pins the adapter at qfxZ0DzB).

## 1. What ships -- three surfaces, one act

| surface | change | commit |
|---|---|---|
| adapter code `qfxZ0DzB..` -> `qosuSxAf..` (S3 version ABB89j26) | `holdings_gold.py` ADDED; `retained.py` (49F fresh path calls the holdings gold; a retained non-OPAL_HOLDINGS 49F report is NOT reopened), `installed.py` (the port from the builder address), `entry.py` (HoldingsWindowNotRuled -> UNSUPPORTED_OPERATION, HoldingsGoldRefused -> OBJECT_NOT_COVERED), `PerformanceReport.schema.json` (+OPAL_HOLDINGS, CTO 102544) | a595a14264, 78eeb223f8 |
| adapter role policy (performance root) | `irpt-performance-retained-policy`: List + Get move from `gold/advi/canonical/twr_daily/` to `irpt/49financial/gold/holdings_performance_daily/` | ae20e904e6 |
| 49F bucket fence (shared-infra) | `DenyPerformanceAdapter{Reads,Listing}Outside...`: the adapter's allowed prefixes move from `twr_daily/*` + `twr_periods/*` to the holdings gold prefix; `DenyForeignFirmPrincipals` and `...AnyOtherAction` unchanged | ae20e904e6 |

Every prefix is the builder's: `address("irpt", "49financial", "gold", "holdings_performance_daily", "date=...")`,
printed; Terraform reads the firm from the registry (the naming gate passed at ENFORCE).

**Gates on the built artifact (U1):** census vs live qfxZ0DzB 69 -> 70, added holdings_gold.py ONLY, four named members
differ, nothing removed; flat census pin skew 0; ~Y zip_module_census 0 new flags (its FAIL set is a strict subset of
live's); cold start with /var/task mapped: IMPORT OK, the same named envelope as live. **Plans (P1):** performance 0/2/0
(the role policy and the Lambda's code fields only); shared-infra 0/1/0 (the bucket policy only).

## 2. Blast radius -- every branch, both readers counted

Writers of the served 49F Performance figure: **1** -- the adapter's fresh path, which also writes the retained report.
Readers of it: **2** -- the compute answer, and the retained REOPEN (irpt-requests + S3 blobs), which the page reads.
Both are read below at `retained.py` @a595a14264.

| # | request | today (qfxZ0DzB) | after |
|---|---|---|---|
| A | 49F, YTD / QTD / 1Y / Since inception, account in the gold | engine figure (twr_daily), OPAL_ENGINE; NEW-01 accounts a named refusal | the holdings chain, prod(1+r)-1 over status-OK days, OPAL_HOLDINGS; non-OK days disclosed PARTIAL |
| B | 49F, any other window (3Y, custom) | WindowNotRuled -> UNSUPPORTED_OPERATION | HoldingsWindowNotRuled -> UNSUPPORTED_OPERATION (same public code) |
| C | 49F account with no gold rows | engine unmapped -> refusal | HoldingsGoldRefused -> OBJECT_NOT_COVERED (named) |
| D | a RETAINED 49F report computed by the engine (OPAL_ENGINE), reopened | reopens (implausible ones refuse, @ae8da14d12) | NOT reopened: the fresh path answers and publishes the OPAL_HOLDINGS report as accepted for the same firm, accounts and window |
| E | a retained OPAL_HOLDINGS report | none exist | reopens as today, with no second gold read |
| F | Cottonwood (BLACK_DIAMOND) and Inflection (ORION) | unchanged | unchanged -- no member of their paths moves |

- **The page words:** portal DEV 50eb1d56 (~D 102556) names OPAL_HOLDINGS "Opal's holdings-based calculation". A page
  build without it shows no provider words for a 49F report; the figure and its dates are unaffected.
- **Latency:** the fresh path reads one gold partition per day in the window (YTD about 184, Since inception 557). The
  after-invoke below measures a real Since-inception answer against the 60 s timeout; over the timeout -> rollback.
- **The apply gap:** the performance root applies first (role policy + code), then shared-infra (the fence) in the same
  minute. Between the two, a 49F request refuses by name (AccessDenied -> DEPENDENCY_UNAVAILABLE); no figure is wrong.

## 3. Apply protocol

1. Window 21 closed (its ledger's D1/A1 closed); both halves at HEAD naming this file's blob.
2. CRO BEFORE-read on qfxZ0DzB: one 49F YTD and 1Y (NEW-01's account and a control), one retained engine report, one
   Cottonwood and one Inflection figure.
3. Fresh plans equal P1's; safe-apply performance, then shared-infra (halt gate; HALT_ACK=1 only on 0 STOP items).
4. Read back: CodeSha256 == qosuSxAf; the role policy and the bucket policy as planned; a real cold-start invoke; one
   real 49F Since-inception answer (provider OPAL_HOLDINGS, wall time printed); re-plan both roots: No changes.
5. CRO AFTER-read: the same reads; 49F reads OPAL_HOLDINGS figures, D does not reopen, F unchanged. Any unnamed
   difference -> same-turn rollback.

**Rollback per key:** Lambda -> S3 version 5bmwADQs (qfxZ0DzB) as the artifact, re-apply; role policy and bucket fence
-> revert ae20e904e6's two .tf files, re-apply both roots (the engine prefixes return). The retained OPAL_HOLDINGS reports
written in between stay as records; after rollback the engine path answers again.
