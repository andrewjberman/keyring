# NFRA_TRNSPT decomposition -- ROUND 1 (2026-09-30, issuer 2.0.0_SA_COO~T)

Cut on the ratified PRD `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.1 @3a6e3dad13, ADMITTED
(ratified-text half 3.0.0_SA_CVO @12880e7f00; brief half auto, the CRO wrote the brief). Notifier 1.0.0_SA_CTO msg 103228.
Seat brief `org/tier1_exec/1.0.0_SA_CTO/deliverables/SEAT_BRIEF_COO_T_NFRA_TRNSPT_20260930.md` @194a27ce43.

**Round 1 is TWO THREADS under ONE issuer** (PRD section 5: a workstream is a scope, not a round; PRD provenance: "the
transcripts thread and the communications workstream run in parallel"). TRANSCRIPTS: the FWD-1 thread, PRD section 2 hops
1-6. COMMUNICATIONS: the FWD-7 thread in test, the CRO's v3 section 9 shape (PRD section 3, communications items 1-5).
The two scopes hold disjoint write surfaces: `data/transcripts/scripts/teams/` and `infra/aws/terraform/transcripts/pull.tf`
against `data/transcripts/scripts/outlook/`, `data/transcripts/assets/` and the registry rows.

**Andrew-direct words carried into every face that touches them (verbatim, records cited):**
- "just create an s3 bucket, opal-data-transcripts and house it there encrypted" (2026-09-29, `ANDREW_DIRECT_20260929_19xxZ_TRANSCRIPTS_HOME_S3_BUCKET_OPAL_DATA_TRANSCRIPTS.md`); readers are two accounts.
- "Bronze is agreed. Silver is typed and deduplicated bronze in parquet with PII wiped. Gold is when we first run Alyssa's schema." (`ANDREW_DIRECT_20260930_020xZ_...`).
- "I'm sure you could download a lib of all names and just include that as a utility/service for the script." (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_03xxZ_TRNSPT_OPEN_CALLS_ANSWERED_TICKET_CENTER_OWN_INGESTION.md`, call 2) -- the word for the name-list download in `TR-a-1`.
- "for now we just need to wing it through my account" (`ANDREW_DIRECT_20260930_04xxZ_..._GRAPH_PERMISSIONS_...`, message 4) -- the route is the existing gateway under Andrew's account.
- "Make it a recorded attribute as well." (same record, addendum) -- the client-domain test is an attribute, never a gate.
- "For testing sake, let's just use my email for the fetching." (`ANDREW_DIRECT_20260930_020xZ_...`) -- test fetches read andrew@opalinvest.com only.

## The rectangle (round 1)

