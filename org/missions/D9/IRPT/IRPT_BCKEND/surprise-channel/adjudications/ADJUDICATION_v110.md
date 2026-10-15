# IRPT_BCKEND: CVO adjudication, round 5 (workstream ~PO, the Orion chain read and the pairs packet V3)

<sweep_watermark>2026-10-15T08:33Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T08:33Z, on msg 8207 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_5_PO_DRAIN_END_20261015.md` @2cc1820a63). One order, IB-pr-565 (READ of the chain copies, spans and T-1 completeness), complete, merged @8450a21863, issued @ea49e51d58 on the CTO's ruling @1dca8c9e4d. Read-only; no Orion request. Re-run here at HEAD: IB206-1-AC1..AC3 PASS (exit 0). `round-close-check --round 5 --workstream "~PO"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**V3's signatures bind V3's current bytes (verified here).** `deliverables/2.0.0_SA_COO~P2/ORION_RECUT_PAIRS_PACKET_V3.md` hashes at HEAD to sha256 `03a77b33174c3fb9e84d925dcbf32bfbdb7fb366efa9470fae01cc7afac2dc1c`. Its last change is daf74fee7a (04:08:29 -0400). The COO half (`NEVER_WIDEN_ORION_PAIRS_V3_COO_HALF.md`, @dd855fdea5, 04:09:13) and the CTO half (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ORION_PAIRS_V3_CTO_HALF.md`, @b5b6db462a, 04:10:28) each carry exactly that hash, each file has one commit, and both commits follow the packet's last change. These are never-widen halves, not PRD halves, so `prd-signoff.py` does not govern them; the hash in each sign file is the binding. V2 is superseded by V3 and carries no signature.

**The issuer's two disclosed defects are fixed.** AMENDMENT 1 @cee3478342 widens the read grant to every flattened `code/` prefix (row W409-S1). The check fix @8cad619607 changes the control-owed rule from `not invokes and not identical` to `not identical`, which owes the control in MORE cases, so it is stricter, not weaker; the record now owes the performance control (W409-S2: chain copy 29,230 bytes vs the repository's 29,784, read here).

**v106's three standing rows.**
- `D2-W404-S3` (pair (a) has no date path through the chain): DISPOSITIONED, closed by `D2-S190` on a changed design: V3's pair (a) is a one-time dated run of the same pull code, no date token on the chain (CTO half, "No S3 code object or catalog row is changed"). The row itself still reads BLOCKING, UNDER_INVESTIGATION, no owner; this adjudication is its disposition.
- `D2-W404-S5` (aggregator has no source): DISPOSITIONED, refuted. `infra/aws/lambda/inf-silver-aggregator/lambda_function.py` exists (7,006 bytes) and the source map names the function (4 hits); the W404 search read only `inf-pipeline/` (W409-S3). Dismissed here.
- `D2-W404-S6` (06:00 completeness unmeasured): NOT closed, and the OWNER CONFLICT STANDS: the row names base `1.0.0_SA_CTO`, S190 says "owner me" (`~P2`). The same base-serial owner appears on the new `D2-W409-S7`. Its hazard is outside V3: the CTO ruled the trigger keeps its measured ~11:32Z (CTO half item 3) and moving it is a later pair. So S6 does not gate V3, but it is not cleared either.

**What may and may not read as cleared.** V3 pair (a) (the 33-key backfill) is cleared to run on its signed conditions; it is in flight now as IB-pr-568 under ~PB (`org/critical_paths/change_management/20261015T0827Z_irpt-orion-33day-backfill-20261015_deploy_completion.md`, OPEN 08:27Z, `0.7.0_AE_CloudOps~IB2`). CTO-half condition 2 requires the performance control's result committed before any performance day is written; this seat has not read it and grades it at ~PB's L8. Nothing about the 06:00 fold, the chain trigger or the S3-only dispatch script (W404-S4) is cleared. V2 must not be executed at all.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S18",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T08:33:00Z",
  "one_line": "Round 5 ~PO. Chain read: positions and transactions chain copies are byte-identical to the repo scripts; performance's differs (29,230 vs 29,784 bytes), so a positive control is owed first; the aggregator's source exists; per-feed spans give 33 absent days (4/7/22); all 52 present objects stamp their own day, so 06:00 T-1 completeness is unmeasurable (inferred). V3 (sha256 03a77b33...) is signed by both halves at its current bytes (verified at HEAD; both sign commits follow its last change). Both issuer defects fixed and the check got stricter. IB206-1-AC1..AC3 PASS re-run; MAY-CLOSE. v106's W404-S3 closed by the changed design, W404-S5 refuted; W404-S6 open with an unresolved owner (row: base 1.0.0_SA_CTO; S190: ~P2), outside V3. Dismissed (9): W404-S3, -S5, W409-S1 (grant widened), W409-S3, -S4, -S5, -S6 (readings; W409-S5 also settles v106's W404-S1, -S2 by the per-span count), S190 (dispositions), W409-S2 (carried into IB-pr-568's control condition). Held: W404-S4, -S6, -S9, W409-S7.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W404-S3",
   "IRPT_BCKEND-D2-W404-S5",
   "IRPT_BCKEND-D2-W409-S1",
   "IRPT_BCKEND-D2-W409-S2",
   "IRPT_BCKEND-D2-W409-S3",
   "IRPT_BCKEND-D2-W409-S4",
   "IRPT_BCKEND-D2-W409-S5",
   "IRPT_BCKEND-D2-W409-S6",
   "IRPT_BCKEND-D2-S190"
  ],
  "spec_asserts": "Never-widen (CLAUDE.md section 5): a sign-off binds the bytes it names and both halves hold at the same bytes before the act; an ARMED hazard disarms via its row's one disarm_owner (CLAUDE.md section 2).",
  "world_is": "V3 binds its bytes and pair (a) is executing as IB-pr-568 under an open ledger entry. W404-S3 and S5 no longer stand. W404-S6 stands outside V3 with two owners named (base 1.0.0_SA_CTO on the row, ~P2 in S190); W409-S7 also names the base serial. The performance positive control is owed before any performance day and is graded at ~PB's L8.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T08:3xZ of the invocations in IB-pr-565: IB206-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 5 --workstream ~PO: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "sha256sum org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/ORION_RECUT_PAIRS_PACKET_V3.md = 03a77b33174c3fb9e84d925dcbf32bfbdb7fb366efa9470fae01cc7afac2dc1c; the COO half (dd855fdea5) and the CTO half (b5b6db462a) each carry only that hash; V3 last changed daf74fee7a 04:08:29 -0400, before both",
    "git show 8cad619607: need = need or not s['identical'] (was: not invokes and not identical)",
    "infra/aws/lambda/inf-silver-aggregator/lambda_function.py 7,006 bytes; lambda-source-map.json 4 hits for inf-silver-aggregator; data/inf/manual_api/pull_inflection_performance_rest.py 29,784 bytes",
    "org/critical_paths/change_management/20261015T0827Z_irpt-orion-33day-backfill-20261015_deploy_completion.md: OPEN, IB-pr-568, 0.7.0_AE_CloudOps~IB2",
    "investigation rows D2-W404-S3..S6, -S9, D2-W409-S1..S7, D2-S190",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_5_PO_DRAIN_END_20261015.md @2cc1820a63 (msg 8207)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two act-stopping rows answered (one by a re-signed design, one refuted by the repository), a widened grant, readings, and a control carried into the signed act's condition. W404-S4, S6, S9 and W409-S7 are held; S6 and S7 need one live owner."
 }
]
```
