# MDPF_SECCLASS decomposition -- ROUND 1 (2026-09-29, issuer 2.0.0_SA_COO~M)

Cut on the ratified PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.1, ADMITTED @b9680cfe86
(ratified-text half 3.0.0_SA_CVO @f08dfa32ad; brief half auto). Handoff 1.0.0_SA_CTO 103040: "Round 1 is the FWD-1
Black Diamond thread. Order inside it: the backfill of every held security into etf-classifications, via the FWD-7
scheduled path with bd-securities as reviewed input (103036); then the industry and O8 fields." CTO DECISION 103036:
industry is a NEW etf-classifications field beside O8, filled by the FWD-7 path, with Bloomberg's GICS industry group as
an input and never a source.

**Andrew-direct 2026-09-29 ~21:4xZ to 2.0.0_SA_COO~M, verbatim:** "the canonical table should not be overwritten by
anything in bd-securities." Record:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260929_214xZ_CANONICAL_TABLE_NOT_OVERWRITTEN_BY_BD_SECURITIES.md`.
It binds every cell that writes, or builds a writer of, `etf-classifications` (SC-k-1, SC-k-2): no existing row is
replaced or edited from bd-securities, and the writer's test proves a GLD overwrite attempt is refused.

## The rectangle (round 1)

| cell | hop / item | surfaces (PRD section 7) | outcome | status | placement | risk | depends on (observed completion) |
|---|---|---|---|---|---|---|---|
| `SC-k-1` | FWD-7 scheduled classification + the backfill census (dry run) + BD's detection step as its first caller | S08, S06 (detection reused, writer retired), S01 (consumed) | FWD-7 (feeds FWD-1) | NOT-EVALUATED | laptop | WORLD | -- |
| `SC-k-2` | instrument_kind (O8) and industry on every seed row; the seed-vs-live diff | S09, S02 | FWD-8, FWD-3 | NOT-EVALUATED | laptop | WORLD | IRPT_BCKEND IB-mr-251 drained (it edits the same seed source for the PHYS row) |
| `SC-t-1` | hop 1: the BD classifier library reads etf-classifications through the one client; fold and guesses removed | S03, S01 (consumed) | FWD-1 | NOT-EVALUATED | laptop | WORLD | -- |
| `SC-t-2` | hop 2: the BD assets dimension takes class and sub-class from the canonical row | S04 | FWD-1 | NOT-EVALUATED | laptop | WORLD | SC-t-1 |
| `SC-t-3` | hops 3-4: BD composition artifacts and client portal summary carry the canonical class; the thread's half | S05 (+ D_04, C_06 as the library's served readers) | FWD-1 | NOT-EVALUATED | laptop | WORLD | SC-t-2 |
| `SC-t-4` | hop 5: the thread trace (harness with a planted-read control) over a real local run | S20 (FWD-1 part) | FWD-1 | NOT-EVALUATED | laptop | WORLD | SC-t-3 |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED (NOT-EVALUATED is the value before a cell's instance exists).

**Chains.** A = SC-k-1 (slot ~1). B = SC-k-2 (slot ~2, spawned when IB-mr-251 drains). C = SC-t-1 -> SC-t-2 -> SC-t-3 ->
SC-t-4 (slot ~3, one queue: each consumes the previous cell's output). Fan-out 3 of 3, cap 8.

**Release order (served acts, each under its signed half, after the cells drain):**
1. SC-k-2's seed write (instrument_kind and industry on the seed rows, and IB-mr-251's PHYS row).
2. SC-k-1's first scheduled write, the backfill. It writes absent tickers only.
3. The thread deploy (SC-t-1..3) on the BD chain, then the COO's one real run of FWD-1 with SC-t-4's trace.

The thread's local builds do not wait on the backfill. Its served move does, because before the backfill most BD
holdings have no canonical row and would read unclassified.

**Write sets (disjoint).**
- SC-k-1: the new `_shared/etf_classification_scheduled.py`, its tests, and `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`.
- SC-k-2: `_shared/etf_classification.py`, `yang_pipeline/seed-etf-classifications.py`, `yang_pipeline/seed-etf-constituents.py` and its tests.
- SC-t-1: `data/black_diamond/scripts/gold/lib/etf_classifier.py`.
- SC-t-2: `data/black_diamond/scripts/silver/build_bd_assets_dim.py`.
- SC-t-3: `D_03`, `D_04`, `C_06`.
- SC-t-4: the new trace harness.
- The shared hookups in `run_gold_layer.sh` and any schedule are added by the issuer at the merge.

**Not in round 1 (enrichment backlog, PRD section 3):**
- the FWD-4 census instrument;
- the COT, INF, 49F, Lambda, lib and portal copies (items 4-9);
- the FWD-6 register, the FWD-3 and FWD-2 exercises, FWD-5.
The other firms' scheduled callers (COT, INF, 49F) ride their own pipelines' enrichment cells (C-FIRM).

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the PRD's section-2 thread hops 1-5 plus the two items CTO 103040 ordered
  inside round 1 (the FWD-7 backfill; industry and O8). By subtraction, hops 1-5 map to SC-t-1..4 and the two items to
  SC-k-1 and SC-k-2, leaving no remainder. The manifest rows not in round 1 are the enrichment backlog above, S01..S20
  minus {S01, S02, S03, S04, S05, S06, S08, S09, S20-part}.
- **Same grain.** One cell per hop or per placed item.
- **Intent coherence.** k cells write or build a writer of the table; t cells move one BD surface onto it.
- **State coherence.** No k cell moves a BD served figure. No t cell writes the table. A seed or scheduled write moves no
  existing class value except the seed rows the SC-k-2 census lists.

## Battery (round 1 of a threaded project)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. Thread round; the lens runs on the enrichment round that touches its
  surface. SC-k-1's schedule is named in its half (C-NAMES `mdpf-secclass-daily`, or BD's existing gold-layer run for
  E_18), never created here.
