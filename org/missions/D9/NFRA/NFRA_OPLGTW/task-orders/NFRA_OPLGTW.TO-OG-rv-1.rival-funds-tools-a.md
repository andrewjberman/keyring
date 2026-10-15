# NFRA_OPLGTW task order -- `OG-rv-1` -- G5r rival funds: peer group, fund holdings, who holds, security reference, coverage

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rv-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rv-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~100</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is a later applier order (NFRA_OPLGTW.TO-OG-ap-22, not yet cut).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; its AWS calls are s3:GetObject and s3:ListBucket on opal-data-etfs, covered by the OG-ap-20 grant (A rival-funds prefixes). Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34190 / 34198 on PRD v3.7 (Andrew-direct ~19:0xZ, rival funds indexed into the gateway) and the CRO's G5r spec @e1b9937129.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-rv-1` (decomposition addendum R3-T.70, workstream RIVAL-FUNDS, FWD-22 G5r)

peer group, fund holdings, who holds, security reference, coverage. Module `infra/aws/ec2/opal-gateway/app/etfs_rivals.py`.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py` (OG-gt-0): `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; `ref` and every
`extra` under a served prefix with no `..`; one audited refusal; call it FIRST, before any S3 call), `list_keys(scope, prefix)`, `newest_part(scope, prefix)`, `read_parquet(scope, key, columns, filters)`, `read_json(scope, key)`
(it decides gzip by the key's suffix: a `.json` object that is gzip-encoded raises; sniff the first two bytes `1f 8b` yourself over `typed_scope._load_capped` in that case), and the re-exports `envelope(body, *, as_of, source_keys, denominator,
absent_reason=None)` (projected to 50 KB; an empty body must carry an `absent_reason`), `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope.
`app/etfs_funds.py` (OG-et-2, merged) is the closest model of a module on this seam: read its top (catalog helper by `entity`, `SERVED_PREFIXES` computed from rows, `_client`) and mirror it; import nothing from it that you can write in six lines, and never edit it.

Build your OWN scope: `Scope("etfs-rivals", <the bucket the catalog rows name>, <the prefixes computed from the rows>, <app.internal_role.s3_client when it returns a client, else a lazily created boto3 S3 client inside a function>)`. The prefix list is a function of the catalog rows and holds exactly what your tools read and nothing else: the release's IAM grant is generated from the same rows.

Each tool is a TOP-LEVEL function with exactly the tool's name and inputs, returns a dict, and answers with `as_of` (the data's own report/partition date, never the read time), `source_keys` (the exact part keys read), a `denominator` dict (which carries
`trading_days_behind_t1` from `lib/trading_calendar.py`, and the counts of rows read and rows returned) and `absent_reason`. An item that is absent returns an empty body with `absent_reason`, never an error. All tools are firm-free (Opal fund research): admission is the Opal-user read class, no firm fork.

### KEYS COME FROM THE CATALOG (CTO ruling msg 34173)

