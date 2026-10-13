# NEVER-WIDEN -- COO half, ADDENDUM 2: a THIRD apply of `exec-summary-generator` (the slot switch ON for `top_nna_mover`, the client-name guard), dry-run only (`2.0.0_SA_COO~B1`, 2026-10-13 ~10:5xZ)

Extends the COO half and its addendum 1 (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md`, `..._ADDENDUM_1.md`), signed with the
CTO's half and addendum 3. The ruling that asks for it: `ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md` (the CTO read the ten-advisor
sample from the second apply): four slots read well, `top_nna_mover` is broken; (a) `top_nna_mover` DISABLED by config for the first regeneration,
(b) the PII guard learns client display names, (c) a -69.2 percent loss traced before serve (`FB-j-12`, read-only), then Andrew is offered the
sample before the trigger (`FB-j-4`). The order it covers: `task-orders/ADVI_FIRMBKTS.TO-FB-j-13.slot-switch-deploy-sample.md`.

## What moves, and what it may touch (the permitted set, nothing wider)

ONE Lambda function's CODE and exactly ONE environment key: `exec-summary-generator` (us-east-1). The artifact is built over the merged tree at
or after the `FB-j-11` merge; the difference from the deployed one (`CodeSha256` `8gbyCaYi896QYTm7MRxbLob7FCHWF5B9DKscxCgRPHY=`, the second apply) is
the slot switch (`EXEC_SUMMARY_DISABLED_SLOTS`, read at call time, empty by default) and the client-name guard in `_build_slot`. The plan is scoped
`-var platinum_mode=canonical -var disabled_slots=top_nna_mover -target=aws_lambda_function.exec_summary_generator` and must read
`0 to add, 1 to change, 0 to destroy`: the code hash and ONE added environment key, `EXEC_SUMMARY_DISABLED_SLOTS=top_nna_mover`; the six
existing keys (including `BD_PLATINUM_MODE=canonical`) unchanged. Role, timeout, rule and every S3 object stay untouched.

## Writers of the property (counted, N printed)

N = 1: `aws_lambda_function.exec_summary_generator` (code and environment). The function writes the served prefix only when invoked WITHOUT
`dry_run`; its only trigger is `exec-summary-trigger`, which the dispatcher has not emitted since 2026-04-22 and which `FB-j-4` would make fire; `FB-j-4`
stays un-deployed until the sample is read, `FB-j-7` is signed citing it, and the CTO's conditions (a) to (c) are done.

## The state this addendum records

Since the second apply the model path WORKS (39 bullets for ten advisors, 0 drops, listing identical). After this third apply the switch is ON:
a non-dry invocation would write real text for the four good slots to up to 158 client-facing keys, and `top_nna_mover` would write none. The act
does not invoke non-dry and no event reaches the rule; the guard is the same as before (the trigger stays un-deployed, no seat invokes without
`dry_run`).

## Both branches

- **Branch A (expected):** the plan is 0/1/0, the code hash plus exactly the one key; after the apply `CodeSha256` equals the artifact's and the
  environment reads the six old keys unchanged plus the one new; ONE dry run for ten pre-screened ids returns 200, `top_nna_mover` bullets 0, the
  four other slots non-empty, the served-prefix listing IDENTICAL before and after.
- **Branch B (STOP, no apply, a BLOCKING row):** any other resource or attribute in the plan, or more than the one environment key; the listing
  differs after the dry run (ROLL BACK to the prior artifact AND remove the key, the same turn, and report); a returned artifact carrying a client
  name or a relationship id (withhold its text and record the count; the deploy stands only if the guard test arms passed and the count is 0 in the
  four enabled slots).

## Rollback per object

The function's code and environment: re-point to the artifact deployed in the second apply (`CodeSha256` `8gbyCaYi896QYTm7MRxbLob7FCHWF5B9DKscxCgRPHY=`,
its S3 VersionId recorded in the entry before the apply), with `disabled_slots` unset in the same scoped `safe-apply` (the key disappears). No
served object is written by this act: nothing to roll back there.

## What this addendum does not know (named)

- Whether the four good slots hold up at 158 advisors: the sample is ten (of 158), spread by the pre-screen; the CTO and Andrew read it.
- Whether the guard catches every shape of a client name: the unit arms cover the two named shapes; the sample is its live read, and a
  returned text with a name is a STOP.
- The IQLT trace (`FB-j-12`): its classification is the CTO's input to serve; this addendum signs the deploy and the dry run only.

**SIGNED by `2.0.0_SA_COO~B1` for exactly this function, this third artifact, this scoped plan with ONE added environment key
(`EXEC_SUMMARY_DISABLED_SLOTS=top_nna_mover`) and dry-run-only invocations (`dry_run: true`, ten pre-screened ids).** A non-dry invocation, a
second environment key, the dispatcher deploy or the first regeneration needs the regeneration pair (`FB-j-7`) and is not this act.

-- 2.0.0_SA_COO~B1
