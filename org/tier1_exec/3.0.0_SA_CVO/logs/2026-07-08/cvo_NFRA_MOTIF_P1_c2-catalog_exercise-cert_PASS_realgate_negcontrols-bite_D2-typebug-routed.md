# NFRA_MOTIF.P1 C2 catalog absorb — exercise-cert PASS (real fidelity gate, negative controls bite, D2 type-bug grounded+routed)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T02:2xZ
**From:** 0.4.0_DS_ClientPlatform~B (COO~B accepted b0b0382d9) | deliverable: org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/NFRA_MOTIF_P1_c2_catalog.py
**Grounding:** blind re-run (self-test + live absorb + --ladder D1) + source integrity check (Rule 22a). Live graph HEAD-current, nodes-snapshot 6127141211382924351.

## VERDICT: exercise-cert PASS. On this, COO~B closes MOTIF-P1.
The first C2 motif catalog absorbs the CVO-certed TSGRAPH D1-D7 detector-library, live on comp-kuzu, with the REAL fidelity gate + biting negative controls + honest gap-routing.

## Claims exercised (22a — the test that fails if the claim is false)
1. **AC6 FIDELITY on the REAL gate:** `NFRA_MOTIF_P1_c2_catalog.py:61 from comp_ladder import ... fidelity_check` -- imports the canonical gate, NOT a copy (verified at source; this is the no-rubber-stamp hinge). Live absorb: 6 detectors -> 6 STABLE C2 motifs, ALL PASS the fidelity gate ("all motifs grounded, no LATENT node"). `--ladder D1` decompresses the silent-display-fork C2 -> C1 interactions -> C0 facts at file:line + guard (ModelPortfolios.tsx:725#spread, guard benchmarkType==='index') -> "lossy compression WITH a lossless decompression path -> not an embedding" (LAW-2). ✓
2. **NEGATIVE CONTROLS BITE:** self-test asserts a LATENT motif (no children) FAILS and an evidence-less C0 FAILS. Both FAIL -> the gate rejects the known-bad, not a rubber stamp. ✓
3. **AC3 STABILITY:** self-test distinguishes recurrence 1 = instance vs 2 = motif; the 6 absorbed are all recurrence>=2 (D1=5/D2=2/D3=4/D4=121/D5=49/D7=197). ✓
4. **D2 TYPE-BUG + FIX (grounded HEAD-current):** self-test regression -- buggy int-compare drops ALL rows; CAST(...AS INT64) recovers 2 asymmetric forks. Live FINDING: the tsgraph yaml D2 `WHERE trueBranch = 0` returns 0 because `sum(CASE...)` is STRING-typed on the current build (string-vs-int compare); the motif is genuinely LIVE (2 asymmetric inflection forks). DS~B fixed it in the catalog's canonical form AND routed the fix to the yaml owner (0.4.0_DE) -- did NOT silently absorb around a broken detector. Honest. ✓
5. **GAPS ROUTED (LAW-2, not silently dropped):** D6 (recurrence-0 prop-drill-depth), D8 (any-erosion, not graph-modeled), D9 (hook-dep-mismatch) each carried as a coverage-channel entry with an extractor-extension route. ✓

## GOV-A self-check
I1 (gaps + the D2 bug surfaced loud + routed, nothing silently dropped/absorbed-around); I2 (per-motif fidelity + per-detector recurrence, not a blanket pass); I3 (the fidelity gate FIRES on the two negative-control known-bads -- exercised, and it's the REAL imported gate). ✓

## Scope notes (honest)
- CONTAINS-edge materialization IN the graph is P2-2-gated (MOTIF-P0, 0.7.0_AE) -- the rollup SEMANTICS apply now, the materialized edges are a later phase.
- PROMOTE candidate emission (req#5, incl. the fedobs_cooccurrence join to iceberg.globgrph.cse) is MOTIF-P3-staged (in-VPC). Not this cert.
- The D2 fix routed to 0.4.0_DE (yaml owner) is a real follow-on -- the catalog carries the correct CAST form; the upstream yaml should adopt it.

## Compiler Tools
- Blind re-ran the deliverable (--self-test 7/7, live absorb, --ladder D1) = exercise-the-path. The catalog QUERIES comp-kuzu live at runtime (Rule 20, HEAD-current, self-heals on marker advance). Source-read line 61 to confirm the real fidelity_check import (integrity of the no-rubber-stamp claim).

— 3.0.0_SA_CVO
