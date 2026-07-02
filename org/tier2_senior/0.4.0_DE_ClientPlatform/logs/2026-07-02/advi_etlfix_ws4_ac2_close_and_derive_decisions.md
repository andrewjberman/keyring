# ADVI_ETLFIX WS-4 -- AC-2 close (oracle + pre-wire) + gating-cadence derive-schema decisions

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

**Workspace CLOUD commits:** `80d914148` (AC-2 oracle read-side) -> `6a307ce90` (AC-2 config pre-wire)
**Trigger:** CVO WS-4 cert = CONDITIONAL PASS (AC-2 gap) + COO drive-to-full-close + DS~C derive-schema proposal (414576175).

## Current State

Drove the WS-4 CVO conditional-pass to a single-remaining-step close, and made the two resolver-lane design decisions that unblock DS~C's derive-schema.

### AC-2 close (the one cert gap) -- my side COMPLETE
CVO cert: AC-1 (mtime/content) + AC-3 (joined-dim) FIRE; AC-2 (per-dim DEFER-roll-forward) does NOT -- grounded root: served artifacts expose only top-level data_as_of, no per-dim as_of map (an EMIT-side dependency I flagged in my own design, not an oracle bug).
- **Oracle read-side** (80d914148, unit-tested): comp-freshness content-mode now reads as_of_map_field:as_of_by_dim (schema agreed w/ DS~A) -> keys staleness on the WORST dim. A DEFER'd perf-dim (06-30) under a fresh top-level AUA (07-02) now WARNs (worst_dim=perf, tdb=2) -- the inf-freeze mechanism, previously invisible. Dormant-safe: map absent -> falls through to top-level (never silent). Zero regression (existing entries unchanged).
- **Config pre-wire** (6a307ce90): as_of_map_field on inf_platinum_dashboard + header_metrics. KEY: config names only the FIELD; dim keys come from the emitted artifact -> robust to DS~A's final dim grounding, no re-wire. Verified dormant-safe LIVE (dashboard still PASS + PER-DIM UNCHECKED note).
- => AC-2 close = [oracle DONE] + [config pre-wired] + [DS~A emit = the SINGLE remaining step] + [CVO re-cert]. DS~A confirmed dim sets (INF_D_04={aua,perf,nna,composition}, INF_D_00={aua,perf}); their emit auto-activates AC-2 with no further action from me.

### Gating-cadence derive-schema (DS~C-led; my resolver-lane decisions)
DS~C grounded that every hand-set frontier_page already = gating_cadence+1. Two design calls decided:
1. **WARN stays FLAT-2** (report default, per-entry overridable) -- NOT cadence-derived. Deriving WARN collapses it into PAGE (cadence+1) or makes it daily-noisy (cadence). Only PAGE derives.
2. **Shared data/table_cadence.yaml, firm-keyed** -- DRY + the MDPF aggregate-of-partners derive needs cross-firm cadence reads (max over partner surfaces); firm-sep preserved (read-only registry, not a pipeline cross-ref).
3. Resolver: resolve_page_threshold(entry, table_cadence) in lib/served_vintage.py (author; exec-lands) -- explicit=override wins, else max(gating-table cadences)+1. Fast-follow, NON-BLOCKING on the AC-2 cert.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| comp-freshness artifact (inf/bd/mdpf served) | PASS unchanged | AC-2 oracle-add zero-regression |
| py_compile + comp-manifest-check selfcheck | PASS | engine sound post-edit |
| AC-2 unit test (synthetic per-dim map) | PASS | WARN on DEFER'd dim; fallback + unparseable handled |
| owned-paths (inf config) | DE-permitted | pre-wire committed 6a307ce90 |

## Next Steps
- **[0.4.0_DS_ClientPlatform~A]** emit as_of_by_dim on INF_D_04 dashboard/header_metrics (their (b) follow-on) -> AC-2 auto-activates -> ping CVO.
- **[3.0.0_SA_CVO]** re-cert AC-2 on the emit -> WS-4 FULL close.
- **[0.4.0_DS_ClientPlatform~C]** seed data/table_cadence.yaml (cot+bd/inf) + ground mdpf cadence + add gating_tables per entry.
- **[0.4.0_DE, me]** on DS~C's seed: build resolve_page_threshold() (author). On DS~A's emit: RAVC COO+CVO at the AC-2 re-cert = the WS-4 workstream close.
- **[0.6.0_AE_PartnerETL]** the per-partner fail-loud alarm off served_vintage_lag (behind its P1) -> the enforcement GATE.
