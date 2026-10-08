# Deploy Completion Record
**Date opened:** 2026-09-04T13:18:45.426074+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T132928Z
**Deploy:** Andrew-direct 2026-09-04 ~13:00Z /open-calls CALL 2 ("Approved for all of these"): the tplus1 models notebook SUMS duplicate (date,ticker) rows instead of failing the pivot. SITE-Z SCHEDULED TASKS RUN THE WORKING TREE, so this edit IS a deploy at the instant it touches disk -- OPAL_BBGTML_daily_pull fires scheduled_daily_pull.cmd whose RUNNER is tplus1. Ruling basis MEASURED on the RAW sheet pre-normalization, not on the loader's normalized output: 2026-08-18 sums to EXACTLY 1.0 with both duplicate pairs present, and all 25 dates in the sheet sum to exactly 1.0 raw with 0 exceptions -- so an accidental duplicate would have pushed the raw total ABOVE 1.0. These are intentional split lots
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the notebook edit committed under 1.0.0_SA_CTO~Z | commit hash | Committed cd6dddab6f under 1.0.0_SA_CTO~Z via safe-commit -F. 1 file changed, 11 insertions(+), 1 deletion(-) -- surgical, and NOT a whole-file CRLF rewrite: the file is CRLF and the writer detected and preserved it (io.open newline=''). | CLOSED 20260904T132928Z |
| L2 | verify | the pivot succeeds on all 5 models with every date summing to exactly 1.0, and the 4 non-duplicate models are ROW-COUNT UNCHANGED (the fix is a no-op where there are no duplicates) | test output with a reproduced-failure control and a drop_duplicates negative control | VERIFIED ON THE EDITED ARTIFACT, not a reimplementation: the function cell was extracted from the notebook ON DISK, compiled, and executed against all five REAL templates -- UST/ST/INT/LT/ULT all return (lens 12/23/25/28/23). REPRODUCED-FAILURE CONTROL taken BEFORE the fix: INT raised the production 'ValueError: Index contains duplicate entries, cannot reshape' while the other four passed, so the battery is not trivially red. NEGATIVE CONTROL on the REJECTED remedy: drop_duplicates leaves 2026-08-18 at 0.9575, so the two remedies are distinguishable and the test is not vacuous. ROW COUNTS: INT 399->397 (exactly the two merged pairs); UST/ST/LT/ULT UNCHANGED, so the fix is a no-op where no duplicates exist. Per-date weight sums after the fix: min 1.0000000000 max 1.0000000000 on every model. | CLOSED 20260904T132928Z |

## Log

- 20260904T131845Z OPENED by 1.0.0_SA_CTO~Z with 2 leg(s)
- 20260904T132928Z LEG L1 closed: Committed cd6dddab6f under 1.0.0_SA_CTO~Z via safe-commit -F. 1 file changed, 11 insertions(+), 1 deletion(-) -- surgica
- 20260904T132928Z LEG L2 closed: VERIFIED ON THE EDITED ARTIFACT, not a reimplementation: the function cell was extracted from the notebook ON DISK, comp
- 20260904T132928Z CLOSED -- all 2 legs proven
