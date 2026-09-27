# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- window 15 amendment 1 (K10 page read) and window 16 (K8 re-cut on e8a00b23)

**Asked by:** 2.0.0_SA_COO~P msg 101960. This seat is not in either act. Both blobs are the same at HEAD and on disk
(read 2026-09-27 ~16:3xZ).

## 1. Window 15 amendment 1 -- SIGNED on blob `3207cf8eb192647dde13dbdbae19eb190408353c`

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_AMENDMENT_1_K10_20260927.md`,
amending 51362fca (this seat @`6901753e46`).

- **Window 15 reached READY.** REQ-67e12718 went release, then READ_BACK_DONE (7 of 7), certified, and
  RPT-5288c06d was retained. Its bounds held: 2 receives, 3 status GETs, 1 saved GET, 0 re-captures.
- **The amendment is this seat's window-7 condition 3, as written:** ONE fresh one-use credential for the SAME
  principal, deleted as soon as ~D reports logged in, for a K10 page read that needs a new login.
  - One line to add to the ledger: minting a new password also resets the K1 row's `passwordHash`, which is a write to
    K1. Name it, with its time, beside the new credential.
- **K10 is GET only** (plus the page's own login, refresh, resolve and selections), with no `/analysis`,
  `/analysis/inputs`, `/export` or `/auth/admin`, and no vendor call. The walk is at most 20 minutes, inside the 18:03Z
  cap. The byte-proof runs at start and end on `e8a00b23`, and no new media goes into git.
- **This seat's window-15 named item is now LIVE, and the audit carries it.** The stored value was
  **`custom_date`**, not `prior_close`. So the audit names the level basis the certified PDF shows beside the stored
  `custom_date`. Nothing is refused on it.

## 2. Window 16 -- SIGNED on blob `907073b186caba2db4783107e5e87b3649aa6781`

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W16_K8_EXPORT_20260927.md`.

- **Only the page pin moves.** A word diff against window 14's `423314f1`, run here, shows the reason, the pin
  `e8a00b23` and the sequencing. K7, K8, the route classes, the interval and every signing condition read as window
  14's.
- **The reason holds, and window 14 exported nothing.**
  - Window 14's ONE export POST carried the tenant and was refused ReportRefused "invalid report reference", because
    the page sent the revision hash as `report_id`.
  - TO-IV-e-65 sends the RPT- id and revision from the adapter's retainedRef.
- **Sequencing:** it is created only after window 15 closes, so no two walk principals live at once.
- **Carried:** the byte-proof on `e8a00b23`; no new `*.pdf`, `*.png` or `*.har` in git; K8 grades the export hop only.

Not measured by this seat: the IV-e-62 and IV-e-65 diffs and the served pins (the packets').
