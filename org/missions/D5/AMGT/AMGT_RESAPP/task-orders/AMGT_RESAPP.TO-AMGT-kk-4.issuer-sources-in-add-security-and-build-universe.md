# AMGT_RESAPP task order -- `AMGT-kk-4` -- A RECORD ADDED BY ADD_SECURITY OR BUILD_UNIVERSE CARRIES ITS MEASURED ISSUER CIK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-kk-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~344</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no store write; tests stub the sources.
comp-adversary: RUN at the cut -- row W340-S2: add_security.py and build_universe.py build without load_issuer_sources(), so a record they add carries no issuer until a crosswalk CLI build. build_universe is packaged with the live function (row D1-S13) but inert on every request path; this cell must not add a request-path call.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-344`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-kk-4` (round 86, decomposition s.94)

CTO~DELL1 round-85 analysis R3. `lib/research/identity/add_security.py` and `build_universe.py` pass `crosswalk.load_issuer_sources()`
into the build they call, so a record they add carries `issuer.cik` when one is measurable (same precedence as the CLI). Code only,
no publish. Keep the import function-scope (row D1-S13: no module-scope import, nothing on a request path). Tests in
`lib/research/identity/tests/test_writers_carry_issuer.py` with the sources stubbed offline.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W344-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit the two writers and the new test file only.

## 3. SURFACES

<paths>
lib/research/identity/add_security.py
lib/research/identity/build_universe.py
lib/research/identity/tests/test_writers_carry_issuer.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~344/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-kk-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/identity/tests/test_writers_carry_issuer.py -q; echo "exit=$?"</invocation><expect>every test passes: a record added by each writer carries issuer.cik from a stubbed measured source, and none when no source measures it; 0 failed; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-kk-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="/c/tmp/stubfitz;$(pwd)" py -3.12 -m pytest lib/research/identity -q; echo "exit=$?"</invocation><expect>the identity folder passes with 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~344 <0.9.0_WK_AMGT_RESAPP~344@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~344/AMGT_RESAPP.TO-AMGT-kk-4.issuer-sources-in-add-security-and-build-universe.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the import scope you used (function-scope);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-85 analysis R3 (row W340-S2). Code only; reaches the live function's package at the next redeploy (inert). Checks dry-run at the base: AC1 base FAIL (no test file); AC2 base PASS (a bound).

<status>pending</status>
<round>86</round>
<slot>0.9.0_WK_AMGT_RESAPP~344</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
