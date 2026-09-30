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
    "id": "NFRA_TRNSPT-W2-S1",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~2",
    "surfaced_at": "2026-09-30T15:00:00Z",
    "one_line": "safe-commit refuses the TR-t-3 complete-flip commit: missions-tree-index check reports INDEX-DRIFT org/projects/NFRA_TRNSPT.json dep_stage index='PRD' tree='EXECUTING' at the worktree base, and the fix is outside the worker's write grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~T (holds the regenerated org/projects/NFRA_TRNSPT.json uncommitted in the shared tree; 0.0.0_AB_MSTR is the integrator fallback for the index carrier)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output 2026-09-30 ~15:0xZ on branch wk-NFRA_TRNSPT-2: '[INDEX-DRIFT] org/projects/NFRA_TRNSPT.json: dep_stage: index=PRD tree=EXECUTING; RESULT: 1 violation(s)'; commit refused rc=1",
        "git -C C:/Users/AndrewBerman/Desktop/ajb_workspace diff org/projects/NFRA_TRNSPT.json: uncommitted dep_stage PRD -> EXECUTING (and generated_at 2026-09-30T14:05:26Z) in the shared tree",
        "git log -1 -- org/projects/NFRA_TRNSPT.json at worktree base 81e350ba0a: 1d8905b007 (the L3 register commit), so the issuance commit flipped the tree row but the generated index was never committed",
        "code commit 80a22d9a89 landed (no org/missions path staged); only the status flip and proof instance commit is refused"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker's complete-flip commit of the task order and its proof instance passes safe-commit (missions-tree-index check 0 violations).",
    "world_is": "The generated index org/projects/NFRA_TRNSPT.json is one dep_stage behind the tree row at the base, so any commit staging an org/missions/D*/ path is refused; the worker's grant excludes org/projects/, and the worker does not bypass or force.",
    "notes": "State left in the worktree, uncommitted: task order <status> flipped to complete, proof instance VALID (rc=0, violations=0), this row. Retry the commit once the index carrier is committed and merged into the branch base."
  },
  {
    "id": "NFRA_TRNSPT-W3-S1",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~3",
    "surfaced_at": "2026-09-30T15:10:00Z",
    "one_line": "safe-commit refuses every commit staging an org/missions/ path (the TO-TR-g1 complete flip, its proof instance, this row) because missions-tree-check reports INDEX-DRIFT org/projects/NFRA_TRNSPT.json dep_stage index='PRD' tree='EXECUTING', a file outside this order's grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... -- <TO file> <proof instance> (2026-09-30 ~15:05Z): 'BLOCKED: missions-tree-check ... [INDEX-DRIFT] org/projects/NFRA_TRNSPT.json: dep_stage: index=PRD tree=EXECUTING; RESULT: 1 violation(s)'; remedy printed: 'R5 = the register's members list, 0.0.0_AB_MSTR's lane; never bypass'",
        "The issuance commit 81e350ba0a moved the tree's dep_stage PRD -> EXECUTING; org/projects/NFRA_TRNSPT.json was not regenerated to match; that file is not in the TR-g1 <paths> grant",
        "Landed and unaffected: registry+targets commit 8e9ed1b539 and nested portal commit d8bad891 (no org/missions path staged, so the check did not run). Uncommitted in worktree: TO status flip to complete, the proof instance (validated rc=0), this row"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~T (issuer) or 0.0.0_AB_MSTR (index regenerate); this worker does not edit org/projects/",
    "spec_asserts": "A worker commits its proof instance and the TO complete flip under its own grant.",
    "world_is": "Any commit staging an org/missions/ path is refused while org/projects/NFRA_TRNSPT.json carries dep_stage PRD against the tree's EXECUTING; all three TR-g1 close-out files stay uncommitted in the worktree until the index is regenerated.",
    "notes": "Every later NFRA_TRNSPT worker order will hit the same refusal on its own proof commit."
  },
  {
    "id": "NFRA_TRNSPT-W3-S2",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~3",
    "surfaced_at": "2026-09-30T15:35:00Z",
    "one_line": "TO-TR-b1 says the inline default carries the three client domains with firm keys 49f / inflection / cottonwood; the commit-time naming gate REFUSED hand-kept firm identifiers in criterion.py, so the default is read from the registry and the first firm key is 49financial, not 49f.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh (build commit, 2026-09-30 ~15:25Z): 'NAMING-GATE: REFUSE 6 graded' at data/transcripts/scripts/outlook/criterion.py:17,19,20,21,85 -- hand-kept carriers of 49financial, 49f, inflection, cottonwood; 'read it through lookup(...)'",
        "infra/logic/registry/scopes.json carries tenant.email_domain for exactly three client scopes: 49financial -> 49financial.com, inflection -> inflectionwealth.com, cottonwood -> cottonwoodmail.com (python: load_registry()['scopes']['scopes'], kind client, 3 of 13 scope rows)",
        "criterion.py now builds DEFAULT_CLIENT_DOMAINS from that read (firm key = the scope key) and the author address manav.shah@<registry domain of the 49financial scope>; recipient_firm for the 49financial domain is '49financial' (scope key), the order named '49f' (that scope's short form). assets/client_domains.json, when present, overrides via its firm_key field."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The inline default carries the three domains 49financial.com (firm key 49f), inflectionwealth.com (inflection), cottonwoodmail.com (cottonwood).",
    "world_is": "Hand-typed firm identifiers in a new data/ file are refused by the naming gate; the registry carries the same three domains, so the default is registry-derived with the scope key as the firm key. Downstream cells that expect the literal '49f' in recipient_firm (TR-w-1, TR-k-1) see '49financial' from the default table; TR-a-1's client_domains.json firm_key value governs when that file lands.",
    "notes": "The order's mixed key forms (49f is a short form; inflection and cottonwood are long keys) are the reason to prefer the registry's single key form."
  },
  {
    "id": "NFRA_TRNSPT-S4",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T17:05:00Z",
    "one_line": "The two VENDOR rows this project added to infra/logic/registry/systems.json (outlook, sharepoint; WK~3 @8e9ed1b539, drained @fed423d013) carry no display_name, so lib/opal_naming.py validate REFUSES the registry at HEAD and every `generate` target refuses with it (found grading DSGN_IRPTV1 item 41, whose vendorDisplayNames.generated.ts mark predates the rows).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~T (the rows are this project's; the display_name value is the CRO's PLATFORM_LOGIC_DOCS lane per @cd2ffcca99 -- one cut naming both, then the CTO regenerates the view)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python lib/opal_naming.py validate (2026-09-30 ~16:5xZ, HEAD): 'REFUSED systems.json[48].display_name: a VENDOR row carries the words a served face prints; missing or empty', the same for [49]; 'VALIDATE: REFUSED 2 refusal(s), 40 warning(s)'",
        "python lib/opal_naming.py generate --out <scratch> --target portal/src/pages/InvestorReporting/header/vendorDisplayNames.generated.ts: 'ERROR: the registry is refused (2 refusal(s))', 0 files written",
        "git log -S'sharepoint' -- infra/logic/registry/systems.json: 8e9ed1b539 0.9.0_WK_NFRA_TRNSPT~3 11:04Z 'registry(NFRA_TRNSPT TO-TR-g1): systems.json rows outlook and sharepoint (VENDOR, D9)'; fed423d013 2.0.0_SA_COO~T 12:58Z drain",
        "cd2ffcca99 4.0.0_SA_CRO 12:10Z: display_name on the 23 VENDOR rows; systems.json at HEAD: 25 rows carry a VENDOR value, 23 carry display_name (this seat's json read)",
        "portal/src/pages/InvestorReporting/header/vendorDisplayNames.generated.ts header: 'GENERATED ... from infra/logic/registry@1c951921d4940c85' (DSGN_IRPTV1 item 41 @e266a14a)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "lib/opal_naming.py validate exits 0 on CLOUD HEAD and every generated target regenerates from the registry (CLAUDE.md rule 30: a builder refusal is a missing registry row to add, never a hand-typed workaround).",
    "world_is": "validate exits with 2 refusals at HEAD; generate writes nothing; the committed vendor view stands on a registry hash two rows old and cannot be reproduced until outlook and sharepoint carry display_name.",
    "notes": "Nothing edited by this seat (registry rows are not the CVO's write surface). The grade of DSGN_IRPTV1 item 41 is unaffected: its file matches its stated sha256 and its test is green. First appended 17:05Z; the shared-tree copy was overwritten at 17:32Z before it was committed, so this is the same row re-appended."
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
  },
  {
    "id": "NFRA_TRNSPT-S5",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "surfaced_at": "2026-09-30T18:20:00Z",
    "one_line": "Closes NFRA_TRNSPT-S1 on 1.0.0_SA_CTO msg 103271: the laptop gateway mail-tool worktrees (wt-gw-f2/f3/int) are INERT for NFRA_TRNSPT; 0.0.0_AB_MSTR names their owner and site Z's order 4 adopts or supersedes them.",
    "disarm_owner": "1.0.0_SA_CTO (ruled 103271; nothing owed by this project)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "inbox 20260930T144354Z_1.0.0_SA_CTO_RE_103267 (Msg-ID 103271): 'S1 ruled -- INERT for NFRA_TRNSPT ... Not your write surface; mark the row INERT with this message id as the disposition'",
        "the channel is append-only; .tools/surprise-row-gate.py _mutation_violations refuses an in-place disposition edit, so the closure is this new row citing S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "1.0.0_SA_CTO msg 103271 rules S1 INERT for NFRA_TRNSPT and routes the worktrees to 0.0.0_AB_MSTR and site Z's order 4; no act remains for this project.",
    "spec_asserts": "S1: the three mail tools are NFRA_OPLGTW's (site Z) build.",
    "world_is": "Ruled INERT for this project by the CTO; the laptop branches are preserved by MSTR.",
    "notes": "Cites NFRA_TRNSPT-S1. The id is S5 because the CVO minted S4 at a3473f576c."
  },
  {
    "id": "NFRA_TRNSPT-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "surfaced_at": "2026-09-30T18:20:00Z",
    "one_line": "Post-drain hygiene at CLOUD: test_teams_parse_silver.py::test_missing_metadata_cue_leaves_wall_clock_null_with_warning splits the metadata fixture on a bare double LF, so it passes on the worker's LF-written file and fails on this autocrlf=true checkout, where every fixture reads CRLF.",
    "disarm_owner": "2.0.0_SA_COO~T (the round's batched repair cell: read fixtures with universal newlines, or an eol=lf rule for data/transcripts/scripts/tests/fixtures/ in .gitattributes)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/transcripts/scripts/tests/test_teams_parse_silver.py at b9b933859f: 1 failed, 9 passed; assert rows[1]['start_utc'] is None -> '2026-01-02T15:00:13.000000+00:00'",
        "fixture bytes: worktree CRLF 22 / LF-only 0; HEAD blob CRLF 0 / LF-only 22; the test's split finds 0 cue boundaries in the worktree text and 7 in the blob",
        "git config core.autocrlf = true; git check-attr text eol on the fixture: unspecified; every teams_pull and outlook_replay fixture also reads CRLF on this checkout"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TR1-t3-AC1: 10 of 10 tests pass (worker proof).",
    "world_is": "One of the ten is checkout-dependent; the parser itself reads CRLF, and the real Monday meeting parsed with unparsed=0.",
    "notes": "A repair row, never a silent recut."
  },
  {
    "id": "NFRA_TRNSPT-S7",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "surfaced_at": "2026-09-30T18:20:00Z",
    "one_line": "Post-drain hygiene at CLOUD: running data/transcripts/scripts/tests in ONE pytest process gives 22 failed / 30 passed because the teams and outlook packages both expose bare top-level modules named land_bronze and pull (sys.path insertion + 'import land_bronze'), so whichever loads first shadows the other.",
    "disarm_owner": "2.0.0_SA_COO~T (the round's batched repair cell: package-qualified imports -- data.transcripts.scripts.teams.* / .outlook.* -- or unique module names; the Lambda packaging of TR-i-1 imports the teams modules top-level too)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/transcripts/scripts/tests -q at 275b43af6a: 22 failed, 30 passed; e.g. test_teams_pull.py AttributeError: module 'land_bronze' has no attribute 'transcript_id_for'",
        "each file alone: test_outlook_bronze 11/11, test_teams_land_bronze 12/12, test_teams_read_meeting 7/7, test_teams_pull 9/10, test_pull_handler 1/2, test_teams_parse_silver 9/10",
        "data/transcripts/scripts/teams/pull.py:28 'import land_bronze'; data/transcripts/scripts/outlook/pull.py:16 'import land_bronze'; tests import both by bare name"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every cell's tests pass (each proof graded its own file in its own worktree).",
    "world_is": "Each file passes alone except the rows S6/S8 name; together the two sources' modules collide by name.",
    "notes": "Found only at the union; no worker could see it. A repair row."
  },
  {
    "id": "NFRA_TRNSPT-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "surfaced_at": "2026-09-30T18:20:00Z",
    "one_line": "Chain A x chain B seam after the drain: with parse_silver.py now beside pull.py, pull.run(with_silver=True) imports it for real and parse_and_write lists the bronze prefix, but the chain-A test fakes (FakeS3 in test_teams_pull.py, _MemS3 in test_pull_handler.py) have no list_objects_v2, so the SILVER-SKIPPED test and the handler test fail.",
    "disarm_owner": "2.0.0_SA_COO~T (the round's batched repair cell: give both fakes list_objects_v2, and assert the in-process silver hop on the fixture instead of SILVER-SKIPPED)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "test_teams_pull.py::test_with_silver_absent_module_is_typed_skipped and test_pull_handler.py::test_fixture_transport_returns_run_record: AttributeError: 'FakeS3'/'_MemS3' object has no attribute 'list_objects_v2' at data/transcripts/scripts/teams/parse_silver.py:169",
        "TR-t-1 was built on a branch without parse_silver (the lazy import typed SILVER-SKIPPED, as its face ordered); TR-t-3 lists bronze to find the sidecar (worker ~2 report)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TR-t-1: with_silver imports parse_silver lazily and types SILVER-SKIPPED when it is absent.",
    "world_is": "It is present now, so the hop runs; the seam is real and untested with a listing fake.",
    "notes": "The seam the round built by construction; its first exercise is the next real scheduled pull."
  },
  {
    "id": "NFRA_TRNSPT-W4-S1",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T15:15:00Z",
    "one_line": "Both public name-list fetches Andrew's word covers were refused by the hosts' bot protection, so names/given_names.txt and names/surnames.txt do not exist and TR1-a1-AC1/AC2 cannot pass.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2026-09-30T15:00:59Z curl -L -A Mozilla/5.0 https://www.ssa.gov/oact/babynames/names.zip -> HTTP 403 'Access Denied' (399-byte HTML, Akamai reference #18.e537c517.1790780459.2aa1f01); python requests retry at ~15:01Z -> 403 again",
        "2026-09-30T15:01:00Z same client https://www2.census.gov/topics/genealogy/2010surnames/names.zip -> HTTP 200 with a 247-byte 'Request Rejected ... support ID 13427891564882941819' HTML page, not a zip (starts b'<htm'); python requests retry -> same body",
        "sha256 of the SSA refusal body 4903db40d959d09244de08efa4c5004cc1306b46d9b9b6c2af3f9f896ee71091; of the Census refusal body adcd2c1213a905d5c1481b523a3f0f1c789c1f9885d1f31f410d86ec5cdb91d0 (neither is committed; no archive was obtained)",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_assets_check.py -> ASSETS-BAD name dictionary entries=0 (< 50000)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "ONE fetch each of the SSA names.zip and Census 2010 surnames names.zip yields the archives to distil into the name dictionary (>= 50,000 entries); 'if a fetch fails, stop on that file and file a surprise row: never substitute a hand-typed list'.",
    "world_is": "Both hosts refuse a non-browser client (SSA 403, Census a 200 rejection page); the worker used its one bounded retry per host and stopped; no name file was written and none was hand-typed. The other five assets, README, lock (name_dictionary_entries 0) and tests are committed; the size and Will/Grant tests fail honestly.",
    "notes": "Unblock is the issuer's or Andrew's: a browser-mediated download placed for the worker, a different public mirror Andrew names (egress word is per-use), or an operator-run fetch; then the worker re-runs pin.py-style pinning and AC1/AC2. The tests were not weakened."
  },
  {
    "id": "NFRA_TRNSPT-W4-S2",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T15:16:00Z",
    "one_line": "The task order asks for a null-address row for Yang's unmeasured 49financial address inside authors.json's authors list, but the issuer's r1_assets_check.py calls a['address'].lower() on every authors row and would raise on null.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_assets_check.py: addrs = {a[\"address\"].lower() for a in authors[\"authors\"]}",
        "task order build item 1 and 'Measured at the cut': carry a null row with claim: absent"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "authors.json {\"authors\":[{name,address,role,claim,basis}]} carries Yang's unmeasured 49financial row with address null and claim absent, and the issuer's check accepts the file.",
    "world_is": "A null address inside authors[] makes the issuer's check raise AttributeError; the worker put the null/absent row under a separate top-level key 'unmeasured' in authors.json so the checker and the wipe's read of authors[] stay total.",
    "notes": "If the issuer prefers the row inside authors[], the checker needs a None guard; the wipe (TR-w-1) should read both keys."
  },
  {
    "id": "NFRA_TRNSPT-W4-S3",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T15:35:00Z",
    "one_line": "The commit-time naming gate (LGIC_ENFORCE) REFUSES the two ordered data assets authors.json and client_domains.json as NEW hand-kept carriers of the firm tokens 49financial, 49f, inflection and cottonwood, so they cannot be committed within this order's grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... at 2026-09-30 ~15:2xZ: 'NAMING-GATE: REFUSE 5 graded' -- data/transcripts/assets/authors.json:12 manav.shah@49financial.com -> lookup('49financial'); client_domains.json:4 49financial.com, :5 49f -> lookup('49financial'); :12 inflection -> lookup('inflection'); :19 cottonwood -> lookup('cottonwood'); commit aborted",
        ".tools/naming-gate.py header: a firm token outside registry files, builder-call arguments and generated blocks is a hand-kept carrier and a NEW one is refused; the waiver kind is an R20 declared exception (a register entry outside this order's paths)",
        "infra/logic/registry/scopes.json:44 already carries email_domain '49financial.com' on the 49financial scope, so the domain table overlaps the registry"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Build items 1-2: authors.json and client_domains.json carry the measured addresses, domains and firm keys (49f, inflection, cottonwood) as versioned data assets committed under data/transcripts/assets/.",
    "world_is": "The gate grades JSON string values; the two files hold exactly those tokens by design. The worker did NOT obfuscate the strings to slip past the gate. Committed subset: allowlist, model_aliases, README, lock (pinning only what is committed), tests, rows, proof. authors.json and client_domains.json sit UNCOMMITTED in the worktree (copies in .scratch/held); the lock on disk is re-pinned over all six for the release.",
    "notes": "Unblock is the CTO's/issuer's: an R20 declared exception for the two files (register row plus a read_context entry), or a ruling that the client-domain and firm-key data are read from the registry (lookup) so the file carries none. Either way the order's paths may need to widen."
  },
  {
    "id": "NFRA_TRNSPT-W4-S4",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T15:50:00Z",
    "one_line": "safe-commit's missions-tree check refuses every org/missions commit from this worktree with INDEX-DRIFT org/projects/NFRA_TRNSPT.json (index PRD vs tree EXECUTING) because the worktree branch predates CLOUD 17ad3ea043, the issuer's index fix.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... (2026-09-30 ~15:4xZ): 'BLOCKED: missions-tree-check ... [INDEX-DRIFT] org/projects/NFRA_TRNSPT.json: dep_stage: index=PRD tree=EXECUTING'; all other gates (commit-gate, naming-gate PASS 0 graded, surprise-row-gate, to-pipeline-gate) passed on the subset",
        "git merge-base --is-ancestor 17ad3ea043 HEAD -> rc 1 (HEAD daee98b79f); git show --stat 17ad3ea043: org/projects/NFRA_TRNSPT.json only, 2 insertions 2 deletions, authored by 2.0.0_SA_COO~T"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worker commits its deliverables on its worktree branch with safe-commit.sh (order notes and standing worker rules: never merge, never widen the grant).",
    "world_is": "The order's own base lacks the issuer's index fix, org/projects/NFRA_TRNSPT.json is outside this order's grant and merging CLOUD is forbidden to a worker, so nothing could be committed; all work sits uncommitted in the worktree and the ROW ITSELF is uncommitted.",
    "notes": "Unblock: the issuer/integrator merges CLOUD 17ad3ea043 into wk-NFRA_TRNSPT-4 (sibling ~3 records the same remedy in its row W3-S1) or tells the worker to; then the worker commits the prepared set (msg in .scratch/msg.txt) after re-checking naming-gate on the two firm-token assets (W4-S3)."
  },
  {
    "id": "NFRA_TRNSPT-W4-S5",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T16:40:00Z",
    "one_line": "The issuer's three rulings on W4-S1, W4-S3 and W4-S4 were applied as amended: CLOUD merged (17ad3ea043 in), client_domains.json retired with the table read from registry email_domain, authors.json reshaped with no firm token, name lists vendored from the PyPI sdist names 0.3.0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~T",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "issuer message to 0.9.0_WK_NFRA_TRNSPT~4 (amended order face, 2026-09-30): RULING 1 merge CLOUD; RULING 2 retire client_domains.json, authors.json shape with firm_domain_rule; RULING 3 pip download names, one fetch",
        "git merge --no-edit CLOUD twice: 17ad3ea043 in HEAD; infra/logic/registry/scopes.json already carries email_domain on the three FIRM rows (49financial.com, inflectionwealth.com, cottonwoodmail.com) plus demo.test; issuer's recut r1_assets_check.py printed 'ASSETS-PINNED n=5 names=93962 registry_domains=4' rc=0",
        "pip download names --no-deps --no-binary :all: -> names-0.3.0.tar.gz sha256 726e46254f2ed03f1ffb5d941dae3bc67c35123941c29becd02d48d0caa2a671; surnames.txt 88799 lines + given_names.txt 5163 lines = 93962 (dist.all.last, dist.female.first, dist.male.first)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The original order face named authors.json and client_domains.json as carriers of firm tokens and a SSA/Census name-list fetch.",
    "world_is": "The amended face replaced all three; W4-S1, W4-S3 and W4-S4 stand as written and are superseded by these applied rulings. W4-S2 is moot (Yang's second address is covered by firm_domain_rule)."
  },
  {
    "id": "NFRA_TRNSPT-W4-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T17:30:00Z",
    "one_line": "lib.opal_naming.address() refuses object=\"\", so the order's bronze prefix call address('outlook','transcripts','bronze','analysis_commentary','date=<d>','') cannot run as written.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/opal_naming.py address() at HEAD 4ef97cc7dd: `if not isinstance(object, str) or not object ...: raise ValueError`",
        "python call address('teams','transcripts','bronze','analysis_commentary','date=2026-09-30','') -> ValueError; object=None -> s3://opal-data-transcripts/teams/transcripts/bronze/analysis_commentary/date=2026-09-30"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-TR-w1 build item 2: the bronze partition prefix is address(source, scope, 'bronze', 'analysis_commentary', 'date=<d>', '') (a trailing empty object).",
    "world_is": "address() raises ValueError \"object must be a non-empty ASCII string not starting with '/'\" for object=''; object=None returns the partition address without a trailing slash. silver.py builds the prefix as address(..., partition) + '/' instead; the output key still uses the object argument."
  },
  {
    "id": "NFRA_TRNSPT-W4-S7",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T17:30:00Z",
    "one_line": "This branch's registry has no `outlook` source row (it is TR-g-1's, on wk-NFRA_TRNSPT-3 @8e9ed1b539), so address('outlook',...) raises here; the silver test borrows a registered source until that row drains.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python: opal_naming.address('outlook','transcripts','bronze','analysis_commentary','date=2026-09-30') -> ValueError source 'outlook' is not a systems.json key (worktree wk_nfra_trnspt_4 HEAD 4ef97cc7dd)",
        "git show 8e9ed1b539 -- infra/logic/registry/systems.json: adds rows outlook and sharepoint; git branch --contains 8e9ed1b539 -> wk-NFRA_TRNSPT-3 only"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-TR-w1 build item 2: silver reads and writes under address('outlook','transcripts', ...) built by lib.opal_naming.",
    "world_is": "On this base the registry's systems.json has no key `outlook` (ValueError: source 'outlook' is not a systems.json key). silver.py takes the source from its own directory name; the test test_outlook_silver.py monkeypatches silver.SOURCE to the first registered source that resolves a bronze address ONLY when 'outlook' does not resolve, and uses the real one once TR-g-1 has drained. The real run at the drain must resolve address('outlook',...) for real; the issuer's run at the drain is that proof."
  },
  {
    "id": "NFRA_TRNSPT-W4-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T17:30:00Z",
    "one_line": "Wipe limits found while building: a name is matched in another case only with same-message evidence (or ALL-CAPS in the dictionary); capitalised surnames that are also English words (Ask, Mail, Reach) are wiped at sentence start; capitalised non-stopword words (headings, labels) go to residual flags, so real messages will hold out often.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/transcripts/scripts/outlook/wipe.py wipe_blocks (commit e555ef8ac9): pass 1 learns names per message, pass 2 applies; STOPWORDS list",
        "python: wipe_blocks('we asked ottoline today') with ottoline in the given-name set leaves it unchanged; 'Ask' and 'Mail' are members of surnames.txt"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "C-WIPE: names applied case-sensitively behind an allowlist; anything capitalised and unknown goes to pii_residual_flags and is held out; C-WIPE-GATE plants a name 'in a different case'.",
    "world_is": "Case-sensitive dictionary matching means a standalone lower-case name (e.g. 'we asked ottoline') is NOT wiped unless the same message showed the name capitalised or ALL-CAPS; matching lower-case case-insensitively would wipe ordinary words (will, grant, mark, rate). The surnames list holds ordinary English words, so sentence-initial 'Ask'/'Mail' are wiped unless in the stopword list (a small one is in wipe.py). The planted-token test plants the lower-case name beside its ALL-CAPS form. The held-out rate on the real sample is unmeasured here; the issuer's real silver run prints held_out=<h>."
  },
  {
    "id": "NFRA_TRNSPT-W4-S9",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T18:10:00Z",
    "one_line": "The TR-k-1 face asks for pdf_sha256 null this round while the issuer's AC1 check requires nullable true ONLY on holdings and request_text; the contract marks pdf_sha256 non-nullable and gold emits the empty string with claim absent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_gold_contract_check.py: NULLABLE = {holdings, request_text}; the check prints GOLD-CONTRACT-BAD if any other field is nullable",
        "TO-TR-k1 worker face build item 2: 'pdf_sha256 null this round' and build item 1 'claim pdf_sha256 absent'; the contract validation refuses a null in a non-nullable field, so both cannot hold",
        "org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json pdf_sha256: nullable false, claim absent; data/transcripts/scripts/outlook/gold.py derive_row emits '' and test_hashes_and_carried_fields asserts it",
        "Also decided without a face line: gold.derive drops silver rows with held_out true or ingest false (C-WIPE holds them out); models_referenced matches single-token aliases case-sensitively (so a capitalised 'Short' at a sentence start matches the Short Term alias); 'Dividend Income' alone is not in model_aliases.json (only 'Dividend Income Strategy/Portfolio'), so it does not match",
        "after git merge CLOUD, address('outlook','transcripts','gold',...) still raises ValueError: source 'outlook' is not a systems.json key (infra/logic/registry/systems.json has no outlook row); the gold test borrows a registered source as W4-S7 does"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "pdf_sha256 is null this round AND is non-nullable per the issuer's check (nullable true only on holdings, request_text).",
    "world_is": "One of the two must give: the contract carries pdf_sha256 as a non-nullable string with the empty-string coverage value and claim absent; when attachment bytes land (S12) the real sha256 replaces it with no schema change. If the issuer wants a true null, the check's NULLABLE set and the contract change together (a version bump).",
    "notes": "Residue: the registry still lacks the outlook source row after the CLOUD merge, so the issuer's gold run needs chain C's row before gold.py resolves its address."
  },
  {
    "id": "NFRA_TRNSPT-W4-S10",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T19:00:00Z",
    "one_line": "The irpt-requests table holds no request composition (variant, comparison_keys, account type, holdings): a full read-only scan of 1102 items found 0 carrying them, so the replay set is the six invented fixture requests.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "boto3 dynamodb scan of irpt-requests (us-east-1), read-only, 2026-09-30: 1102 items scanned; request_revision prefixes: RETENTION 447, ARTIFACT 188, SELECTION 146, REPORT 117, PERFORMANCE_ACCEPTED 112, UPLOAD 25, NORMALIZATION 25, INPUT 21, analysis 15, PERFORMANCE_USE 6",
        "REPORT# items (117) carry only ref{sha256,report_id,revision,immutable,report_kind}, tenant, blob{version_id,bucket,key}, owner{...}, retention_ref, request_revision (attribute-name census; values not printed); SELECTION items (146) and 'analysis' items (15) carry a JSON string of owner/account_set and identity/composition_ref fields; no item has variant, comparison_keys, account_type or holdings",
        "infra/aws/lambda/investor-reporting/ycharts/generate/report_index.py publish(): the REPORT# item is ref/owner/blob/retention only; the Generate composition sits behind analysis.record composition_ref (an artifact blob), which this order's read-only table scan does not open",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/R1_REPLAY_REQUESTS.json: source fixture, items_scanned 1102, composition_items 0, count 6 (invented requests from replay.FIXTURE_REQUESTS)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-TR-q1 build item 2: a read-only scan of irpt-requests for REPORT#/request items yields variant, comparison_keys, an account-type field and holdings category weights for the replay set.",
    "world_is": "The table projects none of those fields; replay.py --extract-irpt scanned 1102 items, found 0 compositions and wrote the six invented fixture requests as the order directs. A real replay set needs the composition blobs (analysis.record composition_ref), an S3 read of client-bearing artifacts this order does not grant.",
    "notes": "project_item() in replay.py is tested on a synthetic item only; it has never met a real composition, so its field names (variant, comparison_keys, account_type, holdings[].category/weight) are the face's, unverified against real data."
  },
  {
    "id": "NFRA_TRNSPT-W4-S11",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T19:10:00Z",
    "one_line": "The naming limb of safe-commit refuses every commit that stages a .py/.json file because systems.json rows outlook (index 48) and sharepoint (index 49) are VENDOR rows with no display_name; the fix is outside this order's paths, so the slicer, replay, tests and proof instance are uncommitted.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... on the q1 paths, 2026-09-30 ~19:05Z: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' naming-gate: 'the registry is refused by validate (2 refusal(s)): systems.json[48].display_name: a VENDOR row carries the words a served face prints; missing or empty'",
        "python read of infra/logic/registry/systems.json at this worktree HEAD fb2d56e333 (the merge of CLOUD 13337dbd4e): VENDOR rows with no display_name = 2 of the VENDOR rows: outlook (48), sharepoint (49); the same two rows are in CLOUD (git log CLOUD -- infra/logic/registry/systems.json: 8e9ed1b539 added them from ~3, cd2ffcca99 added display_name to the 23 VENDOR rows that then existed)",
        ".tools/safe-commit.sh:736-745: the limb runs whenever the staged set holds a *.py/*.json/*.yaml/*.tf/*.js file; an .md-only commit is not refused"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker commits its owned paths through safe-commit.sh and the naming limb grades the commit's own files.",
    "world_is": "The limb validates the whole registry, and the registry on CLOUD is invalid on two rows the NFRA_TRNSPT chain C added, so no .py/.json commit passes on any branch that carries them. Adding a display_name to those two rows is one edit in infra/logic/registry/systems.json, which is not in this order's grant.",
    "notes": "Criteria were run on the uncommitted files: AC1 20 passed; AC2 SLICER-REPLAY client_identifiers=0 requests=6 with_candidates=6 fallback=2 no_precedent=0. The issuer or the registry's owner lands the two display_name values (owner claim for the rows: D9); then the files commit unchanged."
  },
  {
    "id": "NFRA_TRNSPT-W4-S12",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
    "surfaced_at": "2026-09-30T20:10:00Z",
    "one_line": "W4-S11's naming-limb block cleared: the CTO validator fix b5dc2e63d1 and 4.0.0_SA_CRO's registry display names 224058ea3f reached this branch by an issuer fast-forward to 81244a2bf3, and python lib/opal_naming.py validate reads OK.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~T",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git rev-parse --short HEAD in wk_nfra_trnspt_4, 2026-09-30: 81244a2bf3 (branch wk-NFRA_TRNSPT-4, fast-forwarded by the issuer)",
        "python lib/opal_naming.py validate read OK per the issuer's state note, 2026-09-30; W4-S11 cited the validate refusal on systems.json[48].display_name"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker commits its owned paths through safe-commit.sh and the naming limb grades the commit's own files.",
    "world_is": "With the registry fix landed on this branch, the q1 files commit unchanged; row W4-S11 is unedited and its block no longer stands.",
    "notes": "Append-only: W4-S11 and every other row untouched."
  },
  {
    "id": "NFRA_TRNSPT-S9",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-30T19:15:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "FWD-7's round-1 real run broke at its first real input: list_email_attachments returns the Graph envelope {\"@odata.context\", \"value\": [...]}, but the decomposition's BRONZE CONTRACT (issuer text) told TR-b-1 it returns a bare list, so outlook/pull.py --replay crashes in criterion.classify ('str' object has no attribute 'get') on both real messages; nothing was landed.",
    "disarm_owner": "2.0.0_SA_COO~T (issuer contract error; first item of the round-2 repair cell: unwrap value when present, and a fixture in the real envelope shape)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python data/transcripts/scripts/outlook/pull.py --replay C:/Users/AndrewBerman/Desktop/NFRA_TRNSPT_SAMPLE_LOCAL/r1 --dry-run at 0225e80b2f: AttributeError: 'str' object has no attribute 'get' in criterion.classify",
        "the replay directory (outside the repo, client PII): 2 messages copied byte-identical from the harness-persisted raw read_email outputs idx_25_rawtool.json / idx_36_rawtool.json, and the 2 list_email_attachments results as the tool returned them (envelope with value)",
        "decompositions/NFRA_TRNSPT_DECOMP.md BRONZE CONTRACT: 'list_email_attachments(id) returns {id, name, size, contentType, isInline} per attachment' -- read as a bare list by the worker; the fixture (outlook_replay/) is a bare list"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Round 1's real run lands the recorded sample to bronze through pull.py --replay --apply.",
    "world_is": "The real tool envelope is not what the contract described; the lander raises before any write. Measured read-only with the envelope unwrapped: both real messages classify sender_ok=true, client_recipient=true, recipient_firm=49financial, ycharts_pdf=false, near_miss=true, ingest=false (their only non-inline attachments are application/octet-stream images of 6,866 and 197,768 bytes).",
    "notes": "The defect is the issuer's face, not the worker's: the worker built exactly the shape it was given. This is the value of a real run over a fixture."
  },
  {
    "id": "NFRA_TRNSPT-S10",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-30T19:15:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Chain C x chain D seam: outlook/criterion.py load_tables() reads data/transcripts/assets/authors.json only when client_domains.json ALSO exists; TR-a-1's ruled shape retired client_domains.json (the domains are registry tenant.email_domain), so the criterion always falls back to its inline default tables and never reads the ruled authors.json (addresses list + firm_domain_rule).",
    "disarm_owner": "2.0.0_SA_COO~T (round-2 repair cell: load_tables reads authors.json alone and the registry domains, honours firm_domain_rule)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/transcripts/scripts/outlook/criterion.py:48-54 load_tables: 'if os.path.isfile(ap) and os.path.isfile(dp): ... return ... \"inline-default\"'",
        "data/transcripts/assets/ at 0225e80b2f carries authors.json and no client_domains.json (issuer ruling on W4-S3)",
        "the read-only measurement above ran with load_tables() -> the inline-default tables"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The criterion reads the author and domain tables from the versioned assets when present.",
    "world_is": "It reads them only as a pair; after the ruling the pair can never be complete, so the versioned authors table is dead data.",
    "notes": "Built on two branches that could not see each other; found at the union."
  },
  {
    "id": "NFRA_TRNSPT-S11",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-30T22:05:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "S07 (the Research Meeting refusal, read-only): the Research Team Meeting's chat shows a transcript WAS produced on 2026-09-29 (callTranscriptEventMessageDetail, organizer user e44d429b) and a 57-minute recording saved to the organizer's OneDrive, yet the meeting is ABSENT from Andrew's calendar for the next 8 days while the Morning Meeting and OCIO IC appear there with him as an attendee; the likely cause of Graph's 3003 'User does not have access to lookup meeting' is that Andrew is a member of the meeting CHAT but not an invitee of the meeting SERIES.",
    "disarm_owner": "1.0.0_SA_CTO (routing: the remedy is a person act -- the organizer adds andrew@opalinvest.com to the series invite -- or the application-permission route of the recon brief; both are outside this project's write surface)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gateway read_chat_messages(19:meeting_MjBkMmQ0ZDItMjY3My00NTAzLWExZTUtZTQxNTgyZGFkMDYy@thread.v2, top 8) at 2026-09-30 22:0xZ: callTranscriptEventMessageDetail 2026-09-29T12:56:59Z (callTranscriptICalUid present), callRecordingEventMessageDetail status success, duration PT56M38S, URL in the organizer's personal OneDrive; meetingOrganizer and initiator user id e44d429b-b629-4035-b09b-447e978322db (series.json organizer_oid for equity_research_call)",
        "gateway list_calendar(days=8) at 2026-09-30 22:0xZ: 6 events; Morning Meeting 10-05 and OCIO IC 10-06 list andrew@opalinvest.com as an accepted attendee; no Research Team Meeting event, although research_transcripts/raw/ shows it ran about twice weekly (e.g. 04-07 Tue, 04-09 Thu) and it ran 09-29",
        "TRANSCRIPTS_FIRST_PULL_20260929.md: the three meetings Andrew can read are all organized by another user of whom he is an invitee; the refused one is the only one organized by e44d429b"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD S07: the Research Meeting refusal investigated; cause named or a route found.",
    "world_is": "Cause named as likely (not proven): invitee status. Proof needs one act: after the organizer adds Andrew to the series, list_meeting_transcripts on the meeting returns 200; the negative arm is today's 3003.",
    "notes": "Read-only; nothing was changed. The calendar tool reads forward only, so the absence is measured over 8 days, not the series."
  },
  {
    "id": "NFRA_TRNSPT-S12",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-30T22:05:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Off-task observation: the announce-mode seating lint (gate2, .tools/to-decomp-ref-lint.py) reads the per-project worker serial 0.9.0_WK_NFRA_TRNSPT~1 as the generic seat 0.9.0_WK_NFRA and reports all five round-2 orders as 'already holds open TOs on 6 OTHER pipeline projects' -- a false positive under the spine's worker-serial form 0.9.0_WK_<CODE>~<n>.",
    "disarm_owner": "1.0.0_SA_CTO (the lint's owner decides; it is ANNOUNCE mode and blocked nothing)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output of the round-2 issuance 35d912322e: '[gate2] SEATING: this NEW task order for NFRA_TRNSPT is addressed to 0.9.0_WK_NFRA, which already holds open TOs on 6 OTHER pipeline project(s): NFRA_IAMROLES202609 ...' x5; '[gate2] ANNOUNCE mode -- NOT blocking this commit'",
        "spine L6: <issued_to> names the worker serial 0.9.0_WK_<CODE>~<n>; the project code here contains an underscore (NFRA_TRNSPT)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The seating lint counts a seat instance's open orders across projects.",
    "world_is": "It truncates a project code containing an underscore, so every NFRA_* project's workers look like one seat; if the lint is armed to ENFORCE it will refuse every such issuance."
  },
  {
    "id": "NFRA_TRNSPT-S13",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-30T22:20:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "A byte-exact recording of a real message is not reliably available to this seat: the harness persists a gateway read_email result to a file only when it is very large (the two saved samples were 55,763 and 72,569 bytes), and the two admissible candidates read this round came back INLINE (about 40 KB and 22 KB), so they reach this seat only as model context, which is not 'exactly as received'.",
    "disarm_owner": "1.0.0_SA_CTO (routing: the byte-exact bronze landing of a real admitted message rides site Z's headless mail route, item 5 of the relay; until then FWD-7's real run is a LOCAL measurement, never a bronze write)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gateway read_email on candidate n=74 (2026-08-11, admitted: author sender, client recipients, application/pdf 585,757 bytes, body 'Attached is the YC report') and n=14 (2025-11-06, PDF 586,762 bytes): both returned inline at 2026-09-30 21:3xZ-22:1xZ",
        "C:/Users/AndrewBerman/Desktop/NFRA_TRNSPT_SAMPLE_LOCAL/idx_25_rawtool.json (72,569 bytes) and idx_36_rawtool.json (55,763 bytes): the only harness-persisted read_email outputs; both are near-misses (no PDF)",
        "decomposition round 2, 'The issuer's real runs at close' item 1 foresaw this branch: 'or states that the byte-exact recording waits on site Z's headless mail route'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CTO analysis ruling 3b: a real run lands ONE message the criterion admits, its silver read by the two named readers.",
    "world_is": "The admitted message exists and is identified, but the only byte-exact path to it from this laptop is the unbuilt headless mail route; bronze must not receive a model-relayed copy.",
    "notes": "The round-1 near-miss pair stays the only byte-exact real input."
  },
  {
    "id": "NFRA_TRNSPT-W1-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~1",
    "surfaced_at": "2026-09-30T20:30:00Z",
    "one_line": "Round 1's data/transcripts/scripts/tests/test_outlook_bronze.py::test_tables_source_recorded asserts the retired table label (inline-default or an assets: prefix) and now fails on the ruled label assets+registry; the file is outside TO-TR-f2's <paths>.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/transcripts/scripts/tests/test_outlook_bronze.py:53-54: assert criterion.load_tables()[2] in ('inline-default',) or criterion.load_tables()[2].startswith('assets:')",
        "python -m pytest data/transcripts/scripts/tests/test_outlook_bronze.py: 1 failed (test_tables_source_recorded), 48 passed with the four outlook/wipe test files; the same 48 pass after the change",
        "also failing before and independent of this cell: test_assets_lock.py::test_every_pinned_sha_matches (allowlist.json) and the teams land_bronze name collision when the whole tests directory runs in one process (transcript_id_for)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-TR-f2 build item 2: load_tables returns the label assets+registry; the order's <paths> omit test_outlook_bronze.py.",
    "world_is": "The one round-1 assertion on the label was not updated, so it fails on the required label. The order forbids weakening a test to pass and does not grant the file; the new test_outlook_envelope.py asserts the ruled label (7 passed).",
    "notes": "One-line fix for whoever holds that file: accept label == 'assets+registry'. Left unedited by this worker."
  }
]
```
