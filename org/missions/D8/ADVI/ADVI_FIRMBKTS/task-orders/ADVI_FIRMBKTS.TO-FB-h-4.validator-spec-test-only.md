# ADVI_FIRMBKTS task order -- `FB-h-4` -- THE VALIDATOR'S OWNERSHIP-KEY SPEC FOLLOWS THE FLIP (ONE STALE ASSERTION, TEST-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~64</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test file only; no cron, rule, schedule or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a test file only: no AWS act, no grant.
comp-adversary: RUN by the issuer -- at the base the suite reads 5 pass 1 fail (the one assertion above) and the mutant arm reads fail=0 (the old test passes on an emptied list: FAIL as expected). Blindness: unit tests prove the key helper and the generated block, not the deployed validator.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-h-4` (round 5, enrichment item 3; row `D1-C-S33`)

The validator's own spec `infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs` was written when no bucket was engaged: test (i) asserts that
NONE of the generated `FIRM_CONFIG` buckets is in `CANONICAL_PLATINUM_BUCKETS`. The cutover put `opal-data-49financial` in
that list (`_shared/firm-config.mjs`, the GENERATED block, which names exactly that one bucket), so the test reads `true` where
it expects `false`: the suite is 5 pass, 1 fail at HEAD, and a build gate that runs it refuses the next validator build.
The product is correct; the expectation is stale. You update the expectation and nothing else.

### 1a. The edit (one file: `infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs`)

1. Test (i) becomes (rename it to say what it now asserts): the list is the generated one (`toBe(GENERATED)`), it is frozen,
   it contains the bucket of the `49financial` scope (`FIRM_CONFIG["49financial"].bucket`), and it contains NO other
   `FIRM_CONFIG` bucket (every other firm's bucket is `false`).
2. Add ONE test in the "engaged bucket" group: with the shipped list, `ownershipMapKey("49financial", FIRM_CONFIG["49financial"].bucket)`
   equals `OWNERSHIP_KEYS["49financial"].canonical`, and `ownershipMapKey("49financial", "opal-data-bd")` equals
   `OWNERSHIP_KEYS["49financial"].legacy`. Both keys are read from the generated block, never typed.
3. Tests (ii) to (vi) stay as they are (they pass at HEAD).

### 1b. Rules

1. Edit only the spec file. No product file, no registry, no generated block. ASCII only.
2. MUTANT CONTROL: run `python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py mutant --root /c/dev/wk-firmbkts-64`; it copies the
   validator's key helper, your spec and `firm-config.mjs` into a temporary directory, EMPTIES the generated list there, and
   runs the suite: it must print `MUTANT: the spec FAILS as expected`. (At the base it does not: the old test (i) passes on
   an empty list. That is the point.) The temporary copy is deleted; your worktree is not touched.
3. If a module will not resolve, run `bun install --frozen-lockfile` in `infra/aws/lambda-edge/auth-validator-edge` (writes untracked `node_modules`; commit none).

## 2. BOUNDS

1. One commit of the spec file only; everything else is read-only. No deploy, no push.
2. If a failing assertion is NOT test (i), or a handler's output looks wrong rather than an expectation, STOP before editing and file a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~64/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~64/ADVI_FIRMBKTS.TO-FB-h-4.validator-spec-test-only.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-4"><invocation>cd /c/dev/wk-firmbkts-64/infra/aws/lambda-edge/auth-validator-edge &amp;&amp; PATH="$PATH:$HOME/.bun/bin" timeout 110 bun test tests/ 2&gt;&amp;1 | sed "s/\x1b\[[0-9;]*m//g" | grep -E "^ *[0-9]+ (pass|fail)$" | tr "\n" " "</invocation><expect>^ *[0-9]+ pass +0 fail *$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-h-4"><invocation>PATH="$PATH:$HOME/.bun/bin" timeout 110 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py mutant --root /c/dev/wk-firmbkts-64 2&gt;&amp;1 | tail -1</invocation><expect>^MUTANT: the spec FAILS as expected with the list emptied \([1-9][0-9]* fail\)$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-h-4"><invocation>cd /c/dev/wk-firmbkts-64 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-64 --allow infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~64/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the suite's own count (pass count not fixed: one test is added), AC2 the mutant control, AC3 the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~64/ADVI_FIRMBKTS.TO-FB-h-4.validator-spec-test-only.proof_of_spec.json`. Commit the spec edit FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W64-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** row `D1-C-S33` (the CVO; the CTO's round-4 analysis section 2): test-only, as `FB-g-37` did for the router and the guard. Class WORLD by the path floor (an infrastructure path), though the cell writes a test file only. The deployed validator v23 is unaffected.

<status>pending</status>
<round>5</round>
<workstream>VALIDATOR</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-4</to_id>
<slot>~64</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
