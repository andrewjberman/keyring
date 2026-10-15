# NFRA_OPLGTW task order -- `OG-cl-1` -- G2 client data: the shared core of the five client_* tools and the Schwab adapter

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~103</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one read-only probe; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; the vendor read roles and their never-widen asks belong to the release order that carries it. The probe reads with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @4356f15f16 (msg 34516, 2026-10-15) on PRD v3.6/v3.7, Andrew's question on why opal-data-assets has no tools, and the CRO's G2 census.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-cl-1` (decomposition addendum R3-T.72, workstream G2-BUILD, FWD-22)

Build the SHARED CORE of the five `client_*` tools and the SCHWAB adapter. Modules: `app/client_core.py` (the five tool functions, the shared envelope, firm canonicalization, the refusal handling, the vendor registry, the real `Ctx`), `app/client_role.py` (the vendor read-role clients) and `app/client_adapter_schwab.py`; tests `tests/test_og_cl1.py`; your probe `W/probe_schwab.py`.

Read, IN FULL and in this order: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_CLIENT_TOOLS_CONTRACT.md` (the five-tool contract: shared envelope, firm fence kinds, the eight decisions you must not re-open, each tool's section, the Black Diamond clauses, the NOT USED list), `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/G2_ADAPTER_PROTOCOL.md` (the seam every adapter is built against, with the fake `ctx` your tests start from), `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_ROLES.json` (the measured roles and prefixes), and the census part for your vendor under `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/` (`G2_assets_silver.md` and `parts/G2*.md`). Where the contract's per-vendor bullets name Schwab, those bullets are your spec; a bullet that says the vendor serves nothing is a REFUSAL arm with the contract's code, never an empty answer.

**The core (`app/client_core.py`).** Five TOP-LEVEL functions with exactly the tools' names and inputs: `client_resolve_account(firm, account_last4, platform=None, as_of=None)`, `client_get_holdings(firm, account, platform=None, as_of=None)`, `client_get_transactions(firm, account, platform=None, from_date=None, to_date=None)`, `client_get_allocation(firm, account, platform=None, as_of=None)`, `client_get_fees(firm, account, platform=None, from_date=None, to_date=None)`. Each: admits FIRST (the Opal-user check of `typed_scope.admit_scope`, before any S3 call); canonicalizes `firm` (`49financial`, `cottonwood`, `inflection`; aliases `49f` -> `49financial`, `orion/4698` and `4698` -> `inflection`; anything else refused `firm_not_canonical`); refuses a last-4 or a bare number where an `account_ref` is required (`account_not_resolved`); routes by the vendor carried in `account_ref` (`resolve` asks EVERY registered adapter whose `FIRMS` holds the firm and merges the candidate lists); builds the shared envelope from the adapter's `_`-keys exactly as the protocol says (`as_of`, `partition_date`, `source_keys`, `denominator`, `absent_reason`, `platform_label`, `platform_label_source`, `label_claim`, `freshness_td`); catches any exception carrying a `.code` and answers it as an enveloped refusal with that `absent_reason`; projects to 50 KB. The vendor registry is a dict filled by a function `register_adapter(module)` that the ISSUER calls at the hookup (you register only the Schwab adapter in your own test through that function; the core imports no adapter at module level). The core also implements the real `Ctx` of the protocol over `typed_scope` and the DATA_CATALOG rows (`prefix`, `list_partitions`, `newest_partition`, `read_rows` of ONE partition, `freshness_td` from `lib/trading_calendar.py`, `firm_segments` from a table in the core read from the contract's fence kinds).
**The role module (`app/client_role.py`).** `s3_client(vendor)` returns an S3 client built from credentials assumed from an environment variable named for the vendor (read the existing pattern in `app/integrations/schwab/aws_roles.py` and `app/internal_role.py` and mirror it; return `None` when the variable is unset so the caller falls back to a lazily created default client, as the other tools do under the probe). It NEVER uses `INTERNAL_READER_ROLE_ARN`: client data does not read through the internal reader role (PRD v3.2).
**The Schwab adapter (`app/client_adapter_schwab.py`)** per the protocol and the Schwab bullets of every tool section: three masters (08242234, 08335338, 08403355; the masters are key segments, read their ids from the catalog rows or the contract, never typed twice), DEDUPE by account across masters and never sum across them (decision 2), `no_resolve_source` and `platform_enum_open` refusals as the contract names them, weights derived from `dim_position` and `dim_balance` for allocation (`no_model_source` for a model assignment), `no_fee_source`.
**Your probe** (`W/probe_schwab.py`; the issuer re-runs it as AC2): it runs the REAL core and the Schwab adapter against the real Schwab silver with the box's credentials (`INTERNAL_READER_ROLE_ARN` and any vendor role variable unset) and an Opal stand-in principal; for one real account it finds INDEPENDENTLY (boto3 + pyarrow), it asserts (a) the envelope is complete on a real `client_get_holdings` answer, (b) the position count equals the independent read of the same partition, (c) the fence negative arm: a request for firm `cottonwood` reads zero Schwab keys and is refused, (d) no account number reaches stdout. It prints exactly one line `probe schwab: envelope_ok <bool>; independent_count_equal <bool>; fence_negative_arm <bool>; account_numbers_printed <int>`.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py`: `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; call it FIRST, before any S3 call), `list_keys`, `newest_part`, `read_parquet(scope, key, columns, filters)`, `read_json`, and the re-exports `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope. `app/etfs_funds.py` and `app/etfs_rivals.py` (merged) are the closest models of a module on this seam: mirror their top (catalog helper by `entity`, served prefixes computed from rows, lazily created client) and never edit them.
KEYS COME FROM THE CATALOG (CTO ruling msg 34173): the gateway CODE types NO S3 bucket, prefix or key literal (the commit-time naming limb refuses legacy layouts and graded tool names ending in `_group`). Each bucket and key template is read at call time from the table's DATA_CATALOG row (`app/integrations/portal_index/integration.py` `runtime_catalog()`; catalog v0.5 is live). A row not found or retired is an `absent_reason` with zero reads. Do NOT write `app/refs/DATA_CATALOG.yaml`. Every tool answers with the envelope (`as_of`, `source_keys`, `denominator`, `absent_reason`), projected to 50 KB (narrow wide rows to the columns a reader asks about and name the dropped columns once in `columns_dropped`).

### Tests, named (a recording fake, in-memory rows and a synthetic catalog fixture with the same shape; an Opal stand-in principal)

- `test_ogcl1_ac01`: CORE: `firm` canonicalization (the aliases and `firm_not_canonical`), a last-4 refused `account_not_resolved` where a ref is required, non-Opal and absent principals refused every tool with ZERO reads.
- `test_ogcl1_ac02`: CORE: the shared envelope is built from an adapter's `_`-keys (a fake adapter), the `_`-keys are stripped, `freshness_td` is a number, and an exception carrying `.code` becomes an enveloped refusal with that `absent_reason`.
- `test_ogcl1_ac03`: CORE: `client_resolve_account` merges the candidate lists of every registered adapter that holds the firm, never picks one, and each candidate carries a masked `account_ref` with its vendor; the core imports no adapter at module level.
- `test_ogcl1_ac04`: CORE: the real `Ctx` reads ONE partition per `read_rows`, names no bucket or prefix literal (the prefix comes from a synthetic catalog row), `no_catalog_row` costs zero reads, and `app/client_role.py` never reads `INTERNAL_READER_ROLE_ARN`.
- `test_ogcl1_ac05`: SCHWAB: `resolve_account` for Schwab returns the candidate list (never one picked) with masked `account_ref`, `collisions` and the source's own platform label, or raises the contract's refusal code where the contract says the vendor has no resolve source.
- `test_ogcl1_ac06`: SCHWAB: `get_holdings` reads ONE partition (the newest at or before `as_of`), returns the positions and cash of the resolved account with the envelope fields, and refuses with the contract's code where the vendor has no holdings table.
- `test_ogcl1_ac07`: SCHWAB: `get_transactions` honours `from_date` and `to_date`, reads event files over the window only where the contract says so, never sums a snapshot table across partitions, and refuses with the contract's code where there is no source.
- `test_ogcl1_ac08`: SCHWAB: `get_allocation` returns the account's allocation or weights as the contract says (with `absent_reason` for a missing model assignment) and states the partition lag in trading days.
- `test_ogcl1_ac09`: SCHWAB: `get_fees` returns the fee rows or refuses `no_fee_source` (or the contract's code for this vendor), never reading a fee-schedule table as fee rows.
- `test_ogcl1_ac10`: SCHWAB: FENCE: a request for one canonical firm reads only that firm's key segments (`ctx.reads` names none of another firm's), a firm outside the vendor's `FIRMS` is refused, and an `account_ref` of another firm's segment is refused.
- `test_ogcl1_ac11`: SCHWAB: PRIVACY AND REFUSALS: no full account number appears in any returned body, key list or exception text (only the masked `account_ref`); every contract refusal code of this vendor is raised with its exact code; a table with no catalog row raises `no_catalog_row` with zero reads.
- `test_ogcl1_ac12`: SCHWAB: an account present under two masters is returned ONCE (deduped by account) and its balance is not summed across masters; master 08403355 is admitted as a segment; a `platform` filter is refused `platform_enum_open`.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers every tool and re-pins the counts at the merge, in one commit. Name the registrations you expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, a full email address, an account number or an amount, or any object's content, into a report, a row or a log (counts and booleans only); write the catalog file; override a gate. Tool names must not end in `_group` or `_role` (the naming gate refuses them).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_role.py
infra/aws/ec2/opal-gateway/app/client_adapter_schwab.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/aws_roles.py
infra/aws/ec2/opal-gateway/tests/test_og_cl1.py
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

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~103/`. Rows: id `NFRA_OPLGTW-Z-W103-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 12 of 12; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)probe schwab: envelope_ok True; independent_count_equal True; fence_negative_arm True; account_numbers_printed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the named tests pass. `AC2`: the probe, re-run here against the real Schwab silver, prints a complete envelope, a position count equal to an independent read, a refused firm fence and no account number.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-1.client-core-schwab.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-BUILD (decomposition addendum R3-T.72). CTO ruling @4356f15f16 (msg 34516): G2 and the G3/G5 remainders are BUILD cells, they do not wait on a release slot; they rejoin the release queue after OG-ap-22, ahead of OG-ap-17. Each vendor adapter needs its own prefix-conditioned read role and never-widen ask at its release; client data never reads through `gateway-global-internal-reader-role` (PRD v3.2).
- The hookup (registrations, lists, pins) belongs to no cell (CUT BY WRITE SET): the issuer cuts one hookup order per merged batch.
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe or record absent).

