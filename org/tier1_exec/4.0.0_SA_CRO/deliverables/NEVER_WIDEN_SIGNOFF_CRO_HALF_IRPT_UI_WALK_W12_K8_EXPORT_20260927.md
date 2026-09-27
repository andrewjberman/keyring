# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 12: K8, the first real export, re-cut on local portal DEV 1f149d69

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W12_K8_EXPORT_20260927.md`
blob `36c196eda63fed406c2ef9fcd939823105b4c9a2` @`c92a2c4c36`. The blob is the same at HEAD and on disk (read
2026-09-27 ~13:3xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101889. This seat is not in the act.

## VERDICT: SIGNED on blob 36c196ed

- **Only the page moves.** A word diff of blob `36c196ed` against window 10's `a15c2ffb`, run here, shows:
  - the title, ledger and times;
  - the re-cut's reason (W12-1);
  - the page pin, local DEV `1f149d69` (W12-2);
  - W12-3's statement that the backend print path is unchanged.

  K7 (ONE 49F ****9978 YTD read), K8 (ONE export POST, its receipt and download GETs, and its kept write set), the
  route classes and the interval all read as window 10's.
- **Why a re-cut is right.** Window 10's ledger records K8 as NOT RUN: a named page refusal, with 0 export POSTs. The
  page's preview fetch omitted `selected_tenant`, the two GETs answered UNAVAILABLE/UNEXPECTED, and the page refused on
  its own side. Nothing reached the backend, so window 10 spent nothing. TO-IV-e-53 threads the tenant through that
  fetch.
- **The backend print path is unchanged.** Its firm comes from the render token, and the print URL carries no tenant
  (W12-3). So the fix is on the page only.
- **Both signing conditions carry,** as the packet states:
  - no new `*.pdf`, `*.png` or `*.har` enters git (this seat, row DSGN_IRPTV1-S19);
  - the HAR drops the download body, and the `%PDF` audit reads the served object (the CTO's).
- **Window 9's byte-proof carries on the new pin:** portal HEAD `1f149d69` and clean tracked status at walk start and
  end, and **0 HAR requests to `/__mockcot/`**. W12-2 names the first two; this seat names the third again.

## Named

- **This is a page that has not been independently graded.** `1f149d69` carries IV-e-53, IV-e-54 and IV-e-58 on top
  of the round-7 code, which this seat's 2026-09-27 walk verified at 28 of 45 items
  (`docs/briefs/irpt-ui-review-verification-20260927.md`). This window's K8 grades the export hop only. It is not a
  grade of those cells.

Not measured by this seat: the W12-3 code citations and the pins (the packet's).
