# ANDREW-DIRECT 2026-10-09 ~05:3xZ -- Opal_Muni_Income is a Custom model, not ALT Strategies

**Channel:** Andrew at the `2.0.0_SA_COO~S1` terminal (dell1), 2026-10-09 ~05:3xZ, in reply to this seat's read of what
`Opal_Muni_Income` holds and the question "is this $64.1M account your 'Muni SMA', or an ordinary Opal model?".

**VERBATIM:** "no that is a custom model, we should not be putting that in ALT Strategies."

## What it rules

- **C-MUNI-VERIFY, for `Opal_Muni_Income`:** answered by a person. Verdict NO: it is NOT the "Muni SMA"; it stays a Custom model
  (Cottonwood Models > Custom) and is excluded from ALT Strategies. The reason recorded: Andrew's word above. The evidence he read: the
  account holds six public short-duration municipal ETFs (SHYD, EVSM, SUB, SHM, VTES, MEAR) plus cash, $64,119,753.85 on 2026-10-07,
  matching the Opal Rebalancer model `Opal_Muni_Income`; vendor flags `is_sma` false (CRO read
  `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_STRATID_S07_MUNI_VERIFY_20261009.md` @67e20ee89f, re-read by this seat).
- **Open call** `dell1-20261009T043711Z-9afb` closes on this word.

## Scope -- what it does NOT rule (verbatim scope; not widened)

- `Opal_Muni_Sleeve` ($0.55M, a component of another strategy): not named in his answer; still open under C-MUNI-VERIFY.
- What the "Muni SMA" member under ALT Strategies IS: not ruled; the member stays as declared, with no Cottonwood dollars mapped to it.
- FWD-3's text in the PRD: unchanged here; the PRD is `1.0.0_SA_CTO~DELL1`'s.

## What changes at this seat (MDPF_STRATID workstream 2, amendment A7)

The Muni rule row in `sma_name_rules` (member null) must no longer match `Opal_Muni_Income`, and the unidentified list no longer
lists it: it is an Opal Model, excluded as one. Carried as decomposition amendment A7, applied at the drain.
