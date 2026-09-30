# NFRA_MCPMSP task order -- `MS-a-2` -- ROUND 1, hop 3 apply: the writer ships `register_tenant`, no firm live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-a-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~3</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the apply moves the function's code only; no role or policy changes (a plan showing one is a BLOCKING row).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; AC3 is the C11 control.
EGRESS CLASS, declared: none (Opal's own AWS account; the layer is NOT rebuilt).
</preflight>

## 1. THE CELL -- `MS-a-2` (decomposition section 2)

Ship the grant writer's new `register_tenant` op (`MS-w-1`, earlier in your queue, merged to CLOUD before this order)
to the live function `mcportal-grant-writer-lambda` (`name('mcportal', None, 'grant-writer', 'lambda')`), with NO
firm live.

1. **Open the ledger FIRST**: `python .tools/deploy_ledger.py open --slug nfra-mcpmsp-r1-writer-apply --title "NFRA_MCPMSP
   r1: grant writer register_tenant op" --author 0.9.0_WK_NFRA_MCPMSP~3 --leg "L1|activation|writer package build +
   targeted apply|apply line" --leg "L2|verify|deployed lambda_function.py == HEAD, LIVE_FIRMS empty|AC2+AC3 lines"`.
   Blast radius: the writer function's code package only; rollback = re-apply the previous package (its hash is in the
   plan's `source_code_hash` before-value; record it in the entry). Commit the entry and its sentinel
   `org/critical_paths/.open_deploys/nfra-mcpmsp-r1-writer-apply.json` before the apply.
2. **Build the package and apply, targeted to the writer function only**, on NFRA_MCPORTAL's precedent (read
   `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-a-2.writer-apply-sub.md` and its ledger entry for
   the exact build and target): `build_package.py` stages the package; `bash .tools/safe-apply.sh
   -chdir=infra/aws/terraform/opal-gateway apply -target=<the writer function's address>`. **Do NOT rebuild the layer**
   (that is a PyPI fetch, egress, held on Andrew's word): copy the layer zip the issuer restored into the MAIN worktree
   (`infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip`, its hash = the live
   layer's CodeSha256) into yours, so the layer reads no change. Borrow the main tree's `.terraform` via `TF_DATA_DIR`
   (no `init`). Read `mcportal_owner_key_claim` / `mcportal_owner_key` from the LIVE function's environment
   (`MCPORTAL_OWNER_KEY_CLAIM` / `MCPORTAL_OWNER_KEY`) into shell variables and pass them as `-var` -- **never print,
   log or commit the key value**. The plan must show ONLY the function's code changing (no environment change, no
   layer, no role); anything else is a BLOCKING row and no apply. Do NOT add `LIVE_FIRMS` (C11: no firm is live until
   Andrew's word, G-FIRM).
3. Read AC2/AC3, then close the legs and the entry, committing it with the sentinel removed.

## 2. BOUNDS

1. The writer's code package only. No Terraform file edit, no environment change, no layer build, no gateway act.
2. No push, no vendor call, no egress. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpmsp-r1-writer-apply.json
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/.build/
infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

(The two `.build` entries are gitignored build outputs, admitted locally, never committed.) Read, never write:
`infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`, `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/**`,
`.tools/safe-apply.sh`, `.tools/deploy_ledger.py`, the MCPORTAL MP-a-2 order and its ledger entry,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W3-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a2.AC1.sh; echo "exit=$?"</invocation><expect>slug nfra-mcpmsp-r1-writer-apply: entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR present -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a2.AC2.sh; echo "exit=$?"</invocation><expect>function mcportal-grant-writer-lambda: identical=True register_tenant=True verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a2.AC3.sh; echo "exit=$?"</invocation><expect>function mcportal-grant-writer-lambda: LIVE_FIRMS=None or empty -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/NFRA_MCPMSP.TO-MS-a-2.writer-apply.proof_of_spec.json`.
Report once, with: the plan line; the previous and new code hashes; the three check lines; the ledger path; the commit
hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985); WORLD: a deploy. Checks dry-run at base: AC1 FAIL as expected; AC2
FAIL as expected (live `lambda_function.py` is byte-identical to HEAD, sha256 `ee3fd05d4e24...`, and carries no
`register_tenant` -- the check discriminates both arms); AC3 PASS as expected (`LIVE_FIRMS` absent, the C11 control).
G-FIRM later sets `LIVE_FIRMS=inflection` as its own act, on Andrew's word.

**AMENDMENT 1 (issuer, spawn precondition only):** this order runs only after MS-t-1's AMENDMENT 1 (`tenant_firm` in
`app/access_state.py` `POLICY_RECORD_TYPES`) AND MS-w-1's AMENDMENT 1 (the write through `operator_transact`) are
both merged to CLOUD, because the writer's package stages `app.access_state` from the gateway tree at build (row
Z-W3-S1). No criterion changes. Graded by: no gate limb.

<status>staged</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
