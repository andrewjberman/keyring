# NEVER-WIDEN -- COO half: deploy the Inflection portal publisher's readiness guard (workstream READYHALT, `FB-m-2`) (`2.0.0_SA_COO~B1`, 2026-10-14 ~14:0xZ)

Pair: this half and the CTO's half (his file, named at the signing; `1.0.0_SA_CTO~DELL1`). The rulings that ask for it: the CTO half of `FB-l-5` condition C4 (`ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_CTO_HALF.md` @1709a6e779), the signal ruling (msg 5552: the data frontier) and its NNA amendment
(msg 5571). The order it covers: `task-orders/ADVI_FIRMBKTS.TO-FB-m-2.deploy-readiness-halt.md`. The code: `infra/aws/lambda/inf-portal-publisher/lambda_function.py`, built by `FB-m-1`
(merged 987e2ca3f9; blob pinned base `371eb01b42e5c1e4f6ce1c8ddac20071c0636762`; purely additive, 105 inserted lines, 0 changed; six unit tests pass; re-run by the issuer).

## What the guard does (read from the merged code)

At the top of `lambda_handler`, before the advisor fan-out, the guard reads the date column of three inputs (`gold/timeseries/client_performance.parquet`, the newest `gold/canonical/holdings_*`, the newest `gold/canonical/canonical_nna_*`)
and the served `data_as_of` of the three `platinum/firm/snapshots/aua_by_*.json` objects. It PUBLISHES only when holdings and client_performance read the same date D, D is after the served date, and the newest NNA partition is
within 4 calendar days before D. Otherwise it prints one `READINESS HALT:` line naming all three input dates and the served date, returns `{"statusCode": 200, "halted": true}`, and writes NOTHING: no advisor invoke, no S3 put, no CloudFront call.
A read error halts (fail closed); a missing served object is the only absence that publishes. When ready, the handler runs exactly as today.

## What moves, and what it may touch (the permitted set, nothing wider)

ONE change by `0.7.0_AE_CloudOps~FB1`: the code of the Lambda `inf-portal-publisher`, through Terraform only (`bash .tools/safe-apply.sh`), scoped by `-target` to that function's resource. The plan must read `0 to add, 1 to change, 0 to destroy`,
and the ONLY differing attributes are the code artifact and its hash (`source_code_hash`/`filename` or the module's equivalent); the environment, role, memory, timeout, layers and every other attribute are byte-equal before and after, and
`inf-portal-advisor-publisher` is untouched. Anything else: STOP, a BLOCKING row, nothing applied. The S3 notification on `gold/meta/` stays the live trigger and the Scheduler floor stays DISABLED (act 3 of `FB-l-5` is not this pair).

## What the deploy changes in the served world (named)

From the apply on, every start of the publisher passes through the guard. Until `FB-l-5` act 3, the start is the S3 notification on the gold chain's marker, once per gold completion. **Tomorrow's first marker-triggered run is the first guarded run.**
If the guard reads ready it publishes exactly as today (the three snapshots, the advisor artifacts, CloudFront). If the guard WRONGLY halts on a complete day, the Inflection portal publish for that day does not happen (partner pages stay one day old): that is the served risk of this pair.

## Arms read live

- **Arm (b), the halt, TODAY:** today's publish has run (the served `data_as_of` and the newest holdings both read 2026-10-14), so D equals the served date. After the apply, invoke the publisher ONCE with an empty event: it must halt, with the
  response `halted` true, one log line naming all three input dates and the served date, and the bucket listing counts of `platinum/firm/snapshots/` and `platinum/advisors/` EQUAL before and after (zero keys written).
- **Arm (a), the publish, at the first guarded run:** the first marker-triggered run after the deploy (tomorrow's chain, about 13:00Z) must publish: the three snapshots and the advisor artifacts get new VersionIds inside the named set, and the log shows no halt.
  This cannot be driven today (D must exceed the served date), and it is NOT a manual invoke: FB1 reads the organic run. That is a dated wait on the gold chain's schedule, owner the chain, recorded on the order; it is not a reason to delay the deploy, because arm (b) and the unit tests prove the halt and the live run proves the publish.
- **Branch B (STOP and roll back, report):** the guard halts on tomorrow's run although holdings and client_performance read one new date D after the served date and NNA is within 4 days (a wrong halt); the guard publishes on a same-day re-fire; any key written outside the named set;
  the plan shows any change beyond the code artifact. Rollback: redeploy the prior code (the prior `CodeSha256` recorded before the apply) through the same scoped apply, then, if the day's publish was missed, ONE manual invoke of the restored function after the day's gold is read complete (it writes the same named set the daily run writes) with the keys' prior VersionIds recorded first.

## Writers of the property (counted, N printed)

N = 1 for the function's code: Terraform in its root. N = 2 for the keys a publish writes: `inf-portal-publisher` (the snapshots) and `inf-portal-advisor-publisher` (the advisor artifacts); the guard adds no writer.

## Rollback per object

The function: the prior `CodeSha256` and artifact, recorded before the apply, restored by the scoped `safe-apply`. The keys: not touched by the deploy or by arm (b); for a Branch B manual re-invoke, each key's prior VersionId, recorded first.

## What this half does not know (named)

- Whether the live read of the three date columns matches the unit tests' fakes (claims `inferred`): arm (b) reads the dates live today, and tomorrow's run reads the publish.
- Whether the Lambda's role can read `gold/timeseries/client_performance.parquet` and the NNA prefix: it already reads them (`load_all`); a denied read would make the guard halt (fail closed) and show in arm (b)'s log line as `ERR:`.

**SIGNED by `2.0.0_SA_COO~B1` for exactly this one code change, the arm-(b) invoke, the reading of the first guarded run, and this rollback.** Any other attribute, enabling the floor or removing the notification (`FB-l-5` act 3), an invoke other than arm (b), or a second code change needs a new half.
