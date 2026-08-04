# Canonical-map PROD promote (2d33ea2c / portal-v2.1.156) + two ack-channel gates -- 0435-0630Z

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE

Spawned early (COO/CTO lead-time call) for the canonical-map portal promote; the early spawn
converted three would-be morning surprises into pre-gate fixes. Session remains LIVE (event-driven
hold); this is the window log, not a close.

## Current State (zero-context handoff surface)

- **LIVE PROD: `2d33ea2c`, tag `portal-v2.1.156` (peel-verified: tag^{commit} == origin/PROD
  head), CI "Deploy to Production" run 30883025692 conclusion:success** (gh run view --json,
  watched to conclusion in background, never `gh run watch`). Content = canonical map
  (`7d544d27`: Andrew voice memo dispatch @7a585074e, group-1 value repoint + CI-R6R T2/T3
  participation rendering) promoted as pinned head **`0576ef22`** (empty ack-format commit,
  tree-identical -- review/deploy-split law). Rollback base `c6f561b6` encoded in the merge
  message. Parity gate `git diff origin/DEV HEAD` was EMPTY.
- **Authority chain:** Andrew-direct ~0545Z at DE terminal (verbatim @c6b19d7f67: deploy as soon
  as frontend clean; NOT emitter-gated) superseded the {emitter + first clock-v3 fire} gate; CTO
  formal discharge 055142Z; COO explicit GO 055352Z. Promote executed inside the GO with COO's
  054422Z addendum.
- **Hand-check addendum (now a standing /prod-deploy step):** comp-surface-check blocking run BY
  HAND on the real merged tree pre-push, ack extracted from the ACTUAL merge range with the CI's
  exact sed -> verdict READ: CRITICAL benchmark+headline named, then `SEV1 ACKNOWLEDGED ...
  Proceeding.` rc=0. Two ADVISORY contract notes (model_portfolios.headline UNCONTRACTED pending
  CVO TO-3; benchmark WATCH noise).
- **Workspace pointer:** origin/CLOUD gitlink CONTENT-VERIFIED = 0576ef22 via corrective
  `b26bbe4e` (see incident 2 below). Main portal tree ON DEV at `d32f5a52` (DE's deliberately
  UNPUBLISHED next-cycle commit -- kill-list row 15; rides its own review chain). Promote
  worktree torn down + pruned; deploy ledger
  `org/critical_paths/change_management/20260804T0558Z_canonical-map-portal-promote_deploy_completion.md`
  **CLOSED** @64b7f9caa.
- **Incident 1 (pre-gate, caught by early DEV push): SURFACE_ACK format seam.** CI Surface-Check
  Gate FAILED rc=2 on 7d544d27 (run 30880062845) while Build+Validate was green (30880062803,
  same sha) -- DE's ack was authorized + audited but the message line read `SURFACE_ACK
  justification:` where the CI sed requires literal `SURFACE_ACK:`. Exercised both directions
  (real range extracts empty; canonical control extracts). Remediation: DE's empty commit
  0576ef22 with canonical line; MSTR pushed pinned `0576ef22:DEV`; gate green 30880952383
  (empty-range short-circuit DISCLOSED; COO adjudicated MET-WITH-DISCLOSURE on composed
  evidence). CLASS FIX BUILT (CTO-ratified, routed to me): **portal commit-msg hook auto-append**
  @8500c12a5 -- SURFACE_ACK env feeds BOTH channels in one authoring act; post-append self-check
  runs the CI's OWN sed; two-story drift + multiline refused LOUD; selftest 6/6 + installed-hook
  scratch-repo exercise (4 directions) all correct; installed live via install.sh.
  **ACCEPTED-AT-BUILD (CTO 062647Z); full acceptance pends first REAL SEV1-acked fire** (likely
  DE's d32f5a52 cycle -- observation owed to CTO).
- **Incident 2 (Step 6): gitlink clobber.** MSTR's pointer commit 13ac2c307 recorded gitlink
  d32f5a52 (unpublished -> unresolvable downstream) despite its 0576ef22 message: safe-commit's
  pathspec staging re-reads the submodule worktree HEAD, silently clobbering their
  update-index --cacheinfo pin; their verify read STAT not CONTENT. origin/CLOUD carried the
  broken gitlink ~0619-0626Z. Corrective `b26bbe4e`: temp index + commit-tree +
  compare-and-swap update-ref (CAS base moved 2 commits mid-fix -- race-safety was load-bearing),
  audited never-override (safe-commit's staging IS the clobber mechanism; shared index held 2
  FOREIGN staged items a bare commit would sweep; portal checkout untouchable, DE live).
  MSTR pushed + content-verified. **Gate candidate RATIFIED by CTO 062647Z: safe-commit refuses
  on staged-gitlink != pre-staged pin; SEATING VIA COO; acceptance = incident replayed as a
  failing control.**
- **Also this window:** COO-owed supersession committed @09b519740 (07-22 cottonwood
  458,189,558.77 struck at MDPF_NONMODEL_PRODUCER_TRACE_20260728.md:30, KNOWN-WRONG anchor per
  0.4.0_DS @387fa87c90; EXACT verdict stands -- measured shared derivation, not truth).
  Promote-scope defense: DE's content-bearing d32f5a52 appeared on local DEV mid-window; pinned
  OUT (COO scope call, CTO concurrence, DE deliberate-next-cycle answer) -- also surfaced the
  ack-scope-vs-range-scope seam (CI range-scan would let commit A's ack blanket commit B's SEV1
  touches; CTO ACCEPTED-NAMED-DEFERRED, mine to propose after fires clear, design prior
  SURFACE_ACK[<short-sha>]).

## Deployment Sequence + Verification (DT addition -- actual output)

```
git push origin PROD (worktree, audited never-override, MSTR no-objection 060654Z):
  OK: no unlabeled reads ... VALGATE D-1 ... PASS (no-op)
  INFO: PROD push detected -- running typecheck (tsc -b --noEmit)
  OK: typecheck passed -- proceeding with PROD push
  c6f561b6..2d33ea2c  PROD -> PROD
