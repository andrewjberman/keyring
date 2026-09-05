# 1.0.0_SA_CTO -- 2026-09-03 08:20-09:25Z -- the dry-run split, the R4-A class decision, cell_refs at the cut

Inputs (READ-acked): 2.0.0_SA_COO~A 93362 (dry-run friction, measured) + 3.0.0_SA_CVO~A 93368 (the conflation named);
2.0.0_SA_COO 93386 (water-test items closed; first CLOSED row); 3.0.0_SA_CVO~A 93394 (CLDGRPH round 1 stamped);
0.0.0_AB_MSTR 93407 (owner-sweep: 256 findings, class defect in R4-A, decision asked of CTO); 3.0.0_SA_CVO~A 93412 +
1.0.0_SA_CTO~A 93414/93419 (S5's class recurred: space-separated cell_refs; cut-time guard recommended, issuer endorsed).

## Acts
1. proof-of-spec-check @7e78fe9171: PRE-COMMIT splits on whether the INSTANCE is staged -- dry run: a never-committed
   artifact is a PENDING note; hook run: an unstaged artifact is refused; CCX (at HEAD, unstaged) refused in both.
   Four shapes exercised with git add / restore --staged on scratch files, index left clean; CVO~A re-ran it (93355).
2. R4-A class decision @d0737a5a8e: the owned closeout-drift finding RETIRED (unresolvable by any act -- lexical BEHIND on
   a row never touched again); the run lands one line in closeout-runs.log; 250 files resolved as a class with the
   attributed record RESOLVED_R4A_CLASS_20260903.md (198 tracked via the mass-deletion gate ATTRIBUTED, 52 untracked);
   README corrected; fast-path test 7/7; R4-B untouched.
3. S5's class @7b649df39d: proof-of-spec parses cell_refs on any delimiter; to-pipeline-gate resolves every owned cell
   and criterion token against the named decomposition at the CUT (index -> HEAD -> worktree; unreadable = note; flat
   root out of scope). All 13 committed tree faces resolve; 7 arms; batteries green (proof-of-spec 6/6, tree index
   34/34).
4. Broadcast to seven seats with the per-owner sweep table and the cut-time rule.

## Instruments
function-level probes with scratch files and a verified-clean index; the real CLDGRPH instance; comp-state on the
just-closed project (reads only [POST-CLOSE]); the mass-deletion gate's own verdict line; test-closeout-comp-state;
commit-gate x6; git ls-remote / rev-list.

## Open, with owner
- Register owners (COO, CRO, ~Z via MSTR~Z): if a deleted R4-A file named a REAL drift, re-open from the record.
- 2.0.0_SA_COO / ~A: the cut-time cell_refs limb fires on the next non-resolving face; fix at the face.
- Unchanged: ATOM_DECOMP steward items; MSTR's daemon restart on Andrew's word.
