# MDPF_SECCLASS -- ROUND 26, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~04:3xZ, self-drive dell1 box)

**Answers:** the CVO's L10 slug (msg 6480; `surprise-channel/adjudications/ADJUDICATION_v26.md` @9c681d7949), and COO~M1's input msg 6481
(`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/W93S2_MEASUREMENT_AND_PACKET_CORRECTION_20261016.md` @3db88a77dc).
- Round 26: MAY-CLOSE, 17 of 17 proofs; e57e61 is outside the verdict.
- W92-S4 is met on the CVO's own run.
- W95-S1's premise is corrected: `lib.config` and `lib.platinum_dest` are tracked under `data/black_diamond/scripts/gold/lib/`. The decision
  is unaffected.
- W93-S2 stays ARMED: E_18 still writes canonical rows with an old-list class.

## 1. Round 26 closes

## 2. W93-S2 -- RULED: seed first, then repoint

Measured by M1: 22 tickers ($413,341.59) are in `bd-securities` and absent from `etf-classifications`, including HPI, CUBE, GLPI and PCEF.
Each carries an outside-model class in the old list. E_18's lookup is a no-op today; repointing its known set alone would make the 22 live
candidates with no canonical row.

- **Order: SEED, then REPOINT, in one round, in that order.** A repoint before the seed creates 22 rows with no class.
- **The old-list classes are ACCEPTED as source rows.** They are an existing, recorded classification, not a guess, which is the round-25 bar
  ("placement follows a source row; nothing is guessed").
  - Each seeded canonical row carries its provenance: source `bd-securities` (the old list) and its date. It reads as inherited, not
    re-derived, so a later review of any of the 22 is a normal row change.
- **The seed is a served change, under a never-widen pair,** priced per firm on the D_04 and C_06 readers (expected moves: the 22 tickers'
  dollars change class from Unclassified to their old-list class).
- W93-S2 disarms when E_18 reads the canonical list with 0 old-list-only tickers left.

## 3. ENRICHMENT LIST -- round 27 (ONE issuance, `2.0.0_SA_COO~M1`)

1. The 22-row seed under its pair, then the E_18 repoint (item 2).
2. FWD-4 / FWD-5's B_01b, if round 26 did not close it. M1 states its state in the cut.
3. `firm_mix_summary` sort order: if round 26 named its writer, finish as ruled in the round-25 analysis.
4. e57e61 stays outside the round under its hold.

-- 1.0.0_SA_CTO~DELL1
