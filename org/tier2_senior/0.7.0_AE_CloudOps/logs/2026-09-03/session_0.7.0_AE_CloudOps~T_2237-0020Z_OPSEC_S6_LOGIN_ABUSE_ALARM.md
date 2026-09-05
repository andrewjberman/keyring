# Session Log -- 0.7.0_AE_CloudOps~T -- 2026-09-03 22:37Z to 2026-09-04 00:25Z

**Seat:** `0.7.0_AE_CloudOps~T` (site-Z lane, spawned by `2.0.0_SA_COO~Z`)
**Face:** `NFRA_OPSEC202609.TO-OP-S-6` -- the login-abuse alarm (cell `OP-s-6`, endpoint FWD-4)
**Archetype:** BUILD (terraform apply + live exercise)

---

## Current State

**TO-OP-S-6 is COMPLETE with one named open leg.** Proof-of-spec instance **VALID rc=0**
(checker-vintage `50ff3d674a`): 4 of 5 criteria PASS, `S6-AC3`
**UNCOMPUTABLE-BY-CONSTRUCTION** exactly as the face prescribes, citing row
`NFRA_OPSEC202609-Z-S97`. Deploy ledger `opsec-s6-login-abuse-alarm` **CLOSED, 6 of 6 legs
proven**. Status flipped `staged -> complete`.

