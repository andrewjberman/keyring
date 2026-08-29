# CVO~Z session log -- 2026-08-29 0515Z-0640Z: promote #3 VERIFIED 9 of 9, and a field I used as evidence that CANNOT DISCRIMINATE

**archetype:** VALIDATE
**secondary_archetypes:** MIXED (COORDINATE)

**Serial:** `3.0.0_SA_CVO~Z` (site-Z lane, Tier-1 CVO)
**Window:** since the 0415-0515Z log (`223539e8e1`) -> ~06:40Z
**Authority:** Andrew-direct, his three panel edits given to `0.4.0_DE_ClientPlatform~Z` at ~04:2xZ.

---

## 1. THE HEADLINE -- PROMOTE #3 VERIFIED AT THE PIXEL RUNG, 9 OF 9

```
  P1  PASS  entry chunk index-BamLAu6Q.js -> index-D9vMtGZu.js
            Last-Modified 04:08:42Z -> 06:04:25Z, AFTER the promote. BOTH legs.
  P2  PASS  no "As of 2026-08-27" subtitle under the panel header
  P3  PASS  help icon present after the title
  P4  PASS  footer "August 27th, 2026, 5:00p ET | Source: Opal Capital Analysis."
            >> "27th" NOT "26th" -- the ONE row where a PLAUSIBLE value was the failure <<
  P5  PASS  global Models: PRIMARY $1.75B first, Custom $51.90M second
  P6  PASS  global Client headline $267.63M present (edit (a) landed)
  P7  PASS  SMA card ETF Strategies only . Client card Supervised only -- unchanged
  P8  PASS  COTTONWOOD Models: Primary $178.36M FIRST, Custom $8.43M second
  P9  PASS  colours SWAPPED -- Primary takes the first segment colour at BOTH scopes
  9 PASS . 0 FAIL . 0 UNSCORED
```

**The nine rows were `0.4.0_DE_ClientPlatform~Z`'s, filed BEFORE the fire so they could not be fitted
after.** Author writes the falsifiable prediction; an independent seat scores it. **That separation
is the reason this verify is worth anything, and it was ruled rather than assumed.**

## 2. STOP: A FIELD I CITED AS EVIDENCE CANNOT DISCRIMINATE, AND I USED IT TWICE

```
  grep the To: header across my whole inbox
    2404  To: 3.0.0_SA_CVO~Z          18  To: 3.0.0_SA_CVO/~Z
      12  To: 3.0.0_SA_CVO             1  To: CORE Tier-1
  DENOMINATOR 2,435. NOT ONE lists a second recipient.
```

>> **THE `To:` FIELD IS RENDERED PER-RECIPIENT. A message to six seats shows each of them ONLY
   THEIR OWN SERIAL. It is a CONSTANT.** I cited it twice as proof a message was misaddressed. <<

**Both conclusions survive on CONTENT** -- L2/L3 are `0.7.0_AE_CloudOps~Z`'s lane; the other body
named a different seat's BLOCKED row. **Neither survives on the `To:` line.**
**AND IT GENERALISES: no seat can tell from a delivered message whether it went to one recipient or
six.** The per-recipient map lives in the SENDER's tool return. **So a reader cannot recover the
recipient set to disambiguate a bare "you" -- which is exactly why the sender naming the SERIAL is
the only fix.** The measurement stopped me making the same error a third time in one night.

## 3. P8 -- I REPORTED AN INSTRUMENT LIMIT THAT WAS A WRONG FLAG

```
  I RAN     --click "Global (All)"  -> locator timeout 30s, partner control ABSENT from
            the accessible-control list I printed
  I CONCLUDED  "I cannot switch partner with this instrument"     <- DOES NOT FOLLOW
  THE FLAG  --select cottonwood     -> SELECTED: cottonwood, documented in the script header
```

**The control list was accurate; the INFERENCE was wrong. It enumerates what `--click` can reach,
not what the page offers** -- `--click` resolves by accessible name with `exact:true` and
structurally cannot see a native `<select>`.
NOTE: **AND THE CORRECTION ARRIVED AS THE MECHANISM, NOT THE ANSWER.**
`0.4.0_DE_ClientPlatform~Z` HELD a cottonwood render and a 04:47Z PROD before-image and **offered
neither** -- sending the flag so I could score it, because their read would have made an author's
result into the certifier's verdict. **P8 is SCORED, not ACCEPTED.**

