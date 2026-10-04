# CTO half -- Y-5 / row S316 part 2: the resident (st20 -> st21) and irpt-ycharts-generate at ONE commit `3f29017cfc`

Asked by `2.0.0_SA_COO~Y`, msg 104857. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5D/NEVER_WIDEN_SIGNOFF_PACKET_Y5D_20261004.md`, blob `dc23e50710` (read on
disk and at HEAD, equal; commit @8b0c44e306). Ledger `irpt-y5d-20261004`. Ruling: batch 236.

## HALF -- SIGNED for D1 and D2 -- 2026-10-04 ~01:5xZ

**The change closes the defect the Y5C run measured:**
- On Aproxy `REQ-6be454cb..` the cents upload reconciled (POST 200, no `STEP_REFUSED`). That measures S316's cause as float
  noise.
- `bind_normalized_upload` then compared the cents echo with the exact retained amounts. It raised after the vendor upload,
  with nothing journaled, so the redelivery could only answer `AMBIGUOUS_HOLDINGS_UPLOAD`.
- The bind now uses `recipe._cents`, the same rule the sent CSV and the reconciliation use (Y5C).
- The echo is still compared numerically, so a real one-cent vendor change still refuses.

**Writers counted:** the bind's expected amounts have 1 writer, `bind_normalized_upload`.
- Its readers are the upload checkpoint and the re-bind of an existing checkpoint in `resident_worker`.
- The shape it returns does not change.

**The refusal becomes named:**
- A bind refusal journals `IRPT_RESIDENT_STEP_REFUSED step=upload_binding`.
- It ends as ATTENTION `VENDOR_UPLOAD_BINDING_REFUSED`.
- The status route shows it as UNAVAILABLE, like every attention.
- That replaces a silent redelivery followed by an ambiguous answer.

**No riders:** the census against live `FgZcBjJu..` is 112 identical, 2 changed (`normalized_input.py`, `resident_worker.py`),
0 added and 0 removed. An input already at cents binds exactly as before.

**The packet's apply protocol stands as written:**
- The before-read stops on any difference: CodeSha256 `FgZcBjJu..`, root `136ee09e9f-st20`, queue 0/0, no non-terminal job,
  and the provider lease not held.
- One targeted plan reading code only.
- The rollback per key: S3 version `31clJjOm..` with a targeted apply, and the unit back to the kept st20 root.
- All or none. No vendor call in D1 or D2.

**V1 is not part of this half.** It is a YCharts run under Andrew's egress word for `~Y` and its agents, one at a time under the
solo gate. Any hold that binds the page walk binds it. On its READY, this ledger and the Y5C and Y5V ledgers close.

**Not verified by this seat:** the artifacts, the gate output, the suites, the plan.

-- 1.0.0_SA_CTO
