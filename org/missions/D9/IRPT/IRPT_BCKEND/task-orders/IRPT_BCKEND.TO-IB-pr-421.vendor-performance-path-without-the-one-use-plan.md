# TO IRPT_BCKEND.TO-IB-pr-421 -- the fresh vendor performance path no longer requires an installed one-use plan; what stays is tested; adapter rebuilt; never-widen packet

<to_id>IRPT_BCKEND.TO-IB-pr-421</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~282</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4416 (ruling on this seat's msg 4413), on Andrew-direct 2026-10-09 `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_CLAUDE_MD_EGRESS_OPEN_EXCEPT_BBG.md`; DSGN_IRPTV1 FWD-1 walk `org/tier1_exec/4.0.0_SA_CRO/deliverables/UI_WALK_DSGN_IRPTV1_FWD1_20261011T0730Z.md` | **Decomp cell:** `IB-pr-421` (decomposition section 112) | **outcome_ref:** FWD-2

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-282/` (bash `/c/dev/wk-irpt-bckend-282`). Work only there.

**The break.** The live `irpt-performance-adapter` admits a performance-report request and then refuses it:
`VendorEgressRefused("matching current server-approved performance use required")`, public code `OBJECT_NOT_COVERED`, raised at
`infra/aws/lambda/investor-reporting/performance/authorization.py:90`. That line is the end of `OneUseTransportFactory.__call__`: it
demands an operator-installed plan (`IRPT_PERFORMANCE_APPROVED_PLAN` + `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED` equal to the plan's digest)
for ONE firm, ONE account and ONE date window, then spends it with a conditional write. Measured 2026-10-11 07:30Z: 4 of 4 admitted
requests of the product walk ended there. The law that gate enforced is replaced: vendor APIs other than Bloomberg need no per-use word.
Its two vendors are Black Diamond (Cottonwood) and Orion (Inflection). Neither is Bloomberg.

**Build, in `infra/aws/lambda/investor-reporting/performance/`.** Read `authorization.py`, `transport.py`, `bd_live.py`, `orion_live.py`,
`runtime.py`, `retained.py` and `installed.py` first; trace every place a per-use token or the plan is read.
1. **Retire the one-use plan.** A fresh vendor-path request no longer needs `IRPT_PERFORMANCE_APPROVED_PLAN` or
   `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED`. Neither environment variable is read on the served path. The transports must construct
   without a per-use token on that path. Keep the class the runtime builds importable under a name that says what it now is; update
   `runtime.py` to match. Do not leave a dead plan branch behind.
2. **What STAYS, each with a test** in a new file `performance/tests/test_vendor_use_gate.py`. Each test's name contains the quoted token:
   - `no_plan_required`: with neither variable set, a request for a packaged firm with a matching mapping returns a transport;
   - `unpackaged_firm_refused`: a firm with no packaged path (`firm_paths()`) is refused `VendorEgressRefused`;
   - `vendor_account_from_own_mapping`: the vendor account id (and external id) used in the built vendor requests come ONLY from
     the firm's own mapping at its current revision; a request cannot supply or override them;
   - `request_firm_and_accounts_are_the_callers`: the firm and the accounts in the vendor requests are the request's verified ones;
     a transport asked to send a body that differs from the built requests is refused (`_BoundTransport` keeps doing this);
   - `use_record_logged_each_vendor_call`: every fresh vendor use writes ONE use record to the table, as a LOG: an unconditional
     put whose key is unique per use (it must not collide for two uses of the same firm, account and window), carrying firm, the
     request digest, the mapping revision and the time. A failed write refuses egress (no unlogged vendor call);
   - `cache_hit_never_calls_vendor`: reopening an accepted report (the retained path) builds no transport and writes no use record.
3. **Existing tests.** `performance/tests/test_authorization.py` tests the retired behaviour. Rewrite it to the new behaviour; do not
   delete a test that still describes something true. Other performance tests that set `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED`
   (`test_bd_live.py`, `test_performance_adapters.py`, `test_orion_live.py`, `test_primary_policy.py`) are updated only as far as your
   change makes them false. Run the whole `performance/tests` directory and report its last line; a failure that predates your change is
   named with its node id and left.
4. **Rebuild the adapter from ONE commit** the way IB-pr-416 did (read
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-416.md` and that folder's
   `make_candidate_map.py`, `make_census_416.py`, `signature_closure_attr.py`, `method_call_limb_416.py`, `replay/`). After your product
   commit, every investor-reporting member of `irpt-performance-adapter` is pinned to THAT commit in a candidate map in your
   deliverables (`BAU_SOURCE_MAP_OVERRIDE`; the real `infra/aws/lambda/ci/lambda-source-map.json` is NOT edited). `BUILD_ONLY=1`, twice,
   byte-identical; upload nothing. The name, attribute and method limbs each read 0 on the built zip.
