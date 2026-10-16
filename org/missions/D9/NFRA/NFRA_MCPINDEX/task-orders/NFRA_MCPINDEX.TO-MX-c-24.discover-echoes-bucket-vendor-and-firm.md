# NFRA_MCPINDEX task order -- `MX-c-24` -- `opal_discover` echoes `bucket` on every silver answer whose row has one, and `vendor` and `firm` where the row has them

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-24</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-24</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~47</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change: the cell adds three catalog fields to an answer a principal may already see. No AWS call in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- the difference control (c24.AC2: the live tree `38fe44d5cb` against yours, every silver row x four principals) is the control; visibility is not touched.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-24` (round 19, enrichment E1 of the round-18 L10 answer)

Work in your own worktree (cut from `box/sitez`). Every path below is relative to its root. **First**, run once: `git sparse-checkout add infra/aws/ec2/opal-gateway workflows lib` (the only sparse change you may make). The code is `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, function `_silver_answer` (about line 630 to 691).

**Why.** The catalog rows now carry `bucket` on all 280 rows and `vendor` and `firm` on the 136 opal-data-assets / opal-data-bd rows (PRD v0.17 C-GROUP). `opal_discover` answers a silver row with its `bucket` only when the row carries a `contract` key (the `if "contract" in row:` branch that adds `bucket`, `prefix`, `fork_keys`, `contract`, `retired`). So the answer for the opal-data-bd row `blackdiamond_fees` (a row without `contract`) echoes no bucket, and no answer echoes `vendor` or `firm`. A person asking in plain words cannot see which bucket, vendor or firm a returned table belongs to. The probe `deliverables/2.0.0_SA_COO~MI/round18/discover_buckets.py` reads it today as: bucket echoed on 7 of 8 buckets; vendor and firm echoed on 0 of 2 (assets, bd).

**What to build.**

1. In `_silver_answer`, for the answer it already builds (after the existing `answer = {...}` and the `if "contract" in row:` block, before `return answer`), add:
   - `bucket`: the row's `bucket` when it is a non-empty string and the answer does not already carry `bucket` (the `contract` branch already sets it; do not reassign it or change its position);
   - `vendor`: the row's `vendor` when a non-empty string;
   - `firm`: the row's `firm` when a non-empty string.
   A row without the field gets no such key (no `null`, no empty string). Nothing else in the answer changes: not a value, not the key order of the existing keys, not the `servable` or `gate` logic, not the visibility rule above it.
2. The visibility rule is NOT touched: a principal that gets `None` today still gets `None`. A firm principal sees the echo only on a row it may already see.
3. No other function changes (not `_harvest_answer`, not `_answer_row`, not `discover`). Harvest answers already echo `bucket`; portal answers are out of scope.
4. **Tests**: a NEW file `infra/aws/ec2/opal-gateway/tests/test_discover_echo.py` with at least 6 tests that call `_silver_answer` on small inline rows (see `tests/test_firm_catalog_visibility.py` for how a `loaded` catalog and a row are built and for the principal constants): bucket echoed on a row without `contract`; bucket still equal on a row with `contract`; vendor and firm echoed on a row that has them; no `vendor` or `firm` key on a row without them; an empty-string field is not echoed; a firm principal gets `None` for a row of another firm (unchanged) and the echo for its own row; the existing keys are equal to what the function returned before (compare against a hand-written expected dict for one row).

### Steps

0. The sparse command above. Then `cd infra/aws/ec2/opal-gateway && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_opal_discover.py tests/test_firm_catalog_visibility.py` passes before you start (a control).
1. Make the change and the tests. Run the same pytest line with `tests/test_discover_echo.py` added (all pass).
2. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No catalog row, no entry file, no `DATA_CATALOG.yaml`, no other gateway file, no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. The existing answer must not change by one byte for an existing key (`c24.AC2` compares the live tree `38fe44d5cb` with yours on every silver row and four principals).
3. No firm, vendor or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token): read every value from the row.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `deliverables/2.0.0_SA_COO~MI/round19/checks/c24.AC1.sh`, `c24.AC2.sh`, `c24.AC3.sh` (python `c24_check.py`, `c24_answers.py`). Read them for exactly what is graded. Do not edit them.
6. Other workers (`~48`, `~49`) edit catalog entry files and the emitter at the same time (no shared file).
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_discover_echo.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~47/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W47-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-24" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c24.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR buckets probed 8; bucket echoed 8; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-24" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c24.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR answers 788; newly visible 0; altered base keys 0; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-24" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round19/checks/c24.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_discover_echo.py, test_opal_discover.py and test_firm_catalog_visibility.py; the new file holds at least 6 tests -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~47/NFRA_MCPINDEX.TO-MX-c-24.discover-echoes-bucket-vendor-and-firm.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where the count may differ, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) `integration.py` and the test file; (ii) the proof instance.
4. Report once, with: the change by function (lines added); the AC1 DENOMINATOR lines and the CHECK lines verbatim; the answer for one assets row and one bd row before and after (no more than 12 lines each, from your tests); the test count; the two commit shas.

The issuer then merges and carries the file to `MX-r-16`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 19, worker ~47, an independent chain. Source: CVO ADJUDICATION_v13 @c5ba2988f4 carried item 2 (`opal_discover` does not echo `bucket` on opal-data-bd matches nor vendor and firm on assets/bd matches), endorsed by the CTO as a round-19 enrichment (msg 35012). Base dry-runs: `c24.AC1` FAIL (192 of 197 bucket, 0 of 136 vendor, 0 of 136 firm; probe 7 of 8), `c24.AC2` FAIL (no answer gains a key; the control itself passes base-against-base), `c24.AC3` FAIL (no test file). Risk WORLD by the infra path; the cell changes no grant and no visibility.

**A1 (2.0.0_SA_COO~MI, ~14:4xZ), ruling on rows Z-W47-S1 and Z-W47-S2:** the step-0 control reads 2 failed at the base `00113acb2f`, so AC3 could not pass as written. Both are stale expectations in `tests/test_opal_discover.py` from earlier rounds, not behaviour defects: (a) `test_silver_row_fails_closed_on_cross_firm_visibility` asserts that no known firm gets any silver match for "what fees did Black Diamond charge"; since MX-c-19/23 (the `firm` field; the ruled and signed widening) `blackdiamond_fees` carries firm 49financial and its own firm sees it. (b) `test_schwab_ask_names_a_real_schwab_tool` expects `schwab_dim_position` first; since MX-c-23 the 12 `opal_data_assets_silver_schwab_<master>_dim_*` rows rank first. `<paths>` gains `infra/aws/ec2/opal-gateway/tests/test_opal_discover.py`. Resume and change ONLY these two tests: (a) for each known firm and each of the two asks, every `silver_datasets` match must be a row whose `firm` equals that firm (the same row read from `od._loaded()["catalog"]["silver_datasets"]`), no silver match may belong to another firm, the 49financial BD-fees ask must include `blackdiamond_fees`, and the `catalogued` assertion becomes "catalogued equals whether any match exists"; the unknown-firm and empty-firm arms and the last four lines stay as they are. (b) the first match's `dataset` must end with `_dim_position` and start with `schwab_` or `opal_data_assets_silver_schwab_`; nothing else in that test changes (the exact four `schwab_*` rows list stays: the 12 new rows do not start with `schwab_`). Then re-run AC3 (it must read `pytest rc=0`), update the instance, commit through safe-commit (LOCAL, one commit for the test file, one for the instance), report once. Gate limb that graded this amendment: none (a modification; no criterion changed).

<status>issued</status>
<round>19</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
