# Independent retained-upload dependency review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `acc55a4c727e3919f2a972072191e423b81200e7`.
Required P source `aa1cfaea6b063acac5fc974d397d6a278daa17a0`; the reports
subtree diff against this candidate has no changes (exit0).

The bounded upload composition passes **31 supplied tests plus11 subtests**,
and **9/9 independent controls**. No new defect found in these controls.
Original Y-U01 replay and explicit-correction controls still pass. Actual Y
upload code now supplies the retention dependency references to P's real
retained repository/policy; storage, current time and registered ACTIVE policy
remain controlled offline fixtures. No real policy was activated.

## Reproduction and evidence

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin acc55a4c72 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_acc55a4c72.json
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_retained_upload.py --source-evidence org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_acc55a4c72.json --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/RETAINED_UPLOAD_acc55a4c72.json
```

The first command snapshots the exact source and hashes it. The second verifies
all289 snapshot hashes, executes independent controls, then runs the supplied
upload17, retained-upload5 and retained-repository9 tests. The17 upload tests
overlap the first command; they are not added again to31. The11 subtests are
reported separately. Source inspection covered the Y diff/new tests, complete
P composition/retention code, retained repository tests and relevant artifact
put/get implementation. This is not a full repository audit.

The first probe attempt stopped on a reviewer exception-class lookup mistake
before writing evidence. Correcting its lookup to repository.ReportRefused and
rerunning unchanged scenarios produced the recorded results; no candidate
source changed. A later limit-note edit only identifies the separate peer
history review and does not alter test data or outcomes.

## Independent observations

| Control | Result |
|---|---|
| Three revisions created on days0,10,20 | Six original/normalized retention records have the same day30 deadline; each normalized record depends on its own original, each refreshed original on the prior normalized record |
| Recompose retained repositories/policy and service; retry one second before expiry with dependency callbacks forbidden | Identical third result, unchanged deadline, zero additional blob puts |
| Remove oldest retention record | Descendant read refuses RetentionExpired |
| Exact oldest deadline | Descendant read and fresh-token refresh both refuse; zero additional blob puts |
| Registered fixture policy becomes pending during blob read | RetentionRefused; no result returned |
| Expiry during successful refreshed-original blob write | RetentionExpired, one new raw blob, zero new INPUT rows |
| Expiry during successful normalized blob write | RetentionExpired, two raw blobs total, zero INPUT rows |
| Current owner revoked during blob read | ProspectOwnershipRefused |
| Retention service removed from repository serving an already retained input | ReportRefused |

Recorded epoch deadline is1802592000, from original creation1800000000 plus
30days. Current authorization and recursive dependency checks protect these
returns; the delayed-write cases do not claim that stored bytes were removed.

## Limits and integration obligations

Raw blobs/reservations can remain after a refused late write. Physical disposal
and orphan lifecycle remain unproved and no deletion was attempted. Same-process
recomposition is not actual process loss; storage doubles do not prove server
concurrency, clock skew or delayed conditional writes. Promotion of the oldest
dependency chain into accepted report evidence, Y's fenced report index, READY,
browser retry/refresh and maintained runtime assembly still require integration.

Separate CVO~P notice230253Z reports LOCAL452f8d589f closes R-P08 at284436ca11
with79 unchanged tests PASS, explicitly bounded to sequential metadata checks,
not atomic history. That result is attributed only and does not change this
candidate's source or establish Y history/fenced-consumer acceptance. R-P07
closure and the delayed-commit/client-clock/accepted-row recovery obligations
remain separate. All fourteen integrated criteria are NOT_EVALUATED.

No vendor/session/cloud/render/provisioning calls or implementation edits were
performed by this reviewer. Review evidence is LOCAL.

-- 3.0.0_SA_CVO~Y
