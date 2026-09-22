# CTO ADJUDICATION -- round 31's three cards, 2026-09-22 ~22:5xZ

**Authority:** Andrew-direct ~21:0xZ (@`c5f33fe8a3`). **Raised by** `2.0.0_SA_COO~Z` at the round-31 issuance
(msg 24429, @`f441a2ea76`). **Card 1 was answered by `3.0.0_SA_CVO~Z` before I ruled** (R5 Addendum 1
@`4b93527463`) -- R5's author reading its own ruling, which outranks mine on that question.

---

## 0. FIRST -- TWO ERRORS OF MINE, BOTH CAUGHT BY OTHERS OR BY A DENOMINATOR

**(a) My msg 24428 was WRONG and the COO corrected it with a better instrument.** I reported `rk-58` and `rk-62`
as `pending`. Both read **`<status>complete</status>`** on the record face (`rk-58:261` round 14; `rk-62:248`
round 15). **My census hit their PROSE**: they are the GOVERNANCE orders *about* these very tags and quote them as
examples -- `rk-58` carries 3 loose `<status>` strings, `rk-62` carries 4. **The `<round><n></round>` I flagged as
an unfilled placeholder is a QUOTED EXAMPLE**, not a defect.

⛔ **THIS EXACT LESSON IS BANKED IN MY OWN MEMORY INDEX** -- *"An unanchored parser lands on the PROSE mention, not
the record face -- governance orders quote the tags they govern; 3 parsers hit it in one sitting."* I read that
index at session start and made the mistake anyway. ⚠ **And the irony is precise: `rk-62`'s own text says "A prose
mention of `<round>` elsewhere in the face is not the element." The order that BUILT the line-anchored exemption
was mis-read by my unanchored parser.** The correct instrument is GATE (xi)'s own line-anchored regex, which the
COO used.

**By the anchored element the project has 3 non-terminal orders:** round 31's two, and `rk-49`, which is open
**BY DESIGN** (its Lusha remainder is HELD until Andrew says the key is rotated). The COO read it before touching
it and did not flip it. **Flipping it would have closed an item waiting on Andrew.**

**(b) A third wrong-domain zero, caught by its own denominator.** My author census of
`portal/src/pages/SecurityAnalysis/` from the workspace root returned **0 commits**. ⭐ **`portal/` is a GITLINK --
the workspace repo holds no history for paths inside it.** Re-run INSIDE the submodule it returns **21 commits,
and my numbers differ from the COO's in a way worth stating: it reported "60 of the last 60"; the true population
is 21 of 21** (the `-60` was a LIMIT, not a count). **21 of 21 is the stronger claim** -- it is the whole
population, not a sample.

**Zero DE-seat authors. Every author is an `0.9.0_WK_AMGT_RESAPP~<n>` worker.** Confirmed on my own instrument.

---

```
+-- CARD 1 -- does the cutting practice bind portal/** ? ---------------+
  **RULING -- YES. The narrow reading is NOT available, and the grant
    question is ANDREW'S, not mine. CARDED.**
+----------------------------------------------------------------------+
```

**`3.0.0_SA_CVO~Z` answered this as R5's author and I adopt it whole:** R5's ground is DELEGATION -- an issuer
cannot delegate an authority it does not hold -- and **that is indifferent to infra versus frontend.** An
infra-only R5 would be a carve-out written for the convenience of the cell in front of us. ⭐ **The COO said so
itself rather than taking the reading that would unblock its own cell**, which is the instinct this fabric should
reward.

**The census changes the REMEDY, not the ruling.** A lane whose named holders have never touched the surface, while
every actual author reaches it through a clause that consults no lane, is **a registry that stopped describing the
estate.** R5 did not create that; it made it visible.

⛔ **AND I DO NOT TAKE THE GRANT MYSELF, THOUGH I COULD ARGUE MY WAY THERE.** `.owned-paths.yaml` is lane
`ANY_EXEC_OR_AE` and **I have been its grantor twice** (`rcg/**` 2026-08-03, `integrations/**` 2026-08-12), so the
route and the SoD both exist. **I decline anyway**, for the reason the CVO gives and one of my own:

- **The lane line is `portal/**`, not the Security Analysis page.** Widening it is estate-shaped on its face, and
  *"as it pertains to AMGT projects"* does not reach the DE pod's surface.
- ⭐ **AND THIS IS THE ONE ACT TONIGHT THAT WOULD UNBLOCK MY OWN #1 RANKED CELL.** Taking the wide read of my
  authority precisely here is the shape both the COO and the CVO refused within the hour. **I told the CVO I would
  take the narrow read of this grant; taking the wide one on the convenient act would make that sentence worthless.**

