# NFRA_OPLGTW task order -- `OG-en-4` -- client holdings state the weight unit and the currency per row (round 38 E4; CVO v30 ap-23 AC3 PARTIAL; CTO round-37 analysis section 2 ruling 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-4</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~118</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the tools' admission class is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (round-37 analysis `ledger/ROUND_ANALYSIS.round37.md` @afa8003488 section 2 ruling 3: "ap-23 PARTIAL is a defect of the envelope, not of admission. Client holdings state their weight unit (fraction or percent) and currency per row, from the adapter's source. It is a code cell that rides the next batched release") on the CVO's v30 grade (ADJUDICATION_v30.Z.md: "client holdings lack a weight unit and a currency").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-4` (decomposition addendum R3-T.93, round 38 item E4, workstream ENRICH-R38, FWD-22)

THE DEFECT. `client_get_holdings` answers a list of position rows; a row carries `weight` (a number) and, in some adapters, `weight_basis`, but NOT what unit the weight is in and NOT the currency of `market_value` and `price`. A reader cannot tell a fraction (0.12) from a percent (12), nor dollars from another currency. The CVO graded the first client answers PARTIAL on exactly this.

THE FIX (code only, in the gateway app). In each client adapter that builds position rows for `get_holdings` -- `app/client_adapter_bd49f.py`, `app/client_adapter_bdcottonwood.py`, `app/client_adapter_commonwealth.py`, `app/client_adapter_eclipse.py`, `app/client_adapter_orion.py`, `app/client_adapter_schwab.py`, `app/client_adapter_smartx.py` (read each file's `get_holdings`; the assembled envelope is in `app/client_core.py`) -- add to EVERY position row two keys:
1. `weight_unit`: the string `"fraction"` when the adapter computes `weight = market_value / total` (a number between 0 and 1), `"percent"` only if an adapter genuinely emits a 0-100 number. Read each adapter's own arithmetic; do NOT change any weight value.
2. `currency`: the currency code the adapter's SOURCE row carries for that position (read the source column/field in the adapter; use it verbatim, upper-cased). If the source carries no currency for the row, set `currency` to `null` and add `currency_basis: "source_absent"`; if it carries one, `currency_basis: "source"`. NEVER assume USD.
Where an adapter returns rows through a shared helper in `app/client_core.py`, put the keys there once instead of seven times, provided each adapter's own source currency still reaches it. Touch no admission, no entitlement, no tool registration.

TESTS (new file `tests/test_og_en4.py`; read an existing client adapter test such as `tests/test_og_cl*.py` for the fixture style; use each adapter's real row shape from its tests, never a made-up shape):
- `test_ogen4_ac01`: for each of the seven adapters, a position row from that adapter's real row shape carries `weight_unit` and `currency` and `currency_basis`.
- `test_ogen4_ac02`: the currency comes from the source: a source row with currency `EUR` yields `EUR`; a source row with no currency yields `null` and `source_absent`; no row ever yields an assumed `USD`.
- `test_ogen4_ac03`: `weight_unit` matches the arithmetic: where the adapter divides by the total the unit is `fraction` and the weight is unchanged from before (compare against the pre-change value computed in the test from the same inputs).
If a test elsewhere pins the exact key set of a position row, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no change to `app/data_entitlement.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print an account number or a person's name (a client row's account reference is masked `****<last4>`; keep it so).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/app/client_adapter_bdcottonwood.py
infra/aws/ec2/opal-gateway/app/client_adapter_commonwealth.py
infra/aws/ec2/opal-gateway/app/client_adapter_eclipse.py
infra/aws/ec2/opal-gateway/app/client_adapter_orion.py
infra/aws/ec2/opal-gateway/app/client_adapter_schwab.py
infra/aws/ec2/opal-gateway/app/client_adapter_smartx.py
infra/aws/ec2/opal-gateway/tests/test_og_en4.py
infra/aws/ec2/opal-gateway/tests/test_og_cl1.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_cl3.py
infra/aws/ec2/opal-gateway/tests/test_og_cl4.py
infra/aws/ec2/opal-gateway/tests/test_og_cl5.py
infra/aws/ec2/opal-gateway/tests/test_og_cl6.py
infra/aws/ec2/opal-gateway/tests/test_og_cl7.py
infra/aws/ec2/opal-gateway/tests/test_og_cl8.py
infra/aws/ec2/opal-gateway/tests/test_og_cl9.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE the app files and `tests/test_og_en4.py` and, only to follow the new truth, the existing `tests/test_og_cl*.py` files; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~118/`. Rows: id `NFRA_OPLGTW-Z-W118-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en4.py test_ogen4_ac01 test_ogen4_ac02 test_ogen4_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~118 '^infra/aws/ec2/opal-gateway/(app/client_(core|adapter_[a-z0-9]+)\.py|tests/test_og_(en4|cl[0-9]+)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~118: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the app client files and the client tests.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-4.holdings-unit-and-currency.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the adapters changed, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO round-37 analysis, ENRICHMENT LIST E4), workstream ENRICH-R38 (decomposition addendum R3-T.93). LOCAL; it rides the next BATCHED gateway release with E5, E6 and E8 (one release cell, one never-widen ask, cut after the builds merge).
- Cross-project note: `tests/test_og_gp1.py` and `tests/test_og_gf1.py` AC01 tests fail at HEAD since the MCPINDEX v2 catalog landed (18 classified rows absent from the catalog, the rest now carry `read_tool`); that is a separate cell (`OG-ts-1`), not this one.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

- A1 (issuer, 2026-10-16 ~12:4xZ, worker rows Z-W118-S2 and S3; merged `1a535637fd`; gate limb: none graded, a note and a status flip on a completed order): (1) S2: eclipse's `get_holdings` refuses before any read, so it builds no position row for the keys to ride on; the cell's "seven adapters" is met as six adapters carrying the keys plus eclipse's refusal pinned in the test. Ruled: the clause is satisfied; no eclipse change. (2) S3: orion passes the source `assetPercentOfAccount` through as `weight_pct` and its 0-100 scale is not established, so the worker named `weight_unit` null there rather than guess `percent`. Ruled: accepted as the honest answer; carried to the next round's enrichment list as "verify orion's weight scale against a real row, then name its unit" (not a hazard to what ships: no unit claimed). Currency is `null` with `currency_basis: source_absent` on every adapter whose source names none (worker row S1: no client read carries a currency column), never an assumed USD. The cell's work is complete and its criteria PASS (worker proof VALID); the `<status>` flip waits on one clerical point: the worker wrote its instance as `NFRA_OPLGTW.TO-OG-en-4.proof_of_spec.json` (no slug), and the L6 gate looks for `NFRA_OPLGTW.TO-OG-en-4.holdings-unit-and-currency.proof_of_spec.json` beside the order; the owning serial renames it (the lane gives the folder to that serial alone), then the flip lands.

<status>staged</status>
<round>38</round>
<workstream>ENRICH-R38</workstream>
<slot>~118</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
