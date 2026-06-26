# NFRA_TSGRAPH.P2-1 -- Phase-2 harness harden + P2-2 gate flag (session-start drive)
**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Session:** 2026-06-26 (~13:00-13:05Z) · **Agent:** 0.4.0_DE_ClientPlatform · **TO:** NFRA_TSGRAPH.P2-1 (LEAD, pending) · **Commit:** `b47839cff`

## Current State

Session-start drive on the pending lane TO (P2-1) + the NNA-scope F5-retire dispatch. Ground-truth reconciliation
established that P2-1 is NOT stranded -- it was built + committed (`fbf8549b1`, 06-18) + session-logged with full
AC6 repro + RAVC2 CHECKPOINT to COO (164747Z) + schema to AE (164715Z, ACK 165018Z, COO GO'd P2-2 181647Z). The TO
is correctly held `pending` by design: full close = after AE P2-2 materializes the cluster layer onto the live
canonical graph + I verify the edges there (PRD acceptance spans P2-1+P2-2). So this is event-gated, not idle.

**Drive-now actions taken (re-verify against LIVE state, never self-report):**
1. **Live-graph check (P2-2 status):** comp-kuzu canonical surface (HEAD-current, pin==marker, snapshot
   7416840837186625163, 12644n/19329e, auto-refreshed BEHIND->current per Rule 20) has **0 Page/PanelCluster
   nodes** => AE P2-2 NOT materialized. The overnight derive_runner commit (2026-06-26T02:02:30Z) was a different
   derive (+144n/+191e), not the cluster layer.
2. **Real defect found + fixed in my own validation harness** (`load_clusters_scratch.py`): the Phase-2 mandate
   query no longer ran clean on the local kuzu build. **Crash boundary empirically pinned:** an inline rel-property
   filter on a variable-length pattern (`{edge_type:'..'}*0..`) is a PARSER ERROR; the `*0..N WHERE all(r in
   rels(e) ...)` workaround SEGFAULTS (exit 139) at bound **N>=4** (`*0..3` safe, `*0..4+` crash). The real
   drilldown tree reaches depth 4, so no safe recursive bound covers it locally. Rewrote the two recursive
   traversals to EXPLICIT fixed-length single-hop chains (single-hop inline filters are crash-free) UNION'd over
   depths 1..MAXD=4 -- crash-free AND full-depth. Loader now EXIT=0 end-to-end; results identical to the 06-18 emit.
   Recursive `*0..` form reserved for the comp-kuzu CANONICAL surface (newer kuzu build) post-materialize.
3. **Committed** `b47839cff` (ds-commit-gate clean), pushed CLOUD. No change to emitted artifacts.
4. **Flagged the gate to COO** (130154Z): P2-2 (AE, GO'd 06-18) has sat ~8 days unworked -- 1 of 6 pending TOs in
   AE's queue behind ETFS/recon/COTETL/BD-box urgent work; AE not registered. Asked COO (who sequences AE's queue)
   to either slot P2-2 or tell me P2 is de-prioritized so I mark P2-1 blocked-on-COO-sequencing (stop zombie-reading).

## Blockers
None blocking ME. P2-1 full close is event-gated on AE P2-2 materialize (genuine cross-lane gate, COO-sequenced).
The higher-priority sovereign item -- Andrew's F5-vs-Cottonwood call (FE INFMVP.F5-retire) -- remains pending;
I take it the instant it lands (it drops everything else).

## Next Steps
- **[2.0.0_SA_COO]** sequence AE P2-2 (or rule P2 de-prioritized). Reply gates my P2-1/P2-3 close path.
- **[0.7.0_AE_CloudOps]** P2-2: materialize the additive layer (re-zip the 6 Dockerfile-COPY'd files per the
  globgrph S3-source-ZIP gotcha); ping me with any schema concern BEFORE build. Interface unchanged from 06-18.
- **[0.4.0_DE]** On P2-2 materialize: verify cluster edges on the LIVE comp-kuzu canonical surface + re-run the
  recursive `*0..` form there (newer build) -> full P2-1 RAVC2 close, then P2-3 CLI.
- **[Andrew]** F5-vs-Cottonwood sovereign call -> takes precedence over everything above when it lands.

## Compiler Tools

| Tool | Run | Result vs `<expect>` |
|---|---|---|
| `comp-kuzu` (Phase-1, live) | `MATCH (n) RETURN labels(n)[0], count(*)` | PASS -- provenance `current` (pin==marker HEAD, snapshot 7416840837186625163, 12644n/19329e, age 0.0h). Confirms the live P1/P4 substrate is HEAD-current per the Phase-1 mandate. |
| `comp-kuzu` (P2-2 gate check) | `MATCH (n:CloudNode) WHERE n.node_type IN ['Page','PanelCluster'] RETURN n.node_type, count(*)` | EXPECTED-EMPTY -- 0 rows. P2-2 not yet materialized; P2-1 stays pending on the gate (ground-truth, not self-report). |
| `load_clusters_scratch.py` (Phase-2, scratch) | patched loader -> platform-schema scratch Kuzu (548n/387e); per-page CLUSTERS->CONTAINS_DRILLDOWN(1..4); cohort/kind props; SHARES_SOURCE sample | PASS (EXIT=0) -- 15 pages/91 clusters; AdvisorIntelligence depth=4/106 nodes; cohorts {inflection:23,49financial:3,demo:3,cottonwood:2}; SHARES_SOURCE coupling renders. **FINDING:** local kuzu recursive-rel crash boundary pinned (`*0..3` safe, `*0..4+` segfault) -- harness now uses crash-free explicit per-depth chains. |
| `ds-commit-gate.sh` | gate on `load_clusters_scratch.py` | PASS -- py_compile + ruff py39 clean. |

No comp-which rail override needed; comp-kuzu was the canonical tool for the live-graph checks (Rule 20/21).
