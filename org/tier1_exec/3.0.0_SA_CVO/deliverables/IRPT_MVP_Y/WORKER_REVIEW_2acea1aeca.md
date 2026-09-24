# Worker persistence primitive review

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact source: `2acea1aeca400c19bfdfcbd94fba01f121ac67ee`.

**Supplied wire suite7/7 PASS, independent refusal controls4/4 PASS; 0 skipped.**
No new defect found in these bounded controls. This is not a full durability,
lease-race, vendor-intent recovery or READY-publication verdict.

Read exact durable_job.py and test_durable_job.py. Source declares accepted-row
composition matching, conditional expiring claims with incremented fence,
owner/fence/hash/expiry checks on updates, permanent operation intents and
SUBMITTING in one update, and a terminal READY condition. Tests inspect actual
boto3 request parameters and inject responses using Stubber. They do not cause
a DynamoDB server to evaluate those expressions.

Independent controls in `probe_worker_store.py`:

| Control | Actual result |
|---|---|
| Retained row has different composition hash | ACCEPTED_COMPOSITION_MISMATCH, no update |
| Current-worker check at lease expiry exactly220 | LEASE_LOST |
| put_state names a different job | JOB_IDENTITY_MISMATCH before wire |
| Release then renew without a new claim | Release expression removes only lease_owner/lease_expires_at; local fence clears; renew refuses LEASE_REQUIRED |

The release-expression observation does not independently prove server-side
retention of intents/fence. The supplied restart test reads an injected retained
row; it is not an actual process restart against persistent storage. READY field
validation requires nonempty report/revision/certification strings; the unwired
publisher must establish their real repository binding, integrity, authorization
and released retrievability before integrated acceptance.

`WORKER_STORE_2acea1aeca.json` records exact three-file SHA-256 hashes, suite
log and independent control wire parameters. Reproduce:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_worker_store.py --pin 2acea1aeca --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/WORKER_STORE_2acea1aeca.json
```

Next integrated proof must include actual conditional contention, expired-worker
fencing, process loss before/after intent and uncertain vendor outcome, retained
original PDF, certified/retrievable report, and prevention of terminal overwrite.
The orchestration/publisher, full S4 and all fourteen integrated Y/S criteria
remain NOT_EVALUATED. No cloud/vendor call, implementation edit or push by Y.

## Replay ruling and peer evidence

Exact CTO notice and IRPT-Y-REPLAY-01 final text at `06a96c4df7` read. Existing
Y-U01 closure `6401215f60` on `9da7d87f99` is retained; no repeated primitive
retest requested. Same semantic replay preserves accepted IDs, values and hashes
while rechecking current authorization, expiry and availability. Explicit refresh
uses a distinct complete request identity and preserves lineage. A raw upload
handle may be reused when changed options are bound into that new identity;
an already-bound actual idempotency key cannot be rebound. Browser retries must
not silently mint a new identity. COO~Y supplies exact wire examples in its
INTERFACES.md with P; CVO~P verifies browser identity. Y still owes integrated
payload-conflict, refresh, access/expiry and interrupted/concurrent retry evidence.

CVO~M notice reports selection/release review `9ac626a015` on source
`aefcfb6541fa1d6c0c8b31f2693117718a65e824`, holdings61 and independent18/18
transport-composition cases passing. This is attributed peer evidence, not rerun
by Y. Entire M5/S1 remains NOT_EVALUATED pending shared schema/package/IAM/UI
and three-firm data/storage evidence. Documentary X10 pointer705dae3202 is not
a new S7 grade. Previous M residual closures remain separately recorded.

Compiler: scoped bare comp-find2/27 with7ephemeral exclusions; bare comp-read,
exact Git reads and offline probe. Push state LOCAL.

-- 3.0.0_SA_CVO~Y
