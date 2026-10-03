# AMGT_RESAPP round 63 -- am-6 leg 3, the R1 + R2 repair redeploy -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Date:** 2026-10-02
**Task Order:** AMGT_RESAPP.TO-AMGT-am-6 section 7 (AMENDMENT 2), leg 3
**Status:** COMPLETE -- c7 and c8 both PASS, no regression, rollback not taken.

Delta since `3eeb9490f4`, which covered the memory-only act and am-7 AMENDMENT 3.

## Objective

One code-only redeploy at `96f023071a` carrying this seat's repair cells R1 and R2, with
`memory_size` left at the 1769 the preceding act landed. Graded by two cells that did not
exist earlier in the round, c7 and c8.

## Compiler Tools

| Tool | Invocation | Result |
|------|-----------|--------|
| `build-and-upload-scoped-amgt.sh --build-only` | the pre-upload STOP gate | PASS. `353 / 352 / 1 / 0 / 0`, the one file `scoped_amgt.py`. |
| `build-and-upload-scoped-amgt.sh` | the real build | PASS. Reproduced the diff identically, so what shipped is what was graded. |
| `terraform plan` / `show -json` | act (A) | PASS. 49 `resource_changes`, 1 non-no-op, 3 attributes, `memory_size` before=after=1769. |
| `.tools/safe-apply.sh` + `plan -detailed-exitcode` | one code apply | PASS. 0/1/0 then exit 0. |
| `r63_served.py` c7 / c8 `--where deployed` | graded cells | PASS both, after measuring both base arms first. |
| `r63_served.py` c3 / c4 / c5 `--where deployed` | no-regression | PASS, all unchanged. |
| a route sweep + a null-sector-names read | conditions 2 and 4 | PASS. 9 of 9 at 200; the two null names and their reasons printed. |
| `.tools/deploy_ledger.py` | open / close-leg x3 / close | PASS. Sentinel committed at open, so the full lifecycle is on record. |

**What worked:** reading the check's own source before grading it. c8 prints only COUNTS
("92 served, 2 null with a reason"), and CTO condition 2 asks for "the 2 null names with
their reasons" while condition 4 needs them named for the CVO. Had I treated c8's PASS as
the whole deliverable I would have satisfied the criterion and missed the condition. Same
lesson as the A3 served-key print, hit twice in one session.

**What failed:** nothing in this act.

**Gap found:** none new.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | base re-read live | `wIpMasw...`, 1769, 19:27:18Z -- the memory act's own output |
| 2 | pin resolved by content | `96f023071a` vs HEAD over the package roots: EMPTY; worktree clean |
| 3 | `--build-only` | `353 / 352 / 1 / 0 / 0`; the one file `scoped_amgt.py` |
| 4 | base arms measured on deployed | c7 62 false of 94; c8 0 served / 0 reasoned / 94 wrong |
| 5 | entry opened AND COMMITTED before the act | `7153538672` |
| 6 | build + upload | VersionId `VjnAGYKkemkivjQlxH7k9PpvBlhNnFvt`, 41131919 B, read back matched |
| 7 | code-only `safe-apply` | 0 added, 1 changed, 0 destroyed |
| 8 | post-act live read | `31UL+7/s...`, MemorySize 1769, Successful; re-plan `-detailed-exitcode` 0 |
| 9 | c7 / c8 graded | both SERVED YES at exit=0 |
| 10 | no-regression + null-names reads | c3/c4/c5 YES; 9 of 9 routes 200; two null names printed |
| 11 | entry CLOSED + commit | `a8637f3501`, carrying the sentinel deletion |

## Verification

```
PASS C1 0 ranked-in-both bars serve the false 'not ranked' reason 0 false of 94 bars (prior 2026-09-30, 94 rows); e.g. []
PASS C2 every served places_moved equals prior rank minus rank 94 correct, 0 wrong, 0 truly new with a reason
R63 C7 SERVED: YES
exit=0

PASS C1 AMD serves Information Technology from sub_asset_class sector 'Information Technology' source 'opal_classification.sub_asset_class'
PASS C2 every bar serves a GICS sector with its source, or null with a reason 92 served, 2 null with a reason, 0 wrong of 94; e.g. []
R63 C8 SERVED: YES
exit=0
```

Base arms, measured by this seat before the act:
```
c7  FAIL C1 62 false of 94 bars   PASS C2 32 correct, 0 wrong   SERVED: NO  exit=1
c8  FAIL C1 AMD sector None        FAIL C2 0 served, 0 null with a reason, 94 wrong of 94   SERVED: NO  exit=1
```

