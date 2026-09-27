# Never-widen amendment 1 to WINDOW 15 -- K10: ~D reads the READY Analysis report in the page

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~16:2xZ.
**Amends:** `NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_ANALYSIS_20260927.md` (blob 51362fca, signed CTO @04d670fd75 and CRO
@6901753e46). **Ledger:** `irpt-ui-walk-principal-w15-20260927` (open).

## Why

Window 15's job REQ-67e12718b0ba7c0c70ebb45b reached **READY** at 16:23:00Z:
- the read-back released once (calculating), then READ_BACK_DONE on the saved portfolio (7 of 7 present,
  tolerated=level_as_of_type=custom_date);
- CERTIFYING, then READY;
- REPORT#RPT-5288c06d6c9799f5251f3a27632ffc1b retained, with the vendor PDF, 2 extraction-evidence objects and the
  platinum analysis report.

The signed K10 (W11-4, carried) is the journal plus table reads only, because the page could not list a job then. The
page now can (IV-e-62, the owner's requests on local DEV e8a00b23). The report is owner-scoped to THIS window's
principal, so only it can read the report in the page.

## The amendment

- ONE fresh one-use credential for the SAME principal (irpt-uiwalk-1790524948): SSM SecureString
  `/irpt/ui-walk-principal/1790524948/password`, read by ~D BY NAME, and deleted as soon as ~D reports logged in, as
  K1-CRED always is.
- ~D walks at `localhost:5174` on local portal DEV **e8a00b23**, with the byte-proof at start and end (HEAD e8a00b23,
  clean tracked status, 0 /__mockcot/).
- **K10:** the Analysis tab's request list, the READY job's status and sections, and the report. GET/HEAD only, plus the
  page's own login, refresh, resolve and selections (window 5's classes). No /analysis, no /analysis/inputs, no /export,
  no /auth/admin.
- **No vendor call:** the report is retained; reading it calls no vendor.
- **Interval:** the walk runs at most 20 min, inside window 15's 120-min cap (18:03Z). The principal is deleted at the
  walk's end.
- **Audit adds:** the HAR route census, 0 new media in git, and the CRO's line: the level basis the certified PDF shows
  beside the stored custom_date.

## What the halves sign against

This file's committed blob, amending 51362fca: one fresh credential for the same principal, and ~D's GET-only K10 page
read inside the 120-min cap.