- A2 (issuer, 2026-10-15 ~20:0xZ, worker rows Z-W103-S1..S8, all read; the AC1 core and Schwab tests pass 12 of 12): the first seat's AC2 fails on facts the order could not know, ruled here. (S2) The Schwab silver tables the contract names (`dim_position`, `dim_balance`, `dim_transaction`, `dim_asset`) EXIST in the bucket (the issuer listed `schwab/<master>/silver/` with boto3: `dim_asset`, `dim_balance`, `dim_position`, `dim_transaction` and the `fact_*` tables) but the catalog v0.5 carries only the `fact_*` rows: a catalog gap that `NFRA_MCPINDEX` closes in its ASSETS workstream (the issuer asks `2.0.0_SA_COO~MI` for the twelve rows). RULED: production `ctx.prefix()` keeps refusing `no_catalog_row` for a table with no row (the adapter's answer is an enveloped refusal until the rows land, never a typed key); your PROBE's `ProbeCtx` falls back, for a MISSING row only, to the contract's served-key form `<vendor>/<master>/silver/<table>/` of the bucket the catalog gives for the neighbouring `fact_*` row, and prints `catalog_rows_absent <n>` in the probe's own diagnostics (not on the AC2 line). Do NOT substitute a `fact_*` table. (S3, S4, S5) Schwab account references: the Schwab account-reference mechanism that already exists in `app/integrations/schwab/` (its alias registry and the secret it reads) is the ONLY way an `account_ref` for Schwab is minted today; `client_resolve_account` stays `no_resolve_source` for Schwab (contract), and the other four tools take a ref minted by that mechanism, written in the protocol's form `****<last4>/<vendor>/<alias>` (vendor-prefixed: the alias carries no vendor, so the adapter prepends `schwab`). Your probe sets a THROWAWAY secret in-process (never a real one, never printed) through the same seam the adapter reads the secret by (a function the probe can patch), mints a ref for one real account it finds INDEPENDENTLY, and uses it. The registry holds two masters today, so an account of master 08403355 cannot be minted: the adapter refuses it `master_not_registered` and the master stays a segment in the fence (S4). (S6) the roster key `firm_roster` is the protocol's A1 item 4: accepted. (S7) the five non-contract refusal codes are ACCEPTED: list them in the module's refusal table with one line each and put the list in your report. Collision flag, noted by the worker and accepted as a release item: `client_role` reads `SCHWAB_READER_ROLE_ARN`, the variable the existing Schwab integration reads; the release cell decides whether they share the role (they do: `gateway-schwab-read-role`), so no rename is needed. (S8) the gate's REFUSE on firm-name literals in a WARN window is a conformance item the issuer carries to a later cell; do not work around it here. The first seat's commits `5c8c1554e5` and `7360812198` are inherited state: re-record the proof instance. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>G2-BUILD</workstream>
<slot>~103</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
