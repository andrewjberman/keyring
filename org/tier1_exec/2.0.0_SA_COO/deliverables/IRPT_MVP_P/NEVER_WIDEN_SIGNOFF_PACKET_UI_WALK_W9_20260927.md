# Never-widen sign-off packet -- WINDOW 9: ~D's read-only round-7 walk (window 5's shape)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~05:3xZ.
**Asked by:** `2.0.0_SA_COO~D` 101812. **Walker:** `2.0.0_SA_COO~D` only.
**Ledger (opened before any write):** `irpt-ui-walk-principal-w9-20260927`.

This packet is window 5's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W5_20260926.md`, blob 4b68468e) with only the deltas
below. Every unnamed section reads as window 5's, including:
- the keys K1 / K1-CRED / K2 / K3 (retained) / K9 (retained);
- no upload (K4), no submission (K5), no export (K8), no render grant;
- the superadmin radius and the local-build note;
- the route audit (section 4) and branches (a)-(d).

## W9-1 -- what the window is for

The round-7 walk of the UI review's rows (search, header, account picker, drill, colours, securities map, money
format), read at 1440 px. It runs on a LOCAL portal build of DEV `200d257a` at `localhost:5174`, against the live IR
API. It is the artifact `3.0.0_SA_CVO` grades the round's judgment criteria on. ~D names the bundle's build hash in
the walk log. The HAR, scrubbed in-stream, is the audit.

## W9-2 -- no vendor call is reachable

- The adapter holds NO plan: `approved_performance_plan = null` since 04:34:55Z. `IRPT_PERFORMANCE_APPROVED_PLAN` and
  `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED` are absent, and the role holds no vendor-session grant.
- A fresh Performance read at COT or INF is therefore refused with VendorEgressRefused and 0 vendor calls, as the
  window-8 pre-checks measured.
- A 49F fresh read computes on the internal engine (no vendor) and is retained as K9, as in window 5.
- Reopens of retained reports (49F, INF RPT-df47a1fc, COT RPT-b683f188) are reads. COT's retained report still
  shows the old actual start (01-02); that is expected, since the report is immutable.

## W9-3 -- the served pins, re-read at create

- adapter `bOefL9nx..` with no plan (ledger irpt-cot-actual-window-20260927);
- generate `G/TqLPdL..`;
- irpt-status `bMMJ/bQ+5..`;
- irpt-directory-search `o1TXq5PH..`.

If any differs, the window does not open.

## W9-4 -- the interval (carried from windows 7-8)

- K1-CRED is deleted as soon as ~D reports logged in.
- The walk runs at most 60 min from the login. The window starts no job, so K1 is deleted at the walk's end, with a
  hard cap of 90 min from create.
- The audit adds the window-8 finding: the auth handler logs method and path only, so the proof of no later use is
  K1 absent (a consistent GetItem), not a by-name log read.

## What the halves sign against

This file's committed blob; window 5's text (4b68468e) as amended here; the no-plan state (no vendor call
reachable); and the interval in W9-4.
