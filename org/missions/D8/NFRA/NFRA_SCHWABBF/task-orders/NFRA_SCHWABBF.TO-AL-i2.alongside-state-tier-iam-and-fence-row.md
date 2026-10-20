# TO NFRA_SCHWABBF.TO-AL-i2 -- the Alongside box role writes its run records to the Cottonwood firm bucket's state tier, and the bucket's fence admits that role for exactly those prefixes (Terraform text and one registry row)

<to_id>NFRA_SCHWABBF.TO-AL-i2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~15</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-state</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-i-2` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `AL-a-1` and `BF-h-5` (both merged; their files are in your base)

---

## WORKER FACE

### THE CELL

`AL-i-2`, PRD v1.0 C-TIERS applied to the Alongside Schwab Box. C-TIERS: `meta/` and `_ops/` become the builder's `state` tier, which lives in the FIRM bucket: for the four Cottonwood masters, `s3://opal-data-cottonwood/schwab/cottonwood/state/{table}/date={D}/{master}.{name}`. The 49F puller (`infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` at HEAD, functions `Get-StateBucket`, `Get-StateKey`, `Get-RunRecordDests`, lines ~200-230, and the run-record writes near line 750) already writes a firm-form master's run records there with `aws s3 cp --sse AES256`: three objects per run, `daily_pull/date={write day}/{master}.last_run.json`, `daily_pull/date={run day}/{master}.{RUNID}.json` and `pulls/date={run day}/{master}.{RUNID}.json`. So the Alongside box role needs `s3:PutObject` on exactly those tables, per master, and the Cottonwood bucket's policy `DenyForeignFirmPrincipals` (Deny `s3:*` to every principal outside the fence patterns and the registry's exemption rows) must admit the role for those prefixes only. CTO condition 6 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_HALF_CTO_NFRA_SCHWABBF_ALONGSIDE_BOX_BUILD_20261020.md`): no rule is enabled, and no pull runs beyond the first-day trace, until the role's tier statements match v0.9 C-TIERS. This cell edits Terraform TEXT, one registry JSON file and tests. You run no `terraform` command and no `aws` command.

