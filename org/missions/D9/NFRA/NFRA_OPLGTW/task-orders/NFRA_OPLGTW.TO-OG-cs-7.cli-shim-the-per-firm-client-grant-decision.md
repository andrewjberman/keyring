# NFRA_OPLGTW task order -- `OG-cs-7` -- the per-firm client grant decision: a (vendor, firm) pair is granted by a string in a person's record (cli-shim workstream, wave 3; PRD v3.19 FWD-24, the CTO's msg 36202)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-7</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-7</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~185</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the module is pure (standard library and `app/data_entitlement.py` only).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is PRD v3.19 FWD-24 (ADMITTED), applied as one pure function with no deploy and no call site; mounting it on the `client_*` tools is a later, separate order with its own never-widen halves.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cs-7` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-C, wave 3)

WHY. Today a `client_*` tool (the typed client-data tools) is admitted by tool name only: a profiled person who holds the tool reads every firm, and an unprofiled one is master-admin only. FWD-24 says the entitlement is a string in the person's record. This cell writes the decision for ONE pair, as a pure function in ONE new module, `app/client_grant.py` (under `infra/aws/ec2/opal-gateway/`), in the same shape as `app/folder_grant.py` (READ it first, and `app/data_entitlement.py` `PersonAccess` and `_CHANNEL_OR_FOLDER`; do not edit either). A pair is granted by an entry of `channels_allow` in a **client namespace** that the folder grants never reach: the namespace `opal-clients` is not one of the three served buckets, so `folder_grant.folder_decision` refuses it, and the entry already passes the person-access entry parser.

THE INTERFACE (exact names):

1. `CLIENT_NAMESPACE = "opal-clients"`.
2. `client_entry(vendor: str, firm: str = "") -> str`: `"opal-clients/<vendor>/<firm>"`, or `"opal-clients/<vendor>"` when `firm` is empty, or `"opal-clients"` when both are empty.
3. `client_pair_decision(is_master_admin: bool, is_opal: bool, rec, vendor, firm) -> tuple[bool, str]`: `(allowed, reason)`; `rec` is `None` or a `PersonAccess`. Rules, in order: (a) `vendor` and `firm` must each be a `str` matching `^[a-z0-9]{2,32}$`, else refused with a reason naming the field (`vendor` or `firm`); (b) not an Opal principal: refused; (c) a LIVE record (`status == "active"` and not `stopped`) whose `channels_deny` holds an entry that covers the pair: refused, deny wins, the master admin included; (d) the master admin: allowed; (e) a LIVE record whose `channels_allow` holds a covering entry: allowed; (f) anything else: refused with a reason that says no granted entry covers the pair. An entry COVERS the pair when its `/`-split parts are `["opal-clients"]` (every pair), `["opal-clients", vendor]` (every firm of that vendor) or `["opal-clients", vendor, firm]` (that pair only); an entry of any other shape, and every folder entry of the served buckets, covers nothing. Reasons name the pair and the covering entry where one exists (sorted order, so the answer is deterministic).

The module imports only the standard library and `app.data_entitlement` (no AWS, no network, no I/O).

## 2. TESTS

NEW `tests/test_cs7_client_grant.py`, at least EIGHT tests, offline, `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import: the entry builder in its three forms; each covering shape admits exactly what it should and nothing else (pair, vendor, namespace); deny wins over a vendor allow and over the master admin; the master admin with no record; no record, a stopped record, a revoked record and a non-Opal caller refused; each malformed vendor or firm (empty, uppercase, a slash, `..`, one character, thirty-three characters, a non-str) refused with the field named; every `client_entry` string accepted by `data_entitlement._CHANNEL_OR_FOLDER`; a served-bucket folder entry covers no client pair and a client entry is refused by `folder_grant.folder_decision`.

## 3. BOUNDS

- Write only the two files above and, if a row is needed, the channel. No other product file (`data_entitlement.py`, `client_core.py` and every `client_adapter_*.py` stay untouched), no test but the one, no release, no deploy, no AWS call.
- Counts and hashes only: no e-mail address, account number or token in any file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 4. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_grant.py
infra/aws/ec2/opal-gateway/tests/test_cs7_client_grant.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~185/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W185-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 5. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)the namespace and the entry builder .*: ok.*accepted by the person-access entry parser: ok.*a pair entry admits that \(vendor, firm\) only: ok.*a vendor entry admits every firm of that vendor .*: ok.*the namespace alone admits every pair: ok.*deny wins: .*: ok.*the master admin is admitted with no record .*: ok.*no record, a stopped record, a revoked record and a non-Opal caller are refused: ok.*a malformed vendor or firm is refused even for the master admin \(8 of 8\): ok.*served-bucket folder entries cover no client pair .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs_foot.sh org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-7.cli-shim-the-per-firm-client-grant-decision.md app/client_grant.py,tests/test_cs7_client_grant.py tests/test_cs7_client_grant.py 8 tests/test_cs1_folder_grant.py tests/test_og_cp1.py; echo "exit=$?"</invocation><expect>(?s)files that differ from HEAD under the gateway folder: .*: ok.*tests/test_cs7_client_grant\.py: (?:[89]|[1-9]\d+) test functions.*: ok.*new file tests/test_cs7_client_grant\.py: (?:[89]|[1-9]\d+) passed, 0 failed.*neighbours \(2\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` is graded by an issuer-written probe independent of your tests. `AC2`: the footprint is exactly the two files, and your tests plus the two person-access neighbours pass.

## 6. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-7.cli-shim-the-per-firm-client-grant-decision.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-7.cli-shim-the-per-firm-client-grant-decision.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-C, wave 3, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`. Source: PRD v3.19 FWD-24, the CTO's msg 36202 (row Z-S432) and msgs 36299, 36300.
- Widening, plainly: none by this order (a function nothing calls). Mounting it on the `client_*` tools would NARROW a profiled person who holds a client tool today and reads every firm; that act is a separate order after a CTO ruling on the namespace string and on whether an unprofiled-but-granted person is admitted. The namespace `opal-clients` is the issuer's reading of "a string in the record that no served-bucket grant can reach"; the CTO may rename it before the mount order is cut.
- DISCLOSED READINGS: the vendor and firm tokens are the canonical lower-case keys `client_core` hands out (`49financial`, `cottonwood`, `orion`, `schwab`); aliases are the caller's to resolve first (`client_core.canonical_firm`).
- Pre-cut: `AC1` base FAIL as expected (`app.client_grant` absent); `AC2` base FAIL as expected. Arm on a SCRATCH copy of the gateway app (the shared tree untouched): a scratch `client_grant.py` reads `AC1` OK (all ten arms).

<status>pending</status>
<round>48</round>
<workstream>CLISHIM-C</workstream>
<slot>~185</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
