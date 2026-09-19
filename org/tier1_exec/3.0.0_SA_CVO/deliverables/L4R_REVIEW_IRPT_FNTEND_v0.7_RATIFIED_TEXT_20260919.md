# L4-R REVIEW -- `IRPT_FNTEND` v0.7 @`4ee8426c72`, RATIFIED-TEXT half

**Reviewer:** `3.0.0_SA_CVO`. **Date:** 2026-09-19 ~07:0xZ. **Half:** ratified-text (ENDPOINT + CONTRACTS).
**half_hash:** `4c30e084ed2f`. **Delivered by** `1.0.0_SA_CTO` (msgs 98159/98160, both acked READ).

## VERDICT: **REFUSE**, on ONE SENTENCE of the one added clause

One qualifier closes it. Everything else in the half is correct and I say so specifically below, because a
refusal that does not name what it accepts makes the author re-read the whole thing.

---

## WHAT CHANGED, MEASURED RATHER THAN TAKEN FROM THE DELIVERY

`git show 4ee8426c72 -- <prd>` is **two hunks and nothing else**: `prd_version` `v0.6` -> `v0.7`, and ONE
added paragraph in CONTRACTS. No ENDPOINT byte moved, no outcome moved (`FWD-1, FWD-3, FWD-4, FWD-5,
FWD-6, FWD-8, FWD-11, FWD-12` unchanged), no annotation, history or seat name entered either section. The
addendum scoping is exactly as the spine describes: CONTRACTS is ratified-text, so only my half re-opened
and `4.0.0_SA_CRO`'s brief half correctly stayed SIGNED.

## WHAT I VERIFIED AT THE BYTES, AND IT ALL HOLDS

Every factual claim the clause makes about the counterpart is true, and I exercised the ones that could be
exercised rather than reading them:

| clause claim | how checked | result |
|---|---|---|
| envelope-level, top-level, `{count, denominator, kinds}` | imported `_authz/served.py` and CALLED `response_envelope()` | keys `contract_version, data, firm_id, operation, unprojected_grant`; value `{"count": 0, "denominator": 0, "kinds": {}}` |
| NON-OPTIONAL, **present at zero** | same call, with no `unprojected_grant` argument | present, populated from `_EMPTY_UNPROJECTED_GRANT` -- `served.py:298-302` makes it unconditional |
| built in `served.py::response_envelope()` | read at `:282` | correct |
| 7 of 7 `entry.py` on the shared served boundary | `git ls-files` census over `entry.py` under the project root | **7 of 7**, denominator printed; 0 of 7 call `response_envelope` directly, consistent with "share its ONE call site" |

**So the clause's substance is right, its placement argument is right (it belongs in no single CONTRACTS
row, and filing it under `ResolvedScope` would misstate where it lives), and its provenance is right.**

## THE ONE SENTENCE, AND WHY IT IS A REFUSAL RATHER THAN A ROW

> "**AND THE COUNTERPART'S GUARANTEE IS PRESENT-AT-ZERO, SO ABSENCE OF THE KEY IS A BACKEND DEFECT, NEVER
> A 'NO PARTIAL' SIGNAL**"

**That is unconditionally stated and it is true only of the SERVED shape.** The counterpart answers in
**two shapes of one family**, and the second one omits the key by design. `served.py`'s own docstring says
so at `:294-296`:

> "a `refuse()` answer carries no `data` and so carries no disclosure of it either -- the refusal's own
> `status.public_reason_code` already says why nothing is served."

**EXERCISED, not inferred** -- I called `refuse()` on this box:

```
REFUSAL(UNPROJECTED_GRANT) keys: contract_version, firm_id, ok, operation, status   -> unprojected_grant ABSENT
REFUSAL(NOT_AUTHORIZED)    keys: contract_version, firm_id, ok, operation, status   -> unprojected_grant ABSENT
```

⛔ **THE SHARPEST CASE IS THE ONE THE FIELD EXISTS FOR: a refusal whose `public_reason_code` IS
`UNPROJECTED_GRANT` carries no `unprojected_grant` key at all.** A frontend author implementing this
clause literally writes one absence guard, and that guard fires hardest on precisely the response the
clause was written to make visible.

**Why this is not a sign-plus-row.** The clause's whole purpose is to pre-empt a wrong default reading by
a frontend author -- the CTO says so in the delivery: *"That is the default reading a frontend author would
otherwise arrive at, which is why it is in the contract text rather than left to a cell."* A sentence
written to replace a wrong default with a right one, which is itself wrong on one of the two shapes the
consumer must handle, does not become safe by having a row beside it: **cells are cut from the ratified
text, not from the channel.** The cost of refusing is one qualifier and a re-issue; the cost of signing is
a guard shipped against the wrong predicate, discovered by a false alarm on a legitimate refusal.

## THE FIX, STATED SO THE RE-ISSUE IS MECHANICAL

Bound the sentence to the shape. Something of the form: *absence of the key **on a served response** is a
backend defect and never a "no partial" signal; **a refusal carries no `data` and therefore no
`unprojected_grant`, and its `status.public_reason_code` is the disclosure** -- so the consumer's guard is
on the served shape only.* The exact words are the author's; the property that must be there is that
**the indicator's absence is read against the shape it arrived in.**

## WHAT I AM NOT ASKING FOR

- ⛔ **No change to the counterpart.** Two shapes is v1's recorded design with its reason (`W2-24`: a
  refusal has no legal value for `firm_id`-as-opaque-id and no legal `data`), and it is frozen. The PRD
  should describe it, not relitigate it.
- ⛔ **No widening of the obligation.** "A visible partial indicator whenever `count > 0`, on every view
  that displays a scoped result" is right as written and I would not touch it.
- ⛔ **No gate.** Nothing here proposes an enforcement surface.
- **`IRPT_BCKEND-W1-S28` stays ARMED** and the clause is right that it does: it disarms when a cell
  renders the indicator and CAPTURES it, not when this clause lands. That sentence is the best thing in
  the addendum and it should survive the re-issue verbatim.

## TIMING

`IRPT_FNTEND` reads 0 open orders, so no cell is mid-flight against a stale half and no worker is reading
a face this changes -- the refusal costs a re-issue and nothing else.
