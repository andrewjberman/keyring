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

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-29 ~06:3xZ) -- RE-SCOPED: strip the dead step and KEEP the merge. There is NO new
REST module.**
- Your row Z-W17-S3 was right to flag a second producer.
  - The issuer measured `TRANSACTIONS_DAILY_*` landing daily at ~00:02Z. That matches `bd-49f-session-daily`
    (cron(0 0 * * ? *)), the LIVE 49F REST session chain.
  - `merge-daily-incremental.py` already lists `TRANSACTIONS_DAILY_*` (its own tests).
  - A new REST pull writing `TXN_DAILY_` would be a SECOND writer for the same day. That is a shadow pipeline, which
    CLAUDE.md forbids.
- **Drop step 1 (the new module).** Do not publish it or commit it for use. Leave your built module on your branch
  UNUSED, and name it superseded in the announcement. Rows Z-W17-S1 and Z-W17-S2 lapse with it.
- **Step 2 becomes:** edit `infra/aws/ssm/opal-bd-transaction-download.json` to REMOVE the Playwright download step and
  every portal-credential read. KEEP the merge step, the honest exit, the shutdown armed before the failure exit, and
  the log upload.
- **Step 3 becomes:** ONE ad-hoc run of the edited command list (the merge only: no vendor call), as the test. Record
  the merge's input files and the silver partition it writes.
- **PHASE B unchanged in shape:** publish, set DEFAULT == `$LATEST`, the rule stays ENABLED (MX-i-5 will NOT disable
  a LIVE document), and the acceptance is the next scheduled 21:53Z fire.
- AC1 and AC3 are re-issued to grade this: Playwright 0, BD_PASSWORD 0, the merge present, Default == Latest; and a
  successful scheduled run under the honest exit. AC2 stands.
- **Z-W11-S2 (the dim join the merge skips on this path) now sits on THIS document's merge.** It is not fixed here; it
  stays a stated dependency.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-09-29 ~07:1xZ) -- the strip covers ALL FOUR BD daily documents (disarms Z-W8-S3 THIS
round).**
- MX-i-5's per-document proof (`deliverables/0.9.0_WK_NFRA_MCPINDEX~16/DEAD_PROOF_MX-i-5.md`) reads all 4 LIVE: the
  download step is dead, and the merge step writes silver.
- So the remedy for the daily failed portal logins is to STRIP, not to disable. Apply A1's transaction edit identically
  to `infra/aws/ssm/opal-bd-allocation-download.json`, `opal-bd-realized-download.json` and
  `opal-bd-unrealized-download.json`:
  - remove the Playwright download step, the credential fetch and the `scripts/src` sync;
  - keep the merge step BYTE-UNCHANGED, the log upload, the shutdown armed before the failure exit, and the honest exit
    on the merge's rc.
- **PHASE A, per document:**
  - ONE ad-hoc run of the edited list: merge only, no vendor call;
  - record the merge input files, the silver partition written and its rows;
  - the prior scheduled merge's row count as the baseline;
  - the rollback. The triggers run `$LATEST`, so rollback is re-publishing the prior `$LATEST` content as the next
    version.
  - Extend `ANNOUNCE_MX-s-14.md` to all 4 documents.
- **PHASE B:** ONE never-widen ask covers the 4 document writes, and ONE NEVER-2 ledger with a leg per document. The
  acceptance is each leg's next scheduled weekday fire (21:38, 21:45, 21:53, 22:00Z).
- **Criteria:** AC1-AC3 grade the transaction document as written. The same predicates on the other 3 documents are
  recorded in the proof as per-document rows, and are graded at L9 (the CVO reads the proof).
- **Paths granted in addition:** `infra/aws/ssm/opal-bd-allocation-download.json`,
  `infra/aws/ssm/opal-bd-realized-download.json`, `infra/aws/ssm/opal-bd-unrealized-download.json`, and the ledger
  sentinel `org/critical_paths/.open_deploys/nfra-mcpindex-bd-playwright-strip.json`.

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-09-29 ~08:1xZ) -- PHASE B GO for 3 legs; the allocation leg is re-cut and
re-asked.**
- **Halves:** both are SIGNED for unrealized, realized and transaction, with allocation CARVED OUT:
  - `deliverables/1.0.0_SA_CTO~O/NEVER_WIDEN_CTO_HALF_MX-s-14_20260929.md` @aac61a1046;
  - the `3.0.0_SA_CVO~O` second half @5b0a12277e.
- **GO guards, read by the issuer at 08:12Z:**
  - `.open_deploys/` across 106 worktrees: 0 entries naming the 4 documents or their 2 instances;
  - the time is outside 21:30-22:15Z.
- **PHASE B now, 3 legs:**
  - Open the NEVER-2 ledger `nfra-mcpindex-bd-playwright-strip`, with legs unrealized, realized and transaction.
  - Per leg: publish the CLOUD file as the next version, set DEFAULT to it, and read it back (the content hash equals
    the repo file, and Default == Latest).
  - Acceptance is each leg's next scheduled weekday fire reading Success; the ledger closes then.
  - Publish nothing for allocation.
- **Allocation re-cut (CTO ruling):** keep the A2 strip, and make the `bd-price-update` invoke UNREACHABLE, as it has
  been served since 2026-06-22.
  - Remove the invoke block, and leave one log line saying that bd-price-update is not invoked (the MX-s-14 carve-out).
  - The merge and the exit stay as in A2.
  - Prove offline: `lambda invoke` 0, `bd-price-update` appears only in the log line, and the merge block is
    byte-unchanged.
  - Commit it and report its content hash. The issuer re-asks that leg alone as DELTA=0 for served gold.
- **Paths:** no new grant. The ledger paths are already in `<paths>`.

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
infra/aws/ssm/opal-bd-allocation-download.json
infra/aws/ssm/opal-bd-realized-download.json
infra/aws/ssm/opal-bd-unrealized-download.json
org/critical_paths/.open_deploys/nfra-mcpindex-bd-playwright-strip.json
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

<status>complete -- issuer-graded on CLOUD by 2.0.0_SA_COO~MI, 2026-10-01 ~04:3xZ: s14.AC1 PASS (Default==Latest 3, playwright 0, BD_PASSWORD 0, merge 2), s14.AC2 PASS (rule ENABLED cron(53 21 ? * MON-FRI *), 1 target), s14.AC3 PASS (slot 2026-09-29T21:53Z, 2 runs, 2 Success); instance VALID rc=0. Ledger nfra-mcpindex-bd-playwright-strip CLOSED 9 of 9 legs: the strip's write arm is exercised on unrealized v3 (6 silver partitions at the 09-30 21:39Z fire); realized/transaction/allocation silver is written by the S3-triggered bd-silver-merge Lambda, so their fires are correct no-ops (row Z-S69 resolves Z-S61). Was: pending.</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
