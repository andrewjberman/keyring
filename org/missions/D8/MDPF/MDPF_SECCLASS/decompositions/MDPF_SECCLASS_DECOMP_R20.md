# MDPF_SECCLASS decomposition -- ROUND 20 (2.0.0_SA_COO~M1, dell1, 2026-10-11 ~03:3xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers three cells.

**Cut on:** the CTO round-19 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_19_20261011.md` @de2927d9ab, 1.0.0_SA_CTO~DELL1 msg 3419).
- **Item 1 is cell `SC-e-87`** (row D1-S26, the BD served-path reach).
- **Item 2 is cell `SC-e-88`** (row D1-S27, the C_06 total-vs-class-sum trace, a read).
- **Item 3 is cell `SC-e-89`** (rows D1-S23 + D1-S25, the seat-gates limbs).
- Carried, not cut: e57e61 (FWD-10 apply) stays HELD on its trigger; the p1 residue waits on its ruling; IB-pr-417's e56 member is at dell2.

**State the round starts from (measured 2026-10-11 ~03:3xZ, box/dell1):**
1. **BD's three served classify sites call `classify_with_identity` only for a blank ticker.**
   - `D_04.client_portal_summary.py` `_classify_with_canonical` (:160-167);
   - `C_06.client_mix_timeseries.py` `classify_series` (:228-233);
   - `D_03.composition_artifacts.py` `classify_series` -> `_classify` (:135-140).
   A ticker with no row falls to `unclassified` at each site, so SC-e-79's lib branch never runs on the served path.
2. **C_06's firm-daily snapshot** accumulates class dollars as `data['mix'][ac] * total_mv` per relationship (:737-743), where each share is
   `round(class_mv / total_mv, 6)` (:595), and `total` as the sum of `total_mv`. The published gap (total minus class sum) reads -4.71,
   +128.06 and -128.57 on 2026-10-06, 07 and 08.
3. **`.tools/crossbox-deploy-check.py`** keys OPEN-CALL on the deploy's own files since `ecedce453e`. `measure_open_deploy` skips a
   sentinel only when `--serial` equals its `author`, and it dedupes by `(path, blob)`, so one slug read in two worktrees at two
   statuses counts twice. A direct run without `--serial` draws a hit from the deploy's own entry.

## Rule 24 record

- **Domain:** the three enrichment items of the round-19 analysis; nothing else is a cell.
- **(ii) Same grain:** one cell per item; SC-e-87 is the one served-data build, SC-e-88 a read, SC-e-89 a tool build.
- **(iii) Intent coherence:** SC-e-87's acceptance drives each site's OWN served classify function, because round 16's AC1 drove the lib
  function and passed while the served bytes did not move (row D1-S26).
- **(iv) State coherence:** SC-e-87 moves no served key by itself; the ship is a separate pair-gated act. SC-e-88 writes no served key.
  SC-e-89 touches one tool file and no served key.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-87` | The three BD classify sites route a non-blank ticker that `classify()` misses to `classify_with_identity(ticker, name, cusip)`. Nothing else changes. Plus the ship's never-widen half request, both halves left unsigned. | FWD-1 (BD half) | SERVED | none (ship is a later pair-gated act) |
| `SC-e-88` | A read: name the cause of C_06's firm-daily total-vs-class-sum gap for 2026-10-06..08. A defect it names becomes a round-21 item. | FWD-1 (the residual SC-e-87's leg G is stated net of) | LOCAL | none |
| `SC-e-89` | `.tools/crossbox-deploy-check.py`: the actor's serial resolves without `--serial`, so the deploy's own open entry draws 0 hits, and one slug counts once. | seat-gates (rows D1-S23, D1-S25) | LOCAL | none |

## Write sets (disjoint)

- **SC-e-87:** `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`, `.../C_06.client_mix_timeseries.py`,
  `.../D_03.composition_artifacts.py`, new `.../tests/test_served_path_reach_r20.py`, and the half request
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_SERVED_PATH_REACH_20261011.md`.
- **SC-e-88:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C06_TOTAL_GAP_TRACE_20261011.json` and the scratch script under
  that folder's `R20_CHECKS/` named in its order.
- **SC-e-89:** `.tools/crossbox-deploy-check.py` only.
- Each may also append to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Chains

Three cells, no edge between them: three chains. Fan-out 3 of 3, cap 8. Slots ~77, ~78, ~79, `worker` class.
SC-e-87's leg G (a scheduled BD fire after the ship serves the 23 by their NAME:: rows) is read after SC-e-88 names its cause, because
the expected outcome is stated net of that gap.
