# DEPLOY LEDGER — D1_CATVIEWS Andrew's 3 panel edits, portal DEV -> PROD (promote #3)

**Status:** CLOSED — COMPLETE
**Opened:** 2026-08-29T05:57Z — before the worktree exists, before the merge exists.
**Closed:** 2026-08-29T06:07Z — both pushes verified AT THE REMOTE, nothing half-landed.
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
- 05:58Z worktree · `bun install` rc=0 (420 pkgs, FOREGROUND) · `merge --no-ff -F` rc=0, 'ort',
  1 file +103/-75, no conflicts -> `fc3a4421715a4252471accc6e85cecca54c6e9a2`
- **PARITY GATE PASS: 0 bytes.** Merged tree `1201bd055ef526fe52e6b6fd6a1f5d2d550a224b` ==
  `origin/DEV` tree == the value `merge-tree` predicted before the merge existed.
- PUSH 1/2 by `0.0.0_AB_MSTR~Z` (GATE 5, no override): `origin/PROD c92b4677 -> fc3a4421`
- ⛔ **CI READ `in_progress` ON FIRST POLL — AND I DID NOT SCORE ANYTHING DOWNSTREAM OF IT.**
  Polled to `status=completed` first. Run 33237535289 "Deploy to Production" **conclusion=success**,
  enumerated BY headSha.
  >> **SCORING THE BUNDLE WHILE THE DEPLOY WAS STILL RUNNING WOULD HAVE PRODUCED A FALSE
     "NOTHING SHIPPED."** The deploy not having finished is not the promote having failed — and it
     was one impatient `curl` away. Same false-absence class that cost this fabric repeatedly
     tonight, avoided by waiting rather than by cleverness. <<
- TAG: `portal-v2.1.173` **PEELED** — object `42abbacf` -> commit `fc3a4421` == PROD head.
- ⭐ **BUNDLE / DE~Z's P1: `index-BamLAu6Q.js` -> `index-D9vMtGZu.js`**, negative control 0.
  **Scored FIRST, deliberately** — P1 is the gate on their other eight rows: had the chunk not
  moved, every prediction below would have been UNINTERPRETABLE rather than false.
  ⚠ CSS unchanged (`WQYUWqLe`) — expected for a JS-side change; banked in advance as
  corroborating-if-it-moves, never a required arm.
- Step 7: `worktree remove` rc=255 "Filename too long" (documented, acceptable); `prune` rc=0; only
  the main tree remains, **on DEV — it never left**.
- PUSH 2/2 by `0.0.0_AB_MSTR~Z`: `origin/SITEZ -> 739b6bbf34`. Verified two ways — `ls-remote` for
  the ref AND the pointer **VALUE** at origin (`160000 commit 0e1c232d…`).

## THE VERIFIER TANGLE COST NOTHING, AND THE REASON IS ACT ORDERING
Two seats claimed the verify within 90 seconds. **Nothing was staged until one had confirmed** (four
read-only commands), then the merge was built — **local and reversible** — and the coordination
traffic was read **before** the irreversible push was handed off.
`2.0.0_SA_COO~Z` @16363 settled it: **author writes the prediction, an INDEPENDENT seat scores it.**
`3.0.0_SA_CVO~Z` @16366: *"FIRE. Do not wait for this to be resolved."* **A promote was not held on a
coordination question that both parties said did not gate it.**

## WHY THIS PROMOTE WAS CHASED RATHER THAN LEFT
Edit (a) retires a suppression **promote #2 shipped four hours earlier**, so PROD had been rendering
a state Andrew personally and explicitly corrected, on the surface he is most likely to open next.
**Holding was not the neutral option.** It had sat ~90 minutes with nobody saying either way, and a
ruling that the edit *"does not hold the promote"* settled that it was not a GATE while saying
nothing about whether it should SHIP.

## THIRD BASELINE OF THE NIGHT
`Ce258d2k` -> `BMmU0cpj` -> `BamLAu6Q`, each dead the moment its own promote fired.
**A one-way marker is consumed by the event it detects; a content-hash renews its own baseline
because it is DERIVED from the bytes rather than hand-maintained.**

## WHAT THIS DEPLOY DID NOT ESTABLISH
- **The rendered page.** `3.0.0_SA_CVO~Z` scores it against `0.4.0_DE_ClientPlatform~Z`'s nine
  predictions, filed BEFORE the fire so they cannot be fitted afterwards.
- **The scheduled pipeline** — untouched by any promote.
- ⚠ Edit (a) makes the Global Client card show **267,632,047.22, 100%-supervised, 49financial-scoped**
  — **correct-as-built under basis B and the open I2 sovereign fork, NOT a pixel-rung defect.**
