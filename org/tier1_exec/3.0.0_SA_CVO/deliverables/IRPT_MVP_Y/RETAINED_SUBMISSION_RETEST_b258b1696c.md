# Y-S01 independent repair retest

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `b258b1696c75296e203e89fbd85434b3b91d9066`.

**Y-S01 CLOSED for the retained SubmissionService boundary.** The original
independent probe is unchanged. All **8/8 controls PASS**, including both prior
failures. Supplied **54 tests plus24 subtests PASS**, exit0. Original failure
evidence at6cbb714040 remains unchanged in review05a5ab10c6.

## Reproduction

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin b258b1696c --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_b258b1696c.json
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_retained_submission.py --source-evidence org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_b258b1696c.json --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/RETAINED_SUBMISSION_b258b1696c.json
```

Source hashes for290 snapshot files are verified. The repair moves inspection
of the known input/composition reference ahead of the no-service branch and
refuses when that reference has a retention_ref. Its exact two-file diff was
read. Genuinely unretained offline cases remain in the passing supplied suite.
No probe changes or implementation edits were needed for retest.

| Original failed control | Candidate result |
|---|---|
| Expired accepted retained composition; repository retention service removed | AcceptanceRefused / RETENTION_SERVICE_REQUIRED; zero dispatch calls |
| First submission of retained input; repository retention service removed | AcceptanceRefused / RETENTION_SERVICE_REQUIRED; zero dispatch calls, no accepted composition ref |

Other original controls remain passing: exact normalized-input dependency and
oldest deadline, unchanged replay without provider resolution/new blobs,
configured-service exact-expiry refusal, changed input receipt refusal before
storage, and post-acceptance expiry/pending-policy refusal before dispatch.
The supplied new first-submission test additionally asserts no new blob write.
The17 upload tests overlap the54 combined suite and are not counted twice.

These results exercise actual Y/P code with storage/clock fixtures and Mock
acceptance/dispatch. They do not establish real queue delivery, worker recovery,
server concurrency, maintained runtime or full S4/S7/READY acceptance. All14
integrated criteria remain NOT_EVALUATED; original unrelated closures stand.

The same notice reports separate candidate601e1c7bf1 with three P retained
repository/Y fenced adapter composition tests and16 combined index/job tests
passing. That result is producer-attributed here, not independently rerun or
added to this retest's counts. Its successful-write/postcheck-failure case
explicitly preserves an authorized recoverable row; subsequent revocation is
reported to refuse. Simulated transaction effects are not server timing or
Dynamo expression proof. Existing9d33387734 integration obligations remain.

Evidence is LOCAL. No policy activation, cloud/vendor/session call or source
implementation edit was performed by this reviewer.

-- 3.0.0_SA_CVO~Y
