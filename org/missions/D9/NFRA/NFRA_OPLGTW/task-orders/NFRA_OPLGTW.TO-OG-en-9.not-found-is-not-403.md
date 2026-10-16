# NFRA_OPLGTW task order -- `OG-en-9` -- a key that does not resolve answers not-found, an authorization refusal answers 403, with a test of both arms (round 38 E9; row Z-S175; CTO round-37 analysis update msg 34989)

<!-- ===================== RECORD FACE BELOW; THE WORKER FACE IS EVERYTHING UP TO THE RECORD FACE MARKER ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-9</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-9</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~123</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no admission class moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's update to the round-37 analysis (`ledger/ROUND_ANALYSIS.round37.md` @9dbe9546bc: "Add E9 (Z-S175): a missing key answers not-found, a denied one 403, with a test covering both arms") on the CVO's row Z-S175.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-9` (decomposition addendum R3-T.94, round 38 item E9, workstream ENRICH-R38-B, FWD-22)

THE DEFECT (row Z-S175, measured by the Bloomberg seat on the live gateway). `gateway_query_catalog(key='mp.01.aum-metrics')` answered `{"error": "off-catalog: no W5 row for this key -- not resolvable (...)", "key": "...", "http_status": 403}` WITHOUT `guard_denied`, while `opal_describe` on the same key reads `catalogued: true` and `servable: true` to the same principal. A caller reads 403 as "still denied" where the class is "not found". The seat nearly reported a false DENIED.

THE RULE. A refusal's status code names its CLASS: an authorization refusal is the entitlement chokepoint's shape (`guard_denied`, code `entitlement_denied`, HTTP 403); a key that does not resolve (no catalog row, an unknown key) is a not-found or bad-argument class (HTTP 404, or 400 for a malformed key) and carries NO `guard_denied`.

WHERE (read before editing): the verdict that says "off-catalog: no W5 row for this key -- not resolvable" is `GateVerdict(False, ...)` in `app/graphql_plumbing/catalog_gate.py` (about line 88); the tool `gateway_query_catalog` and its HTTP shaping live in `app/integrations/portal_index/integration.py` (about line 431 appends `http_status` from the upstream response) and the code that maps a gate verdict to a status (find it by reading how `GateVerdict` is consumed). Trace exactly how a no-row verdict becomes 403 today.

FIX (code only): make an UNRESOLVABLE key answer `http_status` 404 (a malformed key 400) with an error that says "not found" in words and carries no `guard_denied`, while a key that resolves but the principal may not read keeps 403 with the entitlement shape. Change no admission decision: a principal denied today stays denied; only the code and wording of the not-found class change. Do not change the catalog, the registry or any entitlement set.

TESTS (new file `tests/test_og_en9.py`; read the nearest existing catalog-gate test for the fixture style, `tests/test_og_cat*.py` or the one that imports `catalog_gate`):
- `test_ogen9_ac01`: a key with no catalog row answers 404 (or 400 when malformed), the answer names "not found", and it carries no `guard_denied`.
- `test_ogen9_ac02`: a key that resolves for a principal who is entitled answers as before (served); a key that resolves for a principal who is NOT entitled answers 403 with `guard_denied` and `entitlement_denied`.
- `test_ogen9_ac03`: the two arms are told apart on the same call shape: the same principal asking an un-rowed key and an entitled-denied key gets two different `http_status` values.
If an existing test pins the old 403 on an unresolvable key, update it to the new truth with the smallest edit and name it; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry or catalog change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print an account number or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/__init__.py
infra/aws/ec2/opal-gateway/tests/test_og_en9.py
infra/aws/ec2/opal-gateway/tests/test_graphql_catalog_gate.py
infra/aws/ec2/opal-gateway/tests/test_portal_index_integration.py
infra/aws/ec2/opal-gateway/tests/test_og_cat1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE the two app files and `tests/test_og_en9.py` and, only to follow the new truth, the existing catalog tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~123/`. Rows: id `NFRA_OPLGTW-Z-W123-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en9.py test_ogen9_ac01 test_ogen9_ac02 test_ogen9_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~123 '^infra/aws/ec2/opal-gateway/(app/graphql_plumbing/catalog_gate\.py|app/integrations/portal_index/(integration|__init__)\.py|tests/(test_og_en9|test_og_cat1|test_graphql_catalog_gate|test_portal_index_integration)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~123: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass: not-found is told apart from a denial. `AC2`: the commits of this serial touch only the catalog gate, its tool and the catalog tests.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-9.not-found-is-not-403.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the trace of how a no-row verdict became 403 before, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO update msg 34989, E9; row Z-S175 by the CVO), workstream ENRICH-R38-B (decomposition addendum R3-T.94; a second workstream because the L6 gate keys one issuer to a round and workstream). Risk WORLD by the L6 floor (a gateway infrastructure path), no deploy in this cell; rides the batched gateway release with E4, E5, E6, E8 and E10.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>staged</status>
<round>38</round>
<workstream>ENRICH-R38-B</workstream>
<slot>~123</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
