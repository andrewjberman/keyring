# ADVI_FIRMBKTS task order -- `FB-g-1` -- AUTH-VALIDATOR-EDGE READS THE OWNERSHIP MAP AT THE CANONICAL KEY: THE DORMANT BUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~24</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository source and one test file only; no cron, rule, schedule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. Whether the function's role may read the new key is read at the act (the laptop identity), not here.
comp-adversary: RUN by the issuer -- at base the helper file does not exist, so `r4_validator.py` reads 0 of 4 and the new spec selects no test (AC1 and AC2 FAIL as expected); on a fixture implementation the check reads 4 of 4; AC3 reads FAIL at base because no path has changed (a control: it PASSES only for a change confined to the five allowed paths). Blindness: the check reads the helper in isolation; the `index.mjs` call site is read by text (K4), not run, because the function needs its dependencies and live S3.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-1` (round 4, enrichment item 1; PRD F6; the CTO's ADDENDUM 7 and the round-3 analysis section 3 item 1)

`infra/aws/lambda-edge/auth-validator-edge/index.mjs` loads the per-firm authorization map from S3 in `getOwnershipMap(firmId)`: the bucket comes from
`FIRM_BUCKET_MAP[firmId] || "opal-data-" + firmId`, the key is the literal template
`` `platinum/${firmId}/ownership_map.json` `` (line 174). When the producers' served platinum moves to the canonical home
(round 4's window), the producers write this object at `advi/49financial/platinum/49financial/ownership_map.json` in the
firm's own bucket, and a validator that still reads the legacy key reads a STALE authorization map (row D1-S17, armed).
You build the validator's reader DORMANT: for the registry as it stands the function reads exactly the key it reads today,
and nothing is deployed.

### 1a. Behavior (the whole spec)

1. **A new pure module** `infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs` (ES module, no imports) exporting exactly:
   - `CANONICAL_PLATINUM_BUCKETS`: `Object.freeze([])` -- the buckets whose served keys are the canonical layout. EMPTY by
     construction: nothing engages until the cutover names a bucket here (same convention and name as
     `infra/aws/lambda-edge/shared-advisor-router/index.mjs` line ~114, which you read and do not edit).
   - `OWNERSHIP_KEY_FIRMS`: `Object.freeze(["49financial"])` -- the firms whose ownership-map class the destination registry
     places (the registry row with `legacy_prefix` `platinum/49financial/`); every other firm keeps the legacy key.
   - `ownershipMapKey(firmId, bucket, canonical = CANONICAL_PLATINUM_BUCKETS, firms = OWNERSHIP_KEY_FIRMS)`: returns
     `` `advi/${firmId}/platinum/${firmId}/ownership_map.json` `` when `canonical.includes(bucket)` AND
     `firms.includes(firmId)`; otherwise `` `platinum/${firmId}/ownership_map.json` `` (the legacy key, byte for byte).
2. **`index.mjs`**: import `ownershipMapKey` from `./ownership_key.mjs`, and replace the literal `key` line in
   `getOwnershipMap` with `const key = ownershipMapKey(firmId, bucket);`. Change nothing else: the bucket line, the cache,
   the schema check and every log field stay as they are (the log's `key` field now carries whatever key was read).
3. **The spec** `infra/aws/lambda-edge/auth-validator-edge/test/ownership_key.spec.mjs` (`import { describe, test, expect } from "bun:test"`, importing only
   `../ownership_key.mjs`): (i) the shipped list is frozen and empty; (ii) with the shipped list, every one of
   `49financial`, `inflection`, `cottonwood` on bucket `opal-data-bd` and on its own `opal-data-<firm>` reads the legacy
   key; (iii) with `canonical = ["opal-data-49financial"]`, firm `49financial` on `opal-data-49financial` reads
   `advi/49financial/platinum/49financial/ownership_map.json`; (iv) the same firm on `opal-data-bd` (a bucket not
   named) reads the legacy key; (v) with `canonical = ["opal-data-inflection"]`, firm `inflection` still reads the
   legacy key (its class is not registered). A test that cannot fail is not a control: for each of (iii) and (iv) state in
   your report which one-line mutation of the helper makes it fail.

## 2. BOUNDS

1. Files that change: `infra/aws/lambda-edge/auth-validator-edge/index.mjs` (the import and the one `key` line), the new `ownership_key.mjs` and the new spec.
   No other file; no `package.json` edit; no dependency; no deploy; no AWS call.
2. Do not populate `CANONICAL_PLATINUM_BUCKETS`: engaging it is the act's, in the same deploy as the registry's value
   flip. Do not touch `tier_policy.mjs`, `aggregate_gate.mjs` or the router, guard or `_shared/firm-config.mjs`.
3. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/auth-validator-edge/index.mjs
infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs
infra/aws/lambda-edge/auth-validator-edge/test/ownership_key.spec.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~24/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~24/ADVI_FIRMBKTS.TO-FB-g-1.validator-ownership-key.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-1"><invocation>cd /c/dev/wk-firmbkts-24 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_validator.py --arms key --root /c/dev/wk-firmbkts-24; echo "exit=$?"</invocation><expect>ROUND 4 VALIDATOR KEY: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-1"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-24/infra/aws/lambda-edge/auth-validator-edge &amp;&amp; timeout 110 env -u FORCE_COLOR bun test test/ownership_key.spec.mjs 2&gt;&amp;1 | tail -n 6</invocation><expect>^\s*0 fail$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-1"><invocation>cd /c/dev/wk-firmbkts-24 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-24 --allow infra/aws/lambda-edge/auth-validator-edge/index.mjs --allow infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs --allow infra/aws/lambda-edge/auth-validator-edge/test/ownership_key.spec.mjs --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~24/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/lambda-edge/auth-validator-edge/index.mjs --require infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the helper's exports, its dormant and engaged keys (the engaged key is compared with the producers' seam's
own canonical destination for the same legacy key, read from the checkout), and the call site by text. AC2 is your spec.
AC3 is the write-surface bound (the control: it fails for any change outside the five allowed paths). Each invocation
terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-1.validator-ownership-key.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~24`. Commit the three files, then the instance second. **Do not flip this order's `<status>`**
(the issuer drains it). A row id on this project carries the dell1 infix and your slot:
`ADVI_FIRMBKTS-D1-W24-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs, the two
mutations of the control paragraph, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** class WORLD by path floor (a Lambda@Edge source), built dormant; the deploy is act 4's, by the laptop
identity (protected function), in the same act that names the bucket in this list and in the router's. The router and guard
were built dormant in round 3 (`FB-f-7`, `CANONICAL_PLATINUM_BUCKETS = []`); this cell gives the validator the same
shape so act 4's checklist is one list per function. Closes the validator half of row D1-S17 (the armed stale-map hazard)
once deployed; until then every protected or IRPT pair names it. The firm list is a mirror of one registry row; AC1's K3
arm re-reads the seam, so a registry row added later fails it rather than drifting.

<status>pending</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-1</to_id>
<slot>~24</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
