# ETFS Positioning Summary-vs-Holdings tie -- PROD promote v2.1.167 + smoke/validate (site Z)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Agent:** 0.2.0_DT_PortfolioAnalytics~Z
**Window:** 2026-08-25T15:55Z -> 16:40Z
**Authority:** ANDREW-DIRECT 2026-08-25 at the CTO~Z terminal, naming this seat, relayed as a GO by
1.0.0_SA_CTO~Z (Msg-ID 9041): "have 0.2.0_DT_PortfolioAnalytics~Z to come in and run the /prod-deploy
then smoke and validate those numbers."

## Summary

Promoted portal DEV->PROD as v2.1.167, removing the HoldingsTab `proportionalRound` plug that forced
Holdings Breakdown to foot to 100.00% by rewriting client-facing security weights. Deploy landed
green and content-identity verified. Validation came back MIXED and was reported that way rather than
as a pass: 6 of 8 asset-class cells tie exactly, and the 2 that do not are explained by a PRE-EXISTING
defect this promote made visible. MSTR~Z ruled the promote STANDS; rollback declined as strictly worse.

## Deployment Sequence

| step | act | result |
|---|---|---|
| 0 | DT-lane gate, inbox pull, freeze declared to COO~Z + MSTR~Z | MSTR~Z froze origin/DEV at a00e67cc (only seat that can push it) |
| 1 | main tree state | DEV, clean, == origin/DEV a00e67cc. No Step-1a push needed |
| 2 | `bun run typecheck` (DEV tree) | rc=0 |
| 3 | `git update-ref refs/heads/PROD refs/remotes/origin/PROD` | local PROD -> a7a7ff16 == origin/PROD |
| 4 | ephemeral worktree `.runtmp/portal-promote-20260825T160020Z` @ PROD; `bun install` FOREGROUND | rc=0, 420 packages, 46.83s |
| 4 | `git -c user.* merge --no-ff origin/DEV -F <msgfile>` | merge 0b37cc6e, parents a7a7ff16 + a00e67cc (exactly two) |
| 4 | PARITY GATE + positive control | `diff origin/DEV HEAD` = 0 bytes; control `diff a7a7ff16 HEAD` = 2 files/+33-42 NON-empty |
| 4 | compensating control on MERGED tree | typecheck rc=0; `NODE_ENV=production bun run build` rc=0, 7.99s |
| 4 | `git push origin PROD` | **DENIED by GATE 5 (LD-0367 r2 / LD-0368)** as pre-flighted. No override used. |
| 4 | push escalated to 0.0.0_AB_MSTR~Z, ONE command | MSTR ran it verbatim; origin/PROD a7a7ff16 -> 0b37cc6e |
| 5 | CI + tag verification | run 32869902917 success, 3/3 jobs; tag portal-v2.1.167 peel-verified |
| 6 | workspace SITEZ pointer bump | commit a981415660, gitlink -> a00e67cc (ls-tree content-verified) |
| 7 | teardown | worktree deregistered + pruned; main tree DEV; cwd at workspace root |
| 8 | freeze released, ledger closed 7/7, ledgers committed | commit 1370968204 |

## Verification (actual output)

```
origin/PROD (ls-remote, my seat)  0b37cc6ed2c5bd4caf9446f2dd786b3c13496798
  negative control                a7a7ff16 no longer at refs/heads/PROD

CI, enumerated BY headSha with denominator (30 runs listed, 1 at this sha):
  32869902917 | Deploy to Production | completed / success
  instrument A (gh run view --json jobs): 3 jobs, all success
  instrument B (check-runs API):          total_count=3, all success

TAG: object 882607c2 -> PEELED 0b37cc6e == PROD head
  control 1: peeled != raw object (annotated, real peel)
  control 2: portal-v2.1.166 peels to a7a7ff16 (discriminates between releases)

SERVED BUNDLE (content identity, not a timestamp):
  served index.html names assets/index-B1LXE5_-.js == the entry chunk MY pre-push build produced
  Content-Length 317691 (matches build 317.69 kB); Last-Modified 16:07:47Z
  negative control: prior chunk index-BwhUGwOQ.js now HTTP 403

BEARER (both-directions control BEFORE trusting any render):
  /api/general/etfs/positioning_data.json  no token -> 401 | with bearer -> 200, 126,788 B
  index.html -> 200 (reachability control)
  served artifact generated_at 2026-08-25T13:01:21Z, data_as_of 2026-08-24
```

