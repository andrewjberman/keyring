# POSN_ASTTAX round 5: L5 decomposition, four never-widen halves, ONE issuance of nine orders, five workers spawned -- 2.0.0_SA_COO~Z

**archetype:** COORDINATE

**Date:** 2026-09-14 (17:3xZ-18:5xZ)
**Task Order:** none held by this seat; L5/L6/L7 owner of POSN_ASTTAX round 5.
**Status:** L7 OPEN. Five worker subagents live on slots ~19..~23; the COO drains as each reports.

---

## Objective

Continue from the 17:05-17:3xZ log: decompose round 5 from the aligned breakdown, land the never-widen halves, cut the ONE
issuance once every precondition read at HEAD, and open L7.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-schedule | `--drift` | RUN | 2 armed gates, neither POSN; 7 open deploy ledgers; 12 NEVER clauses -- the decomposition's battery row |
| comp-iam | `service cot-satellites-registry-producer`; `service yang-generate-positioning` | RUN | "No AWS operations detected" on the trigger (the producer is vendored by pin -- BLIND BY CONSTRUCTION, stated); 7 calls / 13 statements, 6 UNRESOLVABLE on the generator |
| comp-adversary | `compose <decomposition>` | RUN | 5 sources / 4 declared exclusions; every pin READ-VINTAGE; appended as s.8 |
| comp-routes | `behaviors` (full output to a file, counted in python) | PASS | 29 behaviors, 39 edge associations, shared-advisor-router origin-request on FIVE (2, 3, 4, 16, 27) -- the B5 radius, agreeing with the CTO half's .tf read |
| comp-read | `--enumerate` on the edge router, ds-precommit-check, the two generators, build_package, the seeder, satelliteAdapter, satelliteRegistry, the round-3 decomp; `--for` on the spine, the gate, the frontend-dev skill | PASS | the edge router's ONE-LEAF refusal at `index.mjs:340-357` is what surfaced B5; the seeder's MERGE SUMMARY templates re-phrased V8-AC8 |
| comp-find | writers of positioning_data.json / holdings_attribution_data.json over `infra data integrations --band SURFACED`; `<placeholders>` precedents; the two generators' Terraform | PASS | the four-writer census for the B1 half; the FE-s-28 order as the placeholders precedent |
| to-pipeline-gate (via safe-commit) | the issuance, twice | rc=1 then rc=0 | first attempt REFUSED on the mandatory `<placeholders>` element (9 of 9), V8-AC8's output vocabulary, V2's comp-iam line; all fixed; second attempt 0 refused |
| missions-tree-index | `derive --write`; `check` | PASS | wrote 0 (the flat index carries no phase); 0 violations |
| safe-commit | x6 (a019666262, 0456cf5b84, 9e6e72ea8b, f381f6f402, 6c7e292c93, 945d1ddd95, 2a882703db) | PASS | all LOCAL |
| aws (shim) | dynamodb scan (filtered, 12 of 285); s3api head-object x10; lambda get-function-configuration x3; stepfunctions list/describe | PASS | the halves' live figures; the R1 prior-values table; the artifact bucket VersionIds (rollback) |
| git (portal) | ls-tree at the pin; show per file; merge-base both ways; for-each-ref refs/drains; worktree add (linked) | PASS | 14 Positioning files; checkout AT the pin; the F-chain slot's portal worktree at e85f6eb84f |

**What worked:** reading the F3 read path at the bytes before cutting it. `satelliteRegistry.ts` exports one endpoint and the edge
router refuses every leaf but `registry.json` by design -- so B2's and B4's artifacts were unreachable by the page under the
aligned eight cells. That is the class of defect the cut exists to catch, it went to the CTO and then to Andrew as a deviation,
and it became AT5-s-9 with its own pair of halves rather than a worker's workaround.

**What failed (mine):** (1) the raw `aws cloudfront get-distribution-config` was rail-denied and I had reached for it first;
`comp-routes behaviors` was the instrument and it counted the same five on a different plane-read than the CTO's. (2) My
prose-placeholder-to-token conversion cut a NESTED placeholder short in V3-AC5, leaving an invocation no instance could match;
caught by re-reading the committed face before the spawn, amended @2a882703db before ~21 was handed the order. (3) The B5 COO half
carried one non-ASCII glyph; the ASCII gate binds messages, not .md, so it landed -- fixed in the issuance commit. (4) The first
issuance attempt was refused on three limbs I had not read for: the gate's refusal text taught each one and the second attempt
passed clean.

**Gap found:** the ad-hoc Bloomberg pull Andrew approved at ~18:2xZ moved V4's premise (GLD/VXX now PRESENT in the 09-11
partition) between the cut and the hand-over. Amended before the order was handed; the amendment is the record.

---

## Work Completed

