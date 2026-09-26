# NFRA_MCPINDEX task order -- `MX-s-3` -- the opal-assets-silver-etf Lambda rebuilt from the repo, so the TrueShares holdings converter runs in production (MX-s-1's AC2, row Z-S4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~I</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the existing sweep schedule (opal-assets-silver-etf-sweep-daily, cron(30 23 * * ? *)) is read, never changed.
comp-iam: RUN at the act -- `comp-iam service opal-assets-silver-etf`; the rebuild changes code only, and a new grant need is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a code refresh of an existing function.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one Lambda code update through Terraform (safe-apply). No vendor.
</preflight>

## 1. THE CELL -- `MX-s-3` (supplementary to round 2, on Andrew's option 4; the DS lane's MX-s-1 ask)

**Measured (0.4.0_DS_ClientPlatform~D, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/trueshares-holdings-silver.result.md`, READ sections 1, 2 and 6):**
- The running `opal-assets-silver-etf` zip is from 2026-07-15 (CodeSha256 `a14fYacwkjPlkj7P5qb7QGTKDeQ2A9GTnkM/t1rTxcs=`).
- Its `etf_conversion.py` holds 0 occurrences of `_convert_trueshares_holdings`. The converter landed in the repo on
  2026-08-24, and the DS fixes are `6c6232a5d7` and `23efc28a2f` on CLOUD.
- The function's zip VENDORS repo files FLAT at the zip root. The list is
  `infra/aws/lambda/opal-assets/opal-assets-silver-etf/BUILD_MANIFEST.json` `vendored_modules` (8 files under
  `data/assets/scripts/`). Its own rule: "repo files are the source of truth; fix there and rebuild, never edit a zip".

Do (CLAUDE.md rule 13 and NEVER-9: a Lambda code change is Terraform only, through `safe-apply`):
1. Re-vendor the 8 modules from CLOUD HEAD into the function's build directory, the way its Terraform/build expects
   (read `infra/aws/terraform/opal-assets/` and the function directory first). Update `BUILD_MANIFEST.json`'s
   `vendor_sha256` to the new bytes.
2. Run the silver suite, `data/assets/scripts/silver/tests/`, and record the result. (AMENDED @ its own commit on
   0.7.0_AE_CloudOps~I's msg 26040: the first cut named `data/assets/tests/`, which does not exist; BUILD_MANIFEST.json
   names no suite path.)
3. NEVER-2 ledger with slug `nfra-mcpindex-silver-etf-rebuild`:
   - open it, and commit the entry and its sentinel;
   - apply the ONE function's code change through `safe-apply`. The plan must name only `opal-assets-silver-etf`
     (plus its source-hash attributes). Any other resource in the plan: STOP, a BLOCKING row;
   - run the deployed import-health smoke the manifest names;
   - close the entry with its proof, and commit the close.
4. **Before 2026-09-26T23:30Z** if at all possible: that sweep would otherwise flip the served guard PASS to FAIL (row
   `NFRA_MCPINDEX-Z-S5`). After the apply, you MAY fire the sweep once ad hoc as QA. The scheduled fire stays the
   acceptance.

## 2. BOUNDS

1. One function's code. No schedule, event rule, role, layer or other function changes. The `.csv` event-rule
   question (the result's section 6 item 2) is NOT this order's.
2. No served data is written by hand. The sweep writes what it writes.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/lambda/opal-assets/opal-assets-silver-etf/
infra/aws/terraform/opal-assets/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-silver-etf-rebuild.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, as a seat row
`NFRA_MCPINDEX-Z-S<k>` (site-Z; take the next free k), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from the workspace root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-3"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s3.AC1.sh; echo "exit=$?"</invocation><expect>after-issue=yes zip-sha==CodeSha256=yes converter occurrences>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-3"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s3.AC2.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-3"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s1.AC2.sh; echo "exit=$?"</invocation><expect>funds whose guard counts the holdings feed 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-3.silver-etf-rebuild.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once to `2.0.0_SA_COO~O`:
- the plan's resource list;
- the new CodeSha256;
- the smoke result;
- the ledger path;
- whether the ad-hoc sweep ran, and its verdict per fund;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary act on Andrew's option 4 (record @bda25438c8): the DS lane's MX-s-1 (issued c3f599e9f2) measured that its AC2 is reachable only by a DT/AE Lambda rebuild (rule 13, NEVER-9); this order carries exactly that act to an AE lane; same issuer, disjoint write set, nothing on the held branch.

**ISSUER NOTES:** Dry-run at base (2026-09-26 ~03:4xZ):
- s3.AC1 FAIL: LastModified 2026-07-15, zip sha == CodeSha256, converter occurrences 0.
- s3.AC2 FAIL: 0 entries.
- s1.AC2 FAIL: 0 of 2 guards count holdings. Live silver is 106 per fund, of which fact_holdings is 33; the guard
  expects 73.

The lane is seated by 0.0.0_AB_MSTR~Z on this seat's ask. `0.7.0_AE_CloudOps~A` is on another project (one project per
Tier-2 seat).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~I</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<status>complete</status>
<!-- complete flipped by 0.7.0_AE_CloudOps~I 2026-09-26T12:2xZ. AC1 PASS exit=0, AC2 PASS exit=0, AC3 PASS exit=0.
     Instance: org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-3.silver-etf-rebuild.proof_of_spec.json
     proof-of-spec-check VALID (rc=0), re-run by this seat after 2.0.0_SA_COO~O added the MX-s-3 decomp row @9f323d492d.
     Live: opal-assets-silver-etf CodeSha256 ZyhzyrjuHLi9TfRC9CFSpvPHY6Rcyq/aPgseJafmuTg=, LastModified 2026-09-26T09:26:39Z.
     Ledger nfra-mcpindex-silver-etf-rebuild CLOSED at 547cd9f613, 7 of 7 legs proven, sentinel removed.
     One row raised: NFRA_MCPINDEX-Z-S12 (record-terraform-deploy.sh reader, BLOCKING/INERT), ruled into MX-s-5.
     The APPEND is deliberate: the earlier tag above is left standing, because an order's status history is
     append-only and the LAST tag is the live one. This comment deliberately does NOT spell the earlier tag
     out -- a first draft did, and a literal copy of it inside this comment became a THIRD tag that won the
     last-tag read and silently reverted the flip. A status parser cannot tell prose from a tag. -->
