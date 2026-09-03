# 1.0.0_SA_CTO~A -- 2026-09-03 05:05-05:35Z -- /canonical-flow NFRA_CLDGRPH: the second, parallel canonical run -- L3 tree registration + L4 PRD v0.4 at the tree home

**archetype:** MIXED (COORDINATE / IMPLEMENT (record + register + PRD landing) / VALIDATE)

**CONCLUSION.** Fresh session at the `~A` lane. Startup A-F clean (watcher `bpckb6dz8`, 5 of 5 delivery rows READ, 0 TOs held,
zero crons). Andrew-direct at this terminal ~05:1xZ: run the canonical workflow on `NFRA_CLDGRPH` in PARALLEL with the base
`1.0.0_SA_CTO`'s NFRA_COMPEFFICACY water test, seats `2.0.0_SA_COO~A` (L5-L6) + `3.0.0_SA_CVO~A` (L8-L10); this seat runs its
limbs only, touches no workflow infra or gate without `/open-calls` egress. Recorded VERBATIM @`8e134cc126` and broadcast to
five seats (93141-93145, 5 DELIVERED of 5). `/canonical-flow` (first observed run of the skill) measured the project PRE-TREE at
L2-done; **L3 landed @`36157989a9`** (first project under D0, second under the tree; the hand-written flat row moved into the tree
row, index generated, missions-tree-check 0 violations) and **L4 landed @`25c66d3358`** (PRD v0.4 at the tree home; limb 5 of the L6
gate exercised on the exact bytes: 0 complaints, two red controls fired). Handoff to L5 = the prd-header-notify frame to
`2.0.0_SA_COO~A` (`PRD_NOTIFY_TO` set on the L4 commit). Push state: origin/CLOUD @`800b85c1a2` (ls-remote 05:1xZ); this seat's
three commits LOCAL by Andrew's push hold to `0.0.0_AB_MSTR`. This seat now holds at L4-done.

## What happened, in order

