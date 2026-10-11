# ADVI_COTBKF PRD v0.6 -- ratified-text review (ADDENDUM v0.6, the method sentence narrowed)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` @df488019bf.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 5215. **Prior review:** `ADVI_COTBKF_PRD_v0.5_RATIFIED_TEXT_REVIEW_20261011.md` (REFUSED).
**Verdict: SIGNED.**

The one point of the v0.5 review is repaired. The method sentence now says what `method_r29` does, and this seat printed the lines
it describes again before signing (`data/assets/scripts/silver/commonwealth_flows.py`):

| the text | the code, printed |
|---|---|
| a federal or state withholding row (`ftax`, `stax`) | lines 179 and 181, the two members of the withholding set; line 160 names both |
| on the account's cash line | lines 234 and 250 test the row's security against the cash line |
| foreign tax is not covered and stays inside the return | line 109 ("a cost inside the return") and line 193 |

The added sentence, that a later seat does not conform the code to a wider reading, answers the risk the v0.5 review named. The
other bullets of v0.5 stand and were found sound there.

## The gate

Delivered by message, as the addenda now are.

## What this seat read

The addendum's 20 lines (`git show df488019bf`); the seven lines above.
