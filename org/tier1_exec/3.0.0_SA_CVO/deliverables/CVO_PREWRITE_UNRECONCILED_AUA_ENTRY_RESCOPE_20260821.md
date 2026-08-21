# PRE-WRITE — the `Unreconciled_Aua` registry re-scope text, for the landing commit

**archetype:** SCRIBE
**Author:** 3.0.0_SA_CVO (cell owner) · 2026-08-21 ~0110Z · **NOT a registry edit.** The registry is
`4.0.0_SA_CRO` base's file and the bump is a base-registrar act; this is the text handed over so the
registrar is not waiting on me when the served key moves.
**Fires when:** `INF_D04.AUARENAME` lands AND the next scheduled INF run has moved the served key
(N4/N5 verified: `total.aua_identity_residual` present, `total.unreconciled_aua` absent, 23 keys → 23,
bd + cot byte-unchanged at 18). **Not before** — the cell's `contested_unresolved` stands until the
rename LANDS, per Andrew's residency ruling and CRO 63978.

---

## Proposed replacement for the `Unreconciled_Aua` entry

```yaml
  Unreconciled_Aua:
    definition: >-
      NAMING-HISTORY ALIAS, resolved 2026-08-21. The name formerly carried TWO served
      computations at two grains -- the defect this entry recorded as contested. RESOLVED by
      Andrew-direct ("rec approved", ~0052Z 2026-08-21, at the CRO terminal; record
      ANDREW_DIRECT_20260821_D04_RENAME_AUA_IDENTITY_RESIDUAL.md): INF's D_04 firm-grain field
      was RENAMED to Aua_Identity_Residual -- it computes total_aua - holdings_total, a FRAMING
      IDENTITY (~0.00 by construction), and never measured attribution completeness despite what
      the old name asserted. INF's D_02 advisor-grain field KEEPS the name unreconciled_aua and
      is the sense this term now denotes: the AUA of accounts carrying no billing record, an
      attribution RESIDUAL that CAN be nonzero (measured 0.0 across all five populated advisor
      books at 2026-08-20, 35 accounts, all zero-balance -- can-be-nonzero, not is-nonzero).
      Rule 24(iv): the two quantities never moved together, which is why ONE rename resolved the
      contest rather than a re-cut of either.
    authority: >-
      ANDREW_DIRECT_20260821_D04_RENAME_AUA_IDENTITY_RESIDUAL.md (the naming act) +
      org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_DISPOSITION_UNRECONCILED_AUA_CONTEST_20260820.md
      (the three-plane disposition: source, served, deployed) + the landing commit <SHA>
    sits_at: INF platinum serving field -- ADVISOR grain (platinum/advisors/{advisor_key}/book.json)
    status: reserved_ratified
    distinct_from: >-
      Aua_Identity_Residual -- ruled TWO OBJECTS 2026-08-21; Residual = the FRAMING check at FIRM
      grain (header_metrics.json total block), this entry = the ATTRIBUTION residual at ADVISOR
      grain. Never populate one meaning the other.
```

**And the sibling entry the same act mints** (registrar's call whether it lands in the same bump):

```yaml
  Aua_Identity_Residual:
    definition: >-
      The INF firm-grain FRAMING check served at platinum/firm/header_metrics.json total block:
      total_aua MINUS holdings_total, therefore ~0.00 BY CONSTRUCTION -- it verifies that the
      passed canonical total rides the same holdings frame, and it is NOT an
      attribution-completeness signal. Attribution completeness is enforced elsewhere by D_04's
      identity_gap (fail-closed). Renamed from unreconciled_aua 2026-08-21 (Andrew-direct)
      because the old name asserted what the computation does not carry.
    authority: ANDREW_DIRECT_20260821_D04_RENAME_AUA_IDENTITY_RESIDUAL.md + landing commit <SHA>
    sits_at: INF platinum serving field -- FIRM grain (header_metrics total block)
    status: reserved_ratified
    distinct_from: Unreconciled_Aua (advisor-grain attribution residual) -- see that entry.
```

## Changelog row for the bump

> `<v>.x 2026-08-21: CONTEST RESOLVED BY NAMING ACT (Andrew-direct, CRO terminal, VERBATIM "rec
> approved") -- one name over two served computations at two grains is retired. INF D_04's
> firm-grain field renamed unreconciled_aua -> aua_identity_residual (framing identity, ~0.00 by
> construction); INF D_02's advisor-grain field keeps unreconciled_aua (attribution residual,
> can-be-nonzero). Unreconciled_Aua leaves `contested_unresolved` and is re-scoped to the D_02
> sense; Aua_Identity_Residual minted for the D_04 sense. Rule 24(iv): the two quantities do not
> move together, so ONE rename resolved both. NEVER#3 discharged pre-deploy (1.0.0_SA_CTO: FE
> renderer census zero under either name; the field is NOT in the frozen cross-firm
> header_metrics shape -- bd 18 / cot 18 ABSENT, bd key set == cot key set TRUE); deploy act
> stated REMOVE+ADD, no dual-key window; served verified 23 -> 23 on the applied plane at the
> next scheduled INF run. Residency: the entry's DATA-PLANE-CLASS relocation to its serving
> contract home is now UNBLOCKED (the residency ruling's stated condition was exactly this
> contest resolving) -- relocation remains its own act, not taken here. Registered by
> 4.0.0_SA_CRO; text pre-written by 3.0.0_SA_CVO (cell owner) with concur.`

## Two facts the registrar should NOT lose

1. **INF is not a superset of the frozen archetype.** 16 shared / +7 INF-only / **−2 INF omits**
   (`existing_client_aua`, `existing_client_count`, which bd and cot both serve). A count delta
   (23−18=5) is not a set delta. Do not let any entry prose say "extends the archetype."
2. **The 2-key omission is a SEPARATE question** with the DS lane as its natural owner — not opened
   by this act, not a rider on this deploy, no clock.

— 3.0.0_SA_CVO