## The tie-out (live PROD, authenticated render)

| book | Summary FI | Holdings FI | Summary EQ | Holdings EQ |
|---|---|---|---|---|
| DIVZ | 0.58 | 0.58 TIE | 99.22 | 99.22 TIE |
| IDVZ | 0.89 | 0.89 TIE | 98.62 | 98.62 TIE |
| PFDE | 0.36 | 0.33 **differs** | 99.65 | 99.65 TIE |
| PFOE | 2.32 | 2.34 **differs** | 97.67 | 97.67 TIE |

CTO~Z sharpest single tell PASSES: IDVZ Fixed Income reads 0.89 in BOTH panels (was 0.90 at the
bottom). SALXX on IDVZ shows 0.89, name "State Street U.S. Government MMKT". Equity ties on all four.

MODELS regression: UST 100.00 | ST 82.63+17.37 | INT 32.82+67.18 | LT 12.74+87.26 | ULT 8.14+91.86,
every book footing to exactly 100.00, 0 page errors. QUALIFIER: this is not a before/after DELTA (the
prior bundle 403s, so old PROD is unrenderable) -- what ran is the FALSIFIER for the DELTA=0 claim,
and it did not fire.

ADVI/PERFRP: /advisor-intelligence mounts clean (AUM chart, leaderboard, 10 rows, no error boundary,
0 page errors). The criterion as worded could not be discharged: NOTHING IMPORTS PerfrpTable.tsx (the
other "PerfrpTable" hits are `PerfrpTableRow`, a different symbol), so there is no PerfrpTable route.

## Findings issued

1. **SCOPE (to CTO~Z, ratified).** The brief said "one file changed"; the promote DELTA is 3 commits /
   2 files. True of a00e67cc alone, not of origin/PROD..origin/DEV. CTO~Z took the correction and
   ratified carrying the passenger (78d77c03, a type-only unused-import removal that unblocked DEV CI
   -- excluding it ships a red tree, which is the LESS conservative option).
2. **CASH BUCKETING DEFECT (new, pre-existing, filed by CTO~Z).** Summary FI = `fixed_income + cash`
   (its legend reads "Bonds & Cash"); HoldingsTab renders classes ["Fixed Income","Equity"] ONLY, no
   Cash group, and DROPS the `CASH&OTHER` row from display -- rendered-row denominators vs served
   data: DIVZ 29->29, IDVZ 44->44, PFDE 90->89, PFOE 24->23. The two short books are exactly the two
   carrying a cash row. The bottom panel therefore disagrees with ITSELF: PFDE 0.33+99.65=99.98 vs its
   own GRAND TOTAL 100.01; PFOE 2.34+97.67=100.01 vs GRAND TOTAL 99.99. MSTR~Z re-derived the
   mechanism independently on the served artifact and rated the dropped row the worse half (a tie
   failure is visible; an omitted position is not).
3. **STALE LEDGER, other fabric (to MSTR/CTO/COO, no action taken).** `20260824T1241Z ... v2-1-165`
   is OPEN at 22.2h, authored `0.4.0_DT_ClientPlatform`, CLOUD-fabric. NOT a strand -- it is a
   COO-adjudicated sovereign hold the tool cannot express. But its PREMISE is overtaken: its staged
   merge a239e4a9 is still on ZERO remote branches while portal-v2.1.165 shipped as d9a98bcc. It
   guards an abandoned artifact. Its LOCAL-STATE CAUTION (laptop `refs/heads/PROD` left at a239e4a9)
   may still be live there; unverifiable from site Z and reported as such.
4. **v2.1.166 ledger was closed but never committed** (this seat own 08:27Z session). Committed now.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| deploy_ledger.py | open / close-leg x7 / close / check | PASS | 7 legs opened at deploy-START, all closed with proof; `check` then surfaced finding 3 |
| safe-commit.sh | -F, pathspec-scoped, x2 | PASS | msg-verify MATCH both times; risk-reflex [HOLD] on portal node read and not applicable |
| comp-which | A.3 startup exercise | PASS | forwarder RAN (banner produced), 98 of 102 comp-tools resolve bare |
| to-check.py | --all --assignee | PASS | 6 ACTIVE TOs held, all OPAL_TAXSMA (39d, staged) -- none touched, Andrew-direct took precedence |

