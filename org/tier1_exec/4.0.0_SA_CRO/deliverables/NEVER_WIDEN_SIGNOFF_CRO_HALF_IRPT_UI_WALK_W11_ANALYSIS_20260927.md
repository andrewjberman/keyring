# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 11: the Analysis chain, fourth attempt, on resident wf

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W11_ANALYSIS_20260927.md`
blob `9ee0c7c50ee0bf552ca35ee76cb3f474b707593e` @`7aad982d3e`. The blob is the same at HEAD and on disk (read
2026-09-27 ~12:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101869. This seat is not in the act.

## VERDICT: SIGNED on blob 9ee0c7c5

- **It is window 7's text** (which this seat signed on blob 3ab51a52, with its K1-CRED condition) **plus bounded
  deltas.**
  - The start is Andrew's own word at ~Y: "yes you can run as many analysis attempts as needed" (@460e2ae8cb).
  - This window is ONE of those attempts: ONE upload and ONE Overview, with no retry inside it.
- **K5's vendor calls are bounded** (W11-3):
  - at most 6 status GETs, 15 s apart, with the lease renewed between them;
  - on a WAF challenge, ONE re-capture through the job's one `session_refresh` intent. A second challenge goes to a
    named ATTENTION with no further capture.

  The two writes a challenge adds (the intent row and a new YCharts session-secret version) are named and kept.
- **K10 is read-only** (the journal, ~Y's status reads, and table reads), and there is no page read.

## Named, not conditions

1. **Andrew's word is not narrowed here.** "As many analysis attempts as needed" is his, given to ~Y, so this half
   adds no attempt limit. Each attempt is its own window and packet.
   - Each re-capture is an automated sign-in on the enrolled vendor account. The audit's re-capture count (W11-5) is
     therefore also the running total across attempts: windows 8 and 11, and any later window.
   - The ledger prints that running total, so it is visible to Andrew if the account ever locks.
2. **This seat's window-6 named item 2 likely closes.** W11-4 records the request-list route as served and
   **owner-scoped** (GET `.../analysis/requests` on irpt-status, P 101848). An owner-scoped list shows no firm viewer
   the kept test requests in `cottonwood`. The item closes when the portal wires that route (DSGN_IRPTV1-S18/E9) and
   a firm-viewer read shows 0 test requests. Until then it stays parked in STATUS~P.

## Carried

- Named item 1 (no ui-walker arm through this window's audit close).
- K1-CRED deleted at login.
- The 120-minute cap with the terminal-job rule.

Not measured by this seat: the W11-1 pins and the resident wf proof (the packet's and ~Y's).
