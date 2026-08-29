# CVO~Z session log -- 2026-08-29 1100Z-1510Z: the fire landed, and my own instrument printed a false RATIFIED

**archetype:** VALIDATE
**secondary_archetypes:** MIXED (DIAGNOSE)

**Serial:** `3.0.0_SA_CVO~Z` (site-Z lane, Tier-1 CVO)
**Window:** since the 0640-1100Z log (`session_cvoZ_0640-1100Z_...`) -> ~15:10Z
**Authority:** Andrew's standing clause -- surprise-channel substance routes to this seat.

---

## 1. THE HEADLINE, AND IT IS MINE

The 13:31Z scheduled fire landed. `ratify_sma_live.py --as-of 2026-08-27 --score-fire` printed
**136 PASS / 0 FAIL, VERDICT: RATIFIED.** It was **FALSE** and I withdrew it inside ninety seconds.

```
  the 132 CONTENT assertions   read the 2026-08-27 objects -- the MANUAL RELAND's artifacts
  the AC provenance row        credited a `written` from COTTONWOOD's 2026-08-28 object
  => CONTENT from one vintage, PROVENANCE from another, ONE banner over both.
```

>> **"ONE EVIDENCE BANNER OVER TWO EVIDENCE CLASSES" -- the failure I had been naming in other
   seats' criteria all session -- IN MY OWN INSTRUMENT AT THE MOMENT IT MATTERED.** <<

**AND IT WAS THE SAME BUG I FIXED THIS MORNING, ONE LEVEL DOWN.** At ~11:2xZ I required
`(kind, status)` to come from ONE MANIFEST. Correct and incomplete: **a manifest spans scopes and
vintages, so the unit was never the manifest -- it was the OBJECT.**

## 2. THREE INSTANCES OF ONE CATEGORY ERROR IN ONE HOUR, ALL MINE

| # | Bound to | Should have been | How it hid |
|---|---|---|---|
| 1 `c9e94d0e3e` | one MANIFEST | one OBJECT | a `written` at 08-28 certified content read at 08-27 |
| 2 `dae5ea0ff4` | a run-level FLAG (`--post-reland`) | the OBJECT | flag cannot know which object it sees |
| 3 `dae5ea0ff4` | `_manifests/{as_of}/` | the KEY's own vintage | folder is keyed by the RUN's as_of; keys inside carry their own |

>> **INSTANCE 3 IS THE SHARPEST AND IS WHY 2 SHIPPED: priming from the wrong folder found nothing
   for the very object the scheduled run had just written, so the row SILENTLY FELL BACK to the flag
   branch and LOOKED LIKE IT WORKED.** A wrong-but-plausible fallback is how these survive. <<

**THE REPAIR PATTERN:** ask which SMALLEST unit the two facts must share -- never the first container
that makes the symptom stop.

## 3. WHAT THE FIRE ACTUALLY DID

```
  conflict  49financial/category-views/2026-08-27.json     as predicted
  conflict  inflection/category-views/2026-08-27.json      as predicted
  written   cottonwood/category-views/2026-08-28.json      I PREDICTED THE OPPOSITE
  written   inflection/account-distribution/2026-08-29.json  a SATURDAY as_of
  global    ZERO rows -- the cross-axis coherence gate REFUSED to emit
```

⛔ **`TM1-AC1` / `CATV-TON1-AC7` DO NOT LIFT.** Three scopes have no 08-28 object; cottonwood has one
that is content-clean on 15 of 15 substantive rows but whose `Models>Custom` is **1 of 4** populated.

⛔ **COTTONWOOD ADVANCED AND I SAID IT WOULD NOT -- and it was THE ONE LEG I CARRIED from
`1.0.0_SA_CTO~Z` rather than measuring.** I labelled it carried at the time. **The two legs I
measured held; the relayed one broke.**

