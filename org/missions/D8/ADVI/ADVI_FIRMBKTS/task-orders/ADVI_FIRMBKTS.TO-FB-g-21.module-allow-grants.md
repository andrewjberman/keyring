# ADVI_FIRMBKTS task order -- `FB-g-21` -- THE `opal_name` MODULE RENDERS A BUCKET-POLICY ALLOW BESIDE EACH SCOPED DENY ROW, AN ALLOW-ONLY `grants` ROW, AND ACCEPTS AN EXACT OBJECT KEY IN A ROW'S PREFIX LIST (THE CTO'S ADDENDUM 10)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-21</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~43</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the module's file and the builder's validation; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. The statements the module learns to RENDER are not applied by this cell; the real registry renders none.
comp-adversary: RUN by the issuer -- at base `r4_modallow.py` reads 1 of 5 (R5 clean plan PASS as the control; R1 to R4 FAIL as expected: no allow output, no exact-key entry, no grants, no refusal of a malformed grants row). Blindness: the check evaluates the module with `terraform console` and `terraform plan` over a mirror tree; it cannot see how S3 evaluates a bucket policy built from these statements, so the close read of the act is the one place that is measured live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-21` (round 4, workstream `FENCEALW`; the CTO's round-3 ADDENDUM 10, msg 3922)

`infra/aws/terraform/modules/opal_name/main.tf` renders each SCOPED exemption row of `infra/logic/registry/exemptions.json` (a row carrying `actions` and a
`prefix`, where `prefix` is a string or a list since `FB-g-19`) into Deny statements that cut the principal down to those
actions under those prefixes. Within one account a bucket-policy ALLOW that names a role's ARN admits that role with no
identity-side grant, so the fence's next act renders an Allow from the SAME row, plus an Allow-only row for principals the
fence already admits by other means. Three additions, dormant: the real registry renders no Allow and no changed Deny.

### 1a. Behavior (the whole spec)

1. **An exact object key in a prefix list.** A `prefix` entry (string, or each list member) that does NOT end in `/` is an
   exact OBJECT KEY; one ending in `/` is a PREFIX (today's meaning). Every entry still must be non-empty, not start with `/`,
   and hold no `*` or `?`; the list must be non-empty. In the Deny statements a prefix entry renders as today
   (`arn:aws:s3:::<bucket>/<p>*` in `NotResource`, `<p>*` in `StringNotLike s3:prefix`), and a key entry renders WITHOUT the
   trailing `*` (`arn:aws:s3:::<bucket>/<key>`, `<key>`). A row whose every entry ends in `/` renders byte-identically to
   today.
2. **An Allow beside each scoped Deny row, from the same row.** A new local AND output named
   `fence_scoped_allow_statements`, keyed by bucket like `fence_scoped_statements` (an empty list for a bucket with no
   scoped row and no grants row). For scoped row N (1-based, the row's position among the bucket's scoped rows):
   - if `actions` holds `s3:GetObject`: one statement `Sid = "AllowScopedExemptionNObjects"`, `Effect = "Allow"`,
     `Principal = { AWS = <the row's principal ARN, as the Deny side computes it> }`, `Action = ["s3:GetObject"]`,
     `Resource` = one entry per prefix entry (`arn:aws:s3:::<bucket>/<p>*` for a prefix, `arn:aws:s3:::<bucket>/<key>`
     for a key);
   - if `actions` holds `s3:ListBucket`: one statement `Sid = "AllowScopedExemptionNListing"`, `Effect = "Allow"`, the same
     Principal, `Action = ["s3:ListBucket"]`, `Resource = ["arn:aws:s3:::<bucket>"]`, `Condition = { StringLike =
     { "s3:prefix" = [<p>* for a prefix, <key> for a key] } }`;
   - `s3:GetBucketLocation` renders no Allow (it stays an identity-side matter).
3. **An Allow-only `grants` row.** `exemptions.json` may carry a top-level `grants` object: `{ "<bucket>": [ row, ... ] }`
   (absent today; read it with `try`, an absent key is the empty map). A grants row's keys are exactly `principal`, `arn`
   (optional), `reason`, `signoff_ref`, `actions`, `keys`. `actions` is a non-empty list drawn from `["s3:GetObject"]`
   only; `keys` is a non-empty list of exact object keys (each non-empty, no leading `/`, no `*` or `?`, not ending in `/`);
   the principal is not `*` and starts `arn:` (or is a role name, as the exemption rows allow). Each grants row N (1-based
   among the bucket's grants rows) renders ONE statement appended AFTER the scoped rows' Allows in the same list:
   `Sid = "AllowGrantNObjects"`, `Effect = "Allow"`, Principal as above, `Action = ["s3:GetObject"]`, `Resource` = one exact
   key ARN per key. A grants row renders NO Deny and does NOT enter `fence_exemption_arns`.
4. **Refusal, fail-closed.** A malformed scoped row (the rules of item 1) or grants row (item 3), or a grants row with a key
   outside the list in item 3, makes `terraform plan` of the module fail through a `precondition` on the output
   `fence_scoped_allow_statements` (and on `fence_scoped_statements` and `fence_exemption_arns` for a scoped row, as today),
   with an error message naming `infra/logic/registry/exemptions.json` and the row.
5. **The builder** (`lib/opal_naming.py`): `validate()` already checks the exemptions file's scoped rows (changed by FB-g-19). Make
   it accept an exact key in a `prefix` entry under item 1's rules and check a `grants` object under item 3's rules; a
   change it does not need to make is not made. The real registry still validates.
6. **Dormant.** The real registry's `fence_scoped_statements` is unchanged for every bucket, and
   `fence_scoped_allow_statements` is the empty list for every bucket.

## 2. BOUNDS

1. Files that change: `infra/aws/terraform/modules/opal_name/main.tf` and `lib/opal_naming.py`. No registry row is added or changed (no fixture row in the real file); no
   other module file; no consumer root; no apply; no AWS call.
2. `terraform init -backend=false` and `terraform test` in the module folder are local and allowed; keep `.terraform` out of
   the commit. The module's own tests must still pass unchanged.
3. If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/modules/opal_name/main.tf
lib/opal_naming.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~43/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~43/ADVI_FIRMBKTS.TO-FB-g-21.module-allow-grants.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-21"><invocation>cd /c/dev/wk-firmbkts-43 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modallow.py --arms render --root /c/dev/wk-firmbkts-43; echo "exit=$?"</invocation><expect>ROUND 4 MODULE ALLOW: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-21"><invocation>cd /c/dev/wk-firmbkts-43/infra/aws/terraform/modules/opal_name &amp;&amp; timeout 100 terraform init -backend=false -input=false -no-color &gt; /dev/null &amp;&amp; timeout 100 terraform test -no-color 2&gt;&amp;1 | tail -n 3</invocation><expect>Success! \d+ passed, 0 failed</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-21"><invocation>cd /c/dev/wk-firmbkts-43 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-43 --allow infra/aws/terraform/modules/opal_name/main.tf --allow lib/opal_naming.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~43/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/modules/opal_name/main.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 evaluates the base module and the tree's over the real registry (Deny identical, allow empty), a string-prefix fixture
(Deny identical), a key-entry fixture (Deny and Allow), a grants fixture, and ten malformed fixtures (all refused). AC2 is
the module's own tests (48 at base). AC3 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-21.module-allow-grants.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~43`.
Commit the file(s) and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W43-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 10 (msg 3922; conditions 1 to 4). The grants row exists because
`irpt-holdings-role` (a full exemption row today) and `irpt-49f-reporting-read-role` (admitted by the scope pattern) are
already admitted at the fence; narrowing their rows to scoped ones would risk their live reads of the same bucket, so they get
an Allow and no new Deny. The registry rows and the shared-infra wiring are `FB-g-22`, cut after this merges. The
performance adapter's row (list prefix, a key entry) replaces its hand-kept statements in `FB-g-22`. Workstream `FENCEALW` (FB-g-19 and FB-g-20 were FENCE3B).
Class WORLD by the path floor, dormant.

<status>complete</status>
<round>4</round>
<workstream>FENCEALW</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-21</to_id>
<slot>~43</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
