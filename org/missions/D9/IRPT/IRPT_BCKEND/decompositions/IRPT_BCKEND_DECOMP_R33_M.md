# IRPT_BCKEND decomposition -- ROUND 33, WORKSTREAM ~M (2026-10-08, 2.0.0_SA_COO~M2, dell2)

**Cut on:** the 1.0.0_SA_CTO~DELL2 round analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_75_76_P_64_Y_20261008.md` @0a91529221 (msg 1336),
section 2, item E3: "S388, the HoldingsSnapshot share -- (1) the cell names which side moved (the schema or the committed wire type)
and brings them into agreement; the generator test regenerates 0 diffs for HoldingsSnapshot. LOCAL."
- Remediations owned by ~M2 at this cut: none. Row S392 (the SC-e-62/e56 per-fire NO-WORSE read) is a standing per-fire obligation
  of this seat, not a cell.

**Rectangle:** E3, one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mw-331` | **The HoldingsSnapshot wire type agrees with its schema** (E3, row S388). Regenerate `HoldingsSnapshot.ts` from the schema at HEAD; commit only that file on the portal branch; one regeneration then rewrites nothing in it. | S388 (enrichment) | LOCAL | none |

**Which side moved (measured by the issuer at the cut, 2026-10-08 ~17:5xZ):** the SCHEMA.
- `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` last changed at 01e843ce2e (the e62 release port, 2026-10-07),
  sha256 `7c221b13df63...`.
- portal a6868784 (MDPF_SECCLASS TO-SC-e23) hand-edited the wire type's class enum to the six classes without regenerating. The body
  equals the generator's output; the header still names the 10-02 schema, `0236991ce32e...`.
- One regeneration at portal DEV 1cbc56a7 rewrites HoldingsSnapshot.ts by 1 line (+1/-1, the `Source sha256` header). The same run
  also rewrites AnalysisReport.ts (~G2's share), ExportBundle/ExportReceipt/responses/index (~P's share, on its DEV candidate) -- none
  of them this cell's.

**Chains:** A = 331. M = 1. fanout: 1 of 1 chains, cap 8. Slot ~200 (this seat's block ~200..~219, msg 974).

**Size and path:** 1 product line, LOCAL -> the DIRECT-ACT path (`/dispatch` Step 2): one order, `<direct_act>true</direct_act>`, a
worker executes it, it drains; no L2, L4-R or L8-L10; the close is the issuer's one real run (the regeneration test on the drained
branch). The portal branch is a DEV candidate touching a product file, so it goes to the CTO for review; this cell never pushes DEV.
