# OPAL_ALTRESEARCH stand-up: transcript corpus, 4-ETF materiality join, and the transcript-access dead end

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, EXPLORE

**Agent:** 4.0.0_SA_CRO (Chief Research Officer, Tier-1)
**Window:** 2026-07-31 ~13:36Z (session start) -> ~15:40Z
**Commits:** `0d48a4e968`, `cfdddb5d8d`, `66207c96a8` (all authored 4.0.0_SA_CRO)

---

## Summary

Andrew-direct commission at the CRO terminal, arriving mid-startup: stand up a transcript
store for the equity research team's Teams calls, register it as `OPAL_ALTRESEARCH`, and
join named securities to the weights of the four Opal ETFs (DIVZ/IDVZ/PFOE/PFDE) so that
alt-data pipeline candidates rank by firm-wide position materiality.

Delivered: the store, the project registration, transcript 1 ingested, and the complete
4-ETF materiality ranking. The join validates the premise on the very first transcript.

Not delivered, and the substance of the second half of the session: an automated transcript
feed. Andrew asked me to pull transcripts myself via the m365 MCP. I could not, and the
reason turned out to be three successively deeper wrong premises -- two of them mine.

---

## What landed

**1. The store (`research_transcripts/`, `0d48a4e968`).**
`raw/` (verbatim, never edited) -> `structured/` (parsed) -> `index/` (transcripts, mentions,
alt-data candidates) -> `analysis/`. Rule 17a applied to text: a research call is a one-shot
capture, so if the parser drops a line and the raw was tidied first the content is gone
permanently. Everything downstream re-derives from `raw/` alone.

Built a PARSER rather than hand-structuring, because Andrew stated the corpus is
multi-transcript ("until we've gone through all of them"). It reports every line it could not
consume instead of dropping it silently, and refuses to write an empty record.

`RT-20260727-1023`: 53 utterances, **0 unparsed lines**, 2 speakers. Coverage is REPORTED, not
assumed -- the paste is PARTIAL at 3.7% of its own 1h17m span across two disjoint segments.
Recorded so no share-of-attention statistic can be computed from it: a gap is unobserved, not
empty.

**2. The 4-ETF materiality ranking (`cfdddb5d8d`).**
Andrew approved TrueShares egress. The holdings were NOT in the bronze HTML we already scrape
daily (0 `<tr>` in 465KB -- JS-rendered); they resolve to a TrueShares-published Google Sheets
CSV export, one sheet per fund. DIVZ 29 constituents, IDVZ 43.

