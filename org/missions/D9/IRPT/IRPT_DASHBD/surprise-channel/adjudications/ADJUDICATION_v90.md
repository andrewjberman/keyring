# IRPT_DASHBD: CVO adjudication, round 126 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T12:49Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T12:49Z, on msg 8278 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND126_B49F_DRAIN_END_20261015.md` @e9cd2d1f96, blob 54ac877520). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Two orders (DB-b-257 WORLD by its infra paths, DB-b-258 LOCAL). No judgment criterion. The orders declare five criteria. Re-run here on the landed tree: 5 of 5 PASS (rc 0). The struck DB118-3-AC3 still FAILS (rc 1), unmet. Two proof instances VALID; `round-close-check --round 126 --workstream B-49F` MAY-CLOSE (2 orders). The Cottonwood landing pair is READ here, NOT signed or adjudicated: its CTO half is the CTO's. Two ARMED rows HELD. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S27",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T12:49:00Z",
  "one_line": "Round 126 B-49F (~D2): the Cottonwood landing root made ready (DB-b-257: memory 1024, 15 members pinned and hashed, a 16-member build-only package byte-equal to sources) and the dim_return_method claim-column reader read (DB-b-258: 11 candidates, none reads a claim column; contract 0.7.0 marks the six columns carrier see_manifest, schema hash unchanged). 5 of 5 PASS re-run. Struck DB118-3-AC3: still unmet. (1) THE HAZARD ROW: yes. D2-S79 (BLOCKING, ARMED, owner ~D2) was filed after v88 and disarmed by D2-S81 in round 125, verified in v89. The pair carries the python3.12 memory gap as D2-W210-S2 (ARMED, owner ~D2). (2) THE PAIR, read only, not signed (NEVER_WIDEN_PACKET_COTTONWOOD_ACCOUNT_RETURN_DAILY_LANDING.md, sha256 c63702ade4df0b69 recomputed equal). It covers its branches: A written, B refused or held with nothing written, C dies between the two puts with a half partition the guard then blocks, D out of memory or time. It names a rollback per key: the seven resources by a safe-apply destroy with the CTO's word; the artifact as the key's first object, a listed-key delete or left; each written day by a listed-key delete of both objects with Andrew's word; the 3,325 history partitions never touched. WHAT A SIGNER WOULD BE MISSING: (a) the served side of the blast radius. Section 10 says no served reader of the new partitions is established, and the never-widen rule is about moving served output, yet no reader read (portal, ~P2 publisher, filled-report builder via the Cottonwood reader of v82) says whether Act 2 moves a served number; D2-W155-S10 (ARMED, owner ~P2) treats this prefix as a served input that is stale. (b) The writer count. CLAUDE.md asks N writers = N rules read; the packet prints one rule in scope and an operator writer whose rule it did not read and cannot exclude (section 5), so N is not settled. (c) The plan: never run (no terraform on this box); the gate is the first reading. (d) Python 3.12 memory: unmeasured; the remedy is a separate pair. (e) Branch C's remedy needs Andrew's word, so a half partition could stand blocked until he gives it. (3) ROUND 124's ledger irpt-dashbd-hop1-filled-report-values-20261015 is NOT closed. It is OPEN only on C:/dev/wk-irpt-dashbd-db2-b253 (26 worktrees read), absent from box/dell2 and origin, held open at L6 to the first scheduled fire by design; TO-DB-b-253 still reads pending on box/dell2. Rows graded: D2-W210-S1 (ARMED, owner ~D2; the layer-import advisory with no BUILD_MANIFEST) is dispositioned in D2-S83 on 'the advisory did not stop the build', which is not a ground. The ground that holds is DB122-4-AC2's staged probe, which ran the handler from its closure members alone in a clean interpreter, so accepted on that. D2-W210-S2 (ARMED, owner ~D2) stays HELD: D2-S83 calls it dispositioned, but its disarm is Act 2's Max Memory Used, which has not happened. D2-W209-S3 (ARMED, owner the CTO) is disarmable on DB-b-258's read but HELD until its owner disarms. D2-W211-S1 is INERT; D2-S82 (~C2's holdings-performance first fire) is noted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W210-S1",
   "IRPT_DASHBD-D2-W211-S1",
   "IRPT_DASHBD-D2-S83"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned or held with a live owner before the slug. CLAUDE.md never-widen: a sign-off names the act's blast radius and rollback per key, covers both branches, and first counts the writers of the property (N writers = N rules read).",
  "world_is": "Two orders complete (merges 1e78f951eb, 1e8ac2180e); nothing planned, applied, uploaded or invoked. irpt-cot-account-return-daily-lambda is still absent (ResourceNotFoundException at 12:4xZ). The Cottonwood pair's COO half is signed and its CTO half is asked. Hop 1 is live since 11:49:38Z with its ledger open on the AE branch until the first fire. DB123-3-AC3 now fails on the landed tree (it hashes the pre-1024 lambda.tf); superseded by DB126-1, and disclosed by the issuer. FWD-2, FWD-11 and FWD-21 are not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T12:4xZ: DB126-1-AC1..AC3, DB126-2-AC1, AC2 PASS rc 0; DB118-3-AC3 FAIL rc 1",
    "sha256 of org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_ACCOUNT_RETURN_DAILY_LANDING.md: c63702ade4df0b69...; its sections 5, 6, 7 and 10",
    "git worktree list (26) and ls-tree of .open_deploys/: irpt-dashbd-hop1-filled-report-values-20261015.json only on C:/dev/wk-irpt-dashbd-db2-b253; absent on box/dell2 and origin/box/dell2",
    "aws lambda get-function irpt-cot-account-return-daily-lambda: ResourceNotFoundException",
    "proof-of-spec-check VALID rc 0 on ~210, ~211; round-close-check --round 126 --workstream B-49F verdict=MAY-CLOSE orders=2",
    "investigation rows D2-S79, D2-S81, D2-W210-S1, S2, D2-W211-S1, D2-S82, D2-S83, D2-W209-S3, D2-W155-S10",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND126_B49F_DRAIN_END_20261015.md blob 54ac877520 (msg 8278)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W210-S1 dismissed on the staged-probe evidence (not on S83's stated ground). W211-S1 is inert. W210-S2 and W209-S3 stay ARMED with their owners. The pair's gaps are named for the signer; this seat does not sign it."
 }
]
```
