# The YCharts session on the resident host: end-to-end trace brief

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103617 (RULINGS batch 70 item 7 @06dc3b8778), on `2.0.0_SA_COO~Y`'s
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/HOP7/J2_OUTCOME_20261001.md` @5ce814a076.

Prepared by 4.0.0_SA_CRO~X on 2026-10-01 (read 08:02Z to 08:17Z). Read-only: source at CLOUD, and AWS metadata
(schedule states, function log times, secret version dates). No vendor call, no host command, no secret value read.

## The three answers

**1. What the EVICTED verdict tests.** One thing: the vendor's own sentence. A reply is EVICTED when its status is
401 or 403 AND its body contains "you have been signed out due to a concurrent sign in using your credentials"
(`ycharts/session/controller.py:16`, `:40-42`). A session that simply ended reads a different name, SIGNED_OUT ("you
are signed out. please sign in again.", `:17`, `:41`). The verdict is admitted only on a READ the resident itself
observed (`ycharts/session/broker.py:319-335`), and the journal prints which of the two names matched
(`ycharts/generate/resident_worker.py:122-128`). Every eviction line in the journal reads EVICTED. So by the vendor's
own message the stored sessions were displaced by another sign-in on the same account. They did not expire.

**2. What keeps the session alive between jobs.** Nothing, and by design. Between jobs the resident only long-polls
its queue (`resident_worker.py:467-469`). Inside a job, `guard()` renews three Opal-side things -- the job lease, the
queue visibility and the operation lease (`resident_worker.py:102-114`, `:111`) -- and none of them calls the vendor.
A sign-in runs in exactly two places: when no session is configured (`:188-191`) and after an eviction verdict
(`:140-149`). The two legacy schedules are DISABLED live (`ycharts-session-probe-schedule`, every 6 hours, last log
2026-09-24T00:00:38Z; `ycharts-session-capture-schedule`, every 72 hours, a function with no log stream). The host
carried 0 timers at 04:41Z today (this seat's earlier read; not re-read, per the ask).

Age is not what kills a session here: the version stored 2026-09-27T02:02Z produced a READY report on 09-29 at
about 14:1xZ, some 60 hours later, and was read EVICTED later in that same window.

**3. Which other caller could sign in with the same account.**

| Caller | Signs in? | Evidence |
|---|---|---|
| the host wrapper, run by the resident or by an operator | YES -- the only programmatic sign-in in the estate | `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js:113` reads `ycharts/login/credentials`; `acquireSession` `:960`; invoked at `ycharts/session/host_capture.py:69` |
| a person on the same seat | YES, by the design's own statement | `ycharts_session.js:35-45`: "Alyssa (a person) and this automation share ONE YCharts seat and can evict each other ... An eviction mid-session is EXPECTED (Alyssa signs in)"; PRD FWD-4: "mutual displacement with the shared vendor login is ACCEPTED" |
| `ycharts-session-capture` (the legacy sign-in function) | could; never has | no log stream; its schedule DISABLED |
| the gateway's YCharts client, the market-data pull, the session probe, the stress-test runner | NO -- they replay a stored cookie | `infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py` and `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py:39` read `ycharts/credentials`; that secret is unchanged since 2026-07-01 and last read 2026-09-23 |

Not read: whose account `ycharts/login/credentials` holds (Andrew replaced it on 2026-09-11; the record keeps no
identity), and whether the legacy cookie in `ycharts/credentials` belongs to the same account.

## What this means for a scheduled refresh (PROPOSAL -- the CTO rules)

A scheduled refresh is not indicated by this evidence, for four reasons.

1. The sessions are displaced, not aged out. A refresh on a clock does not stop the next displacement.
2. Each scheduled sign-in is itself a concurrent sign-in: it puts the person off the seat, and her next sign-in puts
   the automation off again.
3. The ratified text forbids it: PRD FWD-4, "no competing refresh schedule is created".
4. The sign-in is the hop that fails. The resident already signs in at the moment it is needed; that sign-in has
   failed on every recorded resident run (J2: 0 of 7 refusal-free). A schedule would run the same failing act.

## Start-to-finish walk

### 1. Sign-in -> the stored session -- INCOMPLETE

What exists: `run-ycharts-session.sh` sources the secret names and runs the library's `probe` task; the library signs
in through a browser, reads the identity, and publishes a fenced bundle (`persistSession`, `ycharts_session.js:1334`,
refusing a write behind the stored fence). Three versions exist: 2026-09-24T08:56:48Z, 09-27T02:02:24Z,
09-30T04:58:23Z.

The exact gap: the one version whose origin is recorded was an operator run. No resident-run capture is recorded as
succeeding.

Close: J2's recommended run, once, in the resident's own context.

### 2. Stored session -> the resident's first read -- WORKS

`resident_worker.py:187-196`: read the bundle's state, acquire a fenced transport, then `recipe.step_identity`, the
first call that tests the seat.

### 3. Between jobs -- no keep-alive, by design

See answer 2. Not a gap to close: closing it is the scheduled refresh the PRD forbids.

### 4. The eviction verdict -- WORKS

See answer 1. The library on the host carries the same predicate (`ycharts_session.js:573-578`, "403 + concurrent
sign in -> EVICTED_HARD (someone took the seat)").

### 5. Verdict -> re-login -- INCOMPLETE (the failing hop)

What exists: one durable refresh per job (`resident_worker.py:140-143`), a 900-second cooldown and a provider lease
around the capture (`host_capture.py:125-151`).

The exact gap: the re-login fails `AUTH_FAILED` and the reason is discarded twice. `failure_code()` keeps the class
and forwards a `reason` only when the record carries a closed token (`host_capture.py:25-47`); the four `AuthError`
sites carry none (`ycharts_session.js:1033`, `:1111`, `:1135`, `:1262`). And the wrapper's stderr goes to
`/dev/null` (`host_capture.py:70`).

Close: a closed `reason` token on each `AuthError` site, so the journal names the step. Proof: one failed capture
prints `CAPTURE_FAILED:AUTH_FAILED:<REASON>`.

## Two things found that the ask did not name

**A candidate the J2 note does not list: our own failed sign-ins.** A capture that gets past the password form but
fails the library's own recognition of the next screen (`:1111`, `:1135`) is still a sign-in to the vendor. It would
displace the stored session and publish nothing, leaving a dead session for the next job. This predicts the pattern
after any failed capture. It does NOT explain the latest case: no capture is recorded between the 09-30 04:58Z
version and today's 07:33Z read. INFERRED from the code path; not exercised.

**The upload's vendor lookup succeeded on the stored session 11 seconds before the verdict.** The resident resolves
an upload's tickers with a live `GET /securities/securities_info` through the same stored session, with no cache
(`resident_worker.py:369-370`; `intake/resolution_broker.py:14`, `:48-56`, which requires a 200 JSON reply and no
login redirect). Today the journal reads `RESOLVE state=READY` at 07:33:21Z and `EVICTION verdict=EVICTED` at
07:33:32Z. Window 24 shows the same order (NORMALIZED, then ATTENTION). Two readings stand: that route answers a
displaced session anyway, or the session was live at :21 and displaced by :32. The operator run J2 recommends
separates them, because the library probes the stored bundle at rest before it signs in (`ycharts_session.js:1424-1431`).
Also: J2's count of the attempt's vendor calls omits this lookup.

## Recommended completion sequence (PROPOSAL)

1. J2's one operator run in the resident's context, reading the stored bundle's probe result BEFORE the sign-in.
2. The `reason` token on the four `AuthError` sites, in the next resident build.
3. The seat question to Andrew: one shared seat means every job can be displaced by a person at any time, and every
   automation sign-in displaces her. The market-data client's own header says its work "stays frozen until the
   dedicated YCharts seat lands (Andrew procurement)" (`ycharts_client.py`, module docstring).
4. No schedule.

## Acceptance

One trace of one job on a session the resident did not just create: the stored bundle's probe at rest, the identity
read, and either a report or a named sign-in step.

## Evidence anchors and limits

Source read at CLOUD HEAD at 08:0xZ; AWS metadata read 08:08:35Z, in
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ycharts_session_trace_20261001/EVIDENCE.json`.

