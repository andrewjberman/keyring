# DIAL RECORD — comp-blast (CLOSE) — kuzu re-base verified, 07-31 dial discharged

**Verifier/CLOSE:** 3.0.0_SA_CVO · **Date:** 2026-08-04 ~00:5xZ · **Builder:** `0.7.0_AE_CloudOps~A`
(build @72753ea4f2, discharge @7dcebf0c6c, log @60d845c671; baseline vintage a1cab01483).
**Authority:** ANDREW_RULING_projections_default_kuzu_full_graph_20260803.md (+ fix-first addendum);
spec SPEC_comp-blast_kuzu_projection_20260803.md. **This CLOSE also discharges the comp-blast
DIALED-TOOL-FLOW left at 8/9 phases on 2026-07-31** (P8-equivalent: the builder cold-exercised from
the spec + docs; the synthesis is THIS record, committed this time).

## VERDICT: PASS — all 7 acceptance gates, exercised by the verifier (not read from the delivery)

| Gate | Verdict | Verifier's own probe |
|---|---|---|
| 1 Universe conformance | PASS | `comp-blast opal-data-mdpf` rc=0 full answer; kuzu S3_BUCKET census = 33 = projection census; node_type census printed in denominator |
| 2 Freshness overlay | PASS | live mutate→observe→revert on `data/black_diamond/scripts/gold/A_00.accounts_dimension.py`: dirty no→yes→no, content-digest 17db6da49e6c→f704f4bec632→17db6da49e6c, same-invocation; file restored clean |
| 3 Exit-code contract | PASS | 27 passed / 1 by-design skip (crash-skip offset by positive ASCII test); frozen-file assertion diff a1cab01483..72753ea4f2 EMPTY (only candidate derivation re-pointed, per caveat D — verified) |
| 4 Negative control | PASS | bogus node rc=3, denominator "20480 nodes (CANONICAL KUZU GRAPH)" + retired-universe declaration |
| 5 Defect regressions | PASS | (a) suite; (b) A_00 default/up rc=0 CONSUMER-OK 191 dependents (was: up→false phantom rc=4); (c) `load_accounts_dim` rc=5 AMBIGUOUS-SUBJECT, 14 matches, refuses; (d) `endpoint:getPlatinumPartnerAnalytics` 8 dependents rc=0 (was 0) |
| 6 Boundary declaration | PASS | universe + ruling citation in every NOT-FOUND; DECLARED EXCEPTION block prints live on stat modes (named + vintaged + scoped) |
| 7 Registration | PASS | comp-manifest-check completeness PASS; comp-output-contracts.yaml rewritten (dual vintage, address_space, failure_direction, rc=5) |

**Live-DB proof (frozen-map rule):** the kuzu snapshot-id in my battery differed from my pre-build
probe (DB rebuilt 00:14Z between them) and comp-blast's provenance tracked the NEW snapshot — the
projection reads the live canonical DB, not a copy.

## Rulings at CLOSE

- **Item A (three statistical modes on the private trace graph): DECLARED EXCEPTION ACCEPTED** as
  conformant under the ruling's exception clause — explicit, intentional, runtime-declared with
  vintage and scope; the builder's reasoning (idf population = score semantics; silent re-point
  changes what numbers MEAN) is sound and matches purpose-labeling doctrine. NOT a license to
  persist: the kuzu re-base of these modes is ROUTED RESIDUE (CTO/COO build queue), and its landing
  is a re-dial trigger. Andrew may override; surfaced in-session.
- **Item B (id-shape):** verified live — legacy `gold:A_00.accounts_dimension` resolves via the
  colon-boundary suffix tier to the full kuzu id; no fleet break; ambiguity regression banked.
- **Item C (freshness predicate):** correct restraint — the shared `_freshness_probe` expression
  untouched; kuzu vintage is a separate provenance axis.
- **Observed delta, not a defect:** A_00 dependents 143→191 — the wider universe finds more
  consumers; marker semantics unchanged.

## Baselines

Behavior baselines = the 27-test suite pair (`test_blast_exit_code_contract.py` +
`test_blast_kuzu_projection.py`) at 72753ea4f2, plus this record's probe outputs. Re-cut only
deliberately, with a committed one-line reason.

## DECLARED RE-DIAL TRIGGERS (the dial reopens on any of these)

1. kuzu CloudNode/CloudEdge SCHEMA change, or a change to comp-kuzu's freshness contract/cadence.
2. The statistical modes' kuzu re-base landing (retires the declared exception).
3. Any rename touching comp-blast or its engine modules; any comp-output-contracts.yaml edit
   naming it; any canon-surface edit describing its universe.
4. Engine change > ~50 lines in `cli.py` blast paths or `comp_blast_universe.py`.
5. comp-which/HUD routing changes that point new callers at it.
6. A caller found keying on rc semantics outside the published contract.
7. **(added post-CLOSE, ~A's wording, ratified into the template): a universe/data-source change
   re-opens the dial for every suite that DERIVES FIXTURES from it — verify the fixtures still
   SELECT, not that the suite still PASSES.** Live instance that earned it: after the universe
   swap, `test_blast_overlap_pairwise.py` sat 8/8 GREEN with four tests exercising NOTHING (stale
   `gold:`-prefixed population selector → N=0 → "no pair cleared the threshold" true by
   construction) — the vacuous-pass class with the skip symptom removed. Repaired @3a1f36e544:
   selector derived live from the territory + `_assert_non_vacuous` fails an empty sweep;
   mutant-proven (reverted selector: 3 failed/5 passed where the identical state had been 8/8).

## Residue (open, owned)

- Stat-modes re-base — **DISPOSED BY CTO RULING 20260804T002607Z (superseding this record's
  "CTO/COO routing" line the same hour):** declared exception ratified INTERIM ONLY; end-state is
  a **DECLARED TERRITORY derived from the canonical graph** (the ruling's own second clause) —
  neither the private graph nor a naive kuzu re-base (an undefined population would be traded for
  a wrong one). Owner: `0.7.0_AE_CloudOps~A` (volunteered). Acceptance terms: the population
  definition is EMITTED IN the output; scores across population definitions are NOT COMPARABLE —
  any historical series spanning the switch is re-derived, never carried forward.
  **→ DISCHARGED 2026-08-04 ~00:58Z @3a1f36e544 + 3734c4a81d:** all three modes now run on the
  canonical graph narrowed to the DECLARED TERRITORY (role-derived producer predicate, N=842 of
  20,480, definition emitted every run). **CVO-verified by exercise:** live `--all-producers` now
  prints the DECLARED TERRITORY block (role-derived over canonical kuzu + non-comparability
  warning) in place of the private-graph exception block; repaired pairwise suite re-run by
  verifier. Bulk forms of defects (c) and (b) fixed in `--compare`/`--all-producers` in the same
  motion. Re-dial trigger 2 is thereby CONSUMED; trigger 7 (below) was added from this event.
- Spec 3.5 extraction-pass absorb-or-delete — deletions RULED per P7, not taken; unchanged.
- Two naming acts at Andrew (do not block): comp-blast formal purpose line (P1); `chain`
  reserved-term collision.

— 3.0.0_SA_CVO
