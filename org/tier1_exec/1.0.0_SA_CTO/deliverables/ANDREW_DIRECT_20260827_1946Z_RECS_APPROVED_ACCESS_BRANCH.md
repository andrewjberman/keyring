# ANDREW-DIRECT 2026-08-27 ~19:4xZ — "recs approved". THE POSITIONING FORK IS SETTLED: **(b) ACCESS.**

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in response to this seat's `/open-calls` (3 cards).
**Recorded by:** `1.0.0_SA_CTO~Z` · **Law:** `org/XXX.md` — verbatim + same-turn broadcast.

---

## 1. VERBATIM

> **"recs approved"**

**Formula precedent (this is his established form for closing `/open-calls`):** `org/XXX.md` records
the same two words discharging the `/self-drive D4` clause earlier today, and the 2026-08-21 COO-row
strike (*"approved on all"* / *"recs approved"* on a numbered `/open-calls` card).

## 2. ⛔ WHAT IT COVERS — CARD BY CARD, AND ONE CARD IS **NOT** COVERED

| card | my REC | status |
|---|---|---|
| **CALL 1** — *"nobody else": visibility or access?* | **(b) ACCESS** | ✅ **APPROVED** |
| **CALL 2** — *who maintains the satellite registry?* | ⛔ **I GAVE NO REC** | ⛔ **STILL OPEN** |
| **CALL 3** — *retired AE lane: re-seat or re-scope?* | **(b) RE-SCOPE** | ✅ **APPROVED** |

>> ⛔ **CALL 2 CARRIED NO RECOMMENDATION, SO "recs approved" CANNOT HAVE APPROVED ONE.** My card said
   so explicitly: *"REC — none, deliberately, and that is the finding"*, because any seat naming the
   maintainer would be naming one **by inference**, which IS the unowned-list failure `SAT-inv-2`
   exists to refuse. **`REGISTRY_MAINTAINER = None` STAYS `None`. Nobody may read this approval as
   filling that slot.** Reading a blanket approval onto a card that asked for a name he did not give
   is exactly the widening this estate forbids. <<

## 3. WHAT (b) ACCESS SETTLES — R5 IS UNBLOCKED

His ~18:5xZ directive asked for the patterns analysed (**R4, done**), a spec designed (**R5, was
blocked on this fork**) and rigorous breakage validation (**R6**).

**"Nobody else" is an ACCESS boundary, not a UI-visibility statement.** Therefore:

- ⛔ **THE SHIPPED CLIENT-SIDE GATE IS NECESSARY AND NOT SUFFICIENT.** `modesFor(firm)` correctly
  hides the pill and refuses the persisted-toggle tamper — **it does not withhold the bytes.**
  Satellites are arithmetic over `positioning_data.json`, served on `api/general/` to every
  authenticated user of every firm.
- **The governing pattern is the one he has now ruled THREE times** (`ADVI_FIRMSEP` 2026-05-07,
  `MDPF_SCOPED` 2026-05-28, and this): **served-plane firm scoping** — `api/scoped/`, firm in the
  path, firm in the CDN cache key, and ⭐ **`X-Firm-Id` JWT-INJECTED, NOT request-derived**, which is
  the property that makes it real rather than decorative.
- **Cost, measured both ways:** the endpoint **already authenticates** (401 without a bearer, a
  *distinct* 401 for an invalid one), so this is **firm-discrimination work, not authentication
  work**. But `positioning_data.json` is shared with **Attribution** and `ModelPortfolioModal`, and
  **all four partner firms** reach `/positioning` — so the change is **wider than the page he named**.

## 4. IMMEDIATE CONSEQUENCE FOR THE PROD PROMOTE

My CALL 1 stated it: *"(a) → promote TO-3+TO-4 together; (b) → hold until scoping lands."*
**He ruled (b). THE ETFS_SATELLITES PROD PROMOTE IS HELD.** DEV is unaffected and stays 7 ahead.
⛔ **This is his ruling flowing through my own stated consequence — NOT a new gate I am inventing.**

## 5. CALL 3 — RE-SCOPE APPROVED

The AE-class work does **not** get the retired seat back. **Five items re-scope to live lanes:** my
`build_package.py` interlock fix, 3 armed channel rows, and 3 D4 AE TOs. `2.0.0_SA_COO~Z` holds the
re-scoping; `0.0.0_AB_MSTR~Z` holds any spawn that follows.

-- `1.0.0_SA_CTO~Z`
