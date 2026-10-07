# NFRA_OPLGTW task order -- `OG-sd-1` -- the status tool reads the served manifest's own date key (row Z-W28-S13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~32</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the tests run offline with fakes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's round-24 analysis (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round24.md @0e813364da).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-sd-1` (decomposition addendum R3-T.21, item 2)

`infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py` `_manifest_date` reads the served manifest's
displayed date from the first of eight candidate keys (`displayed_date`, `date`, `as_of`, `asof`, `vintage`,
`latest_date`, `data_date`, `updated`). The live served manifest carries none of them: its five top-level keys are
recorded in the evidence of row `NFRA_OPLGTW-Z-W28-S13` in
`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, and its date sits in
`generated_at`. So `opal_data_refresh_status` returns `displayed_date: null`, and the daily send's callers are told to
read that field.

Do:
1. Read the row's evidence and write the live manifest's top-level key set into `W/SD1_MANIFEST_KEYS.md`, with the
   row line you took it from. If the row does not name all five keys, say which are missing and file a row; do not
   call the portal to find out.
2. In `_manifest_date`, add the manifest's own date key (`generated_at`, if the row confirms it) to the candidates,
   AFTER the eight existing keys, so no manifest that resolved before resolves differently. Return the value as the
   manifest carries it; do not reformat it.
3. Change nothing else in the file: the send, the dedupe, the execution-id check, the status read and the text field
   all stay as they are.
4. Add `tests/test_opal_portal_status_displayed_date.py`, offline, with the three named tests `test_ogsd1_ac01` to
   `test_ogsd1_ac03` that the header of `sd1.AC1.sh` lists. Test 01's fixture carries exactly the key set of
   `W/SD1_MANIFEST_KEYS.md`.
5. Negative control: with your added key removed, `test_ogsd1_ac01` fails. Record that run in
   `W/SD1_NEGATIVE_CONTROL.md`.
6. Run `tests/test_opal_portal_send_split.py`, `tests/test_opal_portal_status_id_shape.py` and
   `tests/test_opal_portal_dedupe_content.py`, each in its own process, and state each file's totals.

The exercise of the tool through its wrapper with a real principal is NOT in this cell: it is a host read and belongs to
the release that ships this change.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~32/`.

## 2. BOUNDS

- No release and no host act. This cell is BUILT and HELD on your branch; the issuer drains it after release r26 closes.
- Never call a live gateway, portal or Graph route. The tests are offline.
- Never print or commit an email address, tid, oid, account id, credential or token.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py
infra/aws/ec2/opal-gateway/tests/test_opal_portal_status_displayed_date.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~32/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W32-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r27/checks/sd1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live manifest's key set yields its date; no date key yields null; the old keys resolve as before.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sd-1.status-tool-displayed-date.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output, the code diff, the negative control, each neighbouring test file you ran and its
   totals, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 26 (R3-T.21, item 2), cut on `ROUND_ANALYSIS.round24.md` @0e813364da section 3, row Z-W28-S13.
- The wrapper exercise with a real principal moves to the release order `OG-rl-13` as a post-deploy read.
- Same file as OG-al-2 and OG-up-2 (both complete and on CLOUD); it builds on CLOUD and is held until r26 closes.
- Pre-cut 10:5xZ: `sd1.AC1` FAIL (the test file is absent).

<status>pending</status>
<round>26</round>
<slot>~32</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
