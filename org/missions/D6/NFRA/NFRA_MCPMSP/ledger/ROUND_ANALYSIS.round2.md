# NFRA_MCPMSP -- ROUND-2 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~08:0xZ (site-Z fabric lead; `1.0.0_SA_CTO~O` retired by Andrew-direct ~07:4xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_CTO_O_RETIRED_CTO_Z_LEADS_SITEZ_FABRIC.md`).
**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 32531, `surprise-channel/remediations/REMEDIATION_v2.Z.md` @126e355873.
**Recut by:** `2.0.0_SA_COO~MS`, in ONE issuance.

## Round 2, as read

14 orders: 11 complete (proof_ok=11), 3 cancelled on G-MSPID (MS-sv-1, MS-rn-1, MS-rx-1). MS-dn-1 AC5 was graded PASS at
`ADJUDICATION_v2.Z.md` C-S5. ARMED 0. The infrastructure Andrew asked for on 2026-10-01 is built: *"we just want to have the
infrastructure to do so even if not fully proven"*
(`org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20261001_174xZ_OPEN_CALLS_8194_YES_MSPID_DEFER_MCPINDEX_PRIORITY.md`).

## Rulings

1. **G-MSPID stays Andrew's ACT, not a call.** The MSP calling identity is an identity he holds, and its sign-in is an MFA act. His
   word stands: "Not yet" (2026-09-30, `ANDREW_DIRECT_20260930_225xZ_NFRA_MCPMSP_MSP_CALLING_IDENTITY_NOT_YET.md`) and "doesnt matter
   right now" (2026-10-01). Nothing asks him again. The three cancelled cells, and FWD-6 and FWD-7 behind E4's record, re-cut in
   the first round after he supplies it. `MSP_CALLING_IDENTITIES` stays empty.
2. **Z-W7-S1 (safe-apply grades a plan the apply does not run) is CUT into round 3.** It is a real gate defect, reachable now, and not
   gated on G-MSPID. Owner of the remedy: this round's worker, under `2.0.0_SA_COO~MS`'s order; `1.0.0_SA_CTO~Z` stays the row's owner
   until the cell lands.
3. **Z-W4-S3 (whose identity fills `sender_email`) is CUT into round 3** as a read-first cell: one real refusal record read. Carry the
   sender args in the audit only if `user` is not the Teams sender.
4. **Z-S4 stays with `2.0.0_SA_COO~C`** (NFRA_CTLPLN's checker, the sibling of NFRA_REPORT-Z-S26). It does not hold this project.

## ENRICHMENT LIST -- round 3 (cut in ONE issuance)

| # | cell | source | done when |
|---|---|---|---|
| E1 | safe-apply's tag-authz and tombstone stages grade the apply's OWN plan (the saved planfile, or the same `-target` set), as MS-s-1 did for the naming stage | Z-W7-S1 | a targeted apply whose full-tree plan would trip a stage, but whose own plan would not, passes both stages; the reverse case is refused. Both cases run on a scratch root, with a negative control |
| E2 | read one real `asker_sender_refusal` record and settle whose identity `user` holds; carry `sender_email`/`sender_domain` in the audit args only if it is not the Teams sender | Z-W4-S3 | the record's `user` is printed beside the Teams sender of the same refusal, and `admin_refusals` shows the sender's address |

**Not in round 3:** MS-sv-1, MS-rn-1, MS-rx-1, FWD-2 (Cottonwood: G-IT-COT, G-FIRM), FWD-6 and FWD-7. All of them wait on G-MSPID.

## Act only Andrew can do (cited)

- **Supply G-MSPID**, the MSP calling identity, and sign it in (MFA). Citation: decomp G-MSPID / G-MSPCL; his 2026-09-30 and 2026-10-01
  words above. Until then the project's remaining FWDs are UNREACHABLE by any seat.

-- 1.0.0_SA_CTO~Z
