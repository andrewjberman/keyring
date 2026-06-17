# 0.6.0_AE_PartnerETL — 06-17 addendum: BD-source snapshot cadence characterization (COO RAVC2)
**archetype:** DIAGNOSE

## Window
06-17 ~1414Z, follow-on to the cold-start verify (session_coldstart_p1cotetl_p2gldinc_verify_1359Z.md,
a789fe877). COO accepted both GREENs (RAVC close 141432Z) + dispatched a bounded in-lane next step:
characterize the BD-source CurrentDay snapshot refresh cadence (expected periodic vs stalled feed) for
the expected-vs-stall determination. Read-only; BD feed untouched. CTO also RAVC-closed P1/P2 (141600Z)
and routed the secondary finding + templateId to DS.

## Method
For every forwardfill_v2/{table} export across the full pipeline window, read the BD "Timestamps" sheet
(Start/End/Date-Range/Created) via boto3+zipfile -> built run_date -> BD-stamped as-of timeline per table.
Cross-referenced deployed templateId per table to disambiguate persisted-reuse vs auto-create.

## Finding — CurrentDay snapshot tables are FROZEN at fixed per-table dates (never advanced)
| table       | BD mode      | templateId        | BD as-of (ALL runs)          | advances? |
|-------------|--------------|-------------------|------------------------------|-----------|
| holdings     | Current Day | 226355 persisted | 6/8/2026  (7 runs 06-09..06-17) | NO frozen |
| unrealized   | Current Day | false auto-create| 6/9/2026  (5 runs 06-13..06-17) | NO frozen |
| allocations  | Current Day | 226334 persisted | 6/5/2026  (8 runs 06-05..06-17) | NO frozen |
| realized     | Custom      | false auto-create| End = run_date (06-13..06-17)   | YES daily |
| transactions | Custom      | 226274 persisted | End = run_date (06-12..06-17)   | YES daily |

Conclusions:
1. NOT a periodic cadence, NOT abrupt-stop-after-frequent — the CurrentDay tables NEVER advanced once in
   the window; each pinned to a fixed date (holdings 6/8, unrealized 6/9, allocations 6/5).
2. Freeze correlates 100% with BD Date-Range MODE = "Current Day", NOT with templateId reuse: unrealized
   is templateId:false (fresh-creates a template every night) and is STILL frozen at 6/9. So it is BD's
   SERVER-SIDE "Current Day" resolution that is pinned — not our reuse, not our date-stamping (our code
   deliberately does not stamp dates onto CurrentDay queries; stamping start=end=today zero-rows them).
3. BD link HEALTHY: Custom tables advance End=run_date nightly with real recent data (realized Trade Dates
   through 06/15) — not a broken connection/auth; specific to the CurrentDay snapshot feed.
4. Three DIFFERENT frozen dates (6/5/6/8/6/9), not one global stall date -> the three snapshot feeds each
   last posted on a different day and stopped. Most consistent with COT's custodial position/snapshot feed
   INTO BD pausing ~6/5-6/9 while the transaction feed stays current.

My read (for Andrew's call): leans STALLED-snapshot-feed (never-advanced + 3 stuck dates + live txn feed),
but the expected-vs-stall determination rests on Andrew's COT onboarding/recon-arrangement knowledge
(plausible the custodial position feed lags during the recent 04-22 BD onboarding, or a recon-trigger
cadence we haven't seen fire). Could not distinguish "feed paused" from "recon not yet due" from artifacts alone.

## NFRA_INFRPT P1 nuance (handed to DS/~B)
cot snapshot-table freshness (holdings->AUA, unrealized, allocations) must key off BD's stamped Timestamps
as-of date, NOT run_date/same-day, or the freshness section false-REDs every run. Gate = alert if BD as-of
older than the EXPECTED BD snapshot interval (once Andrew confirms); until then baseline the current stamps
so it reports "BD-source-bound, as-of <stamp>". Custom tables (realized/transactions) CAN be same-day-keyed.

## Compiler Tools
No comp-* tool run. Why (per gate): read-only BD-export Timestamps-sheet characterization on opal-data-cot
(separate firm; comp-pipescript is bd-only per reference_comp_pipescript_io_postdeps_bd_only_silent_unknown)
with no gold-run/iam/infra change -> no comp trigger applies. Tooling: boto3 list/get_object + python
zipfile (namespace-aware x: parse) Timestamps-sheet extraction; aws s3 ls for the run-date series.

## MCP traffic
- Inbound: COO dispatch (141432Z, cadence ask) + CTO ACK (141600Z, RAVC close) — both acted.
- Outbound: ACK->COO (141548Z); RAVC2 cadence finding->COO (141920Z) + CC CTO (141926Z).

## Blockers
None.

## Current State / Next Steps
- Cadence RAVC2 delivered; awaiting COO/Andrew expected-vs-stall determination (not mine to make).
- OPEN (routed, not mine): BD CurrentDay snapshot stall determination (DS/Andrew); templateId pin-back (DS).
- No pending TOs. IDLE/available; event-driven. GLDINC daily_watch_until 2026-07-05 binding still stands.
