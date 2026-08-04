# RCG execution night: B-0001 end-to-end + CVO~B clean close + B-0002 at cap 500 -- 593 files deleted under full gating

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Agent:** 4.0.0_SA_CRO (Chief Research Officer, Tier-1)
**Window:** 2026-08-04 ~01:12Z (prior log close) -> ~03:50Z
**Prior log:** logs/2026-08-03/rcg_standup_p0_to_execution_gating_full_arc.md

---

## Summary

The execution phase went from green-light to 593 files actually deleted, with every leg
gate-verified, one independent CVO verify, and five more instrument defects caught live (two
mine, three in the gate/tooling chain). Andrew reviewed the deletion analysis at close:
"Nope that is all fine by me."

## The chain (all shas in rcg/ledger/BATCHES.jsonl; audit trail org/rcg-sweep-audit.log)

**B-0001 (93 declared-archive client_detail files):**
- CTO~B green-light after their revert-mode build @f189e0c6f1 (last-row-wins fix -- my C3
  finding: load_batch was FIRST-row-wins on an append-only ledger, making executed_commit
  structurally unreadable; their fixture had mutated rows in place, violating the contract
  under test).
- RATIFIED @e0ab95986d (complete-row law learned: status transitions re-carry the whole record).
- Execute 099eb31879 (93 files / 25,243 lines; sweep PERMIT 020727Z; mass-deletion ATTRIBUTED
  after trailer fixed to the ledger-file form -- LD-####-or-existing-file grammar).
- Revert 48db734d1b: revert-mode PERMIT (93/93 blobs hash-identical to parent 67bbb6981d18),
  independently diff-verified empty. THE RECOVERY PATH IS NOW A FACT.
- Re-apply d1c3980c4a after re-ratification @fec27f05e9 (C3 correctly denied re-apply on
  status=EXECUTED; fresh complete RATIFIED row is the documented protocol per CTO~B ruling).
- My wrong-sha row @7ab6fc0348 (shell var captured un-moved HEAD after a denied commit) +
  cap-500 overstatement -- both superseded by append-only corrections; CTO~B accepted the
  chain @86c4b5569d with the correction that 500 was AUTHORIZED-ON-CLOSE, not in force.

**CVO~B independent verify (Andrew-provisioned seat, Andrew-ferried per D-0005):**
CLEAN 26/26 @c11c4b61fb -- everything re-derived from commits+ledgers, incl. chasing the
orphan 020520Z PERMIT down org/mass-deletion-audit.log and proving no commit landed by a
3-commit author census. Cap 500 discharged (s.7.2 item 3), discharge row ledgered.

**B-0002 (500 declared-archive files, 84 directory-complete dirs):**
- RATIFIED (sha256 92799233f214e438) + executed @632c0230f9 (500 files / 202,085 lines;
  PERMIT 033146Z at cap=500; ATTRIBUTED 033155Z). EXECUTED row committed.
- Three DENIED attempts first, each a real lesson: (a) safe-commit lock contention with a
  live peer (timeout 143; waited, never deleted index.lock -- it was a live holder); (b+c)
  THE XARGS SPLIT: piping 500 paths through xargs invoked git commit TWICE with partial
  pathspecs, each C2-denied as batch-tree divergence (exact 375/125 arithmetic; two wrong
  theories chased first). STANDARD FORM RULED: git commit --only --pathspec-from-file=<file>
  for batches >~100 paths. Also: a peer's wrapper reset dropped 124 staged deletions once
  (re-staged); the hook cap is env-set by the operator once earned (RCG_SWEEP_CAP=500).
- Discriminating test (CTO~B's confound): with planted + foreign staged content, BOTH commit
  forms passed C1 -- safe-commit EXONERATED, my full-index causal claim retracted, 014714Z
  mechanism recorded UNDETERMINED. Symptom banked, false mechanism not.

## What was deleted (Andrew-reviewed and approved)

593 files / 227,328 lines, 100% from directories explicitly named archive/:
- data/black_diamond/archive/* (428 files, ~110k lines, ~161d untouched): the Jan-Feb BD/49F
  pipeline generation -- 293 per-client gold snapshots, fargate/EC2 experiments, superseded
  TS downloaders, era process docs.
- docs/architecture/archive/* (125 files, ~90k lines, ~151d): the PRE-SERIAL documentation era
  (role-name task orders: AWS_ENGINEER etc.) -- Causality Engine, Trade Submission v1+v2,
  Portfolio Management/Persistence, Market Update suites.
- infra/aws/archive/* (40 files, ~16k lines): the set Andrew already authorized archiving
  2026-07-09 @a749324e7b; RCG completed the deletion leg.
Recovery: git show 099eb31879^:<path> / 632c0230f9^:<path>; explicit manifests in BATCHES.jsonl.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| rcg-sweep-check (CTO~B's, exercised by me live) | every batch commit | 6 DENYs all correct + 4 PERMITs; the gate composed with mass-deletion-check (independent layers) |
| rcg/bin/manifest_check.py | folder conformance after every ledger commit | CLEAN throughout |
| safe-commit chain (surface-check, risk-reflex, commit-gate) | all ledger commits | PASS; one classifier denial rerouted to smaller steps |
| git primitives as instruments (diff --numstat, cat-file, author census) | deletion analysis + state discrimination | the whole B-0002 diagnosis + the what-was-deleted analysis |

**What worked:** the gates composed (sweep PERMIT + mass-deletion BLOCK on the same commit,
independently); waiting on index.lock instead of deleting it; the discriminating test before
banking a mechanism. **What failed and is owned:** my wrong-sha ledger row; my cap
overstatement; the xargs form (3 denials before diagnosis). **Gap:** the C2 deny message
cannot distinguish batch-tree divergence from partial-invocation -- suggested to CTO~B that
it hint at pathspec splitting; also suggested s.5.1 name --pathspec-from-file as standard.

## MCP traffic

~9 significant sends/receives, all RAVC-closed: CTO~B (green-light, C3 blocker report,
last-row-wins fix, B-0001 acceptance + cap correction, B-0002 report + xargs finding);
CVO~B (verify commission via Andrew ferry, CLEAN verdict); base CTO (tombstone discriminator
armed post-mint, ACKed). Broker re-surfaces of handled messages: not counted.

## Blockers

**None.** Queue: 2,351 ARCHIVE files remain (declared-archive class swept but 116 tail;
next coherent mass = org/threads/ snapshot copies ~1,100). CTO~B owes the 12 BASE_EXEC/POD2
stragglers under ordinary attribution. Non-blocking Andrew ferries: CLAUDE.md taxonomy law
(base CTO), SYSTEM_DEFINITIONS staged entries (CVO canon).

## Current State (zero-context handoff)

- Ledgers: rcg/ledger/BATCHES.jsonl (B-0001 REVERT_EXERCISED + cap corrections; B-0002
  EXECUTED @632c0230f9), LABELS.jsonl (21,624 rows / 17,512 paths, last-row-wins per R-0022),
  MODEL_EVAL.jsonl (E-0001/E-0002), RULINGS.jsonl (R-0001..R-0023 verbatim). All committed,
  manifest-conformant, append-only intact.
- Disposition map at HEAD: ARCHIVE 2,351 remaining / MIGRATE 5,715 / KEEP 4,798 /
  REFERENCE_KEEP 4,054 / CONTESTED 306.
- Gates live: rcg manifest gate (pre-commit stage 5), rcg-sweep-check (stage 6, cap env-set,
  currently earned 500), both fail-closed. Sweep identity 4.0.0_SA_CRO~SWEEP has exactly 5
  commits in existence (B-0001 chain x3 + B-0002 x1 + none stray -- census-verifiable).
- Model v2 (17,530 labels, band 313); retrain owed at cycle 3 with the R-0022/23 corrections.

## Next Steps

- **[4.0.0_SA_CRO]** Batch 3: org/threads/ snapshot-copy mass, directory-complete under cap
  500; then the general-tree ARCHIVE tail. Cycle 3: CONTESTED 306 + retrain.
- **[1.0.0_SA_CTO~B]** 12 stragglers (ordinary attribution); optional s.5.1/C2-message
  amendments from the xargs finding.
- **[Andrew]** Non-blocking ferries above, whenever convenient. MIGRATE/layer-refactor spec
  and step-1b (AWS plane) queue behind the repo-side drain.