The gateway CODE types NO S3 key, prefix or bucket literal (the commit-time naming limb refuses legacy layouts). Each key template and the bucket are read at call time from the table's DATA_CATALOG row (owned by `NFRA_MCPINDEX`; v0.5 is LIVE on the host at `1b18b94979`). Do NOT write `app/refs/DATA_CATALOG.yaml`.
The loader is `app/integrations/portal_index/integration.py` `runtime_catalog()`; find how a row is reached by its `entity` name as `app/etfs_funds.py` does it. A row not found, a row with `retired` true, or a template you cannot fill is `absent_reason` (zero reads), never a guess.
Your module's `SERVED_PREFIXES` is COMPUTED from the rows (a function), not a typed tuple. Tests use a SYNTHETIC catalog fixture with the same shape (synthetic names; no real key text in the test); the issuer's AC2 probe runs against the real catalog and the real bucket.
Your branch carries the committed catalog (v0.5). The one date slot of a template is `{D}` or `{YYYY-MM-DD}`: read it from the row.
The manifest of all rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/TABLE_ROWS_MANIFEST_20261014.md` (entity, row id, bucket, template).

### Binding reading rules (the CRO's G5r spec `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5r_rivalfunds_spec.md` @e1b9937129, and the contracts in `.../G5_etfs.md`: find each table's section by its name; full column lists are there)

1. **Re-run parts supersede, never add.** Under a date partition several parts exist (re-runs); the NEWEST part (by the stamp in its file name) is the complete snapshot; read it only and NEVER sum parts. `source_keys` names the exact part read.
2. **A fund's latest report date comes from `gold/canonical_shape` (its newest part), never from `holdings_coverage` or the platinum manifest (row Z-S124: both understate 9 funds).** A tool that states a fund's report date states the fund's OWN `report_date` and its lag in trading days against T-1.
3. **Weights are fractions in these tables:** say the unit (`weight_unit`) in every answer that carries a weight.
4. **Claims pass through:** `trade_schedule` and `flow_reconciliation` rows are INFERRED; keep the `claim` field as the row has it.
5. **Never `none` for a missing identifier:** an identifier column that is empty for a matched ticker answers `not_held_for_this_security`.
6. **Peer groups (measured 2026-10-14):** IDVZ (rivals BIDD, CGIC, INEQ, SCHY, TXUE) and PFOE (rivals BASG, ETFT, GQGU, PCLG, TSEL, WCMG); DIVZ and PFDE have NO peer group (`no_peer_group`). Do not type these lists: read them from `gold/peer_group_map`.
7. Fund tickers are 2 to 6 uppercase letters; anything else is refused `harvest_bad_argument` with ZERO reads. A well-formed ticker the data does not hold is an empty body with `absent_reason`.

Catalog entities for this cell (all in the bucket `opal-data-etfs`, tables under `rivalfunds/etfs/`): `opal_data_etfs_gold_peer_group_map`, `opal_data_etfs_gold_canonical_shape`, `opal_data_etfs_gold_security_universe`, `opal_data_etfs_gold_security_market`, `opal_data_etfs_gold_corporate_actions`, `opal_data_etfs_gold_security_names`, `opal_data_etfs_gold_input_census`, `opal_data_etfs_gold_holdings_coverage` (read only for the labelled comparison).

### The five tools (G5r spec sections 0, 2, 3, 5)

- **`etfs_get_peer_group(home_ticker: str)`**: the peer group of one Opal home fund. Reads gold `peer_group_map` (newest part of the newest date partition). Returns `home`, `rivals` (list of tickers), `group` name and `as_of`; DIVZ and PFDE (no group) answer an empty body with `absent_reason` = `no_peer_group`.
- **`etfs_get_rival_fund_holdings(fund_ticker: str, as_of: str = None)`**: what one fund (home or rival) holds on a report date. Reads gold `canonical_shape` (newest part per date; `as_of` is a `report_date`, else the fund's newest report date). Returns `holdings` (position rows with the identifiers: ticker, Bloomberg id, CUSIP, ISIN, SEDOL, name, weight, sector and country where the table has them), `weight_unit` (`fraction`), `report_date`, `trading_days_behind_t1` of that report date and the fund's `resolved` / `unresolved` position counts. The fund's name, when null in the part, is not guessed.
- **`etfs_who_holds(security: str, peer_group: str = None, as_of: str = None)`**: which funds hold one security on a date, with weights. `security` matches a ticker, a Bloomberg id, a CUSIP or an ISIN (resolve it in gold `security_universe`, newest part, then match `canonical_shape` positions on the resolved ticker). Reads `canonical_shape` (newest part per date, one date: `as_of` else the newest date present) with `peer_group` an optional home ticker narrowing to that group's funds. A matched ticker whose requested identifier column is empty answers `not_held_for_this_security` for that identifier (never `none`).
- **`etfs_get_security_reference(security: str)`**: the reference record of one security from gold `security_market`, `corporate_actions` and `security_names` (newest part of the newest partition of each; the three dates are returned as the three tables hold them). Absent in a table is that table's `absent_reason`; the answer carries a section per table.
- **`etfs_get_coverage(fund_ticker: str = None)`**: the latest report date per fund FROM `canonical_shape`'s newest part (one fund or all), the lag in trading days against T-1, and the reasons from gold `input_census` for a fund that is behind (newest part). It must NOT read `holdings_coverage` for freshness (Z-S124): when asked, `holdings_coverage` is read only to show its (possibly lower) date beside the canonical one, labelled `coverage_table_says`.


### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_rv1.py` (a recording fake client with in-memory Parquet and a synthetic catalog; Opal stand-in principal)

