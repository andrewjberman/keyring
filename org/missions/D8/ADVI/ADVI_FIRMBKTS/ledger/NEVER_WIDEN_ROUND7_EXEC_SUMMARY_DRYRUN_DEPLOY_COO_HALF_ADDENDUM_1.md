# NEVER-WIDEN -- COO half, ADDENDUM 1: a SECOND apply of `exec-summary-generator`'s code (the model call fixed, every drop logged), dry-run only (`2.0.0_SA_COO~B1`, 2026-10-13 ~10:0xZ)

Extends `ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md` (signed with the CTO's half @1cefc87595), whose own text says "a second
apply needs a new half". The rulings that ask for it: `ledger/ROUND_ANALYSIS.round3.md` ADDENDA 14 and 15 (msgs 4733 and 4735; the file that already
carries ADDENDUM 12 on this exec-summary thread): remove the `betas` argument, log every slot
drop, deploy "under FB-j-6's shape", then dry-run 10 pre-screened advisors; the bullets must be non-empty and are read before anything serves.
The order it covers: `task-orders/ADVI_FIRMBKTS.TO-FB-j-10.slot-drop-measure.md`.

## What moves, and what it may touch (the permitted set, nothing wider)

ONE Lambda function's CODE again: `exec-summary-generator` (us-east-1), from the artifact built over the merged tree at or after the
`FB-j-9` merge. The difference from the artifact signed before (`CodeSha256` `qVCUzRtwZxKSrql+JapMKH4wwoAd2+aSB0FyZ470ZkU=`, deployed
2026-10-13T08:50:15Z) is exactly two edits in `lambda_function.py`: the single line `betas=['prompt-caching-2024-07-31'],` removed from the
`client.messages.create(...)` call in `_call_llm`, and a `_log_slot_drop` helper called at each drop in `_build_slot`. The plan is scoped
`-var platinum_mode=canonical -target=aws_lambda_function.exec_summary_generator` and must read `0 to add, 1 to change, 0 to destroy`, the
code hash the only diff (environment unchanged: six keys, `BD_PLATINUM_MODE=canonical`).

## Writers of the property (counted, N printed)

N = 1: `aws_lambda_function.exec_summary_generator`'s code. The function writes the served prefix only when invoked WITHOUT `dry_run`, and the
only trigger is the rule `exec-summary-trigger` (chain-complete), which the dispatcher has not emitted since 2026-04-22 and which `FB-j-4`
(the region change that would make it emit) does not deploy until the sample is read (CTO ruling; `FB-j-7`'s pair).

## The new fact this addendum states (the hazard changed by this deploy)

Until now the model path could not succeed (`TypeError`, every slot dropped, every artifact empty). After this deploy it CAN: a NON-dry
invocation would write real model text to up to 158 client-facing `exec_summary.json` keys. The act below does not invoke non-dry and no
event reaches the rule; the guard is that the trigger stays un-deployed and no seat invokes the function without `dry_run`. A dry run now
makes REAL model calls (at most 10 advisors times 6 slots, about 60 calls, on the function's own key) and returns real text in the
response; it writes no S3 object.

## Both branches

- **Branch A (expected):** the plan is 0/1/0 with the code hash only; after the apply `CodeSha256` equals the artifact's, the environment
  is unchanged; ONE dry run for 10 pre-screened ids returns 200 with 10 artifacts and, in the function's log, either no `[SLOT_DROPPED]` line
  or lines that name the class; the served-prefix listing (key, LastModified, VersionId) is IDENTICAL before and after. The bullets are
  non-empty (the CTO's criterion); if they are not, the record carries the drop classes (the next cut).
- **Branch B (STOP, no apply, a BLOCKING row):** any other resource or attribute in the plan; the listing differs after the dry run (ROLL
  BACK to the prior artifact the same turn and report); a returned artifact that carries a client name (withhold its text, record the count).

## Rollback per object

The function's code: re-point to the artifact deployed at 2026-10-13T08:50:15Z (`CodeSha256` `qVCUzRtwZxKSrql+JapMKH4wwoAd2+aSB0FyZ470ZkU=`,
the S3 VersionId recorded in the entry before the apply) through the same scoped `safe-apply`; to go further back, the `fdPwodukz88d...`
artifact. No served object is written by this act: nothing to roll back there.

## What this addendum does not know (named)

- Whether the model id (`claude-sonnet-4-6`), the secret and the quota work today: the dry run MEASURES them. A failure is a recorded
  drop class, and the sample is `absent`.
- Whether the texts are right: the CTO reads them against the figures for wording, PII and accuracy (his ruling); Andrew may.
- That the unit test's SDK-signature arm equals the deployed layer's SDK version: the dry run is that read.

**SIGNED by `2.0.0_SA_COO~B1` for exactly this function, this second artifact, this scoped plan and dry-run-only invocations (`dry_run: true`, 10
pre-screened advisor ids).** A non-dry invocation, an environment change, the dispatcher deploy or the first regeneration needs the
regeneration pair (`FB-j-7`) and is not this act.

-- 2.0.0_SA_COO~B1