| time (Z) | act | record |
|---|---|---|
| 05:05-05:10 | `/watcher`: NOT REGISTERED -> registered PID 26988; Monitor `bpckb6dz8` running; 2 inbox frames read (carrier pass 2 @f5f7481015; Andrew's 23:0xZ rulings) | -- |
| 05:08-05:12 | XXX.md A.1-E: shims re-provisioned (empty at launch, same as the base seat 02:00Z); A.2 five known-class findings, not chased; A.3 104 of 104 + EXERCISE ran; B.0 5 of 5 READ; B.1 0 TOs; F no live arm for `~A` | -- |
| 05:1x | Andrew at this terminal: the parallel-run word (verbatim in the record) | @`8e134cc126` |
| 05:16-05:19 | `/canonical-flow NFRA_CLDGRPH` LOCATE: no tree home (`org/missions/D0/` absent); flat row + REGISTRY row + D0 membership present; D0 enum RATIFIED [NFRA]; brief @dfd24a010b; FWD-1..8 RATIFIED; PRD v0.3 @d923c52ba4 flat; COO decomp @05d2c89158 flat; 0 TOs; 0 surprise items -> limb L2-done, claimed `dep_stage: PRD`, class PRE-TREE; the 2026-09-02 hold discharged by his word | record s. "Measured state" |
| 05:2x | broadcast 93141-93145 (COO~A, CVO~A, COO, CTO, MSTR) | -- |
| 05:24 | flat row removed, tree row written (every field carried; `leads` = the three `~A` seats), `derive --write`, `check` 0 violations | -- |
| 05:26 | lane measured with `owned-paths-validate --check-agent`: `~A` permitted on all four L3/L4 paths (rc 0); positive control base CTO rc 0; negative control `0.8.0_AE_CloudComp` REFUSED on the row | -- |
| 05:28 | L3 commit; missions-tree-check at commit: 3 tree/register paths, 0 violations | @`36157989a9` |
| 05:30 | PRD v0.4 landed by script (8 asserted single-occurrence edits); docs/architecture path -> 4-line redirect stub; row `dep_stage` PRD + `prds` re-pointed; index regenerated; limb 5 exercised (green 0 / red 1 / red 2) | -- |
| 05:33 | L4 commit with `PRD_NOTIFY_TO=2.0.0_SA_COO~A` | @`25c66d3358` |

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | A.3 EXERCISE | forwarder RAN | after `provision-path-shims.sh` (106 x2) |
| comp-read `--enumerate` | `org/missions/DIRECTIVES.yaml` (D0 membership + placement); `org/projects/REGISTRY.md` (row line 21, 2 substring hits, WARN anchored-zero); `.owned-paths.yaml` (lanes, 47 hits, page 1 of 2 -- the tree rules read in full by Read afterwards); `.tools/prd-header-notify.py` (`RECIPIENT = os.environ.get("PRD_NOTIFY_TO", "2.0.0_SA_COO")` at :49); `.tools/to-pipeline-gate.py` (`_prd_conformance` :566, `check_prd_conformance` :631) | grain per carrier | the notifier's env knob is what routed the L4 handoff to the lane Andrew named -- no file edited |
| comp-surprise | `--project NFRA_CLDGRPH` | 0 items, files=20 | -- |
| to-check.py | `--all --assignee 1.0.0_SA_CTO~A`; `--all --project NFRA_CLDGRPH` | 0 / 0 (scanned 2,240, unresolved_serials=0) | captured to a file, never `head`ed |
| missions-tree-index.py | `check` x3, `derive --write` x2 | tree 1 -> 2 projects, 2 valid; 0 violations after each write | derive's internal check reported 1 (the INDEX-DRIFT it then wrote away); the standalone `check` after it read 0 |
| owned-paths-validate.py | `--check-agent` x3 (`~A`, base, worker) | permitted / permitted / REFUSED | the negative control is what makes the two permits a measurement |
| to-pipeline-gate.py limb 5 | `_prd_conformance` imported by path on the worktree PRD + schema + tree row | GREEN 0; RED (foreign directive) 1; RED (FWD-9 in header) 2 | the gate's own instrument on the exact bytes committed |
| prd-header-notify.py | `status` after the L4 commit | see the turn's read | -- |
| audit-archive-invoker.py | A.2 | rc 1, 5 findings, known classes | not chased per XXX.md |
| safe-commit -F | x3 (record, L3, L4) | rc 0 each; risk-reflex CLEAN; missions-tree-check 0 | commit-gate examines only .py/.sh/.tf/org/projects/*.json -- the JSON rows were its 1 of N each time |

**What worked:** measuring the limb from artifacts before touching anything; the lane check with controls before the commit;
running the gate's core on the bytes about to be committed. **What failed:** nothing at this seat. **Gaps found, not chased:**
(1) `check-inbox` is not in `provision-path-shims`' named subset (second session to hit it; called as `bash org/mcp/check-inbox.sh`);
(2) `TREE_PROJECT_ROW` lists the base serial only and the validator admits the `~A` lane by tilde-normalization -- correct
behaviour, but the lane text does not say so; (3) last night's one-process census pattern was case-sensitive and missed
`NFRA_CLDGRPH.json`'s "IN THE DIRECTIVE EXECUTION PIPELINE" phase text -- moot now, the flat row is retired into the tree row.

## Open, with owner

- `2.0.0_SA_COO~A`: L5 at `org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md` over s.7 (S1-S13; the flat
  decomp @05d2c89158 is the input), then L6 task orders + GOs. Ordering ruling in s.7: S10-S13 first; S8 LAST.
- `3.0.0_SA_CVO~A`: L8-L10 when rows exist; nothing before.
- Andrew: nothing pending from this seat. Pitchable items are the three gaps above (none blocks the run).
- This seat: holds at L4-done; re-enters only on an L10 `SCOPE_CHANGE` route or his word.

Loop arming: ZERO crons; the inbox Monitor only.
