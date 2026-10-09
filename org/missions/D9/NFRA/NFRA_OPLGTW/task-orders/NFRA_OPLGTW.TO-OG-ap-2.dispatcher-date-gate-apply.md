# NFRA_OPLGTW task order -- `OG-ap-2` -- APPLY: the 49F gold dispatcher's date gate (OG-bf-1 leg Y)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-2</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the dispatcher's two triggers are the 49F floor schedule cron(45 12 * * ? *) and the accelerator notification on schwab/08335338/meta/complete/ (the daily T-1 marker lands ~09:46Z). Neither changes. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no role or policy changes: the plan must read 1 resource changed, code only (source_code_hash, s3_object_version, last_modified).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed never-widen pair on the Y leg: COO half org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-bf-1-Y_20261009.md @9e406fcb00 and CTO half org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~O/NEVER_WIDEN_HALF_CTO_OG-bf-1-Y_20261009.md @094786bd2a, over the ask org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~41/NEVER_WIDEN_ASK_OG-bf-1-Y.md @3167419765.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-2` (decomposition addendum R3-T.30; OG-bf-1 amendment A1, leg Y)

Deploy the 49F gold dispatcher's date gate: `advi-49f-gold-dispatch` SKIPs a qualified accelerator record whose date is
not the production T-1. It is built and tested on box/sitez (`infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/`:
`lambda_function.py` and a byte copy of `lib/trading_calendar.py`; AC4 of OG-bf-1 4 of 4, the OG-m-2a suite 6 of 6).
READ the ask (sections 3, 4, 5) and both halves. The halves BIND.

1. **The source map, its own commit first.** Register `trading_calendar.py` in
   `functions["advi-49f-gold-dispatch"].files` of `infra/aws/lambda/ci/lambda-source-map.json` (one entry), commit it alone
   (row Z-W41-S2). Then `--build-only`: the zip holds exactly `lambda_function.py`, `trading_calendar.py` and the
   builder's manifest, each member equal to the ask's section 1 hashes. Record the built `CodeSha256` (the "after").
2. **Ledger** `nfra-oplgtw-og-bf-1-y-dispatcher-gate` (`.tools/deploy_ledger.py open --lambda advi-49f-gold-dispatch ...`),
   entry AND sentinel committed before the act.
3. **Plan, then apply** through `module.advi_49f_gold_dispatch` with `bash .tools/safe-apply.sh`, `-target` to that module
   only: 1 resource changed, only `source_code_hash`, `s3_object_version`, `last_modified`; the 5-key environment
   unchanged. Any other plan row is a STOP. Never `aws lambda update-function-code`.
4. **Read back:** `CodeSha256` equal to the built hash, `State Active`, `LastUpdateStatus Successful`, a post-apply plan
   reading `No changes`.
5. **Arm 1, on demand:** invoke the deployed function ONCE with a synthetic S3-shaped event naming
   `schwab/08335338/meta/complete/date=2026-09-15.json` at VersionId `ReevhBJRXCWNerbIirOWCfJG5G_Ewqc1`. Expect
   `dispatched: false` and a `skip_reason` ending "is not the production T-1 <T>; historical record, not dispatched".
   Write `W/ap2_arm1.json` = `{"request_id": "<the invoke's RequestId>", "invoked_epoch_ms": <int>, "response": {...}}`.
   Read `ssm list-commands` for the chain document and the host's instance state before and after: both unchanged.
6. **Arm 2 is organic only:** do NOT invoke with a T-1 record. The issuer reads the next daily marker's dispatch.
7. Close the ledger and commit, then run the criteria. A read-back that disagrees: roll back to artifact version
   `AQ2rQSyBdPpB0sWozwovunpWoL9TWVYA` (`CodeSha256 TjIWGFWkbUswLkA+mUac9NS+LRZ1q7o6lR1iQLb0kI4=`) by the same Terraform path
   and file an ARMED row naming `2.0.0_SA_COO~O`. Never leave it half-landed.
8. **Timing:** outside the accelerator's minutes (~09:45-09:50Z) and away from the floor (12:45Z); before 09:30Z if you
   can. Report to `2.0.0_SA_COO~O` once, when the ledger closes.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- One Lambda, code only. No other function, role, notification, schedule or environment key changes.
- One synthetic invoke (Arm 1). No invoke with a T-1 record; no production chain run on demand.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-bf-1-y-dispatcher-gate.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-AE-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap2.sh AC1; echo "exit=$?"</invocation><expect>(?s)member lambda_function\.py: present=True equal-to-HEAD=True.*member trading_calendar\.py: present=True equal-to-HEAD=True.*State=Active LastUpdateStatus=Successful.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap2.sh AC2; echo "exit=$?"</invocation><expect>(?s)SKIP with 'is not the production T-1' True; 'dispatched: doc=' False.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live zip is HEAD's dispatcher and calendar, byte for byte, and no longer the rollback build.
- `AC2`: a historical record SKIPs on the deployed function, by its own log.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-2.dispatcher-date-gate-apply.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32, workstream APPLY-Y: OG-bf-1's leg Y (A1), the CTO-ruled design (CTO half on OG-bf-1 @f9b1f1fd31 section 2),
  deployed by the site Z applier (msg 32057). Halves on the leg: COO @9e406fcb00, CTO @094786bd2a.
- After this ledger closes and its read-back is committed, OG-bf-1 Phase D (08335338) takes a fresh pair of halves.
- Pre-cut: ap2.AC1 base FAIL as expected (live CodeSha256 = the rollback hash; the live zip has no trading_calendar.py,
  its lambda_function.py differs from HEAD's); ap2.AC2 base FAIL as expected (record absent).

<status>complete</status>
<round>32</round>
<workstream>APPLY-Y</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
