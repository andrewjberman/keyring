# AMGT_RESAPP round 31: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T23:3xZ at HEAD after `f656d51f06`, LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND31_L8_PACKET_20260922.md` @`f656d51f06` (11,169 bytes), the two orders,
row `W125-S1`, and this seat's own instruments: a source read of the five tabs and the overlay component, and
server-side calls to `scoped_amgt.read_security_overlay` for both names.

## Round state

**2 of 2 terminal:** `rk-124` (overlay check-face, server half) and `rk-125` (the live render read, read-only).
Sweep **PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12** over 2 orders. **Judgment census: 0 of 12.**

## The finding, verified here, and it is SHARPER than the packet states

The packet says 0 of 5 tabs can distinguish a failed read from an absent object. Confirmed on the source, and the
mechanism differs between the two surfaces, which matters because **the remedies differ**:

| surface | mechanism | remedy |
|---|---|---|
| the five tabs | the hook's error is **DISCARDED AT THE CALL SITE** -- e.g. `ThesisTab:129` is `const { data, isLoading } = useThesisBundle(...)`, so `isError` is never destructured; the body is `{isLoading && Loading}` then `{!isLoading && data && ...}`, with no third branch | add the branch AND destructure the error |
| `SecurityOverlay` | **THE COMPONENT CANNOT RECEIVE AN ERROR AT ALL.** Its props are `bundle` and `isLoading?` (`:32-34`) -- there is no error channel in its type contract. `:73-74` is `if (!bundle) return "No overlay data for this name yet."` | thread an error PROP from the query, then branch |

**0 of 5 tabs destructure `isError`.** The positive control is on the same page: `RankedList` carries the settled
error as its own prop with a documented header (`:57-59`), reads the status off the error object rather than the
message prose (`:76-81`), and renders "Read failure -- the ranked names could not be read." (`:146`).

### The overlay's sentence is FALSE, measured on both names

`scoped_amgt.read_security_overlay`, called here:

| name | bundle keys | header figures | identity |
|---|---|---|---|
| `BA_US_Equity` | 12 | **14** | present |
| `992_HK_Equity` | 12 | **16** | present |

So when the read fails, a viewer is told "No overlay data for this name yet." about a name whose overlay the
producer **did** write. ⛔ **Silence misleads by omission; this misleads by ASSERTION, and it asserts something
about the PRODUCER that the page cannot know from a failed read.** The COO's read that this is worse than the tab
defect is correct and I adopt it.

## `rk-124` is HALF a fix, and is graded as exactly that

Server side, read here: the bundle carries a **top-level `check_face` list of 16 entries** keyed by `figure_id`,
verdicts **PASS 10 / PROVISIONAL 3 / REFUSE 3** -- matching the COO's corrected figures. Client side, `check_face`
is consumed by `ModelTab` and declared in `types.ts:962`, and **`SecurityOverlay` consumes none of it**. So Lenovo's
three REFUSE and three PROVISIONAL header figures still render as bare numbers in the page's most prominent
position. **Not graded as a working overlay.**

⚠ **THIS SEAT'S OWN NEAR MISS, RECORDED RATHER THAN QUIETLY FIXED.** My first probe asked whether each FIGURE
carried a `check_face` key and returned **0 of 16** -- a false finding, and I would have reported the server half as
unwired. `check_face` is a SIBLING list, not a figure field. I caught it by reading the bundle's own key list before
writing. **Same class as the COO's `mnemonic`-versus-`figure_id` near miss hours earlier, on the same object.** The
discriminator both times was reading the shape rather than matching a remembered field name.

## The evidence split, graded as the COO stated it

Settled-blank is captured DIRECTLY for Thesis and Exec Management (the second with a deliberate 10-second long-wait
re-capture); Peers, Model and Posture are **source parity**, flagged as not independently captured. **Capture arm 2
of 5, source census 5 of 5.** That is sufficient for the claim actually made: "no tab has an error branch" is a
CODE property, and the source census is the right instrument for it at 5 of 5. The capture arm proves the rendered
consequence, and 2 of 5 is what it proves. **Neither is rounded up here.**

⚠ **Scope, unchanged: this is the UNAUTHENTICATED view.** Per the CTO @`6705dbd28e` the authenticated read was never
a cell, and its actor is Andrew's browser on both names. **No stage is graded as rendering.** What round 31 proves
is that IF anything fails for him, four of six surfaces say nothing and one says something untrue.

## `W125-S1`, and the remedy improving under contact

The AC1 literal writes its PNG inside `portal/` because the second `$(git rev-parse --show-toplevel)` expands AFTER
the `cd` and resolves to the gitlink's own root. The issuer had exercised the capture before issuing -- **but
exercised a VARIANT with a hand-typed absolute path.** The worker ran the literal, checked `git -C portal status`,
disarmed it the same turn, and filed the row. **The issuer's own AC5, written to enforce the lane bound, caught the
issuer's own invocation violating it.**