- `test_ogrv1_ac01`: `etfs_get_peer_group` answers a home fund's rivals from the newest part; DIVZ and PFDE answer `no_peer_group`; an ill-formed ticker is refused `harvest_bad_argument` with ZERO reads.
- `test_ogrv1_ac02`: `etfs_get_rival_fund_holdings` reads the NEWEST part per date only (a fake holds a re-run with different weights: the answer equals the newer), names `weight_unit`, honours `as_of`, returns the fund's own `report_date` and its lag, and counts resolved and unresolved positions.
- `test_ogrv1_ac03`: `etfs_who_holds` resolves a ticker, a CUSIP and an ISIN through `security_universe`, narrows by `peer_group`, and answers `not_held_for_this_security` when the identifier column is empty for a matched ticker.
- `test_ogrv1_ac04`: `etfs_get_security_reference` answers a section per table with its own date and `absent_reason`; `etfs_get_coverage` takes a fund's latest report from `canonical_shape` even when the fake `holdings_coverage` says `gap` (the Z-S124 arm) and shows the coverage table's value labelled `coverage_table_says`.
- `test_ogrv1_ac05`: a non-Opal and an absent principal are refused all five tools with ZERO reads; an over-cap object is refused `harvest_over_cap`; a catalog row that is absent or retired gives `absent_reason` with zero reads.


The live probe is the issuer's AC2. Run the same calls first, with `INTERNAL_READER_ROLE_ARN` unset (today the box credentials read the bucket; the gateway's internal reader role gets the read grant with OG-ap-20).

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py`, `app/etfs_funds.py`, `app/etfs_ownership.py` and the pinned-count tests are NOT yours: the issuer registers every tool and re-pins the counts at the merge, in one commit (`OG-rv-3`). Do not edit them; name the registrations you expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's text body into a report, a row or a log; write the catalog file; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/etfs_rivals.py
infra/aws/ec2/opal-gateway/app/etfs_funds.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/tests/test_og_rv1.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5r_rivalfunds_spec.md
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~100/`. Rows: id `NFRA_OPLGTW-Z-W100-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rv1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rv1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)rival tools A: peer group IDVZ rivals (\d+) vs independent \1; INEQ holdings (\d+) rows vs independent \2, report_date equal True; who_holds answered True; coverage from canonical_shape True; non-Opal refused True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tools are built, read the newest part per date, take a fund's latest report from canonical_shape, name the weight unit and refuse non-Opal before any read.
- `AC2`: against the real bucket the tools answer with the full envelope, a count equals an independent read, and a non-Opal principal is refused.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rv-1.rival-funds-tools-a.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RIVAL-FUNDS (decomposition addendum R3-T.70; PRD v3.7+ ADMITTED, v3.10 current). CRO G5r spec @e1b9937129; CTO msgs 34190, 34198. The read grant for the rival prefixes rides OG-ap-20 (its ONE G5 ask); these tools release with OG-ap-22 after OG-ap-21.
- Naming: the CRO's `etfs_get_fund_holdings` for rivals collides with OG-et-2's tool of that name (the four Opal funds); ruled here: the rival holdings tool is `etfs_get_rival_fund_holdings`. Every other tool keeps the CRO's name.
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell; `OG-rv-3`).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).
- The five tools of this cell read the SAME newest-part rule as `OG-rv-2`'s; the two modules are separate write sets and may each carry their own six-line helper.

<status>complete</status>
<round>37</round>
<workstream>RIVAL-FUNDS</workstream>
<slot>~100</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
