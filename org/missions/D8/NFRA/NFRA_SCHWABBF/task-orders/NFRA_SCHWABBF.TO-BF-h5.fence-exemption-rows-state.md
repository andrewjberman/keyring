# TO NFRA_SCHWABBF.TO-BF-h5 -- the firm buckets' fence admits the box role and the converter role for the state prefixes only (registry rows, text only)

<to_id>NFRA_SCHWABBF.TO-BF-h5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~4</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>keyform-fence</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-h-5` (`decompositions/NFRA_SCHWABBF_DECOMP_R5.md`, AMENDMENT 1) |
**outcome_ref:** FWD-1, FWD-6, FWD-8 | **depends_on:** `BF-g-5` (merged)

---

## WORKER FACE

### THE CELL

`BF-h-5`, PRD v1.0 C-TIERS. The state tier of a firm-form Schwab master lives in the FIRM bucket (`opal-data-49financial`, `opal-data-cottonwood`). The cell before this one (`BF-g-5`, merged) gave the box role and the converter role the identity-side grants. Each firm bucket's policy also carries `DenyForeignFirmPrincipals` (Deny `s3:*` for every principal outside the firm's fence patterns and the registry's exemption rows), and neither role is in either, so every state write would still be refused. This cell adds THREE rows to the fence registry `infra/logic/registry/exemptions.json`. It edits that JSON file and adds one test. It runs no `terraform init`, `plan` or `apply` and no write `aws` command; the apply is the NFRA CloudOps lane's act after the never-widen pair.

**The rows (fixed).** The file is a JSON object whose `exemptions` key maps a bucket name to a list of rows. APPEND (do not remove, reorder or edit any existing row) to those two lists; row keys are only `principal`, `arn`, `reason`, `signoff_ref`, `actions`, `prefix` (the module refuses any other key, and `actions` and `prefix` go together). Account id `313476888478`.
1. `opal-data-49financial`: principal `quartz-si2-spike-role` (the 0840 box; `arn` `arn:aws:iam::313476888478:role/quartz-si2-spike-role`); `actions` [`s3:PutObject`]; `prefix` [`schwab/49financial/state/pulls/`, `schwab/49financial/state/daily_pull/`].
2. `opal-data-49financial`: principal `opal-assets-silver-schwab-role` (the Schwab converter; `arn` `arn:aws:iam::313476888478:role/opal-assets-silver-schwab-role`); `actions` [`s3:GetObject`, `s3:ListBucket`, `s3:PutObject`]; `prefix` [`schwab/49financial/state/complete/`, `schwab/49financial/state/conversions/`, `schwab/49financial/state/backfill_status/`].
3. `opal-data-cottonwood`: the same converter principal and actions; `prefix` [`schwab/cottonwood/state/complete/`, `schwab/cottonwood/state/conversions/`, `schwab/cottonwood/state/backfill_status/`].
Each prefix must equal what `lib/opal_naming.address('schwab', <firm>, 'state', <table>, 'date=2026-10-20')` returns, cut at `/date=` (the part after `s3://<bucket>/`, plus a trailing `/`): your test derives them from `address()`, the JSON holds the literal strings. Each row's `reason` is one sentence naming the cell (`NFRA_SCHWABBF BF-h-5`, PRD v1.0 C-TIERS, state tier of the Schwab masters, PutObject on two tables for 08403355 / read-write-list on three tables). Each row's `signoff_ref` is exactly: `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md (2.0.0_SA_COO~SB) and org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md @4b0036c6cb (1.0.0_SA_CTO), both halves signed; the CTO's condition: fence apply, then converter deploy, then puller upload`.
Keep the file's own formatting (indent, key order inside a row: principal, arn, reason, signoff_ref, actions, prefix, as the precedent row `opal-clientops-ews-role` in the same file has them) and its own line endings; `git diff --numstat` for the file must show only added lines (about 36).

**What exists (read first).** `infra/logic/registry/exemptions.json` (the precedent row `opal-clientops-ews-role` under `opal-data-49financial`, prefix `schwab/49financial/state/ews_store/current/`); the renderer `infra/aws/terraform/modules/opal_name/main.tf` lines 140-300 (a scoped row stays in `fence_exemption_arns` and renders three extra Denies: any other action, objects outside the prefixes, listings outside them); the merged identity-side grants `infra/aws/terraform/opal-assets/silver.tf` (policy `silver_state_write_schwab_firm`, resource list per master and table) and `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf` (`MonolithSchwabStateWrite`). You READ these and never edit them.

