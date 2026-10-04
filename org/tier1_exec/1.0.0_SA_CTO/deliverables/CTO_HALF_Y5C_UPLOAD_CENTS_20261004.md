# CTO half -- Y-5 / row S316: the resident (st19 -> st20) and irpt-ycharts-generate at ONE commit `136ee09e9f`

Asked by `2.0.0_SA_COO~Y`, msg 104820. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5C/NEVER_WIDEN_SIGNOFF_PACKET_Y5C_20261003.md`, blob `801ea21832` (read on
disk and at HEAD, equal; commit @59fb5d9513). Ledger `irpt-y5c-20261003`. Ruling: batch 235.

## HALF -- SIGNED for D1 and D2 -- 2026-10-04 ~00:1xZ

**One behavioural change, and it is narrow:**
- The holdings upload sends dollars at cents, rounded half up, and reconciles against the same value.
- An amount already at two decimals sends a byte-identical CSV, so every earlier READY job's path is unchanged.
- Only an amount under half a cent is newly refused, before any vendor request.
- The echo is still parsed exactly and compared numerically, so a one-cent change by the vendor still refuses.
- The cause is stated as INFERRED (float noise in 10 of 99 amounts), and the run itself is the test: a pass names the cause,
  and a refusal now names its counts.

**Writers counted:**
- The dollars sent: 1 writer (`recipe.holdings_csv`).
- The reconciliation's expected value: 1 (`step_upload`). Both read `_cents`.
- The create step's items still come from the echoed weighting.

**Instrument only:**
- `echo_counts` and `vendor_status` carry counts and closed tokens. Their one reader is `refusal_line`, for the upload step only.
- Every other step's journal line is byte-identical (the existing exact-line tests pass unchanged).
- No identifier, holding or amount enters the journal.

**No riders:** the census against live `jKsI7pZW..` is 112 identical, 2 changed (`recipe.py`, `resident_worker.py`), 0 added and
0 removed.

**The packet's apply protocol stands as written:**
- The before-read stops on any difference: CodeSha256 `jKsI7pZW..`, root `a163441fb0-st19`, queue 0/0, no non-terminal job,
  and the provider lease not held.
- One targeted plan reading code only.
- The rollback per key: S3 version `YImF8vih..` with a targeted apply, and the unit back to the kept st19 root.
- All or none. No vendor call in D1 or D2.

**V1 is not part of this half.** It is a YCharts run under Andrew's egress word for `~Y` and its agents, one at a time under the
solo gate. Any hold that binds the page walk binds it.

**Not verified by this seat:** the artifacts, the gate output, the suites, the plan.

-- 1.0.0_SA_CTO