- `comp-iam`: RUN, because the thread touches IAM.
  - Measured: `infra/aws/terraform/bd-pipeline/iam.tf` defines the BD roles, including `bd-exporter-ec2-role` and
    `bd-gold-layer-lambda-role`.
  - Blind: which role runs the gold/silver scripts in production, and whether it can read `etf-classifications`
    (GetItem/Query/Scan). SC-t-1's census names the principal, and each half drafts the grant (desired, not applied).
  - Writer side: E_18's principal needs PutItem on `etf-classifications` conditional on absence, and loses its
    `bd-securities` write when the writer retires.
- `comp-adversary`: DECLARED-NOT-APPLICABLE. Thread round. The findings below were read at the cut anyway and are
  inlined into the faces.

**Findings inlined into the faces (read 2026-09-29 20:3xZ-21:5xZ):**
- `etf-classifications` has 344 rows (hash key `ticker`; GSIs asset-class-index and sub-asset-class-index), and
  `bd-securities` has 10,929.
- A stock row carries the GICS sector as `sub_asset_class` (AAPL -> Information Technology) and no industry.
- The BD library resolves in four layers (`etf_classifier.py:81-129`):
  1. a ticker lookup in the bd-securities scan, with a hedge -> alternatives fold at :99;
  2. a name-alias lookup (bd-securities `name_aliases` / `asset_name_raw`), with the fold at :108;
  3. name-pattern guesses (alternatives, cash, fixed income);
  4. a ticker-shape guess (any 1-5 letter ticker -> equity).
  Layers 3-4 are guesses, and layer 2 has no canonical counterpart.
- The library's readers: `silver/build_bd_assets_dim.py` (apply_blend), `gold/C_06.client_mix_timeseries.py`,
  `gold/D_03.composition_artifacts.py:116`, `gold/D_04.client_portal_summary.py:1235` (and its C_06 mix summary),
  `gold/E_25.aua_decomposition_audit.py`, and the classification seeders (retire in FWD-5).
- `E_18.detect_new_securities.py` compares the latest holdings_lots with bd-securities and writes stubs to
  bd-securities for `classify_bd_securities.py`.
- The seed path's merge rule (`seed-etf-classifications.py:72-123`): the module wins where it knows a value. A second
  seeder, `seed-etf-constituents.py`, writes stock rows. That is row MDPF_SECCLASS-S1.
- `find_by_asset_class` / `find_by_sub_asset_class` (the one client, :116-158) return every row of a class. A backfill
  of about 10k rows changes what those queries return, so SC-k-1's half names every caller of both.
