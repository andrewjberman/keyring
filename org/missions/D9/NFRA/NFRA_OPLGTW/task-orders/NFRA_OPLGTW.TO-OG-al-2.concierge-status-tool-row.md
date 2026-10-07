# NFRA_OPLGTW task order -- `OG-al-2` -- ONE allowlist row: the scoped concierge identity may call `opal_data_refresh_status`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-al-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~29</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one text row and one test file; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the row is Andrew's word (org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_041xZ_CONCIERGE_MAY_CALL_DATA_REFRESH_STATUS_TOOL_YES.md @4403ac63df).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-al-2` (decomposition addendum R3-T.19, item 1)

`infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt` is the tracked overlay of `app/identity_scope.py`. Each row is
`<email> <tool> [client=<id>]`. A scoped identity may call only the tools its seed and this overlay name. The file's
own header says a widening is an Andrew ruling and every row carries its authorization.

Andrew ruled on 2026-10-07 ~04:1xZ ("rec approved"): the scoped Teams concierge identity may call
`opal_data_refresh_status`, the read-only status tool of release r25. One row, nothing else.

Do:
1. Append ONE row to `identity_tool_allowlist.txt`: the SAME identity the file's existing
   `opal_data_refresh_upload` row names, then `opal_data_refresh_status`.
   - NO `client=` qualifier. The ruling names the identity and the tool, not a client, and the tool only issues GETs.
   - Directly above the row, comment lines carry its authorization, in the file's existing style:
     - the date and the verbatim words `rec approved`;
     - the record's file name `ANDREW_DIRECT_20261007_041xZ_CONCIERGE_MAY_CALL_DATA_REFRESH_STATUS_TOOL_YES.md` and its
       commit `4403ac63df`;
     - one line saying it authorizes this one read-only tool and nothing else.
   - Change no other line of the file.
2. Add `tests/test_identity_scope_status_row.py`, offline, reading the TRACKED overlay through `app/identity_scope.py`'s
   own loader. Four named tests, `test_ogal2_ac01` to `test_ogal2_ac04`, as `al2.AC1.sh`'s header lists them.
3. Negative control: with the new row removed, `test_ogal2_ac01` fails. Record that run in `W/AL2_NEGATIVE_CONTROL.md`.
4. **AMENDMENT 1 -- the execution-id shape check (row `NFRA_OPLGTW-Z-S65`, `3.0.0_SA_CVO~O`; CTO ruling in msg 30563).**
   `opal_data_refresh_status(execution_id)` in `infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py`
   formats the caller's `execution_id` straight into the status URL path (`STATUS_PATH`, about `:73` and `:163-166`).
   - Before any request, refuse an id that is not a plain token: raise `IntegrationError` naming `execution_id` when it
     does not fully match ONE conservative pattern of letters, digits, `-`, `_` and `:`, 1 to 200 characters.
   - Read `infra/aws/lambda/data_refresh/lambda_function.py` (`handle_trigger`, `handle_status`) for the ids the portal
     really mints, and make sure every one of those shapes passes. Say in your report which shapes you found.
   - **AMENDMENT 2 (corrects A1's wording).** Inside `_read_status_once`, the send path, an id that fails the check
     makes NO request and the function returns `"UNKNOWN"`. It must NOT raise: by then `/trigger` has landed, and an
     error returned after a landed trigger is the lost-response failure of row Z-S63. Only the status TOOL raises.
     `test_ogal2_ac05` also asserts this: a send whose `/trigger` answer carries an empty or malformed `executionId`
     returns normally with pipeline status `UNKNOWN`, makes no status GET, and still records the send for the
     idempotent re-send.
   - Change nothing else in that file.
   - Add `tests/test_opal_portal_status_id_shape.py`, offline, with two named tests:
     - `test_ogal2_ac05`: ids containing `/`, `..`, `?`, `#`, `%2F`, a space or a newline are each refused, and NO HTTP
       request is made for any of them;
     - `test_ogal2_ac06`: a UUID-shaped id and every shape the portal mints are accepted and reach the status GET.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~29/`.

## 2. BOUNDS

- Do not edit `app/identity_scope.py`, its seed, `app/graph_scope_map.py` or any other gateway file, except the one
  shape check of item 4 in `app/integrations/opal_portal/integration.py`.
- No release and no host act: that is `OG-rl-12`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt
infra/aws/ec2/opal-gateway/tests/test_identity_scope_status_row.py
infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_portal_status_id_shape.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~29/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W29-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-al-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/al2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-al-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/al2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)allowlist rows added 1 \(want 1\), removed 0 \(want 0\); the row is the unqualified status-tool row for a known identity: True; authorization cited above it: True; guard test files green 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-al-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/al2.AC3.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 2 of 2; failed/error lines 0.*send-split tests still green: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the concierge is admitted for the status tool, nothing else widened, and its consent did not move.
- `AC2`: the diff is exactly that one row with its authorization above it, and the guard tests stay green.
- `AC3`: a malformed execution id is refused before any request, and the send-split tests stay green.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-al-2.concierge-status-tool-row.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If all three criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`.
4. Report once: literal AC output, the file diff, the negative control, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 25 (addendum R3-T.19, item 1), cut on `1.0.0_SA_CTO~O` msg 30555. Chain: `OG-al-2` -> `OG-rl-12`.
- Verbatim scope: the row is NOT client-qualified, because the ruling names the identity and the tool only. The
  existing upload row keeps its qualifier.
- AMENDMENT 2 (05:0xZ, issuer; GATE (viii) grades the modify): A1 told the send path to raise on a bad id. The
  worker's report showed that would raise AFTER a landed trigger. The send path now returns UNKNOWN instead; only the
  status tool raises. No criterion text changed; `test_ogal2_ac05` carries the new assertion.
- AMENDMENT 1 (04:4xZ, issuer, before the hand-off; GATE (viii) grades the modify): item 4 and `AC3` add the
  execution-id shape check of row Z-S65, which the CTO ruled into this same release (msg 30563). Pre-cut `al2.AC3` FAIL
  (the test file is absent).
- Pre-cut 04:3xZ: `al2.AC1` FAIL (the test file is absent). `al2.AC2` FAIL (0 rows added; guard files 2 of 2).

<status>complete</status>
<round>25</round>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
