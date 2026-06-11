# 0.6.0_AE_PartnerETL — work cycle 2026-06-11 2330Z (GLDINC day-close)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

GLDINC 7/7 engineering COMPLETE (A_04 at DS deploy). One day, Andrew-direct
"fix all of them... be careful and go one by one" -> 6 converted + 1
hardened-keep-full, 4 distinct incremental patterns, 3 production defects
found+fixed, 0 cutovers (all evidence-gated).

## This segment
- A_03 + B_01 deployed by DS (5d2fca51f, one cycle). SHADOW_SET += both
  (803caf0e6, S3 MATCH) -> SIX evidence streams on the 04:00Z run.
- D_02 census flag CONFIRMED IMMATERIAL structurally: parts = per-date
  role_aua partitions; every order-sensitive dedup's tie key INCLUDES date ->
  ties never span parts -> completion order can't flip survivors. Hygiene
  batch only (index-slot convention compliance).
- A_04 (7/7): CLASS-N oracle-fix proof battery = MATERIALITY 0 (latent,
  never bit on current data) / DETERMINISM 0 / **DELTA 0** (zero served-byte
  change -> trivial never-widen). Both remedies (index-slot + provenance +
  total-order). KEEP-FULL recommendation (now()-stamped timestamps vs 31s
  value; parked alt: stamp from max input date). Handed to DS 2317Z.

## Final scoreboard (ADHC_GLDINC incremental workstream, day 1)
| Script | Pattern | Deploy | Evidence stream |
|---|---|---|---|
| A_02 | reconstruct-from-output | 887ffd17d+c8ed91949 | parity (night-2 tonight) |
| A_01 | daily-state-grain | 73ec87a84+ba7b20807+e5575c018+27ffaa55b | parity (night-1) |
| B_02 | per-date input-fingerprint | 4a62d0fdf | containment (BOOTSTRAP) |
| B_03 | per-date fingerprint (pure etag) | 0aa50c017 | containment (BOOTSTRAP) |
| A_03 | whole-run gate (#4) | 5d2fca51f | gate-evidence (BOOTSTRAP) |
| B_01 | whole-run gate (#4) | 5d2fca51f | gate-evidence (BOOTSTRAP) |
| A_04 | CLASS-N fix, keep-full | (DS cycle in flight) | n/a (delta=0) |

Defects fixed: (1) A_01 oracle nondeterminism (served attribution flips;
CTO+COO-signed deterministic fix); (2) swallowed-read-failure load path
(guard + DS retry hardening; fired live on a real transient mid-proof);
(3) A_04 latent CLASS-N (delta=0 hardening). CLASS-N census: DS scan + my
assembly-pattern discriminator + CTO independent read converged; index-slot
convention ratified; AST-rule candidate -> COO.

Capture at full cutover: ~1,294s (A_03+B_01 gates) + per-date narrowing
(A_02 15-24/1,881 files; A_01 11-24/1,808; B_02 7/2,352 dates; B_03 ~same)
on the ~29min/no-change-night measured waste.

## Residue (low-pri)
E_13 classification (CTO residual), D_02+E_* index-slot hygiene batch,
A_02 nightly-shadow A_01-pattern... none blocking. Cutovers = task #8
(clean nights -> Andrew nod, per script).

## AM review queue
COTETL verify (checklist staged) -> PRTORG AC1/4/7; SIX GLDINC scorecards
(gold/_parity/{fee_rate_history,advisor_assignments,canonical_lots,
account_gains,positions_cube,holdings_lots}/); load_flows post-fix counter
(1440 gap should close, counter 0->1).
