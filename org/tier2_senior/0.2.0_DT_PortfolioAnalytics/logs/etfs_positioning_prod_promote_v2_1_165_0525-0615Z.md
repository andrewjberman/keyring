# 0.2.0_DT_PortfolioAnalytics~Z -- ETFS_POSITIONING PROD promote v2.1.165 (0525-0615Z, site Z)

**Archetype:** deploy-execution (single-task seat, spawned on Andrew-direct, task complete)
**Outcome:** DELIVERED. `origin/PROD` = `d9a98bcc` (ls-remote), tag `portal-v2.1.165` peel-verified,
ledger CLOSED with all 6 legs proven. ETFS_POSITIONING is live in production for the first time.

## What was asked

Andrew, at the MSTR terminal ~05:23Z, verbatim: *"Yeah we need an 0.2.0_DT_PortfolioAnalytics~Z
agent spawned to run the /prod-deploy"*. That sentence is the authorization and it was spent at
spawn. Spawn brief added: read the inbox first, MSTR~Z has a blocking sequencing fact.

## The sequencing fact, and why the inbox-first instruction was load-bearing

`/prod-deploy` cuts from `origin/DEV`, not the working tree. At spawn, `origin/DEV` still carried
the THREE-KEY etfAdapter allowlist -- the defect Andrew had watched get fixed at a local render at
05:06Z. All 7 of the night's portal commits were local-only. **A promote at 05:25Z would have
shipped to production the defect he had confirmed fixed twenty minutes earlier, and it would have
passed every one of the six ledger legs while doing it**, because the promote machinery cannot see
a commit that is not on the branch it cuts from.

Three seats (MSTR~Z, COO~Z, CVO~Z) sent the same measurement. I re-derived it rather than acting on
three reports: 7 of 7 commits `<NONE>` on `branch -r --contains`, positive control `8ecb6b68` ->
origin/DEV, negative control `8a96c916` -> origin/PROD, and origin/DEV's adapter printing exactly
QTD/YTD/'1Y' at :92-94 over a 155-line retrieval whose header I checked so the three-key read was a
measurement and not a broken pipe.

Order executed: DE~Z merged -> MSTR~Z pushed -> I re-ran the gate myself at 05:38:06Z (HIT) -> cut.

## Legs

| leg | proof |
|---|---|
| L1 merge | `d9a98bcc` --no-ff; parity `git diff origin/DEV HEAD` = **0 bytes**; spread at :97 present on the merged tree, three-key allowlist absent (negative control); `tsc -b --noEmit` rc=0 |
| L2 prod-push | `origin/PROD` 8a96c916 -> d9a98bcc, **ls-remote read at my own seat**. Pushed by the integrator (see below) |
| L3 ci | 3/3 check-runs success at the merge sha. **Amended, not closed green** -- see the caveat |
| L4 tag | `portal-v2.1.165^{commit}` PEELED == PROD head; raw tag object `8fd31fbb` differs, confirming annotated |
| L5 pointer | `40b1f3c147` on origin/SITEZ; **gitlink CONTENT-verified** `ls-tree origin/SITEZ portal` -> 063ff4d7 |
| L6 teardown | worktree pruned, portal main tree never left DEV |

## The block, and the fork I did not resolve myself

`git push origin PROD` was DENIED by GATE 5 (LD-0367 rule 2 / LD-0368, integrator-only). The
`/prod-deploy` skill still instructs that bare push and has never been updated for the gate.

