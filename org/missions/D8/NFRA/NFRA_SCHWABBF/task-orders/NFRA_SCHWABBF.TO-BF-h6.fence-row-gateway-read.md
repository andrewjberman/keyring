# TO NFRA_SCHWABBF.TO-BF-h6 -- the 49financial fence admits the gateway's catalog read role for GetObject and ListBucket on the state `complete` prefix only (registry row, text only)

<to_id>NFRA_SCHWABBF.TO-BF-h6</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-fence</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-h-6` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, AMENDMENT 1) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** `BF-h-5` (merged)

---

## WORKER FACE

### THE CELL

`BF-h-6`. The gateway reads 0840's completion marker from the state tier (`s3://opal-data-49financial/schwab/49financial/state/complete/date=D/08403355.complete.json`) with the role `gateway-schwab-catalog-read-role`. The bucket policy `DenyForeignFirmPrincipals` of `opal-data-49financial` denies every principal outside the firm fence and the registry's exemption rows, and this role is in neither, so the gateway's new-path read would answer AccessDenied (the gateway's dual read treats AccessDenied as a hard error, not a fallback). CTO ruling (addendum 2 of the CTO half, `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @e79769e167): add ONE scoped row, READ only. This cell edits `infra/logic/registry/exemptions.json` and the test `data/canonical/schwab/tests/test_fence_state_rows.py` (merged by `BF-h-5`; read it first). It runs no `terraform init`, `plan` or `apply` and no write `aws` command.

**The row (fixed).** APPEND to the `opal-data-49financial` list (after the last row; do not remove, reorder or edit any existing row; keep the file's own formatting and line endings; the key order inside a row is principal, arn, reason, signoff_ref, actions, prefix):
- `principal`: `gateway-schwab-catalog-read-role`; `arn`: `arn:aws:iam::313476888478:role/gateway-schwab-catalog-read-role`;
- `actions`: [`s3:GetObject`, `s3:ListBucket`]; NO write action;
- `prefix`: [`schwab/49financial/state/complete/`] (this one table only; equal to what `lib/opal_naming.address('schwab','49financial','state','complete','date=2026-10-20')` returns after `s3://opal-data-49financial/`, cut at `date=`);
- `reason`: one sentence: `NFRA_SCHWABBF BF-h-6 (PRD v1.0 C-TIERS, CTO addendum 2): the gateway's catalog read role reads the completion markers of the 49financial state tier (GetObject and ListBucket on the complete table only, no write).`
- `signoff_ref`: exactly `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md (2.0.0_SA_COO~SB, addendum 1) and org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md @e79769e167 (1.0.0_SA_CTO, addendum 2)`.

**Test.** In `test_fence_state_rows.py` add arms whose function names contain `fence_state_gateway`: (a) the fourth row exists exactly as above (actions and prefix as sets; arn equals `arn:aws:iam::313476888478:role/gateway-schwab-catalog-read-role`); (b) it names no write action, no wildcard, no `s3:DeleteObject`; (c) its prefix equals the `address()`-derived `complete` prefix. Adjust any existing arm that asserts the exact number of new rows under `opal-data-49financial` (now three there: the box, the converter, the gateway; `opal-data-cottonwood` is unchanged at the rows already there) and the arm that requires every new row's prefix to be covered by an identity-side policy in this repo: that arm applies to the box row and the two converter rows only (the gateway's identity side is the gateway's own Terraform, not this repo's). The rows of other seats (`opal-clientops-ews-role`, `schwab-alongside-si2-box-role`) are not yours: your arm (d) of `BF-h-5` ("existing rows byte-equal to HEAD") stays true.

### ACCEPTANCE

<criterion id="BF6-h6-AC1" cell_refs="BF-h-6"><invocation>python -m pytest data/canonical/schwab/tests/test_fence_state_rows.py -q -p no:cacheprovider --color=no -k fence_state_gateway</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-h6-AC1` -- the fourth row exists as fixed (read only, one table). You also run the whole file once (the earlier arms must still pass) and report that line.

<criterion id="BF6-h6-AC2" cell_refs="BF-h-6"><invocation>python lib/opal_naming.py validate</invocation><expect>^VALIDATE: OK </expect></criterion>
`BF6-h6-AC2` -- the seam probe against the REAL neighbor: the registry validator accepts the registry with the fourth row.

<criterion id="BF6-h6-AC3" cell_refs="BF-h-6"><invocation>terraform -chdir=infra/aws/terraform/modules/opal_name test -no-color</invocation><expect>^Success! [0-9]+ passed, 0 failed\.$</expect></criterion>
`BF6-h6-AC3` -- the control: the naming module's `terraform test` (95 passed at the base) still passes.

<expected_criteria>BF6-h6-AC1,BF6-h6-AC2,BF6-h6-AC3</expected_criteria>

Dry-run at the base: AC1 "no tests ran" / deselected (rc 5, no test named `fence_state_gateway`) -- FAIL as expected; AC2 `VALIDATE: OK` and AC3 `Success! 95 passed, 0 failed.` -- PASS as expected (controls that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no deploy, no AWS call. The apply is the NFRA CloudOps lane's act (`BF-r-2`, tonight) under the signed pair.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W2-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]`; the previous last row gains a trailing comma). Do not weaken the test to pass.

<paths>
infra/logic/registry/exemptions.json
data/canonical/schwab/tests/test_fence_state_rows.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6, AMENDMENT 1), cell `BF-h-6`.
<owned_cells>BF-h-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF6-h6-AC1, BF6-h6-AC2, BF6-h6-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-h6.fence-row-gateway-read.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-h6-AC1,BF6-h6-AC2,BF6-h6-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the row's line numbers, the `git diff --numstat` line for `exemptions.json`, the three summary lines, the whole-file summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- registry text; no schedule.
comp-iam: RUN -- scanned the 49financial bucket fence statement (shared-infra/s3-49financial.tf 114-137, read at BF-g-5), the registry exemptions.json (opal-data-49financial rows) and the renderer in modules/opal_name/main.tf, 3 files; the gateway role is in neither list today; this cell adds one scoped READ row (text only); BLIND: the live IAM plane and the live bucket policy (0 read here; the apply order reads them).
comp-adversary: DECLARED-NOT-APPLICABLE -- finding inlined: the row is table-wide (the registry grammar scopes by prefix, not by master) and read-only.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO half addendum 2 @e79769e167 (msgs 110044, 110046, 110054); site Z's findings OG-sk-3 (relayed msgs 110041, 110043, 110053); PRD v1.0 C-TIERS; merge `27acf60210d` (BF-h-5).
