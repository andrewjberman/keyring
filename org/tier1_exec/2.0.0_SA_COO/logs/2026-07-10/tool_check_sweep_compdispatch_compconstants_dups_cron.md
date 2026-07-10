# Tool-check sweep window: comp-dispatch closed, comp-constants reg leg, comp-dups cron answered, comp-debt found, family closed at 3

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, TRACE
**serial:** 2.0.0_SA_COO
**window:** ~2026-07-10T2104Z -> 2120Z

## What this window did

The tool-check workflow's COO leg (I do directory/registration/cleanup downstream of CVO's fix + CTO's gate).
Answered CTO's time-sensitive sovereign-safety question, closed two tool legs, and ran a completeness sweep
that closed the latent-bd-scanner family at exactly three tools with the scariest candidate ruled out at source.

## 1. comp-dups --nightly cron check (CTO's 210432Z, time-sensitive) -> NOT WIRED

The "prohibition stops agents, not crons" trap. Verified the WIRING (did NOT run comp-dups, did NOT read any
bd file). **No automated trigger invokes comp-dups (any mode).** Grounded on 5 independent surfaces + a control:
- `derive_runner.py` (the "post-derive hook" the docstring names): 0 refs to comp-dups/dup_scan/run_scan
  (control: file real, 2015 lines).
- No `.tf` references comp-dups -> no EventBridge/scheduled-Lambda. The two globgrph crons (comp_learns 04:00,
  stitch-produce 03:00) target other tools.
- No `.github/workflows` (CI), no crontab, no nightly/post-derive script.
- No session cron (CronList = "No scheduled jobs").
- `NFRA_DEBTSCAN.json:35` records the nightly hook as an OWED-UNBUILT leg ("comp-dups runs on-demand now").
=> Nothing to pause. Agent hold + CVO's structural guard cover it fully. Answered to CTO 211037Z; CTO accepted 211352Z.

## 2. comp-debt = a THIRD same-family latent bd-scanner (found while grounding #1)

`org/modules/graph/comp_debt/signals/duplicates.py:96-107` -- `run()` defaults to `from_ledger=False` ->
`dup_scan.run_scan()` LIVE (the same 337-bd-file scan). `--from-ledger` reads the gitignored dups_latest.json
which is only written by `--nightly` (never scheduled) so it RAISES on most boxes -- so comp-debt's only working
path IS the bd scan. [SOURCE-CONFIRMED @ working-tree.] **CTO added comp-debt to the fabric HELD list** (211352Z)
and scoped CVO base's guard to the `dup_scan._py_bodies`/`run_scan` CHOKEPOINT (one guard covers all callers).

## 3. Completeness sweep -> latent-bd-scanner family CLOSED at THREE tools

Enumerated every caller of the chokepoint (greps scoped to exclude bd after my first broad grep incidentally
surfaced 2 bd lines -- a different namespace-local `run_scan` in an ACAT diag script, classified false, not read
further; the "a broad grep is itself a latent bd-reader" lesson applies to me too):
- **dup_scan chokepoint** external callers = comp-debt's duplicates.py ONLY (+ comp-dups shells engine direct +
  engine's own main + the existing `test_dup_scan_sovereign_guard.py`). Closed at 2 tools.
- **comp_constants scan_all**: full-surface glob (incl bd) fires ONLY on `only_file=None` (bare check/scan);
  the commit-gate path (`cmd_check` via `check --file <f>`) scopes to `[only_file]` = the one committed file
  (`comp_constants_cli.py:202-205`). **The commit gate does NOT read bd on every commit** -- the every-commit
  breach scare is FALSE, source-confirmed. This is why CTO's carve-out "comp-constants except check --file
  <non-held>" is the right shape.
- **tooltip_cli.py scan_all** = local fn globbing `PORTAL_SRC.rglob('*.tsx')` (portal frontend only) -- NOT bd,
  not in family. False match.
=> Family = {comp-dups, comp-debt, comp-constants}, all HELD. No 4th door, no every-commit exposure.

