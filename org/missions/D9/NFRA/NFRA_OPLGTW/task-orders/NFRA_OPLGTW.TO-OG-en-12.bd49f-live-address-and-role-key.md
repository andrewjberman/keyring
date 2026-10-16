# NFRA_OPLGTW task order -- `OG-en-12` -- the 49F live tables resolve through the catalog row's `address` and read through a dedicated -live role key (round 38; CTO rulings @ed33f552ae and @8b2865e461; rows Z-S292 and Z-S293)

<!-- ===================== THE WORKER FACE IS EVERYTHING UP TO THE RECORD FACE MARKER ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-12</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-12</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~125</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is the later batched applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell; the dedicated read role it routes to is the applier order `OG-ap-29` (three never-widen halves), applied before the release.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's rulings (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md` @ed33f552ae: "(a) an `address` field on the four rows, real prefix kept, unique address, row's own bucket; (b) refused" and @8b2865e461: "-live routes to a dedicated read-only role on exactly opal-data-bd/silver/{unrealized,transactions,allocations,fees}/ (v3.6 item 2), never-widen with three halves; blackdiamond49f keeps its Deny. ~O: the code, the role and the ask") on the CVO's row Z-S292 and the applier's row Z-S293, PRD v3.6 (Andrew-direct 2026-10-14: "We can allow 49F Black Diamond pulls from opal-data-bd").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-12` (decomposition addendum R3-T.96, round 38, workstream ENRICH-R38-D, FWD-22)