gh run view: DEPLOY-PROD 2d33ea2c run 30883025692 CONCLUDED: success
tag peel:   portal-v2.1.156^{commit} = 2d33ea2cd9bfc69809c03787d1240e658c63361d == origin/PROD
pointer:    git ls-tree origin/CLOUD portal -> 160000 commit 0576ef22... portal  (CONTENT read)
hand-check: SEV1 ACKNOWLEDGED (SURFACE_ACK='Sovereign canonical-map dispatch @7a585074e ...')
            -- audited. Proceeding.  rc=0
```
Note: first PROD-push attempt was correctly BLOCKED by the LD-0368 gate (override comment was
pipe-detached); retried with the override on the simple command. The gate works as built.

## MCP traffic (window)

~30 messages handled. Significant: COO closure ACK + timing correction 051254Z + delta 051424Z;
MSTR DEV/CLOUD pushes 051604Z; my RED-gate finding fan-out 0519xZ (DE/COO/CTO); CTO gate
ratification + build routing 052038Z; DE ack-fix 052055Z + next-cycle answer 052926Z; COO pin
ruling 052920Z + adjudication 054422Z; CTO discharge 055142Z; MSTR sequencing relay 055244Z; COO
GO 055352Z; MSTR no-objection 060654Z; MSTR pointer claim 062015Z -> my falsification + fix
062511Z -> their content-verified push 062711Z; CTO ACCEPTED-AT-BUILD + gitlink ratification
062647Z; completion reports 0628xZ (COO/CTO/MSTR).

## Files Modified

See commit messages: 09b519740 (supersession), 76299b0e9 (ledger open), 8500c12a5 (commit-msg
hook + install.sh + /prod-deploy doc: headSha-enumeration law + hand-check step), b26bbe4e
(pointer corrective, plumbing, full mechanism in body), 64b7f9caa (ledger close). Portal:
2d33ea2c (PROD merge). All CLOUD commits through b26bbe4e pushed by MSTR; 64b7f9caa + this log
await the next integrator sweep.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-which (A.3 exercise) | PASS | forwarder ran with banner; 94/94 resolve |
| comp-grep (audit-writer hunt) | PASS | located ack path family: .tools/comp-surface-check -> org/modules/graph/surface_check_cli.py + portal-hooks source-of-truth header |
| comp-surface-check (BY HAND, blocking, merged tree) | PASS -- SEV1 ACKNOWLEDGED rc=0 | the COO-addendum observed composition; output read in full, 2 ADVISORY contract notes banked |
| comp-surface-check (auto in safe-commit x4) | OK all | no critical surface touched by workspace commits |
| comp-pulse (auto risk-reflex x4) | CLEAN x3, HOLD-advisory x1 | HOLD cited a DS/49-schwab-conv commit-authority memory -- read, not applicable to DT-lane prod-deploy doc |
| CI's exact sed (control-on-the-retrieval, x5) | discriminated correctly every time | real range empty vs canonical control extracts; merge-range extraction fed the hand-check |

What worked: every gate that fired tonight was a correct block with a sanctioned path through
(LD-0276 heredoc gate on my scratch compound, LD-0368 push gate on the pipe-detached override,
CI Surface-Check red, commit-msg drift fixture). Listing CI runs BY HEADSHA caught the
green-beside-red workflow split. What failed: MSTR's stat-not-content pointer verify (their own
lesson note banked); my first rc read through a pipe (re-ran unpiped). Gap found: safe-commit
gitlink clobber (gate candidate ratified, COO seating); the CI ack-parse and local ack channel
had no format tie (closed by the auto-append hook this window).

## Blockers

None. All residuals have named owners: gitlink-gate seating [2.0.0_SA_COO]; auto-append
first-fire observation [me -> 1.0.0_SA_CTO]; seam-2 proposal [me, deferred until fires clear];
T3 footnote scope question [0.4.0_DE_ClientPlatform at Andrew, non-blocking]; emitter lights the
served page on its own schedule (zero portal changes needed).

## Next Steps

1. [me] Event-driven hold; observe the auto-append hook's first real SEV1-acked fire (likely
   DE's d32f5a52 next cycle) and route the observation to [1.0.0_SA_CTO].
2. [2.0.0_SA_COO] Seat the safe-commit gitlink-refusal gate build (CTO fix shape bound).
3. [me] Seam-2 (ack-scope vs range-scope) proposal to CTO after fires clear.
4. [0.0.0_AB_MSTR] Next integrator sweep picks up 64b7f9caa + this log commit.
