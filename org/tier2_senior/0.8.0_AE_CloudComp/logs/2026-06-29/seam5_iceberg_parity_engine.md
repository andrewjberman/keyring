# NFRA_COMPDRIFT seam-5 Iceberg-vs-canonical parity ENGINE — BUILT + LIVE-VERIFIED (lane ~B)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Serial:** 0.8.0_AE_CloudComp~B | **Date:** 2026-06-29 | **Window:** ~2051Z -> ~2116Z (follows seam-6)

## Summary

COO GO'd me on seam-5 (the OTHER COMPDRIFT GAP) after seam-6. Built the Iceberg-vs-canonical
parity engine; with seam-6, BOTH drift-topology GAP-seams are now closed. Committed f293f6c1f.
COO ACCEPTED. The standout was a false-parity finding caught by ground-testing before reporting.

## Work done

- New `infra/aws/globgrph/iceberg_parity.py` — standalone seam engine (PRD 4b). Per iceberg table
  (graph_nodes/graph_edges/graph_contracts): SCHEMA-FINGERPRINT (live schema vs producer schema
  SOURCE-PARSED from derive_runner.py — CTO ruling (a)) + VINTAGE-primary (derive run-time vs 26h;
  graph_contracts ensure-only -> N/A). verdict [MATCH,SCHEMA-DRIFT,STALE,UNVERIFIABLE], worst-of
  rollup, tri-state exit, fixed drift-record contract + consumer_evidence (CTO disposition model).
- `tests/test_iceberg_parity.py` — source-parse + _diff_schema + _live_schema + contract-shape +
  live integration. All pass.

## DIAGNOSE — the false-parity finding (caught before reporting)

First run reported graph_nodes SCHEMA-DRIFT (missing props) + STALE 286-407h. SMELL: I'd manually
read a fresh props-having metadata earlier. Ground-tested: Nessie writes a fresh
`00000-<random-uuid>.metadata.json` PER COMMIT (graph_nodes has 3800+), so "newest/lexical-max S3
metadata" is NOT catalog-current — it grabbed a stale orphan. FIX: resolve current via the derive's
authoritative `warehouse/_branch_head.main.json` marker (metadata_location + snapshot_id +
committed_at). VERIFIED == Nessie/Trino current (snapshot 5612831170965463937; base independently
cross-checked on Trino). Also fixed a UTC bug (time.mktime -> calendar.timegm; was giving negative
vintage age). Memory: `reference_nessie_iceberg_current_metadata_via_marker_not_newest_s3`.

## Compiler Tools

| Tool | Why | Result |
|---|---|---|
| `comp-which` | route to compdrift seam-5 design | PASS |
| `comp-kuzu` | (prior) graph grounding | PASS |
| `ds-commit-gate.sh` (x6) | Rule-14 gate on engine + test | PASS (one rail false-positive on the infra/aws path substring — added rail-checked marker) |
| `safe-commit.sh` | Rule-14a commit | PASS |

What worked: ground-testing the engine against the live artifact surfaced the Nessie-currency trap
BEFORE it shipped as a false finding. What failed: the PreToolUse rail HUD false-positived on the
ds-commit-gate command (infra/aws path read as an infra-.tf grep) — used the documented rail-checked
escape. Gap: rail heuristic over-matches `infra/aws/*.py` paths as `.tf` greps.

## Verification

- ds-commit-gate clean; live run -> 3 tables MATCH, vintage 0.2h fresh, exit 0 (grounded vs
  marker-resolved Nessie-current). Test all pass incl. live integration (all MATCH).

## MCP traffic

Sent: CTO seam-5 design-Q + DONE/2-manifest-findings; base coordination + JOIN-key grounding +
seam-5-resolved + debt-flag; COO RAVC2; 0.7.0_AE P2 heads-up #2. Received: COO GO seam-5 + ACCEPT;
CTO bless (canonical-source a); base grain-correction + snapshot-discrepancy + debt-flag-grounded.

## Blockers

None. Open GATES (not blockers): CTO manifest edits (grain correction + marker-track-contracts +
seam-5/6 verdict_vocab land — his ledger); both engines await comp-drift P2 wire-in (0.7.0_AE).

## Current State

BOTH COMPDRIFT GAP-seams CLOSED. seam-5: `infra/aws/globgrph/iceberg_parity.py` (commit f293f6c1f),
seam-6: `code_heat_parity.py` (dd7cd996a). Both module-shaped, same drift-record contract, Trino-
independent, await P2 thin-wrapper promotion. graph_contracts is the one non-authoritative
resolution (not in marker — flagged to CTO). metadata.json 3800+ backlog = dry-run-gated sweep
(base-grounded; flip routed to 0.7.0/CTO).

## Next Steps

1. **[0.0.0_AB_MSTR / via 2.0.0_SA_COO]** dispatch + ferry comp-lineage (IC-20260527-003) to me —
   COO green-lit my designated comp-ferry tester lane (LD-0119); I run the light-cycle test on land.
2. **[1.0.0_SA_CTO]** land the manifest edits (grain correction; marker-track graph_contracts;
   seam-5/6 GAP->COVERED + verdict_vocab).
3. **[0.7.0_AE_CloudOps]** comp-drift P2 wires both engines; the GLOBGRPH_MAINT_MODE dry-run->live
   flip (metadata.json backlog).
4. **[0.8.0_AE_CloudComp~B]** HOLD for MSTR's comp-lineage ferry; run + RAVC the ferry-test on land.
