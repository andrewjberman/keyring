# NFRA_TRNSPT round 1 -- the gateway dependencies owned by NFRA_OPLGTW (site Z), for the CTO's relay

Author `2.0.0_SA_COO~T`, 2026-09-30 ~14:1xZ, at L6 (PRD C-GATEWAY-TOOLS: "Requested through MSTR's bus at L6; this project does
not build them"; seat brief: "Ask the CTO to relay to site Z; you cannot message across fabrics"). One ask: relay this file to
`1.0.0_SA_CTO~O` / `2.0.0_SA_COO~O` so the items below are cut as NFRA_OPLGTW task orders. Nothing here is built by NFRA_TRNSPT.

## What round 1 built against, and what it waits on

| # | item | PRD surface | spec | what NFRA_TRNSPT built meanwhile | un-parks |
|---|---|---|---|---|---|
| 1 | Transcript read tools on the gateway: `find_online_meeting`, `list_meeting_transcripts` (follows `@odata.nextLink`), `read_meeting_transcript` (`Accept: text/vtt`, full body, sha256; a metadata-format read too), registered in `destructive_ops.py` and `data_entitlement.py`; `innerError.code` surfaced (`GraphAccessToTranscriptsDisabled`, `SpeakerAttributionNotAllowed` distinct) | S04 | `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md` sections 4-6 | `data/transcripts/scripts/teams/gateway_client.py` -- a transport protocol with those three shapes and a fixture transport; the HTTP transport is a stub | FWD-1 hops 1-2 for real; the round-1 pull job runs unchanged once the transport is wired |
| 2 | A HEADLESS route for a scheduled caller to reach item 1 under Andrew's stored delegated token, on the `/ms/*` static-bearer pattern (`app/ms_ingest.py`, `/ms/token` capability token), read-only, output allowlisted to transcript rows and bodies | S04, S05 | same spec; C-IDENTITY ("through the EXISTING Opal gateway under Andrew's account; no new app registration, no IT") | `infra/aws/terraform/transcripts/pull.tf` (DESIRED, plan only) names a bearer secret the route would mint; the Lambda is not applied | the apply of TR-i-1 under CTO+COO halves |
| 3 | The stored sign-in's LIFETIME, measured: how long Andrew's server-held token refreshes unattended before `NeedsLogin` (`app/token_broker.py:171-183`) | S05 | PRD C-IDENTITY: "an engineering item with its own criterion, not an Andrew call" | nothing; the pull job types `REFUSED` when the gateway refuses | the schedule cadence in TR-i-1 (hourly 13-22Z Mon-Fri) is chosen; a lifetime shorter than a day changes it |
| 4 | Three mail tools under the existing `Mail.Read`: (i) attachment DOWNLOAD (`.../attachments/{id}/$value`, bytes back), (ii) a filtered, PAGED list (sender, received date, has-attachment, `@odata.nextLink`), (iii) `ccRecipients` returned with each message -- and `internetMessageId`, `conversationId`, `sentDateTime` in `read_email`'s `$select` (measured absent 2026-09-30; row `NFRA_TRNSPT-S2`) | S12 | v3 brief addendum 6 (`docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-v3-20260930.md`) | `data/transcripts/scripts/outlook/pull.py` -- a replay source over today's tool shapes and a stub gateway source; bronze partitions by `receivedDateTime` and carries `id_source=fallback` until (iii) lands | C-DEDUP's primary key, attachment bytes in bronze (`pdf_sha256`, `holdings`), the full dredge to October 2025, the daily pull |
| 5 | A HEADLESS mail route for the daily pull (same pattern as item 2) | S11, S12 | v3 section 3 | the schedule is not yet drafted for mail; it follows item 5's shape | FWD-7 "every day, no person starting it" |

## An observation the relay should carry (not adjudicated here)

Laptop worktrees `C:/Users/AndrewBerman/Desktop/wt-gw-f2` (branch `gw-f2-email-filtered`), `wt-gw-f3` (`gw-f3-inspect-attachment`)
and `wt-gw-int` (`gw-mail-tools-int`) hold UNCOMMITTED edits to `infra/aws/ec2/opal-gateway/app/tools.py`, `data_entitlement.py`,
`destructive_ops.py` and new tests `tests/test_list_email_filtered.py`, `tests/test_inspect_email_attachment.py`, by seats the
relaunch did not restart (`4.0.0_SA_CRO~T` / `0.7.0_AE_CloudOps` per the relaunch brief). They look like items 4(ii) and 4(i) in
progress on this laptop. Row `org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md` `NFRA_TRNSPT-S1`.
Whether site Z builds them or the laptop's branches are drained is the CTO's call; this seat touches neither.

## Not asked this round (round 2)

The IRPT READY hook (S18, IRPT_BCKEND), the `analysis_request` ticket type, service identity, requester-claim and attachments
(S20, D7 `OPAL_TICKET_VNEXT`), the Kimi first call (C-KIMI, Andrew's word after C-WIPE-GATE).
