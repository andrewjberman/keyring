# NFRA_MCPINDEX task order -- `MX-s-14` -- the BD transaction daily leg is ported off the portal login to the REST pull on the 49F session (the MX-s-12 pattern); acceptance is the next scheduled 21:53Z fire

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~17</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- this order PORTS an existing schedule: EventBridge bd-transaction-pipeline-trigger cron(53 21 ? * MON-FRI *) -> Lambda bd-transactions-trigger -> SSM opal-bd-transaction-download stays the ONE producer; MX-i-5 disables the rule first, and this order re-enables it only in PHASE B on the ported document.
comp-iam: RUN -- bd-exporter-ec2-role reads blackdiamond/49f/session (MX-s-10 A5, live); no new grant is expected; a missing permission is a BLOCKING row, never a hand-added grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the pattern is ruled (MX-s-10/s-12).
EGRESS CLASS, declared: the same vendor at the same cadence, narrower (a scheduled REST read in place of a portal login). PHASE A's test run is ONE vendor call budget, logged.
</preflight>

## 1. THE CELL -- `MX-s-14` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Why.** The transaction leg has been dead since 2026-06-23: its Playwright download fails 21 of 21 at the MFA
login. Row Z-W11-S2, the skipped dim join in the transaction merge, depends on this leg producing rows again. The
round-3 analysis (item 6, R-15) ports it first. The other 3 legs follow, one per round.

The asset-dim port is the worked precedent. READ BOTH ORDERS AND THEIR AMENDMENTS:
- `NFRA_MCPINDEX.TO-MX-s-10.bd-asset-dim-schedule-rest.md` (PHASE A, A1-A6);
- `NFRA_MCPINDEX.TO-MX-s-12.bd-asset-dim-phase-b.md` (PHASE B, G1-G3).
Also read the MX-s-9 REST module: `data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py`.

### PHASE A -- no deploy
1. **The REST pull.** Write `data/black_diamond/scripts/bronze/pull_bd_transaction_rest.py` on the MX-s-9 pattern:
   - the 49F session, read-only, 49F only;
   - its names resolved at BUILD time (the MX-s-11 pin), with no `lib.opal_naming` import at run time;
   - it writes the SAME bronze transaction key or keys the Playwright leg wrote, so the downstream merge is unchanged;
   - it prints `OUTPUT_KEY=<key>` per object written.
   Find the export template for transactions from the vendor's catalog, and record the one discovery read.
2. **The document.** Edit `infra/aws/ssm/opal-bd-transaction-download.json` to run that pull instead of
   `download-daily-transaction.ts`:
   - no `BD_PASSWORD`, and no portal-credential read;
   - the honest exit, and the shutdown armed before the failure branch;
   - the log upload;
   - it stages its closure exactly as the asset-dim document does.
   Publishing the module and its closure to where the instance reads is the DS lane's safe-deploy, the MX-s-11 pattern.
3. **One ad-hoc run of the new path, as the test.** Use ssm send-command with the edited commands, not the served
   document. Record the bronze object's row count and date range, and the vendor call count.
4. Write `ANNOUNCE_MX-s-14.md` and report. The issuer asks the never-widen halves on it. DO NOT publish the document or
   re-enable the rule.

### PHASE B -- only on the issuer's GO
5. NEVER-2 ledger `nfra-mcpindex-bd-transaction-rest-schedule`. Publish the document, set it DEFAULT, and confirm
   DefaultVersion == LatestVersion: the trigger runs `$LATEST` (row Z-S48). Read back the content at `$LATEST`.
6. Re-enable `bd-transaction-pipeline-trigger` through Terraform (safe-apply). The plan changes only that rule's state.
7. The acceptance is the next scheduled 21:53Z weekday fire (AC3), never ad hoc. Record its output's `OUTPUT_KEY` and
   the bronze object's row count. Close the ledger.

## 2. BOUNDS

1. One producer before and after: no second schedule, no parallel path, no comparator.
2. Nothing under `data/cot/`. 49F only. Served gold untouched.
3. The other 3 dead legs stay DISABLED (MX-i-5).
4. No private data in the repo: counts and hashes only.
5. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
data/black_diamond/scripts/bronze/pull_bd_transaction_rest.py
data/black_diamond/scripts/bronze/_transaction_rest_pin.py
infra/aws/ssm/opal-bd-transaction-download.json
infra/aws/terraform/bd-pipeline/
infra/aws/ec2/bd-exporter/src/stepwise/download-daily-transaction.ts
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-bd-transaction-rest-schedule.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~17/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W17-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/s14.AC1.sh; echo "exit=$?"</invocation><expect>DefaultVersion==LatestVersion; at $LATEST rest-pull refs>=1 playwright refs=0 BD_PASSWORD refs=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/s14.AC2.sh; echo "exit=$?"</invocation><expect>rule state=ENABLED schedule=cron(53 21 ? * MON-FRI *) targets=1 targets bd-transactions-trigger=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/s14.AC3.sh; echo "exit=$?"</invocation><expect>successful runs at/after slot>=1; run <id>: OUTPUT_KEY lines>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~17/NFRA_MCPINDEX.TO-MX-s-14.bd-transaction-rest-port.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 6. AC3's slot keys on the PHASE B GO commit (subject token `go(NFRA_MCPINDEX.TO-MX-s-14`), which the issuer writes. Z-W11-S2 (the merge join) is a stated dependency after this, not a cell.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