The two null-sector names (c8 gives only a count):
```
BP/ LN   BP/_LN_Equity   asset_class None  sub_asset_class None  sector None
    reason 'the classifications table holds no classification for this ticker'
NG/ LN   NG/_LN_Equity   asset_class None  sub_asset_class None  sector None
    reason 'the classifications table holds no classification for this ticker'
TOTALS CHECK: 92 + 2 + 0 = 94 against a denominator of 94 -> accounted
```

No-regression sweep at the landed code:
```
BA overlay 101996 IDENTICAL  thesis 506924 IDENTICAL  peers 51165 IDENTICAL
VLO overlay 104807 IDENTICAL thesis 658857 IDENTICAL  peers 51356 IDENTICAL
collected/chatter 70296 (was 67005 -- R2 adding sector/sector_source)
BA /timeline 121773        BA /timeline/day/2026-09-08 2045
9 of 9 answered 200; 0 non-200; 0 of 6 leg-1 comparables moved
```

## Decisions Made

1. **Read c7's base as two clauses, not one verdict.** Its C2 already PASSED at the base
   (32 correct, 0 wrong), so the defect R1 repairs is specifically the FALSE "not ranked"
   reason on bars ranked in both generations -- not the `places_moved` arithmetic. Recording
   only "c7 was NO, now YES" would have blurred what was actually broken.
2. **Reported the 32 + 62 = 94 reconciliation as the strongest read of c7.** C2 went 32 ->
   94 correct, and 32 plus the 62 previously-false bars is exactly 94. So R1 produced a
   correct number for precisely the rows that were wrong rather than merely suppressing a
   reason string, and the denominator closes.
3. **Wrote the null-sector-names read rather than citing c8's PASS.** c8 satisfies the
   criterion with counts; conditions 2 and 4 need the names and reasons. Writing the read
   was the only way to satisfy the condition.
4. **Surfaced the slash-ticker pattern without acting on it.** The two null-sector names are
   the same `BP/` and `NG/` LN pair whose peers objects this seat rebuilt under am-7
   AMENDMENT 1. One handling gap rather than two coincidences -- but the half rules
   null-with-reason correct and no cell of mine owns the classifications table.
5. **Named the one body size that moved instead of reporting "no regression" flatly.**
   `collected/chatter` went 67005 -> 70296 B. That IS R2 reaching those rows; a
   byte-identical chatter body would have been the defect. The condition asks for 200 and
   unchanged counts there, and c3 still reads 95 of 95.

## Files Modified

See commit messages: `7153538672` (entry opened), `a8637f3501` (closed + instance). No
terraform file changed -- act (A) is code-only and `memory_size = 1769` stays as the
preceding act committed it.

## Blockers

**None owed by this seat.**

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 31UL+7/shJz1oKH1fc/5lb3vGLqlIDk+HgjLoGxe05w=` at
`MemorySize 1769`, artifact VersionId `VjnAGYKkemkivjQlxH7k9PpvBlhNnFvt`. Six NEVER-2
entries opened and closed this session, every leg proven, none left open.

Round 63 served state: c2 YES (7/37/8 officers), c3 YES (95 of 95), c4 YES (12 of 12 x2),
c5 YES, c6 YES (52 of 52), **c7 YES (0 false of 94)**, **c8 YES (92 + 2 of 94)**. c1
remains NOT MET per addendum ruling 1 -- cold BA 2026-09-08 is ~12 s against a 5,000 ms
bound, and memory is not the lever.

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** DSGN FWD-2 is re-gradeable on PROD after this act, and FWD-7 after
   am-7 A3. Routing both requests is `2.0.0_SA_COO~Z`'s. For FWD-2 the grader needs
   `BP/_LN_Equity` and `NG/_LN_Equity` named as null-sector BY DESIGN with their reason, not
   read as missing.
2. **[`2.0.0_SA_COO~Z`]** Round-64 cold-read cell per addendum ruling 3 -- the only remaining
   lever on c1. It adds code to this artifact, which sits at 96.8% of the ceiling with
   8,473,968 B spare, so it measures size at cut time.
3. **[`1.0.0_SA_CTO~Z`]** Whoever owns the classifications table: no row exists for the
   slash-ticker LN names. Correct as null-with-reason today; worth knowing the pattern is the
   slash ticker.
4. **[`0.0.0_AB_MSTR~Z`]** The push. All eleven commits from this seat today are LOCAL.
