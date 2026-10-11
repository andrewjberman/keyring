# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), ADVI_FIRMBKTS round 3 drain, 2026-10-11 07Z

**archetype:** COORDINATE

Loop: none armed. Same session as the 06Z log; one `/dispatch ADVI_FIRMBKTS` round in the drain.

| UTC | limb | project/round | TOs t/T | act fired |
|---|---|---|---|---|
| 06:3xZ-07:0xZ | L7 drain | ADVI_FIRMBKTS 3 | 5/11 | FB-f-1, 3, 4, 5, 6 closed and merged; FB-f-2 and FB-f-7 re-seated on amendments and closed (mapping_v3 FAULT 89 to 84; advTenant dormant build, grid 88 of 88 and 396 of 396) |
| 07:0xZ-07:5xZ | L7 | ADVI_FIRMBKTS 3 | 7/11 | the window: act 1 pair SIGNED (CTO @d30c5fe203), its all-ASCII precondition built and merged (`acf8a16706`), executor lane `0.7.0_AE_CloudOps~FB1` seated, STOP on the bundled `tier_policy.mjs` ruled (amendment 3), STOP at plan on the WAF ACL ruled by a pair addendum (CTO @d1fe697698, amendment 4); act 2's phase A merged (`b0eebb018d`: registry file, generated `.py` view, module, 66 routed writer lines) |

## Rulings by the issuer in this stretch (inside the decomposition, each with its row)

- D1-W17-S1 and S5: an alias and its scope's own tenant form ONE equivalence class (the PRD's "aliases included, to one
  firm"), so the dormancy grid reads 0 and 0.
- D1-W16-S13: the generated view is a `.py` module, because the deploy plane ships only `.py` and `opal_naming.py targets`
  must exit 0.
- D1-S11: the gate on non-ASCII reads the BUILT artifact (the CTO's close is "the deployed file reads 0").
- D1-S12: the WAF ACL rider is a named permitted change with its own pair addendum, not a route around the pair.

## Defects in this tick's row, stated

- Four of my own cut errors surfaced as worker or executor stops: an alias's own directory missing from its set (my spec
  listed only the scope's tenant); a criterion count floor set at 47 where the build needed 42; a staged order whose
  lens lines read "TO BE RUN" (gate refusal); a phase-A face that left the order's status line below the line count I told
  workers to stop at, so each worker reported the flip as blocked.
- Two worker instances went INVALID at the drain on PENDING artifact rows after a later instance commit; I pinned both.
  The rule (a PENDING row for an already-committed file is the CCX class) is the checker's, not new.

## Left open

- Act 1 (`TO-FB-f-8` phase B): the executor's plan is signed for three changes plus the ACL rider; apply and the CTO's read
  at `Deployed` are the executor's and the CTO's.
- Act 2 phase B (the mode move, 14 scripts + module + view + 9 runner/launch files, 66 writer lines), act 3 (delta copy,
  needs `FB-f-1`'s compare, done) and act 4 (list entry, map value, F6 deploy, 5 non-ASCII source bytes already out) stay
  staged; each needs its pair and its change-management entry.
- `FB-f-2`'s judgement calls (family names, `bronze/eclipse_qa/` placement) are the CTO's to check.
- `wk-firmbkts-4` and `-9`: still held by the submodule disagreement; two scratch-residue directories moved aside.
- Push state: LOCAL on `box/dell1`.

## Compiler Tools

| tool | result |
|---|---|
| `proof-of-spec-check.py` | two worker instances INVALID at the drain on PENDING pins (CCX class), fixed; five VALID |
| `safe-merge.sh` | refused once on another seat's staged files (retried when clear); fast lane on every other merge |
| `opal_naming.py validate`, `targets`, `generate --target` | validate 15 files OK; `targets` exit 1 on a JSON view, 0 on the `.py` view |
| `naming-gate.py --diff --enforce` | refused the hand-kept table (26 REFUSE), passed the generated view through its mark |
| `to-pipeline-gate.py` | refused lens lines that read "TO BE RUN" (9), admitted every amendment after |
| gap | `git worktree remove` leaves an ignored `.scratch/` directory behind and the path cannot be reused until it is moved |
