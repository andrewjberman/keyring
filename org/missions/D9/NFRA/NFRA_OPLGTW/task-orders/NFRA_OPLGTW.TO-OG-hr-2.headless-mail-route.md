# NFRA_OPLGTW task order -- `OG-hr-2` -- workstream TRNSPT-DEPS (O5): the headless mail route, BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-hr-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~16</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request route; the daily pull's schedule is NFRA_TRNSPT's. No alert (C7).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the bearer secret is created at OG-rl-1 under its ledger.
comp-adversary: DECLARED-NOT-APPLICABLE -- the boundary is the CTO's (PRD v1.2 C7 @c9fd271499: sender table only, no thread reach; PDF bytes only).
EGRESS CLASS, declared: NONE. No AWS call, no Graph call, no deploy.
</preflight>

## 1. THE CELL -- `OG-hr-2` (decomposition addendum R3-T)

`GW` = `infra/aws/ec2/opal-gateway`. Read PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.2 C7
"Headless content routes" whole AT @c9fd271499 OR LATER. The mail clause there has NO `conversationId` thread reach.
Build on the same pattern as `OG-hr-1` (your queue position 1, same worktree), with a SECOND prefix and bearer.

1. **Names.** Add key `mail` to `deliverables/0.9.0_WK_NFRA_OPLGTW~16/ROUTE_NAMES.json`, built the same way:
   - `prefix` + `prefix_builder`, `secret_name` + `secret_builder`, `bearer_label`;
   - `probes.message`, with `{prefix}` and `{message_id}`;
   - `probes.attachment`, with `{prefix}`, `{message_id}` and `{attachment_id}`.

   A builder refusal is a BLOCKING row (rule 30).
2. **Bearer.** Its own bearer, compared in constant time and accepted only on this prefix. The transcripts bearer and
   the `/ms/*` bearer are refused here.
3. **Senders.** ONLY messages whose sender address is on the SENDER TABLE are served.
   - The table is configuration. An empty table refuses everything.
   - An off-table sender is refused EVEN WHEN the message shares a `conversationId` with a table sender's message.
4. **Output.** Allow-by-key: the fields of `read_email`'s widened `$select` (as `OG-ml-1` leaves it) plus the body.
5. **Attachments.** `$value` bytes, with sha256, ONLY for a non-inline `application/pdf` at or under a configured size
   cap. Every other attachment, and a PDF over the cap, returns metadata only.
6. **Access.** Use the same ONE fixed server-held identity as `OG-hr-1`. GET only, through a fail-closed path
   allowlist; there is no write, send or reply verb.
7. **Audit and refusals.** The audit records route, ids, byte counts and bearer label, never content. A refusal or
   `NeedsLogin` is returned to the caller, with no alert.
8. **Tests.** A new `GW/tests/test_mail_route.py` with exactly the 10 tests `hr2.AC1.sh` names, with Graph and the
   token broker stubbed.

## 2. BOUNDS

1. Code, tests and the names record only. No AWS call, no Graph call, no deploy. Never edit `ms_ingest.py`,
   `GRAPH_SCOPES`, the identity allowlist or the PRD. No sender address is committed: the table's values arrive at
   `OG-rl-1` (gate G-SENDERS).
2. Every test run sets `AUDIT_PATH` to a temp file; restore `GW/audit.jsonl` if dirtied.
3. Same worktree as `OG-hr-1`, starting from its committed head. If `OG-ml-1` has not merged when you start, read its
   `$select` from its branch; if that differs from what it merged, file a row. Never push, merge, rebase, stash,
   `checkout --` or `clean`.
4. Commit with `.tools/safe-commit.sh` under your serial; every `.py` passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/mail_route.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/tests/test_mail_route.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W16-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-hr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/hr2.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 10 of 10; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-hr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/hr2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)NAMES ok mail.*app/ms_ingest\.py changed since base \w+: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the C7 mail boundary (sender table only, no thread reach, PDF bytes only), by the 10 named tests.
- `AC2`: the prefix and secret are builder output, distinct from the transcripts route's; `/ms/*` is byte-unchanged.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/NFRA_OPLGTW.TO-OG-hr-2.headless-mail-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the builder calls and outputs, the diff
stat, the literal AC1-AC2 output, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~16, queue position 2 (after `OG-hr-1`); edge `OG-ml-1` -> `OG-hr-2` (the `$select`).
- This is the byte-returning `$value` read NFRA_TRNSPT needs for bronze; MCP stays INSPECT-only.
- `<risk>` WORLD is GATE (xii)'s floor; the cell deploys nothing.

<status>staged</status>
<round>8</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
