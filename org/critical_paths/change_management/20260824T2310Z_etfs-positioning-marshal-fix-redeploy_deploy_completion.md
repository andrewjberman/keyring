# Deploy Completion Record
**Date opened:** 2026-08-24T23:10:14.694827+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260824T231307Z
**Deploy:** ETFS_POSITIONING.TO-5 follow-on: redeploy etf-positioning-producer with DS~Z's marshal fix @32faa51d79 -- the handler returned DataFrames, so every invocation reported FunctionError AFTER succeeding, and async retries would re-run the whole pipeline up to 3x against a live served key before 13:00Z.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | rebuilt artifact -> s3://opal-313476888478-lambda-artifacts/etfs-positioning/ | build write-verify size + content-sha256 | Rebuilt from DS~Z's @32faa51d79 (verified in tree first: _summarize=1, json.dumps(out) self-check=1). SHA256 sR9QvfiS82IyXzRC4JUECpn1yFxLKfSehqT32nteems=, write VERIFIED. BAU_PARITY_SKIP=1 again, same justification (shared gold dir; the two avgcap files are unrelated producers). | CLOSED 20260824T231307Z |
| L2 | activation | terraform apply via safe-apply (code-only: source_code_hash) | apply output + new live CodeSha256 | safe-apply, code-only. Plan 0 add / 1 change / 0 destroy (source_code_hash). Apply complete: 0 added, 1 changed, 0 destroyed. Live CodeSha256 -> sR9QvfiS82IyXzRC4JUECpn1yFxLKfSehqT32nteems=. | CLOSED 20260824T231307Z |
| L3 | verify | 0-diff re-plan rc=0 in the owning root | measured rc, no pipe | terraform plan -detailed-exitcode in the owning root -> rc=0, captured with NO pipe. | CLOSED 20260824T231307Z |
| L4 | verify | deployed bytes carry _summarize + the json.dumps self-check; ad-hoc invoke returns 200 with NO FunctionError | downloaded package census + invoke response | CODE: downloaded package sha == live CodeSha256 (sR9Qvf...); _summarize=1 and json.dumps(out)=1 IN THE DEPLOYED BYTES; negative control 0. EXERCISED: ad-hoc invoke -> StatusCode 200 and NO FunctionError (previously Runtime.MarshalError on every invocation). Response is a 611-byte serializable POINTER (run_id/as_of/run_class/expected_frontier/trading_days_behind/status/objects_written/stats), not a payload copy. run_class adhoc, as_of 2026-08-21 with expected_frontier 2026-08-24 and trading_days_behind 1 -- NEVER#1's T-1 selection on a Monday, correct. So the 13:00Z scheduled fire will no longer report FunctionError and will no longer trigger async retries. | CLOSED 20260824T231307Z |

## Log

- 20260824T231014Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20260824T231307Z LEG L1 closed: Rebuilt from DS~Z's @32faa51d79 (verified in tree first: _summarize=1, json.dumps(out) self-check=1). SHA256 sR9QvfiS82I
- 20260824T231307Z LEG L2 closed: safe-apply, code-only. Plan 0 add / 1 change / 0 destroy (source_code_hash). Apply complete: 0 added, 1 changed, 0 destr
- 20260824T231307Z LEG L3 closed: terraform plan -detailed-exitcode in the owning root -> rc=0, captured with NO pipe.
- 20260824T231307Z LEG L4 closed: CODE: downloaded package sha == live CodeSha256 (sR9Qvf...); _summarize=1 and json.dumps(out)=1 IN THE DEPLOYED BYTES; n
- 20260824T231307Z CLOSED -- all 4 legs proven
