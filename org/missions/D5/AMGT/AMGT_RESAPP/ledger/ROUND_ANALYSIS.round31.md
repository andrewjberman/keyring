# AMGT_RESAPP -- ROUND 31 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-22 ~23:4xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24452, ADJUDICATION_v36 @`313ada3924`) over `2.0.0_SA_COO~Z`'s L8
packet @`f656d51f06` (11,169 bytes). Round 31 issued @`f441a2ea76`, two cells.

**GRADE ACCEPTED.** 2 of 2 terminal, **12 PASS / 0 FAIL / 0 UNVERIFIABLE**, channel **552 rows, 0 non-terminal**.
Rows `C-S399` (grade), `C-S400` (the overlay, GRADUATED), `C-S401` (`W125-S1` dismissed).

---

## 1. THE ROUND'S WHOLE VALUE: WE LOOKED

Round 30's analysis refused to let anyone assume the page rendered. **`rk-125` looked** -- both names, all five
tabs, 13 captures, every PNG read. A two-cell round that answers a question nobody could answer by reasoning is
worth more than a six-cell round that advances things already understood, and **the issuer named the round as two
cells rather than padding it**, because four of the six ranked items were blocked behind calls.

## 2. THE FINDING, AND THE CVO'S SHARPENING IS THE LOAD-BEARING PART

The packet reported one defect class. **The slug split it into two, on the source, and the split decides the cut:**

| | the five tabs | `SecurityOverlay` |
|---|---|---|
| what is wrong | **DISCARDS an error that EXISTS** -- `ThesisTab:129` is `const { data, isLoading } = ...`; `isError` is never destructured, and the body is two-branch | **CANNOT RECEIVE one** -- its props (`:32-34`) are `bundle` and `isLoading` ONLY. **There is no error channel in its type contract** |
| remedy | destructure and branch | **thread the prop, THEN branch** |
| harm | misleads by **OMISSION** | misleads by **ASSERTION** |
| row | `Z-S227` | **`C-S400`, its own row** |

⛔ **A branch is not even EXPRESSIBLE in the overlay until a prop is threaded.** That is why it is its own row and
its own cell: **folding it into `Z-S227` would let the tab fix close while the false sentence survives** -- one is a
one-line change per call site, the other is a type-contract change plus a call-site change plus a branch.

## 3. ⛔ THE ASSERTION IS FALSE, AND IT IS MEASURED, NOT INFERRED

On a failed read the page renders **"No overlay data for this name yet."** Measured on the server by two seats
independently: `read_security_overlay` returns **14 header figures for `BA_US_Equity`** and **16 for
`992_HK_Equity`**.

**The producer DID write the overlay. The page tells the viewer it did not.** ⚠ **A failed read cannot support a
claim about what the PRODUCER wrote** -- it supports no claim about the producer at all. This is the exact failure
`AMGT-ri-1`'s own header names, **reappearing in the component that replaced the one it fixed.**

⭐ **The positive control is on the same screen**, which makes it diagnostic rather than theoretical: before a name
is selected, that same Lead Panel prints *"Read failure ... 401 - Invalid or expired token."* **One component tells
a viewer why. Five say nothing. One says something untrue.**

⚠ **AND IT LANDS ON MY OWN ADVICE.** I told Andrew to confirm the fix on `BA_US_Equity` **because it is 7 of 7
populated** -- which is precisely the name the sentence lies about. I corrected that to him directly before the
slug rather than letting the analysis carry it.

## 4. `rk-124` IS HALF A FIX, and is graded so

Server side the bundle now carries a top-level `check_face` list of 16 keyed by `figure_id`
(**PASS 10 / PROVISIONAL 3 / REFUSE 3**). Client side `ModelTab` and `types.ts:962` consume `check_face`;
**`SecurityOverlay` consumes none.** **Lenovo's six non-PASS header figures still render as bare numbers and
nothing a viewer sees has changed.** Not graded as a working overlay, and round 32 must not treat the server half
as the fix.

## 5. ⭐ THE PATTERN NOBODY PLANNED: THREE NEAR-MISSES ON ONE OBJECT IN ONE EVENING

| seat | the probe | what it would have reported | caught by |
|---|---|---|---|
| `2.0.0_SA_COO~Z` | matched on `mnemonic` | 0 of 14 -- a false finding | re-matching on `figure_id` |
| `3.0.0_SA_CVO~Z` | asked whether each FIGURE carried `check_face` | 0 of 16 -- "the server half is unwired" | reading the bundle's KEY LIST first |
| `1.0.0_SA_CTO~Z` | read `drafting/v1/{key}/` | 0 for both names -- "no thesis anywhere" | reading the key CONSTRUCTION at `:1442`/`:1471` |

**Three seats, one object (`scoped_amgt`'s bundles), one shape of error, all within hours.** ⛔ **Every one was a
field-name match against a remembered schema, and every one returned a CLEAN ZERO that read as a finding.**

⭐ **The discriminator was the same all three times: READ THE SHAPE BEFORE MATCHING A NAME.** The key list, the key
construction, the sibling structure. **That is cheaper than the false finding it prevents and it is now the
practice for this object.**

## 6. WHAT ROUND 32 CARRIES -- the cut is `2.0.0_SA_COO~Z`'s

**1. `C-S400`, the overlay's false sentence.** ⭐ **Promoted ABOVE `Z-S227`**: an assertion that is false is worse
than a silence, its remedy is larger (thread the prop before the branch is expressible), and **it is the only
defect that can actively misinform Andrew about data we hold.**

**2. `Z-S227`, the five tabs' error branch** -- still first among the omission defects, and its brief is now
written (packet §2). ⚠ **Both 1 and 2 are `portal/**` and BLOCKED on the lane grant at Andrew.**

**3. `rk-124`'s CLIENT half** -- `SecurityOverlay` consuming `check_face`. Also `portal/**`, same block.

**4. NOT BLOCKED, and therefore the round's spine if the grant does not land tonight:** Lenovo's filings source
(which blocks the Thesis stage), the remaining layout defects on the server side, and `Z-S229`.

⚠ **If the lane grant does not land, round 32 is a server-side round and the page's visible defects all wait.**
That is worth stating plainly rather than discovering at the cut.

## 7. SCOPE, UNCHANGED AND RESTATED

**This is the UNAUTHENTICATED view. No stage is graded as rendering.** The authenticated read's actor is **Andrew's
browser, on BOTH names** -- `BA_US_Equity` confirms the route; **only Lenovo shows the overlay's bare figures.**
What round 31 proves is that **if anything fails for him, four of six surfaces say nothing and one says something
false.**

**The evidence split is graded as stated, not rounded:** capture arm **2 of 5**, source census **5 of 5**. The
source census is the right instrument for *"no tab has an error branch"* -- a code property -- and the capture arm
proves the rendered consequence for the two it captured. **Neither seat rounded one into the other.**

---

**ROUND 31 IS CLOSED.** Round 32's cut is `2.0.0_SA_COO~Z`'s, from this document.

-- `1.0.0_SA_CTO~Z`
