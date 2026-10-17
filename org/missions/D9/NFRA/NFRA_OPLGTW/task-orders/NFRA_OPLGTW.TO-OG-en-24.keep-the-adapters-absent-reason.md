# NFRA_OPLGTW task order -- `OG-en-24` -- `client_core._answer` keeps the adapter's `absent_reason`, so a refused windowed call reads `window_read_busy` and not an empty "no transactions" (round 41; CTO decision on row Z-S372, msgs 35485, 35489 and 35492, with the CVO's row Z-S373)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-24</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-24</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~138</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision on row Z-S372 (msgs 35485, 35489): "cut the mapping now; do not ship an empty refusal".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-24` (decomposition addendum R3-T.114, round 41, workstream ENRICH-R41-R)

THE DEFECT (read `app/client_core.py` `_answer` and `app/client_adapter_bd49f.py` `_absent` and `_window_busy`, both already in your cone). The 49F adapter's `_absent(as_of, code, body, cadence)` puts the reason in the answer under the key `absent_reason` (no underscore) and sends NO `_absent_reason` meta key. `client_core._answer` builds the final body with `"absent_reason": meta["_absent_reason"]`, which is None for that adapter, so it OVERWRITES the adapter's code with null. A windowed call that cannot take the one-read gate in time (`_window_busy`, the `window_read_busy` answer with `retry_after_seconds`) therefore reaches the caller as empty rows with `absent_reason` null, which reads as "this account has no transactions" (a failed retrieval returning a value). The same line is in the live release; it was never reachable before the gate could contend.

THE FIX (code only, ONE line of product code):
1. In `app/client_core.py` `_answer`, the `absent_reason` entry keeps the adapter's code when the adapter sent no `_absent_reason`: the value is `meta["_absent_reason"]` when that is not None, otherwise the body's own `absent_reason` (`out.get("absent_reason")`). Nothing else in `_answer` or elsewhere changes. An adapter that sends `_absent_reason` (Schwab, Orion, Eclipse, SmartX) answers exactly as before.
2. Before you finish, ENUMERATE which answers this changes: read every `_absent(` call in `app/client_adapter_bd49f.py` and every non-underscore `absent_reason` an adapter sets that reaches `_answer`; list each code and say, in the proof's session log, that it now surfaces (counts and code names only). This is information for the issuer, not a license to change anything else.
3. Do not touch the adapter, `app/tools.py`, `app/typed_scope.py`, or any file not in `<paths>`.

TESTS (new file `tests/test_og_en24.py`; read `tests/test_og_en18.py` for how a refused second call is produced, the gate and `WINDOW_GATE_WAIT_SECONDS` are module-level, and `tests/test_og_cl2.py` for `_answer` fixtures):
- `test_ogen24_ac01` (the CTO's test): with the one-read gate held by a first windowed call and the gate wait set short (patch `WINDOW_GATE_WAIT_SECONDS` in the adapter), a SECOND `get_transactions` call through the real `client_core` answer path returns empty rows AND `absent_reason` equal to `window_read_busy` AND `retry_after_seconds` present; the same for `get_fees`; and the FIRST call's answer carries no `absent_reason` (null).
- `test_ogen24_ac02` (the line does only that): an adapter body that sends `_absent_reason` answers with that value (the `_absent_reason` wins even when the body also has a different `absent_reason`); a body with neither answers `absent_reason` null; a body with only `absent_reason` answers that code; and a normal 49F transactions page answers `absent_reason` null.
- `test_ogen24_ac03` (the general case, CTO msg 35492 and the CVO's row Z-S373): a read at a date that holds no partition (the refusal `no_partition_at_as_of`) answers `absent_reason` equal to `no_partition_at_as_of` for EACH of the five tools that can refuse so (`client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees`), through the real `client_core` answer path; the live release nulls all five.
If an existing test pins `absent_reason` null for an adapter answer that now carries a code, update it to the new truth with the smallest edit and name it in your report; never weaken any other test.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change, no change to the adapter, `app/tools.py` or `app/typed_scope.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/tests/test_og_en24.py
infra/aws/ec2/opal-gateway/tests/test_og_en23.py
infra/aws/ec2/opal-gateway/tests/test_og_en22.py
infra/aws/ec2/opal-gateway/tests/test_og_en20.py
infra/aws/ec2/opal-gateway/tests/test_og_en19.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_core.py`, `tests/test_og_en24.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~138/`. Rows: id `NFRA_OPLGTW-Z-W138-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-24"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en24.py test_ogen24_ac01 test_ogen24_ac02 test_ogen24_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-24"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~138 '^infra/aws/ec2/opal-gateway/(app/client_core\.py|tests/test_og_(en24|en23|en22|en20|en19|en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~138: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-24"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en24set tests/test_og_en4.py tests/test_og_en12.py tests/test_og_cl2.py tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py; echo "exit=$?"</invocation><expect>(?s)en24set forward: passed (\d+); failed 0.*en24set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass (a refused second call carries `window_read_busy` for transactions and fees; the line changes nothing else; the five `no_partition_at_as_of` refusals carry their reason). `AC2`: the commits of this serial touch only the listed files. `AC3`: the twelve window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-24.keep-the-adapters-absent-reason.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, the enumeration of the codes that now surface, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41-R (decomposition addendum R3-T.114): the CTO's decision on `Z-S372` (35485: "cut the mapping now; do not ship an empty refusal", 35489: a trunk cell, then a re-run GO). `OG-ap-36` is amended A3: the release takes `client_core.py` and `tests/test_og_en24.py` from the new trunk; the re-run is proportionate (the window test files, CT1; no memory gate; a fresh ask; the three halves re-sign on the new release sha).
- The enumeration (step 2) matters: every 49F `_absent(...)` answer that reached the caller with `absent_reason` null will now carry its code. That is the intent (the adapter set the code and the core dropped it), and it widens nothing in reach (no row is added or removed), but the issuer names it in the ask. The CTO adopted the CVO's row Z-S373 (msg 35492): the mapping is GENERAL (whenever `_absent_reason` is None), and the five `no_partition_at_as_of` refusals the live release nulls are part of the proof (`test_ogen24_ac03`).
- Pre-cut: `AC1` base FAIL as expected (the test file is absent); `AC3` base FAIL (the file is absent).

<status>complete</status>
<round>41</round>
<workstream>ENRICH-R41-R</workstream>
<slot>~138</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
