# MDPF_CANRTE.A Phase-A canonical-route design: built, delivered

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, SCRIBE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~13:26Z -> ~13:52Z (fresh session; startup per org/XXX.md complete —
registration PID 24136, Monitor bh65pe8sz confirmed running, 94/94 comp-tools resolve +
exercise PASS, audit-archive rc=0, TO census 44 TOs at base)

## What happened

- COO GO (132111Z) received on the Monitor at load; ACK'd same turn (RAVC-2, 133010Z).
- Read the governing scope whole (docs/architecture/MDPF_CANONICAL_ROUTE_SCOPE.md @86f52bdfb),
  then the TO; flipped `<status>` staged->pending @11a770a93.
- Built and delivered the Phase-A design:
  **org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_CANRTE_PHASE_A_DESIGN_20260804.md**
  @ab2d2f167 (citation vintage @e0d657799 throughout). Delivered to CTO (135134Z) + COO
  (135207Z) — triangle only, per anti-chatter.
- Recs: F-1 shape-uniform/source-parameterized (C-1 PRESERVED-BY-BINDING; §6.1 ETFS-CANON
  boundary explicit) · F-2 bind-uniformity-at-the-spine (L1 firm-local prep only where vendor
  grain demands; the altitude judgment call NAMED, surfaced not adjudicated) · F-3 Model-B
  with the C-2 rider mandatory.
- Candidate #5 ADJUDICATED AT SOURCE: the cottonwood read in the 49f-named builder is the
  GLOBAL fold's contracted leg read (load_cottonwood_slice dim:1653-1715, invoked only under
  `if "global" in want:` dim:2537-2539) — REFUTED as 49f-leg contamination; the real defect is
  the misnamed one-script-three-firms builder (design §4.5).
- Census-exceeding findings: builder homes span FOUR trees not two; BOTH live served artifacts
  are written from off-route homes (platinum rollup <- data/mdpf/scripts/backfill/
  build_aggregate_aua_timeseries.py:78; hyphenated account-distribution bell <-
  data/smartx/scripts/compute_per_firm_account_distribution.py:275-277); the hyphen/underscore
  split lives INSIDE one script (dim_mdpf_aum_metrics.py:55 vs :74).
- Walls held: zero code changes, zero data/ commits, zero serve-path contact, tail untouched,
  MDPF_GLOBAL execution stream untouched (its scheduled-evidence reads remain open items below).

## Compiler Tools

| tool run (verbatim) | result | pass/fail vs TO `<expect>` |
|---|---|---|
| `comp-estate mdpf` | 2 chains (PPI-05 proxy + mdpf-global-view stitch); producers->served->frontend as census sees it; provenance NOTE = freshness adjectives are CENSUS-VINTAGE, not live | PASS — chain captured; vintage caveat carried into design §1.2 as required |
| `comp-pipescript io dim_mdpf_aggregate_aua_timeseries.py --pipeline mdpf` | READS 2 hardcoded (incl. the cand-5 cottonwood json) + 5 monolith silver names; WRITES none detected | PASS — manifest captured; "none" adjudicated at source: TRUE for this file (local-only writes dim:2575-2580) but attribution-misleading (S3 writes live in stage trio) |
| `comp-pipescript io build_cottonwood_mdpf_slice.py --pipeline mdpf` | "Unknown script in tree [mdpf]" | expected-miss -> C-2 evidence per `<if_mismatch>`: exact rc recorded (see next row), hand-derived from source |
| same, `--pipeline assets` | argparse REFUSED: no assets choice in enum {bd-gold, inf-gold, ..., mdpf, cot*, all, bd, inf} | C-2 evidence: the assets tree is structurally unaddressable |
| same, `--pipeline cot-gold` / `--pipeline all` | Unknown script in both; `all` roster spans every modeled tree, script absent | C-2 evidence: absent from EVERY modeled tree |
| same, `--pipeline mdpf` unpiped | **true rc=1** | rc corrected — first capture was piped through `head` (rc measured the pipe, the A.3 lesson); re-measured clean |
| `comp-pipescript io build_mdpf_wsc_inflection_feeder.py --pipeline mdpf` | READS 1 hardcoded (opal-data-inf client_performance.parquet); WRITES none detected | PASS as recall; both incomplete vs source (feeder:529-533 reads, :451-465 writes) — hand-derived, cited |
| `comp-pipescript io stage_mdpf_revamp_trio.py --pipeline mdpf` | READS/WRITES none; WARN "no s3_layout constants... manual review required" | fully blind -> C-2 evidence; hand-derived (trio:45-49, :77) |
| `comp-pipescript io dim_mdpf_account_distribution.py --pipeline mdpf` | READS 1 hardcoded + 3 monolith names; WRITES none | partial -> writes hand-derived (dist:63-75) |
| `comp-pipescript io dim_mdpf_aum_metrics.py --pipeline mdpf` | READS 2 hardcoded + 1 monolith; WRITES none | partial -> writes hand-derived (metrics:55, :74) |
| `comp-pipescript io mdpf_aggregate_aua.py --pipeline mdpf` | READS/WRITES none; WARN manual review | **fully blind on the legacy SERVED producer** -> strongest C-2 row; hand-derived (agg:228-241, :1353-1360) |
| `comp-glob` x3 (builder locations) | located all route scripts incl. the 4-tree home spread | PASS |
| `comp-grep "account-distribution.json" data/` + `comp-grep "platinum/mdpf/aggregate_aua_timeseries" data/` | found the two LIVE served artifacts' writers (smartx tree; backfill tree); denominators printed (956/960 scanned) | PASS — the §1.3 finding |
| phase-2 self-audit (per TO) | design §9: all five dispositions cited @e0d657799; cand-5 explicitly adjudicated; INFERRED remainders labeled (serve-chain attribution; smartx-dist read set); reserved words absent | PASS |

Gate runs on commits: comp-surface-check OK (no critical surface) + comp-pulse REFLEX CLEAN
(1 file vs 1662 danger nodes) on both @11a770a93 and @ab2d2f167. No commit-gate.sh runs — zero
.py files touched (design-only, by wall).

## MCP traffic (window)

4 sends: ACK to COO (133010Z), delivery to CTO (135134Z) + COO (135207Z), plus registration.
2 receives: COO ACK-of-broadcast (070711Z, informational) + COO GO (132111Z).

## Blockers

None. Phase B is gated on CTO's F-1/F-2/F-3 rulings (by design, not a blocker).

## Next Steps

- [1.0.0_SA_CTO]: rule F-1/F-2/F-3 off the design doc; C-2 routing to the graph stream is
  yours per anti-chatter; sovereign-class residue to Andrew.
- [0.4.0_DS_ClientPlatform] (me): Phase B (migration-plan design) auto-starts at this seat when
  the rulings land — no new GO needed. Meanwhile the OTHER stream's open items stand:
  EMIT-2 scheduled-fire read after today's 09:00 ET cycle; BR1 Gate-1 harness day-1 when the
  AE twin fires; T4.A residue (~30 tables) as fill work.
- [2.0.0_SA_COO]: acceptance read of the deliverable vs the TO criteria at your convenience.