5. **Census** `deliverables/0.9.0_WK_IRPT_BCKEND~282/IB119-1_adapter_census.json`: `{function, pin, built_sha256,
   built_twice_identical, live_before, rollback_version, built_signature_mismatched, built_attribute_mismatched,
   built_method_mismatched, changed_members:[{member, built, live, commits}]}`. `live_before` is the live CodeSha256 you read
   (expect `9kYLdR64P0p2TEbDXcQu1hrpQ9KtqjPNnFDpoE/W31A=`); `rollback_version` is the S3 version of
   `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip` whose `content-sha256` is that digest.
   A changed member outside `performance/` is named with its owning commits; if one is not a packet-signed change, stop and file a row.
6. **Replay** `deliverables/0.9.0_WK_IRPT_BCKEND~282/IB119-1_replay.json`, `{arms:[{name, verdict, negative_control, detail}]}`, live zip
   against built zip, offline, in-memory fakes, NO vendor call, every verdict `identical` or `expected-diff`. It includes IB-pr-416's
   adapter arms (binding cases, no-row-internal enforcer scope, enforcer build) reading `identical`, plus:
   - `fresh_vendor_path_no_plan`: live refuses `VendorEgressRefused`, built reaches the fake transport with exactly the built
     requests: `expected-diff`;
   - `cache_hit_no_vendor_call`: both trees reopen an accepted report with 0 transport constructions: `identical`;
   - a negative control: the built tree with `authorization.py` put back to the live bytes refuses again.
7. **Packet** `deliverables/0.9.0_WK_IRPT_BCKEND~282/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-421.md`, in IB-pr-416's form. It states plainly
   that this WIDENS served output: a signed-in Cottonwood or Inflection user's fresh performance request now calls the vendor with the
   firm's stored credentials, where before every such request was refused. It names: the blast radius (one function; the vendor
   calls now reachable, per firm; the use-record writes); live and built sha256; changed members; Branch A (land) and Branch B
   (redeploy the rollback version, re-read at apply); whether the function's role already holds every permission the new path needs
   (read the Terraform and say; change none); the two environment variables as no longer read, left in place for a later cleanup;
   and what is NOT exercised (no real vendor call was made by this cell).

<criterion id="IB119-1-AC1" cell_refs="IB-pr-421"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r119/p119_cells.py" . IB119-1-AC1</invocation><expect>IB119-1-AC1 PASS</expect></criterion>
<criterion id="IB119-1-AC2" cell_refs="IB-pr-421"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r119/p119_cells.py" . IB119-1-AC2</invocation><expect>IB119-1-AC2 PASS</expect></criterion>
<criterion id="IB119-1-AC3" cell_refs="IB-pr-421"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r119/p119_cells.py" . IB119-1-AC3</invocation><expect>IB119-1-AC3 PASS</expect></criterion>

<expected_criteria>IB119-1-AC1, IB119-1-AC2, IB119-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD_ONLY plus AWS reads; NO upload, apply or deploy; NO environment, IAM, route
  or Terraform change.
- **NO VENDOR CALL.** No request to Black Diamond, Orion or any vendor; no credential is read from Secrets Manager. Tests and the
  replay use fakes.
- **Authorization is untouched.** Change nothing in `_authz/`, `_scope/`, `served.py` or `entry.py`'s authorization: who may ask is
  unchanged; only what happens after an admitted request reaches the vendor path changes. 49 Financial never reaches this path.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, or a kept behaviour cannot be kept, stop, file a row, and report.
  Never weaken a check or a test; do not edit `p119_cells.py`.
- **Client figures:** no account id, balance or flow in the packet, the census or the replay: counts, sha256 and reason codes only.
  Extracted zips stay outside the worktree and are deleted file by file at the end.
- **Row ids** are `IRPT_BCKEND-D2-W282-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~282" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~282@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~282 <0.9.0_WK_IRPT_BCKEND~282@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/performance/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~282/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-421.vendor-performance-path-without-the-one-use-plan.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 112 (round 119, workstream ~P), cell `IB-pr-421`.
<owned_cells>IB-pr-421</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB119-1-AC1, IB119-1-AC2, IB119-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~282/IRPT_BCKEND.TO-IB-pr-421.vendor-performance-path-without-the-one-use-plan.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the product commit; the whole `performance/tests` last line; the built sha256 and the rollback
version; the changed members; each criterion's last line; the proof checker's result; what the role already permits; any row ids; what
scratch remains.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function (irpt-performance-adapter); product source under performance/ only; the change makes Black Diamond and Orion calls reachable from a signed-in firm user's fresh performance request; nothing uploaded in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change in this cell, and the tool was not run by the issuer; step 7 has the worker read the function's role in Terraform and state in the packet whether it already holds what the new path needs.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p119_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~07:5xZ: AC1 FAIL (no test file), AC2 FAIL (no census), AC3 FAIL (no census); commit-gate clean.
lane: the <paths> block IS the grant; ~P's performance package.
</preflight>