**Read first (read-only):** `infra/aws/terraform/alongside-schwab-ec2/iam.tf` and `masters.tf` (your own cell AL-a-1's files, in your base); `infra/logic/registry/exemptions.json` (the `exemptions` object maps a bucket name to a list of rows; READ the precedent rows `opal-clientops-ews-role` and, if present at your base, the three `BF-h-5` rows `quartz-si2-spike-role` and `opal-assets-silver-schwab-role`); `data/canonical/schwab/tests/test_fence_state_rows.py` (the `BF-h-5` test: copy its method for the byte-equal-to-HEAD check); `infra/aws/terraform/modules/opal_name/main.tf` lines ~140-300 (how a scoped row renders: three extra Denies); `lib/opal_naming.py` `address()`.

**Build.**
1. `infra/aws/terraform/alongside-schwab-ec2/iam.tf`:
   - REMOVE the statements `MonolithSchwabOpsWrite` and `MonolithSchwabMetaPullsWrite` (master-scope `_ops` and `meta/pulls` in `opal-data-assets`). The puller no longer writes them for a firm-form master, and this role is new, so nothing legacy needs them. Say so in a comment where they were.
   - ADD one statement `StateTierWrite`: `s3:PutObject` only, on one resource PER MASTER PER TABLE built with a `for` over `keys(local.alongside_masters)` and the two tables `pulls` and `daily_pull`: `arn:aws:s3:::<firm bucket>/schwab/${local.alongside_firm}/state/${table}/date=*/${master}.*` (8 resources). No `s3:GetObject`, no `s3:ListBucket` (the puller only writes there), no `s3:DeleteObject`, no resource that ends `/state/*`. The firm bucket name is NOT typed twice: put it in `local.alongside_state_bucket` in `masters.tf`? No: `masters.tf` is not in your grant, so define `local.alongside_state_bucket` at the top of `iam.tf`. Its value is the `bucket` of the `cottonwood` firm row in `infra/logic/registry/scopes.json` (`opal-data-cottonwood`); a test pins the equality both ways.
   - Keep the code read, the secret statements, the bronze list and write statements and the three Deny planes byte-identical.
2. `infra/logic/registry/exemptions.json`: APPEND (do not remove, reorder or edit any existing row; the previous last row of the `opal-data-cottonwood` list gains a trailing comma, or create the list if the key is absent at your base) ONE row under `opal-data-cottonwood`, in the key order the precedent rows use (`principal`, `arn`, `reason`, `signoff_ref`, `actions`, `prefix`): `principal` `schwab-alongside-si2-box-role`; `arn` `arn:aws:iam::313476888478:role/schwab-alongside-si2-box-role`; `actions` [`s3:PutObject`]; `prefix` [`schwab/cottonwood/state/pulls/`, `schwab/cottonwood/state/daily_pull/`]. `reason`: one sentence naming the cell (`NFRA_SCHWABBF AL-i-2`, PRD v1.0 C-TIERS, the Alongside Schwab Box writes run records for the four Cottonwood masters, PutObject on two tables). `signoff_ref`, exactly: `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/NEVER_WIDEN_ALONGSIDE_STATE_FENCE_COO_HALF.md (2.0.0_SA_COO~SA) and org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_ALONGSIDE_STATE_FENCE_CTO_HALF.md (1.0.0_SA_CTO); the apply waits on both halves signed`. The module refuses any other row key; each prefix must equal `lib/opal_naming.address('schwab','cottonwood','state',<table>,'date=2026-10-20')` cut at `/date=` (the part after `s3://<bucket>/`, plus a trailing `/`). `git diff --numstat` for the file should show about 12 added lines and at most 1 changed line.
3. Tests: new file `data/canonical/schwab/tests/test_alongside_state_tier.py`:
   - STATE TIER (name contains `state_tier`): `iam.tf` has no `MonolithSchwabOpsWrite` and no `MonolithSchwabMetaPullsWrite`; the `StateTierWrite` statement is PutObject only with exactly 8 resources derived from the master map and the two tables; no Get, Delete or List on the state prefix; no resource ends `/state/*`; `local.alongside_state_bucket` equals the registry's `bucket` for `cottonwood`; the bronze write statement and the three Deny statements are unchanged in text from `git show HEAD:infra/aws/terraform/alongside-schwab-ec2/iam.tf`.
   - FENCE ROW (name contains `fence_row`): the new row exists exactly as above; its prefixes equal the `address()`-derived values; its actions are a subset of the module's closed set (`s3:GetObject`, `s3:ListBucket`, `s3:GetBucketLocation`, `s3:PutObject`) and are exactly `s3:PutObject`; no wildcard, no `s3:DeleteObject`, no extra key; every earlier row of both bucket lists is byte-equal to `git show HEAD:infra/logic/registry/exemptions.json` (the old rows are a prefix of the new lists; use `git show` with the path, never a typed old copy); each fence prefix is covered by a `StateTierWrite` resource of that table name.
   - In `test_alongside_box_tf.py`, edit any assertion that pins the removed `_ops` / `meta/pulls` statements so it expects their absence; keep every other assertion. That file's full run must stay green.

### ACCEPTANCE

<criterion id="AL2-i2-AC1" cell_refs="AL-i-2"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_state_tier.py -q -p no:cacheprovider --color=no -k "state_tier"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-i2-AC1` -- the box role writes only the two run-record tables, per master, in the firm bucket, and the master-scope `_ops`/`meta` statements are gone.

<criterion id="AL2-i2-AC2" cell_refs="AL-i-2"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_state_tier.py -q -p no:cacheprovider --color=no -k "fence_row"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-i2-AC2` -- the fence admits the role for exactly those two prefixes with PutObject, and no earlier row moved.

<criterion id="AL2-i2-AC3" cell_refs="AL-i-2"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_tf.py data/canonical/schwab/tests/test_alongside_schedule_tf.py data/canonical/schwab/tests/test_alongside_state_tier.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-i2-AC3` -- the whole Alongside Terraform test suite stays green with the edit.

<expected_criteria>AL2-i2-AC1,AL2-i2-AC2,AL2-i2-AC3</expected_criteria>

Dry-run at the base 2026-10-20: AC1 and AC2 have no test file (rc 4) -- FAIL as expected. AC3 names a file that does not exist yet, so pytest exits 4 -- FAIL as expected. Write the new test file FIRST and watch AC1 and AC2 fail on the unedited files, then edit.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit (including `monolith-iam.tf`, `silver.tf`, `schedule.tf`, `masters.tf`, `secrets.tf`, `box.tf`, `main.tf` of the Alongside root, and every other `exemptions.json` row).
- **WORLD floor, nothing applied.** No `terraform`, no `aws`. The registry row is a never-widen fence edit: it applies only after both halves are signed (the issuer's act with the CTO), and the apply is the CloudOps lane's. Do not claim the fence is open.
- **Refusal clause.** If a criterion cannot be met as written (the module refuses the row, the builder refuses an address), stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W15-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a test.

<paths>
infra/aws/terraform/alongside-schwab-ec2/iam.tf
infra/logic/registry/exemptions.json
data/canonical/schwab/tests/test_alongside_state_tier.py
data/canonical/schwab/tests/test_alongside_box_tf.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-i-2`.
<owned_cells>AL-i-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL2-i2-AC1, AL2-i2-AC2, AL2-i2-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~15/NFRA_SCHWABBF.TO-AL-i2.alongside-state-tier-iam-and-fence-row.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-i2-AC1,AL2-i2-AC2,AL2-i2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the statements removed and added with file and line, the registry row's diff numstat, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule edit.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- one PutObject statement per (master, table), the same shape as BF-g-5's box statement; BLIND: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE -- the finding is the firm bucket's DenyForeignFirmPrincipals (read live by the issuer 2026-10-20 ~20:2xZ: it denies every s3:* to a principal outside `role/*-cot-*` and a named list; `schwab-alongside-si2-box-role` matches neither), so the identity grant alone is necessary and not sufficient.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-TIERS, C-ALONGSIDE, C-ONEWRITER; CTO half condition 6; `~SB`'s `BF-g-5` and `BF-h-5` as the precedent; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-i-2.
