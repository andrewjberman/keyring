# CTO ADJUDICATION -- LGIC_LGCTFM `ANDREW_CARD.md`, on Andrew's unavailability

`1.0.0_SA_CTO`, 2026-09-18 ~02:2xZ. **This is a FALLBACK adjudication, not a substitute for his word.**

## The authority, and the two conditions that had to hold first

Andrew-direct 2026-09-17 ~23:5xZ at the `2.0.0_SA_COO~G` terminal, VERBATIM AND ENTIRE:

> Have CTO adjudicate the ANDREW_CARD.md if I'm not available.

Relayed as 97719, recorded at `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260917_23xxZ_CTO_ADJUDICATES_
LGCTFM_ANDREW_CARD_IF_ANDREW_UNAVAILABLE.md` @`514bc4ba0e`, and carried on this seat's own `org/XXX.md` Step 1b-F row
@`e23fc88aa4`.

**CONDITION 1 -- the card went to ANDREW FIRST.** It did: `2.0.0_SA_COO~G` delivered it to him and copied this seat in
the same act (97740). It has been with him since ~00:36Z.

**CONDITION 2 -- round 1 is TERMINAL**, which is the point at which the round would otherwise sit waiting on a human
read. **Measured, not assumed:** all 14 round-1 orders graded by `surprise-row-gate.py`'s OWN `_proof_terminal(root,
rel, order_text)` -- **14 of 14 return True**, each naming a proof-of-spec instance VALID with `--governing-order`.
**NEGATIVE CONTROL: `NFRA_OPLGTW.TO-OG-q-6`, issued minutes earlier, returns `(False, 'no proof-of-spec instance
tracked')`** -- the function is shown able to say no.

⛔ **AND A DISCLOSURE ABOUT THAT MEASUREMENT, because it is this evening's own class:** my first two callers of that
function were BOTH wrong -- the first passed the wrong arity, the second tested `r is True` against a `(bool, reason)`
TUPLE -- and **each printed "TERMINAL BY PROOF: 0 of 14"**. A confident zero from a broken reader, twice, against an
instrument that was answering correctly the whole time. The values were in the output; the counter was not reading
them. Nothing was acted on until the caller matched the signature.

## The decision put to Andrew, verbatim

> Confirm the ranked list of naming disagreements below for the blackdiamond "49financial" subject is correct and ready
> to drive remediation, or name any row that should rank differently.

## ADJUDICATION: the list is CONFIRMED as printed, with ONE correction to the card's own recommendation

**1. The RANKING is accepted.** The rule -- `irreversible, then client_facing, then live, then rules_colliding;
object_count as tiebreak` -- is applied consistently, and rank 1 (`T-0001`, the `opal-data-bd` S3 bucket) is correctly
first: it is the only row that is `client_facing` AND `live`.

**2. The card's RECOMMENDATION is WRONG BY ONE and is corrected here.** It reads *"the two rows touching a live,
client-facing surface sit above everything else"*. **Measured at the contract the card ranks: of 179 tensions,
`client_facing == true` in 1, `live == true` in 1, BOTH in 1 -- `T-0001` -- and `irreversible == true` in 0.** There is
ONE such row. The card's TABLE and its analysis sentence are both correct ("Rank 1 is the only..."); only the
recommendation overstates the population, and the recommendation is the half a decision-maker reads. **The ranking is
unaffected -- this corrects a claim, not an order.**

**3. Ranks 2-10 are TIED and their internal order is NOT confirmed as meaningful**, which the card itself says and
which this adjudication ratifies rather than softens: all nine are `irreversible: false`, `client_facing: false`,
`live: not measurable`, `rules_colliding: 1`, `object_count: 1`. Their sequence reflects arrival order. **No
remediation may be sequenced on the strength of a rank between 2 and 10**, and any question of the form "why is this
above that" inside that band is answered "they are tied; ask about the row, not the rank."

**4. READY TO DRIVE REMEDIATION: YES, with the scope limit above.** `T-0001` is the actionable head of the list.

## What this adjudication does NOT do

- It does **not** bind Andrew. He may overturn any part of it when he reads the card; this is a fallback so the round
  does not sit waiting on a human read at 02:00, which is exactly the shape his own word ("hoping to wake up tomorrow
  and all of these to be done") exists to prevent.
- It does **not** grade `FWD-4`. The answer is recorded here; the GRADE is `3.0.0_SA_CVO`'s at L9 and this seat's at
  L10, **against this record rather than against silence** -- which is the whole mechanism. A report standing in for a
  read does not close `FWD-4`; a RECORDED ANSWER does.
- It does **not** reach the other reserved classes. Vendor and egress off Opal infrastructure, unrecoverable acts,
  money and contracts, the portal freeze and any promote, and never-widen sign-off on an applied policy remain his.

## The basis, verified before adjudicating (R-41 @`233f5fd5e4`)

`2.0.0_SA_COO~G` disclosed a provenance defect in the card's own run directory (row `LGIC_LGCTFM-S3`) and asked this
seat to TEST its reading rather than take it. Tested on this seat's own instruments and it holds: `contract.json`
hashes `84d4d1e62b` in both the card's run dir and the amendment's default-off run; `MARK.json` absent everywhere;
`VINTAGE.json` still declaring the OLD run id while its contents are the later run's; `53d59778a1` an ancestor of HEAD
carrying the `ADVI_FIRMBKTS` row; and both contracts reading `graph_built 2026-09-17 18:16:22 UTC`, `registry_hash
scopes.json sha256:b2a54608f8ebbade`, 179 tensions, 184 rows, identical `ranking_rule`.

**So the card ranks the AMENDED engine's output on the CURRENT graph.** The defect is the run directory's PROVENANCE,
which is real, is S3's subject, and is `2.0.0_SA_COO~G`'s to remedy under R-40 -- it does not impeach the ranking.
