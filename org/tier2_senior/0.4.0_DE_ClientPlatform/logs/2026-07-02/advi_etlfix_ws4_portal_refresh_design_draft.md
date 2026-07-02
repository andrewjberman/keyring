# ADVI_ETLFIX WS-4 — Predictable Portal Refresh: DRAFT design brief (idle-cap redirect)

**archetype:** SCRIBE
**secondary_archetypes:** IMPLEMENT

**Workspace CLOUD commit:** `ed595f90e` (docs/briefs/advi_etlfix_ws4_portal_refresh_sla_design_DRAFT_20260702.md)
**Trigger:** COO DRIVE redirect (20260702T151148Z) — productive idle-cap while on-call for the P0 post-fix re-publish. Pre-scope WS-4 (my lane) as a DRAFT for the CTO arch-gate.

## Current State

Drafted the ADVI_ETLFIX WS-4 (Predictable Portal Refresh) design brief for the CTO arch-gate (SLA-as-GATE), feeding directly off the 07-02 P0 serving-side ground-truth. DRAFT not implement; RAVC'd COO cc CTO+CVO. Preemptible — drops to the Phase-0 post-fix re-publish the moment an upstream leg (bd/inf/MDPF) un-freezes.

### The design headlines
1. **SLA oracle keys on served CONTENT `data_as_of`, not S3 mtime** — the load-bearing constraint, straight from the P0: bd was mtime-fresh @07-02 / content-stale @06-29, so an mtime-keyed gate false-GREENs. Proposal: a comp-freshness CONTENT-vintage dimension.
2. **Anti-silent-degrade = OUTCOME-keyed alarm** — monitors "did partner P's SERVED content advance to today?" not "did the chain succeed?" — structurally un-silenceable by a downstream degrade (answers PRD SS1.2 / arch-gate-4). Per-partner scope.
3. **No-clobber = per-key byte-size/shape FLOOR** + single-writer registry (ADVI_BREAKS anchor: a 728B stub collapsed the mature inf header). Coordinate with the LIVE opal-globgrph-freeze-monitor + ADVI_BREAKS TO-6b, don't duplicate.
4. **Re-publish path** = my Phase-0 on-call formalized (verify fresh data_as_of → publish MDPF build→served tier → CF-invalidate only if the cache-control-injector TTL holds stale).

Includes the per-partner endpoint→artifact map (bd/inf/MDPF), a proposed SLA-record schema, 6 open arch-decisions (AD-1..6) each with a DE lean, owners/lanes, and 5 machine-checkable ACs.

## Decisions Made
- Kept it a DRAFT/SHAPE for the CTO gate (not implementation) — the COO framed it as pre-scope; arch-gate rules the shape before any durable-wave GO.
- Leaned the gate-location decision to reuse the LIVE opal-globgrph-freeze-monitor + a comp-freshness content dimension (least new infra) rather than a net-new Lambda.
- Flagged the CF-invalidate + no-clobber-enforcement as AE-lane (writer/infra), DE role = verify + trigger + the vintage-extractor config + optional UI.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| `comp-grep` (ADVI_BREAKS clobber lesson) | 9 matches | grounded the stub-clobber anchor (INF_D_00 728B stub vs D_04 race) |
| (P0 session, reused as input) `comp-freshness` / `aws s3` served-content | — | the endpoint→artifact map + data_as_of finding that drives the SLA design |
| `safe-commit.sh` (brief) | PASS | surface-check OK → ed595f90e |

## Next Steps
- **[1.0.0_SA_CTO]** arch-gate the WS-4 shape — esp. the content-vs-mtime oracle + the outcome-keyed anti-silent-degrade model; rule AD-1..6.
- **[2.0.0_SA_COO]** on CTO shape-OK, fold WS-4 into the ADVI_ETLFIX Phase-1 TO decomposition (DE + AE alarm-infra + CVO).
- **[0.4.0_DE, me]** PREEMPTIVE: run the Phase-0 post-fix re-publish/verify the moment bd (0.7.0~A) / inf (0.6.1) / MDPF un-freezes. Then: author the vintage-extractor config (DE-authorable) once the gate shape is ruled.
