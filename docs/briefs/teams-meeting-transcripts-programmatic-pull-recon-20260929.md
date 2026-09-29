# Recon: programmatic lossless Teams meeting transcripts through the Opal gateway

- Author: `4.0.0_SA_CRO~T`, 2026-09-29.
- Order: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_143xZ_TEAMS_MEETING_TRANSCRIPTS_PROGRAMMATIC_PULL.md`
- Kind: recon. Nothing was built, no tenant setting was changed, no Microsoft Graph call was made.

## 1. Conclusion

The pull is feasible with the permission the gateway already requests. Two things stand between today and a
working pull: a Teams tenant setting that defaults to OFF, and the absence of any transcript tool in the gateway.
Neither is an Entra application-permission problem, so the Cloud Application Administrator role is not the role
that unblocks it.

## 2. What the repo shows (claim class: measured from source, NOT from the live tenant)

| Item | Value | Evidence |
|---|---|---|
| Gateway requests `OnlineMeetingTranscript.Read.All` (delegated) | yes | `infra/aws/ec2/opal-gateway/app/config.py` `GRAPH_SCOPES` |
| Gateway requests `OnlineMeetings.ReadWrite` (delegated) | yes | same |
| Scope recorded as admin-consented on the Graph app registration | yes, as of the 2026-06-24 consent screenshot | `infra/aws/ec2/opal-gateway/IT_REQUEST.md` |
| Gateway tools that call a transcript or online-meeting endpoint | 0 of 37 tools registered in `tools.py`; 0 transcript references in any `app/*.py` outside `config.py` | `infra/aws/ec2/opal-gateway/app/tools.py` |
| `CallTranscripts.Read.All` (ad hoc calls) requested | no | `config.py` |
| Live consent state today | UNREAD | the gateway session in this seat is not signed in |
| Tenant "Microsoft Graph access" to transcripts | UNREAD | Teams admin center; not readable from the repo |

All permissions on the gateway are DELEGATED. The gateway acts as the signed-in user and holds no application
permission.

## 3. What Microsoft requires (claim class: read from Microsoft Learn on 2026-09-29)

1. TENANT SWITCH. Teams admin center, Meetings, Meeting settings, "Transcript API access". "Microsoft Graph access"
   is OFF by default. While off, every transcript request returns 403 `GraphAccessToTranscriptsDisabled`
   regardless of app permissions. This takes a Teams Administrator.
2. SPEAKER ATTRIBUTION. A second toggle, "Include speaker attribution", also OFF by default. While off, the
   speaker-tagged format returns 403 `SpeakerAttributionNotAllowed` and only an unattributed text format is
   served. A transcript without speakers is not lossless, so this toggle must be ON.
   PowerShell form of both:
   `Set-CsTeamsMeetingConfiguration -EnableGraphTranscriptAccess true -EnableAttributedTranscripts true -Identity Global`
3. DELEGATED REACH. With the delegated permission, the signed-in user can read transcripts of meetings where that
   user is on the calendar invite, organizer or attendee, for private and channel meetings.
4. APPLICATION REACH (unattended, no signed-in user). Needs the APPLICATION permission
   `OnlineMeetingTranscript.Read.All` plus a Teams application access policy granted to each organizer. Cloud
   Application Administrator cannot consent to Microsoft Graph application permissions; that takes a Privileged
   Role Administrator or Global Administrator. The access policy takes a Teams Administrator.
5. A transcript exists only if transcription was started in that meeting. Meetings must not have expired.

Sources:
- https://learn.microsoft.com/en-us/graph/api/calltranscript-get?view=graph-rest-1.0
- https://learn.microsoft.com/en-us/graph/api/onlinemeeting-getalltranscripts?view=graph-rest-1.0
- https://learn.microsoft.com/en-us/microsoftteams/meeting-transcript-api-access
- https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference

## 4. The call sequence (delegated, as the signed-in user)

```
1. GET /me/calendarView?startDateTime=..&endDateTime=..        -> event.onlineMeeting.joinUrl
2. GET /me/onlineMeetings?$filter=JoinWebUrl eq '{joinUrl}'    -> onlineMeeting id
3. GET /me/onlineMeetings/{id}/transcripts                     -> one row per occurrence, createdDateTime
4. GET /me/onlineMeetings/{id}/transcripts/{tid}/content         Accept: text/vtt
5. GET /me/onlineMeetings/{id}/transcripts/{tid}/metadataContent
```

A recurring series (the Monday meeting, a standing committee) is ONE online meeting id with one transcript per
occurrence, so step 3 is the per-week enumerator.

## 5. What "lossless" means here

`text/vtt` is the fullest form Microsoft serves: every utterance with start and end timestamps and a speaker tag.
Store the raw bytes unmodified, plus `metadataContent`, keyed by meeting id and transcript id. It is lossless
against the Teams transcript, not against the audio: Teams' own speech recognition errors are already in it. The
audio itself is the recording, a separate artifact and permission (`OnlineMeetingRecording.Read.All`), which the
gateway does not request.

The existing gateway file readers truncate at `max_chars` (default 20000). A transcript tool must not truncate;
it must return or land the whole body.

## 6. Two routes

| | Route A: delegated, through the gateway | Route B: application, unattended |
|---|---|---|
| Entra change | none | add Graph application permission + admin consent |
| Role needed for Entra change | none | Privileged Role Administrator or Global Administrator |
| Teams change | the two toggles in section 3 | the two toggles + application access policy per organizer |
| Reach | meetings where the signed-in user is invited | every meeting of each policy-granted organizer |
| Bulk verb | per-meeting listing | `getAllTranscripts` with delta sync, organizer-scoped, no channel meetings |
| Gateway build | two read tools | a new server-held credential path |

Recommendation: Route A. It needs no new permission and fits the gateway's per-user model. Route B is only
needed if a meeting in scope does not have Andrew on the invite.

## 7. Open facts (owner: Andrew)

1. Who organizes each of the three meeting families, and is Andrew on each invite.
2. Whether transcription is switched on in those meetings today. If it is not, no transcript exists to pull.
3. Who holds Teams Administrator in the tenant, to flip the two toggles.

## 8. Build items if this proceeds (owner: NFRA_OPLGTW lane, via `1.0.0_SA_CTO`)

1. `list_meeting_transcripts` and `read_meeting_transcript` on the gateway, read-only, untruncated, raw VTT.
2. Add `CallTranscripts.Read.All` only if ad hoc calls are in scope; that is a consent change and must stay in
   step with the four pinned scope lists named in `IT_REQUEST.md`.
3. A landing home for the stored transcripts, addressed by the naming builder per rule 30.

## 9. Prior work found after the first cut (2026-07-31, `4.0.0_SA_CRO`)

Source: `org/tier1_exec/4.0.0_SA_CRO/logs/2026-07-31/altresearch_standup_and_transcript_access.md`.

| Fact from that session | Effect here |
|---|---|
| The Research Team Meeting is organized by a colleague; Andrew is an attendee | answers part of open fact 1 for that one series |
| Every FILE path to the transcript (OneDrive share, shared-with-me) returned 403 for Andrew | file routes stay dead; this brief uses the meetings API, not files |
| That session stated the delegated permission is organizer-scoped and closed to an attendee | CONFLICTS with section 3 item 3. Microsoft's page (dated 2025-12-02) says the API is "also available to users who are part of the meeting calendar invite". Neither claim was exercised: the gateway has never had a tool that calls the endpoint. |
| Teams showed the transcripts expiring in 120 days | meetings from before about 2026-06-01 may already be gone; backfill oldest-first |
| Andrew elected to obtain the application permission himself | state of that grant is UNREAD |
| A transcript store and a VTT parser exist: `research_transcripts/bin/ingest_vtt.py` | the landing side is built; section 8 item 3 reduces to feeding it |

The conflict is settled by ONE call, not by reading: sign in to the gateway as Andrew, list the transcripts of the
Research Team Meeting through the meetings API, and read the status. 200 means Route A works for attendees. 403
`GraphAccessToTranscriptsDisabled` means the tenant switch is off. Any other 403 means Route B is required. That
call needs the tool from section 8 item 1, or a one-off Graph request on Andrew's word.
