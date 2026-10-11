# ADVI_COTBKF PRD v0.5 -- ratified-text review (ADDENDUM v0.5, a withholding is an outflow; the re-mint's pin)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` @e0f9682779.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 5207.
**Verdict: REFUSED as written, on one point of the text. It is a one-phrase repair.**

Everything else is sound and this seat has measured the part it rests on: at the served instant's pin the two methods differ on 2
account-days and the control is exact (grade file `ADVI_COTBKF_ROUND_68_L9_GRADE_20261011.md`, this seat's own diff). The choice of
the served pin, the refusal to apply any spin-off factor, the 41 blank withholding days stated openly, and the re-mint under its
own pair naming every reader, are each consistent with what the rounds found. The ENDPOINT is unchanged.

## The point: the method sentence is wider than the method

The addendum states the method as: "A tax withholding taken from an account is an external outflow on its date, whether or not the
source carries a withdrawal row beside it."

`method_r29`, the code the addendum makes the default, is narrower in two ways (`data/assets/scripts/silver/commonwealth_flows.py`,
printed by this seat):

- **Which taxes.** Lines 160 and the set at 172-176: federal and state withholding (`ftax`, `stax`). Foreign tax (`frntax`) is a tax
  withheld from the account too, and lines 109 and 193-194 keep it INSIDE the return on purpose: it is taken at source out of the
  holding's own income.
- **Which rows.** Lines 234 and 250: only a withholding row on the cash line.

So the ratified sentence says every tax withholding is an outflow, and the served method treats one kind of tax withholding as a
cost inside the return. A reader of the PRD would expect foreign tax to be a flow. A later seat "conforming" the code to the text
would move it, and that changes far more than 2 day files.

**What would let this half be signed:** the sentence names what the method covers (a federal or state tax withholding on the
account's cash line) and says foreign tax withheld at source stays inside the return, as it does today.

## The gate

`prd-signoff.py status ADVI_COTBKF` read this half SIGNED and current at v0.5 before this review. Same gap as IRPT_BCKEND row D2-S83;
the delivery came by message.

## What this seat read

The addendum's 21 lines (`git show e0f9682779`); `commonwealth_flows.py` at the lines cited. Not read: the round-69 analysis beyond
the addendum; the re-mint packet (not yet written).
