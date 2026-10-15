# NFRA_OPLGTW task order -- `OG-cl-2` -- G2 client data: the Black Diamond 49F adapter

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~104</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one read-only probe; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; the vendor read roles and their never-widen asks belong to the release order that carries it. The probe reads with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @4356f15f16 (msg 34516, 2026-10-15) on PRD v3.6/v3.7, Andrew's question on why opal-data-assets has no tools, and the CRO's G2 census.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-cl-2` (decomposition addendum R3-T.72, workstream G2-BUILD, FWD-22)

Build the Black Diamond 49F adapter behind the five `client_*` tools (`client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees`): `app/client_adapter_bd49f.py`, tests `tests/test_og_cl2.py`, and your probe `W/probe_bd49f.py`.

Read, IN FULL and in this order: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_CLIENT_TOOLS_CONTRACT.md` (the five-tool contract: shared envelope, firm fence kinds, the eight decisions you must not re-open, each tool's section, the Black Diamond clauses, the NOT USED list), `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/G2_ADAPTER_PROTOCOL.md` (the seam every adapter is built against, with the fake `ctx` your tests start from), `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_ROLES.json` (the measured roles and prefixes), and the census part for your vendor under `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/` (`G2_assets_silver.md` and `parts/G2*.md`). Where the contract's per-vendor bullets name Black Diamond 49F, those bullets are your spec; a bullet that says the vendor serves nothing is a REFUSAL arm with the contract's code, never an empty answer.

**49F override (the CTO's ruling @4356f15f16 and PRD v3.6/v3.7, Andrew's 49F word):** the contract's A2 text says 49F reads only `opal-data-assets/blackdiamond/49f/silver/` and refuses holdings, transactions and fees as `no_source_49f_a2`. For 49F Black Diamond that is REPLACED: this adapter ALSO reads the live `opal-data-bd/silver/` tables through its own scoped role (catalog rows of bucket `opal-data-bd`; census part `parts/G2f_bd_live_prefixes.md`): holdings from `unrealized`, transactions from `transactions`, allocation from `allocations` (and `fact_bd_allocation` in the assets bucket for the market-value profile), fees from `fees`; resolve stays `dim_account_xref`. Every account id there is `z08` (the 49F segment): assert it as the fence. The lag in trading days is stated on every answer (tables are 0-2 td behind; `assets` 80 and `transactions_enriched` 122 are NOT read). Measure the increment-versus-snapshot grain of each table you read BEFORE you sum or span dates (contract open item 8) and state the result in your report; until measured a tool answers one partition only.

**Your probe** (`W/probe_bd49f.py`, a script you write and run; the issuer re-runs it as AC2): it builds the adapter's context against the REAL silver with the box's credentials (`INTERNAL_READER_ROLE_ARN` unset) and an Opal stand-in principal, and asserts for the vendor's firm(s): (a) the envelope is complete on a real answer; (b) an independent boto3 + pyarrow read of the same partition gives the SAME row count the tool reports in its `denominator`; (c) the FENCE NEGATIVE ARM: a request naming firm `49financial` of Black Diamond reads zero rows of any other firm's segment (assert on the keys read); (d) no account number reaches stdout. It prints exactly one line `probe bd49f: envelope_ok <bool>; independent_count_equal <bool>; fence_negative_arm <bool>; account_numbers_printed <int>` and nothing else that contains eight or more digits in a row.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py`: `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; call it FIRST, before any S3 call), `list_keys`, `newest_part`, `read_parquet(scope, key, columns, filters)`, `read_json`, and the re-exports `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope. `app/etfs_funds.py` and `app/etfs_rivals.py` (merged) are the closest models of a module on this seam: mirror their top (catalog helper by `entity`, served prefixes computed from rows, lazily created client) and never edit them.
KEYS COME FROM THE CATALOG (CTO ruling msg 34173): the gateway CODE types NO S3 bucket, prefix or key literal (the commit-time naming limb refuses legacy layouts and graded tool names ending in `_group`). Each bucket and key template is read at call time from the table's DATA_CATALOG row (`app/integrations/portal_index/integration.py` `runtime_catalog()`; catalog v0.5 is live). A row not found or retired is an `absent_reason` with zero reads. Do NOT write `app/refs/DATA_CATALOG.yaml`. Every tool answers with the envelope (`as_of`, `source_keys`, `denominator`, `absent_reason`), projected to 50 KB (narrow wide rows to the columns a reader asks about and name the dropped columns once in `columns_dropped`).

### Tests, named (a recording fake, in-memory rows and a synthetic catalog fixture with the same shape; an Opal stand-in principal)

- `test_ogcl2_ac01`: `resolve_account` for Black Diamond 49F returns the candidate list (never one picked) with masked `account_ref`, `collisions` and the source's own platform label, or raises the contract's refusal code where the contract says the vendor has no resolve source.
- `test_ogcl2_ac02`: `get_holdings` reads ONE partition (the newest at or before `as_of`), returns the positions and cash of the resolved account with the envelope fields, and refuses with the contract's code where the vendor has no holdings table.
- `test_ogcl2_ac03`: `get_transactions` honours `from_date` and `to_date`, reads event files over the window only where the contract says so, never sums a snapshot table across partitions, and refuses with the contract's code where there is no source.
- `test_ogcl2_ac04`: `get_allocation` returns the account's allocation or weights as the contract says (with `absent_reason` for a missing model assignment) and states the partition lag in trading days.
- `test_ogcl2_ac05`: `get_fees` returns the fee rows or refuses `no_fee_source` (or the contract's code for this vendor), never reading a fee-schedule table as fee rows.
- `test_ogcl2_ac06`: FENCE: a request for one canonical firm reads only that firm's key segments (`ctx.reads` names none of another firm's), a firm outside the vendor's `FIRMS` is refused, and an `account_ref` of another firm's segment is refused.
- `test_ogcl2_ac07`: PRIVACY AND REFUSALS: no full account number appears in any returned body, key list or exception text (only the masked `account_ref`); every contract refusal code of this vendor is raised with its exact code; a table with no catalog row raises `no_catalog_row` with zero reads.
- `test_ogcl2_ac08`: BD 49F: holdings, transactions, allocation and fees read the `opal-data-bd` rows (no `no_source_49f_a2` refusal), every returned account id belongs to the `z08` segment, and a grain not yet measured makes the tool answer one partition only and say so.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers every tool and re-pins the counts at the merge, in one commit. Name the registrations you expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, a full email address, an account number or an amount, or any object's content, into a report, a row or a log (counts and booleans only); write the catalog file; override a gate. Tool names must not end in `_group` or `_role` (the naming gate refuses them).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_CLIENT_TOOLS_CONTRACT.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_ROLES.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/G2_ADAPTER_PROTOCOL.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G2_assets_silver.md
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~104/`. Rows: id `NFRA_OPLGTW-Z-W104-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 8 of 8; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cl-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)probe bd49f: envelope_ok True; independent_count_equal True; fence_negative_arm True; account_numbers_printed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the named tests pass. `AC2`: the probe, re-run here against the real silver, prints the complete envelope, a count equal to an independent read, a zero-row fence negative arm and no account number.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-2.client_bd49f.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-BUILD (decomposition addendum R3-T.72). CTO ruling @4356f15f16 (msg 34516): G2 and the G3/G5 remainders are BUILD cells, they do not wait on a release slot; they rejoin the release queue after OG-ap-22, ahead of OG-ap-17. Each vendor adapter needs its own prefix-conditioned read role and never-widen ask at its release; client data never reads through `gateway-global-internal-reader-role` (PRD v3.2).
- The hookup (registrations, lists, pins) belongs to no cell (CUT BY WRITE SET): the issuer cuts one hookup order per merged batch.
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe or record absent).

<status>pending</status>
<round>37</round>
<workstream>G2-BUILD</workstream>
<slot>~104</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
