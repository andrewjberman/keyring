# ws-charter — 2026-06-03 1535Z — Andrew GO x2: portal promote v2.1.113 + MDPF_SCOPED close

**CLASS:** FIX (promote-orchestration) + close-relay. ANDREW_DIRECTION (live convo).
**Trigger:** Andrew direct, live: "INFOTD and INFNNA are done" + (AskUserQuestion) "Fire the promote now" + "MDPF is also done".

## (1) Portal promote v2.1.113 — GO'd, dispatched

INFOTD/INFNNA smoke CONFIRMED by Andrew on live v2.1.112 → last gate cleared on the staged promote. Andrew chose "Fire the promote now".

- Verified portal `origin/PROD..origin/DEV` = exactly 3 FE commits: `548c9d7d` (Model Portfolios footnote Inflection→Orion) + `b5d3e923` (ADVI_FEREFI items 1-5) + `21be552d` (FIX1 cold-start retry:false drop). PROD base v2.1.112 (`6549038c`). Main tree on DEV (Rule 19). Next tag portal-v2.1.113.
- DT (0.4.0_DT_ClientPlatform, portal-promote executor) is OFFLINE → I cannot spawn (HARD-BLOCK #8, MSTR scope). Sent the full PROMOTE PACKET to DT's inbox + a SPAWN REQUEST to MSTR (spawn DT to execute). CC COO (drive-track).
- Packet: Rule-19 ephemeral-worktree, gates (ci/VALGATE-D1/PROD-typecheck/HALTGT), tag+push --follow-tags, CF invalidation, rollback `git push origin 6549038c:PROD`, post-promote smoke-scope (6 FE items + FIX1 deep-drilldown), RAVC2 to CTO+COO on ship. Flagged the MSYS_NO_PATHCONV footgun (do NOT set for the push — fail-closes VALGATE D-1).
- ON SHIP: I convene the SERVED-PROD e2e CVO verify on the NEW live bundle.

## (2) MDPF_SCOPED — Andrew S5 smoke done → CLOSE relayed to COO

Andrew confirms S5 visual-smoke DONE. Both close-legs now met: OPS1 CVO-closeout GREEN (`3ffad298c`, all 6 AC re-derived, AC4 sharp-test, 6/1 honest-hole accepted per CTO NO-backfill ruling) + S5 Andrew-smoke. Relayed CLOSE-GO to COO (close convener). OPS1 was the last AE leg.

## Manifest discipline (reinforced to COO)

PORTAL bundle (v2.1.113) = 3 FE commits ONLY. Fee-split is DATA-layer, separate: #6 INF live (inf-pipeline-v1.7.69) · W2b 49F (D_02 gold, COO ruled FULL-publish/AC4-required, DS standing by for 0.6.0 run) · bd hardening (bd-v2.25.0, DEPLOYED-PENDING-AC4 CVO served-parity, rides W2b cascade). #6 FE = verify-only.

## Tracking after this turn

- portal-v2.1.113: DISPATCHED (DT spawn pending MSTR) → expect RAVC2 → then SERVED-PROD e2e CVO convene.
- MDPF_SCOPED: CLOSE-GO relayed → COO convenes.
- bd hardening: DEPLOYED-PENDING-AC4 (CVO served-parity).
- Andrew stack remaining: keep-warm GO (PRD staged) · cost-basis a/b.