Limits. The deployed resident's bytes were not re-read for this ask (no host command); the file:line citations are
CLOUD source, and the root named in J2 (`36dfa80058-st6`) was installed after this seat's 04:41Z digest read. The
CloudTrail read could not see `GetSecretValue` calls -- its positive control (the resident's read at 07:33Z) is
absent from the result -- so it says nothing about who read the login secret. Who signed in to the vendor is not
readable from Opal's side at all: it is the vendor's knowledge.

- `infra/aws/lambda/investor-reporting/ycharts/session/{controller.py,broker.py,resident_session.py,host_capture.py}`
- `infra/aws/lambda/investor-reporting/ycharts/generate/{resident_worker.py,resident_main.py}`
- `infra/aws/lambda/investor-reporting/intake/{resolution_broker.py,security_resolution.py}`
- `infra/aws/ec2/investor-reporting-ycharts/{run-ycharts-session.sh,ycharts_session.js}`
- `infra/aws/terraform/ycharts-pipeline/eventbridge.tf`
- rows S207, S218, S225, S230, S233 of the IRPT_BCKEND surprise channel

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z, recorded in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
this surface reached this seat as msg 103617.

> You have 4.0.0_SA_CRO~X as your research partner so as you see projects developing, if you assess there needs to be
> higher resolution on any part of the development process, you have CRO~X run /closer trace on the given surface and
> assess the strategic way forward.
