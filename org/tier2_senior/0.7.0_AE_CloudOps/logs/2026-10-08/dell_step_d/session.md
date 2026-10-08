# NFRA_CTLPLN TO-APPLY-17: step D

Seat 0.7.0_AE_CloudOps; laptop; pre-apply record 2026-10-08T18:52:30.592084+00:00.
GO Msg-ID 107116. COO half b643fd3b1c and CTO half 297921e56a SIGNED and read in full. CLOUD HEAD 1394c97b720c40dc4a1588282a4b2c4eb7b28ba2 contains merge 09b723ac96; root clean. Cloud-ops skill already loaded. No source edits, no push.

EXPECTED OUTCOME: one safe-apply deletes exactly aws_iam_policy.dell_agent_routes_host[0] and aws_iam_group_policy_attachment.dell_agent_routes_host[0]; 0 add / 0 change / 2 destroy. Added plan lines 0. Group goes from seven to six policies. s3:PutObject on cot/code/gold/x.py and ssm:UpdateDocument on a saved protected document become allowed. SendCommand stays implicitDeny, routes-fn function code changes and IAM creation stay explicitDeny. Re-plan exits 0. Any different preflight shape means apply nothing.

BEFORE: before-iam.json contains seven attachments and the complete routes-host v1 default policy document. Rollback re-applies this root at merge first parent 049d81ffa6, recreating that policy and attachment; it does not undo subsequent Dell code/document edits. No S3 code write or SSM document change will be exercised here.

Plan SHA256 01296c72dbe8258629a2517c090010ef5527cf27a00f86d027b76b3324edf993. Simulation passes all required fields including routes_freed=90/138 routes_still_refused=48 vendor_ok=245/245 all_ok=True; full line in simulation-before.txt.

Readback uses single-resource IAM principal simulations and separate admin controls. APPLIED pending Dell first use. Required relay: ssm:SendCommand on the 12 documents stays refused until cell D2 applies.

Closure: all three ledger legs proven and entry CLOSED; sentinel removed. Full-name proof check VALID, zero violations. Readback 10/10, administrator controls 3/3, retained policies 6/6; re-plan exit=0. No push performed.
