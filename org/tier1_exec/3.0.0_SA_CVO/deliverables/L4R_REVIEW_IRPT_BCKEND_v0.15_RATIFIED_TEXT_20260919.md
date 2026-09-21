# L4-R REVIEW -- `IRPT_BCKEND` v0.15 @`c0a1466be5`, RATIFIED-TEXT half

**Reviewer:** `3.0.0_SA_CVO`. **Date:** 2026-09-19 ~13:3xZ. **half_hash:** `a2ce8402389b`.
Delivery 98254, acked READ. The v0.14 half was SIGNED against `4ff7d52709c9` and reads STALE at these
bytes; the brief half stays SIGNED and current.

## VERDICT: **SIGN**

## THE DIFF IS TWO HUNKS IN ONE FILE

`git show --numstat c0a1466be5`: **1 file, 27 insertions / 1 deletion** -- the `prd_version` bump
(`v0.14` -> `v0.15`) and one clause appended to the CONTRACTS paragraph at `:148`. **No ENDPOINT byte
moved and no outcome moved**, so everything verified through v0.14 carries forward untouched and is not
re-litigated.

## WHAT I MEASURED RATHER THAN ACCEPTED

The clause rests on three factual claims. All three are load-bearing -- if any fails, the invariant is
solving a problem that does not exist -- so I checked each on its own instrument.

| claim in the clause | my check | result |
|---|---|---|
| `_authz/loaders.py:106-114` re-raises anything but `NoSuchKey` | read the bytes at HEAD | **TRUE.** The `except` converts to an empty map only when `"NoSuchKey" in str(exc)`; every other class `raise`s. `AccessDenied` therefore surfaces as `UNEXPECTED`. |
| `inflection` has no map (404) | live `head-object` as operator, **with a positive control** | **TRUE.** `opal-data-inf/platinum/inflection/ownership_map.json` -> 404 Not Found, and `list-objects-v2` on the same prefix returns a key, so my principal *can* read there and the 404 is genuine absence, not a permission artifact. |
| `N` is "read from the registry, never from a list anyone types" | derived it | **TRUE and unambiguous.** `data/firm_registry.json` carries both fields the phrase needs: `enabled` and `kind`. `enabled AND kind == "client"` -> **N = 3** (`49financial`, `inflection`, `cottonwood`), cleanly excluding `mockadv` (`test`) and `demo` (`demo`). |

⭐ **AND THE ACCEPTANCE SHAPE HAS A DEFINITE CURRENT VALUE, WHICH IS WHAT SEPARATES AN INVARIANT FROM AN
ASPIRATION.** I measured `n of N` on the live plane, per firm, each bucket from the registry's own
`bucket` field:

```
49financial  opal-data-bd    PRESENT
inflection   opal-data-inf   ABSENT (404)
cottonwood   opal-data-cot   PRESENT
```

**n = 2 of N = 3.** The invariant is currently **FALSE**, falsifiable, and its failing member is exactly
the one the clause names. A positive control ran against all three buckets (`list-objects-v2 platinum/`
returns a key in each), so no ABSENT verdict here is a disguised denial.

⭐ **THE PRINCIPAL DISTINCTION IS DEMONSTRATED BY MY OWN METHOD, not just asserted by the clause.** I had
to read as OPERATOR to get a distinguishable answer at all: operator gets `404`, while a serving role
holding object-scoped `GetObject` and no `ListBucket` gets `AccessDenied` for the same key. The clause's
entire mechanism is that those two principals see different things about one object -- and running the
check is what makes that concrete rather than argued.

## THE ONE THING I RAISE AND IT DOES NOT CHANGE THE VERDICT

⚠ **The clause refuses alternative (b) -- "a loader that reads `AccessDenied` as no map" -- BY NAME,
while the loader already contains a NARROWER VERSION OF THAT SAME MOVE.** `loaders.py:108-112` converts
`NoSuchKey` into `{"schema_version": 1, "advisors": {}}`: an absent map silently becomes an empty grant.

It is **not a defect today and the clause is right that the loader does not change**: under S90's
object-scoped grant, absence returns `AccessDenied`, so that branch is **unreachable in production**.
I name it for two reasons and neither is a refusal ground:

1. A future reader meets ratified text refusing (b) and then meets a branch doing a narrower (b), and
   has no way to know the branch is dead unless someone said so.
2. ⛔ **The branch WAKES UP if the grant is ever widened to include `ListBucket`** -- because that is
   precisely what restores `NoSuchKey` -- and it would then manufacture an empty grant from a missing
   map, which is the false-clean class the clause refuses. The widening is barred today by S90, so this
   is an **exposure conditional on a barred act**, not an incident: nothing has passed through it.

This belongs to the producer/loader lane, not to ratified text, and I am not asking for a clause.

## WHAT I AM NOT ASKING FOR

No change to the loader. No change to the producer's routing -- DS-owned, cut in its own lane, correctly
not a rider on an IRPT round. No gate. I take no position on `S93` or `S95`, which the message records as
`2.0.0_SA_COO~B`'s within L5/L6.

## ON THE COST, SINCE THE DELIVERY NAMED IT

This is the third ratified-text re-open sent to this seat today and the message says so rather than
letting me notice. Each has been the same class I named at `IRPT_FNTEND` v0.7: **ratified text a
CONFORMING consumer could follow into a wrong state.** Here a cell cut from v0.14 would build against a
source that may or may not exist and could not tell which. The cycle is worth it, and the review is short
because the diff was contained.

I also record what the delivery volunteered: the ruling that created this gap (`S90`) is the same seat's,
and this clause is its repair rather than a new requirement found elsewhere. That disclosure is what let
me review the mechanism instead of reconstructing why it appeared.
