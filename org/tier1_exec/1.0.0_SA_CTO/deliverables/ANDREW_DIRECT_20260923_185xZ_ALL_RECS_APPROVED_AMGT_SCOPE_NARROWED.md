# ANDREW-DIRECT -- "All recs approved", AMGT scope narrowed, DE restored

**2026-09-23 ~18:5xZ, `1.0.0_SA_CTO~Z` terminal, site Z.** Answering `/self-drive AMGT` tick 1.

## HIS WORDS, VERBATIM

> *"Sorry i killed DE because I wasnt sure what you were doing here. As long as your work sticks
> squarely to AMGT pages/pipeline/domain that is fine. All recs approved, bring DE back"*

## WHAT "ALL RECS APPROVED" COVERS -- STATED NARROWLY, BECAUSE OVER-READING AN APPROVAL IS THE FAILURE MODE

The recs put to him in tick 1, and only these four:

| call | REC as put to him | now |
|---|---|---|
| **1** | spawn a pod DE to add the missing `/api/scoped/amgt` dev proxy | ⭐ **APPROVED** (and he asked for the DE back explicitly) |
| **2** | use **port 5174**; the `5173` comment and `CLAUDE.md`'s `5175` are a doc defect | ⭐ **APPROVED** |
| **3** | **one sentence naming the never-widen half as an act those seats may perform** | ⭐ **APPROVED -- `2.0.0_SA_COO~Z` MAY SIGN ITS HALF** |
| **4** | **the same sentence closes closer `S` and the AE carrier** | ⭐ **APPROVED -- those seats hold their mandate** |

## ⛔ WHAT IT DOES **NOT** COVER -- ENUMERATED SO NOBODY INHERITS A WIDER READ

- ⛔ **It does NOT authorize the DEPLOY.** It authorizes `2.0.0_SA_COO~Z` to SIGN. **The sequence is
  unchanged: pair (CTO + COO) -> `3.0.0_SA_CVO~Z` review -> deploy.** The CVO's acceptance is IN
  ADDITION to the pair, by its own narrowing, and it refuses a cutover whose pair is absent.
- ⛔ **It lifts NO standing gate:** vendor egress still needs his per-use word; no S3 deletes; the
  portal main tree never leaves DEV; no PROD promote.
- ⛔ **It grants no lane and no path.** Seats act inside the grants they already hold.
- ⛔ **It does not make a render an ACCEPTANCE.** The deployed API still serves 179 sentences the
  ratified clause withholds; until the repair lands, a working page is a DIAGNOSTIC.

## THE SCOPE NARROWING, WHICH IS A NEW CONSTRAINT AND BINDS EVERY SEAT I DRIVE

> *"As long as your work sticks squarely to AMGT pages/pipeline/domain that is fine."*

⭐ **Read as: AMGT surfaces only -- no other portal page, pipeline, route family or domain, and no
refactor, cleanup or drive-by fix of anything passed on the way.** ⛔ **A change that appears to
require a non-AMGT surface is STOPPED AND REPORTED, never widened.**

⚠ **Why he said it matters: he stopped the first DE because its scope was unclear to him, and its
task touched `portal/vite.config.ts` -- a SHARED file serving every portal page.** ⭐ **The task was
AMGT-only in intent; the FILE was not, and the direction did not say so.** **A correct task in a
shared file reads as unbounded unless the direction bounds it explicitly.** The replacement direction
does.

## ACTS TAKEN THIS TURN

- `0.1.0_DE_MarketIntelligence` **RESPAWNED** with the narrowed scope stated explicitly: ONE proxy
  entry modeled on `security-scanner` at `:188`, **nothing else in that file**, port 5174, divergence
  reported not reconciled.
- Broadcast to `2.0.0_SA_COO~Z` (its half is now performable), `3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z`,
  `0.7.0_AE_CloudOps~A` and `0.0.0_AB_MSTR~Z`.

-- `1.0.0_SA_CTO~Z`. Commits LOCAL; push owed by `0.0.0_AB_MSTR~Z`.
