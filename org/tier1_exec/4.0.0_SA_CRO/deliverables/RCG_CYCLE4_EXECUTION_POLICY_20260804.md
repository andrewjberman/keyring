# RCG Cycle-4 Execution Policy (addendum to the cycle-3 protocol)

**Author:** 4.0.0_SA_CRO. **Reviewer:** 1.0.0_SA_CTO~B (cycle-3 protocol). **Ratifier:** Andrew.
**Ordered:** Andrew-direct 2026-08-04 (~2040Z, CRO terminal): cycle 4 enters higher-risk segments;
policy must be "locked down and rollback-able," and the program stays in the knowledge plane (git) --
the execution plane is NFRA_VELOCITY's matter, not RCG's.
**Status:** DRAFT -> CTO~B review -> Andrew ratification. No cycle-4 disposition executes before
ratification.

## 1. Scope lock -- knowledge_space only

- RCG is the codebase estate in the knowledge_space, solely and entirely (grader charter; R-0008,
  R-0012). Cycle 4 executes **git operations only**: `git rm` (ARCHIVE), `git mv` + citation repair
  (MIGRATE), label/ledger appends.
- **Execution-plane routing rule (predicate, not gate-catch):** any file whose disposition is
  deploy-coupled -- deleting or moving it changes the next deployed artifact of a live system
  (Lambda bundle contents, TF-referenced paths, EC2-pulled code) -- is EXCLUDED from RCG execution
  at derive time and routed to the owning lane as a prepared handoff. Cycles 1-3 caught this class
  at the lane gates three times; cycle 4 excludes it before the batch is cut.
- Step 1b (AWS-plane debt pass) stays QUEUED and is NFRA_VELOCITY-adjacent territory. It does not
  ride cycle 4 under any framing.

## 2. Ratify-before-execute (unchanged) + tightened batch mechanics

- Every batch: RATIFIED (recorded, sha256 manifest over the exact file set) -> EXECUTED -> close
  row. Append-only ledgers. `rcg-sweep-check` PERMIT + owned-paths lane gates unchanged.
- **Batch cap drops 500 -> 100, single-cohort batches.** One revert restores one coherent decision.
- **No model-only execution.** Auto-eligibility requires HIGH confidence (>=3 independent feature
  families, none contradicting) AND a ruled cohort verdict covering the file. Everything in the v6
  uncertainty band (172 files @ 465f15ce) requires the Andrew sitting.

## 3. Label-vs-warrant validation (NEW -- the control this cycle's defect demands)

For any ledger row citing ruling R over cohort C: **assert label == R's ratified verdict for C**
before the row lands or trains. Contradictions ESCALATE, never land. Descent verification alone
("does this row descend from Andrew's ruling?") passes exactly the defect below, at whatever weight
the reviewer just blessed. Mechanical check: `rcg/bin/manifest_check.py` gains a label-vs-warrant
pass over LABELS.jsonl at commit time (build item, this cycle, before batch 1).

**Type specimen (2026-08-04, both seats on record):** the R-0022 precedence correction wrote a
constant MIGRATE/ARCHIVE_CANDIDATE on all 4,110 rows; 4,103 cited "R-0019 layers/ KEEP supremacy"
as their own warrant while carrying the archive-side label. CRO authored the constant; CTO~B's
145728Z weight review had the inversion on screen ("all MIGRATE, top prefix layers/") and verified
descent but not label-vs-warrant, then set weight 5.0 on the restoration premise -- amplifying the
wrong side at max weight. Found by CRO deriving the MIGRATE population against R-0019; repaired
append-only @32d835195 (4,103 KEEP rows; MIGRATE 5,717 -> 1,614; layers/ non-KEEP = 0); CTO~B
re-derived clean from the ledger independently. v5 41e47353 retired; v6 465f15ce is the cycle-4
basis. Zero repo damage -- caught pre-execution, which is what this policy is for.

## 4. Rollback -- exercised, not asserted

- Every deletion/move is a git commit on CLOUD; **rollback = `git revert <batch-commit>`**, total
  and atomic. MIGRATE units land as atomic move+citation-repair commits, revertible as single units.
- **Drill EXERCISED 2026-08-04 (pre-policy, per the accepted-on-observed-green-run law):** scratch
  worktree, `git revert 1d920662f` (batch B-0008, 24 files), restored set verified byte-identical
  (`git diff 1d920662f^ HEAD -- <paths>` empty), worktree+branch torn down. The rollback path is a
  run control, not posture.
- Ledger repairs are append-only rows (R-0022 semantics) -- the correction history is itself
  revert-proof and self-documenting.

## 5. Vintage + eval discipline

- Cycle-4 scoring basis: post-sweep vintage 20260804T174531Z_f919615b, model v6 465f15ce (repaired
  ledger). No verdict cites the retired v5 band.
- E-0005 stays prospective under CVO~B sealed blinds; adjudications land before the eval is read.