WHAT IS KNOWN (read the code first; the line numbers are the issuer's reading, to check). The 49F Black Diamond adapter (`app/client_adapter_bd49f.py`) asks `ctx.prefix("blackdiamond", "49f-live", "silver", <table>)` for `<table>` in `unrealized`, `transactions`, `allocations`, `fees` (its `_live_prefix`, about line 252). `app/client_core.py` `Ctx.prefix` (about line 242) returns the key `blackdiamond/49f-live/silver/<table>/` only for a non-retired catalog row whose `prefix` EQUALS it with the same `layer` and `table`; `Ctx._row` and `Ctx._scope` (about 232-257) resolve by `prefix` too and take the row's `bucket`, and `typed_scope.list_keys` lists with the prefix verbatim. The four opal-data-bd rows exist in the catalog with `prefix: silver/<table>/` (so the lookup refuses `no_catalog_row`: row Z-S293), and `s3://opal-data-bd/blackdiamond/49f-live/` holds nothing. `app/client_role.py` `role_key` (about line 34) strips a trailing `-live` so the live tables go through `blackdiamond49f`, the role whose policy explicitly DENIES every opal-data-bd key (row Z-S292).

THE RULING. (a) The four catalog rows gain an `address` field (NFRA_MCPINDEX writes it: `address: blackdiamond/49f-live/silver/<table>/`, the row's real `prefix` `silver/<table>/` KEPT, its own `bucket` `opal-data-bd`, the address unique). The code: a row that carries an `address` is found by it, and the S3 reads and listings use the row's REAL `prefix` in the row's own `bucket`. (b) is refused (the adapter does not build `silver/<t>/` itself). (c) `-live` routes to a DEDICATED role key, not `blackdiamond49f`.

BUILD, in `app/client_core.py` and `app/client_role.py` only (and `app/client_adapter_bd49f.py` only if a line there must follow; the adapter should need none):
1. `Ctx.prefix(vendor, segment, layer, table)`: build `want` as today; return `want` when a row matches by `address == want` (when the row has an `address`) OR by `prefix == want` (a row with no `address`: today's behaviour, unchanged), in both cases requiring the same `layer` and `table`. Add a small private helper that maps a returned key back to its row (by address first, then prefix) and use it in `_row`, `_scope` and `list_partitions` and every read path in the class that takes a prefix, so that: the Scope's bucket is the row's `bucket`; the listed/read S3 prefix is the row's REAL `prefix` (not the address); the partition tail is cut at the real prefix; and the key handed back to the adapter for object reads is a real key under the real prefix. An address never reaches S3.
2. `client_role.role_key(vendor, segment)`: a firm-keyed vendor whose segment ends `-live` returns the key with the suffix `live` appended instead of stripped (`blackdiamond/49f-live` -> `blackdiamond49flive`; the non-live `49f` stays `blackdiamond49f`; every other vendor is unchanged). `role_env_name` then gives `BLACKDIAMOND49FLIVE_READER_ROLE_ARN` for it (read its code; do not hand-type a name elsewhere). If that environment variable is unset or empty, the live read REFUSES CLOSED (the gateway's existing refusal for a missing role); it never falls back to `blackdiamond49f`'s role, to the Gateway instance role or to the internal reader.
3. FLAT LIVE FILES (NFRA_MCPINDEX's measurement, msg 35037, read 2026-10-16 ~13:5xZ; the CTO's ruling @96ea4ac3da: the catalog gets FOUR NEW live rows for `opal-data-bd`, prefix `silver/<t>/`, with `address`, `read_tool` and a measured freshness, `table` = `<t>` plain, and the eight legacy rows stay out): the live tables are FLAT dated files, `s3://opal-data-bd/silver/fees/2026-10-14.parquet`, `silver/transactions/2026-10-16.parquet`, `unrealized` and `allocations` weekly to 2026-10-09, plus non-dated files such as `silver/unrealized_gain_loss.parquet`; they are NOT `date=YYYY-MM-DD/` folders. `client_core` has a `_DATE_PARTITION` pattern of the folder form and `read_rows` builds `<prefix>date=<d>/`, so `list_partitions` finds nothing and a read cannot be made. Make the partition logic accept BOTH layouts per partition: a key whose tail after the real prefix is `date=<YYYY-MM-DD>/...` (today's form, unchanged) OR `<YYYY-MM-DD>.parquet` (the flat form). A partition's read uses the KEYS that were listed for that date (never a path built from the date), whichever form they are in; a key whose tail matches neither (for example `unrealized_gain_loss.parquet`) is not a partition and is ignored without an error. Everything the adapter already does with partitions (newest, window, the one-partition-only statement for a grain not yet measured) keeps working on both forms.
4. The other adapters and their prefixes are unchanged: prove it.

TESTS (new file `tests/test_og_en12.py`; read `tests/test_og_cl2.py` and `tests/test_og_cl1.py` for the Ctx fixture style; the fixture catalog carries rows WITH and WITHOUT `address`):
- `test_ogen12_ac01`: the four 49F live tables resolve through `address` (a row with `address: blackdiamond/49f-live/silver/<t>/` and `prefix: silver/<t>/`, bucket `opal-data-bd`); a row without `address` resolves by `prefix` exactly as before; an unknown table still refuses `no_catalog_row`; a retired row does not resolve.
- `test_ogen12_ac02`: for an address-resolved row the Scope bucket is the row's bucket, the S3 list prefix is the REAL `silver/<t>/`, a partition tail is parsed from the real prefix, and no recorded S3 call carries the address string.
- `test_ogen12_ac03`: `role_key("blackdiamond", "49f-live")` is `blackdiamond49flive` and its env name `BLACKDIAMOND49FLIVE_READER_ROLE_ARN`; `49f` still maps to `blackdiamond49f`; every other vendor's key is unchanged; with the live variable unset the live read refuses closed and does NOT use the `blackdiamond49f` key, the instance role or the internal reader (assert the client factory is never asked for them).
- `test_ogen12_ac04`: parity for the other vendors: for every non-49F-live row of the fixture the key `Ctx.prefix` returns and the Scope it builds equal what the pre-change code produced (compute the expected values in the test from the row's `prefix` and `bucket`).
- `test_ogen12_ac05`: the flat layout: with listed keys `silver/fees/2026-10-14.parquet`, `silver/fees/2026-10-13.parquet` and `silver/unrealized_gain_loss.parquet` under the fixture, `list_partitions` returns the two dates (newest first as today), ignores the non-dated file without raising, and a read of a date uses exactly the listed key; a folder-form fixture (`date=2026-10-14/part.parquet`) still lists and reads as before.
If an existing test pins the old `role_key` for a `-live` segment, update it to the new truth with the smallest edit and name it; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no catalog or registry change (the `address` rows are NFRA_MCPINDEX's file; the role is `OG-ap-29`).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print an account number or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_role.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en12.py
infra/aws/ec2/opal-gateway/tests/test_og_cl1.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_cl3.py
infra/aws/ec2/opal-gateway/tests/test_og_cl4.py
infra/aws/ec2/opal-gateway/tests/test_og_cl5.py
infra/aws/ec2/opal-gateway/tests/test_og_cl6.py
infra/aws/ec2/opal-gateway/tests/test_og_cl7.py
infra/aws/ec2/opal-gateway/tests/test_client_role.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_core.py`, `app/client_role.py`, `tests/test_og_en12.py` and, only as the change needs, the 49F adapter and the existing client tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~125/`. Rows: id `NFRA_OPLGTW-Z-W125-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en12.py test_ogen12_ac01 test_ogen12_ac02 test_ogen12_ac03 test_ogen12_ac04 test_ogen12_ac05; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~125 '^infra/aws/ec2/opal-gateway/(app/client_(core|role|adapter_bd49f)\.py|tests/(test_og_(en12|cl[0-9]+)|test_client_role)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~125: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the four named tests pass: address resolution with the real prefix on the row's bucket, the dedicated -live role key that refuses closed, and parity for every other vendor. `AC2`: the commits of this serial touch only the client core, the role key, the 49F adapter and the client tests.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-12.bd49f-live-address-and-role-key.proof_of_spec.json` (the file name includes the slug). Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the exact env variable name, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO rulings @ed33f552ae, @8b2865e461; rows Z-S292, Z-S293), workstream ENRICH-R38-D (decomposition addendum R3-T.96; a fourth workstream for the L6 gate's one-issuer-per-workstream key). Risk WORLD by the L6 floor (a gateway infrastructure path), no deploy in this cell. Order of the chain: NFRA_MCPINDEX writes the `address` field on the four rows; this cell; `OG-ap-29` (the dedicated role, three halves, applied BEFORE the release); the batched release (with the `BLACKDIAMOND49FLIVE_READER_ROLE_ARN` env key in its deploy hunk); then the `OG-en-11` re-run, which closes Z-S292.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>staged</status>
<round>38</round>
<workstream>ENRICH-R38-D</workstream>
<slot>~125</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