I measured the gate's own stated hazard and it was absent here -- `rev-list origin/PROD..PROD --not
origin/DEV` = **1 commit** (mine), positive control without the filter = 42, so the filter
discriminates. **I reported that as evidence for the integrator's decision and explicitly not as a
self-authorization**, and escalated the same turn naming both acceptable forms: MSTR pushes, or
MSTR grants explicit no-objection for an audited override. MSTR took the push and recorded why --
*"an audited override would have produced the same ref with a weaker record."*

Banked: the override precedent's own record shows its first attempt failed because the marker was
**pipe-detached**. Mine had been too (piped through `tail`), which is why the first denial fired
the way it did.

## The rung beyond DEPLOYED

CI green proves the deploy job ran; a local render proves the code. Neither proves what CloudFront
hands users. I fetched the served bundle: `Last-Modified 05:55:06Z` (post-deploy), and served chunk
`assets/index-CJlD8UOW.js` contains verbatim `?.returns||{}` and
`["1D","WTD","MTD","1M","QTD","1Q","YTD","1Y"]` -- **all eight windows in the production artifact**.
Marker `Opal ETFs` (introduced tonight by 3134ccda) present = PROD carries tonight's commits.

**My first probe of this was broken and only the control caught it.** I searched double-quoted
`"QTD"` against a minified bundle, got 0 -- and the positive control returned 0 too. A zero whose
control also reads zero is a broken instrument, not a finding. `returns.QTD` = 0 carries weight only
because `QTD` appears 34 times elsewhere.

**NOT verified: the visual render.** Served CODE and rendered PAGE are different rungs and I did not
collapse them.

## Findings raised

1. **L3's domain is narrower than its question** (MSTR~Z found it, I re-derived from workflow
   source). `ci.yml` fires on `branches:[DEV]` only, `deploy.yml` on `[PROD]` only -- so a
   headSha-scoped CI check on a PROD merge **structurally cannot see the workflow that validates the
   code**. Amended L3 rather than closing it green.
2. **Correction routed upward to MSTR~Z:** their note said "type-check and build both passed." That
   run's steps 8-11 were **SKIPPED** -- ESLint failed at step 7. CI is not evidence they passed; it
   is evidence they never ran. They are evidenced elsewhere (my `tsc` rc=0 on the merged tree; Build
   Production Assets success on the shipping sha). Disposition unchanged and correct.
3. **Correction received from CVO~Z and recorded as a ledger addendum:** my "inherited, not
   introduced" is right about authorship and incomplete about PROD -- the file did not exist on old
   PROD (positive control: package.json did), so this promote introduced it. Another fabric's ADVI
   work rode as a passenger of the 5-day backlog.
4. **Open item, routed not fixed:** `origin/DEV` has been shipping a red Build & Validate for at
   least one cycle. **Duration UNMEASURED and not guessed.** Carded to COO for daylight, ADVI owner.
   Not fixed inside a promote -- an `--fix` on an untouched subtree at 06:00Z is scope creep.
5. **ADVI re-derived at my cut ref** as instructed: 15 rows, held 14 / structural 1, **FLIP 0**,
   lands DORMANT. The 17h-old census reproduced. **My first count said FLIP 1 and was wrong** -- it
   matched the TYPE DECLARATION `state: 'flip' | 'held' | 'structural'`, not a registry row. A token
   census counted a type as a value; scoping to the `ADVI_REPOINT` object fixed it. That file's own
   header warns about exactly this and names the direction, and I got the "invent a discrepancy"
   half on the first read having just read the warning.

## Compiler Tools

`comp-routes behaviors` (serving/CloudFront path, to locate the PROD serving target -- its own
header disclosed DESIRED-plane-only, which is why I went to the live bundle instead of trusting it).
`comp-find` not needed: the searches were git-object and served-artifact reads, not repo censuses.
The PreToolUse HUD nudged `comp-transform`/`comp-estate` on a portal-component search; I took
`comp-routes` and then grounded on the live served bytes per Rule 22a rather than stopping at the
DESIRED plane.

## Not done, deliberately

- **SALXX display-name handoff** (Andrew routed it to me via DE~Z if they could not complete it).
  Queued behind the promote, not folded into it. COO~Z's 05:51Z warning against the seeder landed
  before I went near it. Five remedies have now been proposed and all five fail differently; act 1
  (add SALXX to `ETF_NAME_OVERRIDES` with Andrew's verbatim string) is the live one and DS~Z has
  measured act 3's coverage at zero.
- **`rm -rf` of the `.runtmp` worktree dir.** `worktree remove` hit the known Windows long-path
  error; deregistered and pruned, gitignored, inert. Recursive deletion needs a human.
- **The laptop fabric's 11.8h OPEN ledger** for this same promote (`20260824T1241Z_...v2-1-165`,
  authored by `0.4.0_DT_ClientPlatform`, no `~Z`). Rule 26 -- another device's record. Flagged to
  COO~Z for cross-fabric routing; not reused, not closed, not touched.

## Blockers

None open at this seat.

## Next steps

1. [Andrew / 0.4.0_DE_ClientPlatform~Z] Visual render of the Positioning page against PROD -- the
   fifth rung, the one nobody has run. CVO~Z's acceptance test: the page matches the artifact at the
   moment of the check and all eight columns render.
2. [1.0.0_SA_CTO~Z] The ESLint break on origin/DEV, and the scope question CVO~Z/COO~Z raised: there
   is no display-name authority at all for non-ETF holdings inside an ETF.
3. [me] SALXX act 1 on request; otherwise event-driven.
4. [0.0.0_AB_MSTR~Z] `cf14116501` + this log ride the next integration window.