`$740,398,918` combined net assets, 166 unique securities, 12 held in more than one fund.
Two rankings, deliberately kept apart: share of COMBINED net assets (AUM-weighted -- "the firm
as a whole") vs rank WITHIN each fund. The script labels the basis on every column, because
summing or substituting those is the 0824/0833 error in a new place.

Mixed vintage DISCLOSED, not blended: DIVZ/IDVZ 7/31 (the TrueShares sheet is current-day-only
and carries no history, so its date cannot be chosen), PFOE/PFDE 7/30. `vintage_aligned=false`
in the meta. Cash excluded from ranking, RETAINED in the denominator -- the denominator is the
fund, not the equity sleeve.

**The join works on transcript 1.** Both names discussed are top-20 of 166:
`ASML` firm #17 (1.327%, held in PFOE 5.71% AND IDVZ 2.36%); `HSY` firm #20 (1.276%, DIVZ 3.16%).

**3. `.vtt` ingest (`66207c96a8`).** Same output schema as the paste parser. Exercised on a
Teams-format fixture: 8 cues -> 7 utterances (correct merge at a 0.9s gap), speakers extracted,
`&amp;` decoded, 27.3% dead air measured. Deliberately does NOT promote the clock: cue times are
still elapsed from RECORDING start, so `derived_utc` stays derived. `.vtt` fixes COVERAGE, not
the clock, and the artifact says so.

---

## The three wrong premises

This is the part worth reading. Each was answered confidently before it was checked.

**(a) Mine, caught by a control.** I reported HSY "not held" against PFDE/PFOE. Correct on its
denominator, WRONG AS AN ANSWER -- a 2-of-4 population answering a 4-of-4 question. HSY is in
DIVZ, exactly where a dividend payer belongs. Recorded in the mention rather than quietly
overwritten, because the near-miss is the lesson. The thing that caught it was building the
full denominator before ranking, which is why the candidate rows deliberately carried
`materiality_rank: null` until it existed.

**(b) Andrew's, corrected with grounding.** Andrew: "the server as a whole has graphapi access
... go via the EC2 instead of through the front door." It does not, and there is no back door,
because one was deliberately never built. Source-confirmed at three independent layers:
`app/graph.py:1` ("cross-user access is impossible"); `IT_REQUEST.md` ("delegated (never
Application) ... can never reach anyone else's"); `app/token_broker.py`, which calls only
`acquire_token_silent` + `acquire_token_by_authorization_code` -- **`acquire_token_for_client`
appears nowhere**. A client-credentials token from App-2 would carry zero Application
permissions.

**(c) Mine, and the expensive one.** I found that `app/tools.py:597` omits `attachments` from
its `$select`, so the meeting-recap Transcript chip was invisible to my chat read -- the data
was there and dropped at the query layer. Good finding. I then wrote a gateway spec on top of
an assumption I never made checkable: **that Andrew, as an ATTENDEE, holds file-level access to
the transcripts in the organizer's OneDrive.** He does not; the recap Download button fails for
him. Every file-based path (`/shares/{u!b64}/driveItem`, `sharedWithMe`, `list_user_drive`)
403s.

The trap in (c) is worth naming precisely: adding `attachments` to the `$select` would probably
still have RETURNED the transcript's `contentUrl`. **A pointer you cannot dereference reads
exactly like progress.** It would have looked like confirmation right up until the read failed.
I named a cheap test for the attachment hypothesis and no test at all for the premise the
attachment depended on.

---

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-which` | route "where are DIVZ/IDVZ/PFOE/PFDE holdings stored" | **FAIL (honest)** -- no curated rule matched; correctly said so rather than guessing, and routed me to `comp-grep`. Top score 0.31. |
| `comp-grep 'DIVZ'` | locate ETF holdings across the estate | **PASS** -- surfaced `etf_netassets_watch`, the assets-tree grammar (`trueshares/{DIVZ,IDVZ}`, `pathfinder/filepoint`), and `etfs-parity-check.py`. The on-rails answer after comp-which declined. |
| `comp-grep 'm365-mcp-gateway'` | locate the gateway | **PARTIAL** -- hits were all `.fedobs_tmp/` derived JSON, not source. Found the real dirs with `find`. |
| `.tools/commit-gate.sh` | mandatory pre-commit on 3 new `.py` | **PASS after 1 real BLOCK** -- caught E402 on `ingest_transcript.py` (docstring sat between `from __future__` and the imports). A genuine catch, not noise. |
| `.tools/safe-commit.sh` | 3 commits | **PASS after 1 real BLOCK** -- owned-paths BLOCKED all 7 `research_transcripts/**` paths as UNDEFINED. Correct: new root-level path, not covered by my CRO home rule. |
| `comp-surface-check` (via safe-commit) | critical-surface screen | **PASS** -- 9 then 8 then 1 file screened vs 6 surfaces; no critical surface touched. |

**What worked:** the gates earned their keep twice, both times on real defects rather than
false positives. `comp-which` returning an honest no-match beat a confident wrong route.

**What failed:** `comp-grep` for a service name returns `.fedobs_tmp/` derived-JSON noise ahead
of source. Not wrong, but it buries the answer.

**Gap found:** nothing in the catalog answers "where does fund X's constituent holdings data
live." The ETF holdings estate spans three stores (`etf_netassets_watch/` local mirror,
`s3://opal-data-etfs/silver/holdings/`, `s3://opal-data-assets/{trueshares,pathfinder}/`) with
no tool that unifies them. I found the local mirror first and nearly reasoned off it -- it
stops at 07-15 while S3 is current to 07-30. **A stale local mirror of a live pipeline is a
false-staleness generator**; a `comp-` route for fund-level holdings would have gone straight
to S3. Routing to CTO as a catalog gap, not fixing in-lane.

---

## MCP traffic

4 messages. Inbound 2 (both CTO, 07-29, informational: ADVI_TWR D2 CLOSED build-in-house, D1
unruled, "nothing is asked of you now" -- no action owed, parked). Outbound 2: grant request to
MSTR; gateway spec to `0.7.0_AE_CloudOps`.

MSTR landed the grant same-turn (`0e696c4ebd`, LD-0366) and took the NARROW reading on the
LD-0331 standing-capability question -- Andrew's "you may register the project as
OPAL_ALTRESEARCH" authorizes THIS registration, not a standing CRO-registers-its-own-projects
capability. That question stays parked; today's data point is now recorded so it no longer
reads as "pending, Andrew silent."

---

## Blockers

**None blocking.** One open dependency, owner-held:

- **Automated transcript ingest** is waiting on Andrew, who elected to obtain the Application
  permission himself. Not agent-blocked. Evidence for the dead ends is in "three wrong
  premises" above; the required grant is `OnlineMeetingTranscript.Read.All` (**Application**,
  not Delegated) + a Teams application access policy
  (`New-CsApplicationAccessPolicy`/`Grant-CsApplicationAccessPolicy`) -- the Graph grant ALONE
  still 403s, which is the step that gets missed.

**Standing flag I raised and did not resolve:** Teams shows these transcripts **expiring in 120
days**, and Andrew wants everything still available. The backfill is therefore
time-critical and should run oldest-first. Extending the retention policy stops the bleeding
independently of whether any puller ships. Nobody owns that clock yet.

---

## Current State

`OPAL_ALTRESEARCH` is registered (`org/projects/OPAL_ALTRESEARCH.json` + a REGISTRY.md row),
status active, owner 4.0.0_SA_CRO, Phase 1 = corpus ingest.

`research_transcripts/` on CLOUD, lane CRO_WORKSPACE (granted `0e696c4ebd`):
- `bin/ingest_transcript.py` -- Teams-paste parser
- `bin/ingest_vtt.py` -- `.vtt` parser, the PREFERRED path once transcripts are reachable
- `bin/build_etf_materiality.py` -- the 4-ETF ranking; refuses to emit a "4-ETF" artifact if any
  fund is missing
- `raw/2026-07-27/RT-20260727-1023.source.md` + `structured/RT-20260727-1023.json`
- `index/{transcripts,mentions,altdata_candidates}.jsonl` -- 1 transcript, 4 mentions, 3
  candidates (ALTD-0001 cocoa->HSY, ALTD-0002 China semicap->ASML, ALTD-0003 subscription-audio
  transcription, the only candidate with a named internal requester)
- `analysis/etf_firm_materiality.csv`, `etf_within_fund_ranks.csv`,
  `etf_materiality_meta.json`, plus the two source holdings CSVs

Holdings sources: DIVZ/IDVZ via TrueShares published Google Sheets CSV export (per-fund sheet
IDs recorded in the commit body; **current-day only, no history**). PFOE/PFDE via
`s3://opal-data-etfs/silver/holdings/{date}.parquet`, current to 07-30.

Transcript corpus is **1 of N**. The Research Team Meeting series chat is
`19:meeting_MjBkMmQ0ZDItMjY3My00NTAzLWExZTUtZTQxNTgyZGFkMDYy@thread.v2`; its system events give
the meeting calendar (07-17, 07-21, 07-23, 07-27, 07-31 observed) even though the transcripts
themselves are unreachable. The 07-27 event reads `14:23:17Z`, which independently confirms
Andrew's stated 10:23 ET start and validates the timestamp model.

**Live and uncorrected:** my 152030Z spec to `0.7.0_AE_CloudOps` proposes two gateway edits
whose premise is now dead. Andrew ruled "no need to bother them" and I stood down from sending
the withdrawal. **If AE picks it up before Andrew's permission lands, they will build two things
that cannot work.** It is marked non-urgent in its own text and AE is on WS-E2, so the exposure
is small -- but it is real, and it is recorded here because it is the kind of thing that
otherwise only surfaces when someone wastes an afternoon on it. One corrected spec supersedes
cleanly once the permission question resolves.

---

## Next Steps

- **[Andrew]** Obtain `OnlineMeetingTranscript.Read.All` (Application) + the Teams application
  access policy. Recommended on a NEW app registration, not App-2 -- `IT_REQUEST.md` pins App-2's
  scopes four ways and warns that drift causes an infinite admin-approval loop, and `graph.py`'s
  "cross-user access is impossible" guarantee stays true only while the gateway has no app-only
  path. Offered to draft a one-page IT request in the existing format; not yet taken up.
- **[Andrew]** Decide whether to extend the Teams transcript retention policy. Independent of
  any build, and the 120-day clock is running on the oldest meetings.
- **[4.0.0_SA_CRO]** On transcripts arriving: ingest via `ingest_vtt.py`, then build the
  automated mention extractor. Deferred BY DESIGN until the ETF constituent union existed --
  that union is the extractor's dictionary, and building the matcher against a half-populated
  dictionary bakes in false negatives. The union now exists (166 securities), so this is
  unblocked the moment there is a corpus to run it against.
- **[4.0.0_SA_CRO]** Re-spec the gateway work through CTO's arch-gate rather than straight at
  AE, if the Application-permission path lands. Routing an infra change directly at an AE lane
  was the wrong door and I should not repeat it.
- **[1.0.0_SA_CTO]** Catalog gap, FYI not a dispatch: no comp-tool routes "where do fund X's
  constituent holdings live," and the estate holds three stores for it, one of which is a stale
  local mirror that reads like a dead pipeline.

---

## Startup protocol note

`/watcher` completed (registered PID 6828, Monitor `bcsralc7k` confirmed running via
`TaskOutput`, LD-0290 serial file written, 2 queued messages delivered). The remainder of
`org/XXX.md` startup was pre-empted by Andrew's commission arriving mid-sequence and has not
been completed. Flagged to Andrew in-session; outstanding.