⛔ **MY GLOBAL EXPLANATION WAS ALSO WRONG.** I inferred "no legs to assemble from";
`0.7.0_AE_CloudOps~Z` opened `.errors` and global had **composed at 08-28** and refused on five
members with `model_value=None` against `account_count>0`. A gate working. `0.4.0_DS_ClientPlatform~Z`
traced it to the date-conditional constituency switch at `:2392-2399` -- **which vindicates my
control-row call on Models/SMA as correct rather than merely cautious.**

## 4. THE FRONTIER INVESTIGATION (pre-fire) -- FOUR SEATS, FOUR WITHDRAWALS

I read the term three seats called unread. **Global's axis is a SET UNION (`:2281`), so `as_of_last`
is the MAX across firms, NEVER the min** -- which falsified "the feed MIN gates it." Then measured
all three legs: 49f `max(fact_model_aum_daily._day)`, inflection via `_vendor_label_of`, cottonwood
carried. **All 08-27 at ~11:4xZ.**

⚠ **AND THE FEEDS MOVED AFTER I MEASURED** -- eclipse and orion both reached `date=2026-08-29` by
~15:00Z. **I had bounded the measurement explicitly ("does not forecast the next two hours"); that
bound turned out load-bearing rather than decorative.**

⭐ **THE TRANSFERABLE HALF: a feed "at 08-28" is a PARTITION claim; the frontier consumes a `day`
COLUMN or a normalized LABEL, one trading day behind.** Four seats read partition dates as frontier
claims and built a conditional on a phantom.

## 5. SURPRISE CHANNEL -- ADJUDICATED AS OWNER

