# Review: IRPT_ANLREQ PRD v0.28 @ea3014a892, brief half (4.0.0_SA_CRO~TCKT, 2026-10-20 ~18:3xZ)

## What changed

The diff `cd00de4ecb..ea3014a892` on the PRD is 21 insertions and 2 deletions. It changes:
- the version line;
- the C-AUDIT-RECORD row: the address is now `opal-data-irpt/irpt/<firm>/platinum/analysis_audit/`, the IRPT product
  bucket under the firm prefix;
- addendum v0.28, which is added.

The ENDPOINT is byte-unchanged.

## Andrew's word on the one departure

- His original words: "an analysis-report folder in each firm's bucket" (@f2581e90b9).
- This seat asked him the exact question: the shared Investor Reporting bucket, with a folder per firm, versus each
  firm's own bucket.
- His answer, verbatim: "OK, per-firm folder (Recommended)".
- Record: `ANDREW_DIRECT_20261020_18xxZ_AUDIT_RECORD_IRPT_BUCKET_FIRM_PREFIX_OK.md` (this commit).
- So the v0.28 row now carries his word, not only the driver's ruling.
- The addendum's "this seat states the difference in its close-out" is discharged by that answer.

## Note (no refusal)

`run.json` for REQ-d6231c013ae90519c67d18e9 was read live on 10-20 at
`s3://opal-data-49financial/irpt/49financial/state/ycharts_runs/...`, in a FIRM bucket (prior-art read, M). The addendum
says the firm buckets are fenced against the resident role (`resident.tf` 229-241).

Both can be true if a different writer puts `run.json` there, or if the fence denies only some actions. The audit
record's address is unaffected. Whoever owns `resident.tf` should read the run.json writer against that fence once
(see the surprise channel if it does not reconcile).

Verdict: SIGN.
