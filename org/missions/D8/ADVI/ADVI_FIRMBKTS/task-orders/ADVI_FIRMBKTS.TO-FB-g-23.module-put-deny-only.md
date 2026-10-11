# ADVI_FIRMBKTS task order -- `FB-g-23` -- A SCOPED FENCE ROW MAY NAME `s3:PutObject`, RENDERED ON THE DENY SIDE ONLY (THE CTO'S ADDENDUM 11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-23</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~45</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the module's file and the builder's validation; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. The module learns to RENDER a Deny exemption for a write action; the real registry renders none.
comp-adversary: RUN by the issuer -- at base `r4_modput.py` reads 3 of 5 (P1 identical, P4 refusals and P5 clean plan PASS as controls; P2 and P3 FAIL as expected: a Get+Put row does not plan, PutObject is outside the closed set). Blindness: `terraform console` and `terraform plan` over a mirror tree; it cannot see how S3 evaluates the statements.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-23` (round 4, workstream `FENCEPUT`; the CTO's round-3 ADDENDUM 11, msg 3927)

The exec-summary generator writes `platinum/advisors/<id>/exec_summary.json`. After the flip it must write the canonical home,
so the bucket's fence needs a Deny EXEMPTION that lets `s3:PutObject` through under one prefix. The standing rule the CTO set:
generated bucket-policy Allows are read-only; a write is granted identity-side in the writer's own root. So the module learns
a write action on the fence side and never renders an Allow for it. Dormant: the real registry names no write action.

### 1a. Behavior (the whole spec)

1. **The closed action set.** A scoped row's `actions` may now also hold `s3:PutObject` (today: `s3:GetObject`,
   `s3:ListBucket`, `s3:GetBucketLocation`). Nothing else is added: `s3:PutObjectAcl`, `s3:PutObjectTagging`,
   `s3:DeleteObject`, `s3:PutObjectVersionAcl` and `s3:*` stay REFUSED, through the same `precondition`s that refuse an
   action outside the set today.
2. **The Deny side.** `s3:PutObject` is an OBJECT action: it renders in the row's `AnyOtherAction` statement's `NotAction`
   (so it is not denied) and in the `ObjectsOutsidePrefix` statement's `Action` with the row's `NotResource` (so it is denied
   outside the row's prefix entries), exactly as `s3:GetObject` does. A row without `s3:PutObject` renders byte-identically
   to today.
3. **No write Allow, ever.** `fence_scoped_allow_statements` (from `FB-g-21`) renders its Allow for `s3:GetObject` and
   `s3:ListBucket` only. A row whose actions are `["s3:PutObject"]` alone renders NO Allow statement. A `grants` row naming
   `s3:PutObject` is refused (its closed set stays `["s3:GetObject"]`).
4. **The builder** (`lib/opal_naming.py`): `validate()` accepts `s3:PutObject` in a scoped row's `actions` under item 1 and still
   refuses the actions item 1 names; a change it does not need to make is not made. The real registry still validates.
5. **Dormant.** The real registry's two outputs are unchanged for every bucket.

## 2. BOUNDS

1. Files that change: `infra/aws/terraform/modules/opal_name/main.tf` and `lib/opal_naming.py`. No registry row is added or changed; no other module file; no consumer root; no
   apply; no AWS call.
2. `terraform init -backend=false` and `terraform test` in the module folder are local and allowed; keep `.terraform` out of
   the commit. The module's own tests must still pass unchanged.
3. If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/modules/opal_name/main.tf
lib/opal_naming.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~45/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~45/ADVI_FIRMBKTS.TO-FB-g-23.module-put-deny-only.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-23"><invocation>cd /c/dev/wk-firmbkts-45 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modput.py --arms put --root /c/dev/wk-firmbkts-45; echo "exit=$?"</invocation><expect>ROUND 4 MODULE PUT: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-23"><invocation>cd /c/dev/wk-firmbkts-45/infra/aws/terraform/modules/opal_name &amp;&amp; timeout 100 terraform init -backend=false -input=false -no-color &gt; /dev/null &amp;&amp; timeout 100 terraform test -no-color 2&gt;&amp;1 | tail -n 3</invocation><expect>Success! \d+ passed, 0 failed</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-23"><invocation>cd /c/dev/wk-firmbkts-45 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-45 --allow infra/aws/terraform/modules/opal_name/main.tf --allow lib/opal_naming.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~45/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/modules/opal_name/main.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 compares the base and tree over the real registry (both outputs identical), a Get+Put fixture (the Deny carries both
actions), a Put-only fixture (no Allow) and five refusals. AC2 is the module's own tests. AC3 is the write-surface bound.
Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-23.module-put-deny-only.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~45`.
Commit the file(s) and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W45-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 11 (msg 3927, three conditions: no PutObjectAcl; act 4b lands before the
04:30Z exec-summary run or act 2 waits a day; the `advisors/` writer census N=2). Act 4b's own cell (the exec-summary root's
narrow identity Allow at `advisors/*/exec_summary.json`, and its registry row) follows. Workstream `FENCEPUT`.
Class WORLD by the path floor, dormant.

<status>complete</status>
<round>4</round>
<workstream>FENCEPUT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-23</to_id>
<slot>~45</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
