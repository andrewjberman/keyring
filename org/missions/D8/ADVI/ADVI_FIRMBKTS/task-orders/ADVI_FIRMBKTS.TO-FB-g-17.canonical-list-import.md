# ADVI_FIRMBKTS task order -- `FB-g-17` -- THE ROUTER AND THE VALIDATOR IMPORT THE GENERATED CANONICAL-BUCKET LIST: DORMANT, BYTE-IDENTICAL DECISIONS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-17</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~40</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository source and tests only; no cron, rule, schedule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_canonlist.py` reads 0 of 4 (the generated list is not yet imported; the router gate reads 51 pass 0 fail as the control the cell must keep). Blindness: the router gate and the validator spec read decisions on their own fixtures; the 193-event corpus is the CTO's round-2 instrument and is not re-run here.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-17` (round 4, workstream `CANONLIST`; the CTO's round-3 ADDENDA 4 and 7)

The edge router's dormant canonical-key path (`infra/aws/lambda-edge/shared-advisor-router/index.mjs`, `CANONICAL_PLATINUM_BUCKETS = Object.freeze([])`, ~line 114)
and the validator's helper (`infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs`, `CANONICAL_PLATINUM_BUCKETS = Object.freeze([])`) each hold a hand
list that the act's flip would have to EDIT with a bucket literal, which the enforcing naming gate refuses and which would
be a second statement of the cutover. The CTO's rule: the cutover is the registry's one value. The builder now renders
`export const CANONICAL_PLATINUM_BUCKETS` into `_shared/firm-config.mjs` (cell `FB-g-16`, merged: the sorted unique canonical
destination buckets of the platinum classes; today one, and no firm's CURRENT routed bucket is in it). You make both
consumers IMPORT that list instead of defining their own.

### 1a. Behavior (the whole spec)

1. **Router.** In `infra/aws/lambda-edge/shared-advisor-router/index.mjs` import `CANONICAL_PLATINUM_BUCKETS` from `../_shared/firm-config.mjs` (the file already
   imports from it) and delete the local `const CANONICAL_PLATINUM_BUCKETS = Object.freeze([]);` with its comment, keeping
   the explanatory comment's meaning in one updated sentence (the list is the registry's). Every other line stays. If the
   router's specs inject a list, keep that seam working (the handler already takes the map and list as arguments in the
   specs' shape; read `test/canonical-platinum.spec.mjs` first and make the smallest edit that keeps every spec's intent).
2. **Validator.** In `infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs` import the list from `../_shared/firm-config.mjs`, re-export it unchanged as
   `CANONICAL_PLATINUM_BUCKETS` and use it as the default of `ownershipMapKey`'s `canonical` parameter; define no list of
   your own. In `infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs` change test (i) from "the shipped list is frozen and empty" to "the list
   is the generated one: frozen, and none of the generated `FIRM_CONFIG` buckets is in it"; the other tests are unchanged.
3. **Dormant.** For the registry as it stands every decision of both functions equals base's: the generated list holds a
   canonical bucket and no routed bucket of any firm is in it, so the canonical path never engages.
4. Do NOT edit `_shared/firm-config.mjs` (generated), the guard, or any other file.

## 2. BOUNDS

1. Files that change: `infra/aws/lambda-edge/shared-advisor-router/index.mjs`, the router's spec file(s) only if a spec referenced the deleted local, `infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs`
   and `infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs`. No deploy, no AWS call, no dependency change.
2. No bucket, firm or key literal is typed in any file you write. If a commit is refused by the naming gate, do not
   override or force: file a BLOCKING row with the gate's lines.
3. ASCII only for your additions; the router and the validator may carry pre-existing non-ASCII comment bytes (row
   D1-W24-S2): leave them. LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/shared-advisor-router/index.mjs
infra/aws/lambda-edge/shared-advisor-router/test/
infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs
infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~40/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~40/ADVI_FIRMBKTS.TO-FB-g-17.canonical-list-import.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-17"><invocation>cd /c/dev/wk-firmbkts-40 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_canonlist.py --arms list --root /c/dev/wk-firmbkts-40; echo "exit=$?"</invocation><expect>ROUND 4 CANONICAL LIST: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-17"><invocation>cd /c/dev/wk-firmbkts-40 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_validator.py --arms key --root /c/dev/wk-firmbkts-40; echo "exit=$?"</invocation><expect>ROUND 4 VALIDATOR KEY: 4 of 4 arms</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-17"><invocation>cd /c/dev/wk-firmbkts-40 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-40 --allow infra/aws/lambda-edge/shared-advisor-router/index.mjs --allow infra/aws/lambda-edge/shared-advisor-router/test/ --allow infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs --allow infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~40/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/lambda-edge/shared-advisor-router/index.mjs --require infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the generated list, both imports, and the router's own gate (at least 51 pass, 0 fail) and the validator's spec
(0 fail). AC2 is a difference control: the validator's key check (dormant keys, engaged keys) must still read 4 of 4. AC3
is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-17.canonical-list-import.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~40`.
Commit the files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W40-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs,
the router's gate counts before and after, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** follows `FB-g-16` (the builder block). After this cell the act-4 flip is ONE registry value: the routed
alias marker; the regenerated `firm-config.mjs` and `loaders.py` carry the new routed bucket, which is in the list, so the
router, validator and IRPT ownership read engage the canonical keys together. The router and validator are protected
edge functions: their deploy is the laptop lane's, in act 4.

<status>complete</status>
<round>4</round>
<workstream>CANONLIST</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-17</to_id>
<slot>~40</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
