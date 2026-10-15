# NFRA_OPLGTW task order -- `OG-et-2` -- G5 wave A: etfs_get_fund_nav_history, etfs_get_fund_holdings

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-et-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-et-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~85</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-et-2` (decomposition addendum R3-T.52, workstream FWD22-W7, FWD-22 G5)

G5 wave A fund tools `etfs_get_fund_nav_history` and `etfs_get_fund_holdings`.

Build two G5 Opal-fund tools over `opal-data-etfs` (wave A). Module `infra/aws/ec2/opal-gateway/app/etfs_funds.py`.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py` (OG-gt-0): `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; `ref` and every
`extra` under a served prefix with no `..`; one audited refusal; call it FIRST, before any S3 call), `list_keys(scope, prefix)`, `newest_part(scope, prefix)`, `read_parquet(scope, key, columns, filters)`, `read_json(scope, key)`
(it decides gzip by the key's suffix: a `.json` object that is gzip-encoded raises; sniff the first two bytes `1f 8b` yourself over `typed_scope._load_capped` in that case), and the re-exports `envelope(body, *, as_of, source_keys, denominator,
absent_reason=None)` (projected to 50 KB; an empty body must carry an `absent_reason`), `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope.

Build your OWN scope: `Scope("etfs", <the bucket the catalog rows name>, <the prefixes computed from the rows>, <app.internal_role.s3_client when it returns a client, else a lazily created boto3 S3 client inside a function>)`. The prefix list is a function of the catalog rows and holds exactly what your tools read and nothing else: the release's IAM grant is generated from the same rows.

Each tool is a TOP-LEVEL function with exactly the tool's name and inputs, returns a dict, and answers with `as_of` (the object's own as-of or its file date, never the read time), `source_keys` (the exact keys read), a `denominator`
dict (which carries `trading_days_behind_t1` from `lib/trading_calendar.py`) and `absent_reason`. An item that is absent returns an empty body with `absent_reason`, never an error.

### KEYS COME FROM THE CATALOG (CTO ruling msg 34173; replaces "FIRST ACT")

The gateway CODE types NO S3 key, prefix or bucket literal for these tables (the commit-time naming limb refuses legacy layouts). Each key template and the bucket are read at call time from the table's DATA_CATALOG row, owned by `NFRA_MCPINDEX` (v0.5, the 216 table rows). Do NOT write `app/refs/DATA_CATALOG.yaml`.
The loader is `app/integrations/portal_index/integration.py` `runtime_catalog()` (it returns the loaded catalog `query_v0._catalog()`, built by `app/catalog_gate.py` `load_catalog`); read both to find how a table row is reached by its `entity` name. If the loaded catalog has no accessor by entity,
write a SMALL helper in YOUR module that scans the loaded catalog's entries for `entity == <name>` and returns `bucket`, `prefix` and `key_template`; do not edit `catalog_gate.py` or `query_v0.py`. A row not found, a row with `retired` true, or a template you cannot fill is `absent_reason` (zero reads), never a guess.
Your module's `SERVED_PREFIXES` is COMPUTED from the rows (a function), not a typed tuple. Tests use a SYNTHETIC catalog fixture with the same shape (synthetic names; no real key text in the test); the issuer's AC2 probe runs against the real catalog and the real bucket.
Your branch must carry the committed catalog: before the build run `git merge box/sitez` in your worktree if `app/refs/DATA_CATALOG.yaml` at your HEAD lacks the entity named below (`~MI` commits v0.5 to box/sitez; the issuer syncs your branch).

Catalog entities for this cell (row ids in parentheses): `opal_data_etfs_silver_netassets_daily` (c-f040a4641168; one parquet object), `opal_data_etfs_gold_holding` (c-7113cef03772; `gold/holding/date={YYYY-MM-DD}/holding.parquet`),
`opal_data_etfs_gold_book` (c-fc3803f3ed55; `gold/book/date={YYYY-MM-DD}/book.parquet`), `opal_data_etfs_silver_holdings` (c-a7871a05f171; `silver/holdings/{YYYY-MM-DD}.parquet`). The manifest of all rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/TABLE_ROWS_MANIFEST_20261014.md`.

### Binding reading rules (G5 census section (c), lines 112-121 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md`)

1. **Re-run parts supersede, never add.** Where a prefix keeps several parts per date, the newest part (max `revision`) is the complete snapshot; never sum parts.
2. **Three dates in one row:** the file key (run date), `data_as_of` (the issuer date, usually the day before) and `_ingested_at`. Weekend files carry Friday's data and are NOT staleness. Report all that the row carries.
3. **Units differ by layer:** weights are percentage points in Opal silver and gold/holding; say the unit in the answer.
4. **Claims are in the data** (`claim` MEASURED/INFERRED per row where present): pass them through.
5. **Never sum across firms.** A partner-firm slice is read for ONE firm per call; no tool returns a total that adds firm slices.

