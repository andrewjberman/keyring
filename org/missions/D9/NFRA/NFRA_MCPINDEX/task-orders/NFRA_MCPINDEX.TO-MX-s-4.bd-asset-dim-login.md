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
   - **AMENDED A2 (2.0.0_SA_COO~O, 2026-09-27 ~19:1xZ, on 1.0.0_SA_CTO~O's msg 20260927T185833Z):** at the login
     timeout, the ONE reproduction run captures ONE full-page screenshot and the page URL. The evidence decides which of three
     causes this is: (a) the login form re-shown with an error, meaning the password expired or changed; (b) an MFA or
     consent prompt; (c) a changed page structure, meaning a code fix in this lane. The screenshot stays OUTSIDE the repo
     (`C:/tmp/mx-s4-evidence/`) and is never committed or uploaded. The result records ONLY: the URL's scheme, host and
     path (no query or fragment); which of (a)/(b)/(c) it shows; and one sentence of description with no account,
     client or personal data. (a) and (b) are Andrew's: STOP with a BLOCKING row naming which. (c) proceeds to the fix.
   - **AMENDED A3 (2.0.0_SA_COO~O, 2026-09-27 ~20:2xZ), on Andrew-direct 2026-09-27 ~19:5xZ** (record
     `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260927_195xZ_CTO_O_SPRINT_OWNER_ONLY_AND_BD_MFA_USE_THE_TRUST_TOKEN_ROUTE.md`
     @785fc4d71f): Black Diamond added MFA around 2026-06-23, which is the cause. **The fix is a CODE fix in this lane.** The
     download consumes the durable trust-token/session that `bd-49f-auto-login` (the ADVI_BDAPIMIG producer) writes to
     Secrets Manager, instead of a fresh portal username/password login. No new credential, MFA device or vendor act is
     needed, so this is not a STOP. **Firm by firm:** read ONLY the bd firm's secret, never cot's, and never mirror or
     sync between them (CLAUDE.md rule 13).
     - A2's screenshot run becomes OPTIONAL. Run it only if the token route fails, to show what the token did not clear.
     - Do NOT modify `bd-49f-auto-login` or anything under ADVI_BDAPIMIG. Read its secret's NAME and SHAPE from its
       code, and consume it read-only. If the secret is absent, stale, or of another firm, STOP with a BLOCKING row
       naming which.
   - **AMENDED A4 (2.0.0_SA_COO~O, 2026-09-27 ~20:4xZ), SUPERSEDING A3's mechanism**, on Andrew-direct ~20:1xZ relayed
     by 1.0.0_SA_CTO~O (msg 20260927T203308Z): "see if you can just have a rest api pull for those tables. shouldnt
     need to make another 49 Financial bd crawler to get the long-trust token because we already have it with that
     existing crawler". Step 1 is now:
     1. **Check coverage first.** Do the `bd-49f-runner` and `bd-49f-fees-runner` Lambdas already pull the fees (and
        allocation) tables by REST? If a Playwright downloader is simply dead because REST already covers its table,
        report that with the evidence and do not rebuild it.
     2. **Replace the asset-dim Playwright portal download with a REST pull**, following those runners' pattern:
        - auth from the session / device-trust token the EXISTING `bd-49f-auto-login` writes to Secrets Manager
          `blackdiamond/49f/session`, read-only;
        - routes from `data/black_diamond/API/` (DataMining query types, `domains/datamining/endpoints`);
        - build NO new crawler and NO new login.
        The pull feeds the same downstream (`convert_assets_to_silver.py`).
     3. **49F only.** cot is a separate firm; never read its secret or mix its routes.
     Step 2 (the honest wrapper exit) stands for whatever path remains scheduled. A path this needs outside `<paths>` is a
     BLOCKING row naming it, and the issuer grants it; never an override.
   - **AMENDED A5 (2.0.0_SA_COO~O, 2026-09-27 ~22:0xZ), ruling row NFRA_MCPINDEX-Z-S30 (the successor seat's option (c)):**
     step 1 LEAVES this order, and AC1 (the download succeeding) leaves with it. MX-s-4 is now step 2 only, the honest
     wrapper exit, which landed at 03e744ec3f (SSM DocumentVersion 3 Active). It is graded on AC4, the CVO's judgment,
     once its last open leg L4 closes. Step 1.1 is ANSWERED: REST does not cover asset-dim. Step 1.2 (the REST pull) is
     routed to 1.0.0_SA_CTO~O as a new cell to DESIGN, because two things are not the issuer's to grant:
     (i) the 49F runner's ingest module lives in cot's tree (`data/cot/scripts/bronze/cot_bronze_ingest.py`), and
     Andrew's word is 49F only, with cot and bd never mixed; (ii) the dim's classification columns (`asset_super_class`,
     `asset_class`, `asset_segment`) have no documented REST route, so the pull may not reproduce what
     `build_bd_assets_dim.py` consumes.
2. **Make the wrapper's exit code honest.** A failed download or merge returns non-zero, so SSM records Failed. This is
   a producer reporting its own result, not an alarm.
3. **Restore the compaction to `silver/bd_assets.parquet`.** Check what the SSM document passes to
   `convert_assets_to_silver.py`; it writes the compacted file unless `--no-compacted` is passed.
4. Rebuild the bridge once, `build_bd_assets_dim.py`, from the now-current input. Adding the builder to the schedule is
   NOT this order's: report the spec (section 5, item 4) for a later ask.

**AMENDED by the issuer (2.0.0_SA_COO~O, 2026-09-26 ~21:3xZ) on your row NFRA_MCPINDEX-Z-S15:** steps 3 and 4 LEAVE this
order. The compaction to `silver/bd_assets.parquet` is gated on `--backfill` in `convert_assets_to_silver.py`, not on
`--no-compacted`, and the scheduled path passes `--latest`. So restoring it is a change to a DS-owned silver script (rule
13), and the bridge rebuild depends on it. Both move to `NFRA_MCPINDEX.TO-MX-s-6` (0.4.0_DS_ClientPlatform~D), with this
order's former AC2 and AC3. This order is now steps 1 and 2 only: the login, and the honest wrapper exit. Its
criteria are AC1 and AC4.

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
