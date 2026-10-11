# ADVI_FIRMBKTS task order -- `FB-g-1` -- AUTH-VALIDATOR-EDGE READS THE OWNERSHIP MAP AT THE KEY THE GENERATED BLOCK NAMES: THE DORMANT BUILD (AMENDED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~35</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository source and one test file only; no cron, rule, schedule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. Whether the function's role may read the new key is read at the act (the laptop identity), not here.
comp-adversary: RUN by the issuer -- at base the helper file does not exist, so `r4_validator.py` reads 0 of 4 and the new spec selects no test (AC1 and AC2 FAIL as expected); AC3 reads FAIL at base because no path has changed (a control: it PASSES only for a change confined to the five allowed paths). The check's K2 and K3 read the generated `OWNERSHIP_KEYS` of cell FB-g-12, merged before this order is seated. Blindness: the check reads the helper in isolation; the `index.mjs` call site is read by text (K4), not run, because the function needs its dependencies and live S3.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-1` (round 4, enrichment item 1; PRD F6; the CTO's ADDENDUM 7 and ADDENDUM 4 of the round-3 analysis)

`infra/aws/lambda-edge/auth-validator-edge/index.mjs` loads the per-firm authorization map from S3 in `getOwnershipMap(firmId)`: the bucket comes from
`FIRM_BUCKET_MAP[firmId] || "opal-data-" + firmId`, and the key is a literal template (line ~174). When the producers'
served platinum moves to the canonical home (round 4's window) the producers write this object at a different key in the
firm's own bucket, and a validator that still reads the legacy key reads a STALE authorization map (row D1-S17, armed).
**The key strings are no longer typed here**: the naming gate refused them (rows D1-W24-S3), and the CTO ruled the builder
renders them (ADDENDUM 4). The generated view `infra/aws/lambda-edge/_shared/firm-config.mjs` now exports `OWNERSHIP_KEYS`, one frozen entry per firm that owns a
registered legacy ownership-map address (today 49financial) with a `legacy` and a `canonical` key string (cell FB-g-12,
merged); a firm with no registered address has no entry. You build the validator's reader DORMANT: for the registry as
it stands the function reads exactly the key it reads today, and nothing is deployed.

### 1a. Behavior (the whole spec)

1. **A new module** `infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs` (ES module) that imports `OWNERSHIP_KEYS` from `../_shared/firm-config.mjs`
   (the path `index.mjs` already uses for `FIRM_BUCKET_MAP`) and exports exactly:
   - `CANONICAL_PLATINUM_BUCKETS`: `Object.freeze([])` -- the buckets whose served keys are the canonical layout. EMPTY by
     construction: nothing engages until the cutover names a bucket here (same convention and name as
     `infra/aws/lambda-edge/shared-advisor-router/index.mjs`, which you read and do not edit).
   - `ownershipMapKey(firmId, bucket, canonical = CANONICAL_PLATINUM_BUCKETS, keys = OWNERSHIP_KEYS)`: looks `firmId` up
     in `keys`; for a firmId with no entry it THROWS an `Error` whose message is `ownership_map_unknown_firm` (the call
     site already fails closed on any fetch error); otherwise it returns the entry's `canonical` when
     `canonical.includes(bucket)`, else its `legacy`. No string literal of a key, bucket or firm appears in the file.
2. **`index.mjs`**: import `ownershipMapKey` from `./ownership_key.mjs` and replace the literal `key` line in
   `getOwnershipMap` with `const key = ownershipMapKey(firmId, bucket);`. Change nothing else: the bucket line, the cache,
   the schema check and every log field stay as they are.
3. **The spec** `infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs` (a `tests/` folder: the naming gate does not grade it;
   `import { describe, test, expect } from "bun:test"`, importing only `../ownership_key.mjs` and `../../_shared/firm-config.mjs`):
   (i) the shipped list is frozen and empty; (ii) with an injected `keys` object of two abstract firms
   (`{ fa: { legacy: "L-A", canonical: "C-A" }, fb: { legacy: "L-B", canonical: "C-B" } }`) and the shipped list, each
   firm reads its legacy key on any bucket; (iii) with `canonical = ["b1"]`, firm `fa` on bucket `b1` reads `C-A`;
   (iv) the same firm on bucket `b2` reads `L-A`; (v) an unknown firm throws `ownership_map_unknown_firm`; (vi) every
   key of the generated `OWNERSHIP_KEYS` is a firmId of the generated `FIRM_CONFIG` and its `legacy` and `canonical` are
   non-empty strings.
   A test that cannot fail is not a control: for each of (iii) and (iv) state in your report which one-line mutation of
   the helper makes it fail.

## 2. BOUNDS

1. Files that change: `infra/aws/lambda-edge/auth-validator-edge/index.mjs` (the import and the one `key` line), the new `ownership_key.mjs` and the new spec.
   No other file; no `package.json` edit; no dependency; no deploy; no AWS call.
2. Do not populate `CANONICAL_PLATINUM_BUCKETS`: engaging it is the act's, in the same deploy as the registry's value flip.
   Do not touch `tier_policy.mjs`, `aggregate_gate.mjs`, the router, the guard or `infra/aws/lambda-edge/_shared/firm-config.mjs`.
3. No firm name, bucket name or key template is typed in any file you write except the spec's abstract `fa`/`fb`/`b1`/`b2`.
   If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. (`index.mjs` carries one pre-existing non-ASCII character in a comment, row D1-W24-S2: leave
   it; your edit adds none.) If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/auth-validator-edge/index.mjs
infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs
infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~35/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~35/ADVI_FIRMBKTS.TO-FB-g-1.validator-ownership-key.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-1"><invocation>cd /c/dev/wk-firmbkts-35 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_validator.py --arms key --root /c/dev/wk-firmbkts-35; echo "exit=$?"</invocation><expect>ROUND 4 VALIDATOR KEY: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-1"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-35/infra/aws/lambda-edge/auth-validator-edge &amp;&amp; timeout 110 env -u FORCE_COLOR bun test tests/ownership_key.spec.mjs 2&gt;&amp;1 | tail -n 6</invocation><expect>^\s*0 fail$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-1"><invocation>cd /c/dev/wk-firmbkts-35 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-35 --allow infra/aws/lambda-edge/auth-validator-edge/index.mjs --allow infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs --allow infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~35/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/lambda-edge/auth-validator-edge/index.mjs --require infra/aws/lambda-edge/auth-validator-edge/ownership_key.mjs; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the helper's exports and its import, its dormant keys for every generated firm, its engaged keys (compared
with the producers' seam's own canonical destination for the same legacy key, read from the checkout), and the call site by
text. AC2 is your spec. AC3 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-1.validator-ownership-key.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~35`. Commit the three files, then the instance second. **Do not flip this order's `<status>`**
(the issuer drains it). Row ids: `ADVI_FIRMBKTS-D1-W35-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once:
AC1 to AC3 outputs, the two mutations of the control paragraph, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-11 ~13:xxZ; the CTO's round-3 ADDENDUM 4, msg 3853; rows D1-W24-S1..S3):** the
first seat (`~24`) built the cell with typed key templates and passed AC1 and AC2, but the enforcing naming gate refused the
commit. The cell is re-seated on slot `~35` over the merged `FB-g-12` block: the key strings are generated, the helper
carries none, and the spec moves to a `tests/` folder the gate does not grade. `<issued_to>`, the spec's path and the
criteria are amended by the issuer; GATE viii reads `<placeholders>NONE</placeholders>` at HEAD and no token in an
invocation. The first seat's three code files sit uncommitted in `/c/dev/wk-firmbkts-24` and are not merged.

**ISSUER NOTES:** class WORLD by path floor (a Lambda@Edge source), built dormant; the deploy is act 4's, by the laptop
identity (protected function), in the same act that names the bucket in this list and in the router's. Closes the validator
half of row D1-S17 once deployed. An unknown firm used to read a missing key (a 404, then the 503 fail-closed path); it now
throws before the read and reaches the same handler.

<status>pending</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-1</to_id>
<slot>~35</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