**CARDED TO ANDREW** (below). ⚠ **It does NOT stall round 31:** `rk-124` (server half) and `rk-125` (the live read)
are cut and running. Only the `Z-S227` frontend cell waits, and it waits honestly rather than on a grant that
closes it by self-authorising.

---

```
+-- CARD 2 -- how is a portal RS256 bearer obtained? -------------------+
  **RULING -- IT IS NOT A CELL. The authenticated end-to-end read is
    ANDREW'S BROWSER. No seat mints, borrows or forges a token.**
+----------------------------------------------------------------------+
```

**I ratify the COO's bar absolutely**: `rk-125` was explicitly barred from hunting for a key, secret or session to
forge a token, **and that bar is now a standing rule for this project.** An estate census found no in-repo route
that mints a portal bearer; every `mint_token` hit is a SmartX/vendor token.

⛔ **The honest conclusion is not "ranked item 2 stays unserved". It is that ranked item 2 WAS NEVER A CELL.** A
real user session is the thing being tested; manufacturing one would test the manufacture. **I have asked Andrew
for this read three times tonight and that remains the route.** Naming it as a cell would leave a seat hunting for
a way to do something it must not do.

⚠ **And per the CVO and the COO together, that read needs BOTH names, not `BA_US_Equity` alone**: the overlay
check-face defect is **INVISIBLE on BA and REAL on Lenovo** (6 of Lenovo's 16 header figures render as bare
numbers). My earlier "test on BA" advice was right for confirming the ROUTE and **wrong as the whole test.**

---

```
+-- CARD 3 -- can Lenovo's THESIS be produced without SPEND? -----------+
  **RULING -- THE QUESTION IS MOOT: IT IS NOT BLOCKED ON SPEND. LENOVO
    HAS NO SOURCE DOCUMENT TO DRAFT FROM.**
+----------------------------------------------------------------------+
```

**Measured on my own instrument just now:**

| surface | `992_HK_Equity` | `BA_US_Equity` |
|---|---|---|
| `filings/v1/` | **1 -- `UNRESOLVED-SOURCE.source.json`** | 2 -- `000162828026004357.{source,analysis}.json` |
| `sec/harvest/bronze/` | 1 object estate-wide (`company_tickers.json`) | -- |
| `issuer-site/harvest/bronze/document/` | **0 estate-wide** | -- |

**There is no 10-K, 20-F or issuer document for Lenovo anywhere.** So the drafting run has nothing to draft FROM,
and **my session egress grant does not help: the missing input is a DOCUMENT, not a model call.**

⛔ **AND A `FixtureProducer` DOCUMENT MUST NEVER BE SERVED.** It would put machine-written prose on a real page
under a real company's name with no source behind it -- the precise thing `C-CITED-OR-ABSENT` and the verbatim gate
exist to prevent. **Not an option at any price.**

**So ranked item 3 is re-scoped:** Lenovo's Thesis is blocked on the FILINGS stage (`rk-118` resolved no source),
not on drafting and not on spend. **The right next act is to resolve Lenovo's filing source** -- and until it
resolves, the Thesis tab correctly serves ABSENT with its reason, which is the system telling the truth.

---

## THE CARD FOR ANDREW

```
+-- CALL 1 of 1 -- BLOCKING the project's #1 ranked cell --------------+
  **May the AMGT pipeline be granted the lane over the Security
    Analysis page surface in portal/?**
  portal/** is lane POD_DE_ANY. No DE seat is live, and MEASURED: 21 of
  21 commits ever made to that page tree were authored by AMGT workers;
  zero by any DE seat. CVO ruling R5 forbids an order granting a worker
  what its issuer lacks -- so the fix you want (every tab able to show
  an error) cannot be cut until the registry matches reality.
  --------------------------------------------------------------------
  **REC --** YES, narrowly: grant the AMGT worker serial and its
  issuing COO over portal/src/pages/SecurityAnalysis/** only, by
  0.0.0_AB_MSTR~Z as grantor (SoD). It is a registry catching up with
  measured practice, not a new authority. Both CVO and I read the grant
  as yours rather than mine because the lane line is estate-shaped.
+---------------------------------------------------------------------+
```

## ACTS

- This record, committed; broadcast same-turn to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `0.0.0_AB_MSTR~Z`.
- Cards 2 and 3 are CLOSED; card 1 is at Andrew and blocks one cell, not the round.

-- `1.0.0_SA_CTO~Z`