**Graded as the remedy IMPROVING UNDER CONTACT, not merely as a 13th instance.** The amendment -- run the
invocation's BYTES, pasted from the order, in a directory reproducing the cell's own `cd` chain -- closes the exact
gap this instance opened, at unchanged cost. **A remedy that gets sharper the first time it is tested is the
outcome we want from adopting one.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S399",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T23:35Z",
    "one_line": "L9 GRADE RECORD for round 31: 2 of 2 terminal, sweep 12/0/0, judgment 0; verified here that 0 of 5 tabs destructure isError and that SecurityOverlay has NO error channel in its props at all; the overlay's 'No overlay data' sentence is FALSE for both names (BA 14 header figures, Lenovo 16, read server-side); rk-124 graded as HALF a fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 31: PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12 over 2 orders; judgment 0 of 12.",
        "Source read: 0 of 5 tab files reference isError; ThesisTab:129 destructures only {data, isLoading}; SecurityOverlayProps (:32-34) declares bundle and isLoading only; SecurityOverlay:73-74 returns 'No overlay data for this name yet.' on a falsy bundle.",
        "Positive control on the same page: RankedList carries the settled error as its own prop (:57-59), reads status off the error object (:76-81), renders 'Read failure -- the ranked names could not be read.' (:146).",
        "scoped_amgt.read_security_overlay called here: BA_US_Equity 12 keys / 14 header figures / identity present; 992_HK_Equity 12 keys / 16 header figures / identity present.",
        "Bundle carries a top-level check_face list of 16 entries keyed by figure_id: PASS 10, PROVISIONAL 3, REFUSE 3; SecurityOverlay consumes none of it (ModelTab and types.ts:962 do)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Both cells meet their orders; the round's deliverable is a measured page defect, and the server half of the overlay fix is wired while the client half is not.",
    "notes": "Grade carrier. This seat's own near miss is recorded in the review body: a per-figure check_face probe returned 0 of 16 and would have been a false finding; check_face is a sibling list. Capture arm 2 of 5, source census 5 of 5, neither rounded up. No stage is graded as rendering.",
    "dismissal_reason": "Grade record: this row carries the round-31 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S400",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T23:35Z",
    "one_line": "GRADUATED, its OWN row and not Z-S227's scope: SecurityOverlay renders 'No overlay data for this name yet.' on any falsy bundle and its props carry no error channel, so a failed read is asserted to the viewer as a fact about the producer -- FALSE for BA (14 header figures) and Lenovo (16).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SecurityOverlayProps :32-34 declares bundle and isLoading only -- no error prop exists to branch on.",
        "SecurityOverlay :73-74 returns the sentence on any falsy bundle, whether the fetch failed or the object is absent.",
        "read_security_overlay returns 14 header figures for BA_US_Equity and 16 for 992_HK_Equity, so the sentence is false for both on a failed read."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The page distinguishes a failed read from an absent object, and never states as fact what a failed read cannot know.",
    "world_is": "The overlay asserts absence of producer output on any read failure.",
    "notes": "SEPARATE FROM Z-S227 because the remedy differs: the tabs discard an error that EXISTS at the call site and need a branch; the overlay needs an error PROP threaded before a branch is possible. Its harm also differs -- omission versus assertion. Owner: the same cell that carries Z-S227 if the lane grant lands, otherwise a seat holding portal/**. Remediation row owed at L10."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S401",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T23:35Z",
    "one_line": "DISMISSED: W125-S1, the 13th Z-S235 instance -- the AC1 literal writes inside portal/ because the second $(git rev-parse --show-toplevel) expands after the cd; graded as the remedy IMPROVING UNDER CONTACT, since the issuer's own AC5 caught the issuer's own invocation and the amendment (run the BYTES, in a directory reproducing the cell's cd chain) closes the gap at unchanged cost.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The worker ran the literal, checked git -C portal status, disarmed same-turn and filed the row.",
        "The issuer had exercised a VARIANT with a hand-typed absolute path before issuing, not the literal's bytes."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "An order's literal invocation runs as written, inside the lane its <paths> grants.",
    "world_is": "The literal resolved to the gitlink's own root; the worker caught it at execution and disarmed it.",
    "notes": "Exercising an EQUIVALENT is not exercising the LITERAL. The amendment is adopted into the L6 practice this seat ruled at ADJUDICATION_v35.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W125-S1"
    ],
    "dismissal_reason": "An issuer-text defect caught by the worker at execution, disarmed same-turn, with the class remedy amended rather than merely re-counted."
  }
]
```
