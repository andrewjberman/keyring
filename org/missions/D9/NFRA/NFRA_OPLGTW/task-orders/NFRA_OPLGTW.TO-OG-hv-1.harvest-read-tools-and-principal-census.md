# NFRA_OPLGTW task order -- `OG-hv-1` -- the gateway's harvest read tools for Opal principals (24 prefixes, non-Opal refused), and the asset-manager principal census (R4, FWD-21)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-hv-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-hv-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~64</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, tests, one read-only census and the ask; no deploy. The grant and the release are NFRA_OPLGTW.TO-OG-hv-2 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut, for the API calls the new code makes (s3:GetObject and s3:ListBucket on opal-data-harvest): simulate-principal-policy opal-gateway-role s3:GetObject on opal-data-harvest/packs/1299_HK_Equity/input_ledger.json -> implicitDeny, and on wsj/harvest/x -> implicitDeny; positive control opal-data-portal-v2/json/x.json -> allowed (2026-10-13 ~20:4xZ). No bucket policy exists on opal-data-harvest (get-bucket-policy: NoSuchBucketPolicy) and encryption is SSE-S3 AES256 (no KMS). The grant is OG-hv-2's apply; this cell changes no IAM. The census reads gateway-access-state-table with the dynamodb:Scan already live on opal-gateway-role (NFRA_MCPORTAL MP-z-4) -- the worker's own session reads it with the box credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-36 analysis R4 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round36.md @713305ee56) on PRD v2.7 FWD-21 (@27ba6b6191: V1 admits by identity, the grant writer writes nothing; CTO msg 33764) and Andrew-direct ~20:0xZ call 8 (all 24 prefixes SERVE to Opal principals, raw included; non-Opal refused on every prefix), list v4 @7e0da2dfee.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-hv-1` (decomposition addendum R3-T.49, R4)

Today no gateway tool reads `s3://opal-data-harvest`: `gateway_query_catalog` reads only the catalog's one bucket
(`opal-data-portal-v2`, `app/query_v0.py:58`), and `opal-gateway-role` is implicitDeny on the harvest bucket. Andrew
(2026-10-13 ~20:0xZ, call 8): "Yes that is available for opal users only for now, which will be managed via opalgateway
entitlements." All 24 top-level prefixes serve to Opal principals, raw included; a non-Opal principal is refused on every
prefix.

1. **The served prefixes, from the list, never typed from memory.** Read
   `MSYS_NO_PATHCONV=1 git show 7e0da2dfee:org/tier1_exec/1.0.0_SA_CTO/deliverables/SERVABLE_PREFIXES_OPAL_DATA_HARVEST_20261013.md`,
   section "v4 -- CURRENT", the row "the 24 top-level prefixes". Put exactly those 24 prefixes in a module constant
   `SERVED_PREFIXES` (a tuple of strings, each ending in `/`) in a new module `infra/aws/ec2/opal-gateway/app/harvest_read.py`.
   The bucket name comes from the naming builder: `python -c "import sys; sys.path.insert(0,'lib'); import opal_naming"`
   and its generated locals map `harvest` -> `opal-data-harvest` (`infra/aws/terraform/modules/opal_name/generated_locals.tf:81`);
   write it as the module constant `BUCKET` with a comment citing that line.
