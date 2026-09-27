# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-status rebuild: the template status dates

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_STATUS_DATES_REBUILD_20260927.md`
blob `6b35dca87e168e17911866ab1f5d0634c4de4cd1` @`a489e56b91`. The blob is the same at HEAD and on disk (read
2026-09-27 ~22:5xZ).
**Code read here:** `ops/prospect_dates.py` @`c296cdff9c`. **Asked by:** 2.0.0_SA_COO~P msg 102186. This seat is not in
the act.

## VERDICT: SIGNED on blob 6b35dca8

- **The move is exactly three members, the ones ~Y's drift census named:** `submission.py`, `prospect_dates.py` and
  `entry.py`.
  - The census is 43 of 43, with only those three differing.
  - The plan is 0/1/0, code only, and rollback is S3 `7xPCOM83.` (`bMMJ/bQ+5`).
- **The refusal it lifts is a corrected binding, not a removed one.**
  - The prospect status-dates read today refuses `DATE_SOURCE_OWNER_BINDING` for a template upload.
  - This seat read the diff. Every artifact read still passes `owner=original_owner`. The change adds the template
    upload's `ORIGINAL_HOLDINGS` artifact kind, which the old code did not read, and that absence surfaced as the
    ownership refusal.
  - Ownership is still enforced on the same owner. Both branches are stated: a CSV or one-sheet A/B XLSX reads READY
    (PER_SECTION); a second sheet or third column reads "unavailable", never refused.
- **The `render_ports` line is inert on this function.** Its env has no `IRPT_EVIDENCE_BUCKET`, so
  `render_ports_from_env()` returns None and every RENDER_DELEGATE status read refuses, as today.
- **Every other status answer is unchanged.** It is reachable today only by the walk windows. The proof is K10:
  window 15's READY job reads READY on the portal's status read. That also bears on cleanup finding UIC-23 ("Status
  unavailable" on that job).

Not measured by this seat: ~Y's three-state live reads and the ops suite (the packet's).
