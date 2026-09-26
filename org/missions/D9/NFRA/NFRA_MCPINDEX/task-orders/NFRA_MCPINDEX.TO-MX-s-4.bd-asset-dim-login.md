# NFRA_MCPINDEX task order -- `MX-s-4` -- the Black Diamond asset-dim download logs in again, and its wrapper stops reporting Success on failure (MX-s-2's root cause, rows Z-S8/Z-S9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~I</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the existing trigger bd-asset-dim-pipeline-trigger (weekdays 22:10Z) is read, never changed, by steps 1-3; step 4 is a schedule change only after 1-3 land, and is its own ask.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy changes; a need for one is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a producer repair.
EGRESS CLASS, declared: Opal's own AWS (SSM, S3) plus the EXISTING producer's own login to the Black Diamond portal, run as the producer runs. Andrew-direct 2026-09-26: API egress is permitted this session and every call is ledgered by the seat that makes it. A NEW credential, an account change or any contract with the vendor is NOT covered and is Andrew's word.
</preflight>

## 1. THE CELL -- `MX-s-4` (supplementary to round 2, on Andrew's option 4; the DS lane's MX-s-2 ask, msg 26021)

**Measured (0.4.0_DS_ClientPlatform~D, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/bd-cusip-bridge.result.md`, READ sections 1-5):**
- The chain is: `bd-asset-dim-pipeline-trigger` (weekdays 22:10Z), then Lambda `bd-asset-dim-trigger`, then EC2
  `i-0e6f6dc014fdcf1cd` running SSM document `opal-bd-asset-dim-download`. The download feeds
  `convert_assets_to_silver.py`, which writes `silver/bd_assets.parquet`, which feeds `build_bd_assets_dim.py`, which
  writes `silver/bd_assets_dim.parquet` (the cusip bridge).
- 69 consecutive runs have failed since 2026-06-23, all 69 with the same Phase-1 login error: `TimeoutError: forURL:
  Timeout 30000ms exceeded. waiting for navigation to "**/bd3.bdreporting.com/**"`. The logs are
  `s3://opal-data-bd/logs/asset-dim-download-*.log`: 119 read, last OK 2026-06-22.
- The wrapper exits 0 on `download_rc=1 merge_rc=99`, so SSM records Success, and 95 days of failure were invisible.
- Both parquets have been frozen since 2026-04-14. The compaction to `silver/bd_assets.parquet` also stopped
  (section 5, item 3).

Do, in order:
1. **Find and fix why the login times out.** Read the download script the SSM document runs. Fire the producer ONCE ad
   hoc as it runs (its own SSM document) to reproduce, and ledger each vendor-facing run in your deliverables.
   - If the fix needs a new credential, an MFA device, an account change or anything from the vendor: STOP, file a
     BLOCKING row, and report. That is Andrew's word.
2. **Make the wrapper's exit code honest.** A failed download or merge returns non-zero, so SSM records Failed. This is
   a producer reporting its own result, not an alarm.
3. **Restore the compaction to `silver/bd_assets.parquet`.** Check what the SSM document passes to
   `convert_assets_to_silver.py`; it writes the compacted file unless `--no-compacted` is passed.
4. Rebuild the bridge once, `build_bd_assets_dim.py`, from the now-current input. Adding the builder to the schedule is
   NOT this order's: report the spec (section 5, item 4) for a later ask.

## 2. BOUNDS

1. No served gold is rewritten. The `holdings_lots` correction is MX-s-2's, under its own never-widen sign-off.
2. No alarm, monitor or notification is built (the standing moratorium).
3. Terraform-managed resources change only through `safe-apply`. An SSM document or EC2 script change follows its
   existing deploy path.
4. Standing: no push. REFUSE a criterion you cannot meet as written, and report the refusal with its measurement.
   Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
data/black_diamond/
infra/aws/lambda/bd-asset-dim-trigger/
infra/aws/ssm/
infra/aws/ec2/
infra/aws/terraform/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

The producer's scripts may live elsewhere. Find them from the SSM document's content. A needed path outside this list
is a question to the issuer, never a silent widening.

## 4. PROOF OF SPEC (literal; run from the workspace root after the fix and one real run)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-4"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s4.AC1.sh; echo "exit=$?"</invocation><expect>written after issue>=1; download_rc0=yes failed_lines=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-4"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s4.AC2.sh; echo "exit=$?"</invocation><expect>silver/bd_assets.parquet after issue=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-4"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s4.AC3.sh; echo "exit=$?"</invocation><expect>silver/bd_assets_dim.parquet after issue=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-s-4" judgment="true"/>
</proof_of_spec>

AC4 (JUDGMENT, graded by `3.0.0_SA_CVO~O` at L9; record it UNVERIFIABLE-BY-INSTRUMENT): the wrapper now reports a
failed download or merge as a non-zero exit (SSM Failed). Show a real or planted failure's SSM status in your result.

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-4.bd-asset-dim-login.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once to `2.0.0_SA_COO~O`:
- the cause;
- the fix and its deploy path;
- the ledgered vendor-facing runs;
- the wrapper change;
- the new LastModified values and asset_id counts;
- the schedule spec for the later ask;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary act on Andrew's option 4 (record @bda25438c8): the DS lane's MX-s-2 (issued c3f599e9f2) measured that its cause is a dead upstream producer, an AE/CloudOps repair (rule 13); this order carries exactly that repair to the lane already seated for NFRA_MCPINDEX; same issuer, disjoint write set.

**ISSUER NOTES:** Dry-run at base (2026-09-26 ~05:4xZ):
- s4.AC1 FAIL: 119 logs listed, 0 written after issue.
- s4.AC2 FAIL: silver/bd_assets.parquet LastModified 2026-04-14T20:09:23Z.
- s4.AC3 FAIL: silver/bd_assets_dim.parquet LastModified 2026-04-14T20:44:16Z.

Queued after MX-s-3 on the same lane (0.7.0_AE_CloudOps~I). MX-s-3 has the 23:30Z window.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~I</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