2. **Two READ tools**, registered beside `list_shared_folder` in `infra/aws/ec2/opal-gateway/app/tools.py` (about line
   1237), their logic in `app/harvest_read.py`:
   - `harvest_list(prefix: str, start_after: str = "")`: ONE page of `list_objects_v2` (MaxKeys 1000, `Delimiter="/"`),
     returning keys, sizes, LastModified (UTC) and common prefixes, plus `truncated` and `next_start_after`.
   - `harvest_read(key: str)`: one object. JSON (`.json`, `.json.gz`) is parsed and returned; Parquet (`.parquet`) is read
     with the installed `pyarrow==18.1.0` and returned as rows (at most 1000 rows; `truncated` says so); any other type
     returns its text decoded as UTF-8 (`errors="replace"`). The read is capped at 4 MB on the read itself (the
     `query_v0._fetch_capped` pattern), refused over the cap with `harvest_over_cap`.
   - **Admission, in this order, before ANY S3 call:** (a) a principal is present in the request
     (`context.get_current_principal`), else `principal_required`; (b) the principal is an Opal user: the caller's email
     passes `tools._is_opal_user` (the OG-tg-1 predicate: domain `identity_scope.OPAL_USERS_DOMAIN`, no `#ext#`), else
     `harvest_opal_only`; (c) the `prefix` / `key` starts with one of `SERVED_PREFIXES` and contains no `..`, else
     `harvest_prefix_not_served`. Each refusal is a dict with `error`, `code` and `guard_denied: True`.
   - Every call writes one audit record (`audit.log_call`) with the tool, the key or prefix, the verdict and the bytes --
     never object content.
   - The S3 client: `internal_role.s3_client()` when it returns a client, else a module-scope `boto3.client("s3")` (the
     `query_v0` pattern, so comp-iam resolves the operations statically).
3. **Classify both tools.** Add them to `destructive_ops.SAFE_TOOLS` and to `data_entitlement.NATIVE_TOOLS` (class
   `legacy`; NOT `DATA_GRANT_TOOLS`), or `classify()` fails closed and the guard denies them as `tool_unclassified`.
   Re-pin the counts that move: `tests/test_entitlement_admin.py` 63 -> 65, `tests/test_data_entitlement_family.py`
   non-data 54 -> 56.
4. **Tests,** in `infra/aws/ec2/opal-gateway/tests/test_og_hv1.py`, S3 stubbed (record every call):
   - `test_oghv1_ac01`: `SERVED_PREFIXES` equals the 24 prefixes of list v4 (parsed from `git show 7e0da2dfee:...` in the
     test, or a literal the test asserts against that parse).
   - `test_oghv1_ac02`: a non-Opal principal (`someone@example.com`, and an `#ext#` Opal guest) is refused
     `harvest_opal_only` on `packs/` and on `wsj/harvest/` by BOTH tools, with zero S3 calls recorded.
   - `test_oghv1_ac03`: an Opal principal reads one stubbed JSON key under `packs/` and one stubbed Parquet key under
     `amgt/harvest/gold/chatter_daily/`; a key outside the 24 (`zzz/x.json`) and a `..` key are refused
     `harvest_prefix_not_served` with zero S3 calls; an over-cap object is refused `harvest_over_cap`.
   - `test_oghv1_ac05` (PRD v2.8, the research-only arm): the SAME unprofiled, standard-tier Opal principal that reads
     `packs/` is refused one `schwab_*` tool and `blackdiamond_list_fees` by the entitlement guard (with OG-bd-2's code,
     already on your HEAD).
   - `test_oghv1_ac04`: both tools are SAFE and classified (not `tool_unclassified`), and an unprofiled Opal principal's
     dispatch reaches the tool.
5. **The asset-manager principal census (read only).** Write `W/HV1_PRINCIPALS.json`:
   `{"read_at", "identity_store", "sources": [...], "denominator": {"identity_store_principals": N, "audit_lake_principals_30d": M},
   "principals": [{"principal_hash", "email_domain", "opal": bool, "profiled": bool, "profile_status",
   "asset_manager": true|false|"unknown", "asset_manager_source"}], "asset_managers_named": K}`.
   - `identity_store` and `identity_store_principals` (PRD v2.8): the store that ADMISSION actually reads, never the grant
     store (it holds no harvest record). Trace it in the code: `context.get_current_principal` and the sign-in path that
     sets it name where a principal's identity comes from; name that store in `identity_store` (with the code line that
     reads it) and count its principals, auto-paginated, counted client-side.
   - `audit_lake_principals_30d`: the distinct principals of `s3://opal-mcp-audit/audit/dt=<day>/` for the 30 UTC days
     before today.
   - `asset_manager` comes from a NAMED source only (an Opal roster or record that names the asset-management team; search
     with `comp-find`). If no source names them, write `"unknown"` and file a BLOCKING row; never guess from a name.
   - Never print a person's name or full email in the JSON, the report or a row: `principal_hash` = the first 10 hex of
     sha256 of the lower-cased email; the domain is kept.