| cell | hop / item | surfaces (PRD section 7) | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `TR-t-2` | hop 3: the bronze lander -- raw WebVTT, metadata WebVTT and sidecar land byte for byte at the builder's address, never overwriting, idempotent on identical bytes | S01 (consumed), S03 (its landing half) | FWD-1 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `TR-t-1` | hops 1-2: the pull job -- enumerates each series by meeting id through a gateway client, lands what is new via `TR-t-2`, writes a run record; the gateway transport is a stub against the spec until site Z lands the tools (S04) | S03, S04 (consumed), S05 (consumed) | FWD-1 | NOT-EVALUATED | laptop | LOCAL | worker | TR-t-2 |
| `TR-i-1` | hop 1's clock and the writer principal, DESIRED ONLY: Lambda, role with key use, EventBridge schedule, in Terraform; `plan` clean; NO apply this round | S03 (its schedule half), S01 | FWD-1 | NOT-EVALUATED | laptop | WORLD | worker | TR-t-1 |
| `TR-t-3` | hop 4: bronze to silver -- one meeting's speaker turns as parquet with wall-clock times from the metadata WebVTT; real run on one held Monday meeting | S06 | FWD-1, FWD-5 | NOT-EVALUATED | laptop | SERVED | worker | -- (reads bronze objects that already exist) |
| `TR-t-4` | hop 5: the reader route -- a seat-shell CLI over silver prints who said what, in order; NOT-HELD with a cause when a meeting is absent | S06 (reader half), S21 (Andrew's route, round-1 form) | FWD-1, FWD-5 | NOT-EVALUATED | laptop | SERVED | worker-light | TR-t-3 |
| `TR-t-5` | hop 6: the thread trace -- hops 3-5 run end to end on one real meeting by a script, per-hop timestamps, a negative arm, no person | S22 (FWD-1 part) | FWD-1 | NOT-EVALUATED | laptop | SERVED | worker-light | TR-t-4 |
| `TR-g-1` | comm item 1a: registry rows `outlook` and `sharepoint` in `infra/logic/registry/systems.json`; `validate` passes; the generated targets regenerated at the new registry hash | S02 | FWD-6, FWD-7 | NOT-EVALUATED | laptop | WORLD (the gate's path floor for `infra/`; nothing applied) | worker-light | -- |
| `TR-b-1` | comm item 2: the mail criterion and the bronze landing of Andrew's mailbox under today's gateway tools -- replay-fed; the daily pull's gateway transport is a stub until the headless mail route exists (S12) | S10, S11, S13 | FWD-7 | NOT-EVALUATED | laptop | SERVED | worker | TR-g-1 |
| `TR-a-1` | comm item 1b: the versioned, hash-pinned data assets -- author table, client-domain table, model alias table, name dictionary, allowlist | S09 | FWD-7 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `TR-w-1` | comm item 3: silver with the PII wipe; the planted-token test is the gate (C-WIPE-GATE) | S14 | FWD-7 | NOT-EVALUATED | laptop | SERVED | worker | TR-a-1 (bronze shape from this file's contract, not from TR-b-1's drain) |
| `TR-k-1` | comm item 4: the gold contract file and the first gold derivation on the C-GOLD-FIELDS schema | S15 | FWD-7, FWD-10 | NOT-EVALUATED | laptop | SERVED | worker | TR-w-1 |
| `TR-q-1` | comm item 5: the slicer as a tested Python function over gold, run over a REPLAY of past Generate compositions; no AI, no live trigger | S16 | FWD-10 | NOT-EVALUATED | laptop | LOCAL | worker | TR-k-1 |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED (NOT-EVALUATED is the value before a cell's instance exists).

**Chains (M = 4, one worker each; fan-out 4 of 4, cap 8).**
- A = TR-t-2 -> TR-t-1 -> TR-i-1 (slot ~1: the lander is the job's dependency; the handler wraps the job).
- B = TR-t-3 -> TR-t-4 -> TR-t-5 (slot ~2: the reader reads the parse's silver; the trace runs both).
- C = TR-g-1 -> TR-b-1 (slot ~3: `address('outlook', ...)` refuses until the row exists -- measured at the cut, `ValueError source 'outlook' is not a systems.json key`).
- D = TR-a-1 -> TR-w-1 -> TR-k-1 -> TR-q-1 (slot ~4: the wipe consumes the assets; gold consumes silver; the slicer consumes gold).
- The cross-scope seam TR-b-1 -> TR-w-1 (real bronze into the real wipe) is NOT an edge: TR-w-1 builds against the BRONZE CONTRACT below and the seam is proved at the drain by the issuer's real run.

**Write sets (disjoint; every `__init__.py` and `data/transcripts/README.md` are created by the issuer at the cut, so no cell writes them).**
- TR-t-2: `data/transcripts/scripts/teams/land_bronze.py`, `data/transcripts/scripts/tests/test_teams_land_bronze.py`.
- TR-t-1: `data/transcripts/scripts/teams/pull.py`, `data/transcripts/scripts/teams/gateway_client.py`, `data/transcripts/scripts/teams/series.json`, `data/transcripts/scripts/tests/test_teams_pull.py`, `data/transcripts/scripts/tests/fixtures/teams_pull/`.
- TR-i-1: `infra/aws/lambda/transcripts-pull/handler.py`, `infra/aws/lambda/transcripts-pull/build.sh`, `infra/aws/terraform/transcripts/pull.tf`, `data/transcripts/scripts/teams/NAMES.json`, `data/transcripts/scripts/tests/test_pull_handler.py`.
- TR-t-3: `data/transcripts/scripts/teams/parse_silver.py`, `data/transcripts/scripts/tests/test_teams_parse_silver.py`, `data/transcripts/scripts/tests/fixtures/teams_vtt/` (SYNTHETIC cues only).
- TR-t-4: `data/transcripts/scripts/teams/read_meeting.py`, `data/transcripts/scripts/tests/test_teams_read_meeting.py`.
- TR-t-5: `data/transcripts/scripts/teams/thread_trace.py`.
- TR-g-1: `infra/logic/registry/systems.json` and the generated targets `python lib/opal_naming.py targets` lists (named on its face).
- TR-b-1: `data/transcripts/scripts/outlook/criterion.py`, `data/transcripts/scripts/outlook/land_bronze.py`, `data/transcripts/scripts/outlook/pull.py`, `data/transcripts/scripts/tests/test_outlook_bronze.py`, `data/transcripts/scripts/tests/fixtures/outlook_replay/` (SYNTHETIC messages only).
- TR-a-1: `data/transcripts/assets/` (every file), `data/transcripts/scripts/tests/test_assets_lock.py`.
- TR-w-1: `data/transcripts/scripts/outlook/wipe.py`, `data/transcripts/scripts/outlook/silver.py`, `data/transcripts/scripts/tests/test_wipe_planted.py`, `data/transcripts/scripts/tests/test_outlook_silver.py`.
- TR-k-1: `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json`, `data/transcripts/scripts/outlook/gold.py`, `data/transcripts/scripts/tests/test_outlook_gold.py`.
- TR-q-1: `data/transcripts/scripts/outlook/slicer.py`, `data/transcripts/scripts/outlook/replay.py`, `data/transcripts/scripts/tests/test_slicer.py`.
- Hookups the issuer adds at the merge: none expected; a `requirements` line or a README pointer if a cell's report names one.

**Code home (this round's ruling, the issuer's; PRD section 4 engines).** Source lives at `data/transcripts/scripts/` (the estate's `data/<pipeline>/scripts/` form, CLAUDE.md rule 13), one package per SOURCE (`teams/`, `outlook/`), tests beside them. The Lambda handler and its Terraform live under `infra/aws/` (deployable plane, AE lane at apply). Every S3 address is `lib.opal_naming.address()` output and every resource name `name()` output (rule 30). Round-1 simplification, ruled here and listed as enrichment: the pull job runs the silver parse IN-PROCESS after landing (one scheduled job, hops 1-4), and the event-triggered bronze-to-silver Lambda of PRD section 4 is a round-2 item. The addresses measured at the cut:
- `s3://opal-data-transcripts/teams/transcripts/bronze/<series>/date=YYYY-MM-DD/<ID>.vtt|.metadata.vtt|.graph.json` (91 objects held; 30 transcripts x 3, plus `_provisioning/probe-20260929.txt`).
- `s3://opal-data-transcripts/teams/transcripts/silver/<series>/date=YYYY-MM-DD/<ID>.parquet`.
- `s3://opal-data-transcripts/teams/transcripts/state/pull_runs/run=<ISO>/run.json` (R21: workflow state is the fifth class).
- names: `name('teams','global','transcripts-pull','lambda')` -> `teams-global-transcripts-pull-lambda` (a PRODUCT scope is refused in the scope slot; the product rides the function slot; the system is the source vendor `teams`).

**BRONZE CONTRACT, analysis_commentary, round 1 (what today's gateway tools return; measured 2026-09-30 13:4xZ on one real message).** `read_email(id)` returns Graph `{id, subject, from, toRecipients, receivedDateTime, body{contentType:html, content}}` -- the RAW HTML body is present; `internetMessageId`, `ccRecipients`, `conversationId`, `sentDateTime` are ABSENT. `list_email_attachments(id)` returns `{id, name, size, contentType, isInline}` per attachment, no bytes. So:
- partition `date=<receivedDateTime UTC date>` (v3 says sent date; `sentDateTime` is not returned today -- stated limit, enrichment when the tools land);
- objects: `msg_<rid16>.json` = the `read_email` result exactly as recorded; `msg_<rid16>.attachments.json` = the `list_email_attachments` result exactly as recorded; `msg_<rid16>.sidecar.json` = `{record_id, id_source: "fallback", graph_id, received_at, pulled_at, run_id, mailbox: "andrew@opalinvest.com", tool_versions, sha256: {message, attachments}, criterion: {sender_ok, client_recipient, ycharts_pdf, ycharts_basis: "heuristic:name-size-body", trade_update_excluded, recipient_firm}}`;
- `record_id` = sha256 of `lower(from.address) | receivedDateTime | subject | sha256(body.content)`, `rid16` its first 16 hex, `id_source=fallback` on every row until the tools return `internetMessageId` (C-DEDUP);
- attachment bytes are NOT landed this round (no download tool; C-GATEWAY-TOOLS); `ycharts_pdf` is the heuristic: a non-inline `application/pdf` of 300 KB or more, or body words `YC report`/`YChart`, basis recorded.
- The daily pull needs a headless gateway mail route (site Z). Round 1's real run is a RECORDED SAMPLE: the issuer records `search_email` (date-sliced, `from:manav` / `from:yang` `hasattachments:true`) + `read_email` + `list_email_attachments` results verbatim into a replay directory and lands them with `pull.py --replay <dir> --apply`. The full dredge back to October 2025 is enrichment behind the tools.

**Release order and the issuer's real runs at close (after the cells drain).**
1. Transcripts: `TR-t-5`'s trace on the Monday meeting `MM-20260928-0858` (hops 3-5, no person) is the FWD-1 round-1 exercise; hops 1-2 wait on S04/S05 (site Z) and `TR-i-1`'s apply, which is a release act under CTO+COO halves with a change-management entry, not this round.
2. Communications: the recorded sample lands to bronze (`TR-b-1`), then silver (`TR-w-1`) only after the planted-token test passes, then gold (`TR-k-1`), then the slicer replay (`TR-q-1`) over the real gold rows. No Kimi call this round (C-KIMI: first call only after C-WIPE-GATE and Andrew's word, round 2).
3. The `TR-g-1` restamp is named to `2.0.0_SA_COO~P` and `~M` before its drain lands (CTO placement precedent `CTO_PLACEMENT_20260929_170xZ_TRANSCRIPTS_BUCKET_LANDING.md` step 1: a restamp moves blob hashes signed packets pin).

**Owned elsewhere, named here and NOT built (PRD section 5).** S04 transcript tools and a headless transcripts route, S05 stored-sign-in lifetime, S12 the three mail tools plus a headless mail route: `NFRA_OPLGTW` (site Z) via the CTO's relay (the issuer's one L6 message). OBSERVED at the cut: laptop worktrees `wt-gw-f2`, `wt-gw-f3`, `wt-gw-int` carry UNCOMMITTED gateway mail-tool work (`app/tools.py`, `data_entitlement.py`, `destructive_ops.py`, `tests/test_list_email_filtered.py`, `tests/test_inspect_email_attachment.py`) by seats not relaunched after the 07:52Z reboot -- row `NFRA_TRNSPT-S1`. S18 the READY hook (IRPT_BCKEND) and S20 the ticket work (D7) are round-2 asks, not needed by any round-1 cell.

**Not in round 1 (enrichment backlog, PRD section 3):** transcripts items 1-6 (Research Meeting refusal, the other archetypes' unattended pull, backfill, the completeness table, the 29 repository transcripts, the second reader); communications items 6-8 (FWD-6 market updates -- NOTE for round 2: Manav emails a weekly "Market Update" with an attachment, measured 2026-09-30, so mail may be a live source beside SharePoint; the Kimi call, ticket write, READY hook, D7; FWD-9). Also: the event-triggered silver Lambda; `sentDateTime`/`internetMessageId`/attachment bytes when the tools land; the full dredge.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: PRD section 2 hops 1-6 (six) plus PRD section 3 communications items 1-5 (five) = eleven members. By subtraction: hop 1 splits into the job (TR-t-1) and its clock and principal (TR-i-1); hop 2's adapter on this side is the job's gateway client (TR-t-1) and its other half is S04, owned elsewhere; hop 3 = TR-t-2; hop 4 = TR-t-3; hop 5 = TR-t-4; hop 6 = TR-t-5; item 1 splits by write set into the registry rows (TR-g-1) and the data assets (TR-a-1); item 2 = TR-b-1; item 3 = TR-w-1; item 4 = TR-k-1; item 5 = TR-q-1. Remainder: none. The manifest rows not in round 1 are S07, S08, S17, S18, S19, S20, and S21/S22 beyond their round-1 parts.
- **Same grain.** One cell per hop adapter or per placed item; where one member has two write sets it is two cells, never one cell over two files another cell writes.
- **Intent coherence.** `t` cells move the Monday meeting one hop; `i` is the clock and principal, desired only; `g`/`a` are records and data; `b`/`w`/`k`/`q` move the mail sample one tier each.
- **State coherence.** No cell applies Terraform, grants a principal, deletes an object, calls a vendor model, sends mail, or creates an alarm. No cell writes a tier another cell of the round writes. A silver or gold write moves nothing served today (no reader of these tiers exists yet); the real bronze write of the mail sample is the issuer's act at the drain.

## Battery (round 1 of a threaded project)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. Thread round; the pull schedule is DESIRED in `TR-i-1`'s Terraform and applied on a later release under halves. Cadence chosen there: hourly 13:00-22:00Z Mon-Fri (the Monday meeting ends about 13:50Z; FWD-1 ACCEPT is "the same day").
- `comp-iam`: RUN, because the thread touches IAM.
  - Measured: `infra/aws/terraform/transcripts/main.tf` grants key USE to `var.reader_principal_arns`, default `arn:aws:iam::313476888478:user/Andrew_Berman` only; the account root administers and cannot use; every PutObject must carry the transcripts key (bucket policy `DenyAWriteUnderAnyOtherKey`).
  - Consequence: any principal that writes bronze or silver needs key use. This round's real runs are executed by the issuer's seat shell under Andrew's own AWS identity (the one grantee), so nothing is granted. `TR-i-1` DRAFTS the writer role's key use as a third principal (C-READERS: "a pipeline role that WRITES is a third principal and is named in the round's halves") -- desired, unapplied.
  - Blind: whether the gateway's instance role will need key use for the second reader (route A of `TRANSCRIPTS_READER_PRINCIPAL_20260929.md`) -- round 2, FWD-8.
- `comp-adversary`: DECLARED-NOT-APPLICABLE. Thread round. Findings read at the cut and inlined into the faces:
  - The Research Meeting is refused (403, 3003) for Andrew as invitee; the other three series list and read (first pull 2026-09-29, 30 of 34 landed, 4 expired). The pull fixture carries one refused series and one expired row so both outcomes are typed.
  - The metadata WebVTT carries per-cue wall-clock `startDateTime`/`endDateTime` and `speakerName` as JSON; the content WebVTT carries `<v Speaker>` tags. Silver takes wall-clock from the metadata file (OBSERVED), never derived from an operator-stated start (the `research_transcripts/` README's three-clock trap).
  - The 09-29 sidecar (`MM-20260928-0858.graph.json`) is the shape `TR-t-2` reproduces: `transcript_id, archetype, teams_subject, organizer, source, graph{meetingId,id,createdDateTime,endDateTime}, content{object,bytes,sha256,cues,speaker_tagged_cues,distinct_speakers,last_cue_end}, metadata_content{object,http,bytes,sha256}, id_clock, pulled_utc, pulled_by`.
  - `read_email` returns no `internetMessageId`/`ccRecipients`/`conversationId`/`sentDateTime` (row `NFRA_TRNSPT-S2`); one real Manav-to-client reply (2026-09-23) carried four non-inline PNG charts and no PDF -- a near-miss the criterion must record, not ingest.
  - `name()` refuses a PRODUCT scope in the scope slot; the accepted form is measured above.
  - The three non-research archetypes never land in the git repository (spec 9.4; `research_transcripts/schema/series.json` `repo_store_allowed:false`): every test fixture in this round is SYNTHETIC and every deliverable carries counts and keys, never cue or email text.
