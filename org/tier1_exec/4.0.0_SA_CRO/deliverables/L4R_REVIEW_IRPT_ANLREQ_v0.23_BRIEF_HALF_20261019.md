# L4-R review -- IRPT_ANLREQ v0.23 @6500db27df, BRIEF half -- REFUSED (two stale rows, one missing denominator)

Reviewer: 4.0.0_SA_CRO~PRFRPT (dell2), on the CTO's delivery (msg 10951). Half hash c8a8c41d1a23.
Brief pins: original `ANDREW_DIRECT_20261008_223xZ_...` @2b21a349d1 (14 items); midstream
`docs/briefs/irpt-anlreq-ticket-center-flow-cleanup-brief-20261019.md` @b01824a2a1 (O1 to O7).

## What passes

The ENDPOINT carries every midstream outcome: O1 -> FWD-1 + C-FIRM; O2, O3, O4 -> FWD-2; O5 -> C-PACKAGER (ready-triggered);
O6 -> FWD-8; O7 -> FWD-7 (unchanged). The placement and order in ADDENDUM v0.23 match the brief's Part II.

## Corrections (by line at @6500db27df, `prd/IRPT_ANLREQ_PRD.md`)

1. **Section 6 row 1 (line 176) contradicts FWD-2.** It reads "The form offers the report types the engine serves (Overview,
   Comparison, Multi-Comp)". FWD-2 now says no report-type dropdown, with the variant derived from the comparable count. A cell
   that reads this row builds the field Andrew asked removed. Restate it: the variant is derived from the count (none: Overview;
   one: Comparison; two or more: Multi-Comp), the client sets `report_type`, and the form has no type field.
2. **Section 6 row 5 (line 180) contradicts FWD-1's bar.** "The driven arm is a synthetic Opal staff user" now conflicts with
   FWD-1's "the bar is Andrew, signed in as himself... a synthetic advisor or a pre-seeded directory row does not meet it".
   Restate the driven arm and the proof gap: the filer is never refused for want of an advisor (C-FIRM, `prospect_owner()`).
3. **Section 6 has no rows for the midstream brief.** The heading denominator is still "brief @2b21a349d1, 14 items". Add the
   second brief and one row per O1 to O7, each carrying its content into the consuming cell:
   - O3: the five models at first paint, no network wait;
   - O4: only the other-ETF check needs the catalogue;
   - O5: the packager on READY, not on `commentary_requested` (`resident_worker.py:254`);
   - O6: element cards only behind "Technical details";
   - O1: `_authz/served.py:1069-1111`, the one function family absorbed, in the same release as the email-field removal.

   Row 8 should also name C-PACKAGER's READY trigger.

Note: ADDENDUM v0.23 says this half "is accepted because the CRO wrote the brief". The notifier delivered it anyway, and two
rows now contradict the ENDPOINT, so this review grades it. The corrections are text only; nothing in the ENDPOINT changes.

## Re-check at v0.24 @7b55cfefe1 (half hash 4680bc391161) -- SIGNED

- Row 1 now derives the variant from the count; the report-type field is gone.
- Row 5 states the any-firm, never-refused, unseeded bar. It is consistent with FWD-1's restated ACCEPT: the unseeded synthetic
  staff user meets the bar, and Andrew's filing is the organic arm.
- The midstream brief has its own table (O1 to O7, denominator 7). Each row carries content, path, guard and proof gap:
  `_authz/served.py:1069-1111`, the READY trigger at `resident_worker.py:254`, "Technical details", and first paint.
- No outcome, contract or surface moved beyond the text the two reviews asked for.
