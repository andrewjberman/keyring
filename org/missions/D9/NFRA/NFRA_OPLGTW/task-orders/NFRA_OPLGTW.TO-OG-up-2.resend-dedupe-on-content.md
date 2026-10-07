# NFRA_OPLGTW task order -- `OG-up-2` -- the re-send dedupe keys on CONTENT, not size (CTO R36)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-up-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~29</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the tests run offline with fakes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's ruling R36 (1.0.0_SA_CTO~O msg 30594).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-up-2` (decomposition addendum R3-T.20)

`infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py` holds an in-process record of recent real
sends (`_RECENT_SENDS`). A `confirm=True` call whose two files match a trigger made in the last 30 minutes returns that
execution with `already_triggered: true` and does not POST `/trigger` again.

The match is on file NAME and SIZE. That does not tell two pulls apart. Measured on 2026-10-06/07: three generations
of `model 20261005 v1.pkl` were each 17,919,590 bytes with different content. So a corrected re-pull whose files keep
their sizes is dropped, and the caller reads the stale served file as success.

Do, in that file:
1. **The signature is (name, size, content hash) per file.**
   - Read the hash from the SharePoint drive item the tool ALREADY resolves in `_graph_find_pkl`: the item's
     `file.hashes` (prefer `sha256Hash`, then `quickXorHash`, then `sha1Hash`), else the item's `cTag`.
   - Make no extra request and no second download for it. Return the hash from `_graph_find_pkl` beside `id` and `size`.
2. **If either file has an unreadable hash, do NOT dedupe: fire.** An unreadable hash is a missing `file.hashes` with a
   missing or empty `cTag`. The send then proceeds exactly as a first send, and it is still recorded.
3. The returned text on `already_triggered: true` says the match was on content, in one short sentence.
4. Change nothing else: the 30-minute window, the in-process record and its lock, the send split, the status tool, the
   execution-id check and the `dry_run` path all stay as they are.
5. Add `tests/test_opal_portal_dedupe_content.py`, offline, reusing the fakes of
   `tests/test_opal_portal_send_split.py`. Four named tests, `test_ogup2_ac01` to `test_ogup2_ac04`, as the header of
   `up2.AC1.sh` lists them. If an existing test in `test_opal_portal_send_split.py` or
   `test_opal_portal_status_id_shape.py` fakes a drive item without a hash, give that fake a hash rather than weakening
   the new rule; name each such change.
6. Negative control: with the signature restored to name and size only, `test_ogup2_ac01` fails. Record that run in
   `W/UP2_NEGATIVE_CONTROL.md`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~29/`.

## 2. BOUNDS

- No release and no host act: that is `OG-rl-12`.
- Never call the real upload or trigger routes. Never run `opal_data_refresh_upload` against the live gateway.
- Do not edit `identity_tool_allowlist.txt`, `app/identity_scope.py` or `app/graph_scope_map.py`. The drive item GET
  is the same request as today, so no Graph scope changes.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_portal_dedupe_content.py
infra/aws/ec2/opal-gateway/tests/test_opal_portal_send_split.py
infra/aws/ec2/opal-gateway/tests/test_opal_portal_status_id_shape.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~29/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W29-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-up-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/up2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-up-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/up2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test files green 5 of 5; allowlist and scope map changed since the cut: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a corrected re-pull of equal size fires; an identical one does not; an unreadable hash fires.
- `AC2`: the send split, the id check, the allowlist row and the consent tests all stay green.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-up-2.resend-dedupe-on-content.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output, the diff of the signature code, each test fake you changed, the negative control,
   commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 25, workstream SEND-DEDUPE-R36, cut on `1.0.0_SA_CTO~O` msg 30594 (R36) from the evidence in
  `0.0.0_AB_MSTR~Z` msg 30592 (`0.0.3_BG_BBGTerminal` msg 30591). It ships in r26 with OG-al-2. Chain: -> `OG-rl-12`.
- It follows OG-al-2 (complete, drained @5e9d9e8ae6) in the same file; the two do not run at once.
- Interim rule for callers, from the CTO: a corrected same-date re-send that returns `already_triggered: true` did NOT
  fire; re-send 30 minutes after the first send.
- Pre-cut 05:2xZ: `up2.AC1` FAIL (the test file is absent). `up2.AC2`: see the issuance commit.

<status>pending</status>
<round>25</round>
<workstream>SEND-DEDUPE-R36</workstream>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