### The two tools (G5 section (c), lines 135-136; contracts: silver holdings 333-408, gold holding 761-834, gold book 683-760, silver netassets 409-468, netassets_daily 469-524, snapshots 525-582)

- **`etfs_get_fund_nav_history(fund_ticker: str, start: str = None, end: str = None)`**: NAV, market price, shares outstanding and net assets for ONE Opal fund (`DIVZ`, `IDVZ`, `PFDE` or `PFOE`; any other ticker is refused
  `harvest_bad_argument` with ZERO reads; the four tickers are read from the data, not typed twice). Reads the consolidated history `silver/netassets_daily.parquet` (one file, rewritten each run; columns `date, key, ticker, name, source,
  source_system, nav, market_price, shares_outstanding, shares_basis, net_assets_reported, net_assets, inferred, data_as_of, staleness_days, _ingested_at`; one row per run date per fund). `start` and `end` are inclusive `YYYY-MM-DD` (a window over
  400 days is clamped, `limit_applied` says so). Returns `series` (a list of `{date, nav, market_price, shares_outstanding, net_assets, inferred, data_as_of, staleness_days}`, oldest first), with `inferred` passed through. `as_of` = the last
  `date` in the series; the denominator carries `rows_in_file` and `rows_after_filter`.
- **`etfs_get_fund_holdings(fund_ticker: str, as_of: str = None)`**: what one Opal fund holds on a date, with weights (percentage points: say so in `weight_unit`) and the sector or country mix where the table carries them. `fund_ticker` as above.
  Read `gold/holding` for the fund's holdings (the contract at 761-834) and `gold/book` for the book totals (683-760); the issuer's `silver/holdings` (333-408) is the source those are built from and is read only when the gold tables lack the
  requested date (say so in the answer). With `as_of` that date, else the newest date present. Re-run parts supersede: the NEWEST part per date only, never summed. Returns `holdings` (list), `weight_unit`, and the three dates a row carries.

Served prefixes of your scope: the prefixes of the catalog entities named above, computed from their rows, and nothing wider.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_et2.py` (a recording fake client with in-memory Parquet; Opal stand-in principal)

- `test_oget2_ac01`: NAV history returns only the requested fund's rows, oldest first, within `start..end` inclusive, with `inferred` passed through, `as_of` equal to the last date, and the denominator's two counts.
- `test_oget2_ac02`: an unknown ticker is refused `harvest_bad_argument` with ZERO reads; a window over 400 days is clamped with `limit_applied`.
- `test_oget2_ac03`: holdings read the NEWEST part per date only (a fake holds a re-run with different weights: the answer equals the newer), name `weight_unit`, honour `as_of`, and fall back to silver only when the gold date is absent, saying so.
- `test_oget2_ac04`: a non-Opal and an absent principal are refused both tools with ZERO reads; an over-cap object is refused `harvest_over_cap`.

The live probe is the issuer's AC2. Run the same calls first, with `INTERNAL_READER_ROLE_ARN` unset. NOTE: today the box credentials read the bucket; the gateway's internal reader role does NOT yet (the release carries a grant).

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/etfs_funds.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/tests/test_og_et2.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~85/`. Rows: id `NFRA_OPLGTW-Z-W85-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-et-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/et2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-et-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/et2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)etf funds: IDVZ nav series (\d+) rows vs independent \1, last nav equal True; unknown ticker refused True; holdings answered with a weight unit True \([1-9]\d* rows\); non-Opal refused True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the two fund tools are built, read the newest part per date, name the weight unit and refuse non-Opal before any read.
- `AC2`: against the real bucket the NAV series for IDVZ equals an independent read of the consolidated file, an unknown ticker is refused, holdings answer with a weight unit, and a non-Opal principal is refused.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-et-2.etfs-funds-tools.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.52; PRD v3.5 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- Decomposition addendum R3-T.52 (G5 wave A). Rides release `OG-ap-20` with the G5 never-widen ask and the read grant on `opal-data-etfs` (cell OG-et-3, cut when this cell's served prefixes exist). Today neither the gateway role nor the internal reader reads this bucket.
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).


- A1 (issuer, 2026-10-14 ~23:5xZ, CTO ruling msg 34173 and `NFRA_MCPINDEX` MX-c-14 rows, rows Z-W84-S1/Z-W85-S1/S2): the worker stopped at the commit-time naming gate on legacy key literals. Ruled: no key, prefix or bucket literal in the module; every key template and the bucket are read from the table's catalog row at call time; `SERVED_PREFIXES` is computed from the rows; the release's grant (`OG-et-3`) is generated from the same rows. The FIRST ACT paragraph is replaced by KEYS COME FROM THE CATALOG. The order is re-cut; the slot's blocked branch is synced to trunk and reopened. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>FWD22-W7</workstream>
<slot>~85</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
