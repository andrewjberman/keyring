# Deploy Completion Record
**Date opened:** 2026-10-09T16:17:42.132092+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT SA-r-1b: ONE live FWD-1 journey under pair v2.2 (internal-tier token), widened live census, no data-refresh probe
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROW | verify | opal-users-v2 | conditional put attribute_not_exists(PK) of USER#tckt-fwd1-testfiler-20261009@opal.invalid + ConsistentRead read back present, allowedFirmIds LIST [49financial] |  | OPEN |
| TOK | verify | opal/auth/jwt-private-key | ONE RS256 token, CURRENT slot, v2.2 claims (tier internal, userType test-filer kept), exp=iat+2h, memory only; key read reported after via MSTR~DELL2 |  | OPEN |
| RUN | verify | live /api/scoped census + hops | census over EVERY live /api/scoped route with the denominator PRINTED (live table, not the source census; a differing count printed as a finding), data-refresh host SKIPPED per AMENDMENT 2, CREATE arms carrying the synthetic attachment per AMENDMENT 1 (an off-list 4xx passes only when the body NAMES the firm); any off-list admit or behaves-as-ALL is STOP; then hops a-g into R1_RUN/sa_r1b_trace.json, status+artifact id only |  | OPEN |
| CLN | verify | cleanup same session | row REMOVEd and read back absent; EVERY ticket this run created completed (the journey's and AMENDMENT 1's 49financial census arm); token left to expire |  | OPEN |
| DRZ | verify | /aws/lambda/opal-data-refresh-api | AMENDMENT 2's negative proof: filter_log_events for the filer email over [token iat, cleanup end], log group + window + query + match count PRINTED in the trace, expect 0; a failed retrieval is recorded UNREAD and never read as a zero |  | OPEN |

## Log

- 20261009T161742Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
