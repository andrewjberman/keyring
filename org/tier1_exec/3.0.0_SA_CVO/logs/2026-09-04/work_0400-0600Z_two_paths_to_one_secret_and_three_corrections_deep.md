# 3.0.0_SA_CVO~Z -- work log 2026-09-04 04:00-06:00Z: two paths to one secret, and a correction three deep

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_0210-0400Z_*`. **Channel:** 134 -> **142 rows**,
40 this seat's, ids contiguous. **Push state:** local HEAD ce67ce539c; `origin/SITEZ` last read 001709c96e,
**UNREAD at this vintage**.

## 1. The JWT_SECRET thread, sized by three seats in three hours

Z-S127 found a symmetric `JWT_SECRET` in cleartext Lambda environment variables on two trade-pipeline
functions. **Z-S140 sized it into the worst branch: FORGEABLE AND REACHABLE** -- the secret both MINTS and
VERIFIES, `trade-submission-api` has a deployed prod stage with `DisableExecuteApiEndpoint` FALSE, six of
seven routes are authorized by that authorizer, **the 129-day dormancy was absence of TRAFFIC not absence of
WIRING** (a probe woke it), and 14 principals of 231 can read it including three human users. **Z-S141**
completes it: the API HAS been successfully authenticated against (2026-01-07, 105 requests, zero 4xx, 18
authorizer runs all ALLOW), and whether it was ever ABUSED is **uncomputable beyond 14 days** -- stage access
logging never enabled, authorizer retention 14 days. Its framing is exactly right: **a finding, not a
demonstrated incident, and not a demonstrated NON-incident either, because no instrument reaches.**

## 2. Z-S142 @ce67ce539c -- the second read path, with the good half leading

Z-S140's count is correct for the path it measured and is not the whole reachable set.

⭐ **THE GOOD HALF FIRST, because it rules out the worst branch available:** `JWT_SECRET` is assigned at
`trade-pipeline/lambdas.tf:59` and `:90` as a **VAR REFERENCE, not a quoted literal**. A literal would have put
a signing secret in git history -- unrotatable by any AWS action, readable by everyone who ever cloned. It is
not that, and establishing so was worth more than the rest of the row.

⛔ **BUT TERRAFORM RECORDS RESOLVED VALUES IN STATE.** This root's backend is S3 at
`opal-313476888478-terraform-state`, so the same secret sits in plaintext where reading it needs
`s3:GetObject` on that bucket and **NO lambda permission at all** -- a different principal set from the 14
simulated, and unmeasured. **BOUNDED, NOT OPEN, and measured rather than assumed:** all four public-access-block
flags TRUE, SSE-AES256. Authenticated-internal reach, not internet reach.

**Seventh instance of the Z-S122 shape, and the MIRROR of Z-S136:** there, terraform was a second WRITER
invisible to a principal census because it needs no fourth principal; here it is a second READ PATH, invisible
for the identical structural reason. **A seat that has just run a 231-principal simulation has every reason to
believe the question is answered, which is exactly when the second path goes unasked.**

**It probably adds no work and does add a CRITERION:** moving the value into a secret store clears both at
once, but a remediation verified only against `get-function-configuration` would PASS while state still carried
it.

⛔ **NO SECRET VALUE WAS READ, STORED OR ECHOED**, and the method is in the row so the claim is checkable: the
assignment was CLASSIFIED by testing its right-hand side against a prefix set, printing only the classification
and a character count. The file was never displayed.

## 3. Z-S138 @aab6e5f67b -- and this seat's correction chain, three deep

On Z-S136 (terraform as a second WRITER erasing the blocked-IP sets) this seat amplified up-lane and **added a
gloss the row never contained** -- "an address that is currently blocking traffic". Corrected two minutes
later on recognising `203.0.113.42` as TEST-NET-3. **But that correction reasoned from the ONE address the row
happened to name, and Z-S137 then reported FOUR queued deletions** -- so it covered one of four.

⛔ **AN OVERSTATEMENT CORRECTED FROM A SINGLE EXAMPLE IS STILL A CLAIM ABOUT A POPULATION.** Three calls
settled it: all four sets hold exactly one address, total 4, reconciling exactly with Z-S137's independent
count -- two IPv4 in TEST-NET-3 (RFC 5737) and two IPv6 in `2001:db8::/32` (RFC 3849) with a `dead:beef`
placeholder. **All fixtures.** Agrees with Z-S102's finding that the sets are empty by design under C-2.

**Nothing in Z-S136 is corrected by any of it** -- its wording is accurate, its mechanism and remedy stand,
ARMED with its owner. What Z-S138 settles is WHEN it bites: when the reconciler writes its first REAL address,
not on the next unrelated apply. **An armed row's priority is set by what it would destroy, and no row carried
that.**

## 4. A caution sent rather than filed

Z-S141 cites "the authorizer's log group is 14-day retention with **storedBytes 0**" as supporting detail, and
20248 says that row is being surfaced to Andrew. Per Z-S93 storedBytes is not a delivery signal at either
grain, and Z-S140 reports the stream advanced to now. **Its CONCLUSION does not depend on it** -- retention
alone carries "uncomputable beyond 14 days" -- so this went to the routing seat as a one-clause caution rather
than a row: a human meeting "storedBytes 0" may read "no logs exist", which is a different and wrong finding.
**Correct what changes a conclusion; flag what could mislead a reader; attribute the rest.**

## 5. State

**142 rows, contiguous, 40 this seat's.** Nothing waiting on this seat. **The one blocked item is unchanged:**
the four round-1 closure rows; gate here still `c3ef3a2530`, 0 occurrences of `REMEDIATED`.

⭐ **The pattern worth carrying to L9: every correction tonight NARROWED rather than reversed.** The mechanism
survives, the overstated clause goes, and the replacement is more precisely bad than the original claim --
Z-S139's "breaks permanently" became "a partial, silent, self-clearing outage of unbounded tail duration",
which is worse and truer. **That is the difference between a record that converges and one that accumulates.**
