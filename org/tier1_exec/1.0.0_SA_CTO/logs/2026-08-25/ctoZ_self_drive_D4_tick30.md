# /self-drive D4 -- ticks 29-30 log (2026-08-25 04:47Z - 05:15Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE, EXECUTE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick28.md`.
**BOTH OF ANDREW'S ASKS ARE DELIVERED AND HE CONFIRMED ONE AT THE RENDER HIMSELF. This window: his 1Y realisation retired a workstream, the display gap was pinned to five lines, and I withdrew pressure from an item I had mis-ranked four times.**

## SCOPE + COMPLETION

```
D4 -> ETFS_CANON(scoping) · ETFS_POSITIONING(active) · +ETFS_INGEST(claimed, active)
  COMPLETION TEST: NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.  open TOs 6
  1 of 9 live directives · device SITEZ · 20 ahead of origin/SITEZ (integration window)
  open calls: 0 ADJUDICABLE · 2 RESERVED (Pathfinder weekend stamp · the SALXX tolerance question)
```

## ⭐ ANDREW ~04:50Z -- ONE REALISATION RETIRED A WORKSTREAM

VERBATIM: *"I just realized we only display up to 1Y anyway on the 'Performance' section ... which
means we dont need max backfill for these tickers"*
```
sized deep backfill    1,569,204 rows    (169 securities x 36.8y mean)
what was ACTUALLY run     16,265 rows    (64 securities x ~13 months)   = 1.0%
```
**Ran it: 59 of 64 returned, collision-guarded write, archive 109 -> 168 tickers.**
**RESULT on served bytes: DIVZ 8->28/29 · IDVZ 3->38/44 · PFDE 87->88/90 · PFOE 22->23/24.**
**Phase 2 RETIRED, not deferred (`2.0.0_SA_COO~Z` recorded it).**

## ⭐ ANDREW ~05:06Z -- SOVEREIGN CONFIRMATION AT THE RENDER

VERBATIM: *"We now have full performance for everything but still missing SALXX YTD and 1Y"*
>> **HE CONFIRMED `0.4.0_DE_ClientPlatform~Z`'s ADAPTER FIX AT THE PAGE BEFORE ANY OF US VERIFIED IT
AT A DIFF.** <<

## ⛔ THE DISPLAY GAP -- AND MY THIRD ARTIFACT-vs-DISPLAY ERROR

I told Andrew twice that returns were "on his page." **They were in the ARTIFACT; the page rendered
THREE of eight columns.** `0.4.0_DE_ClientPlatform~Z` built the instrument that settled it -- rewrote
all 187 rows with values NAMING THEIR OWN COLUMN (1D=11.11 ... 1Y=88.88), so a value cannot be
mis-mapped and a blank cannot be a misread. **QTD/YTD/1Y printed; five columns blank.**
I then grounded the CAUSE at source (Rule 22 -- a symptom is not a mechanism):
```
etfAdapter.ts:90-96   returns: { QTD, YTD, '1Y' }        <- a THREE-KEY ALLOWLIST
HoldingsTab.tsx:1053  performancePeriods = [...8 windows] <- the renderer ALREADY expected eight
```
⭐ **THEIR FIX BEAT MY SPEC: I said "add the five missing keys." They shipped
`returns: { ...h.returns }` @753b62a0 -- the allowlist is GONE, so it cannot go stale the next time a
window is added. I would have patched the instance; they removed the class.** **Second time tonight a
seat improved on a spec of mine by refusing its shape.**

## ⛔ THE CALENDAR HYPOTHESIS CLASS -- I HELD ONE AND ALMOST SHIPPED IT

SALXX misses 3 dates (YTD nulled by ONE absent day of 161). I formed the tidy mechanism -- *Columbus
Day and Veterans Day are BOND holidays, a govt MMF strikes no NAV, so SALXX follows SIFMA while the
producer checks NYSE* -- **and it fit two of three dates.**
**FALSIFIED by one same-class control: FXFXX (also a govt MMF) HAS all three, including
`2025-10-13 = 0` -- A REAL ZERO, NOT A MISSING ROW.**
⭐ **`3.0.0_SA_CVO~Z` then killed the ENTIRE CLASS in one measurement where three seats had been
falsifying variants one at a time:** for each missing ticker-date, how many of the other 167 tickers
have it? **164-167 of 167.** With **both** controls run: Thanksgiving 2025-11-27 present for **0 of
168** (the test CAN detect a closure) and an ordinary session for **166 of 168**.
>> **NO MARKET CLOSURE LEAVES ONE INSTRUMENT DARK WHILE 164+ OTHERS PRINT. Per-instrument gaps at the
vendor. Nothing to fetch -- I tried.** <<

## ⛔ AND I MIS-RANKED THE RESIDUE BUCKET FOUR TIMES

I called it "the last item between Andrew and complete" four times in fifty minutes and pressed two
seats on it. **It makes a KNOWN defect VISIBLE; it does not FIX anything** -- the 2.69% is ICT + MER
failing to resolve at Bloomberg. ⛔ **And Andrew was AT THE PAGE and named ONE gap, which was not this
one.** I escalated an item the sovereign had looked straight at and not raised, **while telling the
fabric to stop verifying things nobody disputes -- the same error one level up.**
✅ **RULED: daylight item, carried in ONE cell with the identifiers it exposes (2602335D · ICT · MER ·
RBGLD) -- surfacing an unresolved identifier and resolving it are two halves of one problem.**
⭐ **`0.4.0_DS_ClientPlatform~Z`'s `:196` objection was right from the start and I spent fifty minutes
pushing against it.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| served-artifact read | which securities lack 1Y | 64 -> the exact pull list |
| blp_client (cma) | 64 secs x 13 months | 59 with data, 16,265 rows |
| boto3 + collision guard | archive write | 109 -> 168 tickers, 0 overwritten |
| bloomberg_historical_data | SALXX vs FXFXX vs AAPL, same dates | **the calendar theory falsified** |
| sed/grep on portal src | the render cause | `etfAdapter.ts:90-96`, three-key allowlist |

## Blockers

**None at this seat. Both asks DELIVERED.** 2 RESERVED at Andrew: the Pathfinder weekend provenance
stamp; **whether "complete coverage or NULL" bends for an immaterial-return instrument (SALXX ~0.01%/day,
3 days ~0.03% of its own return) -- I put it to him and did NOT recommend it.**
Daylight: the residue bucket + the four unresolved identifiers, one cell, `2.0.0_SA_COO~Z` to route.
