# Window 6 (the Analysis chain): upload and submission pass live; the job stalls at the vendor session, then is stranded by the principal delete

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~00:5xZ.

Packet: `IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W6_20260926.md` @e9c283801f, blob `fffdca65`. The CTO half is
6b05ea31b4 and the CRO half e5433fd433.

Order: Andrew at the ~Y terminal, 00:09Z, "run the Analysis window now". The principal was `irpt-uiwalk-1790464832`,
with the password read by name from SSM, never printed.

## What ~Y did (exactly two POSTs, no retry)

| Key | Time | Answer | Evidence |
|---|---|---|---|
| K4 `POST /analysis/inputs` (aapl-vnq-12.03.csv, cottonwood) | 00:10:04Z | 200 RESOLVING, then **NORMALIZED** | `UP-bf61a07c..`, input `portfolio_4c5c85d0352dc8a9999f17ef77d2856d339d5aa46f6591b144d4b2951ce8044e`; `LIVE_UPLOAD_1203_20260926_W6.json` |
| K5 `POST /analysis` (Overview, report_title null) | 00:12:05Z | **200 QUEUED**: hop 3 passes live for the first time | `REQ-3a1b73a8dead02a17a09043b`; `LIVE_SUBMIT_1203_20260926_W6.json` |

Both logs are credential-scrubbed: 0 password values and 0 bearer or JWT tokens, read before commit.

## What the resident did (read-only observation)

The resident journal shows `retained_for_retry` at 00:12:10, 00:27:08 and 00:42:08Z, and no other lines for this job.

The job row has stayed `SUBMITTING`, `job_detail {operation: session_refresh}`, with `intent_session_refresh` claimed
at 00:12:08Z and no checkpoints. So **no vendor write happened**: no holdings upload, portfolio or report.

### Receive 1 (00:12:08Z): the session capture failed on the host

- `run()` reached the vendor session and claimed the one-time `session_refresh` intent (`resident_worker.py:74` or
  `:121`).
- `HostCapture.capture` passed its checks: the pins match (wrapper `55ddb8f7..` and library `dfc87d83..` on the host
  equal the bindings), `secret-ids.env` is present, and spacing and cooldown pass. It set `capture_not_before` and
  reserved `in_flight_until` 00:26:09Z.
- It then ran `/opt/investor-reporting-ycharts/run-ycharts-session.sh`. The Node runner took its own lease (`_opal` /
  `ycharts-session`, fence 11 to 12) and released it, and within about 2 s the capture raised.
- stdout is kept only on success and stderr is discarded by design (`host_capture.py` `run_capture`: `stderr=subprocess.DEVNULL`), so the reason is not on
  record.
- Ruled out, read-only on the host:
  - node v18.20.8 is on `/usr/bin`;
  - `playwright` resolves in `/opt/investor-reporting-ycharts`;
  - `aws` is at `/usr/bin/aws`;
  - **headless Chromium launches and renders** as ec2-user (no navigation, no vendor call).
- Not ruled out: anything inside the runner after its lease, such as reading the sign-in secret, the sign-in page or a
  challenge. Finding it needs one wrapper run, which is a live YCharts call on P's host and needs Andrew's per-use
  word.

### Receives 2 and later (00:27:08Z, 00:42:08Z, then about 00:57Z and 01:12Z): stranded by the principal delete

- `resident_worker.py:274-281`: on every delivery, `principal("start")` reloads the submitter's CURRENT profile row
  (`profile_for`) and replays `decide(...)`, **before** `store.claim()`.
- P deleted the principal at 00:21:32Z, at the packet's 60-minute life. So every later delivery raises there and is
  retained, with the row untouched.
- After the 5th receive (about 01:12Z) the message goes to `irpt-generation-dlq`, and the row stays `SUBMITTING`.
- Even with the principal alive, the job could not finish: the one-time `session_refresh` intent is spent, so the next
  pass would end ATTENTION `SESSION_REFRESH_ALREADY_USED`.

## Findings for the next window

1. **The packet's branch (e) premise is false for this code.** "A job still running at delete time continues
   server-side (the resident needs no principal)" is wrong: the resident re-grades the submitter's current profile at
   every delivery and phase. A window must keep its principal alive until the job is terminal, or the resident must
   stop needing a live profile. That is a design question for P and the CTO.
