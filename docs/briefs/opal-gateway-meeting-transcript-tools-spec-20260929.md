# Spec: meeting-transcript read tools on the Opal gateway

- Author: `4.0.0_SA_CRO~T`, 2026-09-29. Status: PROPOSED. Not dispatched; routed to `1.0.0_SA_CTO`.
- Recon: `docs/briefs/teams-meeting-transcripts-programmatic-pull-recon-20260929.md`
- Orders: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_143xZ_TEAMS_MEETING_TRANSCRIPTS_PROGRAMMATIC_PULL.md`,
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_16xxZ_TRANSCRIPTS_FOUR_MEETINGS_ON_ALL_INVITES.md`

## 1. Outcome

Signed in as andrew@opalinvest.com, a session lists and reads the complete speaker-attributed transcript of every
occurrence of four meetings: the 9a ET Monday Meeting, the OCIO investment committee, the Asset Management
investment committee, and the Research Meeting.

## 2. HYPOTHESIS this spec rests on, and its test

Hypothesis: the DELEGATED permission reaches a meeting where the signed-in user is an invitee and not the
organizer. Microsoft's reference page states it; the 2026-07-31 session recorded the opposite; neither was
exercised. The FIRST act of the build is the test in section 6 step 1. If it fails on reach, stop: sections 3 to 5
are void and the application route in the recon brief section 6 is the only one left.

## 3. Preconditions outside the gateway

| Precondition | Owner | Role it takes |
|---|---|---|
| Teams "Microsoft Graph access" to transcripts ON | Andrew via IT | Teams Administrator |
| Teams "Include speaker attribution" ON | Andrew via IT | Teams Administrator |
| Entra change | none | none: `OnlineMeetingTranscript.Read.All` and `OnlineMeetings.ReadWrite` are already in `GRAPH_SCOPES` |

Cloud Application Administrator does not reach the two Teams settings. They are Teams meeting configuration, not
an Entra application permission.

The ask to IT, verbatim:

```powershell
Set-CsTeamsMeetingConfiguration -EnableGraphTranscriptAccess true -EnableAttributedTranscripts true -Identity Global
```

Readback: `Get-CsTeamsMeetingConfiguration -Identity Global` shows both properties True.

## 4. Tools (all in `infra/aws/ec2/opal-gateway/app/tools.py`, all through `_run`, all read class)

### 4.1 `find_online_meeting(join_url: str) -> dict`

`GET /me/onlineMeetings?$filter=JoinWebUrl eq '{join_url}'`. Returns id, subject, organizer, start, end.

### 4.2 `list_meeting_transcripts(meeting_id: str) -> dict`

`GET /me/onlineMeetings/{meeting_id}/transcripts`, following `@odata.nextLink` to exhaustion. Returns every row
(id, createdDateTime, endDateTime) and the row count.

### 4.3 `read_meeting_transcript(meeting_id: str, transcript_id: str, offset: int = 0, limit: int = 0) -> dict`

`GET /me/onlineMeetings/{meeting_id}/transcripts/{transcript_id}/content` with `Accept: text/vtt`.

Returns `content`, `total_bytes`, `sha256` of the FULL body, `offset`, `returned_bytes`, `complete`.
`limit = 0` means the whole body. No `max_chars` default. A caller that pages reassembles and checks `sha256`.

### 4.4 `list_calendar` change

Add `onlineMeeting` and `seriesMasterId` to its `$select`, and accept a start date, so the join URL of a PAST
occurrence is reachable. Today it reads forward only and omits the join URL.

## 5. Constraints

1. `graph.call` hardcodes `Accept: application/json`. The content read needs `text/vtt`. Add an optional `accept`
   argument; do not fork a second client.
2. Register each new tool in BOTH classification lists or it is denied: the read set in
   `app/destructive_ops.py` and the tool table in `app/data_entitlement.py`.
