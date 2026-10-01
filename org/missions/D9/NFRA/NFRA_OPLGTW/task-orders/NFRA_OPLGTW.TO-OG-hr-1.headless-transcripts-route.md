# NFRA_OPLGTW task order -- `OG-hr-1` -- workstream TRNSPT-DEPS (O2): the headless transcripts route, BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-hr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~16</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request route; the caller's schedule is NFRA_TRNSPT's. No alert (C7, CLAUDE.md moratorium).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the bearer secret is created at OG-rl-1 under its ledger.
comp-adversary: DECLARED-NOT-APPLICABLE -- the boundary is the CTO's (PRD v1.2 C7 "Headless content routes", ratified-text half SIGNED @9018714ff3).
EGRESS CLASS, declared: NONE. No AWS call, no Graph call, no deploy.
</preflight>

## 1. THE CELL -- `OG-hr-1` (decomposition addendum R3-T)

`GW` = `infra/aws/ec2/opal-gateway`. Read PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.2 C7
"Headless content routes" whole, and `GW/app/ms_ingest.py` as the PATTERN (static bearer, `hmac.compare_digest`,
server-held token). Build a NEW module; `ms_ingest.py` stays byte-unchanged.

1. **Prefix and secret names come from the builder** `lib/opal_naming.py` `name(system, scope, function, kind,
   qualifier)`. Record each builder call and its output in
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/ROUTE_NAMES.json` under key `transcripts`:
   - `prefix` = "/" + builder output, and `prefix_builder`;
   - `secret_name` and `secret_builder` (SECRET grammar);
   - `bearer_label`;
   - `probes.transcripts_of_meeting`, a format string with `{prefix}` and `{meeting_id}`.

   **If the builder refuses** (it has no route kind today), STOP: that is a BLOCKING row naming the missing registry
   row (CLAUDE.md rule 30). Never hand-type a name.
2. **Bearer.** Read the bearer from the environment variable your module names. Compare it in constant time. Accept
   it ONLY on this prefix: the `/ms/*` bearer is refused here, and this bearer is refused on `/ms/*`.
3. **Access.** Use the server-held delegated token of the ONE fixed identity the existing machine route uses (the
   token broker's server-held path, as `ms_ingest` does). Graph calls are GET only, through a server-side path
   allowlist that fails closed. There is no write, send or reply verb.
4. **Meeting allowlist** comes from configuration, and an empty allowlist refuses everything. Only allowlisted meeting
   ids are reachable.
5. **Allow-by-key output:** meeting id, transcript id, `createdDateTime`, `endDateTime`, the `text/vtt` body, its byte
   count and its sha256. Nothing else, so a new Graph field cannot leak.
6. **Audit:** route, ids, byte counts and the caller's bearer label. Never content.
7. A refusal or `NeedsLogin` is returned to the caller. There is no alert, notification or SNS.
8. Register the routes in `GW/app/server.py`. Tests: a new `GW/tests/test_transcript_route.py` with exactly the 9
   tests `hr1.AC1.sh` names, with Graph and the token broker stubbed.

## 2. BOUNDS

1. Code, tests and the names record only. No AWS call (no secret created), no Graph call, no deploy. Never edit
   `ms_ingest.py`, `GRAPH_SCOPES`, the identity allowlist or the PRD.
2. Every test run sets `AUDIT_PATH` to a temp file; restore `GW/audit.jsonl` if dirtied.
3. Work in the worktree named in your identity line. Never push, merge, rebase, stash, `checkout --` or `clean`.
   REFUSE a criterion you cannot meet as written.
4. Commit with `.tools/safe-commit.sh` under your serial; every `.py` passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/transcript_route.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/tests/test_transcript_route.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W16-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`. A module name other than
`transcript_route.py` is a row, never an unlisted path.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-hr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/hr1.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 9 of 9; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-hr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/hr1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)NAMES ok transcripts.*app/ms_ingest\.py changed since base \w+: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the C7 headless boundary for transcripts, by the 9 named tests.
- `AC2`: the prefix and secret are builder output and used in the code; `/ms/*` is byte-unchanged.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/NFRA_OPLGTW.TO-OG-hr-1.headless-transcripts-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the builder calls and outputs, the diff
stat, the literal AC1-AC2 output, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~16, queue position 1. `OG-hr-2` follows in the same slot (both edit `server.py`).
- The four meeting ids are G-MEETINGS, resolved after release; the allowlist ships empty, so it fails closed.
- `<risk>` WORLD is GATE (xii)'s floor; the cell deploys nothing.

<status>staged</status>
<round>8</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
