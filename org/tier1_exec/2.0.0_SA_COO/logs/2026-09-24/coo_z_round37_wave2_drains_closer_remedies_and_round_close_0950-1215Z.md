# 2.0.0_SA_COO~Z -- 2026-09-24 09:50Z-12:15Z -- round 37 wave 2, two closer cells, the round closed

Continues `coo_z_crosswalk_incident_and_round37_wave1_drains_0815-0950Z.md` (@85543bf200). Push state of everything below: LOCAL
(this lane does not push; 0.0.0_AB_MSTR~Z pushes on its cadence and drained both closer commits onto CLOUD/origin).

## 1. Closer cell 1 -- one pool put per run + the universe input (CTO R-38 / R-40 preconditions 3 and 4)

closer/amgt-peers-z-20260924 @a125f8be8b (+ STATUS.md @725a9d1d08), drained by MSTR~Z as 8c75f4f90d, byte-verified by the CTO at
R-51. `add_security --batch` lands N in one run with ONE put; `_identity_universe` read once per run and passed to every build
(collision check + pool document); unreadable universe -> rc 5. Live read-only acceptance 194 -> 197 (+3) / 36 withheld; identity
tests 89 of 89. The induction re-fired at 11:11Z under the pair: 20 registered, one put, versions 22 -> 23, MEASURED 214 (R-59).

## 2. Closer cell 2 -- a registration resolves its folder's UNRESOLVED coverage record (COO~X row AMGT_CORPUS-Z-S16, CTO R-59)

The fire's 20 registrations had been APPENDED beside their folders' UNRESOLVED coverage records: two records per folder, both
claiming the folder's `security-<hash>` form, `resolve()` AMBIGUOUS, re-ingest 0 of 20. `build_crosswalk` now replaces the
UNRESOLVED record IN PLACE (same position, folder form kept as the one claimant, key forms added, provenance
`resolves_coverage_record`); denominator `resolved_folders` only when > 0; schema admits it. Live: records 274 -> 254, UNRESOLVED
60 -> 40, MEASURED 214 unchanged, multi-claimed forms 20 -> 0; tests 97 of 97 (the ENRICH byte-identity arm re-scoped around the
remedy and says so). closer @a2b84a1b2a -> CLOUD a5b9859e0a (MSTR~Z), CTO half #2 in force (R-62); COO~X re-minted under the fresh
pair: versions 23 -> 24, records 254, resolved_folders 20, 214 of 214 keys present (R-63). Record:
`deliverables/AMGT_EXPERIENCE/CLOSER_FOLDER_RESOLVE_20260924/`.

## 3. Round 37 wave 2 -- drained, round closed

| cell | worker | outer drain | close-out | result |
|---|---|---|---|---|
| rl-10 the export | ~139 | fa3b0152d2 | 096a06ca6b | 3 of 3 PASS: landed pack measured (8 pages, model-block only, 11 of 11 brand items NOT MET, FIGURES 162/179 CITES 43/0 ABSENCES 5/5); branch (b) built on the producer, parity 162/162 43/43 5/5 EXPORT-COMPARE OK; ROUTE_ASK written (existing /print leaf, `?format=rich`) -- APPROVED by the CTO (R-57), carrier round 38 (R-58), deploy leg AE CloudOps |
| rl-9 designed states + re-assert | ~138 | 6fdce83b63 | 7d13903604 | AC2 PASS (4 of 4 designed states, 18 cells), AC3 PASS (harnesses green, census 31 files TOTAL 0), AC1 REFUSED per bound 2 -- 35 of 48 predicate cells fail on files OUTSIDE the rectangle (App.tsx sidebar, PageHeaderVariants.tsx, panels/PanelHeader+PanelFooter, index.css named layers); lowContrast now 0 on all six (Z-S247 fixed, carrier Z-S249); AC4 the CVO's |

Portal: rl-10 merged clean (c6ecc9ba); rl-9 conflicted on PrintExportAction.tsx (both wave-2 cells touched it) -- resolved to rl-10's
bytes, the owning cell, census 0 and the three harnesses re-run green on the resolved tree (65a41a1f). Drain-time contract reads
`contract-check-after-rl-10/`, `-rl-9/`. Packet FINAL @7d13903604; L8/L9 handoff sent to 3.0.0_SA_CVO~Z (msg 25491) with the
round's one judgment criterion (rl-9 AC4) and the FWD-29 finding for the CTO's analysis. All nine wave worktrees and branches removed.

## 4. Rulings received and acted on

R-51 (all four preconditions hold), R-52/R-54/R-58/R-59/R-62/R-63 (information), R-57 (FWD-30 route approved), R-58 (round 38 is
the carrier; closer build phase is Andrew-gated -- the offer to build it on the closer branch was refused on the lane, not the offer).

## 5. Lessons banked

- a-served-key-with-a-producer-on-an-unmerged-branch-has-a-second-writer-on-the-trunk
- a-surprise-row-names-the-issuer-as-disarm-owner-never-a-worker
- an-appended-replacement-leaves-the-superseded-row-standing-supersede-in-place
