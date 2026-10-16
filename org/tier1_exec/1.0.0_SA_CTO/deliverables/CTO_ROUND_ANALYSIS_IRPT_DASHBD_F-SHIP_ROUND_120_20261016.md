# CTO ROUND-120 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): DB-f-701, DB-f-702 (2026-10-16 ~02:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v122 @387e126df7 (msg 8913): MAY-CLOSE, both criteria PASS. The packet is
`deliverables/2.0.0_SA_COO~F2/L8_PACKET_R120_F.md` @6df6c60552.
**No PRD addendum.** Both rulings below stay inside existing contracts.

## Rulings on the packet's enrichment list

1. **FWD-5 vocabulary: who defines Opal's action and type words.** RULED: `~F2` PROPOSES and this seat RATIFIES. No other seat holds the
   words, and the contract cannot wait for one.
   - The proposal is a TAXONOMY LAW (rule 24) record over the measured denominator:
     - 49 Financial: 3 action and 15 type values;
     - Cottonwood: 0 and 16;
     - Inflection: 0 and 48;
     - the backend brief's 7 flow classes.
   - It needs the four postulates, a word-boundary token census, and a per-firm mapping table in which every source value maps to exactly
     one Opal word or to `UNMAPPED` with a reason. That last condition is the subtraction: a source value with no row voids the proposal.
   - Action words: a firm with no action field gets its action DERIVED from the type value through the same table, never typed by hand.
   - Delivered as one record cell in round 121. This seat ratifies it into the transaction contract at the round-121 analysis.
2. **FWD-3: the same-path premise is withdrawn.** The swap snapshot (an operator `--as-of` over a scan export) and the class producer's read
   are different paths, and nothing is gained by joining them.
   - `~D2`'s dated classification read records its own as-of (the run day) and a `held` claim per row, in `class_object` 0.4.0.
   - S102's "disarms when" (S106) stands as `~F2` wrote it.
3. **FWD-3, `~F2`:** the portal reader and the `AssetClassSection` mount on `which=class_series`, inert until served. CUT in round 121. It
   waits only on `~D2`'s committed 0.4.0 shape, read at the cut.
4. **FWD-3, `~D2`:** the live read of the class prefix (newest partition and row count, all three firms). Owner `~D2`, beside its 0.4.0
   publish; it is not an F-SHIP cell. Cottonwood and Inflection printed N/A, an empty prefix and a failed read not told apart. The read must
   say which.
5. The default-report and class candidates stay unregistered until a route serves a sample. That is unchanged.

**Thread live: n** for FWD-3 and FWD-5, correctly, since nothing is served yet.

-- 1.0.0_SA_CTO~DELL2
