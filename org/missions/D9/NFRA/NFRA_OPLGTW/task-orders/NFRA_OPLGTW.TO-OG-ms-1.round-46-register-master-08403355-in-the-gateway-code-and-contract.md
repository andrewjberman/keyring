# NFRA_OPLGTW task order -- `OG-ms-1` -- CODE: register Schwab master `08403355` (0840, the Tax SMA master) in the gateway's entitlement code, audit set, contract (both copies) and scopes registry (round 46; Andrew-direct ~19:55Z 2026-10-19; the CTO's ruling (B): rides tonight's off-hours batch)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ms-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ms-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~165</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository edits only; no schedule, trigger or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no IAM edit in this order (`infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` already lists the `schwab/08403355/...` prefixes at lines 72-78; whether the LIVE role holds them is the applier's Phase A read, not yours).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew-direct ~19:55Z 2026-10-19 ("we need to add 0840 to her search ability for schwab. she has the 0824 and 0833 accounts at schwab, the smartx and black diamond masters. she needs the 0840 master too added to her entitlements"; record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261019_195xZ_ALYSSA_SCHWAB_MASTER_0840_ADD_TO_ENTITLEMENTS.md`), relayed by `1.0.0_SA_CTO~Z` msg 36102 and ruled (B) in msg 36104. The master 08403355 is the Tax SMA master 0840-3355; its S3 prefix `schwab/08403355/` holds silver tables `dim_position`, `dim_balance`, `dim_asset` and `dim_transaction` and a `meta/complete/` marker folder (read by the issuer).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ms-1` (decomposition addendum R3-T.123 amendment A6, round 46, workstream ENRICH-R46-F)

Your worktree is `C:/tmp/og-ms1` (branch `wk-NFRA_OPLGTW-165`), cut by the issuer from the `box/sitez` commit that carries this order. Work ONLY there; paths are relative to its root.

Register `08403355` wherever the gateway keeps its closed list of Schwab masters, and nowhere else. Make exactly these edits:

1. **`infra/aws/ec2/opal-gateway/app/data_entitlement.py` line 77:** `MASTERS = ("08242234", "08335338")` becomes `MASTERS = ("08242234", "08335338", "08403355")`.
2. **`infra/aws/ec2/opal-gateway/app/schwab_audit.py` line 70:** `_MASTERS = frozenset({"08242234", "08335338"})` gains `"08403355"` (same comment).
3. **`infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json`:** in `masters` add `"08403355": "TaxSMA"` after the `08335338` entry; in `data_prefixes` add the four lines `schwab/08403355/silver/dim_position/`, `.../dim_balance/`, `.../dim_asset/`, `.../dim_transaction/` after the `08335338` four, in that order; in `completion_prefixes` add `schwab/08403355/meta/complete/`. Change no other key. **Do not touch `target_instance_type`**: it already reads `t4g.large` here (the `OG-rz-1` edit).
4. **`org/standards/NFRA_OPLGTW_CONTRACT.json`:** the SAME contract, byte-for-byte equal to the deploy copy after your edit (`tests/test_grant_calendar_months.py::test_ogcm1_ac05` requires the two files byte-equal). **Defect to cure here:** `OG-rz-1` changed `target_instance_type` to `t4g.large` in the deploy copy only, so `test_ogcm1_ac05` fails today; the `org/standards` copy must therefore ALSO carry `t4g.large`, in addition to your three additions. After your edits `cmp` of the two files must print nothing. Keep line endings as they are.
5. **`infra/logic/registry/scopes.json`:** line 23, the `49financial` firm's `"masters": ["08242234", "08335338"]` gains `"08403355"`; and a new MASTER row for `08403355` beside the `08335338` row, with the same keys and shape as that row (`key`, `class` `MASTER`, `long`, `short` all `08403355`, `tenancy`, `firm` `49financial`, `vendor` `schwab`, `bucket`, `bucket_provisioned`, `aliases`): copy the `08335338` row and change only the three identifier fields. Keep the file's formatting.
6. **A new test file `infra/aws/ec2/opal-gateway/tests/test_og_ms1.py`** with exactly these tests (offline, no network): (a) `"08403355" in app.data_entitlement.MASTERS` and the contract's `masters` keys equal `set(MASTERS)`; (b) `app.schwab_audit._MASTERS` equals `set(MASTERS)`; (c) the contract's `data_prefixes` hold 4 prefixes per master for every master and `completion_prefixes` 1 per master; (d) the two contract copies are byte-equal; (e) a grant scope naming `08403355` with the accounts of one test account validates through the entitlement parser (`app.data_entitlement`'s scope parser: read how `tests/test_data_entitlement_guard.py` builds one) instead of raising `Malformed`. Mirror the style of the neighbouring tests.
7. If a neighbouring existing test asserts the CLOSED two-master set (a `MASTERS ==` comparison or a length 2), update only that assertion to three masters and list the test in your report; count the hits with the native Grep tool over `tests/` as the denominator.

**AMENDMENT A1 (issuer ruling on your row `Z-W165-S1`): edit `app/client_adapter_schwab.py` as the ONE adapter change, behaviour-preserving.** The adapter's alias gates (lines 152 and 186, `master not in de.MASTERS`) must keep refusing `08403355` as `master_not_registered`, because Andrew's word is a Schwab SEARCH entitlement and not a client-tools widening. Add `_ALIAS_MASTERS = ("08242234", "08335338")` after the imports (comment: the alias registry holds these two contract masters; independent of `data_entitlement.MASTERS`) and change BOTH gates to `master not in _ALIAS_MASTERS`. Nothing else in the adapter. `tests/test_og_cl1.py::test_ogcl1_ac12` then passes UNCHANGED (do not edit that test). Your channel row is not committed to your branch: restore `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` to its bytes at `7ea7a96bc627be60062396898f7a4b4764480361` in a NEW commit (`git show 7ea7a96bc627be60062396898f7a4b4764480361:<path> > <path>`, then commit that one path), so the branch's net change to the channel is zero; the issuer files the ruling row. **Do NOT touch:** any other line of the adapter, any `.tf` file, `deploy-to-ec2.sh`, `EC2_MANIFEST.json`, the unit file, or any other line. If something else needs `08403355` to work (a hard-coded master list elsewhere in `app/`), do NOT edit it: file a row `NFRA_OPLGTW-Z-W165-S<k>` and report it.

Run, from `infra/aws/ec2/opal-gateway/` in your worktree: `python3 -I -m pytest tests/test_og_ms1.py tests/test_grant_calendar_months.py tests/test_data_entitlement_guard.py tests/test_data_entitlement_family.py tests/test_entitlement_admin.py tests/test_og_cl1.py tests/test_schwab_query.py -q -p no:cacheprovider`. The ONLY failure allowed is `test_data_entitlement_guard.py::test_ogz1_ac08` (a route-set pin that already fails at the live ref); every other test passes.

Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPLGTW~165 <0.9.0_WK_NFRA_OPLGTW~165@opal.agent>" -F <msgfile> -- <the paths you changed>` (message file by the Write tool). Never push, rebase, stash, `checkout --` or `clean`.

## 2. BOUNDS

- Only the files above. No AWS call, no network, no deploy. `08403355` is the ONLY master added.
- No account id, tid, oid or e-mail in any file or report; counts and names only.
- REFUSE a criterion you cannot meet as written. File a row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/schwab_audit.py
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
org/standards/NFRA_OPLGTW_CONTRACT.json
infra/logic/registry/scopes.json
infra/aws/ec2/opal-gateway/tests/test_og_ms1.py
infra/aws/ec2/opal-gateway/tests/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; run from the repo root of YOUR worktree, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ms-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/ms1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)MASTERS names 08403355: yes; schwab_audit _MASTERS names 08403355: yes; contract masters 3 \(want 3\), data_prefixes 12 \(want 12\), completion_prefixes 3 \(want 3\): yes; the two contract copies byte-equal: yes; target_instance_type t4g\.large in both: yes.*scopes\.json firm masters 3 and a MASTER row for 08403355: yes; client adapter alias gates keep the two masters \(_ALIAS_MASTERS\): yes.*files changed against the merge-base \d+; outside the named set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ms-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/ms1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)named test files: \d+ passed, failed names \[test_ogz1_ac08\] \(allowed: test_ogz1_ac08 only\).*test_og_ms1: \d+ passed, 0 failed.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the master is registered in the code, the audit set, both contract copies (equal) and the scopes registry, and nothing else changed.
- `AC2`: the new tests and the six neighbouring files pass except the one carried red.

## 5. WHEN YOU ARE DONE

Report once in your final message: the commit hash, the output of both checks, the tests you changed with the denominator, and any other file you found hard-coding the two masters.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, a mid-round cell (CTO ruling (B), msg 36104), amendment A6 of R3-T.123. The grant write that gives Alyssa the master is a later applier cell (`OG-ms-2`); this cell only makes the master legal for a grant to name.
- Found by the issuer reading the code: a grant naming `08403355` is `Malformed` today (`MASTERS` has two); `client_adapter_schwab.py` already refuses it `master_not_registered`; the reader IAM `.tf` already lists its prefixes (live state not read).
- Defect of mine cured in step 4: `OG-rz-1`'s worker edited one of the two contract copies, so `test_ogcm1_ac05` fails at trunk; the `org/standards` copy is the twin.
- Pre-cut: `ms1.AC1` and `ms1.AC2` base FAIL as expected.
- A1 (issuer, 2026-10-19 ~20:5xZ), on worker ~165's row `Z-W165-S1`: adding `08403355` to `MASTERS` made the client adapter's alias gates (`master not in de.MASTERS`) admit it, so `test_ogcl1_ac12` failed; that would have widened the `client_*` tools to a master Andrew did not name. Ruled: the adapter keeps its own `_ALIAS_MASTERS` (the two contract masters), a behaviour-preserving edit; `ms1.AC1` (script and expect) gains the adapter line and the adapter in its named set. The worker's channel row is dropped from its branch by a restoring commit; the ruling is filed by the issuer. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>46</round>
<workstream>ENRICH-R46-F</workstream>
<slot>~165</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