| Item | Filed by | Verdict |
|---|---|---|
| `D1_CATVIEWS-S8` | `0.4.0_DE_ClientPlatform~Z` | **FALSIFIED BY EVENTS** (distinct from S37's FALSE-WHEN-WRITTEN) |
| RTX coercion | `0.4.0_DS_ClientPlatform~Y` | **INERT CONFIRMED** -- fetched live on all 4 dates ABT is missing |
| PROOF_OF_SPEC MECE gap | `0.7.0_AE_CloudOps~M` | **REAL** -- container declares the domain; a 4th value would trade 24(i) for 24(iii) |
| `lastEventTimestamp` lag | `0.7.0_AE_CloudOps~M` | **ACCEPTED** -- fails toward making a HEALTHY run look TRUNCATED |
| inflection 08-29 key | routed by `2.0.0_SA_COO~Z` | **NOT a fabricated run date** -- content-derived from a real partition |
| base-serial HALT mail | `2.0.0_SA_COO~Z` | **INERT**; their refusal to forge `read/` is the load-bearing half |

⭐ **ABT: a DIVZ holding, continuously held, both sources frozen at 08-24, ALL EIGHT windows null on
the served artifact -- the only REAL priced holding in the estate in that state.** Benign
explanations eliminated by three seats from three directions; mechanism (a doubly-stripped CUSIP
routed to `/sedol/`) found by `2.0.0_SA_COO~Z`; owned under D4.

⭐ **THE INVERSION worth keeping: RTX's GROSSLY corrupted id is SAFER than ABT's PLAUSIBLY corrupted
one.** Gross corruption fails `isalnum()` and falls back to a ticker query; plausible corruption is
queried as legitimate and fails silently.

## 6. COMPILER TOOLS

| Tool | Run | Result | Note |
|---|---|---|---|
| `ratify_sma_live.py` | 6 invocations, 2 vintages | **FOUND 3 DEFECTS IN ITSELF** | positive + negative controls both exercised |
| `s3api` manifest/artifact reads | ~25 | PASS | denominators printed; `None` on a guessed prefix = out-of-corpus, not absence |
| independent checksum impl | CUSIP mod-10 + SEDOL, 8 values | **CORROBORATED a peer's negative control** | my own implementation, not their gate |
| `safe-commit.sh` | 4 | PASS | gate clean each time |
| background watch | 1 | PASS | fired at 13:31:22Z, no polling |

**What worked:** the UNREADABLE/INDETERMINATE rung caught the false RATIFIED when the banner did not.
**What failed:** three unit-binding errors in my own instrument inside one hour.
**Gap found:** a correction reaching 3+ carriers reads as propagated and is likelier to have skipped
the operative one.

## 7. BLOCKERS

**NONE AT THIS SEAT.** Owned elsewhere: ABT remedy (`2.0.0_SA_COO~Z`, D4); leg C (Andrew, 0833 scope);
`ETFS_POSITIONING` promote conditions (Andrew -- and `2.0.0_SA_COO~Z` correctly declined to rule them
met while closing them advances their own arm's stop-condition).

## 8. CURRENT STATE

- **PROD unchanged and correct.** The fire refused rather than served wrong; `AFTER == BEFORE`.
- `ratify_sma_live.py` at **136 scored assertions**, vintage-pinned, trigger derived from the manifest.
- Commits, **push state MEASURED PER COMMIT at 15:32Z** (`ls-remote` + `is-ancestor`, origin/SITEZ
  at `e998abbfa62e`):
  | commit | what | push state |
  |---|---|---|
  | `981368efdf` | fire scorer | **ON ORIGIN** (ancestor of `e998abbfa6`) |
  | `c9e94d0e3e` | vintage limb | LOCAL ONLY |
  | `dae5ea0ff4` | derived trigger | LOCAL ONLY |
  | `081fe91c02` | certificate amendment | LOCAL ONLY |
  | `6ea7135d04` | this log | LOCAL ONLY |
  - ⚠ **CORRECTED ~15:3xZ. The original line read "Push state: LOCAL, unread since `e998abbfa6`"
    across all four — and `981368efdf` was ALREADY ON ORIGIN.** One banner over two states, in the
    log that spends its own section 1 on that exact class. **A blanket push-state stamp is the cheap
    form of the error: the set was mixed and I wrote the majority value over all of it.**
    Push remains the integrator's act (LD-0367); nothing here asks for one.
  - ⭐ **RE-MEASURED 18:26:46Z, and the table above is now STALE — which is the point, so the first
    reading is PRESERVED rather than overwritten:**
    ```
      origin/SITEZ e7803b93d266   ALL SIX commits ON ORIGIN, incl. d02dd63823 (this correction)
      NEGATIVE CONTROL: an all-zero sha is correctly NOT an ancestor -- the predicate can fail
    ```
    **15:32Z: one of five on origin. 18:26Z: six of six. An integrator ran in between.** The 15:32Z
    row was not wrong; it aged. ⛔ **A push-state value read once and quoted later is stale BY
    CONSTRUCTION — the only sound form is `ls-remote` in the same breath as the sentence, with the
    timestamp attached.** Three seats produced a wrong push-state value in one exchange this evening;
    **the vintage stamp is what kept this one safe, not the accuracy of the reading.**

## 9. NEXT STEPS

- [`2.0.0_SA_COO~Z`] ABT under D4 -- the fix is upstream coercion and needs a TO.
- [`0.7.0_AE_CloudOps~Z`] `catvp-c` L2 on the 13:50Z publisher manifest; use the FILENAME stamp, not
  `LastModified` (local-vs-UTC rendering).
- [`Andrew`] 0833 scope; the `ETFS_POSITIONING` promote conditions.

## 10. SURPRISE CHANNEL (raised BY this seat)

- **OBSERVATION, INERT** -- one firm, one feed, TWO date semantics: `account-distribution` takes the
  eclipse partition date RAW while the axis path normalizes and bounds it. Two trading days apart in
  one run. Whether the T-1 offset applies to account COUNTS is the producer's question.
- **OBSERVATION, INERT** -- ~1 in 10 future doubly-stripped CUSIPs will be SEDOL-valid and silently
  refused repair, retaining the ABT failure. The fix is strictly better everywhere; it does not close
  the class.

-- `3.0.0_SA_CVO~Z`
