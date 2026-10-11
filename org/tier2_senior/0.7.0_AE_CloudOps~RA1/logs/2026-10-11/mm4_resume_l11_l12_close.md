# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-mm-4: resumed at L11, ledger closed

**Date:** 2026-10-11 (22:1xZ session start 2026-10-10 US Eastern evening)
**Task Order:** AMGT_RESAPP.TO-AMGT-mm-4.redeploy-the-selector-refusal-and-filing-sentence-flag
**Status:** COMPLETE

## Objective

A prior session of this lane applied mm-4 at 22:55:03Z on 2026-10-09 and stopped after leg L10, leaving L11 (the
source-map record) and L12 (AC1-AC3) unrun and the ledger OPEN 27.7h against a 6h window. This session re-measured
before acting, finished the two legs, and closed the ledger. Nothing was re-deployed.

## The act
**archetype:** VALIDATE

Order of operations, each read before the next:

1. **Live function first** (COO msg 3304 asked for it, and CLAUDE.md NEVER-2 requires measuring the artifact before
   acting on an open entry): `get-function-configuration` reads CodeSha256 `KlosR/ap8O3..` (the mm-4 build),
   LastModified 2026-10-09T22:55:03Z, Active, Successful, Memory 1769 / python3.11 / Timeout 29. Unchanged for 27h.
2. **L11 was already landed.** `git log` on the source map found `4607adbfcd` (this lane, 2026-10-09 18:59:30 -0400,
   record-terraform-deploy.sh), an ancestor of origin `box/dell1` `cecf2a458c` with the reverse read as the control.
   The entry reads sha `KlosR..`, ledger `amgt-resapp-r88-mm4-scoped-api-dell1`, at 22:59:02Z. I closed L11 on that
   measurement and not on the ledger's silence.
3. **The one field that did not move is not a miss.** `last_deployed_commit` still reads `271e8f8b43` because it is the
   last commit touching the entry's `source_dir`, and that commit is `271e8f8b43` (2026-09-12). The build pin
   `4d006edc74` is not in the map; it is an ancestor of the record commit's `daaa6f76d8` with 0 changed closure
   members between them. Recorded as a forward note, not a defect of this order.
4. **L12.** AC2 and AC3 run live, exit=0. AC1 needs HEAD = the pin and the L7 build tree `c:/tmp/mm4-build` is gone,
   so I created a detached worktree `C:/tmp/mm4-ac1` at exactly `4d006edc74` (HEAD read back) and ran it there:
   K1, K2 PASS, deployed `scoped_amgt.py` sha256 `5b987a17468e59fc` == HEAD's, exit=0.
5. Proof instance generated from the ledger's own leg text (no leg retyped), `proof-of-spec-check` VALID rc=0, 12 of
   12 controls discriminate.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | close-leg L11, L12; close | PASS | refuses a close with an unproven leg |
| proof-of-spec-check.py | on the mm-4 instance | PASS | VALID rc=0, 12 of 12 controls |
| r88_package.py / r87_withheld.py / r84_listing.py | the three order criteria | PASS | exit=0 each |
| .tools/aws | get-function-configuration, s3api head-object | PASS | live re-read before any leg closed |
| comp-rail hook | a heredoc python `find()` helper | DENIED | read as a blind recursive search (F1); used native Grep/Read instead |

**What worked:** reading the live function and the record commit from git before closing a leg; generating the proof
from the ledger so the two cannot disagree.
**What failed:** the rail's F1 matcher denied an inline python helper named `find`, a false positive on a JSON walk of
one known file.
**Gap found:** none new.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Closed L11 on the existing commit, did not re-run record-terraform-deploy.sh | the record was already landed and pushed; a second run would write a second record for one deploy |
| Recreated a pin worktree for AC1 | AC1 compares the deployed member to HEAD of the tree it runs in; the grade is the same on any tree at the pin |
| Left `C:/tmp/mm4-ac1` in place | a recursive delete wants a human word under CLAUDE.md; `/cleanup` or `git worktree remove` clears it |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/.open_deploys/amgt-resapp-r88-mm4-scoped-api-dell1.json` | L5-L12 proofs, closed | see commit |
| `org/critical_paths/change_management/20261009T2241Z_amgt-resapp-r88-mm4-scoped-api-dell1_deploy_completion.md` | L5-L12 proofs, CLOSED | see commit |
| `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-mm-4...proof_of_spec.json` | new instance | see commit |
| this log | new | see commit |

## Open at close

- Worktree `C:/tmp/mm4-ac1` (detached, clean) is mine and can be removed.
- The ledger was OPEN 27.7h past its window before this session; the cause was the prior session stopping, not a
  failed leg.
