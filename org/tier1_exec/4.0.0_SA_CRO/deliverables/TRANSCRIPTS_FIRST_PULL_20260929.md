# First pull of Teams meeting transcripts into opal-data-transcripts -- 2026-09-29

- Author: `4.0.0_SA_CRO~T`. Order: `ANDREW_DIRECT_20260929_190xZ_TRANSCRIPTS_BUILD_UNILATERALLY_ANDREW_OVERSEES.md`.
- Every figure below was read from Microsoft Graph or from the bucket on 2026-09-29, about 20:45Z to 21:15Z.

## How it was run

Andrew signed in by device code as andrew@opalinvest.com to Microsoft Graph Command Line Tools. Calls were
delegated, Graph v1.0. The token sat in a file in the session temporary folder, outside the repository, and the
folder was deleted after the pull (absence read back). The token carried MORE scopes than the two requested,
including directory, site and file write scopes, because the tenant already holds broad consent for that
application. Only `/me/onlineMeetings` and its transcripts were called. The standing consent is a finding.

## What Microsoft returned

| Archetype | Teams subject | Organizer | List | Listed | Content 200 | Content 404 |
|---|---|---|---|---|---|---|
| monday_meeting | Morning Meeting | Austin Graff | 200 | 19 | 15 | 4 |
| ocio_ic | OCIO IC | Austin Graff | 200 | 7 | 7 | 0 |
| asset_management_ic | Asset Management IC | Austin Graff | 200 | 8 | 8 | 0 |
| research_meeting | Research Team Meeting | Lauren Harmon | 403 (3003) | 0 | - | - |

Denominator: 34 listed across 3 meetings; 30 landed; 4 failed.

- The tenant setting is on: a 200 on `/content` with `text/vtt` needs Graph transcript access and speaker
  attribution enabled.
- Invitee access works: Andrew organizes none of the three and reads all three.
- The 4 failures are the 4 oldest rows (2026-04-10, 04-13, 05-04, 06-01), "Item not found". The next row
  (06-08) returned content. The cause, the roughly 120-day expiry, is INFERRED from the dates.
- The Research Meeting is refused: "User does not have access to lookup meeting".
- Three other "Asset Management IC" chats and "Opal Investment Committee" returned 404 on a derived id. One probe
  failed locally (shell fork error) and is UNREAD.

## What is in the bucket

| Measure | Value |
|---|---|
| Objects under `teams/transcripts/bronze/` | 90 (30 transcripts x raw vtt, metadata vtt, graph.json) |
| Encryption read on one object | aws:kms, key 44a2284f, bucket key on |
| Checksum read back on one object | served sha256 equals the sidecar |
| Speaker tags | every cue tagged, all 30 |
| Other object | `_provisioning/probe-20260929.txt`, the cloud operations seat's probe |

## Not done

No silver tier. No repeatable or scheduled puller (this was a one-off under a one-hour sign-in). The second
reader has no access. The pull script lived in the temporary folder and is gone.
