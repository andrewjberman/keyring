# AMGT_RESAPP round 32 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `4332d8f825`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-23 ~00:2xZ.

**DRAIN-END, complete: 1 of 1 terminal, 0 open.** 0 round-32 worktrees, 0 branches.
**ONE cell by measurement, not shortfall** -- s.40a/s.40b record why the other two server-side candidates
dissolved into calls, and the lane grant at Andrew still gates every visible defect.

## 1. `rk-126` -- substrate card S1 ANSWERED, zero pulls, zero spend

| criterion | result |
|---|---|
| AC0 store census | 7 objects / 4 securities, MATCHES the issuer's cut-time figure |
| AC1 Q1 field read | **18 `BEST_*` field-value instances** (6 distinct names x 3 fiscal periods) |
| AC2 Q2 vintage diff | all 3 two-vintage securities **IDENTICAL on every consensus field** |
| AC3 three-part answer | (a)/(b)/(c) present and separate; (c) not sized as an act |
| AC4 no code written | diff list EMPTY |
| AC5 spend control | `0` of 3 scripts carry any Bloomberg call token |

**Verified on MY OWN instrument, a direct leaf-diff rather than the worker's script:** 48 leaf fields per
vintage; **3 moved and all three are `/requests/N/at`**, the envelope fetch timestamps; **0 of the `BEST_*` leaves
moved**; **0 contributor/analyst-count candidates present.**

⭐ **THE DECISIVE FINDING IS ONE NOBODY ANTICIPATED, INCLUDING ME: THE CONTRIBUTOR COUNT IS ABSENT.** Zero of
seven candidate estimate/analyst-count field names appear anywhere in the schema. **That is not a detail -- it is
the third requirement for any revision test, and it is a REQUEST-SCHEMA question nothing on disk can answer.**

## 2. What S1 now says, in the three parts the criterion forced apart

- **(a) WHAT A VINTAGE CONTAINS:** 6 consensus fields (`BEST_DPS`, `BEST_EBITDA`, `BEST_EPS`,
  `BEST_PERIOD_END_DATE`, `BEST_PE_RATIO`, `BEST_SALES`) x 3 fiscal periods. **No contributor count.**
- **(b) WHAT THE STORE DEMONSTRABLY PRESERVES:** distinct vintages that a reader can diff, proven on three
  securities. **Nothing more.**
- **(c) WHAT REMAINS UNANSWERED** -- and the worker's framing is **stronger than the card I asked for**. A real
  revision test needs THREE things, not two:
  1. **Interval:** weeks, spanning at least one earnings or scheduled estimate-refresh window. Days is the floor;
     anything shorter returns a null by construction.
  2. **Pull count:** at least 2 ADDITIONAL vintages per security (3+ total) across that window, so a step change
     can be told from single-sample noise.
  3. ⭐ **A FIELD THE SCHEMA DOES NOT CARRY.** Without a contributor/estimate-count, **even a real value move
     across a weeks-long gap cannot be told apart from a change in the analyst ROSTER versus a genuine re-estimate
     by the same panel.** So the test also needs an open request-schema question answered: does Bloomberg expose an
     analyst-count field for this request type at all, and under what name?

⛔ **STATED FOR THE CTO TO CARD, EXPLICITLY NOT SIZED AS AN ACT.** The standing vendor NO is not closed by this
round, and could not have been: **the cheap answer was structurally incapable of closing it**, which is what AC3
was written to guarantee.

## 3. For the grade -- three defects in one order, all mine, all filed by the worker

### 3.1 `Z-W126-S1` -- the "~33 minutes" premise was MINE and was NEVER COMPUTED

Measured interval: **2:32:29, ~152.5 minutes**, identical to the second across all three pairs
(`12:48:48 -> 15:21:17`). **Wrong by 4.6x.** Asserted in FIVE places: decomposition s.40f, the order body, AC2's
own `<expect>`, the issuance commit message, and the message to three seats. Re-measured on my own instrument
before accepting the correction; corrected in place @`4332d8f825`.

⛔ **THE CONCLUSION IS UNCHANGED, AND THAT IS PRECISELY WHY IT SURVIVED FIVE RESTATEMENTS.** 152 minutes is still
one afternoon and still uninformative about consensus revision, so **no reader had any cause to check the figure**.
**A wrong number that does not change the argument is the hardest kind to catch.** Same family as this seat's
`s.39a` "last 60 commits" (a LIMIT read as a count). ⭐ **THE TELL BOTH TIMES IS THE SAME AND IS WORTH THE
ESTATE'S ATTENTION: a number stated in prose that no line of output ever printed.**

### 3.2 `Z-W126-S2` -- my order told the worker to do something its own grant forbade

s.6 instructs the worker to flip its own `<status>`; the order's `<paths>` does not name `task-orders/`. **The
instruction was unperformable as written.** ⭐ **The worker refused it and filed a row rather than reaching outside
its grant** -- exactly right, and the second time this round's workers have declined to exceed a grant my own text
invited them to exceed. The flip is the issuer's and is made in the same commit.

### 3.3 `Z-W126-S3` (ARMED, `1.0.0_SA_CTO` / `2.0.0_SA_COO~Z`) -- a grant the validator cannot honour

`.owned-paths.yaml` carries **no static lane entry covering `.scratch/`**, so `owned-paths-validate.py` refuses
`.scratch/r126/**` even though this order grants it at HEAD. **The worker could not commit its own scratch
scripts.** ⚠ **This is a standing estate gap, not a one-order defect** -- every cell whose criteria run scratch
scripts hits it, and every previous one apparently worked around it silently. It needs an owner.

### 3.4 Not a row, but recorded: `safe-commit` REFUSED my first close-out

The commit message carried non-ASCII glyphs. **The gate is right** -- a `U+2B50` in a commit message crashed the
deploy gate on 2026-09-01 -- and I rewrote the message rather than working around it. Noted because the refusal is
the control working, and because I had written four ASCII-clean messages tonight before letting one slip.

## 4. What this seat asks of L9/L10

1. **Card part (c)'s THREE requirements to `1.0.0_SA_CTO~Z`**, the third especially: the missing
   contributor-count field makes a revision test un-interpretable even with the right interval and pull count.
   **That is new information for the vendor decision and it points at a request-schema question, not a purchase.**
2. **`Z-W126-S3` needs an owner** -- it is an estate-wide validator gap, not this project's.
3. **Grade 3.1 as the class it is.** Two instances tonight, both mine, both numbers no output ever printed, both
   surviving because they did not change the argument. I would rather that pattern were named in the analysis than
   filed as two unrelated slips.
4. **Round 33 is not cut and will not be until this round's analysis** (LD-0521). If the lane grant lands first,
   `C-S400` is its first cell on the CTO's promotion.

**Push state: LOCAL on SITEZ @`4332d8f825` plus this commit; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).**

-- `2.0.0_SA_COO~Z`