**What is now live on the authentication path**, where nothing was before: two CloudWatch
alarms (`OPSEC-auth-login-rate-limit-blocked` on the WAF rule's `BlockedRequests`,
`OPSEC-auth-throttled` on a metric filter over the auth handler's `auth_throttled` line), one
dedicated SNS topic `opal-login-abuse-alerts`, one metric filter `OPSEC-AuthThrottled`.
Alarm count 49 -> 51; module state 88 -> 92; account SNS topics 15 -> 16.

**BOTH ALARMS HAVE DEMONSTRATED A REAL `ALARM` TRANSITION, from two different real causes** --
which is stronger than the single staged exercise the face asked for:
- Alarm (b) transitioned `OK -> ALARM` at **00:03:36Z** on this seat's staged burst.
- Alarm (a) transitioned `INSUFFICIENT_DATA -> ALARM` at **23:46:29Z** on a *peer lane's*
  genuine 60-block burst -- unplanned production traffic, two minutes after the alarm existed.

---

## Blockers

**ONE, and it is an input rather than a defect.** `C-6` requires one email per event to ONE
NAMED PERSON. Nobody has that name. The SNS topic exists with **zero subscribers** and no
address was guessed, defaulted to Andrew's, or set to a role address. Row
`NFRA_OPSEC202609-Z-S97` is **ARMED** with `2.0.0_SA_COO~Z` as `disarm_owner`; the issuer
confirmed at 23:25Z it has routed the question to Andrew. **One `aws_sns_topic_subscription`
closes it.** Until then the estate has two working alarms that reach nobody -- which is the
honest state, recorded rather than papered over.

---

## What was learned, and it cost something each time

**1. THE CONTROL THAT FIRED TWICE BEFORE IT PASSED.** `S6-AC2`'s negative control -- state the
alarm's state BEFORE the burst -- is the whole criterion, and it blocked two claims this seat
would otherwise have made. First the WAF alarm was already in `ALARM` pre-burst (a peer's
probe). Then a burst at 23:54 came *after* an `OK -> ALARM` transition at 23:52:36Z caused by
the peer's 23:51 datapoint, so it **sustained** an alarm rather than transitioning it, and was
not claimed. **On a live production auth path, "the alarm is currently OK" is a PERISHABLE
precondition and timing alone can never attribute a transition.** The fix was to move
attribution to CONTENT: a burst sized an order of magnitude outside the peer's range, carrying
a unique User-Agent. The crossing datapoint was 190.0 and 190 + 45 = **235 = exactly this
burst's 429 count**, in a minute whose WAF records were **240 of 240 `opal-s6-probe`**.

**2. I CORRECTED MY OWN ROW TWENTY MINUTES AFTER FILING IT, AND THE CORRECTION INVERTED.**
`Z-S98` claimed a JSON metric-filter pattern could not match the auth handler's Text-format
prefixed lines, and recommended a substring pattern. **Every fact in that row was measured and
true** -- `LogFormat: Text`, the lines are prefixed, `throttle.ts:118` emits
`console.log(JSON.stringify(...))`. **The conclusion drawn from them was false.** The step from
those facts to "the matcher will not match" was a belief that was never itself measured, and
the true facts made it feel evidenced. `test-metric-filter` settles it in one read-only call
and I filed before running it. Worse, the counter-evidence was already in the file I was
editing: four sibling FIRMSEP filters use the condemned pattern form. **Direction of the
avoided harm: the substring pattern also matches bare prose containing the token, so I would
have shipped a LOOSER filter that over-counts on the authentication path, feeding the
project's only authorised notification.** Filed as `Z-S99`, append-only, before building.

**3. A CLEAN ZERO FROM AN IDLE RESOURCE.** A census of the 377 `AWS/WAFV2` metrics for a
`Rule=AuthLoginRateLimit` dimension returns **0** -- and that is NOT absence of the rule. A WAF
rule publishes no rule-scoped metric until its first match. Reading the **WebACL object**
instead showed the rule present at priority 2 with action `Block`. Positive control before
believing the zero: the same matcher against `Rule=RateLimitRule` returns 1.

**4. THE DIMENSION TRAP THAT WOULD HAVE SHIPPED SILENTLY.** CLOUDFRONT-scope WAF metrics carry
**only** `WebACL` + `Rule`. The regional sibling `opal-gateway-waf` carries three including
`Region`. An alarm copying the sibling's shape matches no metric and sits in
`INSUFFICIENT_DATA` forever. Measured from the live metric inventory, not inferred.

**5. THE MODULE WAS NEVER AT 0-DIFF.** `S6-AC5` asks for an unscoped re-plan "0-diff after".
The baseline BEFORE the first edit already read `0 to add, 1 to change` -- a standing churn on
`aws_wafv2_web_acl.opal_cloudfront_protection` whose removed and added rule blocks are 39 lines
each with an **empty symmetric difference**. Provider re-serialisation, committed config vs
live AWS, not this face's. The apply was **targeted** so it would not ride along, and verified
by an **unscoped** re-plan so the scoping could not certify itself. Reported as DELTA=0 against
the quoted baseline, with the divergence from the criterion's literal wording declared.

---

## Compiler Tools

- **`comp-read`** on the task order, the terraform carrier and `surprise-row-gate.py`. On the
  carrier it surfaced a tail comment asserting `opal-infrastructure-alerts` has **no**
  subscribers -- **false on the live plane** (it has one SMS subscriber), so that comment was
  not relied on. On the TO its UNREAD LEDGER showed 15 of 67 lines surfaced, so the file was
  then read WHOLE rather than acted on from the extract.
- **`comp-find "auth_throttled" --all --limit 40`** -- DENOMINATOR 12 hits across 51,633 files,
  bands SURFACED=2 CONFIG=2 DOC=8. Located the emitter and separated it from 8 DOC-band
  mentions. **The rail correctly refused an earlier attempt that piped this census into
  `head`**, which would have erased the denominator.
- **`aws logs test-metric-filter` with a negative control** -- the decisive instrument of this
  face; see learning 2.
- **`deploy_ledger.py`** open (before the apply, rollback named) / close-leg x6 / close.
- **`safe-apply.sh`**, **`safe-commit.sh -F`** (message files written by a non-shell writer on
  session-unique paths), **`proof-of-spec-check.py`** VALID rc=0.

---

## Next Steps

**[`2.0.0_SA_COO~Z` / Andrew]** The recipient address. It is the only thing between this face
and a human actually being reached, and it is one fact.

**[`0.7.0_AE_CloudOps~T`]** Push state is **LOCAL-ONLY** for `e2dabdc3ab`, `ab76a1c0c8` and the
closing commit, measured by `ls-remote` + `is-ancestor` with a negative control. The push is
the integrator lane's act, not this seat's.

**[open question, not chased]** This seat's 240-request burst did **not** trip the WAF rate
rule (0 blocks; `Default_Action` on 240 of 240) while a peer's burst did trip it 60 times. The
application throttle returns 429 before the WAF rate-based threshold is crossed. Whether the
WAF rule's threshold is correctly sized for the abuse it exists to stop is a real question and
**belongs to `TO-OP-S-23` (rate-threshold review), not here** -- surfaced, not chased.
