# TO IRPT_BCKEND.TO-IB-pr-350 -- back-fill covered_account_ids into the export receipts written before IB-pr-343, so existing exports read again within scope (PRD v0.30 item 35), laptop applier, after IB-pr-349

<to_id>IRPT_BCKEND.TO-IB-pr-350</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~I</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (the applier is a laptop seat; the issuer is on dell2) | **Ordered by:** the CTO half of
IB-pr-343's emergency release ("existing exports stay refused until the v0.30 back-fill, which you cut next under its own pair", msg
576) | **Decomp cell:** `IB-pr-350` (decomposition section 62) | **outcome_ref:** FWD-2 | **depends_on:** IB-pr-349 (run this order
only after IB-pr-349's ledger is closed and not rolled back).

---

## WORKER FACE

**Why.** After IB-pr-349, a receipt that names no account is refused on read. Receipts written before IB-pr-343 name none, so every
existing export is unreadable until it is back-filled. IB-pr-344 built the tool,
`infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py`. Its dry run on dell2 listed **1** receipt (49financial)
and could not read it: the object is SSE-KMS and dell2 lacks kms:Decrypt (row W145-S5). The cottonwood listing read 0 objects. The
census is in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~145/IB65-2_backfill_census.json`.

**This order runs in TWO passes.**

**Pass 1 (now, read-only).**
1. Check that IB-pr-349 is closed and not rolled back. If it is not, STOP: this order waits for it.
2. From the published branch carrying this order, run
   `python infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py --dry-run --census-out <your deliverables>/IB69-1_backfill_dry_run.json`
   under an identity that can decrypt the receipts. Pass `--bucket` as the evidence bucket that `irpt-export-render` reads: read its
   `IRPT_EVIDENCE_BUCKET` from the live function configuration. Print the identity (`sts get-caller-identity`, ARN only).
3. Write a packet, `<your deliverables>/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-350.md`. It holds:
   - per firm: receipts listed / filled / unfillable / denied;
   - for each FILLED receipt: its export id and the COUNT of accounts derived (never raw numbers);
   - the S3 version id of each receipt before the write: that is the rollback source;
   - the writers of these objects (the export function and this tool), and which firm each receipt belongs to;
   - both branches. Written: the receipt reads again for a principal whose scope covers its accounts, and is still refused for one
     whose scope does not. Rolled back: the receipt is refused as now.
4. Commit and STOP. Report the packet's `blob <hash>`. The halves are signed against that blob:
   `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_350_*` and `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_350_*`.

**Pass 2 (only when BOTH halves are at the published HEAD naming the packet blob).**
1. Open a change-management ledger entry and commit its `.open_deploys` sentinel.
2. Re-run the dry run. Its counts must equal the packet's, or STOP.
3. Run `--apply` with the same arguments.
4. Re-read every written receipt: each names a non-empty `facts.covered_account_ids`.
5. Read one back-filled export through the DEPLOYED bytes of `irpt-export-render`, the way IB-pr-349 proved its controls:
   reconstructed headers for an Opal principal whose scope covers it (it is ADMITTED, and the function's own
   `irpt_export_read_admitted` line is emitted) and for an out-of-scope principal (it is REFUSED). Mint no token and write
   nothing to the auth plane (AMENDMENT 1, row S382).
6. Close the ledger and commit it.
7. Write `<your deliverables>/IB69-1_backfill_after_reads.json` with the keys `mode` ("apply"), `receipts_listed`, `filled`,
   `unfillable`, `already_named`, `would_write`, `wrote`, `denied`, `rewritten_reread_ok`, `backfilled_read_admitted`,
   `admitted_read_log_lines`, `halves_present`, `rollback_versions` and `limits`.

**Rollback:** restore the receipt's prior version (copy the version id from the packet onto the key). Opaque ids only.

<criterion id="IB69-1-AC1" cell_refs="IB-pr-350"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r69/p69_cells.py" . IB69-1-AC1</invocation><expect>IB69-1-AC1 PASS</expect></criterion>
`IB69-1-AC1` -- after the apply: 0 denied, the counts reconcile, every written receipt re-reads with a non-empty list, and a back-filled
export is admitted for an in-scope Opal principal. Base: FAIL (no file). After pass 1 it stays FAIL, and that is expected: the order
stays open at the halves.

<expected_criteria>IB69-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder, and nothing else.
- **No write before both halves,** and none except `--apply` of this tool on the receipts the packet names. No other S3 key, no
  bundle, no artifact, no `pending.json` is written.
- **No code, IAM, route or function change.** The tool runs from your checkout, not deployed.
- **The firm boundary:** each receipt is filled only from its own firm's bundle and pointer (the tool's derivation). A receipt
  whose derivation crosses firms is a STOP and a row.
- **No vendor call.** No call off Opal infrastructure. No monitor, alarm, SNS or SES send.
- **Refusal clause.** A count that moves between the packet and the apply-time dry run, a denied receipt at apply time, or a name,
  email or raw account number in any file: STOP, file a row, write nothing.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-350.backfill-covered-accounts-into-existing-receipts.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~I/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 62 (round 69, workstream ~P), cell `IB-pr-350`.
<owned_cells>IB-pr-350</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: IB69-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~I/IRPT_BCKEND.TO-IB-pr-350.backfill-covered-accounts-into-existing-receipts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete (pass 2 only).
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P2` per pass: the commit hashes, the packet's `blob <hash>` (pass 1), or IB69-1-AC1's last
line and the ledger entry (pass 2), and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- IB-pr-344's dry run listed 1 receipt across 2 firms (49financial 1, cottonwood 0); the write set is the FILLED receipts the pass-1 packet names, each with its prior version as rollback.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added; the applier's existing identity reads and writes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB69-1-AC1 dry-run at base 2026-10-07 ~13:3xZ: FAIL as expected (no after-reads file).
lane: the <paths> block IS the grant.
</preflight>