3. No new scope. `IT_REQUEST.md` pins the scope list four ways; this spec changes none of them.
4. Errors surface `innerError.code`. `GraphAccessToTranscriptsDisabled` and `SpeakerAttributionNotAllowed` are
   distinct outcomes and must not collapse into one generic 403. `graph.GraphError` reads only the outer code today.
5. Never fall back silently to the unattributed format. A transcript without speakers is a different artifact.
6. Transcript text is untrusted external content, the same rule as Teams chat text.
7. The audit record carries meeting id and transcript id, never transcript text.

## 6. Acceptance, in order

1. REACH. As Andrew, `list_meeting_transcripts` on the Research Meeting, which a colleague organizes. Expect 200
   with at least one row. Negative arm: a meeting Andrew is not invited to returns a refusal.
2. COMPLETENESS. `read_meeting_transcript` on one occurrence. `total_bytes` equals the byte length of the body and
   the last cue's end time is within one minute of the transcript's `endDateTime`.
3. ATTRIBUTION. The body contains `<v ` speaker tags.
4. ALL FOUR. Steps 1 to 3 on each of the four meetings; print 4 of 4.
5. LAND. One transcript parsed by `research_transcripts/bin/ingest_vtt.py` with 0 unparsed cues.

## 7. Out of scope

Recordings (audio or video). Ad hoc calls (`CallTranscripts.Read.All` is not consented). The application-permission
route. Any scheduled puller: this spec delivers on-demand reads only.

## 8. Clock

Teams showed these transcripts expiring at 120 days (2026-07-31 log). Occurrences before about 2026-06-01 may
already be unreachable. Read oldest first once the tools exist.

## 9. ADDENDUM 2026-09-29: the private home (Andrew-direct, layout approved, two readers)

Order: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_19xxZ_TRANSCRIPTS_LAYOUT_APPROVED_PRIVATE_TWO_ACCOUNTS.md`.
Layout: `docs/briefs/transcripts-sharepoint-layout-proposal-20260929.md`.
Readers, exactly: andrew@opalinvest.com, opalbloomberg@opalinvest.com.

### 9.1 What the gateway cannot do today (measured 2026-09-29 from source and by call)

| Need | Gateway today |
|---|---|
| Write a file into the signed-in user's OneDrive | no tool; `upload_text_to_site` writes to a SharePoint SITE only |
| Address the personal site as a site id | refused: Graph 400 "Url specified is invalid" |
| Set sharing on a folder | no tool; 0 references to invite, permissions or createLink in `app/*.py` |
| READ sharing on a folder | no tool |

A folder on a team site inherits that site's membership, so it is not private and must not be used.

### 9.2 Tools to add

1. `upload_to_onedrive(folder_path, filename, content)`: `PUT /me/drive/root:/{folder}/{filename}:/content`,
   conflictBehavior fail, bytes preserved. The home is `Transcripts/` in Andrew's OneDrive.
2. `list_item_permissions(item_id)`: `GET /me/drive/items/{id}/permissions`. Read class.
3. Sharing is NOT a gateway tool in this spec. Andrew shares the folder to the second reader by hand, once.
   A grant tool is a write to access control and needs its own security review.

### 9.3 Acceptance, added

6. PRIVATE. `list_item_permissions` on `Transcripts/` returns exactly two principals, the two readers above, and
   no link-type permission. Any third principal or any sharing link fails the step. This step runs BEFORE the
   first committee transcript is written.

### 9.4 Carried constraints

- The three non-research archetypes never land in the git repository. `research_transcripts/bin/land_graph_transcript.py`
  refuses them (`repo_store_allowed` in `schema/series.json`), exit 4.
- opalbloomberg@opalinvest.com is a tool-scoped identity on the gateway (`app/identity_scope.py`). If it is to read
  transcripts THROUGH the gateway, its allowlist needs the read tools; reading the shared folder in SharePoint
  needs no gateway change.
