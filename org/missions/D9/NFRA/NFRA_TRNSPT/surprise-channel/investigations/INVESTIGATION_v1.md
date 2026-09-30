# NFRA_TRNSPT -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~T` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_TRNSPT-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_TRNSPT-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_TRNSPT-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
{
  "id": "NFRA_TRNSPT-S1",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~T",
  "surfaced_at": "2026-09-30T13:35:00Z",
  "one_line": "The three gateway mail tools the PRD names as NFRA_OPLGTW's (site Z) build are being built UNCOMMITTED in laptop worktrees wt-gw-f2, wt-gw-f3 and wt-gw-int by seats (4.0.0_SA_CRO~T / 0.7.0_AE_CloudOps) that the 2026-09-30 07:52Z reboot killed and the relaunch word did not restart.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO (owns the S12 relay to site Z and the seating of the laptop gateway work; this seat only surfaces)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C C:/Users/AndrewBerman/Desktop/wt-gw-f2 status --porcelain (2026-09-30 13:2xZ): M app/data_entitlement.py, M app/destructive_ops.py, M app/tools.py, M tests/test_entitlement_admin.py, ?? tests/test_list_email_filtered.py",
      "git -C C:/Users/AndrewBerman/Desktop/wt-gw-f3 status --porcelain: M app/data_entitlement.py, M app/destructive_ops.py, M app/tools.py, ?? tests/test_inspect_email_attachment.py",
      "git -C C:/Users/AndrewBerman/Desktop/wt-gw-int status --porcelain: three files staged (M in the index), nothing committed; branch gw-mail-tools-int at 2ab90bf162 = CLOUD",
      "org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md: 'wt-gw-f1 / f2 / f3 / int -- gateway mail tools (CRO~T / CloudOps)'; neither seat is in the relaunch table",
      "PRD C-GATEWAY-TOOLS (org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:110): the three tools are NFRA_OPLGTW's (site Z), requested through MSTR's bus at L6"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The attachment-download tool, the filtered paged mail list and ccRecipients are built by NFRA_OPLGTW on site Z; this project does not build them.",
  "world_is": "Uncommitted implementations of at least the filtered list and an attachment inspector sit in three laptop worktrees whose owning seats are dead; nothing on CLOUD carries them; site Z's state is unread from this seat.",
  "notes": "Not touched by this seat (a worktree with uncommitted work is never removed; COO_STARTUP.md worktree-wipe edict). The L6 relay to the CTO names the worktrees so site Z and the laptop do not build the same tools twice."
},
{
  "id": "NFRA_TRNSPT-S2",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~T",
  "surfaced_at": "2026-09-30T13:48:00Z",
  "one_line": "The deployed gateway's read_email returns the raw HTML body but no internetMessageId, ccRecipients, conversationId or sentDateTime, so C-DEDUP's primary key cannot be computed this round and every round-1 mail row carries id_source=fallback.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~T (round-1 bronze contract in the decomposition uses the fallback id; the primary key rides the S12 tools)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcp opalgateway read_email on message AAMkAGJl...fhTyRAAA= (2026-09-30 13:4xZ, as Andrew@opalinvest.com): keys returned = @odata.context, @odata.etag, id, receivedDateTime, subject, body{contentType:html, content}, from, toRecipients",
      "mcp opalgateway list_email_attachments on the same message: per attachment id, name, size, contentType, isInline; no contentBytes; four non-inline image/png charts, zero PDFs",
      "PRD C-DEDUP (org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:112): record_id = sha256(internetMessageId); fallback = hash of (sent_at, sender domain, subject, body hash) flagged id_source=fallback"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "record_id = sha256(internetMessageId); conversationId groups threads; partition by sent date.",
  "world_is": "Today's tool exposes none of those three fields; the round-1 contract partitions by receivedDateTime and derives the id from sender, receivedDateTime, subject and the body hash, flagged fallback on every row.",
  "notes": "Also observed: the v3 brief's claim that raw HTML needs a NEW gateway call is not so -- body.content is the raw HTML; the cut rules (Signature, appendonsend, divRplyFwdMsg, the 49 compliance boilerplate) are visible in it."
},
{
  "id": "NFRA_TRNSPT-S3",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~T",
  "surfaced_at": "2026-09-30T14:45:00Z",
  "one_line": "All 12 generated naming targets at CLOUD HEAD are stale: stamped registry@5576b01fd4684bfa while infra/logic/registry at HEAD hashes ffa41913935c3281, so a `python lib/opal_naming.py generate --out .` moves every target before NFRA_TRNSPT adds a row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO (the registry lane's owner decides who restamps; round-1 cell TR-g-1's regenerate will carry the restamp for its own rows and the issuer names it to 2.0.0_SA_COO~P/~M before the drain)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_registry_check.py targets at HEAD a7a6d286f2+ (2026-09-30 14:4xZ): TARGETS-STALE n=12 moved=[all 12]; git diff --stat: 11 workspace files, 12 insertions 12 deletions, each a GENERATED stamp line only; the portal target moved likewise (10-line diff)",
      "data/firm_registry.json:2 at HEAD: '_generated ... registry@5576b01fd4684bfa'; regenerated: 'registry@ffa41913935c3281'",
      "git log -- infra/logic/registry/: 0146e0c954 (2026-09-30 06:48Z, MSTR merge of origin/CLOUD 33c1d096a3, 1460 site Z commits) and d451070fb1 (4.0.0_SA_CRO~Z, rivalfunds row) postdate the last target regenerate f13d9e9222 (2026-09-29 20:10Z)",
      "the tree was restored to HEAD's bytes with git restore after the dry-run; nothing of this drift is committed by this seat"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Every generated target is byte-identical to what the registry at HEAD produces (LGIC_ENFORCE: per-view registry hashes, 39cbad4214).",
  "world_is": "The 12 targets carry the pre-merge registry hash; the site Z registry change landed without a laptop regenerate, and no gate refused the merge.",
  "notes": "Blast radius per CTO placement 2026-09-29 step 1: a restamp moves blob hashes that signed IRPT packets pin; the issuer names TR-g-1's drain to ~P and ~M first. Whether a merge-time gate should regenerate is the CTO's, not this project's."
},
{
 "id": "NFRA_TRNSPT-W1-S1",
 "project": "NFRA_TRNSPT",
 "fabric": "laptop",
 "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~1",
 "surfaced_at": "2026-09-30T15:05:00Z",
 "one_line": "safe-commit's missions-tree-index check refuses the TO-TR-t2 complete flip on an INDEX-DRIFT it did not cause: org/projects/NFRA_TRNSPT.json says dep_stage PRD at CLOUD HEAD 81e350ba0a while the tree project.json says EXECUTING.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "disarm_owner": "2.0.0_SA_COO~T (its uncommitted org/projects/NFRA_TRNSPT.json edit PRD -> EXECUTING sits modified in the main worktree; committing it, or the drain, closes the drift; the worker's write grant does not include org/projects)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "bash .tools/safe-commit.sh ... -- <TO file> <proof instance> (2026-09-30 ~15:0xZ, worktree wk_nfra_trnspt_1 @adff7d4596): '[INDEX-DRIFT] org/projects/NFRA_TRNSPT.json: dep_stage: index=PRD tree=EXECUTING', RESULT: 1 violation(s), safe-commit did NOT commit (rc=1)",
   "git -C C:/Users/AndrewBerman/Desktop/ajb_workspace diff HEAD -- org/projects/NFRA_TRNSPT.json: dep_stage PRD -> EXECUTING, generated_at 2026-09-30T14:05:26Z, uncommitted in the main worktree"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "The worker's order flips <status> to complete and commits the proof instance, deliverables and flip together (worker standing rules).",
 "world_is": "The commit that stages any org/missions path is refused by the tree/index check on a drift in a file outside the worker's grant; the code commit adff7d4596 (no org/missions path) landed, the proof instance and the flip are written and VALID but uncommitted."
},
{
 "id": "NFRA_TRNSPT-W1-S2",
 "project": "NFRA_TRNSPT",
 "fabric": "laptop",
 "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~1",
 "surfaced_at": "2026-09-30T15:30:00Z",
 "one_line": "TO-TR-t1 criterion 2 names fixture files <meeting_id>.list.json etc., but a real 148-char online_meeting_id makes the path 276 chars, past the Windows 260-char limit: the file cannot be created in a worktree.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "python Path.write_bytes on <wt>/data/transcripts/scripts/tests/fixtures/teams_pull/<148-char id>.MM-20260928-0858.metadata.vtt (2026-09-30 ~15:2xZ): len(path)=276, FileNotFoundError [Errno 2]",
   "data/transcripts/scripts/teams/series.json: 4 of 4 online_meeting_id values are 148 chars"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "FixtureTransport replays <meeting_id>.list.json and <meeting_id>.<transcript_id>.vtt from a directory.",
 "world_is": "Built as specified for any id that is its own file stem, plus a fixtures/teams_pull/index.json ({meeting_id: short stem}) so the four real ids resolve to monday_meeting.list.json etc.; the criterion outputs are unchanged.",
 "notes": "The same length bites any future fixture or object keyed by a raw meeting id on a Windows checkout."
},
{
 "id": "NFRA_TRNSPT-W1-S3",
 "project": "NFRA_TRNSPT",
 "fabric": "laptop",
 "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~1",
 "surfaced_at": "2026-09-30T15:32:00Z",
 "one_line": "The parked gateway spec's read_meeting_transcript has no fmt argument and returns a paged dict, not bytes; it has no metadata-VTT format at all, and it names tools, not routes, so the transport protocol in TO-TR-t1 does not match the spec's tool shapes.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md:51-55 (read at the worktree HEAD): read_meeting_transcript(meeting_id, transcript_id, offset=0, limit=0) -> {content,total_bytes,sha256,offset,returned_bytes,complete}, GET .../content with Accept: text/vtt",
   "the same file 4.1-4.4 and section 5: no call fetches the metadata WebVTT (land_bronze.land requires metadata_bytes)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-TR-t1 item 2: read_meeting_transcript(meeting_id, transcript_id, fmt) -> bytes, fmt in vtt | metadata (spec 4.3).",
 "world_is": "Built as the order states (fmt, bytes) against a fixture; the stub names the spec's tool and Graph route (list: GET /me/onlineMeetings/{meeting_id}/transcripts; read: GET .../transcripts/{transcript_id}/content). When S04 lands, the real GatewayTransport must page by offset/limit, reassemble, check sha256, and the source of the metadata VTT is unspecified.",
 "notes": "Class and disposition are the reporter's form call; whether the spec or the order's shape moves is not this worker's."
},
{
 "id": "NFRA_TRNSPT-W1-S4",
 "project": "NFRA_TRNSPT",
 "fabric": "laptop",
 "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~1",
 "surfaced_at": "2026-09-30T16:20:00Z",
 "one_line": "lib.opal_naming.name() refuses the kinds log-group and secret (and rule), so NAMES.json carries 4 rows (lambda, role, policy, cadence-named EventBridge rule), not the 6 the order lists; the log group and the secret are named by their own grammars and graded by grade().",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "python: name('teams','global','transcripts-pull','log-group') -> \"ValueError: kind 'log-group' is neither a NAMING_SCHEMA.json kind nor a cadence\"; the same refusal text for 'secret' and 'rule' (2026-09-30 ~16:0xZ, wk_nfra_trnspt_1 @9fc353133a)",
   "org/standards/NAMING_SCHEMA.json: kind.values has no log-group/secret/rule; kind.closed_at_l4 says 'secret was DROPPED: secrets keep their own slash-path grammar'; resource.last_slot.EVENT_RULE = cadence; log_group.grammar = /aws/{service}/{resource-name}, derived",
   "name('teams','global','transcripts-pull','hourly') -> teams-global-transcripts-pull-hourly; grade('teams/global/gateway-token','SECRET') -> CONFORMANT; grade('/aws/lambda/teams-global-transcripts-pull-lambda','LOG_GROUP') -> CONFORMANT",
   "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_names_check.py rebuilds every NAMES.json row with name() and would report NAMES-BAD on a log-group or secret row"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-TR-i1 build item 1: a NAMES.json row for the Lambda, its role, its policy, its log group, the EventBridge rule and the gateway-bearer secret, each computed with name(); a refused kind is replaced by the kind the builder admits.",
 "world_is": "Rows: lambda, role, policy (kinds the builder admits) and the EventBridge rule with kind 'hourly' (the cadence the builder admits for an EVENT_RULE). The log group /aws/lambda/teams-global-transcripts-pull-lambda (derived from the lambda name) and the secret teams/global/gateway-token are literals in pull.tf with no NAMES row, because no kind the builder admits fits them and a row would fail the issuer's check.",
 "notes": "The check therefore proves 4 of 6 names; the other two are proved by grade(), whose output is recorded above."
},
{
 "id": "NFRA_TRNSPT-W1-S5",
 "project": "NFRA_TRNSPT",
 "fabric": "laptop",
 "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~1",
 "surfaced_at": "2026-09-30T16:22:00Z",
 "one_line": "The order says python3.12 and the layer pandas-pyarrow-layer:1, but that layer is py3.11-only, so pull.tf declares runtime python3.11.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "infra/aws/lambda/ci/lambda-layer-map.json layers.pandas-pyarrow-layer: python_version '3.11', description 'pandas + pyarrow for data processing (Python 3.11)', latest_version_arn ...:layer:pandas-pyarrow-layer:1",
   "infra/aws/terraform/opal-assets/silver.tf (comment ahead of data.aws_lambda_layer_version.pandas_pyarrow): 'the mirror families run python3.11 -- pinned to pandas-pyarrow-layer (py3.11-only wheels)'"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-TR-i1 build item 3: the Lambda is python3.12 with the layer pandas-pyarrow-layer:1.",
 "world_is": "Built as runtime = python3.11 with the layer read by name via data.aws_lambda_layer_version (the estate's own form), so the two agree. Nothing in the packaged tree needs 3.12; the handler ran from the unzipped dist under local Python 3.12.10. Plan is 9 adds either way.",
 "notes": "Whether the layer is rebuilt for 3.12 or the Lambda stays on 3.11 is not this worker's. Also of note: pull.py imports its siblings as top-level modules, so the handler imports gateway_client and land_bronze top-level too (the package-path copies define different Expired/Refused classes and pull would not catch them)."
}
]
```
