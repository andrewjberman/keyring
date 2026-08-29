# DEPLOY LEDGER — D1_CATVIEWS portal DEV -> PROD promote (chain step 4)

**Status:** CLOSED — COMPLETE
**Opened:** 2026-08-28T22:22Z
**Closed:** 2026-08-28T22:42Z — nothing half-landed; both pushes verified on the remote.
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
- 22:23Z worktree · bun install rc=0 (420 pkgs, FOREGROUND) · merge `--no-ff` rc=0, 17 files
  +1839/-108, no conflicts -> `1b91b1972957b1cc011fe366060115f112bc54e1`
- **PARITY GATE PASS: 0 bytes.** Corroborated by a second instrument — merged tree
  `2eff1e2720406644a9bee2e730568a986f185a04` == `origin/DEV` tree, **the value `merge-tree` predicted
  before the merge existed.** Prediction and outcome agree.
- PUSH 1/2 by `0.0.0_AB_MSTR~Z` (GATE 5, no override): `origin/PROD d4a048fd -> 1b91b197`
- CI: `gh -R Opal-Capital/portal`, enumerated BY headSha — **1 run at `1b91b197`, "Deploy to
  Production", conclusion=success, id 33216893773.** Denominator of 1 is consistent with the prior
  promote `d4a048fd` (ci.yml fires on DEV, deploy.yml on PROD), so it is not a missing workflow.
  ⚠ First `gh` attempt returned **rc=1, TLS handshake timeout** — a RETRIEVAL failure that would have
  read as "no runs yet" had rc not been captured. Retried; rc=0.
- TAG: `portal-v2.1.171` **PEELED** — ls-remote object `09bc3763` -> commit `1b91b197` == PROD head.
- **BUNDLE (the scored stop condition): `index-Ce258d2k.js` -> `index-BMmU0cpj.js`** (CSS
  `BrZ63NPq` -> `WQYUWqLe`). `Last-Modified` printed, NOT scored.
- SERVED BYTES: `Fee split unavailable` 1 -> 0 in the ModelPortfolios chunk; positive control
  `Asset Category Views` still 1; negative control 0.
- Step 7: `worktree remove` rc=255 "Filename too long" (documented Windows behaviour, acceptable);
  `worktree prune` rc=0; only the main tree remains, **on DEV — it never left**. `.runtmp/` confirmed
  ignored at `.gitignore:426` and absent from `status` (checked, not assumed).
- PUSH 2/2 by `0.0.0_AB_MSTR~Z`: `origin/SITEZ -> 240a85eec4` (the pointer commit), verified by
  `ls-remote`. ⚠ The branch is **SITEZ**, not the skill's `CLOUD` (a laptop-fabric name), and GATE 5's
  regex does **not** cover SITEZ — routed to the integrator on **LD-0367 (the rule), not because a
  gate refused.** Of the 5 unpushed commits, **2 were peers'** — the precise harm the rule names.

## TWO CORRECTIONS MADE DURING THE ACT, KEPT BECAUSE THE SHAPE IS THE VALUE
1. **A false-PASS marker, caught by another seat.** I first scored the served-bytes leg on a marker
   whose OLD side was read at `origin/DEV`, while PROD served `2858e7f5ff`. The string went
   0 -> 1 -> 0 and **never reached PROD**, so its pass condition was ALREADY MET on the un-promoted
   bundle. Right instrument, wrong REFERENT. Caught by `3.0.0_SA_CVO~Z` @14385; re-scored against the
   served bytes. **The bundle-filename control survived the same audit only because its baseline was
   read from the LIVE SERVED PAGE rather than from a git ref** — anchored to the artifact, not a branch.
2. **An INDETERMINATE correctly not called a PASS.** An earlier read returned discriminator ABSENT
   *and* control ABSENT — which means the wrong chunk, not a landed fix. The component lives in the
   ModelPortfolios route chunk, not the entry chunk. **Checking only the discriminator would have
   scored a false pass.**

## WHAT THIS DEPLOY DID NOT ESTABLISH
- **The visual render.** DATA is verified through the page's own route (`1.0.0_SA_CTO~Z` AC3, 3-arm:
  real bearer 200 / no auth 401 / **BOGUS bearer 401** — the load-bearing arm). The pixel check is a
  separate rung and was UNASSIGNED at close; `0.4.0_DE_ClientPlatform~Z` volunteered for it.
- **The scheduled pipeline.** Tonight's artifact came from an ad-hoc reland stamped
  `_provenance.trigger = "manual"` (measured — NOT the `"adhoc"` two seats predicted). Monday
  2026-08-31's fire settles it, scored **AC1-S structural, never AC1-L** — the literal is
  market-valued and Monday's correct value will differ.
- Edge cache: `1.0.0_SA_CTO~Z` measured the data object **`X-Cache: Miss`, no `Cache-Control`** —
  gap opened at 14222, **closed by measurement**, no invalidation act required.
