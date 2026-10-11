# ADVI_FIRMBKTS task order -- `FB-g-19` -- A SCOPED FENCE-EXEMPTION ROW'S `prefix` TAKES A STRING OR A LIST (THE CTO'S ADDENDUM 9, AHEAD OF ACT 3b)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~41</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the builder and the module's files; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_modfence.py` reads 3 of 4: R1 diff 0, R3 refusal and R4 clean plan PASS as controls; R2 FAILS as expected (a list-prefix row renders nothing: the module refuses it). Blindness: the check runs the module with `terraform console` and `terraform plan` over a mirror tree; it cannot see how a bucket policy built from the statements behaves in S3.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-19` (round 4, workstream `FENCE3B`; the CTO's round-3 ADDENDUM 9, msg 3917)

`infra/aws/terraform/modules/opal_name/main.tf` renders each SCOPED exemption row of `infra/logic/registry/exemptions.json` (a row carrying `actions` and a `prefix`)
into three Deny statements that cut the principal down to those actions under that prefix. `prefix` is one string ending in
`/`. The performance adapter must read two places in the canonical bucket (its holdings gold and the ownership key), and the
live policy holds hand-kept statements for it that deny anything outside ONE prefix: a row cannot say two. The CTO ruled:
`prefix` takes a string OR a list, rendered as `NotResource` over each. You build that in the module and the builder's
registry validation, dormant: every existing row renders byte-identically.

### 1a. Behavior (the whole spec)

1. **The module** (`infra/aws/terraform/modules/opal_name/main.tf`): a row's `prefix` may be a string (today's form) or a non-empty list of strings. Every prefix
   (each list member too) must end in `/`, not start with `/`, hold no `*` or `?`, and not be empty; a malformed list, an empty
   list, or a list holding a malformed member is refused by the same `precondition` that refuses a malformed string today
   (nothing is rendered). The statements:
   - object statement: `NotResource` is the list `[arn:aws:s3:::<bucket>/<p>*, ...]`, one entry per prefix;
   - listing statement: `StringNotLike` `s3:prefix` is the list `[<p>*, ...]`;
   - the any-other-action statement is unchanged.
   For a string prefix the rendered statements are byte-identical to today's (a one-element list renders as today's
   one-element list: today's `NotResource` and `StringNotLike` values are single-element lists/strings; keep the exact
   JSON shape for a string row).
2. **The builder** (`lib/opal_naming.py`): if `validate()` checks the exemptions file's row fields, accept a list `prefix` under the
   same rules (read the function that validates `exemptions.json`; if it does not check `prefix`, change nothing there).
3. **Dormant.** The real registry's rendering is unchanged (`diff 0`, every bucket printed by the check).

## 2. BOUNDS

1. Files that change: `infra/aws/terraform/modules/opal_name/main.tf` and, only if its validation names `prefix`, `lib/opal_naming.py`. No registry row is added or
   changed (no fixture row in the real file); no other module file; no consumer root; no apply; no AWS call.
2. `terraform init -backend=false` and `terraform test` in the module folder are local and allowed; keep `.terraform` out of
   the commit.
3. If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/modules/opal_name/main.tf
lib/opal_naming.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~41/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~41/ADVI_FIRMBKTS.TO-FB-g-19.fence-prefix-list.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-19"><invocation>cd /c/dev/wk-firmbkts-41 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modfence.py --arms render --root /c/dev/wk-firmbkts-41; echo "exit=$?"</invocation><expect>ROUND 4 MODULE FENCE: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-19"><invocation>cd /c/dev/wk-firmbkts-41/infra/aws/terraform/modules/opal_name &amp;&amp; timeout 100 terraform init -backend=false -input=false -no-color &gt; /dev/null &amp;&amp; timeout 100 terraform test -no-color 2&gt;&amp;1 | tail -n 3</invocation><expect>Success! \d+ passed, 0 failed</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-19"><invocation>cd /c/dev/wk-firmbkts-41 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-41 --allow infra/aws/terraform/modules/opal_name/main.tf --allow lib/opal_naming.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~41/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/modules/opal_name/main.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 evaluates the base module and the tree's over the real registry (diff 0), a list-prefix fixture (renders; the base
refuses it) and four malformed fixtures (refused). AC2 is the module's own tests (48 at base). AC3 is the write-surface
bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-19.fence-prefix-list.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~41`. Commit
the file(s) and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it). Row
ids: `ADVI_FIRMBKTS-D1-W41-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 9 (msg 3917) after the identity-side census
(`IDENTITY_CENSUS_20261011.txt`: the performance adapter is admitted but scoped to one prefix by three hand statements).
Workstream `FENCE3B`; act 3b's registry rows (the performance adapter's two-prefix row among them) are the next cell.
Class WORLD by the path floor, dormant.

<status>complete</status>
<round>4</round>
<workstream>FENCE3B</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-19</to_id>
<slot>~41</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