1. **L5** `decompositions/POSN_ASTTAX_DECOMP_round5.md` @`f381f6f402` (draft, B5 proposed) -> @`6c7e292c93` (nine cells aligned,
   B5 approved by Andrew ~18:1xZ). Rectangle over S1/S2/S3; edges keyed to observed completion; five chains, four waves, max
   concurrency 5; the portal chain F1->F2->F3 serial on one slot and one drain ref; battery per lens; Rule 24 record; s.8 adversary.
2. **Never-widen halves (the COO's):** `ledger/NEVER_WIDEN_ROUND5_COO_HALF.md` (B1 two keys, the FOUR-writer property census,
   B2 registry + new holdings.json, R1 12 of 285 rows with the prior-values table, B4 non-application) @`f381f6f402`, matched to
   the CTO half @`af667548d1` on the four B1 commits (incl. non-POSN `b0e1f33471`) and the Branch A/B pre-apply delta rule;
   `ledger/NEVER_WIDEN_ROUND5_B5_COO_HALF.md` (radius FIVE behaviors, bounded) @`6c7e292c93` beside the CTO's @`f5a744f412`.
3. **L6** ONE ISSUANCE @`945d1ddd95`: TO-V1-1..TO-V9-1, `fanout: 5 of 5 chains, cap 8`; project.json phase ROUND 5 ISSUED.
   Amend @`2a882703db` (V3-AC5 invocation; V4 premise).
4. **L7** worktrees `/c/tmp/wk-posn-5-19..23` (sparse cones from 945d1ddd95; ~21 fast-forwarded to 2a882703db; ~22 carries a
   linked portal worktree on `wk-posn-5-22-portal` at `e85f6eb84f`). Workers spawned as the harness's worker subagent type:
   ~19 V1 (B1), ~20 V2 (B2), ~21 V3 (B3), ~22 V5 (F1), ~23 V9 (B5). Wave 2 (V4 on ~20, V6 on ~22), wave 3 (V7 on ~22), R1 (V8 on
   ~19) are handed at drain; ~20's and ~22's branches get SITEZ merged in at hand-over so the amended/newer faces are in their tree.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| B5 as a tenth cell (rec a), not folded into registry.json (b) | two functions on one key is the measured NEVER#1 two-writer hazard; registry.json's reader binds its contract; the CTO ruled the same at L4 and Andrew approved |
| The portal chain serial on one slot | F2 and F3 both touch the PositioningAllocation consumers; one submodule HEAD; one drain ref -- parallel clones onto one ref is the append-only-shared-file inversion in git |
| Linked portal worktree, not a clone | shares the object store; the AMGT precedent used clones; a linked worktree is cheaper and its branch is visible in `git -C portal worktree list` |
| Tokens for every prose placeholder | the gate's mandate; a worker's instance is compared to the FILE's invocation modulo the declared tokens |
| Amend V3/V4 BEFORE the hand-over rather than correct in the spawn prompt | the S31 class the placeholders limb exists to catch: a correction in the prompt and not the file |

---

## Files Modified (all LOCAL)

| File | Change | Commit |
|------|--------|--------|
| decompositions/POSN_ASTTAX_DECOMP_round5.md | NEW; B5 approved | f381f6f402, 6c7e292c93 |
| ledger/NEVER_WIDEN_ROUND5_COO_HALF.md, NEVER_WIDEN_ROUND5_B5_COO_HALF.md | NEW | f381f6f402, 6c7e292c93, 945d1ddd95 |
| task-orders/POSN_ASTTAX.TO-V1-1..TO-V9-1 | NEW (nine); V3/V4 amended | 945d1ddd95, 2a882703db |
| project.json | phase ROUND 5 ISSUED | 945d1ddd95 |
| this log | NEW | this commit |

---

## Blockers

None at this seat. Observed: every commit LOCAL (0.0.0_AB_MSTR~Z carries on Andrew's word); the organic next-day fires (B2 07:00Z,
B4 07:20Z, the yang pipeline 11:0xZ) are ledger legs the COO records tomorrow, not waits; the worktree cleanup of rounds 2-4
(13 dirs) waits on L9.

---

## Current State

POSN_ASTTAX: 28 orders (15 complete, 2 superseded, 2 cancelled, 9 staged -> pending as each worker flips). Round 5 L7 open on
five slots. PRD v0.7 @99cc431075 ADMITTED. Monitor bnot9mzwj live; 20 of 20 messages READ-acked; zero crons.

---

## Next Steps

1. **[this seat]** drain each worker as it reports: verify its instance with the WORKTREE's checker (memory: the checker grades
   the tree the script lives in), merge its branch via `.tools/safe-merge.sh`, drain portal branches onto `refs/drains/posn-5-portal`
   and record the hash in `ledger/PORTAL_REFS.md`; hand wave-2/3 orders with the dependency hashes; R1 last.
2. **[3.0.0_SA_CVO~Z]** L8 on the first drained instance.
3. **[0.0.0_AB_MSTR~Z]** carry 6c7e292c93, 945d1ddd95, 2a882703db and this log.