## 4. comp-dispatch (TOOL-14) cleanup leg CLOSED

CVO fixed (8531cf95a, CTO-GREEN 210406Z). My leg:
- Close verified BY HASH: 8531cf95a ancestor of origin/CLOUD (impossible-hash control correct); corrupted
  247ebed24 confirmed ABSENT.
- Directory/naming clean: `.tools/comp-dispatch` wrapper + `comp_dispatch.py` engine + test; no rename, no fork.
- 2 pre-existing surface gaps reproduced with my own controls (`- id:` entry=0; comp-tools.yaml=0, ctl
  comp-aws=10) -> recorded as worked-example #3 in the coverage-gap brief. FED THE TO, no piecemeal patch.
- Committed **72a672a36** (verified ancestor of origin/CLOUD).

## 5. comp-constants registration leg CLOSED (pending one CTO design ruling)

0.7.0~C's CC2 guard landed (b4868c28b + 10c928176 + CTO test 38fa71f5e -- all verified ancestors of origin/CLOUD).
comp-constants is structurally held (exit-3 refuse on any held-surface scan). My reg-leg disposition:
- NO registration surface is now false -> no touch required. tools_index enumerates subcommands (unchanged) +
  accurate `does:`; no surface enumerates exit codes so exit-3 breaks nothing; wrapper propagates exit-3.
- ONE design Q routed to CTO: comp-tools.yaml:665 usage omits the new `--allow-held-scan` (the audited sovereign
  BYPASS). COO lean + tool-author (0.7.0~C) intent ALIGNED: keep it obscure, do NOT advertise the bypass; if the
  reconcile lists it, with a loud "sovereign sign-off required" note, via TOOLPASS-D1 not piecemeal. CTO's call.

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| CronList | session-cron check for comp-dups | PASS (none) | confirmed no scheduled comp-dups |
| git grep (bd-excluded) | enumerate chokepoint callers | PASS | family closed at 3; scoped to exclude bd |
| git merge-base --is-ancestor | verify 5 commits landed by hash | PASS | all with impossible-hash controls |

What worked: hash-ancestry + impossible-control for every close; source-grounding the cron negative on 5 surfaces
rather than one grep; scoping greps to exclude bd after the incidental brush. What failed: my first caller-grep
was not bd-scoped and incidentally read 2 bd lines (false matches; corrected by re-scoping). Gap found: comp-debt
was an undocumented third latent bd-scanner -- now HELD.

## Current State

- **comp-dispatch:** CLOSED (72a672a36 on origin).
- **comp-constants:** structurally guarded (b4868c28b); reg leg closed pending CTO's advertise-or-not ruling on
  `--allow-held-scan`.
- **comp-dups + comp-debt:** HELD; awaiting CVO base's chokepoint guard fix (`dup_scan._py_bodies`/`run_scan`,
  EXCLUDE-with-loud-note, not sys.exit -- would kill comp-debt's non-bd signals). I delivered CVO the complete
  fixture set (external callers) + the commit-gate source-ruling. CVO briefs me for the registration/cleanup leg
  after CTO gates the diff.
- HELD list (bd-scan class, sovereign): comp-constants (except `check --file <non-held>`), comp-dups (except
  `--validate-dead`), comp-debt (duplicates signal / any run_scan path). On-demand only; agent hold covers today.

## Next Steps

- **[2.0.0_SA_COO]** On CVO base's comp-dups/comp-debt chokepoint-guard brief: verify by hash, check .tools
  registration + naming + deprecated forks, disposition the registration (feed-TO vs no-touch), record worked
  example if a surface gap surfaces. Monitor is live for the inbound.
- **[1.0.0_SA_CTO]** advertise-or-obscure ruling on `--allow-held-scan` (COO + author lean = obscure).
- **[1.0.0_SA_CTO]** TOOLPASS-D1 reconcile TO carries comp-which #1 / comp-cluster #2 / comp-dispatch #3 as
  worked examples (durable brief: tool-registry-coverage-gap-and-missing-status-registry-20260710.md).
