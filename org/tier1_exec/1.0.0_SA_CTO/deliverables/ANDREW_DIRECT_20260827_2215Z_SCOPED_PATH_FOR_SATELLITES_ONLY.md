# ANDREW-DIRECT 2026-08-27 ~22:1xZ — **A SCOPED API PATH FOR SATELLITES ONLY. THE PAGE'S PLUMBING IS NOT TOUCHED.**

**Received at:** the `1.0.0_SA_CTO~Z` terminal, answering `/open-calls` CALL 1 of 2.
**Recorded by:** `1.0.0_SA_CTO~Z` · **Law:** `org/XXX.md` — verbatim + same-turn broadcast.

---

## 1. VERBATIM

> *"I think it is better to just do a scoped api path for the satellites, that way we dont have to
> mess with the rest of the plumbing of the page and it is inobtrusive + if we decide later that it
> makes more sense to just handle this elsewhere, then doing so is not a massive effort. also agreed
> on call 2"*

**This is branch (a) of the fork put to him:** ADD a firm-scoped path for the Satellites payload —
**not** (b), re-plumbing the whole Positioning serving plane.

## 2. WHAT IT RULES

```
SATELLITES payload   -> a NEW firm-scoped API path (/api/scoped/ family)
positioning_data.json -> UNTOUCHED. Stays general, stays on /api/general/, keeps serving four firms
MODELS / ETFS         -> UNTOUCHED. No re-plumbing, no migration, no re-point
```

⭐ **HIS REASONING IS THREE-PART AND THE THIRD PART IS A PRINCIPLE, NOT A PREFERENCE:**
1. *"we dont have to mess with the rest of the plumbing of the page"* — blast radius.
2. *"it is inobtrusive"* — the general page is working and serving four firms.
3. >> *"if we decide later that it makes more sense to just handle this elsewhere, then doing so is
   not a massive effort"* — **HE PRICED REVERSIBILITY AS A SELECTION CRITERION.** Not which design is
   most correct today, but which is cheapest to be WRONG about. <<

## 3. ⛔ IT DISCHARGES THE CAVEAT I ATTACHED — IT DOES NOT DODGE IT

My CALL 1 card carried a caveat in terms: *"(a) puts Satellites on a different footing from the other
two modes, and your ~21:3xZ rule called 2-of-3 divergence 'not acceptable'."* **He ruled (a) with that
caveat in front of him.**

>> **THAT SETTLES IT AND IT MUST NOT BE RE-LITIGATED.** Either the forked-routes rule governs HOW an
   exception is built rather than WHETHER one exists, or it does not reach this case — **and that is
   his to know, not a seat's to re-derive.** A concern raised, seen, and ruled past is a DECISION. <<

⚠ **The constraint that DOES survive, because it never came from the uniformity rule:** the scoped path
must exist **BEFORE OR WITH** the Satellites payload, never after. `2.0.0_SA_COO~Z` measured
`positioning_data.json` as **Opal-common** — five Opal models, benchmarks, segments — so today there is
nothing firm-specific to leak. **Satellites IS the first firm-specific payload, and therefore IS the
trigger.** Shipping it onto the general path, even briefly, is the leak.

## 4. CONSEQUENCE FOR THE CERTIFIED CELLS — `2.0.0_SA_COO~Z`'s TO AMEND, `3.0.0_SA_CVO~Z` TO CERTIFY

`PT-a-1` reads *"**Positioning's artifact** is served through `/api/scoped/`, firm-discriminated at the
SERVING layer."* **Under this ruling that subject is wrong.** Positioning's artifact is NOT what moves —
a **new Satellites path** is created beside it.

**This is a cell AMENDMENT descending from a sovereign ruling, not a defect and not a re-cut.** The
oracle survives unchanged and is still the right one: *a fetch as firm A cannot obtain firm B's bytes,
exercised with both arms.*

⛔ **`PT-a-2` (X-Firm-Id JWT-INJECTED) and `PT-a-3` (firm in the CDN cache key) are UNAFFECTED** — they
govern the scoped path's mechanism, and the ruling creates a scoped path. If anything they bind harder:
the new path is the *only* firm-discriminated surface, so its injection and cache key carry the whole
boundary.

## 5. CALL 2 — *"also agreed on call 2"*

My REC was **none, deliberately** — that any seat naming a maintainer names one BY INFERENCE, the
unowned-list failure `SAT-inv-2` exists to refuse.

>> ⛔ **HE AGREED WITH THAT FINDING. HE DID NOT NAME A MAINTAINER, AND AGREEING THAT ONE CANNOT BE
   INFERRED IS NOT NAMING ONE.** `REGISTRY_MAINTAINER` **STAYS `None`** — now by his explicit agreement
   rather than by an unanswered card. <<

**Disposition change, stated precisely:** the item moves from *OPEN CALL AWAITING HIS WORD* to
**ACKNOWLEDGED AND DELIBERATELY UNFILLED**. It is no longer a card at him. It remains a **SHIPPING
CONDITION** — satellites cannot ship to a client surface with an unowned membership registry — and it
will need a name eventually. **Nobody may read "agreed" as filling the slot.**

-- `1.0.0_SA_CTO~Z`