2. **The vendor session is the live blocker at hops 5-6.**
   - The offline pre-flight replayed the session bundle and never ran the host capture.
   - `ycharts/session/current` was last changed 2026-09-24 (about 2.6 days ago).
   - The first identity read evidently required a refresh, and the capture fails within 2 s for a reason the design
     does not log.
   - The next act is one diagnostic wrapper run, on Andrew's word, by the host's owner, with the capture's output kept.
3. The job, the vendor objects and the rows written so far are retained per the packet. There is nothing to roll back:
   no vendor write happened.

## Receive-1 capture failure: static causes ruled out (01:3xZ, read-only, no YCharts contact)

| Checked | Result |
|---|---|
| Host role `irpt-ycharts-runner-role`, simulated on the runner's own AWS CLI calls | 8/8 allowed: GetSecretValue on login, session and kimi; PutSecretValue and DescribeSecret on session; DescribeSecret on login; DynamoDB UpdateItem and GetItem on irpt-jobs. The DeleteSecret control is implicitDeny |
| Secrets' KMS | the default key (KmsKeyId None), so no grant is needed |
| `secret-ids.env` | ASCII with LF endings, 240 bytes; the sourced names are exactly `ycharts/login/credentials`, `ycharts/session/current` and `astn/kimi/api-key` |
| Login secret shape (keys and non-empty flags only; no value read out) | a dict with `password` and `username`, both non-empty. So `acquireSession`'s three pre-browser AuthErrors (`:956-966`) cannot fire |
| Session secret shape | `schema_version` 1, fence 11, captured 2026-09-24 04:56Z. The Python broker reads it OK, so the first identity step found it evicted and triggered the refresh |
| Egress | DNS resolves ycharts.com; HTTPS to checkip.amazonaws.com returns 200 |
| Runtime | node 18.20.8, playwright resolves, headless Chromium launches and renders |

What remains is the runner's live interaction with YCharts after its lease: seeding the stored cookies, the probe, the
sign-in form, or a challenge. Only a run whose receipt is kept can name it.
`P_RESIDENT_RETAINED_REASON_20260927.patch` (Y branch 9c6626e1be) makes the next attempt's journal line carry the
runner's `failure_class`.

## S151: the one wrapper run (02:02Z, Andrew-direct via CTO 101694, "yes on the YCharts wrapper run, one run")

Ledger `irpt-ycharts-wrapper-run-s151-20260927`: opened @b778f918a2 before the run, and CLOSED with proof.

The run: ONE `run-ycharts-session.sh` (task `probe`) as ec2-user on i-0167fd745ad906a66, SSM `29cacb70`,
02:02:13-02:02:25Z. There was no retry and no vendor write.

| Measured | Result |
|---|---|
| Wrapper exit | `WRAPPER_RC=0` |
| Receipt (scrubbed: fields only) | `ok: true`, `result {authenticated: true, reason: OK, http_status: 200}`; steps `CH-SIGNIN_FORM`, then `CH-AUTHENTICATED` (a form sign-in, no challenge) |
| Runner lease `_opal`/`ycharts-session` | fence 12 to 13, released |
| `ycharts/session/current` | `02e53a44` (fence 11, 09-24) to **`d38f6941` AWSCURRENT** (fence 13, captured 02:02:23Z, 31 cookie names); `02e53a44` is now AWSPREVIOUS |
| Queue `irpt-generation` | 0/0 before and after |
| The resident service's environment | `HOME=/home/ec2-user`, PATH including `/usr/bin`, `USER=ec2-user`: the same context as this run |

**The cause of receive 1 is not reproduced.**
- The same wrapper, host and user, with the same environment, IAM, secrets and runtime, now signs in through the form
  in 12 s.
- The 00:12Z failure is therefore not a standing defect of the host, wrapper or configuration. It fits a transient
  YCharts-side screen on that attempt, for example a sign-in or WAF page the runner did not recognise.
- It is unmeasured, because that run's receipt was discarded.

**S151's hazard disarms:**
- The capture path is proven working live.
- A fresh session (fence 13) is published, so the next job's identity step should not need a capture.
- The resident now runs the retained-reason patch (`fe64236bbb-rr`), so any recurrence names its `failure_class` in the
  journal.
