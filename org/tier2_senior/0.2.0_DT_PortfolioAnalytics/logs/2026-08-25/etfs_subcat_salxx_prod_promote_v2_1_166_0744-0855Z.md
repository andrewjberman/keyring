# 0.2.0_DT_PortfolioAnalytics~Z -- ETF Sub-Categories + SALXX PROD promote v2.1.166 (0744-0855Z, site Z)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Outcome:** DELIVERED. `origin/PROD` = `a7a7ff16` (ls-remote at my own seat), tag `portal-v2.1.166`
peel-verified, CI success on all 3 jobs, deploy-completion ledger CLOSED with all 7 legs proven.
**RUNG 3 discharged on live production: BOTH defects verified on a render.**

## What was asked

ANDREW-DIRECT 2026-08-25 ~07:3xZ, verbatim: *"i need all of that fixed... they are to fix this and
only this, verify visually that it is fixed (and confirm pipelines are scheduled/robust), commit,
push / prod-deploy, and do all necessary logging."* My lane: the portal DEV->PROD promote, AFTER
DE~Z + DS~Z land and MSTR~Z pushes. Scope fence: two defects, not a third.

## Deployment Sequence

| step | act | result |
|---|---|---|
| pre-flight | manifest re-derived AT the cut ref, not from my 07:5xZ pre-read | 5 commits / 5 files, no dep or lockfile change |
| S1 | portal tree clean, on DEV, local == origin/DEV | 0 dirty, 0/0 |
| S3 | `update-ref refs/heads/PROD refs/remotes/origin/PROD` (dry-run-pollution class) | local PROD == origin/PROD d9a98bcc |
| S4 | ephemeral worktree `.runtmp/portal-promote-20260825T082800Z` on PROD | main tree never left DEV |
| S4 | `bun install` FOREGROUND | rc=0, 420 packages, 42.65s |
| S4 | `merge --no-ff origin/DEV -F <msgfile>` | a7a7ff16, parents d9a98bcc + f67b3a48 |
| S4 | PARITY GATE | `git diff origin/DEV HEAD` = **0 bytes** |
| S4 | compensating control (Step 2 unavailable) | `typecheck` rc=0; `build` rc=0, 51 assets |
| S4 | `git push origin PROD` | **BLOCKED by GATE 5** -- escalated, MSTR~Z took the push |
| S5 | CI | run 32827830122 success, 3/3 jobs |
| S6 | workspace pointer | cac2003625, landed LOCAL, rides integration |
| S7 | teardown | worktree pruned, main tree on DEV, cwd = workspace root |

## Verification (actual output)

```
git ls-remote origin refs/heads/PROD
  a7a7ff165078c99562700ecd3eef6e9a7c91f1d9   refs/heads/PROD

PARITY   git diff origin/DEV HEAD -> 0 bytes / 0 lines   EMPTY
         POSITIVE CONTROL git diff d9a98bcc HEAD -> 5 files / 157 insertions, NON-empty

TAG      refs/tags/portal-v2.1.166      fe0fccfb512c1c4034ffb0c2fca5b15c07e205f6  (tag object)
         refs/tags/portal-v2.1.166^{}   a7a7ff165078c99562700ecd3eef6e9a7c91f1d9  (PEELED == PROD)
         NEGATIVE CONTROL: object sha != peeled commit -> annotated, so the peel was real

CI       Build Production Assets => success
         Deploy to S3 + CloudFront => success
         Tag Deployment => success
         (confirmed twice: gh run view --json jobs AND the check-runs API at the merge sha)

BUNDLE   served index.html Last-Modified 08:42:19Z -> names assets/index-BwhUGwOQ.js
         my own pre-push build dist/index.html    -> names assets/index-BwhUGwOQ.js   IDENTICAL

GITLINK  git ls-tree cac2003625 portal -> 160000 commit f67b3a480fd9e33bf1716966b8cd48a232b9e07a
         git show --stat cac2003625    -> exactly 1 file changed (nothing swept in)
         git branch -r --contains cac2003625 -> EMPTY (landed LOCAL, rides integration)
```

