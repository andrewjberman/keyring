# Why the Research Team Meeting is not pulled -- measured 2026-10-16

**Seat:** `4.0.0_SA_CRO~XXX` (dell1) | **archetype:** DIAGNOSE | **Project:** NFRA_TRNSPT (series `research_meeting`)
**Andrew-direct, Claude Code terminal on dell1, 2026-10-16, VERBATIM:** "I want to find out why its refused, we
should be pulling those meetings every single time they happen"

## Finding

Microsoft Graph refuses Andrew's delegated token on this one meeting. Every other link in the chain works.

| link | measured | result |
|---|---|---|
| pull schedule | `teams/transcripts/state/pull_runs/` in `s3://opal-data-transcripts`: 48 runs, first 2026-10-09T11:14:54Z, last 2026-10-15T22:00:09Z | `research_meeting` refused=1, listed=0 on **48 of 48** runs read; the other three series list (monday 20, ocio_ic 7, asset_management_ic 8) |
| pull record detail | `run=2026-10-15T22:00:09Z/run.json` series[3] | `REFUSED: list GatewayGraphError status=502` |
| gateway allowlist | same record: not `403 meeting_not_allowed` | the meeting IS on the gateway's allowlist |
| Microsoft's answer | gateway audit lake `s3://opal-mcp-audit/audit/dt=2026-10-15/2026-10-15T22:00:28...`, user `andrew@opalinvest.com`, tool `hx_transcripts` | **`graph_status=403 graph_code=Forbidden`** on `GET /me/onlineMeetings/{research id}/transcripts` |
| meeting id | `data/transcripts/scripts/teams/series.json:27` decodes to organizer `e44d429b-b629-4035-b09b-447e978322db` | the organizer is Lauren Harmon (matches her 1:1 chat id and the meeting chat's `meetingOrganizer`, NFRA_TRNSPT-S11) |
| Andrew on the invite? | gateway `list_calendar`, 2026-09-28 + 19 days: 14 events | Morning Meeting x3, Asset Management IC x2, OCIO IC x1 (all Austin's, Andrew an attendee); **0 Research Team Meeting events**, though it ran in that window (transcript event 2026-09-29) |

**Cause:** delegated transcript access reaches meetings where the signed-in user is the organizer or **on the
calendar invite**. Andrew is in the Research meeting's chat but not on the series invite, so Graph answers 403.
This confirms NFRA_TRNSPT-S11's 2026-09-30 hypothesis on a second, wider measurement (19 days of calendar vs 8)
and against the live 403 rather than the earlier 3003. Still not proven by the positive arm, which is the fix below.

## Two fixes

1. **Lauren adds `andrew@opalinvest.com` to the Research Team Meeting series invite** (Outlook: open the series,
   add attendee, send update). No code, no permission change. The next hourly pull (on the hour) should read
   `research_meeting` listed > 0 and land bronze + silver. Transcripts Teams still retains (about 120 days, per the
   2026-07-31 session; unverified) come back with the first listing, so August to October should backfill.
   **Proof:** the first `pull_runs/run=.../run.json` after the invite shows `research_meeting` refused=0.
2. **App-only access (survives anyone's invite list):** Graph application permission
   `OnlineMeetingTranscript.Read.All` (Global Admin or Privileged Role Admin consent; not within Cloud Application
   Administrator) plus a Teams application access policy granted to each organizer (Teams Administrator).
   This is the "every meeting, every time" route.

Recommendation: do 1 today; it is a one-minute act and restores the series. Take 2 only if meetings by other
organizers must be pulled without Andrew being invited.

## Not claimed

- That 1 works: proven only when a pull after the invite lists the meeting.
- How far back Teams still holds Research transcripts.
- Why the 29 silver files stop at 2026-08-03: they were loaded once on 2026-10-09 from an earlier local store
  (`research_transcripts/`), not by this pull.
