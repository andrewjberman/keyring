# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PL, the anatomy of 49 Financial's remaining refusal)

<sweep_watermark>2026-10-15T17:54Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:54Z, on msg 8509 (the shared packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md` @9ac52f5198; this file grades ~PL r1; v126, v127 and v128 grade ~PJ r2, ~PJ r3 and ~PN r1). One order, IB-pr-584 (risk SERVED, read-only), complete, merged @945ecc8f88, amended once @d911b8752f (adds the cause split; states its gate limb). Re-run here at HEAD: IB220-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PL"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**(1) "Our join", with the record's own denominators.** `IB220-1_49f_refusal_anatomy.json`, candidate 2026-10-14 against served 2026-10-12, firm 49financial, claim measured. The method was a read-only in-process build of HEAD over the live pinned inputs, with an S3 client restricted to get/head/list. The two arms, WITHOUT and WITH the exemption provider, were run on deep copies of one build.
- `account_lost`: **1 of 7,640** served accounts after the exemption. Lost accounts total 2: 1 exempted absent_at_source (the v116/v117 account) and 1 `in_source_with_positions`. Cause split: join 1, source 0, undetermined 0.
- `classified_security_lost`: **4 of 1,839** served placed securities (all equity in the served placement). Cause split: join 4, source 0, undetermined 0. The candidate carries 23 unclassified securities against 19 in the served publication.

So both remaining conditions are ours: the source carries the item and our candidate drops it or leaves it unclassified. **S203's owner does not yet have an order for it.** D2-S203 (ARMED, `2.0.0_SA_COO~P2`) carries the hazard, and the packet says "the CTO rules the remedy per cause class". The task-order folder lists IB-pr-592, 594, 595 and 596, none of which is the 49F join remedy. The next act is the CTO's ruling, then an order.

Two held rows. `D2-W426-S2` (ARMED, `~P2`): the check's AC2 would count a closed-directory account as remaining and so could FALSE-FAIL a correct record. It is latent here (`closed_by_directory` 0) and not fixed by AMENDMENT 1. `D2-W426-S3` (ARMED, `~P2`): the build module prints a ticker identifier to the console for each security it cannot classify, so a counts-only harness puts identifiers on screen. That is a client-data hygiene item for the module's owner.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S33",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:54:00Z",
  "one_line": "~PL r1. 49 Financial's remaining refusal is ours (record, measured): account_lost 1 of 7,640 served accounts (in source with positions, join), classified_security_lost 4 of 1,839 served placed securities (join 4); source 0, undetermined 0. S203 (ARMED, ~P2) carries it; NO order exists yet for the remedy (the CTO rules per cause class). IB220-1-AC1..AC3 PASS re-run. Dismissed (1): D2-W426-S1 (a file-name premise). Held: D2-W426-S2 (latent false-fail in the check), D2-W426-S3 (identifiers printed to console by the build module), D2-S203.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W426-S1"
  ],
  "spec_asserts": "CTO round analysis @57266eeb77 (msg 8435): the refusal's anatomy with denominators and a cause split; spine L10: an armed hazard has an owner and a next act.",
  "world_is": "49 Financial stays served at 2026-10-12. Its block is two join failures in our own build (1 account, 4 securities); the custodian is not the cause. The remedy needs the CTO's per-class ruling and an order.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:4xZ of the invocations in IB-pr-584: IB220-1-AC1..3 PASS, exit 0; round-close-check ~PL round 1 MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~426/IB220-1_49f_refusal_anatomy.json: conditions_detail account_lost tripped 1 denominator 7640 join 1; classified_security_lost tripped 4 denominator 1839 join 4; lost_accounts total 2, exempted 1, remaining 1",
    "task-orders listing: IB-pr-592, 594, 595, 596 (no 49F join remedy)",
    "git show d911b8752f (AMENDMENT 1, the cause split; gate limb stated)",
    "investigation rows D2-W426-S1..S3, D2-S203",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md @9ac52f5198 (msg 8509)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A file-name premise. The refusal itself, the check's latent false-fail and the console identifiers stay held with ~P2."
 }
]
```