## RUNG 3 -- live production render, both defects

Authenticated render of `https://opalinvest.dev/positioning` (ETFs mode, details expanded) using a
minted RS256 bearer so the edge auth-validator serves real data. PNG READ, and the DOM extracted so
the picture has an exact numeric companion.

```
                          DIVZ     IDVZ     PFDE     PFOE
Ultra Short Duration      0.58     0.89     0.33     2.34
Information Technology    6.84     6.54    39.05    21.26      <- PERCENT scale, not 0.39
Financials                9.40    20.52    13.62    14.78
COLUMN SUM               99.80    96.82   100.01    99.99
asset-class bars         99.80    99.51   100.01    99.99
DELTA                    -0.00     2.69     0.00     0.00

SALXX row: "State Street U.S. Government MMKT"   (BEFORE: "STATE STREET INST U.S. GOVERNMENT M...")
```

Three of four books reconcile to the hundredth against a panel computed by a different code path.
IDVZ is short by exactly 2.69 = ICT 1.66 + MER 1.03 -- the KNOWN null-`sub_asset_class` drop (filed
05:13Z, re-measured by CTO~Z, ruled known by MSTR~Z). Not a new defect; not re-filed by me.

**The three-capture sequence is itself the control:** BEFORE (old code + old data) panel absent /
SALXX raw; MID at 08:35Z pre-push (old code + NEW data) panel absent / SALXX fixed; AFTER (new code +
new data) panel present / SALXX fixed. The MID capture is what proves the instrument reads live
production rather than my worktree -- a worktree render would have shown the panel POPULATED.

## Findings raised

1. **DEV CI has not type-checked, built, or run the provenance guard since 2026-08-25T02:08:25Z** --
   8 consecutive red runs. ESLint fails at step 7, so steps 8/9/10/11 are SKIPPED, not failed. **The
   build did not fail; the build never ran.** Cause: ONE deletable line, `PerfrpTable.tsx:29`, an
   unused type import. Word-anchored grep = 1 (the import itself); a bare grep returns 5, all four
   being substring matches on `isPerfrpFigure`/`PerfrpFigureCell`; positive control `PerfrpColumn` =
   3. This CLOSED my own prior log's open item, which said "duration UNMEASURED and not guessed."
   **FILED, NOT FIXED** -- a PERFRP file, reserved at Andrew. Three seats converged on deleting it;
   CTO~Z ruled (a) then reversed to (b) within 12 minutes on COO~Z's entanglement argument.
2. **`deploy.yml` runs typecheck + build but NOT eslint** (controlled absence: the grep pattern would
   have matched any lint step). That is why a red-DEV window still ships correct bytes, and why my
   promote was never blocked by finding 1.
3. **The null-`sub_asset_class` drop, re-derived independently** and confirmed on the rendered page.
   I initially reported the gap as 3.18 and CTO~Z corrected it to **2.69** -- the other 0.49 is the
   issuer's own book not totalling 100 and is not ours. Correction taken whole; the over-statement
   would have invited "force the book to 100", i.e. manufacturing a number on a client-facing page.
4. **`comp-estate`-class instrument anomaly:** one `gh run list | filter headSha` returned 0 hits
   when the truth was 1. NOT reproducible (3/3 re-runs = 1). L3 grounded instead on the run-id and
   check-runs reads, which do not use that filter.
5. **Page renders `prior_date` as its as-of label:** footer reads "August 21st, 2026" while the
   artifact carries `data_as_of` = `data_date` = 2026-08-24 and a per-book `prior_date` = 2026-08-21.
   FILED to the CVO surprise channel as an OBSERVATION, not chased.
