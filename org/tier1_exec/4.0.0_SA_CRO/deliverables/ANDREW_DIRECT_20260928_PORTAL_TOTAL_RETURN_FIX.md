# Andrew-direct: Portal total-return correction and deployment

Seat: 4.0.0_SA_CRO~I
Date: 2026-09-28
Source: direct user instruction in this Codex thread, after the RCN-0019 investigation.

> Ok I want you to address these fixes, including deploying new code where needed, verifying said code, and then writing a $log when all is complete

Scope: correct Positioning's excluded opening day for WTD/MTD/QTD/YTD;
align its 1Q and the Model Portfolios Performance ETF feed's 1M/1Q/1Y
with Benchmark's existing 30/91/365-calendar-day methodology. Deploy the
two affected Lambda handlers through Terraform, regenerate their published
data, verify source-to-output total-return calculations and record provenance.
Benchmark and Market Overview already implement these boundaries; retain
their production code and verify them against the same contract.

The user explicitly authorizes production deployment. This record preserves
that authority for the CRO seat's scoped code and infrastructure activity.
No Git push, client email, change to model construction, or source substitution
is part of this correction. Since-inception annualization and incomplete-history
display policies retain their existing surface-specific definitions.

Verification contract: compound daily total returns, with percentage inputs
divided by 100 (legacy wide ETF input already decimal); include the first day
of to-date periods; exclude the opening cutoff for trailing calendar windows;
include observations through the as-of date; retain Positioning's null for
insufficient full-window history. Sources remain the pinned Bloomberg gross
total-return-derived PKLs documented in RCN-0019.
