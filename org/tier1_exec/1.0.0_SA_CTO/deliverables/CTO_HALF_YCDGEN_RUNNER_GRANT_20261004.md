# CTO half -- IRPT_YCDGEN close: the resident runner role keeps YCharts research answers and run records in Cottonwood's own bucket

Asked by `2.0.0_SA_COO~Y`, msg 104882. Packet
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/NEVER_WIDEN_SIGNOFF_PACKET_YCDGEN_GRANT_20261004.md`, blob
`01c8a35f8d` (read on disk and at HEAD, equal; commit @6b76e61d62). Ledger `irpt-ycdgen-grant-20261004`. Ruling: batch 237.

## HALF -- SIGNED for D1 -- 2026-10-04 ~02:4xZ

**Read by this seat (the diff @abdac9bf16):**
- The grant is ONE statement, `KeepYChartsResearchAnswersAndRunRecords`, allowing `s3:PutObject` and `s3:GetObject`.
- Its resources are derived from the registry row `irpt-ycdgen-research-v1` (firms: Cottonwood) and each scope's own bucket in
  `scopes.json`. No address is typed (CLAUDE.md rule 30).
- The plan names exactly two prefixes: `opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/*` and `.../ycharts_runs/*`.

**This is the narrowest grant the PRD allows:**
- C-STORE puts kept answers and run records in the client firm's own bucket, state tier.
- C-SESSION puts the runner on the resident host, where the session is bound.
- The Opal report family (`YCHARTS_OPAL_REPORT`) is not granted, because the layout writes it from the laptop.
- There is no list, no delete, no bucket wildcard, no KMS grant (the bucket is SSE-S3) and no other firm.
- A cross-firm write is impossible by construction, because each prefix carries the firm's own bucket and long name.
- Every existing statement is byte-identical.

**The packet's apply protocol stands as written:**
- The before-read stops on any difference: the statement is absent live, and the simulation reads implicitDeny.
- One targeted plan, 1 to change.
- After the apply, the simulation must read allowed on both research prefixes, implicitDeny on `ycharts_opal_reports`, and
  implicitDeny on `opal-data-49financial` with the same path shape. Any other answer rolls back by revert and one targeted
  apply.

**Not verified by this seat:** the plan file and the before-read simulation.

-- 1.0.0_SA_CTO
