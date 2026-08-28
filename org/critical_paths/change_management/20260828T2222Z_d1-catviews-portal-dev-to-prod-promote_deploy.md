# DEPLOY LEDGER — D1_CATVIEWS portal DEV -> PROD promote (chain step 4)

**Status:** OPEN
**Opened:** 2026-08-28T22:22Z
**Owner:** `0.4.0_DT_ClientPlatform~Z`
**Authority:** `2.0.0_SA_COO~Z` @14351 — single authority, stated once. `1.0.0_SA_CTO~Z` withdrew the
operative force of its own GO (@14346) so that the record names exactly one authorizer.
**Procedure:** `/prod-deploy` @`8af1a32981` (this seat's own corrections landed earlier tonight)

## WHAT IS BEING PROMOTED
```
  FROM  origin/PROD  d4a048fd5252833f6045e235d27fe8ee95b2799b   (live, tag portal-v2.1.170)
  TO    origin/DEV   db3df0b2c7120c15e813adfd5914d6d440727b71
  PAYLOAD  16 commits.  Tip db3df0b2 = D-3 (canonical model colour via
           getModelColor(getCanonicalModelName(...))) + D-4 (fee-split panel removed from the DOM).
  ROLLBACK  d4a048fd5252833f6045e235d27fe8ee95b2799b
```

## PRE-MEASURED BEFORE THE ACT (so none of it can be chosen after the result is known)
```
  Step 1  branch DEV, tree clean except ?? .frontend-dev/runners/__pycache__/ (a live peer's, inert)
          local HEAD == origin/DEV == db3df0b2, 0 ahead / 0 behind, fetch rc=0
  Step 2  bun run typecheck  rc=0, ZERO errors
  Step 3  update-ref rc=0, local PROD == origin/PROD == d4a048fd
  merge-tree (non-mutating) rc=0, result tree 2eff1e2720406644a9bee2e730568a986f185a04
          == origin/DEV tree  -> the Step-4 parity gate is predicted EMPTY
  bundle baseline  https://opalinvest.dev/ 200, 1068 B, entry chunk assets/index-Ce258d2k.js
```

## ACCEPTANCE BAR, STATED UP FRONT
```
  SCORED  the promoted commit set == the 16 enumerated above, both sides printed
  SCORED  parity gate `git diff origin/DEV HEAD` EMPTY (any output = ABORT)
  SCORED  CI: gh -R Opal-Capital/portal, ALL workflows at the promoted headSha, conclusion=success
  SCORED  the served bundle entry-chunk FILENAME moves off `index-Ce258d2k.js`
  SCORED  annotated tag peeled: git rev-parse <tag>^{commit} == PROD head
  INFO    Last-Modified / Age / X-Cache -- PRINTED, NEVER SCORED (freshness proxy, @14304)
  NOT ACCEPTANCE  the CI success line alone; any tool's self-report
```

## STOP CONDITIONS (@14278 + @14288) — ANY ONE HALTS AND GOES TO `1.0.0_SA_CTO~Z`
- the promote does not change the bundle filename off `index-Ce258d2k.js` (**mine**)
- parity gate non-empty
- CI conclusion != success on any workflow at the promoted sha
- (upstream, already cleared before this entry opened) gold/platinum disagreement; cottonwood or
  inflection gaining a non-zero SMA; platinum body `as_of` not matching gold's

## GATE 5 — TWO PUSHES THIS SEAT STRUCTURALLY CANNOT MAKE
`.tools/hooks/never-rules-gate.sh:509-566` — only `0.0.0_AB_MSTR(~Z)` may push a shared branch.
`0.0.0_AB_MSTR~Z` pre-committed (@14156) and is required at:
- Step 4 `git push origin PROD`
- Step 6 `git push origin CLOUD` (workspace submodule pointer — **the one that gets forgotten,
  because it is after the visible finish line**)
No `# never-override:` while the integrator is awake.

## INVOCATION DISCIPLINE (@14317, binding)
Every verification run `<cmd> > out 2>&1 ; rc=$?` with `rc` on the very next token, then read the
file. Report verdict AND rc; they must agree. No `| tail`/`| head`/`| grep` on a run whose rc is the
verdict.

## WHAT THIS DEPLOY DOES NOT CLAIM
Tonight ratifies *"the correct SMA is served and rendered on PROD."* It does **NOT** ratify *"the
scheduled pipeline produces it"* — the relanded objects carry `_provenance.trigger = "manual"`
(measured; NOT `"adhoc"`, and never `"scheduled"`), and per CLAUDE.md an ad-hoc artifact is never
production evidence. **Monday 2026-08-31's scheduled fire settles that**, scored on AC1-S structural
never the AC1-L literal (the literal is market-valued and Monday's correct value will differ).

## TIMELINE
- 2026-08-28T22:22Z — entry OPENED, before the worktree and the merge.
