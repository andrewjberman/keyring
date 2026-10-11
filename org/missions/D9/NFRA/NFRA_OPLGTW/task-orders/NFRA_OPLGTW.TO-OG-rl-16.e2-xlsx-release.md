# NFRA_OPLGTW task order -- `OG-rl-16` -- gateway release: dell2 ADVI_BILLING E2, copy_site_file_to_s3 (.xlsx -> fee_statement ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-16</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rl-16</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~51</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- host queue: r29, the allowlist and MP-x-4 are LIVE (host 1e32562729); MX-r-9 (applier AE~MX) is in flight next; THIS release's deploy follows MX-r-9's ledger close. Window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: RUN-BY-ISSUER -- the release carries ONE new inline policy, `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf` (aws_iam_role_policy.advi_billing_gateway_put: s3:PutObject on the bronze fee_statement prefix only), planned and applied by the applier under the pair, never here.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s rulings msg 32663 (TAKE E2) and @14cbf27dec (E2's .xlsx pair releases ALONE; the .pptx pair waits on S1 and S4), on dell2's packet org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/RELEASE_PACKET_E2.md @9828e7761f.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM reads of the gateway host).
</preflight>

## 1. THE CELL -- `OG-rl-16` (decomposition addendum R3-T.39)

Release dell2's E2 tool, `copy_site_file_to_s3`, with ONLY its `.xlsx` -> bronze `fee_statement` pair. The `.pptx` ->
`market_update` pair (OG-ab-2, on box/sitez) is NOT in this release. READ the packet (`MSYS_NO_PATHCONV=1 git show
9828e7761f:org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/RELEASE_PACKET_E2.md`), sections 2-7,
and the r29 ANNOUNCE (`deliverables/0.9.0_WK_NFRA_OPLGTW~43/ANNOUNCE_OG-rl-15.md` sections 13-14) for the form.
Reuse the ~43 r29 tooling in `deliverables/0.9.0_WK_NFRA_OPLGTW~43/` (`r29_ssm_prog.py`, `r29_md5_host.py`,
`r29_verify.py`) by copying to `rl16_` names in `W`.

### PHASE A (now) -- build and ask; NO deploy

1. **Base = the host's LIVE ref**, read by host md5 (`1e32562729` at the cut; if MX-r-9 has deployed by then, its ref).
2. **Release worktree** `C:/tmp/og-rel16`, branch `rel-nfra-oplgtw-r16`, at that base. Carry E2 ONLY:
   - the module and its tests (`931774fb11`);
   - the registration and the IAM file (`e8290dd5fe`; code paths only, as OG-ab-1 took them);
   - the carry (`cf84fd9a4d`: destructive_ops and data_entitlement entries, the deploy env line from address(), the
     tests, and the two count-updated tests);
   - NOT `5c2f6e9324` (OG-ab-2's .pptx pair).
   Cherry-pick per commit, restoring any path outside E2's set. If a cherry-pick conflicts because the base differs,
   resolve so that E2's hunks land and nothing else changes; report every conflict. The release commits need the
   audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` (the release tree carries no copy of this order; OG-tl-1 A1
   precedent) -- on the release branch's commits ONLY. Write `W/rl16_release.json` = `{"base_sha", "release_sha"}`.
3. Run E2's suites in the release tree (`test_advi_site_to_s3.py`, `test_advi_site_to_s3_registration.py`,
   `test_og_ab1_carry.py`) and the tool census (`r32/checks/tool_class_census.py <release tree>`).
4. `W/ANNOUNCE_OG-rl-16.md`: the never-widen ask for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`,
   `3.0.0_SA_CVO~Z`). It covers:
   - the release diff by file;
   - the ONE new write tool and its refusals (bad quarter, non-.xlsx, existing key: conditional put);
   - the ONE new grant (PutObject on the fee_statement prefix only; plan expected 1 add, 0 change, 0 destroy);
   - the ONE new env key (`ADVI_FEE_STATEMENT_S3_ROOT`, from address(); 52 -> 53 names);
   - both branches of a call (refused, writes nothing; admitted, one new key, never an overwrite);
   - writers N printed;
   - the order of acts (the TF policy under its own ledger, then the gateway deploy under `nfra-oplgtw-gateway-release-r16`);
   - the rollback per act (redeploy the base; destroy the one policy; delete written keys by key);
   - the triggers (`/health`, tools 66 -> 67 only, `.env` names 52 -> 53 only, no other value hash moved, md5 =
     release).
5. Run AC1, commit, REPORT, STOP.

### PHASE C (after the applier's deploy report, named by the issuer's continuation)

6. One SSM read through the INSTALLED host -> `W/RL16_READ.json` = `{"body": {...}, "ssm_command_id", "instance_id"}`,
   the host printing `E2_DIGEST <sha256 of json.dumps(body, sort_keys=True)>`. Body exactly: `served_release`,
   `installed_code: true`, `tool_listed`, `tool_safe`, `tool_write_class`, `bad_quarter_refused` (one call with
   quarter `2026Q9`, through the installed code's own entry, writes nothing), `objects_written: 0`,
   `fee_root_equals_address`, `market_update_root_present`. Then AC2.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~51/`.

## 2. BOUNDS

- You deploy, plan, apply, upload and restart NOTHING; the applier does Phase B.
- E2's paths only; never the .pptx pair, never another cell's gateway change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into a branch (row Z-W41-S5); override a
  gate other than the one audited lane escape named in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/advi_billing/
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/
infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~51/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W51-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; AC1 after Phase A from your worktree root; AC2 after Phase C)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-16"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rl16.AC1.sh; echo "exit=$?"</invocation><expect>(?s)outside E2's paths 0 \(want 0\); \.pptx-pair tokens in the release gateway tree 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-16"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rl16.AC2.sh; echo "exit=$?"</invocation><expect>(?s)E2 served: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-16" judgment="true"/>
</proof_of_spec>

- `AC1`: the release carries E2's .xlsx pair and nothing else.
- `AC2`: the served gateway lists and classifies the tool, refuses a bad call, and its root is the builder's.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): dell2's first real use (the Q3 2026 SMArtX statement) lands one new key and
  returns its sha256. Record it UNVERIFIABLE-BY-INSTRUMENT naming the CVO.

## 5. WHEN YOU ARE DONE

Proof instance at `W/NFRA_OPLGTW.TO-OG-rl-16.e2-xlsx-release.proof_of_spec.json`, validated; flip `<status>` only when
AC1 and AC2 PASS (after Phase C). Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Host queue: r29 -> allowlist -> MP-x-4 (all LIVE by 16:27Z) -> MX-r-9 (in flight) -> THIS -> the metadata route.
- Pre-cut: rl16.AC1 and rl16.AC2 base FAIL as expected (records absent); rl15_attest.py gains the E2_DIGEST rule
  (additive; tl1.AC2 re-run PASS after the edit).

<status>pending</status>
<round>33</round>
<workstream>E2-RELEASE</workstream>
<slot>~51</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
