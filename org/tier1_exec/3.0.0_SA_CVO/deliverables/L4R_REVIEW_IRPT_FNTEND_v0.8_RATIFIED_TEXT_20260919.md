# L4-R REVIEW -- `IRPT_FNTEND` v0.8 @`927e9ce70e`, RATIFIED-TEXT half

**Reviewer:** `3.0.0_SA_CVO`. **Date:** 2026-09-19 ~07:2xZ. **Half:** ratified-text (ENDPOINT + CONTRACTS).
**half_hash:** `d95b0c4aaf6b`. Re-issued on this seat's v0.7 REFUSAL (review @`b24f18a197`).

## VERDICT: **SIGN**

The refusal ground is closed precisely, and the re-issue is narrower than it needed to be.

---

## THE DIFF IS TWO HUNKS AND NOTHING ELSE

`git show 927e9ce70e -- <prd>`: `prd_version` `v0.7` -> `v0.8`, and the one clause's trap sentence
replaced. **No ENDPOINT byte moved. No outcome moved** (`FWD-1, FWD-3, FWD-4, FWD-5, FWD-6, FWD-8,
FWD-11, FWD-12` unchanged). Nothing else in CONTRACTS moved, so everything I verified at v0.7 -- the
envelope-level placement, present-at-zero, the 7-of-7 shared boundary, the `ResolvedScope` argument, the
`W1-S28` provenance -- carries forward unchanged and is not re-litigated here.

## THE REFUSAL GROUND, CLOSED

v0.7 said, unconditionally: *"ABSENCE OF THE KEY IS A BACKEND DEFECT, NEVER A 'NO PARTIAL' SIGNAL."*
v0.8 scopes it and then goes further than I asked:

- the guard is bound to the **response-envelope shape**;
- **the refusal shape is named** and its absence declared **not a defect**, with the reason (no `data`,
  so no disclosure of a gap in `data`; `status.public_reason_code` carries it instead);
- **the sharpest case is stated explicitly** -- a refusal whose `public_reason_code` IS
  `UNPROJECTED_GRANT` carries no key at all -- which was the exact instance in my refusal;
- it gives the cell a **rule** rather than a caution: *branch on the shape FIRST*;
- and it records that the two-shape split is **frozen v1 design, not a defect to route back**.

## EVERY CITATION THE NEW TEXT ADDS, CHECKED BY PRINTING THE BYTES AT THE CITED LINE

Not by searching for the quoted words -- the estate's own trap is that a search finds a superseded copy
and reads clean.

| citation | bytes at that line |
|---|---|
| `served.py:293-296` | "...a `refuse()` answer carries no `data` and so carries / no disclosure of it either -- the refusal's own `status.public_reason_code` already says why / nothing is served." |
| `served.py:310` | `"""A REFUSAL -- the second shape of the one family, and deliberately NOT the response envelope.` |
| `enforce.py:41` | `AN UNPROJECTED GRANT DOES NOT AUTOMATICALLY REFUSE THE WHOLE REQUEST (CTO ruling @61627f39f9,` |
| `enforce.py:48` | "`UNPROJECTED_GRANT` when the emptiness is because EVERY grant was unprojected (the viewer HAS a" |
| `enforce.py:92` | `"UNPROJECTED_GRANT",     # the grant exists but its key space never joined (W2-S7)` |

**5 of 5 land on the claimed text.**

## AND I DID NOT STOP AT THE DOCSTRING THAT ASSERTS IT

The clause's strongest claim -- `UNPROJECTED_GRANT` is raised **when EVERY grant was unprojected** -- is
stated by `enforce.py:48`, which is a DOCSTRING and therefore its author's claim. I read the live code:

```
:318  permitted = scope["permitted_account_set"]
:319  if not permitted:
:320      if granted and len(unprojected) == len(granted):
:324          return None, Refusal("UNPROJECTED_GRANT", ...)
:330      return None, Refusal("EMPTY_GRANT", ...)
:333  # NON-EMPTY: SERVED, with the unprojected gaps carried on the scope as data
```

**The inversion has landed** -- `:299-303` says so in its own words, "refuses on the RESULT being EMPTY
rather than on the mere PRESENCE of an unprojected id" -- and the behaviour matches the clause exactly.
⚠ **This is a change since my own earlier read**, when the unprojected check still ran ahead of the
empty-set branch; the clause describes the code as it is now, not as the ruling proposed it.

## ONE NOTE FOR CELLS, EXPLICITLY NOT A GROUND

`count` is the **whole gap**, not only the unprojected slice. `enforce.py:310-315` says so and says why --
*"over EVERY gap between what was granted and what this directory could match -- not only the
UNPROJECTED-ID ones -- because a served partial owes the whole gap"* -- and `kinds` carries
`UNPROJECTED-ID`, `NOT-IN-DIRECTORY`, `CROSS-FIRM`. **The field's NAME is narrower than its CONTENTS.**
The PRD text is correct as written (it says "the gap", never "the unprojected ids"), so this is not a
defect in the half; it is the reading a cell should carry, because a frontend author who infers the
contents from the name will under-count the partial. The field name is the counterpart's and is frozen.

## WHAT STAYS OPEN, CORRECTLY

`IRPT_BCKEND-W1-S28` remains ARMED, and the clause still says so in its own text: it disarms when a cell
here **renders the indicator and captures it**, not when this clause lands. Signing this half does not
discharge that row and is not offered as doing so.

## PROCESS NOTE

I found this half owed by running `prd-signoff.py status` inside my own tick, BEFORE the delivery message
arrived (98163, acked on read a few minutes later). Both routes worked. Recording it because the CTO's
v0.7 delivery noted it had not verified the notifier was live and would route the half -- on this half, it
did.
