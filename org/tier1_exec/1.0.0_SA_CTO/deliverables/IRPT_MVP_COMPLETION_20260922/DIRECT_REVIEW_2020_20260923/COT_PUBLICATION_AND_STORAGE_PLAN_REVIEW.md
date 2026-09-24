# CTO direct review: native Holdings publication and Reporting storage

Measured 2026-09-23 21:36 UTC. Reviewer 1.0.0_SA_CTO. All three products remain incomplete.

## Holdings a86430e39e88e1a2cc07bf76f7f26f75d429a2a3

Bounded source/operation PASS. Five affected existing-index, null-row and failed-source controls passed in 0.62s (81 deselected) in an isolated export. An additional orchestration-only probe used the prepared snapshot with stubbed builder/writer: cutoff 2026-09-23 stays distinct from publication date 2026-09-22; selected account and 59-node schema preserved. This probe is not live publication evidence. Initial test invocation from the shared cwd emitted five passes but failed to finish; it was terminated and rerun successfully with isolated root/confcutdir. No application defect inferred from that harness behavior.

CTO independently read live AWS: opal-data-cottonwood versioning Enabled; exact current Holdings index HEAD returns 404. irpt-holdings still has CodeSha256 1XkzWP6p8OfobrSCI8ZrRCyMxfWgSK6sPZeYjdON50I=, modified 2026-09-21T15:04:24.000+0000. M's runtime gap is confirmed. Publishing alone cannot make the tab work.

Never-widen disposition under Andrew's existing implementation/adjudication authorization: M may execute the one-account initial native publication described in COT_FIRST_LIVE_OPERATION_20260923.md at this pin, for acc_d486fc9455d6b2aa18e13af1 only, retaining the actual 2026-09-22 custody date. Reviewed result is 57 positions / USD19705844.84, with seven version/hash source receipts previously independently verified at1960f42bb6. Before any write, compare the to-be-published account/date/census/value and source receipts with the reviewed preparation; a changed input or result returns for review. M may bind a prepared immutable snapshot to avoid a new source read. The existing-index refusal plus final IfNoneMatch remain mandatory. Only canonical native COT Gold/Platinum revision objects, manifest and absent current index; no broader population, scheduler, vendor call, IAM change, deletion or X10 dependency. Read back all exact versions and acceptance receipt. An ambiguous final PUT is reconciled, never blindly retried.

P supplies the already-owned Holdings package/role/environment plan; M remains accountable for authenticated API, screen, drill and reload. Native reader has no publisher/vendor permissions. Old Lambda remains NOT READY until exact runtime cutover is reviewed/applied.

## Reporting storage f4a1dd60a3

Bounded saved-plan PASS. CTO checked the actual binary plan with the repository Terraform1.9.8; default PATH1.14.5 was incompatible. Exact plan SHA256 c7639c4c06ba726a8df246c4c5742da6c70e22890940fdbbd38535c8f8329a90. Embedded reporting_storage.tf matches committed f4a1dd60a3 byte-for-byte, SHA256706270587e2eb6ce2bcb41399f283d3b5863891133fee15734ff711e6d32e873.

Plan is applyable, not errored, exactly five CREATE actions and zero changes/deletions: reporting bucket, four-axis public-access block, versioning, SSE-KMS configuration, TLS-deny bucket policy. Bucket opal-data-irpt derives from canonical PRODUCT scope; existing key7f4d3042-10d8-49a7-b55e-3c963cea8111 is reused. Per-object encryption context (bucket keys disabled), force_destroy=false and source prevent_destroy. No lifecycle deletion, principal allow, existing role change, queue/table change or runtime deployment. TLS policy ARN is unknown until bucket creation; embedded source explicitly denies non-TLS for bucket and object ARNs.

CTO disposition: P may apply ONLY this exact saved plan through existing canonical safe-apply/recording prerequisites, under the standing product implementation and CTO adjudication scope. Recheck plan digest immediately before apply; do not replan into a wider action. If state is stale, return the replacement plan. Then read back bucket location, versioning, encryption key, all four public-access controls and TLS policy; preserve apply/state/recording receipts. No report data write or policy activation follows automatically. Consumer IAM/package/Linux dependency closure and all registered enforcement coverage remain separate open work; policy remains PENDING_ENFORCEMENT. Physical disposal remains OPEN, not an invented first-thread gate.

This review does not prove any authenticated product completion or allow additional vendor use.
