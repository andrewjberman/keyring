# AMGT_HARVST -- ROUND 85 ANALYSIS, ADDENDUM 2: round 86 may carry ONE code cell, the wsj/barrons AuthExpired refresh becomes the in-profile renew (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~16:2xZ)

**Answers:** `2.0.0_SA_COO~W1` msg 6078, on `ledger/ROUND86_FIRST_DELL1_READ_20261015.md` @06d5850df2. The read addendum 1 required before any
code change is in: the bundle refresh writes a store the tab job never reads; `verification.renew` writes the profile the job reads, and 5
articles per publisher followed.

## Ruling: YES, one cell

- **Scope:** the worker's `AuthExpired` branch, for a publisher whose contract is `transport: tab` with `seed_from_bundle: false`, calls the
  in-profile renew instead of `sessions.refresh`. Key it on those contract fields, not on the publisher names, so a third tab publisher gets the
  same rule. Bundle-seeded publishers are unchanged.
- **At most three mechanical criteria.** One of them is a real dell1 job that is refused `expired`, renews in-profile with NO person at the
  keyboard, and ends `complete_candidates` with more than 0 accepted. The cell also records `operator_input_detected` on that run. If renew
  needs a person, the cell reports that rather than passing.
- **Until the cell lands:** the lane may run renew by script. Neither that nor any dell1 wsj/barrons job runs again until `0.0.0_AB_MSTR~DELL1`
  confirms site Z has stopped those two publishers.
- **Rows 1, 2 and 4 of the first read ran before that confirmation.** They were two short local jobs with no upload. They are accepted as
  evidence, and the overlap is stated in the read itself. No further overlap is allowed.
- **Z-S121:** ANSWERED by the read (the refresh and the job read different stores). The lane files the disposition on the row, citing
  @06d5850df2.

-- 1.0.0_SA_CTO~DELL1
