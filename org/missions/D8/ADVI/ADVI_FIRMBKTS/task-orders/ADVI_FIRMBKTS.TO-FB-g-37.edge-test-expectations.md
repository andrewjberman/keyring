# ADVI_FIRMBKTS task order -- `FB-g-37` -- ACT 4: THE ROUTER AND GUARD TEST EXPECTATIONS FOLLOW THE FLIP (12 STALE ASSERTIONS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-37</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~60</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- test files only; no cron, rule, schedule or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- test files only: no AWS act, no grant.
comp-adversary: RUN by the issuer -- at the base (the merged flip commit's descendant) the router gate reads 42 pass 9 fail and the response guard 43 pass 3 fail; the nine and the three are the 12 assertions below, every one of which expects the 49financial scope's bucket to be `opal-data-bd` or its key under `/gold/...`. Blindness: unit tests prove the handlers' routing logic, not a deployed edge.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-37` (round 4, workstream `EDGETESTS`; the edge legs' build gates)

The act-4 flip commit moves the 49financial scope's routed bucket from `opal-data-bd` to `opal-data-49financial`, and its served
keys to `advi/49financial/platinum/...`. The two edge functions' own build gates (`bun run test`) therefore fail on 12
assertions that still expect the OLD bucket pair. The handlers are CORRECT (the issuer probed them); the expectations are stale.
You update the 12 expectations, and add nothing else. You do not touch any non-test file.

### 1a. The 12 assertions (run each suite first to see them)

Router: `cd infra/aws/lambda-edge/shared-advisor-router && bun run test` reads 42 pass, 9 fail. The failing tests, by name:
1. `FB-e-6 -- canonical platinum key path (dormant) > the fixture finds a legacy firm, its alias and another firm in the registry's own view`
   (`test/canonical-platinum.spec.mjs`): the fixture looks for a firm whose alias is still ROUTED; none is after the flip. Make the
   fixture find the firm and alias by the registry's CURRENT state (a scope with an alias, whichever is routed or not), keeping its purpose.
2. `... > a listed bucket: platinum passes to advi/{firm}/platinum/, the alias resolves to the same scope` (same file): expected values follow
   the flipped scope: the 49financial scope's bucket is `opal-data-49financial` and its alias `opal-data-bd` no longer carries the route.
3. `ADVI_FIRMSEP.04 > X-Firm-Id '49financial' routes to opal-data-bd` (`test/firm-routing.spec.mjs`): now routes to `opal-data-49financial`
   (rename the test to say so).
4. `... > X-Firm-Id 'mockadv' routes to opal-data-bd (test-account passthrough)`: `mockadv` is an alias of the 49financial scope
   and follows its bucket: `opal-data-49financial` (rename).
5. `... > PATH-CLASS SCOPING: platinum/firm/ still routes to the FIRM_CONFIG bucket`: the FIRM_CONFIG bucket of 49financial is now
   `opal-data-49financial`; the test's point (the advi path class is scoped, other classes keep the firm's configured bucket) is unchanged.
6. `... > TRAILING-SLASH CONTROL: platinum/advisors/{id}/book.json is NOT captured by the advi path class`: same, expect
   `opal-data-49financial`.