**What worked:** the ledger contract carried this promote end to end -- opening it at deploy-START
with a stated manifest is what made the GATE-5 denial a routine escalation instead of an incident,
because L2 was already named as its own leg with its own proof requirement.
**What failed:** nothing at tool level.
**Gap found:** `deploy_ledger.py check` reports `stranded=[...]` for legs that were NEVER ATTEMPTED
(finding 3 entry). NOT-YET-STARTED and PARTIALLY-DONE are opposite states with opposite remedies.
Already a filed Rule-24 finding routed to CTO; re-observed here, not re-opened.

## Instrument discipline (recorded, not omitted)

- Attempted to prove PerfrpTable.tsx is tree-shaken out of the bundle. **NOT REPORTED as a result:**
  the bundle is minified, my pattern returned zero AND SO DID MY POSITIVE CONTROL, so the instrument
  was broken and could support neither verdict.
- First row-count filter excluded any row containing "TOTAL" and silently ate IDVZ `TotalEnergies
  SE`, manufacturing a phantom 43-of-44 second dropped row. Caught by re-anchoring to the asset-class
  column; then CHECKED (not assumed) that PFDE/PFOE hold no similarly-named security. That check is
  what makes their 89/23 counts trustworthy.
- Corrected my own escalation to MSTR mid-flight: I had said "two push forms"; reading deploy.yml
  showed CI mints the tag itself, so a `--follow-tags` from the integrator seat would have published
  unrelated local tags during a live promote. Cut to ONE command before it reached their hands.

## Blockers

None open at this seat.

## Current State

ETF Positioning on production carries the plug removal. `origin/PROD` = `0b37cc6e`, tag
`portal-v2.1.167`, served bundle `assets/index-B1LXE5_-.js` (Last-Modified 16:07:47Z). Positioning
Summary and Holdings Breakdown now agree exactly on DIVZ and IDVZ (both rows) and on Equity for all
four books; PFDE/PFOE Fixed Income differs by exactly each book cash weight, which is the separate
cash-bucketing defect filed by 1.0.0_SA_CTO~Z under ledger
`20260825T1624Z_etfs-positioning-nav-residual-cash-other`.

Workspace pointer commit `a981415660` and ledger commit `1370968204` are LANDED LOCAL on SITEZ and
RIDE INTEGRATION -- both sit on ZERO remote branches (`branch -r --contains` empty); 0.0.0_AB_MSTR~Z
holds the push under LD-0367 / GATE 5. Portal main tree is on DEV at a00e67cc, worktree pruned; the
physical `.runtmp/portal-promote-20260825T160020Z` persists (Windows long-path, gitignored, inert) --
now the FOURTH such directory, a standing housekeeping item for a human, not chased.

Deploy-completion ledger `20260825T1559Z_etfs-positioning-holdings-tie-prod-promote-sitez` is CLOSED,
7/7 legs proven, sentinel removed. Freeze on portal DEV RELEASED at 16:30Z.

## Next Steps

- [1.0.0_SA_CTO~Z] Ratify (or reject) the re-worded acceptance bar MSTR~Z recommended: "the two panels
  agree wherever they measure the same quantity, and where they do not, the difference is fully
  explained by a named definitional gap." I have NOT treated it as ratified.
- [1.0.0_SA_CTO~Z] The cash-bucketing defect is yours (ledger opened at your seat). The dropped
  `CASH&OTHER` row is the priority half per MSTR~Z ruling -- it is invisible to a user, unlike the
  0.03 tie failure.
- [2.0.0_SA_COO~Z] Disposition of the stale `v2-1-165` ledger (finding 3) -- close as SUPERSEDED or
  re-state against whatever actually carried the ADVI machinery. NOT mine to close; queued to you,
  seat not live at send time.
- [0.0.0_AB_MSTR~Z] Integration push carries a981415660 + 1370968204.
- [any laptop-side seat] Check `git -C portal rev-parse PROD` on the CLOUD fabric -- it may still be
  parked at the abandoned a239e4a9.
- AGG note, logged not chased per MSTR~Z: the brief listed six models books incl. AGG; five tabs
  render (UST/ST/INT/LT/ULT).
