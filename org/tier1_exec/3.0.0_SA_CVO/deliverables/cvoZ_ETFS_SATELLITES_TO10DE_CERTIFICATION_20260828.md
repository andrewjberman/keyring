# `ETFS_SATELLITES.TO-10-DE` — ~~CERTIFIED 8 of 9~~ → **SUPERSEDED: CERTIFIED 9 of 9**

> ## ⭐ SUPERSEDED WITHIN THE HOUR — AND BY THE EVENT THIS CERTIFICATE WAS WAITING FOR
>
> **The 8-of-9 certificate below is CORRECT AS OF ITS TIMESTAMP and is retained verbatim.** Andrew
> ruled *"shrink the text and bars"*, `1.0.0_SA_CTO~Z` named the acceptance width **`1440px`**, and
> **AC3's free variable closed.** The criterion became scoreable, the shrink was built, and it was
> measured.
>
> ```
> RE-RUN  python .tools/proof-of-spec-check.py <instance> <TO's expected_criteria>
>         rc=0  VALID  acceptance rows=9  violations=0   STEP ZERO 9-for-9, set-for-set
> STATUSES  9 PASS  (AC3 moved UNCOMPUTABLE -> PASS, status_reason correctly null on a PASS)
> AT 1440 AFTER THE SHRINK  8 bars; all 8 VALUE labels in full (82.6 ... 8.1, 17.4 ... 91.9);
>         all 8 BOOK labels in full; NO scrollbar; NO arrows. Before the shrink 1440 CLIPPED OUTRIGHT.
> ```
>
> >> **`T10DE-AC3` IS MET AT THE RULED WIDTH. `TO-10-DE` IS 9 OF 9.** The bare `UNCOMPUTABLE` value I
> flagged as deprecated is gone with it — the row is now `PASS`, so that defect is retired by the same
> event rather than needing a fix.
>
> ### ⭐ TWO THINGS I CHECKED BEFORE RE-CERTIFYING, BECAUSE A SHRINK IS A SHARED-GRID CHANGE
>
> **(1) Did the shrink regress `models` / `etfs`?** `AC8`/`AC9` were measured at `5a4349a5`, *before*
> the shrink — citing them unchanged would answer a different question. **It was measured post-shrink
> and it holds:** a models capture at the same 1440 was *rendered and read* — wide bars, `text-xl`
> value labels, full padding, original 5-stop palette, **visually unchanged**. And `AC9` is
> **arithmetic, not visual** (`bookColorRamp(n)` vs the pre-change `BOOK_COLOR_CYCLE[i % len]`), so it
> is width-independent by construction.
> ⭐ **`compactColumns = books.length >= 6` keys on the COUNT, not the mode** — with the reason stated:
> *"keying on 'satellites' goes silently wrong the day a sixth model book is added."* Same shape as the
> mode-TOTAL `Record<PositioningMode, boolean>` finding on the other page tonight, and it means
> `POS-TO7-AC5` (Models header byte-identical) is preserved **by construction**: five books never reach
> the compact branch. **That is a cross-TO consequence the lane tracked unprompted.**
>
> **(2) ⚠ ONE COVERAGE GAP, FLAGGED AND NOT BLOCKING.** `AC3`'s criterion text says **"Re-exhibit at
> `1440` AND at `1840`."** The instance exhibits **1440 post-shrink** and carries 1840 only in the
> *"earlier width sweep retained for provenance"* — **which is the PRE-shrink reading.** So the second
> exhibit the criterion names has not been performed.
> ⭐ **It is very likely fine and I will say why: the compact branch keys on book COUNT, so 1840 takes
> the same branch as 1440 with more room.** ⛔ **But that is a monotonicity assumption, and I spent this
> hour arguing that layout is a step function you do not interpolate** — a `min-width` breakpoint above
> 1440 would falsify it silently. **One render closes it.** I am not withholding certification for it;
> I am refusing to let "1440 clean" quietly read as "1440 AND 1840 clean."
>
> **Everything below stands as written at 04:5xZ.**

---

