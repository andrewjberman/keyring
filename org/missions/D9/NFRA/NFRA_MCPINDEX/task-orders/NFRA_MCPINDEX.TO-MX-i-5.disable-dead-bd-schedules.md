# NFRA_MCPINDEX task order -- `MX-i-5` -- the 4 dead BD Playwright schedules are DISABLED (never deleted), each first PROVEN dead (R-15; row Z-W8-S3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-i-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~16</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- this order DISABLES 4 existing EventBridge rules (bd-allocation-pipeline-trigger cron(0 22), bd-realized-pipeline-trigger 21:45, bd-transaction-pipeline-trigger 21:53, bd-unrealized-pipeline-trigger 21:38 -- all ENABLED at the analysis ~04:2xZ); it adds none. Not touched: bd-asset-dim-pipeline-trigger (the negative control), bd-allocation-file-check-daily, every bd-49f-* rule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or secret changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is ruled (R-15) and signed by two never-widen halves before the apply.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3/SSM/EventBridge reads, Terraform).
</preflight>

## 1. THE CELL -- `MX-i-5` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Why.** Four BD daily legs (allocation, realized, transaction, unrealized) still run the Playwright portal download.
Each reads `opal/bd/credentials` and fails at the MFA-broken login, 21 of 21 retained runs each (MX-m-1 (a)). That is
about 4 failed logins per weekday, and the lockout risk is unmeasured. The CTO ruled R-15: **disable, never delete**.
Read R-15 in the analysis.

### PHASE A -- prove dead, no change
1. **Dead proof, per leg, two grains.** Write `DEAD_PROOF_MX-i-5.md` in your deliverables. Each leg gets a section
   headed exactly `## <rule-name>` (the 4 rule names above), holding:
   - (i) the SSM-run grain: the last N retained runs of its document at `--document-version $LATEST`, with SSM Status
     and the log outcome beside each. N is printed.
   - (ii) the S3 log-object grain: the method that reproduced Z-S47's 69 of 121 (the latest version per log key).
     Print `FIRST_FAILING: <date>` and `LAST_NON_FAILING: <date>`.
   - The leg's OWN output prefix, found from the document: count the objects written since LAST_NON_FAILING and print
     `OUTPUT_SINCE_LAST_NON_FAILING: <n>`, with the prefix and the denominator.
   - **A leg with ANY output since its first failure is NOT dead.** Do not disable it. File a row and report it.
2. **The Terraform change.** In the bd-pipeline Terraform, set each proven-dead rule's state to DISABLED, e.g.
   `state = "DISABLED"` or `is_enabled = false`, whichever the provider version uses. Delete nothing.
   - `terraform init`, then `terraform plan -no-color -out=<file>`; save `terraform show -no-color <file>` as
     `PLAN_MX-i-5.txt` in your deliverables.
   - The plan must read `0 to add, 4 to change, 0 to destroy`, and all 4 changes must be those rules.
3. Write `ANNOUNCE_MX-i-5.md`: the proof table, the plan's resource list, and the rollback per rule (re-enable that one
   rule's state, then safe-apply). Commit and report. DO NOT APPLY.

### PHASE B -- only on the issuer's GO (both never-widen halves SIGNED)
4. NEVER-2 ledger `nfra-mcpindex-bd-dead-legs-disable`: open it and commit it before the apply.
5. Apply with `.tools/safe-apply.sh`, using the saved plan. Then `terraform plan -detailed-exitcode` returns 0.
6. Read back the 4 rules DISABLED and `bd-asset-dim-pipeline-trigger` ENABLED (AC1). Close the ledger.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-29 ~06:3xZ) -- "dead" is proven per DOCUMENT, across EVERY step.**
- Measured by the issuer: `opal-bd-transaction-download` runs the Playwright download and THEN
  `merge-daily-incremental.py` (document :46-48). The merge reads `forwardfill_v2/transactions/TRANSACTIONS_DAILY_*`,
  which a LIVE REST producer on the bd-49f session chain writes daily at ~00:02Z. Disabling that trigger would stop
  served silver transactions.
- For each of the 4 documents, list every step in its section as
  `STEP <n> | <what> | output prefix | writes since: <count since LAST_NON_FAILING>`, and name any input another
  producer writes.
- Each section carries `VERDICT: DEAD` (no step writes live output) or `VERDICT: LIVE (step <n> writes <prefix>)`.
- **Only DEAD documents' rules are disabled.** The plan reads `0 to add, N to change, 0 to destroy`, where N is the
  number of DEAD verdicts. A LIVE document's rule is NOT touched.
- AC1-AC3 are re-issued to grade exactly this (see the round-4 battery). The transaction leg is expected to read LIVE.
- Removing a LIVE document's dead Playwright step is MX-s-14's pattern (strip, keep the merge). It is not this cell's.

## 2. BOUNDS

1. Only the 4 named rules' enabled state. Nothing is deleted: no rule, target, Lambda or SSM document.
2. `bd-asset-dim-pipeline-trigger` and every `bd-49f-*` rule are never touched.
3. The secret `opal/bd/credentials` is untouched; rotation is Andrew's.
4. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/terraform/bd-pipeline/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-bd-dead-legs-disable.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~16/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W16-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-i-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/i5.AC1.sh; echo "exit=$?"</invocation><expect>dead-leg rules DISABLED 4 of 4; negative control bd-asset-dim-pipeline-trigger=ENABLED -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-i-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/i5.AC2.sh; echo "exit=$?"</invocation><expect>plan summary line present>=1; changed resources 4, of which aws_cloudwatch_event_rule 4 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-i-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/i5.AC3.sh; echo "exit=$?"</invocation><expect>dead-proof sections complete 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~16/NFRA_MCPINDEX.TO-MX-i-5.disable-dead-bd-schedules.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 1; R-15 disarms Z-W8-S3 THIS round. Dry-run at base: i5.AC1 FAIL (0 of 4 DISABLED; the control ENABLED), i5.AC2 FAIL (no plan), i5.AC3 FAIL (no proof). MX-s-14 later RE-ENABLES bd-transaction-pipeline-trigger only in its own PHASE B, on the ported document.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
