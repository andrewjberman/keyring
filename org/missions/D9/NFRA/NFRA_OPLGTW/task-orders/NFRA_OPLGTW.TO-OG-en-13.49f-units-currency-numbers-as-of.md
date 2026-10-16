# NFRA_OPLGTW task order -- `OG-en-13` -- the 49F live answers carry units and currency on every figure, serve numbers at sensible precision, set `as_of` from the partition date and drop duplicate profile rows (round 39 E2 and E3; CVO v35 AC3 findings 1 to 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-13</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-13</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~126</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the adapter reads the same partitions it reads today.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-38 analysis (`ledger/ROUND_ANALYSIS.round38.md` @faa77bd49e, E2 and E3) on the CVO's reading of the six live answer bodies (`surprise-channel/adjudications/ADJUDICATION_v35.Z.md`, findings 1 to 4).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-13` (decomposition addendum R3-T.99, round 39 items E2 and E3, workstream ENRICH-R39-B)

INPUT YOU READ FIRST. `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/E1_PARTITION_MEASURE.json` (the applier's measurement of the live data, order `OG-ev-2`): its `body.allocations.weight_scale` is `fraction`, `percent` or `unclear`. If the file is absent when you start, STOP with a BLOCKING row: the issuer spawns you after it exists.

THE GAP (all in `app/client_adapter_bd49f.py`, the 49F Black Diamond live adapter; read the whole file first, 509 lines):
1. `get_allocation` rows (`weights[]` and `market_value_profile[]`) carry `account_allocation` and `cash_allocation` with no unit. `get_transactions` rows carry `amount` and `get_fees` rows carry `amount` with no currency and no currency basis. Holdings already carry `weight_unit` and `_currency_keys(row)` (OG-en-4); use the same helpers and the same honesty.
2. The `market_value_profile` serves allocations as 24-decimal strings and market values as 6-decimal strings, and repeats identical rows. A holdings weight serves as 1e-05-style scientific notation and market values carry 14 significant digits.
3. Holdings and allocation answers carry `as_of: null` beside a real `partition_date`.

THE FIX (code only):
- **Units.** Add `weight_unit` to every allocation `weights[]` row, every `market_value_profile[]` row and the answer top level: `"fraction"` if the measure's `weight_scale` is `fraction`, `"percent"` if `percent`; if `unclear`, `null` plus `weight_unit_basis: "not_established"` (never a guess). Keep the value in a module constant (`ALLOCATION_WEIGHT_UNIT`) whose comment cites `E1_PARTITION_MEASURE.json`. Add `currency` and `currency_basis` to every `transactions[]` row, every `fees[]` row and the answer top level, through `_currency_keys(row)`; if the source columns constants (`TXN_COLUMNS`, the fees column constant) carry no currency column and the fixture schema has none, serve `currency: null, currency_basis: "source_absent"` without requesting a column that does not exist (the live holdings and unrealized tables carry none: the CVO read it). NEVER assume USD.
- **Numbers.** Serve every figure as a JSON number, never a string: allocation and holdings weights (`weight`, `account_allocation`, `cash_allocation`) rounded to 6 decimals; money (`market_value`, `account_market_value`, `cash_market_value`, `amount`) rounded to 2 decimals. A nonzero weight whose plain text would use an exponent (absolute value below 0.0001 after rounding) is served as `0.0` and its row carries `rounded_to_zero: true`; no figure prints with an exponent (`e` or `E` inside a number token) in the serialized JSON text.
- **as_of.** Where the answer's `as_of` is null because the caller gave none, set it to the `partition_date` of the partition read (the data's own date; read `_envelope`, which writes `_as_of` and `_partition_date`). An `as_of` the caller supplied is unchanged; an `absent` answer is unchanged.
- **Duplicates.** Drop exact duplicate rows from `market_value_profile` (equal on every emitted field; keep the first) and add `profile_duplicates_removed: <n>` to the answer.
Change no admission, no fence and no other adapter.

TESTS (new file `tests/test_og_en13.py`; read `tests/test_og_en4.py` and `tests/test_og_en12.py` for the fake-ctx fixtures):
- `test_ogen13_ac01`: allocation `weights[]` and `market_value_profile[]` rows carry `weight_unit` per the measure's `weight_scale` (test all three values by patching the constant: `fraction`, `percent`, and `unclear` giving null plus `not_established`); a profile with two identical rows serves one and `profile_duplicates_removed: 1`.
- `test_ogen13_ac02`: transactions and fees rows and both answers carry `currency` and `currency_basis` (`source_absent` for a source without the column; `source` and the upper-cased code for a fixture that carries a `currency` column); no row has a USD default.
- `test_ogen13_ac03`: in the SERIALIZED JSON text (`json.dumps`) of holdings, allocation, transactions and fees answers no figure is a string, no number token carries an exponent, weights have at most 6 and money at most 2 decimals; a weight of 0.00001 serves as 0.0 with `rounded_to_zero: true`; `as_of` equals `partition_date` when the caller gave none and the caller's own date when given.
If an existing test pins the old row shape (string figures, null `as_of`), update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no other adapter. (The windowed-partition change is the separate cell `OG-en-15`, which edits the same file after you: leave `get_transactions`/`get_fees` window logic and `window_partial` exactly as they are.)
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_en4.py
infra/aws/ec2/opal-gateway/tests/test_og_en12.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_ch1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_adapter_bd49f.py`, `tests/test_og_en13.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~126/`. Rows: id `NFRA_OPLGTW-Z-W126-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en13.py test_ogen13_ac01 test_ogen13_ac02 test_ogen13_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~126 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en13|en4|en12|cl2|ch1)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~126: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the listed files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-13.49f-units-currency-numbers-as-of.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39 E2 + E3, workstream ENRICH-R39-B (decomposition addendum R3-T.99). Risk WORLD by the L6 floor (a gateway infrastructure path); no deploy in this cell. Same worker queue as `OG-en-15` (same file): this order first, then `OG-en-15`. SPAWN waits on `OG-ev-2` (the allocation weight scale).
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>complete</status>
<round>39</round>
<workstream>ENRICH-R39-B</workstream>
<slot>~126</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
