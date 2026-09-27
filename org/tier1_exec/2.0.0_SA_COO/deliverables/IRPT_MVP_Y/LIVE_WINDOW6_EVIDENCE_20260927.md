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
