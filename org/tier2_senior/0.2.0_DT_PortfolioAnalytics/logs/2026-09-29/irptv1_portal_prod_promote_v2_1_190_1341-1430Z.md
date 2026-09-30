# Portal DEV 18899c96 -> PROD 9a8f6c71 (portal-v2.1.190): the promote whose authorized sha was stale before it was authorized -- 0.2.0_DT_PortfolioAnalytics~P

**archetype:** DEPLOY

**Date:** 2026-09-29
**Task Order:** ad-hoc, Andrew-direct (no TO; this lane holds none)
**Status:** COMPLETE

---

## Objective

Run `/prod-deploy` to promote portal DEV to PROD on Andrew's word, unblocking two held release orders:
`2.0.0_SA_COO~M`'s Holdings CATEGORY step and AD-10's directory reader. The AD-10 re-mint was HELD because a
PROD reader without `account_masks` would REFUSE the new key and client search would fail.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'account_masks' portal/src --limit 20` | PASS | Located the reader (`contracts/directory-browse.ts`) and the wire type in one shot; printed denominator 11 hits / 1203 files, 5 BINARY not searched. The DEF/SURFACED banding put the validator line above the tests without my filtering. |
| comp-which | `comp-which "how do I grep the repo"` (startup exercise) | PASS | Forwarder RAN, not merely resolved. |
| comp-tool rail | PATH census at startup | PASS | 104 of 104 comp-tools resolve bare. |
| comp-pulse (risk-reflex) | auto, inside `safe-commit.sh` | WARN | Self-reported `ANSWER STATE: PARTIAL_OR_BLIND`, danger map 117.0h STALE, `scanned 0 of 1 file(s)`. It said plainly that it COULD NOT clear the diff rather than printing a clean line -- correct behaviour, and the reason I did not cite it as validation. |
| commit-gate | auto, inside `safe-commit.sh` | WARN | `checked 0 of 1 file(s) -- NOTHING WAS CHECKED`; reads only .py/.sh/.tf/org/projects/*.json, so a gitlink and a .md fell through. Cited as NOT-evidence, per its own text. Frontend evidence came from `tsc -b` and the served-bytes read instead. |
| comp-pipescript io | not run | SKIPPED | DT minimum applies to a deployed SCRIPT. This promote deployed no script: it is a git-merge + CI build of the portal frontend. No `.py` touched. |
| comp-iam service | not run | SKIPPED | No new boto3 call; no Lambda touched. |
| comp-routes behaviors | not run | SKIPPED | No CloudFront behavior or Lambda@Edge change. CI's own `deploy.yml` owns the S3 sync + invalidation; I changed no route. |

**What worked:** `comp-find`'s printed denominator and DEF banding answered "where does the reader live" without
a manual sweep, and its `--limit` kept the census intact. The two auto-gates inside `safe-commit.sh` were more
valuable for what they REFUSED to claim than for what they checked -- both printed explicit not-evidence lines,
which is exactly what stopped me citing a green commit as frontend validation.

**What failed:** Nothing in the comp-tool layer. The failure this session was in `gh` (below).

**Gap found:** No comp-tool answers "does the SERVED, code-split frontend bundle contain token X". I did that by
hand: enumerate the entry bundle's chunk references, fetch all 51, sweep with a printed denominator and both
controls. That sequence is the reusable shape, and its first form was WRONG (see Instrument Failures). A
`comp-served <token>` that resolved chunk fan-out and printed the denominator would have made the wrong answer
unreachable. NOT proposing a build: CLAUDE.md bars me from implementing an unrequested gate, and this is a
routing note for whoever owns the comp-tool surface.

---

## Work Completed

### 1. The payload was stale before it was authorized -- asked, did not adjudicate

The Andrew-direct record authorized DEV `27eae57a`. I measured `origin/DEV` at `18899c96748e`, ONE commit ahead:

| | |
|---|---|
| passenger | `18899c96` `2.0.0_SA_COO~D` 2026-09-29T13:18:15Z, "DirectoryEntry wire type regenerated from the committed schema -- account_masks (AD-10)" |
| ancestry | `27eae57a` IS an ancestor of `18899c96` (`merge-base --is-ancestor`) |
| timing | landed 13:18Z, **BEFORE** the ~13:3xZ card -- the card's 12:14Z `ls-remote` was already stale when Andrew answered |
| count | `origin/PROD..origin/DEV` = **137**, not the card's 136 |

Every signal pointed at "obviously fine": one commit, by the project's own COO, CI-green, CTO-approved at
`50469a2a6c`, and serving the exact reason the card named. I still did not take it. CLAUDE.md is explicit --
*"the receiving agent does NOT adjudicate scope ... if wider seems plausible, ASK"* -- and a DT widening
Andrew's word on a PROD promote because the extra commit looked helpful is the whole failure class. Asked
`0.0.0_AB_MSTR` (msg 102825) and HELD the merge and push.

MSTR amended the record on Andrew's second word, verbatim **"Promote 18899c96 (Recommended)"**, covering exactly
that sha and nothing later (record `@af463119f2` AMENDMENT; relayed by `1.0.0_SA_CTO` msg 102829 because MSTR is
barred from Tier-2 writes; acked READ). The record states the stale read was MSTR's error and that MSTR asked
rather than widening.

**Consequence for the merge command:** because the word covers exactly `18899c96`, I merged the **explicit sha**,
not the moving `origin/DEV` ref. Had a DEV push raced my merge, `--no-ff origin/DEV` would have silently widened
the payload past Andrew's word -- the precise hazard `/prod-deploy` Step 0 documents. The parity gate then proved
the two were still identical.

### 2. The promote -- 10 of 10 steps

| # | Step | Evidence |
|---|---|---|
| 0 | DT gate; `$WS` derived not typed; inbox empty, no `[STOP]`; freeze declared to `~D`+`~M` | 2 DELIVERED / 0 QUEUED / 0 REFUSED, denominator 2 |
| 1 | tree on `DEV`, local NOT ahead of `origin/DEV` -> Step 1a not entered, no DEV push | `origin/DEV..HEAD` empty |
| 2 | `bun run typecheck` -> `tsc -b --noEmit` | rc=0, ZERO errors |
| 2b | DEV CI green enumerated BY headSha | `18899c96` run `36574405728` success |
| 3 | `update-ref refs/heads/PROD refs/remotes/origin/PROD` | **caught stale local PROD `36a37afce`** -> `a0314f22`. The dry-run-pollution class, live on this device. |
| 4a | ephemeral worktree at PROD | `.runtmp/portal-promote-20260929T135632Z` |
| 4b | `bun install` FOREGROUND | 377 packages, rc=0, 208.35s |
| 4c | `git merge --no-ff 18899c96` (explicit sha) | `9a8f6c71efb2`, rc=0, no conflicts |
| 4d | parity gate | EMPTY vs both `origin/DEV` and `18899c96`; positive control vs PROD base non-empty (183 files, +17379/-3021) |
| 5a | `git push origin PROD` | `a0314f22..9a8f6c71`; VALGATE D-1 PASS, paired-provenance OK, pre-push `tsc` PASS |
| 5b | `deploy.yml` | run `36580348558` conclusion=success, n=1 workflow on the sha |
| 5c | tag PEELED | `portal-v2.1.190`: object `b95ab8cecf21`, commit `9a8f6c71` == `origin/PROD` |
| 6 | pointer commit | `06f4c5d7ce`, msg-verify MATCH len=1235 -- **LOCAL, see 4** |
| 7 | teardown | `worktree remove` FAILED "Filename too long" (documented long-path class); `prune` OK, 0 promote worktrees tracked; main tree on `DEV`; cwd at workspace root |
| 8 | report | freeze released (102833/102834), MSTR ask (14:28:48Z), ledger CLOSED `6b33fa6790` |

### 3. Served-artifact verification -- and the read I got wrong first

CI success is the producer's self-report, and CLAUDE.md forbids resting on it. The real gate is whether PROD
SERVES a reader admitting `account_masks`.

**First read, WRONG:** `account_masks` = **0** occurrences in the served entry bundle
(`index-27CK7J5N.js`). Taken at face value that reads as "the promote did not ship the reader" -- and I would
have reported a landed promote as functionally failed. The bundle is 347 KB and the app is **code-split across
51 chunks**, so the entry bundle is the WRONG DENOMINATOR: an out-of-corpus zero, not an absence.

What exposed it was the **positive** control, not the negative one. My negative control (`zzz_not_a_real_token`)
also returned 0 -- which proves nothing, since a broken read returns 0 for everything. Checking a token that
MUST be present did it: `DirectoryEntry` = 0 in the entry bundle too, while `InvestorReporting` = 1. A
never-present token and a must-be-present token returning the SAME 0 is the tell.

**Correct sweep:** all **51 of 51** referenced chunks fetched (denominator printed, zero fetch failures). ONE
carries the token: `resolveBundle-BVyRHWDP.js`, `Last-Modified 14:10:19 GMT` (the new build; push was ~14:07Z).
Served bytes:

- `...,"revision","cohort"],["contract_version","account_masks"]),...` -- the key is in the OPTIONAL-keys array
- `...||!uI(e.account_masks)||...` -- the validator actually calls the mask check
- controls in that chunk: `masked_discriminator` = 1 (positive), `zzz_absent_token` = 0 (negative)

**AD-10 precondition MET:** the served PROD reader admits `account_masks`, so it will not refuse the new key and
client search will not fail. The bundle skip (102500 / 102812) has its release condition satisfied; lifting it
is `~D`/`~M`'s act, not mine.

### 4. What I did NOT do: push CLOUD

`/prod-deploy` Step 6 prints `git push origin CLOUD`. I did not run it. Step 0 of that same skill quotes GATE 5
as admitting a DT pushing `PROD`/`DEV` **in the portal repo** and states *"Workspace branches and any `pull`
stay integrator-only"*; org/XXX.md SHARED-BRANCH LAW agrees. The skill contradicts itself, so I took the
narrower line and left both workspace commits LOCAL, then handed the push to `0.0.0_AB_MSTR` with the defect
named. Not worked around silently, and not self-adjudicated by trying the push to see whether the hook let me.

---

## Push state (MEASURED at report time)

| Ref | State |
|---|---|
| `origin/PROD` (portal) | **`9a8f6c71`** ON ORIGIN (ls-remote read), CI-verified |
| `portal-v2.1.190` | ON ORIGIN, peeled to `9a8f6c71` |
| workspace `CLOUD` | **LOCAL `6b33fa6790`**; `origin/CLOUD` = `15655f4a25` (ls-remote read) |

---

## Instrument Failures (both mine, both recorded because the wrong answer was believable)

1. **`gh run list --branch DEV` returned stale rows.** Its newest row was 2026-09-11 `5b959f63`
   conclusion=**failure**, which I read as "DEV CI has been dead 18 days and the last run was red" -- and I said
   so before checking. The UNFILTERED `run list` shows DEV CI running green hourly through 14:20Z. The
   `--branch` filter's result was simply wrong, and a wrong-filter read is INDISTINGUISHABLE from a real
   finding. This is the same class `/prod-deploy` Step 5 flags for `-R`, on a different flag of the same
   command. **Enumerate by `headSha` against an unfiltered list; positive-control every empty or surprising
   `gh` result.**
2. **The code-split zero** (section 3) -- a 0 from the wrong denominator, where only a positive control could
   tell it from a true absence.

Minor: `gh repo view` takes the repo POSITIONALLY and rejects `-R` (`unknown shorthand flag: 'R'`), unlike
`gh run list`. The positive-control line in Step 5 as written fails.

---

## Blockers

None.

---

## Next Steps

- [`0.0.0_AB_MSTR`] Carry local CLOUD `6b33fa6790` (pointer `06f4c5d7ce` + this ledger) to `origin/CLOUD`. Asked
  14:28:48Z. Also owns the `/prod-deploy` Step 6 text conflict.
- [`2.0.0_SA_COO~D` / `~M`] Freeze is released. The AD-10 served-reader precondition is MET, so the bundle skip
  (102500 / 102812) can be lifted -- your act, not the DT's.
- [Andrew] Optional visual smoke of the investor-reporting surfaces on PROD (`portal-v2.1.190`). 137 commits of
  `~D`'s design work now serving.
- [whoever owns the comp-tool surface] The served-bundle token sweep has no comp-tool. Routing note only; I am
  not building it.
