# DEPLOY LEDGER — D1_CATVIEWS Andrew's 3 panel edits, portal DEV -> PROD (promote #3)

**Status:** OPEN
**Opened:** 2026-08-29T05:57Z — before the worktree exists, before the merge exists.
**Owner:** `0.4.0_DT_ClientPlatform~Z`
**Authority:** `2.0.0_SA_COO~Z` @16329 (authorized **with a bar**), concurred `1.0.0_SA_CTO~Z` @16325
(who corrected their own over-broad brake to release it).
**Procedure:** `/prod-deploy` @`8af1a32981`

## ⛔ THE BAR, AND IT WAS SATISFIED BEFORE ANYTHING WAS STAGED
COO @16329: *"Do not fire until a verifier is confirmed live … if neither confirms: HOLD. A promote
nobody can verify is worse than a 90-minute lag."*
```
  VERIFIER CONFIRMED: 3.0.0_SA_CVO~Z @16335 -- LIVE, and the instrument is EXERCISED not asserted
    (real RS256 bearer minted from the committed smoke cred, ui-smoke --origin against PROD,
     PNG SAVED AND READ at 04:2xZ).
  0.4.0_DE_ClientPlatform~Z @16337 filed 9 FALSIFIABLE PREDICTIONS *before* the fire, so they
    cannot be fitted afterwards. They are NOT duplicating CVO's read.
```

## WHAT IS BEING PROMOTED
```
  FROM  origin/PROD  c92b4677a9b47f209696ce939f8ddf5649ab5017   (live, tag portal-v2.1.172)
  TO    origin/DEV   0e1c232d5fe1ca0f4ecf28e33fe8fb122266a3c6
  PAYLOAD  1 commit -- Andrew's three panel edits, given by him directly at ~04:2xZ:
    (a) Client-card total at global   (b) Primary before Custom   (c) canonical panel/timestamp
  ROLLBACK  c92b4677a9b47f209696ce939f8ddf5649ab5017
  NEXT TAG  portal-v2.1.173
```
⭐ **WHY HOLDING WAS NOT THE NEUTRAL OPTION:** edit (a) retires a suppression **promote #2 shipped**,
so PROD has been rendering a state Andrew personally and explicitly corrected, on the surface he is
most likely to open next. **Not shipping was itself a choice with a cost.**

## PRE-MEASURED AT GO (05:56:23Z) — re-measured, not carried forward
```
  local == origin/DEV, 0 ahead / 0 behind, on DEV; only a peer's ?? __pycache__
  merge-tree rc=0, result tree 1201bd055ef526fe52e6b6fd6a1f5d2d550a224b == origin/DEV tree
        -> the Step-4 parity gate is PREDICTED EMPTY
  SERVED BEFORE  assets/index-BamLAu6Q.js  +  assets/index-WQYUWqLe.css
```

## ⛔ THE BASELINE IS NEW AGAIN — THIRD OF THE NIGHT
```
  index-Ce258d2k.js   promote #1 baseline   DEAD
  index-BMmU0cpj.js   promote #2 baseline   DEAD
  index-BamLAu6Q.js   THIS promote's BEFORE -- and it dies the moment this fires
```
**A one-way marker is consumed by the event it detects; a content-hash renews its own baseline.**
⛔ **`ab19d657e3` (CVO's 130/130) covers the PRE-EDIT bundle and will NOT be cited for (a)/(b)/(c).**

## ACCEPTANCE BAR, STATED UP FRONT
```
  SCORED  promoted set == the 1 commit above, both sides printed
  SCORED  parity gate `git diff origin/DEV HEAD` EMPTY (any output = ABORT)
  SCORED  CI: gh -R Opal-Capital/portal, ALL workflows at the promoted headSha, conclusion=success
  SCORED  served entry chunk moves off index-BamLAu6Q.js   <- DE's P1, and the FIRST row scored
  SCORED  annotated tag peeled: rev-parse <tag>^{commit} == PROD head
  INFO    Last-Modified / Age / X-Cache -- PRINTED, NEVER SCORED
```
⭐ **DE~Z's P1 IS THE GATE ON EVERY OTHER ROW:** *if the entry chunk does not move, the promote did
not reach the edge and every prediction below it is UNINTERPRETABLE.* **Score P1 first.**

## ⛔ WHAT MUST NOT BE READ AS A DEFECT AT THE PIXEL RUNG
Edit (a) makes the served Global Client card show **267,632,047.22 with a 100%-supervised split,
both 49financial-scoped.** `1.0.0_SA_CTO~Z` @16325: **CORRECT-AS-BUILT under basis B, and it is the
open I2 sovereign fork.** `3.0.0_SA_CVO~Z` @16335 has explicitly agreed not to score it as a defect.
**A verifier who did not know this would file a finding against a correct promote.**

## GATE 5 — TWO PUSHES THIS SEAT CANNOT MAKE
`0.0.0_AB_MSTR~Z` executes `push origin PROD` and the workspace pointer push. **No override.**

## WHAT THIS PROMOTE DOES NOT CLAIM
The rendered page (`3.0.0_SA_CVO~Z`'s rung, against DE~Z's 9 pre-filed predictions), and the
**scheduled pipeline** — untouched by any promote.

## TIMELINE
- 2026-08-29T05:57Z — entry OPENED, before the worktree and the merge.
