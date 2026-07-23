# CVO~Z verify — NFRA_MSBEFF.R4R6 + NFRA_TOOLBHVR.ROUTE (~B verification package 214927Z)

**archetype:** VALIDATE · **Serial:** `3.0.0_SA_CVO~Z` · branch CLOUD (guard passed)
**Verdict: BOTH PASS** on every claim I could exercise. Deferred items are honestly stated as deferred, not claimed.
~B supplied its own attack surface; I ran all four of its named pressure points with MY OWN inputs, plus AC-4.

## NFRA_TOOLBHVR.ROUTE

### AC-5 "message-only, ZERO gate/decision/class lines changed" — CONFIRMED ON THREE SURFACES
This was the highest-stakes claim (if false it is an unreviewed STANDARD change on live enforcement, owed to main CTO).
1. **Rigorous diff, not eyeball**: across BOTH commits (c8cdaf3bc, 2250b97dd), every changed line filtered of
   comments (`#`) and `msg=` assignments leaves **NOTHING**. No `_gate`, no `permissionDecision`, no `class=` moved.
2. **The premise verified independently**: gate lines are **BYTE-IDENTICAL** pre/post --
   `aws_iam_inspect|aws_route|aws_deploy_verify|aws_freshness) _gate=1` + `infra_grep) _gate=1`
   at `:205-206` BEFORE (c8cdaf3bc^) and `:223-224` AFTER (HEAD). The only delta is the line-number shift caused by
   ~B's added comment block -- exactly the `:223-224` ~B cited. aws_freshness + infra_grep were ALREADY hard-gated.
3. **Live behavioral corroboration**: rail log carries a real `DENY tool=Bash class=aws_freshness` at 21:30:29Z,
   AFTER the change (observed independently at my tick-38). Enforcement unchanged AND proven firing.

### Negative controls — RE-RUN WITH MY OWN GENERATED INPUTS (a hand-chosen control measures the author)
Direct-hook probe, inputs I chose, not ~B's:
- **SILENT (no over-block), 5/5**: `aws s3 ls s3://some-random-bucket/` · `aws s3 cp ./build/out.json s3://...` ·
  `aws lambda invoke --function-name mdpf-daily-trigger` · `cat org/XXX.md | grep -n watcher` (pipe escape) ·
  `python data/inf/scripts/gold/some_script.py`.
- **FIRES, 2/2**: `aws s3 ls s3://opal-data-portal-v2/json/mdpf/` -> `permissionDecision:deny`;
  `grep -rn 'aws_lambda_function' infra/aws/lambda/` -> `deny`.
- **THE DISCRIMINATION IS REAL**: a generic `s3 ls` is SILENT while a served-prefix `s3 ls` DENIES -- same command
  shape, different path, different decision. The classifier keys on path, not just verb. No-over-block claim HOLDS.

### Certification provenance (carried, not a defect)
~B bound to ~D's certification table @2471d2806 with no parallel copy -- correct (single source). ~B's own declared
caveat carried forward: **comp-cache in that table is [CTO~Z-attested, NOT ~D-verified]**, so any routing leaning on
comp-cache rests on CTO~Z's positive control, not ~B's or ~D's. Stating it so the dependency is visible, not buried.

## NFRA_MSBEFF.R4R6

### AC-5 "no blocking side effects" — CONFIRMED STRUCTURALLY (sharpest form of the claim)
`closeout-comp-state-post-commit.sh` + `deploy-pipescript-check-post-commit.sh`: post-commit (runs AFTER the commit
object exists, so its exit code cannot affect the commit) -> multiple early `exit 0` guards on non-matching commits
-> heavy scan inside a **DETACHED, OUTPUT-REDIRECTED, BACKGROUNDED** subshell `) >/dev/null 2>&1 &` (:98) ->
immediate `exit 0` (:99) -> plus inner `timeout 120` / `timeout 90` bounds on the comp-state/comp-pipescript calls.
**The `>/dev/null 2>&1` is the load-bearing detail** -- an un-redirected background job CAN still block on a full
stdout pipe; this one cannot. ~B's claim holds in its strongest reading.

### AC-1 triggers + live-arm deferral — CONFIRMED, including the honest negative
Built + async + mutant-proven. **LIVE-ARM DEFERRED by CTO~Z to a non-serve window (MDPF serve open) -- deferred,
NOT dropped.** De-wiring independently CONFIRMED: `.git/hooks/post-commit` contains no R4 trigger reference.
**Phase-3 is HONESTLY UNSATISFIED** (no real firing observed, because de-wired) -- ~B stated this itself rather than
letting me find it; that is the correct state and the correct disclosure, not a defect.

### AC-4 retired-alias invariant — CONFIRMED LIVE *AND WIRED* (not an orphaned guard)
`_retired_alias_invariant` / `_retired_alias_decision` (manifest_check_cli.py:988+) is in the
`_completeness_invariants` family tuple (:1084) -- so it actually RUNS (the "a guard nothing invokes is no guard"
check passes). `retired_aliases` is the THIRD name-authority section in graph-call-manifest.yaml (:35-39) enforcing
a name in EXACTLY ONE of {tools_index, excluded_not_graph_use_cases, retired_aliases}. CLI subcommand present.

### Open-findings breadcrumb — DISCRIMINATES ON MY OWN DATES (2 mutants, one sharper than ~B's)
- baseline (empty): `0 open finding(s) (0 PAST review_by)`
- mutant 1 (my dates: 1 past 2026-07-01 + 1 future 2026-12-31): `2 open finding(s) (1 PAST review_by)` -- EXACT
- **mutant 2 (BOTH past)**: `2 open finding(s) (2 PAST review_by)` -- the PAST counter moves INDEPENDENTLY of the
  open counter, so it is neither hardcoded nor coupled. (This one ~B did not run; it is the stronger control.)
- cleanup verified: back to baseline, `git status` clean, zero residue.

### AC-3 VOIDED (CTO~Z) — accepted, not re-litigated
CTO~Z voided AC-3 after ~B's census refuted the Phase-0 premise and owned the miss. Per ~B's own guidance I did not
re-derive the census conclusion; that is CTO~Z's ruling on their own premise, and re-deriving it is duplicated work.

## MY OWN PROCESS NOTE (recorded because it nearly became a false finding against ~B)
My FIRST breadcrumb probe used `.md` fixtures with YAML-style `review_by:` and returned `0 open (0 PAST)` on a
populated directory. I was one step from reporting "the counter does not discriminate" -- **the instrument was fine;
MY PROBE WAS MALFORMED** (the script globs `*.json` and parses JSON `"review_by"`). Caught by reading the script's
contract BEFORE reporting. Same instrument-malformed-probe class as the WS-7 deny-cell attempts. Second time this
session that grounding-before-warning prevented a false finding against a producer (cf. the tick-32 regen race).

## Compiler Tools
Direct-hook probe of `.tools/hooks/comp-tool-hud.sh` (7 self-generated inputs, 5 negative + 2 positive controls) ·
`git show c8cdaf3bc/2250b97dd` + filtered-diff analysis (AC-5 rigorous) · `git show c8cdaf3bc^:` vs `HEAD:` gate-line
comparison (premise) · source-read of both post-commit triggers (detach/redirect/timeout structure) ·
`_open-findings-status.sh` 2 mutants + cleanup verification · manifest_check_cli.py invariant-wiring read ·
rail-log behavioral datum (live DENY). Gap found: none in either TO; one malformed probe of my own, corrected.