**Test.** New file `data/canonical/schwab/tests/test_fence_state_rows.py` (names of the test functions contain `fence_state`): (a) the three rows exist exactly as above (principal, actions as sets, prefix lists as sets), each prefix equals the `address()`-derived value; (b) no row names a wildcard, `s3:DeleteObject`, an action outside the closed set the module allows (`s3:GetObject`, `s3:ListBucket`, `s3:GetBucketLocation`, `s3:PutObject`), or a key outside the module's closed row-key set; (c) every prefix of the two converter rows is covered by the identity-side policy text in `silver.tf` (the table name appears in a `state/<table>/` resource of that policy) and every prefix of the box row by `monolith-iam.tf`, so a fence prefix with no identity grant fails; (d) the rows of the existing keys are byte-equal to HEAD (`git show HEAD:infra/logic/registry/exemptions.json` is the base; the old rows are a prefix of the new lists; use `git show` with the path, never a typed old copy); (e) the bucket of each new row's key equals the `bucket` of its firm in `infra/logic/registry/scopes.json`.

### ACCEPTANCE

<criterion id="BF5-h5-AC1" cell_refs="BF-h-5"><invocation>python -m pytest data/canonical/schwab/tests/test_fence_state_rows.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-h5-AC1` -- the three scoped exemption rows exist as fixed, built from the builder, covered by the identity grants, existing rows untouched.

<criterion id="BF5-h5-AC2" cell_refs="BF-h-5"><invocation>python lib/opal_naming.py validate</invocation><expect>^VALIDATE: OK </expect></criterion>
`BF5-h5-AC2` -- the seam probe against the REAL neighbor: the registry validator (`lib/opal_naming.py validate`) accepts the registry with the new rows (it refuses a malformed scoped row).

<criterion id="BF5-h5-AC3" cell_refs="BF-h-5"><invocation>terraform -chdir=infra/aws/terraform/modules/opal_name test -no-color</invocation><expect>^Success! [0-9]+ passed, 0 failed\.$</expect></criterion>
`BF5-h5-AC3` -- the control: the naming module's own `terraform test` (95 passed at the base) still passes with the new rows (its plan-time preconditions refuse a half-scoped or malformed row).

<expected_criteria>BF5-h5-AC1,BF5-h5-AC2,BF5-h5-AC3</expected_criteria>

Dry-run at the base: AC1 "file or directory not found" (rc 4) -- FAIL as expected; AC2 `VALIDATE: OK` and AC3 `Success! 95 passed, 0 failed.` -- PASS as expected (controls that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply` in any root, no deploy, no AWS call. The shared-infra apply is the CloudOps lane's act under `safe-apply` after the never-widen pair; both halves are written and signed. You do not write either half and you do not edit `infra/aws/terraform/shared-infra/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W4-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]` and keep the file's own line endings; verify `git diff --numstat` shows only added lines). Do not weaken the test to pass.

<paths>
infra/logic/registry/exemptions.json
data/canonical/schwab/tests/test_fence_state_rows.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R5.md</decomp_doc> (round 5, AMENDMENT 1), cell `BF-h-5`.
<owned_cells>BF-h-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF5-h5-AC1, BF5-h5-AC2, BF5-h5-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~4/NFRA_SCHWABBF.TO-BF-h5.fence-exemption-rows-state.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF5-h5-AC1,BF5-h5-AC2,BF5-h5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the three rows' line numbers, the `git diff --numstat` line for `exemptions.json`, the three summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- registry text; no schedule.
comp-iam: RUN -- scanned the two firm buckets' fence statements (shared-infra/s3-49financial.tf 114-137, s3-lgic-firm-buckets.tf 142-170, read by worker ~4 at BF-g-5), the registry exemptions.json (opal-data-49financial 30 rows, opal-data-cottonwood 7) and the renderer in modules/opal_name/main.tf, 3 files; neither the box role nor the converter role is in either bucket's list today; this cell adds three scoped rows (text only); BLIND: the live IAM plane and the live bucket policies (0 read).
comp-adversary: DECLARED-NOT-APPLICABLE -- surprise row NFRA_SCHWABBF-W4-S9 is the cell; the scoped grammar is prefix-wide while the identity side is master-wide, named in the COO half.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-TIERS, C-ALONGSIDE (IAM shape); row NFRA_SCHWABBF-W4-S9; the precedent row `opal-clientops-ews-role` (commit e2313fed924); decomposition round 5 AMENDMENT 1; merge `f27dfcc831e` (BF-g-5).
