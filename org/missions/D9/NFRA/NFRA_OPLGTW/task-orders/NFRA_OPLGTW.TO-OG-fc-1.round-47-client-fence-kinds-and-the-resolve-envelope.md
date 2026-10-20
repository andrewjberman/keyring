# NFRA_OPLGTW task order -- `OG-fc-1` -- the client core serves orion, eclipse and commonwealth (D1) and its resolve envelope describes every vendor read (D3): `app/client_core.py` and one test file (round 47; round-46 analysis item 1 and item 5; PRD FWD-22)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-fc-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-fc-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~166</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the client tools read S3 prefixes the gateway role already reads.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429), rank 1: D1 first, "fence_kind rows for orion, eclipse and commonwealth", with D3 (row Z-S411) in the same file.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-fc-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY. The `client_*` tools never answer for three of the five vendors the gateway has adapters for. The core binds a table of FENCE KINDS per vendor in `_names()` (`infra/aws/ec2/opal-gateway/app/client_core.py`, the `"fence_kind"` dict, about line 194): it holds only `schwab` and `blackdiamond`. `Ctx.firm_segments(vendor, firm)` (about line 389) reads that table, so it returns `[]` for orion, eclipse and commonwealth, and each of those three adapters refuses `firm_not_served` before any read (`client_adapter_orion.py` `_segments`, `client_adapter_eclipse.py` `_segments`, `client_adapter_commonwealth.py` `_firm`). The data is current in S3 (orion `fact_positions` to 2026-10-19, eclipse `fact_models` to 2026-10-17). A second defect lives in the same file: `client_resolve_account` (about line 549) merges the candidates of every adapter that holds the firm but answers under the FIRST answering adapter's envelope (`merged = dict(answered)`), and the refusal codes of the other adapters are collected in a local list that is used only when NO adapter answers.

READ FIRST: `app/client_core.py` lines 182-208 (`_names`), 389-406 (`firm_segments`), 549-584 (`client_resolve_account`), 506-526 (`_answer`, `_META_FIELDS` at line 44); `tests/test_og_cl1.py` lines 219-300 (a fake-adapter fixture and the resolve-merge test `test_ogcl1_ac03`); `tests/test_og_cl7.py` (`test_t2_core_names_bind_spellings_aliases_and_fence_kinds`).

DO, in `infra/aws/ec2/opal-gateway/app/client_core.py` ONLY (plus the new test file):

