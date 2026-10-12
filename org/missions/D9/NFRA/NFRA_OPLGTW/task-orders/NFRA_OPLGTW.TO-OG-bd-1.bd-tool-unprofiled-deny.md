# NFRA_OPLGTW task order -- `OG-bd-1` -- census the callers of `blackdiamond_list_fees`, then deny it to unprofiled principals (E8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bd-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-bd-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~57</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an audit-lake read and a code change; the deny reaches users only in a later gateway release.
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the operator's identity; the code change narrows a tool's admission, it widens nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling on row W45-S2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_W45_S2_BD_TOOL_UNPROFILED_20261011_Z.md @135719d313 (read it whole).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads of the audit lake).
</preflight>

## 1. THE CELL -- `OG-bd-1` (decomposition addendum R3-T.42, E8)

Row W45-S2: `blackdiamond_list_fees` is classified legacy and is NOT denied to an UNPROFILED principal. `decide()`
(`infra/aws/ec2/opal-gateway/app/data_entitlement.py:448`) passes it through to the tool's own gate, while the five
Schwab tools are denied. The ruling: deny it, but only after a caller census. An unprofiled caller found means STOP, and
an Andrew admission call is owed.

1. **Census.** Read the gateway audit lake (the bucket is the gateway's `AUDIT_S3_BUCKET`; records are written by
   `app/audit.py`, which carries `tool` and `principal` = `<tid>/<oid>`). Cover the whole retained history. List every
   distinct principal that called `blackdiamond_list_fees`, and say whether it is PROFILED, by the same profile lookup
   `decide()` uses (read it in data_entitlement.py). Write `W/BD1_CENSUS.json` =
   `{"window", "records_scanned", "callers": [{"principal", "profiled", "calls"}]}`, with principal ids only and no names.
2. **If any caller is unprofiled: STOP.** Build no deny, and file a BLOCKING row naming the callers' count and the owed
   Andrew admission call. Report. Leave the order pending.
3. **If none:** add the deny to `decide()`: an unprofiled principal is denied `blackdiamond_list_fees` like the Schwab
   family. A profiled principal's answer is unchanged. Tests in `infra/aws/ec2/opal-gateway/tests/test_og_bd1.py`:
   - `test_ogbd1_ac01`: unprofiled is denied the BD tool;
   - `test_ogbd1_ac02`: profiled is unchanged;
   - `test_ogbd1_ac03`: the five Schwab tools are still denied to unprofiled.

   Re-pin `tests/test_data_entitlement_family.py::test_ogpf1_ac02`, which pins the old pass-through, to the new answer,
   and name it in your report.

## 2. BOUNDS

- Audit-lake reads, and the code and tests above. No release, no deploy, no grant or profile written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or email; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_og_bd1.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~57/`. Rows: id `NFRA_OPLGTW-Z-W57-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/bd1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)audit records scanned [1-9]\d*; .*unprofiled 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-bd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/bd1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*failing ids not in the baseline: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the census is clean (the ruling's precondition). `AC2`: the deny is built, and nothing else regresses.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bd-1.bd-tool-unprofiled-deny.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, E8. Second on slot ~57 after OG-dq-1. The deny rides the next gateway release after this merges.
- Pre-cut: bd1.AC1 and bd1.AC2 base FAIL as expected (census and test file absent).

<status>superseded -- CLOSED for round 34 by 2.0.0_SA_COO~O, 2026-10-11 ~22:3xZ, HELD on the CTO ruling's own STOP: the census (@c49a0ed0bb, 255,023 audit records, 110 days) found 2 unprofiled callers of blackdiamond_list_fees, so no deny was built and an Andrew admission call is owed (row Z-W57-S2, surfaced to Andrew by 0.0.0_AB_MSTR~Z msg 33359). NOTHING IS RE-GRADED BY THIS CLOSE: AC1 stands as measured (unprofiled 2). The cell RE-CUTS in round 35 on Andrew's answer. Was: pending.</status>
<round>34</round>
<slot>~57</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
