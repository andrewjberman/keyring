# NFRA_MCPINDEX task order -- `MX-s-8` -- the two mirror_conversion.py source fixes (Z-S3, Z-S25) go into the 4 vendored silver Lambda copies, deployed in one never-widen act

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~7</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change to 4 existing functions; no schedule, event rule, cron, alarm or monitor is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant changes; Terraform touches only the 4 functions' code attributes.
comp-adversary: DECLARED-NOT-APPLICABLE -- two ruled source fixes, vendored.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (Terraform apply, lambda get-function, get-layer-version).
</preflight>

## 1. THE CELL -- `MX-s-8` (supplementary; rows Z-S3 and Z-S25, routed by 1.0.0_SA_CTO~O to this issuer)

Two source fixes are on CLOUD in `data/assets/scripts/silver/mirror_conversion.py`:
- `8ba0d6645b` (Z-S3): in `to_arrow`, the float64 parse-or-raise guard `elif t == "float64" and df[c].dtype == object:`
  also takes the pandas-3 string dtype: `(df[c].dtype == object or pd.api.types.is_string_dtype(df[c].dtype))`.
- `bbf8cfefa6` (Z-S25, ruled by the CTO at msg 20260927T072615Z): in `_numeric_or_raise`, an EXACTLY-empty string
  returns None (`if v == "": return None`), before the float parse. Whitespace and every other token still raise.

Four functions vendor this module FLAT into their zips from their own directories, and each copy still carries neither
fix: `infra/aws/lambda/opal-assets/opal-assets-silver-{blackdiamond,etf,eclipse,orion}/mirror_conversion.py`. The guard
sits at blackdiamond:330, etf:330, eclipse:275 and orion:277; `_numeric_or_raise` is at :283, :283, :228 and :230.
The handoff with both hunks: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/Z-S3_PATCH_FOR_AE_VENDORED_COPIES.md`
(sections 1 and 7). All four functions deploy from `infra/aws/terraform/opal-assets/silver.tf`.

**The copies are NOT re-vendored whole.** blackdiamond, eclipse and orion carry OTHER modules whose bytes differ from
source, and that sweep is parked. Apply exactly the two hunks to each copy and nothing else.

### PHASE A (pre-GO) -- no deploy
1. Apply the two hunks to each of the 4 copies. `git diff` per file shows only those two hunks.
2. `opal-assets-silver-etf/BUILD_MANIFEST.json` carries `vendor_sha256`: set its `mirror_conversion.py` entry to the
   new bytes' sha256. The other three manifests carry no hashes; leave them.
3. `python -m py_compile` each patched copy, and run the silver suite `data/assets/scripts/silver/tests/`. Record
   passed/failed/skipped.
4. Measure, for the signers:
   - each function's current `CodeSha256` and `LastModified` (the rollback keys);
   - the pandas version its layer carries: read the function's `Layers` ARN, then `get-layer-version`, then the
     `pandas-*.dist-info` name in the layer zip. This decides whether Z-S3's arm moves any served answer; Z-S25's
     empty-field arm moves one either way.
5. Save each function's CURRENT zip (from `get-function` `Code.Location`, sha256-checked against `CodeSha256`) under
   `C:/tmp/mx-s8-rollback/` as the rollback artifacts. Name the rollback act.
6. Run `terraform plan` in `infra/aws/terraform/opal-assets` (read-only; `.tools/safe-apply.sh -chdir=... plan` if it
   accepts `plan`, else the plan it prints before apply without approving). The plan must name ONLY the 4 functions'
   code attributes. Anything else: STOP, a BLOCKING row.
7. Commit steps 1-2, write `ANNOUNCE_MX-s-8.md` in your deliverables dir with steps 3-6's numbers, commit it, and
   report. Do NOT apply.

### PHASE B (GO) -- only after the issuer says GO
8. NEVER-2 ledger with slug `nfra-mcpindex-silver-mirror-guard`: open it; commit the entry and its sentinel.
9. `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -auto-approve`. The plan must name only the
   4 functions; anything else: STOP before approving.
10. The import-health smoke per function: the designed refusal of `lambda_entry` on a non-S3, non-sweep event, as the
    MX-s-3 ledger `org/critical_paths/change_management/20260926T0844Z_nfra-mcpindex-silver-etf-rebuild_deploy_completion.md` did it.
11. Record with `bash infra/aws/lambda/ci/record-terraform-deploy.sh --function <the 4 names>`; see its header for flags.
12. Close each leg with its proof, commit the close, then run the criteria.
A failed leg: redeploy the saved zips, close the entry as rolled back, report. Never half-landed.

## 2. BOUNDS

1. The 4 copies' two hunks, the etf manifest hash, and the ledger. No other module, function, layer, schedule, role or
   event rule changes. The parked re-vendor sweep is not this order's.
2. No served data is written by hand. The 4 missing pathfinder partitions are backfilled by 0.4.0_DS_ClientPlatform~D
   after this deploy, not here.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report it with its
   measurement. Never repair or widen a criterion.

## 3. SURFACES

<paths>
infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/mirror_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-etf/mirror_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-etf/BUILD_MANIFEST.json
infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-orion/mirror_conversion.py
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-silver-mirror-guard.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~7/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W7-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-8"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s8.AC1.sh; echo "exit=$?"</invocation><expect>vendored copies=4 both fixes 4 of 4 old guard 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-8"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s8.AC2.sh; echo "exit=$?"</invocation><expect>functions carrying the fix 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~7/NFRA_MCPINDEX.TO-MX-s-8.silver-mirror-guard-vendor.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase: the diffs, the suite result,
the layer pandas versions, the rollback keys, the plan's resource list, the ledger path, AC lines, commit hashes, rows.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary vendoring cell routed to this issuer by 1.0.0_SA_CTO~O (msgs 20260927T065208Z and 072615Z) after 0.7.0_AE_CloudOps~I died holding the Z-S3 handoff (@5dd42c44e9); two ruled source fixes, one deploy, one sign-off.

**ISSUER NOTES:** Dry-run at base: s8.AC1 FAIL (both fixes 0 of 4, old guard 4); s8.AC2 FAIL (0 of 4 functions; all
4 zips sha-verified). Positive control: AC1 PASS on 4 patched scratch copies via `VENDOR_ROOT=`. Never-widen (served
silver moves): CTO half offered by 1.0.0_SA_CTO~O (065208Z); the second, non-acting half is asked of 3.0.0_SA_CVO~O
after PHASE A's announcement. GO is the issuer's, on both halves SIGNED. MX-s-7 (the recorder UTF-8 fix) landed
first @b8a7da3c17, so step 11's record does not re-arm the mojibake loop.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~7</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
