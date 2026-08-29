# DEPLOY LEDGER — D1_CATVIEWS AC5 portal DEV -> PROD promote (promote #2)

**Status:** OPEN
**Opened:** 2026-08-29T04:00Z — before the worktree exists, before the merge exists.
**Owner:** `0.4.0_DT_ClientPlatform~Z`
**Authority:** `2.0.0_SA_COO~Z` @16027 — single authorizer per the resolution of the 14324/14291
fork. `1.0.0_SA_CTO~Z` also wrote "PROMOTE RELEASED" @16009; **that was NOT taken as the word.**
**Procedure:** `/prod-deploy` @`8af1a32981`

## WHAT IS BEING PROMOTED
```
  FROM  origin/PROD  1b91b1972957b1cc011fe366060115f112bc54e1   (live, tag portal-v2.1.171)
  TO    origin/DEV   b26c6fe6458e8fd9858f4e0cfeddbbfce83ea13d
  PAYLOAD  2 commits, ONE file (src/components/CategoryViewTree.tsx, +80/-7):
    3f762bb6  AC5: a held node may show its TOTAL -- what the STOP holds is the SPLIT
    b26c6fe6  AC5: my own guard expired the moment the work it guards against lands
  ROLLBACK  1b91b1972957b1cc011fe366060115f112bc54e1
  NEXT TAG  portal-v2.1.172
```

## PRE-MEASURED BEFORE THE ACT (03:59:14Z, re-measured at GO, not carried forward)
```
  local == origin/DEV, 0 ahead, on DEV; only a peer's ?? .frontend-dev/runners/__pycache__/
  merge-tree (non-mutating) rc=0, result tree e12c67c054183f006240cd04e19565132fb6b1d4
        == origin/DEV tree  -> the Step-4 parity gate is PREDICTED EMPTY
  SERVED BEFORE  assets/index-BMmU0cpj.js  +  assets/index-WQYUWqLe.css
```

## ⛔ THE BASELINE IS NEW — PROMOTE #1's IS DEAD
```
  index-Ce258d2k.js       promote #1's baseline. GONE. Reusing it would pass trivially.
  "Fee split unavailable"  SPENT -- already 0 on PROD, so it satisfies its own pass condition
                           BEFORE this promote runs. NOT a usable discriminator.
```
**A one-way marker is consumed by the event it detects; a content-hash renews its own baseline.**

## ACCEPTANCE BAR, STATED UP FRONT
```
  SCORED  promoted set == the 2 commits above, both sides printed
  SCORED  parity gate `git diff origin/DEV HEAD` EMPTY (any output = ABORT)
  SCORED  CI: gh -R Opal-Capital/portal, ALL workflows at the promoted headSha, conclusion=success
  SCORED  the served entry chunk FILENAME moves off index-BMmU0cpj.js   <- THE stop condition
  SCORED  annotated tag peeled: git rev-parse <tag>^{commit} == PROD head
  INFO    Last-Modified / Age / X-Cache -- PRINTED, NEVER SCORED (freshness proxy, @14304)
  NOT ACCEPTANCE  the CI success line alone; origin/PROD merely carrying the commit
```

## ⛔ THREE THINGS THAT ARE NOT DEFECTS AND MUST NOT BE REPORTED AS ONE
1. `idvz` / `pfde` / `muni` / `tax` rendering NULL — **no dollars exist for them today.** Andrew:
   *"Muni does not exist yet"*, *"Tax is the only ALT Strategy currently being traded"* (unwired).
   **null is the correct emission; 0.00 would be the defect.**
2. `global` showing no Client headline/split — **declared unimplemented aggregation**, and
   independently predicted by `0.4.0_DE_ClientPlatform~Z` as AC5 (B) holding.
3. The two dollar-bearing members rendering as human names while the two null ones render as raw
   tickers — **pre-existing, `D1_NAMEDISCOVERY` territory, not tonight's ship, not fixed mid-chain.**

## VERIFY-B IS NOT MINE, AND MY REPORT IS ITS TRIGGER
`0.4.0_DE_ClientPlatform~Z` holds a **matched served-plane BEFORE** — 5 PROD renders, real bearer,
captured 22:41-23:14Z against `index-BMmU0cpj.js`, **confirmed still-served at 03:59:14Z**, so the
pair is real rather than reconstructed. Their falsifiable prediction, stated in advance:
```
  cottonwood  Client card GAINS its headline (~$294.9M)
  global      Client card still shows NO headline (unconditional)
  ⛔ IF COTTONWOOD DOES NOT GAIN ITS HEADLINE, AC5 DID NOT LAND and this promote must NOT be
     reported as carrying it.
```

## GATE 5 — TWO PUSHES THIS SEAT CANNOT MAKE
`.tools/hooks/never-rules-gate.sh:509-566`. `0.0.0_AB_MSTR~Z` executes `push origin PROD` and the
workspace pointer push. **No `# never-override:` while the integrator is awake.**

## INVOCATION DISCIPLINE (@14317, binding)
`<cmd> > out 2>&1 ; rc=$?` with rc on the very next token; report verdict AND rc; they must agree.
No `| tail` on a run whose rc is the verdict.

## WHAT THIS PROMOTE DOES NOT CLAIM
The **scheduled pipeline**. Tonight's data came from an ad-hoc reland; `TM1-AC1` and
`CATV-TON1-AC7` require a SCHEDULED fire by their own verbatim and are unchanged by this promote.

## TIMELINE
- 2026-08-29T04:00Z — entry OPENED, before the worktree and the merge.
