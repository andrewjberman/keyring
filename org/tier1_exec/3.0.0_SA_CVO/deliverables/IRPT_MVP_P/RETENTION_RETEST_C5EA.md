# R-P07 independent retest — bounded closure

Reviewer: `3.0.0_SA_CVO~P`. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and `CVO_P.md`.

Candidate: **c5eace08c76176c6d9ebb78dd31ced3b0e57ea2d** (LOCAL). Original finding: **217cc1a**, candidate bd7c9f1b2c23737566f90a519634f904ff89f201. Independent run: 2026-09-22T22:27:46.652950Z.

**R-P07 CLOSED for the retention primitive.** The successful conditional write delayed across original reservation expiry no longer becomes readable acceptance. Supplied suite **16 PASS**, unchanged original independent suite **9 PASS**, additional receipt-boundary suite **12 PASS**. All three separate pytest processes exited 0. Full S7 and P1-P8/S1-S7 acceptance remain **NOT_EVALUATED**; this is not enforcement activation.

## What changed and what was verified

The transition persists a non-serving PROMOTING intent containing the original reservation deadline. Only the successful writer can then sample its server clock before that deadline and publish a separate conditional immutable receipt. Reads bind that receipt to the complete persisted intent hash, tenant, key and valid timestamp. Input rows directly marked ACCEPTED are refused. A fresh instance cannot certify an abandoned intent; this deliberately sacrifices recovery availability for the same identity when no timely receipt exists.

The original assertion file is unchanged: SHA256 `a4ce15e3852ec4e96fa91981e08ed7a2898cf25416393fb4669542a2101a39e0`. Original evidence and failing JSON are preserved. The new harness preserves repository-relative layout because the replacement supplied suite imports the canonical accessor by a root-relative path. It snapshots that accessor, schema and all seven registry files at the same candidate pin; it does not substitute working-tree implementations.

Added independent controls:

- A fresh observer refuses the intent before receipt persistence. Receipt transport failure before persistence stays non-serving after expiry, restart, reserve and promote retry. Failure after actual receipt persistence remains readable and idempotent because timely intent completion was already certified.
- Receipt persistence delayed past the reservation deadline may succeed only with the previously sampled timely intent completion; the accepted ceiling remains original. This is the declared completion boundary, not a new eligibility decision at persistence time.
- Intent-generation mutation, wrong receipt hash/tenant/key, boolean timestamp, direct ACCEPTED input state, and receipt transplantation to another identity all refuse. These are storage corruption/misbinding controls, not claims of an unprivileged storage-write exploit.
- Access revoked immediately after the intent write prevents receipt creation. Restored access cannot make the uncertified intent readable.
- Receipt delay to the accepted ceiling refuses promotion and fresh reads at equality.

Code inspection confirms `DynamoReportIndex.publish` uses `attribute_not_exists(request_revision)` and strongly consistent reads; the retention read validates the stored receipt even when publication returns an existing item. The supplied restart, missing response, original deadline equality, finite dependency lifetime, current owner checks, and canonical pending/isolated ACTIVE policy tests also pass. Actual committed registry remains pending; synthetic ACTIVE/enforcement_ref is test-only.

## Evidence and limits

- `retention_retest_c5ea.py`: reproducible pinned runner, raw commands, source hashes and process outputs in `retention_retest_c5ea.json`.
- `retention_receipt_cases.py`: 12 additional independent cases; SHA256 `14ff47c5c1164171cd091007505b42f4230ef814dd851ea318be10e823f787bf`.
- Retention module SHA256 `1777f3cf7887050cef3fde867ed8ec304e24136af8d99ebf9e2a2013d2cbb307`.
- Repository module SHA256 `805805dd922e9cd77a9873c4c77aa1f8a857469b2d9440ebed6fd64ec55ed2ba`.

Execution uses actual pinned retention/repository/accessor modules and boto3 serialization/supplied Stubber, with synthetic transport, clock, owner and isolated ACTIVE policy. Interleavings are controlled in one process; actual multiworker clock skew/concurrency and deployed IAM are not measured. No lifecycle integration, physical cleanup, provider, browser, export, live cloud or deployment run occurred. New Python files passed Ruff.

CVO~M's exact notification `20260922T222434Z_3.0.0_SA_CVO_M_IRPT_X10__bounded_independent_PASS_eb00a.md` reports independent registry review **eb00a0c6b2** for pending candidate **587e782bc6**, generation evidence **3c14153eeb**, and policy SHA `cb9c4e6e9541fefc315f57844490309ad15c9735593fe3a165b067a3087dc220`. This is retained as peer evidence, not rerun here. Its owner signoff/integration, reader/writer enforcement and full S7 limitations remain. The message requested no ACK.

Next acceptance requires a completed pinned integration showing the approved policy, actual producers/readers, immutable report/artifact dependencies and release-time access/expiry checks compose. No broad acceptance, activation, provisioning, deploy, cleanup or vendor authorization follows from this closure.
