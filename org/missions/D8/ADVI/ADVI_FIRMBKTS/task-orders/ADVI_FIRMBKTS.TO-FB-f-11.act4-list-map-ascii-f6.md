# ADVI_FIRMBKTS task order -- `FB-f-11` -- WINDOW ACT 4: THE LIST ENTRY, THE MAP VALUE, THE ALL-ASCII ROUTER AND THE F6 DEPLOY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~18</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>BEFORE_AFTER_PAGE_CHECK, STAFF_PROXY_CHECK, ROUTER_VERSION_4, ROUTER_SHA256_4</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- iam:SimulatePrincipalPolicy on user/cloudops-dell1-agent-user reads allowed for lambda:PublishVersion, lambda:UpdateFunctionCode, lambda:GetFunctionConfiguration, cloudfront:GetDistributionConfig and cloudfront:UpdateDistribution (5 of 5, resource *); the role the Terraform apply runs under is read by the amendment. No grant is created. The CloudFront serving grant on `advi/49financial/platinum/*` of the new bucket is read from the live bucket policy at the amendment.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a version, a hash, a second manifest) or a check the amendment writes; at the cut each reads FAIL by construction. The amendment writes each scripted check, dry-runs it at the base and tests it against a mutant BEFORE the GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S AMENDMENT SAYS SO.

Un-park conditions, all required, each read from a file at HEAD:
1. Acts 1, 2 and 3 (`FB-f-8`, `FB-f-9`, `FB-f-10`) are `complete`, and act 3's `compare` read `DEST-VS-MANIFEST: EQUAL`
   after act 2 and within the same window (no producer write to the old home since: act 2's `OLD HOME` read).
2. The never-widen pair for this act reads SIGNED in both halves
   (`ledger/NEVER_WIDEN_ROUND3_ACT4_CUTOVER_COO_HALF.md`, `..._CTO_HALF.md`): it names every served key and class that
   moves, the activation as BOTH gates (the list entry AND the map value), the staff proxy's requests read before and
   after (row D1-S7), and the rollback (the previous router version re-associated; the old home untouched).
3. The actor's change-management entry is OPEN and committed first.
4. The amendment commit fills the placeholders' meaning (section 4), names the executor and the window time, and sets
   `<status>pending</status>`.

## 1. THE CELL -- `FB-f-11` (round 3, enrichment item 1, step 4; PRD F6 and F7; rows D1-S4, D1-S7, D1-S9, D1-W9-S1)

One act, one never-widen pair, in this order:
1. **All-ASCII.** Replace the 5 pre-existing non-ASCII comment lines of
   `infra/aws/lambda-edge/shared-advisor-router/index.mjs` with ASCII (CLAUDE.md section 4: "all non-ASCII out", the first
   safe move). Close: the built file reads 0 bytes above 127 (the amendment adds the criterion that counts them).
2. **The list entry.** Add `opal-data-49financial` to `CANONICAL_PLATINUM_BUCKETS` (`index.mjs:128`, `Object.freeze([])`
   today). It is generated or typed by the rule the build's naming gate allows; the build proves it (section 4).
3. **The map value.** Move the 49 Financial value of `FIRM_BUCKET_MAP` (the registry's `scopes.json` row, regenerated into
   `_shared/firm-config.mjs`) from `opal-data-bd` to `opal-data-49financial`. `mockadv` stays on `opal-data-bd`; its
   access to the 49 Financial tenant directory is the declared alias from act 1.
4. **The F6 deploy**, through Terraform and `safe-apply` as act 1 did (build, artifact, plan JSON read for the
   association, apply, read back each behavior's version and `CodeSha256`).
5. **The window's read** (the CTO's analysis item 1): through the page's own route, a firm session and the staff proxy
   read byte-identical pages before and after; every served key answers from `opal-data-49financial`; nothing writes the
   old platinum keys after act 2; the old bucket is untouched through the rollback window.

## 2. BOUNDS

1. Only the router's source, the registry value and its generated block, the Terraform apply of the router (and the guard
   if its generated block changed), and the ledger change. No other function, grant, schedule or bucket changes.
2. The old home is read-only for this act. No delete, ever, in this window.
3. If the before-read and after-read differ on any served key, the rollback in the pair runs at once and the order stays
   open with a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/shared-advisor-router/index.mjs
infra/aws/lambda-edge/_shared/firm-config.mjs
infra/logic/registry/scopes.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~18/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~18/ADVI_FIRMBKTS.TO-FB-f-11.act4-list-map-ascii-f6.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-11"><invocation><BEFORE_AFTER_PAGE_CHECK></invocation><expect>PAGES: every served key identical before and after, 0 differ</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-11"><invocation><STAFF_PROXY_CHECK></invocation><expect>STAFF PROXY: requests identical before and after, 0 differ</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-11"><invocation>.tools/aws lambda get-function-configuration --function-name shared-advisor-router --qualifier <ROUTER_VERSION_4> --region us-east-1 --query CodeSha256 --output text</invocation><expect><ROUTER_SHA256_4></expect></criterion>
</proof_of_spec>

A fourth arm is the build's own: the router's gate, the difference control and the naming gate pass on the edited source
before the deploy (the amendment adds them as criteria with their counts). Placeholders: `BEFORE_AFTER_PAGE_CHECK` and
`STAFF_PROXY_CHECK` are issuer-written, dry-run checks that make the before and after reads through the page's route
(they need the sessions of act 1's `ROUTE_FETCH_CHECK`); `ROUTER_VERSION_4` and `ROUTER_SHA256_4` are read back at the
apply.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance; report once:
the pair's two blob ids, the diff of the router, the plan summary, the live association per behavior, the before/after
reads, the three outputs, the post-apply plan line, the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged, class WORLD. This is the act the CTO's round-2 analysis item 1 names last; it is the first act
in this project that changes what a user's request reads. It takes slot `~18`: the three other staged acts ride the
queues of `~11`, `~16` and `~17`. The deploy mechanics mirror act 1; the amendment states both in one place so the
actor's pair can quote it.

<status>staged</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-11</to_id>
<slot>~18</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
