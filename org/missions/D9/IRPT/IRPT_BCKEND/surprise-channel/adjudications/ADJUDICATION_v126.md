# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PJ, the release candidates: performance function and holdings bundles from HEAD)

<sweep_watermark>2026-10-15T17:54Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:54Z, on msg 8509 (the shared packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md` @9ac52f5198; this file grades ~PJ r2). Two orders, both risk SERVED, BUILD-only and read-only on AWS, complete: IB-pr-585 (the performance function's candidate, merged @5bdf4f810a) and IB-pr-589 (the holdings bundles from HEAD, merged @0237797857). Re-run here at HEAD: IB221-1-AC1..AC3 and IB222-1-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 2 --workstream "~PJ"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**IB-pr-585.** `irpt-holdings-performance-lambda` candidate `fvmE5j1h...` against live `o9UugRAV...`: 2 of 14 members differ, `holdings_performance.py` and `sources.json`, as the packet says. The packet notes the candidate is rebuilt after IB-pr-592 and the pair re-issued on the new digest, so this digest is not the one to sign.

**IB-pr-589: a bundle built from HEAD widens the release.** `IB222-1_holdings_bundles_candidate.json` (pin c5c0646241, run twice, STABLE). For each of the three firms, 8 of 46 members differ from the live bundle. Two are the intended changes (`holdings_snapshot.py`, `infra/aws/lambda/investor-reporting/holdings/publication.py`). The **SIX drifted members**, changed since the minting pins by other projects, are:
1. `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`
2. `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`
3. `data/mdpf/scripts/gold/mdpf_category_registry.py`
4. `infra/logic/registry/exemptions.json`
5. `infra/logic/registry/reporting_policies.json`
6. `lib/opal_naming.py`

That finding stopped this approach. It is carried in v127 and on `D2-S206`. Note that the live bundles read in this record (49F `bce6e936...`, Cottonwood and Inflection `02487ed9...`) are the IB-pr-549 mint, whose version ids the worker matched to the mint record (3 of 3). They are no longer the v118 bundles.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S34",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:54:00Z",
  "one_line": "~PJ r2. Performance candidate fvmE5j1h differs from live o9UugRAV in exactly 2 of 14 members (holdings_performance.py, sources.json), to be rebuilt after IB-pr-592. The holdings bundles built from HEAD change 8 of 46 members per firm: 2 intended (holdings_snapshot.py, publication.py) and SIX drifted from other projects (dim_mdpf_aggregate_aua_timeseries.py, dim_mdpf_aum_metrics.py, mdpf_category_registry.py, registry exemptions.json, registry reporting_policies.json, lib/opal_naming.py), so a HEAD build is not the exemption alone. 6 of 6 criteria PASS re-run; build-only. Dismissed (5): D2-W427-S1, -S2, D2-W428-S1, -S2, -S3 (readings; S3 is the drift itself, carried on D2-S206).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W427-S1",
   "IRPT_BCKEND-D2-W427-S2",
   "IRPT_BCKEND-D2-W428-S1",
   "IRPT_BCKEND-D2-W428-S2",
   "IRPT_BCKEND-D2-W428-S3"
  ],
  "spec_asserts": "Never-widen (CLAUDE.md section 5): a release names its blast radius; CLAUDE.md rule 22a: compare the built bundle to the live bytes by content.",
  "world_is": "No candidate here is signable: the performance digest will be rebuilt, and the HEAD-built holdings bundles carry six unrelated members. Nothing was deployed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:4xZ of the invocations in IB-pr-585 and IB-pr-589: IB221-1-AC1..3, IB222-1-AC1..3 PASS, exit 0 each; round-close-check ~PJ round 2 MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~428/IB222-1_holdings_bundles_candidate.json: per firm members_total 46, changed_members 8 (listed), determinism STABLE",
    "investigation rows D2-W427-S1..S2, D2-W428-S1..S3, D2-S206",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md @9ac52f5198 (msg 8509)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build readings; the drift they found is carried by D2-S206 and graded in v127."
 }
]
```
