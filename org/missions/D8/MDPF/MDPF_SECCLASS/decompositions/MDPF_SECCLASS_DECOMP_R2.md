# MDPF_SECCLASS decomposition -- ROUND 2 (2026-09-30, issuer 2.0.0_SA_COO~M, on the CTO's round-1 analysis)

Cut in ONE issuance on `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md` @151c890591
(msg 103116), enrichment list E1-E8. The rectangle is that list, one cell per item, with the thread-breaking item (E3)
first.

Standing rulings carried into every face:
- **Andrew-direct 2026-09-30 ~02:2xZ:** "yes, bd-securities values can seed new rows. THey just don't overwrite
  existing rows."
- **CTO C-WRITER ruling (analysis section 1):** `classified_by` takes the values `seed` / `scheduled` /
  `constituents` / `legacy`.
  - `seed` always wins.
  - `scheduled` and `constituents` write only where no row exists.
  - A missing label reads as `legacy`.

| cell | item | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-3` | E3: re-census the BD thread against the post-backfill table; fresh thread half incl. the BD principal's etf-classifications read (IAM, desired) | FWD-1 | NOT-EVALUATED | laptop | WORLD | A, ~4 |
| `SC-e-1` | E1: contract v0.2.0 (four `classified_by` values); the constituents seeder sets `constituents`; the one `legacy` label update (dry-run census + its half) | FWD-4, FWD-7 | NOT-EVALUATED | laptop | WORLD | B, ~5 (first) |
| `SC-e-2` | E2: name the instrument_kind input source; an instrument_kind-only update mode; census over the 2,163 rows without it + half | FWD-8 | NOT-EVALUATED | laptop | WORLD | B, ~5 (after e-1: same seeder file) |
| `SC-e-4` | E4: a ticker-keyed Cottonwood caller of the scheduled classification (COT's own E_18, C-FIRM) + its dry-run census | FWD-2, FWD-7 | NOT-EVALUATED | laptop | WORLD | C, ~6 (first) |
| `SC-e-7` | E7: E_18's IAM (PutItem on etf-classifications, bd-securities PutItem removed; desired) + the ordinary schedule named + half | FWD-7 | NOT-EVALUATED | laptop | WORLD | C, ~6 (after e-4: both scheduled callers) |
| `SC-e-5` | E5: D_04 `build_advisor_positions._classify_ticker` (:2766) folds into the one library; positions.json carries the canonical fields additively | FWD-4, FWD-2 | NOT-EVALUATED | laptop | WORLD | D, ~7 (first) |
| `SC-e-6` | E6: the FWD-3 exercise prepared -- one scheduled ticker the fork had wrong, corrected once in the seed source, the surfaces to read named + half | FWD-3 | NOT-EVALUATED | laptop | WORLD | D, ~7 (second) |
| `SC-e-8` | E8: the 884 unresolved names reviewed -- a proposed class with its source, or a stated reason, each | FWD-2, FWD-7 | NOT-EVALUATED | laptop | WORLD | D, ~7 (third) |

**Chains and slots.**
- The edges are real data or file dependencies: e-1 -> e-2 (the constituents seeder), e-4 -> e-7 (the scheduled
  callers), and e-5 -> e-6 -> e-8 (queued on one slot).
- Fan-out is 4 of 4 chains. The cap of 4, not 8, is set by disk: each worktree is about 2.8 GB and C: had 24 GB free.
- Slots follow S197: round 1 used ~1, ~2 and ~3, so round 2 uses ~4, ~5, ~6 and ~7.

**Write sets (disjoint across chains).**
- e-3: census and half files only.
- e-1: org/standards/MDPF_SECCLASS_CONTRACT.json, yang_pipeline/seed-etf-constituents.py and a new label script.
- e-2: seed-etf-constituents.py (after e-1) and a new instrument_kind script.
- e-4: data/cot/scripts/gold/E_18.detect_new_securities.py.
- e-7: infra/aws/terraform/bd-pipeline/iam.tf.
- e-5: data/black_diamond/scripts/gold/D_04.client_portal_summary.py.
- e-6: _shared/etf_classification.py.
- e-8: a review file only.

**Every cell is LOCAL build + record.** Each served act -- the label write, the kind write, the thread deploy and live
run, the IAM applies, the FWD-3 seed run, and the seed rows from the review -- follows its own signed halves after
the drain. A write to an EXISTING row from a bd-securities value is outside Andrew's word and needs his own.

## Rule 24 record

- **MECE over a declared domain.** Domain: the analysis's E1-E8. By subtraction, E1-E8 map to eight cells with no
  remainder. Anything outside that list (FWD-6 departures, FWD-5 delete) is not in the rectangle.
- **Same grain.** One cell per enrichment item.
- **Intent coherence.** Each cell serves the FWDs the analysis names for it.
- **State coherence.** No cell moves a served value; every served move is a separate signed act.

## Battery

- `comp-schedule`: RUN on e-7. E_18 runs inside the BD gold-layer schedule; the cell names it. DECLARED-NOT-APPLICABLE
  elsewhere, since no other cell touches a schedule.
- `comp-iam`: RUN on e-3 and e-7, the BD principal's read and E_18's write; both desired, not applied.
  DECLARED-NOT-APPLICABLE elsewhere.
- `comp-adversary`: RUN.
  - Read at the cut: the analysis; the round-1 censuses (backfill: bd 207, 49financial 601, inflection 76 unresolved);
    the live table at 2,309 rows (1,934 scheduled, 238 unlabelled); D_04:2705-2888 (build_advisor_positions writes
    platinum/advisors/{id}/positions.json, wire contract docs/architecture/ADVI_49EXEC.md); COT's own
    E_18.detect_new_securities.py.
  - BLIND: the instrument_kind input source (e-2 names it), and Cottonwood's ticker-bearing holdings source (e-4
    finds it).
