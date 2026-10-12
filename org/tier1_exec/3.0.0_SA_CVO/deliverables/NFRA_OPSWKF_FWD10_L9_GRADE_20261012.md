# NFRA_OPSWKF -- L9 grade of OW-sd3-AC1 (FWD-10: the second door is closed)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T00:10:38Z. Row NFRA_OPSWKF-D2-S15.
**Input:** `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/S5_FINAL_REPORT_SECOND_DOOR_CLOSED.md @e6c3267f85 (msg 6188)`. Graded against PRD v0.11's DONE WHEN, signed by this seat in the same hour.

**Verdict: OW-sd3-AC1 MET. FWD-10 REALIZED.**

| limb of the DONE WHEN | evidence | whose read |
|---|---|---|
| the setting read back from the API's own configuration, separately from the write | TRUE | the applier's; the CTO's at 23:58:15Z; **this seat's at 00:08:48Z** |
| one request with no credential to a route behind the authorizer: 401 before, the endpoint's refusal after | 401 `Unauthorized` at 23:51:13Z; 404 `Not Found` at 23:57:49Z | the applier's |
| the two answers written out and shown different | both printed in the report, status and body | the applier's |
| both domain planes and the distributions read, none carrying the API | 0, 0, and 0 of 2 scanned | the applier's; this seat read 0 API domain names in the region |
| no request to the sign-in route, by any seat | six requests made, none to it | the applier's statement |
| the act is one reversible setting, with the value that restores it | one call, named in the report; not used | read in the report |

The setting is now read TRUE by three seats separately, which is the direct evidence. The probe is the witness that the setting
does what it says: the same request that the API itself refused with 401 before the act is refused at the endpoint after it.

The control that makes the probe mean something is in the same report: the missing-route request reads 404 before and 404 after.
Had that been the only probe, as PRD v0.10 had it, the proof would have passed with the door open.

## What this closes, and what it does not

- **Closed:** the public endpoint of the second API. Nobody on the internet can present a password to its sign-in route, and nothing
  reaches the trade workflow function through it. This seat's grade of FWD-8 and FWD-9 said "Opal staff only" was not shown on
  every path to those functions; this was the other path.
- **Not closed, and stated by the CTO:** the API, its two functions and their signing key still exist; one call re-opens it. Deleting
  them is unrecoverable and is Andrew's. Who may invoke the trade functions directly is a separate row, carried to another box.
- **Not known and not knowable from here:** whether the sign-in route was ever used against the users table in the nine months
  before the 30-day metric window. Access logging was off.
- **Not read by this seat:** the stage, the two distributions, the report's request log.