6. **NON-FINDING pre-empted:** "August 21st" is NOT a staleness defect. Trading calendar resolved
   before forming a view -- 08-21 Fri, 08-24 Mon, 08-25 Tue; Monday's 13:00Z run correctly produced
   T-1 = Friday, and today's run had not yet fired at 08:2xZ.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | PASS | forwarder RAN (produced its own banner), not merely resolved |
| `comp-find` | `--name '*PERFRP_ON_PROD*'`, `--name '*OPEN_CALL*'`, `-i 'portal-test-login'` | PASS | denominators printed; the `portal-test-login` sweep returned DOC-only hits, which is what established that no code consumes the sanctioned creds |
| `comp-routes behaviors` | serving/CloudFront path | PARTIAL | its own header discloses DESIRED-plane only; used to locate the distribution, then grounded on the live served bytes per Rule 22a |
| `.tools/deploy_ledger.py` | open / close-leg x7 / close / check | PASS | 7 legs, all proven; `check` surfaced two other entries, neither mine |

**What worked:** `comp-find`'s denominator + BAND lines made the PERFRP census self-framing.
**What failed:** a raw `grep` of `infra/aws/.../jwt.ts` was correctly GATED by the comp-rail; no
comp-tool answers "what claim fields does this TS signer emit", so I used native `Read` (rail-free)
rather than burning an override marker.
**Gap found:** none new. `comp-routes` DESIRED-plane-only is already disclosed in its own header.

## Blockers

None open at this seat.

## Current State

ETF Positioning on production carries both fixes. `origin/PROD` = `a7a7ff16`, tag `portal-v2.1.166`,
served bundle `assets/index-BwhUGwOQ.js` (Last-Modified 08:42:19Z). The Positioning page in ETFs mode
renders `ASSET SUB-CATEGORIES (12)` populated across DIVZ/IDVZ/PFDE/PFOE on the percent scale, and
the SALXX row reads `State Street U.S. Government MMKT`. Defect B needed no deploy at all -- it is a
published-artifact fix (`s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`, 126,809 B
@08:31:06Z, sha256 98650407cd82922536cabbdb, verified at my own seat).

Workspace pointer commit `cac2003625` (gitlink -> `f67b3a48`) is LOCAL and needs the integrator's
push. Deploy ledger
`org/critical_paths/change_management/20260825T0827Z_etfs-subcat-salxx-prod-promote-v2-1-166-sitez_deploy_completion.md`
is CLOSED. Portal main tree is on DEV; worktree deregistered and pruned; the physical
`.runtmp/portal-promote-20260825T082800Z` directory persists (Windows long-path, gitignored, inert).

## Not done, deliberately

- **`PerfrpTable.tsx:29`** -- reserved at Andrew via MSTR~Z. Untouched by anyone.
- **The IDVZ null-drop** -- already filed twice; MSTR~Z ruled that re-derivations must not be written
  up as new defects. Not re-filed.
- **Recursive deletion of the three `.runtmp/portal-promote-*` directories** -- needs a human.
- **The laptop fabric's ledger** `20260824T1241Z_etfs-positioning-prod-promote-v2-1-165`, author
  `0.4.0_DT_ClientPlatform`, still OPEN at 14.7h. Another device's record under Rule 26; flagged, not
  touched. It will keep tripping `deploy_ledger check` until that fabric closes it.

## Next steps

1. [0.0.0_AB_MSTR~Z] Push `cac2003625` (workspace pointer) on the next integration window.
2. [Andrew] Visual smoke at his discretion. `comp-closure` does NOT go on the D4 item until he
   smokes it himself.
3. [2.0.0_SA_COO~Z] Carry finding 1 (DEV CI compile gate disabled) forward as an owned item after
   the promote -- CTO~Z asked that it not die with this session's scope.
4. [3.0.0_SA_CVO~Z] Surprise-channel items filed: the null-drop (OBSERVATION, already known) and the
   `prior_date`-as-as-of render (OBSERVATION).
