# NFRA_OPLGTW task order -- `OG-tx-1` -- workstream TRNSPT-DEPS (O1): the meeting-transcript read tools, BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tx-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- three read tools; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no new Graph scope (C7).
comp-adversary: DECLARED-NOT-APPLICABLE -- the tool shapes are the CTO-admitted spec's (PRD v1.2 C7, ratified-text half SIGNED @9018714ff3).
EGRESS CLASS, declared: NONE. No AWS call, no Graph call, no deploy.
</preflight>

## 1. THE CELL -- `OG-tx-1` (decomposition addendum R3-T)

`GW` = `infra/aws/ec2/opal-gateway`. Build EXACTLY sections 4 and 5 of
`docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md` (read it whole), under PRD
`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.2 C7 "Interactive tools" (read C7 whole):

1. In `GW/app/tools.py`, through `_run`, read class:
   - `find_online_meeting(join_url)`;
   - `list_meeting_transcripts(meeting_id)`, which follows `@odata.nextLink` to exhaustion and returns every row plus
     the row count;
   - `read_meeting_transcript(meeting_id, transcript_id, offset=0, limit=0)`. It returns `content`, `total_bytes`, the
     `sha256` of the FULL body, `offset`, `returned_bytes` and `complete`. `limit=0` means the whole body.
2. `list_calendar`'s `$select` gains `onlineMeeting` and `seriesMasterId`, and the tool accepts a start date (spec 4.4).
3. `GW/app/graph.py` `call` gains an OPTIONAL `accept` argument whose default keeps today's `application/json`. Never
   add a second client.
4. `innerError.code` is surfaced. `GraphAccessToTranscriptsDisabled` and `SpeakerAttributionNotAllowed` are distinct
   outcomes, never one generic 403. There is no fallback to an unattributed transcript.
5. Register all three tools in `GW/app/destructive_ops.py` SAFE_TOOLS AND `GW/app/data_entitlement.py` NATIVE_TOOLS.
   Bump the hard count in `GW/tests/test_entitlement_admin.py::test_ogz2_ac08` by exactly 3, naming the three tools
   in a comment.
6. The audit record carries meeting id and transcript id, never transcript text. Transcript text is untrusted content.
7. A scoped identity (`GW/app/identity_scope.py`) and a restricted (Schwab-profile) principal stay denied by default.
8. Tests: a new `GW/tests/test_transcript_tools.py` with exactly the 8 tests `tx1.AC1.sh` names, with Graph stubbed.

## 2. BOUNDS

1. Code and tests only. No Graph call, no AWS call, no deploy. Never edit `GRAPH_SCOPES`, `IT_REQUEST.md`, the
   allowlist, `ms_ingest.py` or the PRD.
2. Every test run sets `AUDIT_PATH` to a temp file. If the tracked `GW/audit.jsonl` is dirtied, restore its HEAD
   bytes.
3. Work in the worktree named in your identity line. Never push, merge, rebase, stash, `checkout --` or `clean`.
   REFUSE a criterion you cannot meet as written.
4. Commit with `.tools/safe-commit.sh` under your serial. Every `.py` you touch passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/graph.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_transcript_tools.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `INVESTIGATION_v1.md` above, id `NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tx-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tx1.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 8 of 8; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tx-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tx1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)REG 3 of 3; SCOPES same.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the C7 transcript clauses, by the 8 named tests.
- `AC2`: the three tools are in BOTH lists, the 17 Graph scopes are unchanged, and `test_ogz2_ac08` passes.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-tx-1.transcript-tools.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the diff stat, the 8 test names, the
literal AC1-AC2 output, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~15, queue position 1. Cut after OG-t-2 lands (`1.0.0_SA_CTO~O` msg 27439). It shares `tools.py`,
  `destructive_ops.py`, `data_entitlement.py` and the ac08 count with `OG-ml-1`, the next order in this slot.
- The live REACH arm is `OG-tx-2`'s, held on G-TEAMS-TX. The release is `OG-rl-1`'s.
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell deploys nothing.

<status>staged</status>
<round>8</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