1. **D1. Add three fence-kind entries to the `fence_kind` dict in `_names()`**: `orion` -> the inflection firm owns the one master segment named by the inflection firm's own registry key; `eclipse` -> the same; `commonwealth` -> the cottonwood firm owns the one segment named by the cottonwood firm's registry key. Use the same tuple form the blackdiamond row uses, `("segment", <name>)`, and take each segment name from the values `_names()` already binds from `lookup()` (the variable `kinf` and `kct` in that function); do NOT type a firm or segment string (LGIC rule 30: names come from the registry). The catalog's silver prefixes that make this correct are `orion/inflection/silver`, `eclipse/inflection/silver` and `commonwealth/cottonwood/silver`; the orion prefix `orion/4698/silver` is an alias the adapter does NOT read and must stay unserved. Result you must reach: `Ctx().firm_segments("orion", <inflection>) == ["inflection"]`, `("eclipse", <inflection>) == ["inflection"]`, `("commonwealth", <cottonwood>) == ["cottonwood"]`; every other (vendor, firm) pair that returned `[]` still returns `[]`; schwab and blackdiamond unchanged.
2. **D3. Make the merged `client_resolve_account` envelope describe every vendor read.** After the change, for a call where several adapters hold the firm: (a) `source_keys` is the sorted union of the `_source_keys` of every adapter that ANSWERED; (b) `denominator` is a dict whose `"candidates"` equals the merged `candidate_count` and whose `"by_vendor"` maps each answering vendor to that adapter's own `_denominator`; (c) `absent_reason` is `None` whenever `candidate_count` is above 0, and otherwise the first answering adapter's own absent reason (the zero-candidate behaviour does not change); (d) when at least one adapter REFUSED while another answered, the envelope carries a new key `refusals`: a list of `{"vendor": <vendor>, "code": <the refusal code>}` in vendor order, and when nobody refused the key is ABSENT (the single-vendor shape is unchanged); (e) when NO adapter answers, the existing behaviour stands (the first refusal code is the enveloped refusal; nothing else changes). `_answer(...)` is the one place the shared envelope is built: reuse it, do not duplicate it, and do not change the single-vendor tools (`client_get_holdings` and the others).
3. **The new test file `infra/aws/ec2/opal-gateway/tests/test_og_fc1.py`** with at least these tests (names fixed): `test_ogfc1_d1_served_pairs` (the three pairs above through a real `core.Ctx()`), `test_ogfc1_d1_unserved_pairs_stay_empty` (orion with the cottonwood firm, eclipse with the 49financial firm, commonwealth with the inflection firm, and the `4698` alias: all `[]`), `test_ogfc1_d3_merge_envelope` (three fake adapters as in `test_ogcl1_ac03`: one answers zero candidates with source key `a/k`, one answers one candidate with source key `b/k`, one refuses `firm_not_served`; assert (a) to (d)), `test_ogfc1_d3_single_vendor_shape` (one adapter answering: no `refusals` key, `source_keys` that adapter's) and `test_ogfc1_d3_all_refused` (two adapters refuse: the enveloped refusal carries the first code and `candidates` is absent as before).

## 2. BOUNDS

- Write only `infra/aws/ec2/opal-gateway/app/client_core.py`, `infra/aws/ec2/opal-gateway/tests/test_og_fc1.py`, `W/` and, if a row is needed, the channel. NO adapter file, no other test, no contract file, no release, no deploy, no Terraform, no AWS call.
- The seven adapters are NOT edited: a refusal they raise stays theirs.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, an email address or a client value in a test, a record or a report (fake fixtures only; the last-4 `1234` is a fixture).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/tests/test_og_fc1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~166/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W166-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-fc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/fc1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)served pair orion/inflection: segments \['inflection'\].*served pair eclipse/inflection: segments \['inflection'\].*served pair commonwealth/cottonwood: segments \['cottonwood'\].*served pairs 3 of 3; controls held 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-fc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/fc1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)merge: candidate_count 1, absent_reason None: ok.*merge: source_keys \['a/k', 'b/k'\].*: ok.*merge: denominator candidates 1, by_vendor keys \['fakea', 'fakeb'\]: ok.*merge: refusals \[\{'vendor': 'fakec', 'code': 'firm_not_served'\}\]: ok.*control one adapter.*: ok.*control zero candidates.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-fc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/fc1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_fc1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (D1): the three served pairs read their segment and four control pairs plus schwab are unchanged. `AC2` (D3): the merged envelope names every source, the total denominator and the refusal. `AC3`: your test file passes and the 17 existing client-surface test files still pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-fc-1.round-47-client-fence-kinds-and-the-resolve-envelope.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) rank 1 (D1, Z-S409) and rank 5 (D3, Z-S411); the release is a later applier order under its own never-widen.
- READINGS DISCLOSED TO THE CTO: (1) the shape of the D3 envelope is the issuer's: `denominator` becomes `{"candidates": n, "by_vendor": {...}}` for a merged answer and a new `refusals` key appears only when some adapter refused; a reader that parses `denominator` as the adapter's own dict keeps `candidates` at the same key. (2) D1 is the table row only: whether the orion, eclipse and commonwealth adapters then answer correctly is proved on the host by the release order's one live call per vendor, not here. (3) `4698` stays unserved: the orion adapter's own docstring says the alias is not read.
- Base blob of `app/client_core.py` at the issuance is the trunk tip at the cut. Pre-cut: `AC1` base FAIL as expected (served pairs 0 of 3), `AC2` base FAIL as expected (merge lines NO; the two controls hold), `AC3` base FAIL as expected (no test file). The 17 neighbour files pass at the base (81 tests).

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~166</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