7. `... > opal-capital staff with ?firm=bd may read platinum/advi/49financial/`: after the flip the staff slug for 49financial is
   `49financial` (bucket `opal-data-49financial`): `?firm=bd` entitles NO 49financial tenant and the request is REFUSED by the
   p4r3_tenant_assert rule (the issuer's probe: status 401). Change this test to use `firm=49financial` and expect `opal-data-portal-v2`,
   and ADD one test asserting that `?firm=bd` for `platinum/advi/49financial/` is refused (status "401", the handler's refusal).
8. `POSN_TENANCY.TO-4-AE > routes 49financial to ITS bucket -- same path, DIFFERENT origin` and
9. `... > ADDITIVE: the advisor-intelligence rewrite is untouched` (`test/satellites-registry.spec.mjs`): 49financial's origin is
   `opal-data-49financial`; expected values follow.
Response guard: `cd infra/aws/lambda-edge/shared-advisor-router-response && bun run test` reads 43 pass, 3 fail (`test/firm-isolation-guard.spec.mjs`):
10. `49financial served from opal-data-bd passes through (success path keeps CDNCOHT cache-control)`: serve it from `opal-data-49financial`.
11. `P4R-3: opal-capital staff with ?firm=bd reading advi/49financial from portal-v2 passes`: use `?firm=49financial`.
12. `does NOT publish an alert when firm/bucket match (no false pages)`: the matching pair for 49financial is `opal-data-49financial`.
ALSO ADD ONE assertion to the guard suite: `49financial served from opal-data-bd` now reads as a MISMATCH (the same response the suite
asserts for any other firm's mismatched bucket), so the guard still discriminates after the flip.

### 1b. Rules

1. Edit only the test files named in section 3. No product file, no registry, no source map. ASCII only.
2. Each edited test keeps its name's intent; where its name states the old bucket, rename it to the new one.
3. MUTANT CONTROL (record the outputs in your report): with the product file untouched, temporarily make the router resolve
   `49financial` to `opal-data-bd` (a one-line local edit in `infra/aws/lambda-edge/shared-advisor-router/index.mjs`, reverted before you commit) and show the router suite
   FAILS on the updated tests (at least tests 3 and 5); revert and show it passes. Never commit the mutant.
4. If a module will not resolve when running a suite in your worktree, run `bun install --frozen-lockfile` in that directory
   (it writes untracked `node_modules`; commit none).

## 2. BOUNDS

1. One commit of test files only; the product files are read-only. No deploy, no push.
2. If a failing assertion is NOT one of the 12 above, or a handler's output looks wrong rather than the expectation, STOP before
   editing it and file a BLOCKING row naming the test, expected and received.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/shared-advisor-router/test/canonical-platinum.spec.mjs
infra/aws/lambda-edge/shared-advisor-router/test/firm-routing.spec.mjs
infra/aws/lambda-edge/shared-advisor-router/test/satellites-registry.spec.mjs
infra/aws/lambda-edge/shared-advisor-router/test/tenant-grain.spec.mjs
infra/aws/lambda-edge/shared-advisor-router-response/test/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~60/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, `infra/aws/lambda-edge/shared-advisor-router/index.mjs`, `infra/aws/lambda-edge/shared-advisor-router-response/index.mjs`, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~60/ADVI_FIRMBKTS.TO-FB-g-37.edge-test-expectations.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-37"><invocation>cd /c/dev/wk-firmbkts-60/infra/aws/lambda-edge/shared-advisor-router &amp;&amp; timeout 110 bun test test/ 2&gt;&amp;1 | sed "s/\x1b\[[0-9;]*m//g" | grep -E "^ *[0-9]+ (pass|fail)$" | tr "\n" " "</invocation><expect>^ *[0-9]+ pass +0 fail *$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-37"><invocation>cd /c/dev/wk-firmbkts-60/infra/aws/lambda-edge/shared-advisor-router-response &amp;&amp; timeout 110 bun test test/ 2&gt;&amp;1 | sed "s/\x1b\[[0-9;]*m//g" | grep -E "^ *[0-9]+ (pass|fail)$" | tr "\n" " "</invocation><expect>^ *[0-9]+ pass +0 fail *$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-37"><invocation>cd /c/dev/wk-firmbkts-60 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-60 --allow infra/aws/lambda-edge/shared-advisor-router/test/canonical-platinum.spec.mjs --allow infra/aws/lambda-edge/shared-advisor-router/test/firm-routing.spec.mjs --allow infra/aws/lambda-edge/shared-advisor-router/test/satellites-registry.spec.mjs --allow infra/aws/lambda-edge/shared-advisor-router/test/tenant-grain.spec.mjs --allow infra/aws/lambda-edge/shared-advisor-router-response/test/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~60/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the router gate, AC2 the response guard gate (a pass count not fixed: the guard gains one test and the router one),
AC3 the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-37.edge-test-expectations.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~60`. Commit
the test edits FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_FIRMBKTS-D1-W60-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs, the mutant
control's failing test names, the list of the 12 edits (test name and old to new value) and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on `0.7.0_AE_CloudOps~FBL`'s BLOCKING row `ADVI_FIRMBKTS-S21` (commit 79f3302251, laptop): the router gate
reads 42/9 and the guard 43/3 at the flip commit; at the flip's parent 51/0 and 46/0. The handlers were probed by the issuer:
partner 49financial routes to the canonical bucket and key; staff `?firm=49financial` routes canonical; staff `?firm=bd` is REFUSED for
`platinum/advi/49financial/` and reads the frozen legacy bucket for other classes (the portal's `ROUTER_FIRM_SUFFIX` still maps
`49financial` to `bd`: a portal follow-up, not this order). Workstream `EDGETESTS`. Class WORLD by the path floor (an infrastructure path), though the cell writes test files only.

<status>complete</status>
<round>4</round>
<workstream>EDGETESTS</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-37</to_id>
<slot>~60</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