## 4. THE ROW I PRE-COMMITTED TO NOT SCORING, AND DID NOT

The Client card reads **$267.63M, 100% Opal Supervised** at global, 49financial-scoped under basis B.
**SCORED AS NEITHER DEFECT NOR PASS.** Filing it fails a correct promote; passing it launders an open
fork into a settled one. **I raised that label question, which makes me the seat most likely to
mis-score it -- so I declared the position BEFORE the render, not after.**
NOTE: **cottonwood renders BOTH legs** (Supervised $2.25M, Unsupervised $292.65M, headline $294.91M).
**So global showing one leg is the SAME suppression rule acting on a 0.00 value, not a different
card.** That settles a question I had left open.

## 5. THE HOLD THAT WAS CORRECT, AND WHY IT WAS NOT A COAST

P1 was NOT satisfied for ~4 minutes after `origin/PROD` moved. **The ref moved and the bytes had
not.** I held the render and reported position.
```
  AND I NAMED WHAT I COULD NOT TELL: CI-still-running vs edge-cache.
  My ?cb=<epoch> returned X-Cache: Hit -- what a distribution that IGNORES QUERY STRINGS returns.
  So my cache-buster may not bust. I did NOT conclude from it.
```
**"It has been a few minutes" is not evidence about a CDN.** I re-read P1 instead of inferring
propagation from elapsed time, and P1 cleared on its own at 06:04:25Z.

## 6. COMPILER TOOLS

| Tool | Run | Result | Note |
|---|---|---|---|
| `ui-smoke.mjs --origin --token` | PROD global, real bearer | PASS | PNG **READ** |
| `ui-smoke.mjs --select cottonwood` | PROD cottonwood | PASS | the flag I should have used first |
| curl entry-chunk + Last-Modified | P1, 4 reads across the window | PASS | both legs, never either |
| `git ls-remote` + `is-ancestor` | promote payload | PASS | 0e1c232d IS in fc3a4421 |
| inbox `To:` census | 2,435 messages | **FOUND MY OWN BAD EVIDENCE** | the field is a constant |

**What worked:** holding the render on P1 rather than rendering on elapsed time; and pre-declaring
the row I would refuse to score.
**What failed:** an inference from an accessible-control list, and a `To:`-line argument used twice.
**Gap found:** `--click` uses `exact:true` and cannot see native `<select>` controls -- a near-miss
name and a genuinely absent control render identically in its failure output.

## 7. BLOCKERS

**NONE AT THIS SEAT.** Owned elsewhere: the INC3 cell-id form (decomp author; option (c) now
ELIMINATED by `2.0.0_SA_COO~Z` tracing the run's own closed `omitted` list); the 0833 scope + IAM
(Andrew); `r7_comparator.py:284` (mine, held -- inert, not protective).

## 8. CURRENT STATE

- **PROD: Andrew's three edits LIVE and VERIFIED 9/9.** SMA dollars live and verified at every rung.
- **origin/SITEZ == HEAD at the last read; every commit of mine is PUSHED.**
- **NOT COVERED by any certificate of mine:** inflection ordering (no row predicted); the I2 label
  question (Andrew's); the SCHEDULED-pipeline claim (`trigger='manual'`, honest and required).

## 9. NEXT STEPS

- [`3.0.0_SA_CVO~Z`] Add the CROSS-SCOPE axis to the ratifier (global vs the sum of its declared
  constituents, per node) -- still the largest known blind spot in my own instrument.
- [`3.0.0_SA_CVO~Z`] Score the ~13:00Z and ~13:30Z scheduled fires; they discharge `TM1-AC1` and
  `CATV-TON1-AC7`, which a reland structurally cannot.
- [`1.0.0_SA_CTO~Z`] The INC3 decomp cell-id form -- two edits, unblocks every INC3 certification.
- [`Andrew`] 0833 scope + IAM; the Global-All label reading; the carve-out/additive basis
  vocabulary; the 22-day-old rung-2 scope call.

## 10. SURPRISE CHANNEL

- **OBSERVATION, INERT** -- `--click`'s `exact:true` makes a near-miss name and an absent control
  indistinguishable in its failure output. It cost me one false "instrument limit" tonight.
- **OBSERVATION, INERT** -- a delivered message cannot reveal its own recipient set, so a bare "you"
  is unrecoverable by the reader. Sender-side serial naming is the only remedy.

-- `3.0.0_SA_CVO~Z`
