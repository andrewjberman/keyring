# AMGT_RESAPP task order -- `AMGT-ee-1` -- THE SECURITY ROUTE RESOLVES A TYPED NAME OR TICKER: ONE CANDIDATE SERVES, SEVERAL LIST, NONE IS NOT FOUND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ee-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~318</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one branch and one test.
comp-iam: DECLARED-NOT-APPLICABLE -- the resolver reads what /resolve already reads; no grant.
comp-adversary: RUN at the cut (round81_prep/GROUP_ROUTE_NOTES.md @2a2b247b7c) -- on the live function /security/AMD/thesis, 'Advanced Micro Devices', 'ABNB', 'Microsoft' and 'Micro' all 404 while name_search.resolve_query gives one candidate for the first four and three for 'Micro'. AC1 FAILs at the base, AC2 PASSes.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-318`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ee-1` (round 81, decomposition s.89)

A person types a ticker (`AMD`) or a company name (`Advanced Micro Devices`) where the page asks for a security. Today the
per-security routes (`/security/<typed>/...` in `lib/research/api/scoped_amgt.py`) answer 404 "no security matches ..." for
anything that is not already a stored form (the 404 branch near `:6978-7002`; identity via `resolve_identity`, `:3102`). The estate
already has the resolver: `lib/research/api/name_search.py` `resolve_query`, served at `GET /resolve?q=` (`scoped_amgt.py:7076`),
answering `exact`, `candidates` or `none`. The ruling: one candidate resolves, several return the list, none keeps the 404; no
coverage gate.

Read `scoped_amgt.py` around the per-security arm and its 404 branch, and `name_search.py` whole, first.

1. ONLY at the existing 404 branch of the per-security arm: call `name_search.resolve_query(<the typed string>)`, imported at
   FUNCTION scope as `:7076` already does.
2. `exact`, or `candidates` with exactly ONE match: resolve the identity again with that match's `security_key` and serve the
   route exactly as for that key. `identity.requested` keeps the typed text.
3. `candidates` with TWO or more: answer 404 with the plain sentence `<n> companies match '<typed>'; type the ticker.` and a
   `candidates` list beside it, each entry the match's `security_key` and name as `resolve_query` gives them. Never pick one.
4. `none`: today's 404 sentence and body, unchanged.
5. A string that resolves today never reaches the branch: its body stays byte for byte as today. The timeline arm is not moved.
6. New test `lib/research/api/tests/test_route_typed_name.py`: the three arms (one, several, none) on plants, plus an exact key
   that never reaches the branch.

Run `lib/research/api/tests/` before your commit and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W318-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `scoped_amgt.py` at the 404 branch only, and add the one test file.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_route_typed_name.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~318/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ee-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_route.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a typed ticker and a typed name serve the canonical key's page, 'Micro' answers 404 saying several companies match with the candidates, an unknown string keeps today's 404; C1-C4 PASS; R81 ROUTE AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ee-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_route.py" --crit AC2; echo "exit=$?"</invocation><expect>an exact key's /thesis body on the tree hashes equal to the deployed function's, 4 of 4; R81 ROUTE AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~318 <0.9.0_WK_AMGT_RESAPP~318@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~318/AMGT_RESAPP.TO-AMGT-ee-1.the-security-route-resolves-a-typed-name.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.
- the hookup the redeploy must carry (the function-scope import), or that none is needed.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-80 analysis @6d8d699c09 R3 / enrichment item 2; ruling @9e03417c14. Grounded round81_prep/GROUP_ROUTE_NOTES.md @2a2b247b7c. Checks dry-run at the base: AC1 base: FAIL as expected (C1, C2, C4 FAIL); AC2 base: PASS as expected (4 of 4, with PYTHONPATH set). Served only through AMGT-ee-6.

<status>pending</status>
<round>81</round>
<slot>0.9.0_WK_AMGT_RESAPP~318</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @21f7c2bee9 (build 67e51346c2, proof b9fd63cbba VALID rc=0; mutant control with resolve_query forced to none fails C1, C2, C4). Re-run by the issuer on the branch: R81 ROUTE AC1 SERVED: YES (AMD and "Advanced Micro Devices" serve AMD_US_Equity; "Micro" 404 "3 companies match ..."; "zzqx" keeps the 404), AC2 YES 4 of 4. Merged-tree suites (api, freshness, lists): 941 passed, 2 failed (pypdf absent on dell1). ISSUER RULING on the worker's finding: an UNREADABLE name list answers 500 with /resolve's own sentence (not a 404): it is not a "none" answer, and the route mirrors /resolve. Served only through AMGT-ee-6.</status>
