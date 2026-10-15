# CTO ROUND-124 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): the hop-1 apply (2026-10-15 ~16:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8460, ADJUDICATION_v93 @b0828d159a, MAY-CLOSE.
**No PRD addendum.** Issuer: `2.0.0_SA_COO~D2`.

- **Applied, not yet proven.** Live equals Terraform: 8192 MB, timeout 900, 11 sids, and the schedule is unchanged (cron 41 7 MON-FRI New York).
  There have been 0 invocations since the apply, and `filled_report_values` holds 0 objects.
- **The proof is the first scheduled fire, Friday 2026-10-16 at about 11:41Z.** That is a trading day, and its answer is Thursday's (T-1).
  - The read after that fire is the round's one remaining act, not a new cell.
  - It reads the invocation's result and the `filled_report_values` objects it wrote, with the count and keys printed against the signed
    hop-1 half (sha 2f25b84dc85c).
  - The read grades DB118-3-AC3. On PASS, the ledger closes. On a failure, the rollback in the signed half runs (the 10-13 artifact
    version, policy reverted to 7), and the failure comes back as a row.
- Any later partition delete stays a listed-key delete on Andrew's word. Nothing in this round needs one.
- **The L3 enrichment is unchanged** (the round-121 and 123 analyses). It is cut only after this proof reads PASS.

-- 1.0.0_SA_CTO~DELL2
