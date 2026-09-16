# Nine L4-R reviews, and the signature that cannot see its referent -- 3.0.0_SA_CVO

**Date:** 2026-09-16
**Task Order:** none (L4-R sign-offs are spine-owned acts; LGIC_LGCTFM-S1 intake)
**Status:** WOUND DOWN on Andrew's word (~20:3xZ)

---

## Objective

Close LGIC_LGCTFM-S1, then answer every L4-R ratified-text half delivered to this seat.

---

## Work Completed

| Item | Verdict | Review | Stamp |
|---|---|---|---|
| LGIC_LGCTFM-S1 pre-issuance intake | S1 born DISARMED | -- | aa2174b96e |
| NFRA_OPLGTW v0.3 | REFUSE (seat names in FWD-9; C6 outside contract v1.0) | bec64dea66 | 15f94697aa |
| NFRA_OPLGTW v0.4 | SIGN | ad8bb4b5c0 | e50f2b6947 |
| LGIC_CANON v1.4 | SIGN (+ brief-half C6 finding) | 9bc1cac31a | 0fc7c71160 |
| NFRA_OPLGTW v0.5 | SIGN (half hash back to v0.1's 908c9e9460c1) | 9bc1cac31a | 1807bd83a6 |
| MDPF_CANON v2.4 | REFUSE (state typed; history; + FWD-1 addendum) | 9bc1cac31a, ea5f7bcbb5 | 3959966c00 |
| MDPF_CANON v2.5 | SIGN | dabede56b6 | c4dd4afe4f |
| NFRA_OPLGTW v0.6 | REFUSE (contract v1.1 not landed; access-state table OUT-OF-PATTERN) | d7faaaab7d | b0b8254107 |
| NFRA_OPLGTW v0.7 | SIGN | 13ca2e8aa3 | 9efe1ed8bc |

**End state measured by `prd-signoff status`:**
- ADMITTED: LGIC_CANON v1.5, MDPF_CANON v2.6, NFRA_OPLGTW v0.7, LGIC_LGCTFM v1.4

**Rulings adopted from this seat's findings:**
- R-21 addendum: a disarm word names the clock's file.
- R-OG-8: the table rename, plus two binding constraints -- writes quiesced through copy and
  cutover, and the old table removed only after the rollback window.

---

## Open at wind-down (for the next session of this seat)

1. **R-OG-10 (msg 97579, ACKed):** `access` joins the contract's `operations` enum in v1.1. **UNCHECKED:**
   does the ADMITTED v0.7 CONTRACTS prose close the operation classes by enumeration? If it does, the
   new class makes the section disagree with its authority, and the half needs a re-read. My read
   was interrupted by a tool error before it returned.
2. **Grading inputs for the coming L9s, all ACKed and on record:**
   - R-26: the per-plane deploy split, used for ENFORCE cell 9.
   - R-27: ENFORCE cell 4 re-points live readers only; census set equality at the vintage.
   - R-OG-9: W4-S11 was a read-only bound excess; OG-c-2 AC6's evidence vintage is disclosed.
   - R-OG-10: AC26 re-cut to 5 tools.
3. **Carried from earlier:**
   - Clocks still ARMED: W2-S8, S24 (belt), S21, S25.
   - C-S20 has no carrier.
   - NFRA_SPMOVE L4 waits on Andrew's DONE WHEN.
4. **Push:** every commit above is LOCAL. At 20:0xZ origin/CLOUD read a13b182032, with ~55 commits
   fabric-wide ahead. Pushing is 0.0.0_AB_MSTR's, on Andrew's word.

---

## THE THING WORTH CARRYING

**A sign-off bound to a half's BYTES cannot see that half go stale when what it DESCRIBES moves.**

LGIC_CANON v1.4 re-qualified FWD-5 in ENDPOINT. The brief half's hash did not move, so its signature read
CURRENT, while four of its rows still named the superseded subject that a COO would cut C6 from. The
mechanism was correct and blind at the same time. Only a read of the OTHER half for the changed fact
found it.

And the companion, measured on myself: I handed the CTO an eight-row carrier census built from lines
two seats had already flagged. v2.5 moved all eight, and an unscoped re-read found two more. A census
seeded from findings is a scoped read wearing a denominator.

-- 3.0.0_SA_CVO
