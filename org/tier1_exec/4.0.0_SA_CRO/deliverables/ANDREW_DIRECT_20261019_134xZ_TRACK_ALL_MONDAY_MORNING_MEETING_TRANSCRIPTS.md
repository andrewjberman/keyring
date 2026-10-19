# ANDREW-DIRECT 2026-10-19 ~13:4xZ -- track transcripts for every Monday morning meeting

**Channel:** Andrew at the `4.0.0_SA_CRO` terminal (laptop). **Recorded by:** `4.0.0_SA_CRO`, same turn.

VERBATIM:

> make sure we are tracking transcripts for all monday morning meetings. i want to be sure that todays transcript is available

## What was measured (2026-10-19, 13:4xZ)

- Andrew's calendar holds three Monday-morning items today: Morning Meeting (13:00-14:00Z, organizer Austin Graff),
  Opal Investment Committee (13:00Z, CANCELED today; its join URL returns Graph 404), and AJ x Andrew Sync (13:30-14:00Z,
  organizer Andrew).
- Morning Meeting is series `monday_meeting` in `data/transcripts/scripts/teams/series.json` (NFRA_TRNSPT). The scheduled
  pull runs hourly on weekdays at 13:00Z-22:00Z; the 13:00Z run today listed 20 transcripts, 16 HELD, 4 READ-REFUSED
  (2026-04-10, 04-13, 05-04, 06-01: Graph 502 on every run), 0 new. Last landed: MM-20261012-0858 at the 14:00Z run.
- AJ x Andrew Sync: Graph lists 0 transcripts ever for its meeting id; it is not a tracked series.
- research_meeting (Tuesday, Lauren) stays list-REFUSED (502/403 on Andrew's delegated token); not a Monday meeting.

## Carried

- Today's Morning Meeting transcript: watched by this seat until it lands in bronze
  `s3://opal-data-transcripts/teams/transcripts/bronze/monday_meeting/date=2026-10-19/`.
- Adding a series (AJ x Andrew Sync, or the Opal IC when it meets) is an NFRA_TRNSPT series row and needs transcription
  turned on in Teams; surfaced to Andrew, not adjudicated here.
