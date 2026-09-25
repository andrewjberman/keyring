# Deploy Completion Record
**Date opened:** 2026-09-25T23:03:11.864295+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP rr-3: the redeploy -- opal-amgt-scoped-api carries rr-2's Model Cases rule
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= and LastUpdateStatus=Successful (AC1); prior artifact VersionId ujFHMNbjbg6Yv3wFotVvfDPnF4reNQdO read at build and recorded as the rollback |  | OPEN |
| L2 | verify | the served /print?format=rich body across the LIVE research library with the CASES axis | AC2 served over N of N folders: OK N, NOT_OK 0, CAPTURE_FAILED 0, cases over N of N compared names at missing=0 extra=0, exit=0 |  | OPEN |

## CLOSURE DIFF vs the deployed build input 9b7b146d9a -- limbs 2 and 3 graded BEFORE the build

Build commit: HEAD at the entry commit. Diff over lib/research: 7 files, 810 insertions, 30 deletions
(corpus/backlog.py, corpus/dossier.py, 2 corpus tests, print/render_pack.py, 2 print tests).

### LIMB 3 (the CTO's, carried forward from rq-2) -- CLEAR.
`git diff --stat 9b7b146d9a HEAD -- lib/research/api/scoped_amgt.py` is EMPTY: the file is untouched
entirely, so neither the `if fmt == "rich":` gate nor the `build_pack(display_form, block)` call can have
moved.

### LIMB 2 -- `build_pack` CHANGED? NO. And this time the usual control did NOT fire, so a second one was needed.
AST function-byte comparison, 30 defs at the deployed input and 31 at HEAD:
  build_pack       dep L242-359 sha 11d26e85b4e906e0 | HEAD L242-359 sha 11d26e85b4e906e0 -> IDENTICAL
  build_rich_text  dep L788-941 sha 7bfd5a48f275f152 | HEAD L812-965 sha 7bfd5a48f275f152 -> IDENTICAL
At rq-2, `build_rich_text` reading CHANGED was the control that proved the comparator could see movement.
HERE IT IS IDENTICAL TOO -- only line-SHIFTED (788-941 -> 812-965), which a byte comparison correctly
ignores. So that control is unavailable and an all-IDENTICAL read would otherwise be indistinguishable
from a blind comparator.
THE REPLACEMENT CONTROL, over the same instrument and the same pair of files: the comparator DOES report
movement elsewhere in render_pack.py -- `_model_case_line` ADDED (1) and `_model_cases_markdown` CHANGED
(1), 2 of 31 defs, with the whole-file sha moving 6706eb04ae5f66c4 -> 959c6dd8389a69bd. The instrument is
therefore demonstrably not blind on THIS diff, and build_pack's IDENTICAL is a measurement.
That the two moved functions are exactly the Model Cases pair is also the half's stated outcome landing
where it says it does: "the Model Cases section renders each case the Model tab renders".

Limb 1 (the shipping subtraction) requires the built package and is graded after `--build-only`, below,
before the apply.

## Log

- 20260925T230311Z OPENED by 0.7.0_AE_CloudOps~A with 2 leg(s)
