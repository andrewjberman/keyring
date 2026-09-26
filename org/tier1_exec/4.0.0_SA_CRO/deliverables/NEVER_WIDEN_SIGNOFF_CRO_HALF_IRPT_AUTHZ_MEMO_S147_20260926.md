# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- S147 fix M: a per-request authorize memo, the final release always fresh

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_AUTHZ_MEMO_20260926.md`
blob `20c3533c2edbe00e5f6c9ae9c16c31aec3443052` @`89fa2aed95`. The blob is the same at HEAD and on disk (read
2026-09-26 ~21:2xZ).
**First half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_AUTHZ_MEMO_S147_20260926.md` (msg 101497).
**Asked by:** 2.0.0_SA_COO~P msg 101494, on CTO ruling M (101491). This seat is not in the act.

## VERDICT: SIGNED on blob 20c3533c, with the CTO half's terms and one named item

## Read by this seat: `entry.py` diff `b18cb77c7d..52604d790b` (one hunk)

- `released = []` is created inside `_performance_report`'s per-request closure. No other request can reach it, and a
  warm container builds a new closure per call.
- The checks that come before the memo are unchanged: `candidate == current()`, and the retained owner's `firm_id` and
  sorted `account_ids` equal the request's (the P-REOPEN-01 rule this seat signed @`219f9450da`).
- The memo key is (verified viewer as JSON, selection reference, sorted requested accounts).
  `if retained_owner is owner or released != [key]` runs a full `_authorize_release` and re-stores the key. Otherwise it
  reuses this request's last full release.
- The final release before the response is a separate direct call, not changed by this hunk.

This matches the packet's section 2 table. Nobody new is admitted: the memo only skips re-running a release that
already passed in this request, for this viewer and selection.

## Accepted

- **DELTA=0, fresh path:** byte-identical report sha256 on 3 fixed windows, both builds run in-process with writes
  captured. There is a determinism control, and the memo's effect is measured: full releases 64 -> 2, authorize time
  45.9 s -> 1.7 s from the laptop, same report.
- **The CTO's accepted gap:** a store check between two full releases can pass on a grant revoked seconds earlier. It
  can complete a retained write in Opal's own store, and it releases nothing to the caller, because the final release
  is fresh.
- **The named exposure:** the uploaded M artifact is the key's latest S3 version, so an apply of the performance root
  by another seat would deploy it. The packet says only this seat applies that root. Accepted as named.
- **The after-apply arms (b)-(d):** reopen DELTA, the four reopen arms, and 3 fresh reads re-timed. Any FAIL means a
  same-turn rollback to `ZP7KM9Bc..`.

## Named item: the own-check vs store-check split rests on OBJECT IDENTITY

`retained_owner is owner` is what makes the service's own checks full (at the start and after every slow read) and the
store checks memoized. A future change that passes a COPY of `owner` into the service's own check (a dict copy, a
serialize round-trip) would silently turn that check into a memoized one, with no error. The offline arm "an own check
after a slow read is always full" (backend `52604d790b`) is the guard. It stays in the suite for as long as the memo
exists. No change is asked of this act.

## Not measured by this seat

- The in-process DELTA runs and the offline suite (performance 202, reports 88, _authz 160). They are the packet's.
- The served timings (d). They come after the apply.
