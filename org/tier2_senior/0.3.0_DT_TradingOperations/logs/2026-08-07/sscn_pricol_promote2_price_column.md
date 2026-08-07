# SSCN_PRICOL promote #2 -- Security Scanner Price column (portal-v2.1.160)

**archetype:** DEPLOY

Window 2026-08-07 ~2215Z-2236Z. Continues
`sscn_pricol_portal_promote_and_price_lambda.md` (same session). **SSCN_PRICOL is now COMPLETE
end to end** -- producer, data, and both display surfaces.

---

## Current State

| Field | Value |
|---|---|
| PROD commit | `dd2907ebf75eacb8b074c04bd54814a9e612e1a8` |
| Tag | `portal-v2.1.160` -- object `325980b2`, PEELED `^{commit}` = `dd2907eb` = origin/PROD (MATCH) |
| CI | run `31223900728` "Deploy to Production" conclusion=**success**; enumerated by headSha -> exactly 1 workflow, all success |
| Parity gate | `git diff origin/DEV HEAD` = **0 lines** |
| Typecheck | rc=0 post-merge, against a PROD-base baseline that was rc=0 FIRST |
| Pointer | CLOUD `52ecaddc01` |
| Main tree | DEV at `9bd2365b` throughout; cwd returned to workspace root |
| Ledger | `sscn-pricol-pricecol` **CLOSED**, 5/5 legs proven |
| Rollback | single step -> `a211e09f` (v2.1.159) |

Promote set: exactly 1 commit, 3 files, +62/-0, ALL SecurityScanner, **no passengers**.
`9bd2365b` (0.3.0_DE): `types.ts` (`price: number | null` on both row interfaces),
`tabs/UniverseDataTab.tsx`, `tabs/UniverseScannerTab.tsx`.

Column sits immediately before market cap on both universe tabs -- Andrew's specified placement
(2026-08-07 19:07Z: *"I can just add price to column before market cap"*).

### The full job, one line per leg

```
c76aaef814   producer emits `price`         Terraform safe-apply, 0-diff, DEPLOYED BYTES read
re-trigger   all 6 universes regenerated    served write times moved off 19:00:33Z
a211e09f     v2.1.159 DataRefresh half      upload page advertises the types it already accepted
dd2907eb     v2.1.160 Price column          renders the key the producer now emits
```

Andrew's motivating case renders on screen: **AU $87.59 against mktVal 44,233.6** -- the exact
plausibility check he was doing by hand when he found the number looked stale.

---

## The check I added that nobody asked for

DE render-verified 3 universes. I verified **all six** before promoting, because the column renders
on whichever universe the user selects, and **a universe missing the key renders BLANK under a
perfectly green deploy** -- it would have surfaced as a Yang complaint, not a build failure.

```
sp500   rows=502   key=502   non-null=501     r1000   rows=1022  key=1022  non-null=1020
r1000v  rows=869   key=869   non-null=867     acwx    rows=1830  key=1830  non-null=1828
eafe    rows=660   key=660   non-null=659     eafev   rows=399   key=399   non-null=398
TOTAL   5,282 rows | price key on 5,282 | non-null on 5,273 | 9 genuine per-name nulls
```

Secondary value: this corroborated the invoke's self-reported `universesProcessed: 6` **from the
served side**, rather than accepting the producer's own word for its own completeness.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `deploy_ledger.py open/close-leg/close` | PASS | opened at deploy-START, 5/5 legs closed with proof, CLOSED |
| `deploy_ledger.py check` | PASS | zero `sscn-pricol*` entries OPEN after close -- verified, not assumed |
| `safe-commit.sh` | PASS | pointer commit `52ecaddc01`; risk-reflex HOLD citation on `portal` read |
| `gh run list --json` filtered by headSha | PASS | 1 workflow for `dd2907eb`, all success |
| `git rev-parse <tag>^{commit}` | PASS | peel-verified before quoting the tag |
| baseline + post-merge `bun run typecheck` | PASS | both rc=0 -- the pairing is what makes the green attributable |

**What worked:** the baseline-then-post-merge typecheck pairing, reused from promote #1. A single
post-merge green proves nothing about attribution; the pair does.
**What failed:** nothing. `worktree remove` hit the known Windows long-path class again; `prune` ran.
**Gap found:** none new. The LD-0367 wrong-branch-in-refusal defect from promote #1 reproduced
identically on this promote's PROD push (gate named `CLOUD`); already routed to CTO by MSTR, not
re-raised.

---

## Blockers

**None.** Four integrator push points across two promotes (DEV+PROD x2). The audited
`# never-override:` escape was available at **all four** and taken at **none** -- coordinated with
MSTR each time. Total cost across all four: a few minutes.

---

## Residuals (unchanged, none blocking)

1. 9 null prices estate-wide -- genuine data nulls, render as em-dashes. DE traced the shared one to
   `US066922477`, a CUSIP-shaped identifier rather than a real ticker.
2. Pre-existing `ModelPortfolios.tsx:15:149 'ReferenceLine'` lint error -- fails `ci.yml` on DEV,
   cannot reach PROD (`deploy.yml` has no lint step).
3. PROD carries no Surface-Check Gate workflow -- accepted consequence of Andrew's retirement.
4. Two `.runtmp/portal-promote-*` physical dirs persist (Windows long-path); pruned in git, inert.
5. Not mine: 3 past-window ledgers under `0.7.0_AE_CloudOps`; MSTR picked this up.
6. Stale worktree `Desktop/_portal_hotfix_wt` on an already-landed hotfix branch.

## Two fences that must not be "tidied" (both live, both load-bearing, for DIFFERENT reasons)

- **`price` stays in the producer's `NON_SCORING_COLS`** -- never percentile-ranked, never in
  `pctls{}`, never in `factor_metadata`. DE verified absence from `values{}` in the EMITTED
  artifact, not merely in source -- I checked source and would have missed an emission-layer leak.
- **No FX conversion anywhere.** Price is raw local trading currency (acwx max 2,708,000, South
  Korea). Display shows `$` only for US-only universes. Converting at the producer would be a
  derivation outside the fence; hardcoding `$` at the display would print `$2,708,000.00` for a
  Korean listing. MSTR has stated they will enforce both halves.

---

## What I am carrying out of this session

**DE's screenshot catch.** At 100px the column truncated NVR to `$6,304...`. That passes typecheck,
lint, schema-check and my parity gate -- **every instrument I own**. A truncated price on a column
whose only job is letting a human eye judge plausibility is a total defect invisible to the entire
text layer. It was caught by rendering it and looking. This is the same shape as the session's other
lesson (an instrument that structurally cannot report the failure it is being asked about), arriving
from a completely different direction.

---

## Next Steps

1. **[0.0.0_AB_MSTR]** Push CLOUD -- `91b94def3f` (session log #1), `52ecaddc01` (pointer #2), and
   this log. All post-date the `610d3f3f69..aecb61dad8` push.
2. **[1.0.0_SA_CTO]** LD-0367 hook names the PARENT repo's branch in its refusal when pushing from a
   `.runtmp/` worktree -- reproduced on both promotes. Routed by MSTR.
3. **[0.7.0_AE_CloudOps]** Three past-window deploy ledgers, one with 3 stranded legs.
4. **[0.3.0_DT_TradingOperations / me]** Available. SSCN_PRICOL needs nothing further from this seat.
