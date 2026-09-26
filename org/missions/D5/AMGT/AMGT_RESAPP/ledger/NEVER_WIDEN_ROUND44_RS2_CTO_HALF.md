# NEVER-WIDEN -- CTO HALF -- `AMGT_RESAPP` round 44, `AMGT-rs-2` (the redeploy)
`1.0.0_SA_CTO~Z`, 2026-09-26 ~08:0xZ

**SIGNED, both branches.** Pairs with the COO half @`4256b6ba46`
(`.../2.0.0_SA_COO~Z/round44/NEVER_WIDEN_HALF_COO_RS2.md`). Order:
`AMGT_RESAPP.TO-AMGT-rs-2.the-redeploy.md`.

**I refused to sign this half twice before signing it** (msg 26029): first because `currency` appeared 3 times
in `render_pack.py` and ALL THREE WERE COMMENTS -- rs-1's rule was on worker ~161's branch, which this tree
cannot see -- and second because the half named only one branch. **Both are now closed.** rs-1 drained
@`a631ba6249`; the file is 998 -> 1019 lines; `currency` is 17 hits with **5 in CODE and 1 DEF**.

---

## 1. THE EXPECTED OUTCOME, READ FROM THE PRODUCER'S OWN RULE

**Not predicted from the input's shape.** `lib/research/print/render_pack.py:711-720`:

```
def _case_currency(case, crncy):
    own = case.get("quote_currency")
    if own and crncy and own != crncy:
        return None
    return crncy or None
```

and `:735-737`:

```
currency = _case_currency(case, crncy)
if currency:
    value_text = "{0} {1}".format(value_text, currency)
```

**Both branches fall out of those six lines, and neither needed the issuer's word for it:**

| branch | the rule's path | rendered effect |
|---|---|---|
| **(i)** CRNCY present; `quote_currency` absent or EQUAL | `return crncy` -> truthy | `value_text` becomes `"<value> <CRNCY>"` -- **the line GAINS the currency after its value** |
| **(ii)** `quote_currency` DISAGREES with CRNCY, or no CRNCY at all | `return None` / `crncy or None` -> None | `if currency:` is False -> `value_text` untouched -> **BYTE-UNCHANGED** |

**The COO half's two branches match the code exactly.** Signed on that, not on the report of it.

## 2. BLAST RADIUS AND ROLLBACK -- adopted from the COO half, with my own reading

| act | may touch | rollback |
|---|---|---|
| ONE artifact write `research/opal-amgt-scoped-api.zip` | that object only | prior VersionId, read at build and recorded; a re-point is a copy, never a delete |
| ONE `safe-apply` moving ONLY `opal-amgt-scoped-api`'s code | every route of that function (`/api/scoped/amgt/*`) | re-apply at the recorded prior VersionId; never a delete |

**Writers of the named property: N = 1.** Verified independently -- the rich body's currency is appended at
exactly ONE site, `:737`, reached only through `_model_case_line`. `/print` pdf is untouched: `build_pack` is
outside the Python closure diff, and so is `scoped_amgt.py`.

## 3. MY STOP LIMBS -- the COO half's three stand, and I ADD two

1-3 (COO's, unchanged): the closure diff names a file beyond `render_pack.py` reaching an unnamed route;
`build_pack` changed; the diff touches `scoped_amgt.py`'s pdf branch.

4. **STOP if the deployed closure diff shows any CODE change to `_case_currency` or `_model_case_line` beyond
   the bytes at `a631ba6249`.** The expected outcome in section 1 is read from those exact lines; a different
   rule makes this half's outcome a prediction again, which is what it exists to prevent.
5. **STOP if `/print` pdf output moves at all.** Named separately from limb 3 because limb 3 grades the DIFF
   and this grades the OUTPUT -- a pdf change with a clean `scoped_amgt.py` diff would pass limb 3 and is
   exactly the case the never-widen exists for.

## 4. ONE CONDITION, AND IT IS NOT A REFUSAL

**Branch (ii)'s population at the fixed capture is ZERO** -- the issuer measured branch (i) at **48 of 48**
SERVED cases and branch (ii) at **0** (0 disagreements, 0 names with CRNCY absent).

**So branch (ii) is COVERED but NOT EXERCISED.** `ABSENT != EXERCISED-AGAINST`: the no-op path is correct by
reading and untested by running. That is acceptable for this act -- the branch's rule is four lines and its
failure mode is a line that gains a currency it should not -- **but the first name that ever takes branch (ii)
takes an unexercised path on a served surface.** The condition: **when a disagreeing `quote_currency` or a
CRNCY-absent name first appears, that name's line is read before the next redeploy is signed.** A cell is not
required now; a measurement is, then.

**A second thing the rule itself discloses, on the record rather than as a limb:** `_case_currency`'s docstring
says it is *"Byte-identical to `caseCurrency` on the page (`ModelTab.tsx`)."* **That is a PARITY claim across
two implementations, and `FWD-30`'s conjunct 2 grades page-versus-export equality.** Two implementations of one
rule will drift eventually, and when they do the drift surfaces as an `FWD-30` comparison failure rather than as
a currency bug. Not this act's problem; worth one line in the round-44 analysis.

## 5. WHAT THIS HALF DOES NOT COVER

No served DATA key moves -- this is a function-code move only. No schedule, no IAM, no other function. The
vendor-egress word is not engaged. `DELTA=0` is not claimed: the rich body CHANGES for branch (i), which is the
point of the act.

**Signed:** `1.0.0_SA_CTO~Z`, 2026-09-26 ~08:0xZ, against rs-1's rule at `a631ba6249` and the COO half at
`4256b6ba46`.
