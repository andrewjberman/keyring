# IRPT_BCKEND: CVO adjudication, round 195 (workstream ~P)

<sweep_watermark>2026-10-14T17:06Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T17:06Z, on msg 7763 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_195_P_DRAIN_END_20261014.md`). One order (IB-pr-539, the live-against-pin differential), read-only, 3 of 3 PASS re-run here; no judgment criterion. 4 rows dismissed below. HELD: D2-W384-S1 (BLOCKING, ARMED, owner 2.0.0_SA_COO~P2). This seat confirmed it at the pin: `_IRPT_HOLDINGS_CLOSURE` in `.tools/safe_deploy_core.py` @49467335d2 lists build_cottonwood_mdpf_slice.py and opal_strategy_matcher.py and not opal_unidentified.py, which the slice builder imports at lines 132/136. So a pin mint crashes Cottonwood, and every measurement so far ran on the repo tree, not the bundle. HELD: D2-W384-S3 (Cottonwood's 236 beyond-rule changes are measured and attributed to the member, but not to a commit). ARMED unchanged: D2-W349-S1, D2-W361-S1, D2-W348-S2, D2-W368-S2, D2-S158.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S4",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T17:06:00Z",
  "one_line": "Round 195 ~P. IB195-1-AC1..AC3 PASS re-run here. The differential is measured: 32 / 485 / 841 SECURITY nodes; 49financial and Inflection are the signed cash rule only; Cottonwood has 236 beyond it (basis 236, sub_asset_class 51, 45 become absent), reproduced by the holdings_snapshot.py swap alone and attributed to no proven commit. Confirmed here: the pin's bundle closure lacks opal_unidentified.py, which the Cottonwood builder imports, so a Cottonwood bundle minted from the pin raises ModuleNotFoundError (D2-W384-S1). Dismissed (4): D2-W384-S2 (Inflection REFUSED on both codes because the served frontier moved to 2026-10-13; a gate comparison must be live against pin at the same served state, carried to packet v4), D2-W384-S4 (python -I wrote __pycache__ into scratch trees, outside the repo), D2-S174 (the issuer's cross-read, equal to the worker's counts), D2-S175 (the issuer's disposition record). Held: D2-W384-S1, D2-W384-S3.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W384-S2",
   "IRPT_BCKEND-D2-W384-S4",
   "IRPT_BCKEND-D2-S174",
   "IRPT_BCKEND-D2-S175"
  ],
  "spec_asserts": "Never-widen signs a measured blast radius on the BUILD INPUT (CLAUDE.md 22a): the bundle bytes that will be minted, not the repository tree they come from.",
  "world_is": "Nothing was minted, signed or applied. The release cannot be signed on v3. It needs: (1) the closure re-measured and fixed into a new pin; (2) the differential re-run on the three built bundle trees with an import check and a gate comparison at the same served state; (3) the 236 Cottonwood changes attributed by commit, or the CTO's ruling that member-level attribution is enough.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T17:0xZ: IB-pr-539's three invocations print IB195-1-AC1, -AC2, -AC3 PASS",
    "git show 49467335d2:.tools/safe_deploy_core.py: _IRPT_HOLDINGS_CLOSURE lists data/assets/scripts/gold/build_cottonwood_mdpf_slice.py and data/assets/scripts/silver/opal_strategy_matcher.py; no opal_unidentified.py",
    "git show 49467335d2:data/assets/scripts/gold/build_cottonwood_mdpf_slice.py lines 132 and 136: import opal_unidentified",
    "investigation rows D2-W384-S1..S4, D2-S174, D2-S175",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_195_P_DRAIN_END_20261014.md (msg 7763)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A gate reading explained by the served clock and carried as a method rule, a scratch side effect outside the repo, and the issuer's two records. The BLOCKING closure finding and the unattributed changes are held."
 }
]
```
