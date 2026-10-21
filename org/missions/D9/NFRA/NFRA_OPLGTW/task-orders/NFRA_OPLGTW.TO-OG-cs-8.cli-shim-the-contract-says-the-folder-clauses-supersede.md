# NFRA_OPLGTW task order -- `OG-cs-8` -- the contract revision: its per-account, per-column and masked-account-reference clauses are stated as superseded for folder grants (cli-shim workstream, wave 2; PRD v3.19 FWD-24 DONE WHEN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-8</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-8</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~184</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two data files and a test; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is PRD v3.19 FWD-24's DONE WHEN ("the contract's per-account, per-column and masked-reference clauses are revised to say they are superseded"), ADMITTED, applied as a statement in the contract file with no behaviour change.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cs-8` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-B, wave 2)

WHY. PRD v3.19 FWD-24 says a person's entitlement is a bucket or a folder and nothing else, so the contract file's per-account, per-column and masked-reference clauses no longer describe the folder tools. The contract has two byte-equal copies: `infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json` (the deploy copy) and `org/standards/NFRA_OPLGTW_CONTRACT.json` (the standards copy; a test requires them equal). Each is `contract_version` `"1.4"` today (blob `e24c1fcc85`). This cell states the supersession in both, and changes nothing else.

DO, in the TWO contract files and one new test (nothing else):

1. In BOTH files, by TEXT edit (do not parse and re-dump: the formatting of every other line must stay exactly as it is):
   - change the line `  "contract_version": "1.4",` to `  "contract_version": "1.5",`;
   - insert this block directly after the line `  "activation": "DESIGN_ONLY_NOT_A_GRANT",`, indented as shown (two spaces for the key, four inside), with the trailing comma after the closing brace:
```
  "fwd24_supersession": {
    "authority": "org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md FWD-24 (v3.19)",
    "applies_to": "the folder tools (folder_list, folder_describe, folder_query) and the folder strings a person_access record carries in channels_allow and channels_deny",
    "superseded_clauses": ["per_account_grant", "per_column_grant", "masked_account_reference"],
    "meaning": "for a folder grant the entitlement is the bucket or the folder named, and nothing else: a granted folder shows exactly what the AWS CLI would show for it, apart from five column classes dropped by name (tax identifiers, mailing addresses, email addresses, phone numbers, date of birth) and never reaching a bronze or raw prefix",
    "unchanged": "the schwab_* tools keep this contract's per-master, per-account, per-column and per-date grant until the folder tools are proven and the tools they replace retire"
  },
```
   The two files must end BYTE-EQUAL (copy the first edited file over the second after you check it; same line endings as the original, which are `\n`).
2. NEW `tests/test_cs8_contract_supersession.py` (under `infra/aws/ec2/opal-gateway/`), at least THREE tests, offline, reading the two files by path relative to the repository root (model on the copy-equal test in `tests/test_og_sk2.py`: read how it finds the two copies): both copies parse; they are byte-equal; `contract_version` is `"1.5"`; `fwd24_supersession.superseded_clauses` is exactly `["per_account_grant", "per_column_grant", "masked_account_reference"]` and its other four keys are non-empty strings; every key the pin had is still there with the same value (`masters`, `datasets`, `limits`, `tools` and `rolling_window` are enough: compare against literals you copy from the pre-edit file).

## 2. BOUNDS

- Write only the three files above, `W/` and, if a row is needed, the channel. No other file, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
org/standards/NFRA_OPLGTW_CONTRACT.json
infra/aws/ec2/opal-gateway/tests/test_cs8_contract_supersession.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~184/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W184-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs8.AC1.sh; echo "exit=$?"</invocation><expect>(?s)both copies parse and are byte-equal: ok.*contract_version is 1\.5 and fwd24_supersession holds its five keys with the three superseded clauses: ok.*nothing else moved: the document minus the new key equals the pin \(hunks [12], removed 1, added \d+\): ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs_foot.sh org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-8.cli-shim-the-contract-says-the-folder-clauses-supersede.md deploy/NFRA_OPLGTW_CONTRACT.json,tests/test_cs8_contract_supersession.py tests/test_cs8_contract_supersession.py 3 tests/test_og_sk2.py tests/test_og_mg3.py tests/test_schwab_catalog.py tests/test_grant_calendar_months.py; echo "exit=$?"</invocation><expect>(?s)files that differ from HEAD under the gateway folder: .*: ok.*tests/test_cs8_contract_supersession\.py: [3-9]\d* test functions.*: ok.*new file tests/test_cs8_contract_supersession\.py: [3-9]\d* passed, 0 failed.*neighbours \(4\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the two copies, byte-equal, the statement present and nothing else moved, graded by an issuer-written probe. `AC2`: the footprint under the gateway folder is the deploy copy and your test, and your test plus four neighbours that read the contract pass (the standards copy is covered by `AC1`'s equality).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-8.cli-shim-the-contract-says-the-folder-clauses-supersede.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-8.cli-shim-the-contract-says-the-folder-clauses-supersede.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-B, wave 2, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`. Source: PRD v3.19 FWD-24 DONE WHEN; the CTO's msgs 36299 and 36308.
- Widening, plainly: none (a statement in a design file; `activation` stays `DESIGN_ONLY_NOT_A_GRANT`). The supersession statement applies to the folder tools only; the `schwab_*` tools keep their grants.
- Pre-cut: `AC1` base FAIL as expected (no `fwd24_supersession`, version 1.4); `AC2` base FAIL as expected (the new test absent). Pin: both contract copies are blob `e24c1fcc85` at the cut.

<status>pending</status>
<round>48</round>
<workstream>CLISHIM-B</workstream>
<slot>~184</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
