# ETFS_RIVALS round 30 on dell1: both J1s graded, L8 compile landed, round-close-check MAY-CLOSE -- 3.0.0_SA_CVO~RV

**archetype:** VALIDATE
**Date:** 2026-10-15 ~19:25Z to ~20:00Z (first log of this lane; it succeeds `3.0.0_SA_CVO~RV1`, last log
`logs/2026-10-12/session_dell1_RV1_1740Z-2125Z.md`)
**Task Order:** ad-hoc (ETFS_RIVALS round 30 L9 grades and L8 compile, on packet @7d58db9f71, msg 5618 to ~RV1, and
2.0.0_SA_COO~RV msg 6167 on Andrew's ask)
**Status:** COMPLETE (seat event-driven)

---

## Objective

Grade RIV-xa-2 and RIV-xc-2 J1 on the 2026-10-15 13:00Z sweep page, the first page on pin ea0e5025ac, and compile the
channel for the round-30 L10 slug.

## Work Completed

| Act | Verdict | Commit |
|---|---|---|
| Startup: /watcher (Monitor b6jrpzd7n, script pid 24920), register, XXX.md steps A-E | OK; inbox empty at load | -- |
| ADJUDICATION_v3.dell1.md / D1-C-S21 | xa-2 J1 MET: the sentence sits directly before 13 of 13 calendars, and stays in view and uncovered with each centred (Playwright, 1280x720) | 10f0414c92 |
| ADJUDICATION_v3.dell1.md / D1-C-S22 | xc-2 J1 MET as written: frame_of v2 gives 12 families of 13; CGIC stores shared_frame_with + frame_still_shared. Outcome not served: reader families of 4 and 3 that v2 splits | 10f0414c92 |
| REMEDIATION_v2.dell1.md (L8 compile, watermark D1-S18) | 4 gating items: W42-S1, W40-S1, W40-S3 REMEDIATED; D1-S16 OPEN to 1.0.0_SA_CTO~DELL1 | 52766ff0d6 |

MCP: 1 message received and acked (6167). One send to 2.0.0_SA_COO~RV was REFUSED by the L8 correspondence guard (the
CVO's one send is the slug to the CTO). The handoff therefore rides the files and round-close-check.

## Decisions Made

- xa-2 is graded on the served S3 bytes. The production URL answers 302 to Microsoft sign-in, and no session was
  available. The bytes' sha256 equals the manifest's, and the gateway route (`rivalfunds_view.py:174-194`) returns the
  object unchanged. The unexercised limb is named in the row.
- xc-2 is graded by the instrument its J1 names (frame_of v2), not by this seat's reader measure. The gap between the two
  is routed to the CTO in D1-C-S22, not folded into the grade.
- W40-S1's fix was verified by content in the pin's bytes (`git show ea0e5025ac:...gold_trade_schedule.py`), with a
  control at 9a1ce314dc, never by is-ancestor.
- The L10 slug is left to 2.0.0_SA_COO~RV under the CTO's ruling @f8191183f6. This seat did not send a slug.

## Blockers

None in this lane.

## Current State

- round-close-check `--project ETFS_RIVALS --round 30`: MAY-CLOSE (judgment 2, graded 2, ungraded 0).
- Channel: `org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/adjudications/ADJUDICATION_v3.dell1.md` and
  `remediations/REMEDIATION_v2.dell1.md`. D1-S16 remains ARMED: on 10-15 its 10:50Z and 12:50Z detect-and-void reads were
  missed, the fix is a round-31 cell, and the project parks after round 30.
- Evidence copies (not committed): scratchpad `r30/` -- page/, rh.parquet, rh14.parquet, xc2_read.py,
  xa2_bidd_calendar_20261015.png.
- Push state: LOCAL @52766ff0d6; origin box/dell1 read bc76b7f58a (ls-remote ~19:57Z).

## Next Steps

1. [2.0.0_SA_COO~RV] Send the round-30 L10 slug to 1.0.0_SA_CTO~DELL1 (round-close-check MAY-CLOSE; CVO compile @52766ff0d6).
2. [1.0.0_SA_CTO~DELL1] Round-30 analysis: D1-S16 before the park (cut the fix cell, name a standing reader, or stop the
   lookup); D1-C-S22 (the template moved into the slot v2 keeps; reader-visible largest family went from 2 of 13 to 4 of 13).
3. [3.0.0_SA_CVO~RV] Event-driven; grade anything that reaches this lane.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-rail | DENIED 4 times, each re-run per its RUN NEXT or with `# rail-checked` | An S3 listing for the bytes graded (not freshness); a curl loop; one recursive grep; one `find` |
| comp-routes trace | No match | Does not model mcp.opalinvest.dev gateway paths. The route was read in rivalfunds_view.py instead |
| comp-find | PASS | `platinum/page` census, 623 hits / 84,544 files; located the gateway viewer |
| round-close-check | PASS | MAY-CLOSE after the grades; strict-grades counted both with a verdict word |
| surprise-row-gate (commit hook) | PASS | 2 adjudication rows; 4 remediation rows; L10 precondition: 162 orders, 0 open; acceptance 22/22 |
| Playwright | PASS | Local render of the served audit.html; production URL stopped at sign-in |
| Gap | -- | comp-routes cannot trace an opal-gateway (EC2) path, so a production-URL question has no comp-tool route |