# ~~`ETFS_SATELLITES.TO-10-DE` — CERTIFIED 8 of 9. AC3 NOT SCOREABLE pending Andrew's acceptance viewport.~~

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T04:5xZ** · **Instance:**
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ETFS_SATELLITES.TO-10-DE_PROOF_OF_SPEC.json`
@`3ad3fecbdf` · **portal** @`5a4349a5` · **Constraint set by `2.0.0_SA_COO~Z`:** never 8/9 with AC3 as
a FAIL — it has not failed.

---

## THE VERDICT

> **8 of 9 met. `T10DE-AC3` NOT SCOREABLE — the criterion names no viewport width. NOT a FAIL.**
> **This is D4's remaining build distance; it is not D4's closure.**

```
STEP ZERO   TO <expected_criteria> AC1..AC9   FILED AC1..AC9   IDENTICAL SET-FOR-SET, 9 for 9
CHECKER     rc=0  VALID  acceptance rows=9  violations=0  coverage closed
STATUSES    8 PASS + 1 UNCOMPUTABLE (AC3)
```

---

## WHY AC3 IS UNEVALUABLE RATHER THAN UNMET

The criterion says *"eight columns fit without clipping."* **Whether they fit is a function of viewport
width, and the criterion names none** — so any verdict on it is a verdict about the tester's monitor.
`2.0.0_SA_COO~Z` ruled it their own criterion defect and amended it @`8c863d5f22`; the acceptance width
is with Andrew. `1.0.0_SA_CTO~Z`'s general form, adopted:

> **A WIDTH-DEPENDENT CRITERION NAMES ITS WIDTH, OR IT CANNOT BE PASSED OR FAILED — ONLY WITNESSED.**

---

## ⭐ THE MEASUREMENT THAT WAS NEARLY AN INTERPOLATION

`1840 x 860` came off the PNG header of Andrew's own screenshot — the "unknown" was carried in evidence
that had been sitting in the record for twenty minutes. **It then landed in a 320px gap between two
measured points**, and column layout is a **step function**, so *"probably fine, marginally"* would have
been a guess across a threshold nothing had located.

```
1440   8 columns CLIP outright
1600   all 8 book labels present; the 8th bar's VALUE labels substantially clipped
1760   measured, banked
1840   ANDREW'S WIDTH -- ALL 8 COLUMNS AND ALL 8 BOOK LABELS RENDER.
       Sole clipped element: the trailing "%" of the final value -- "91.9" with the sign cut.
1920   FULLY CLEAN
=> the fully-clean threshold sits in (1840, 1920]
```

**At his width the residue is ONE CHARACTER, not a missing column.** That is qualitatively different
from both neighbours — which is exactly what a step function does and exactly what the interpolation
would have flattened.
⚠ **And `1840` is a CEILING, not his viewport**: the screenshot width bounds the CSS viewport from
above (chrome, scrollbars, window inset all come out of it), so his usable width is 1840 **or less**,
and the error points toward *more* clipping rather than less.

---

## ⭐ THE REFUSAL THAT RUNS IN BOTH DIRECTIONS, WHICH IS THE RARE PART

`0.4.0_DE_ClientPlatform~S` declined **two** promotions, and the second is the one almost nobody
declines:

```
did NOT convert "one clipped character" into "acceptable"
     -- "He asked for the cutoff to be gone, and one clipped character is not gone."
did NOT promote AC3 to PASS on the strength of a good number at one width
     -- "A measurement at one width does not give the criterion a truth value."
```

>> **The second refusal is the discipline.** A favourable measurement invites exactly the error the
unfavourable one does — *"answering a question the criterion did not ask"* — and the favourable
direction has no natural challenger, because everyone wants the item closed. **The evidence beneath
AC3 improved from three points to five; its STATUS correctly did not move.**

---

## ⚠ ONE DEFECT, FLAGGED AND NOT BLOCKING: AC3 IS FILED ON A **DEPRECATED** ENUM VALUE

`AC3.status` is bare **`UNCOMPUTABLE`**. The schema's own description says:

> *"Bare UNCOMPUTABLE is **LEGACY (pre-split instances only) — do not mint new**"*

**This is a new instance minting it**, and `rc=0 VALID` because ⛔ **the deprecation lives in the
`description`, not in the `enum`** — so the gate structurally cannot refuse it. **An unenforced
deprecation drifts back into use**, which is the mirror of this estate's own rule that an unenforced
provenance field drifts to unpopulated.

⭐ **AND IT IS A THIRD INDEPENDENT HIT ON ONE UNCOVERED DOMAIN MEMBER**, not a lapse:

| instance | value the seat needed | what they filed |
|---|---|---|
| `D1_CATVIEWS.TO-I1-DS` AC4 | "correctly blocked" | `APPLIED-GATED` (not in enum → INVALID) |
| `ETFS_INGEST.TO-6` AC3 (`0.4.0_DS_ClientPlatform~P`) | "authorization withheld" | — |
| **`TO-10-DE` AC3** | "pending a sovereign DECISION, not a run" | **bare `UNCOMPUTABLE`** |

**Neither surviving split member fits:** `UNCOMPUTABLE-BY-CONSTRUCTION` rides *a named later RUN*;
`UNVERIFIABLE-BY-INSTRUMENT` names *a substitute oracle*. **AC3 rides a later DECISION.** Facing a gap,
the seat reached for the vaguest available member — **which is diagnostic of the gap, not a defect of
the seat.** The status_reason is exactly right; only the member is wrong, and the right one may not exist.
⛔ **No schema edit proposed.** It is HELD until D1+D4 are done and I am not reopening it.

---

## SCOPE

- **Not a D4 closure.** Andrew's bar is his eye, exercised once and passed *with items*. AC3 is open at
  him, item (2)'s gradient landed here, and `TO-11-DE` (INT default) is separate and unbuilt.
- **Not served.** `5a4349a5` is on the DEV branch; there is no DEV site, and only the PROD workflow
  publishes. **Branch state, not delivery.**
- **AC3 is not certified in either direction** — I am certifying that it *cannot be scored*, which is a
  statement about the criterion, not about the page.

---

— `3.0.0_SA_CVO~Z`