6. **The ask.** Write `W/NEVER_WIDEN_ASK_OG-hv-1.md` for the release order this cell rides (`NFRA_OPLGTW.TO-OG-hv-2`):
   - the diff by file;
   - the two new tools, their class (READ, SAFE, legacy), and their refusals;
   - the widening, stated plainly: the gateway's reach grows to the 24 harvest prefixes, for Opal principals only; AND
     `opal-gateway-role`'s own S3 read on `opal-data-harvest` is itself a widening of that role (PRD v2.8), named as one;
   - the research-only arm: an asset manager stays refused every Schwab and Black Diamond tool unless Andrew admits it
     to v2.2's connected set;
   - the IAM grant it needs (`s3:GetObject` on the 24 prefix ARNs, `s3:ListBucket` on the bucket conditioned on those
     prefixes; policy name `gateway-global-harvest-read-policy`, builder output), plan expected 1 add, 0 change, 0 destroy;
   - tools 63 -> 65, no `.env` key change, no `ENABLED_INTEGRATIONS` change;
   - both branches of a call (refused, reads nothing; admitted, one capped read);
   - the rollback: redeploy the prior release ref; destroy the one policy.

## 2. BOUNDS

- Code, tests, the census (read only) and the ask. No release, no deploy, no IAM or Terraform change, no grant written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or full email; write the catalog file
  (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/tests/test_og_hv1.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~64/`. Rows: id `NFRA_OPLGTW-Z-W64-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-hv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/hv1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*SERVED_PREFIXES equals list v4: 24 of 24, extra 0.*failing ids not in the baseline: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-hv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/hv1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)census: identity_store named; identity_store_principals [1-9]\d*, audit_lake_principals_30d [1-9]\d*; principals [1-9]\d*; asset_manager field on every row: yes; plaintext emails 0.*ask sections: 7 of 7.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tools are built, admit only Opal principals on the 24 listed prefixes, and nothing regresses.
- `AC2`: the asset-manager principals are named from the stores with the denominator printed, and the release can be
  signed against the ask.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-hv-1.harvest-read-tools-and-principal-census.proof_of_spec.json`. Validate it
after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip
the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, R4 (FWD-21, PRD v2.7 @27ba6b6191). Cut only after `python .tools/prd-signoff.py status NFRA_OPLGTW` reads ADMITTED
  (LIMB 6; the analysis's own condition).
- The release this cell rides: `NFRA_OPLGTW.TO-OG-hv-2` (CVO cut-template rule, round 36: a deferred-release build cell
  names its release order).
- Measured at the cut (~20:4xZ): `comp-find 'opal-data-harvest' infra/aws/terraform/opal-gateway infra/aws/ec2/opal-gateway`
  -> 0 gateway hits (23 hits repo-wide, all in `terraform/harvest/` and `etfs-rivalfunds/`); `opal-gateway-role`
  implicitDeny on two harvest keys, control allowed; no bucket policy; SSE-S3. NFRA_MCPINDEX MX-c-8 (round 10) catalogs
  16 prefixes at list pin 0b2778751a with `read_tool: null` and `gap_owner: NFRA_OPLGTW`; the v4 extension to 24 is
  NFRA_MCPINDEX round 11 (row Z-S105). This cell does not touch the catalog.
- Admission rule (V1): Opal identity, no per-principal harvest grant record. Andrew: "managed via opalgateway
  entitlements ... no undue holds ... those policies merely need to be designed and expanded upon between the NFRA_OPLGTW
  and NFRA_MCPINDEX projects." Per-person enable/disable is NFRA_MCPORTAL FWD-21 (direction Z2), later.
- Pre-cut: hv1.AC1 base FAIL as expected (`tests/test_og_hv1.py` absent; `app/harvest_read.py` absent); hv1.AC2 base FAIL as
  expected (`HV1_PRINCIPALS.json` absent).

<status>complete</status>
<round>37</round>
<slot>~64</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
