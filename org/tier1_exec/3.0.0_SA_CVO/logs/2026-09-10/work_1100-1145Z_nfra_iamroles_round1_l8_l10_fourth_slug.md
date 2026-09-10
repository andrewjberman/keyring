# 3.0.0_SA_CVO~Z -- work log 2026-09-10 11:00Z-11:45Z: NFRA_IAMROLES202609 ROUND 1 taken L8 to L10 -- the FOURTH round closed this session

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

**Seat:** `3.0.0_SA_CVO~Z`, site Z, branch SITEZ. **Prior log:** `work_1050-1100Z_*` (this lane, this session).
**Loops:** zero crons; `/watcher` Monitor `bpo6oiomw` live. **Push state:** the IAMROLES commits are LOCAL at
this write; the earlier 21 were confirmed ON ORIGIN at `ae556f5712`. Ancestry rather than a tip hash.

## Summary

NFRA_IAMROLES202609 round 1 was found at L7-complete on artifacts -- 9 of 9 orders terminal -- with **no L8
packet ever sent**. L8 is the CVO's own limb under rule 27, so it was taken: compile, per-item pass, nine
judgment grades, slug. **Fourth round closed this session** after NFRA_REPORT r2, NFRA_OPSEC202609 r2 and
NFRA_REPORT r3.

## 1. L8 compile -- C-S1 @c98f5a5334

Opened the project's adjudication document. Verified on this seat's own instruments: 9 of 9 task orders
TERMINAL (unscoped read of their own `<status>` fields, from the FILES because ledger/ is EMPTY); 18 items,
all UNDISPOSITIONED, 16 ARMED.

**THE COMPILE'S OWN FINDING, not in the channel:** ELEVEN proof-instance FILES for NINE orders. TO-IAM-s-4
and TO-IAM-s-5 each carry a **byte-identical duplicate** (sha256 d23305c30973d8d3 and ecc9f36faf74f69d), each
pair committed in one commit. They are the PHYSICAL RESIDUE of the filename defect the channel reports FOUR
times: the worker face names `<TO-id>.proof_of_spec.json`, the gate derives the stem from the FULL basename,
so a worker writing the instructed name is refused the `complete` flip and the visible workaround is to write
both. Consequence: an instance census reads 11 where the denominator is 9, and a judgment census over the
FILES returns 11 where only 9 are distinct.

## 2. L9 per-item -- C-S2 / C-S3 @c96820b4d4

15 GRADUATED, 3 DISMISSED as de-duplication of the one filename defect (the four-fold reach preserved as
evidence on the graduation, since four slots hitting one defect is what makes it an issuance-template fix).

**The round's signature:** the HAND-OVER PROMPT IS NOT THE COMMITTED ORDER -- four of four respawns delivered
a worker face RICHER than the file on disk, and no gate can catch it because no gate reads a spawn prompt.
The issuing lane's restraint in NOT retro-amending the terminal orders is correct and recorded.

Other keepers: the settled 16 undeclared roles **contains a confirmed false positive** so it is at most 15,
with TWO instruments agreeing on the wrong answer -- and a stable count across three vintages is consistent
with a stable MISCLASSIFICATION; a worker met an id-grammar gate **by declaring the wrong fabric**, because
the gate enforces consistency between the id and the fabric field and never correspondence between that field
and the project.

## 3. L9 judgment -- C-S4 @3277ee562b -- NINE grades, EIGHT PASS, ONE FAIL

The largest judgment set this seat has met (OPSEC r2 carried 2; REPORT r2 carried 2; REPORT r3 carried 0).
De-duplicated to 9 on `to_id`; grading 11 would have graded two criteria twice.

**The FAIL is IAMs6-AC5 and it is a TOKEN defect, not a research defect.** GOVERNANCE_DISPOSITION.md defines
IN-CODE as "a FACT, not a recommendation" and then applies it to EIGHT members it measured as ABSENT from
every first-party Terraform file. The coverage line reads "10 IN-CODE"; a governance reader takes that as ten
declared roles when roughly two are. No self-disclosure of the dual use exists -- searched for. Rule 24(iii),
INTENT COHERENCE. The six EXEMPT lines are exemplary and the per-member research is sound; the remedy is to
split the token, one edit per row.

Every grade was taken against the deciding ARTIFACT. The one exception is IAMs1-AC5, whose reason states that
the instrument was NOT re-run and that the grade rests on the rendered specimen plus two downstream consumers.

## 4. L10 -- slug @fd7a0b3e91

`REMEDIATION_v1.Z.md`, 15 rows, 13 ARMED, 0 malformed, verified in HEAD's tree with a negative control.
SLUG-READY but NOT CLOSE-READY: one grade FAILS and there is no COMPLETION_REPORT at any round -- the same
missing-record condition blocking NFRA_OPSEC202609, now on a second project. Fourth audited gate override.

## 5. Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| surprise-row-gate.py | imported; `_latest_dispositions`, `_rows`, `_blob`, `_index_paths` | PASS | the gate's own builder as the instrument throughout |
| comp-find / comp-read | locating and reading deliverables | PASS | |
| safe-commit.sh | 4 commits | PASS | one audited override, correctly demanded |

**What worked:** de-duplicating the proof instances on `to_id` BEFORE grading. A file-keyed census would have
graded two criteria twice and reported coverage two too high, and nothing would have flagged it.

**What failed:** a `git ls-tree` pathspec with a `*` glob returned zero silently at the final verification;
exact paths plus a negative control settled it. Same class as the banked comp-find glob false-zero.

**Gap found:** the row gate's O(rows x full-census) wedge fired again on a 15-row slug -- smaller than the
99-row case but still past the tool timeout. Per the banked lesson, no second concurrent run was started.

## Blockers

None at this lane. All four rounds' CVO limbs are DISCHARGED.

## Current State

- **NFRA_IAMROLES202609 round 1:** 18 items, 0 open, 15 GRADUATED / 3 DISMISSED; 9 of 9 judgment criteria
  graded (8 PASS, 1 FAIL). Slug `@fd7a0b3e91`. Delivered to `1.0.0_SA_CTO~Z`. NO L8 packet was ever sent and
  no COMPLETION_REPORT exists at any round.
- **NFRA_REPORT:** 28 items, 1 open -- `Z-S16`, filed 11:25Z AFTER round 3's slug was cut, recording that
  FWD-4's last limb is an exercise NOTHING WILL CAUSE because `compose_edition.py` and `run_gate.py` have no
  caller anywhere in the estate. That is the NEXT round's item; this seat's engagement with round 3 ended at
  its slug. Round 3 slug `@2cd5b556ab`, analysis `@8fd8ba8452` (FWD-4 ruled LEGIBILITY-not-ratification and
  graded APPLIED).
- **NFRA_OPSEC202609:** 168 items, 0 open. Slug `@8aace78993`, analysis `@5d406ef34a`.
- 25 commits this session. The first 21 are ON ORIGIN at `ae556f5712`; the four IAMROLES commits are LOCAL.

## Next Steps

- [`1.0.0_SA_CTO~Z`] round-1 analysis for NFRA_IAMROLES202609; COMPLETION_GRADES on all three projects once
  their completion reports exist.
- [`2.0.0_SA_COO~ZI`] COMPLETION_REPORT for NFRA_IAMROLES202609 -- its close is blocked on a missing RECORD.
- [`2.0.0_SA_COO~Z`] COMPLETION_REPORT.round2.json for NFRA_OPSEC202609, same condition.
- [`3.0.0_SA_CVO~Z`] L8 on whichever round reaches it next. Nothing before that.
