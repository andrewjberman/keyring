# How can the YCharts session be restored? No path exists today for "Andrew's sign-in through the CAPTCHA" -- reads only

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~09:3xZ. No vendor call, no sign-in, no secret value read. Asked of: `1.0.0_SA_CTO`.
**Why now:** every remaining Analysis act (st11's and st12's live proofs, the remaining arms in batch 61) waits on a live session.
CTO batches 120 item 7, 121 item 4 and 130 list the sign-in as Andrew's act. As far as this seat can find, nothing lets
him perform it.

## Measured

1. **The capture library refuses a CAPTCHA by design.** `ycharts_session.js:546` maps any page matching
   `captcha|are you a human|verify you are human` to `CHALLENGE_CAPTCHA_UNSUPPORTED`, and the run ends. Nothing waits for
   a person.
2. **The host has no screen a person can reach** (`HOST_SIGNIN_READ_20261002.txt`, SSM `9055904d`, 09:29:51Z):
   - Xvfb, x11vnc, Xvnc and noVNC are all absent;
   - `tigervnc-server` and `xorg-x11-server-Xvfb` are available from dnf;
   - headed Playwright Chromium `chromium-1228` is installed, and node is present;
   - the runner defaults to headless (`YC_HEADLESS=1`).
3. **The stored bundle must say `capture_origin: "EC2"`** (`generate/transport.py`, `_initialize_bundle`). A session taken in
   another browser does not fit the contract as written.
4. **Sign-in history on the host** (all of the resident's journal): 8 capture failures (4 `AUTH_FAILED`, 2
   `CHALLENGE_CAPTCHA_UNSUPPORTED`, 1 other `UNEXPECTED_CHALLENGE`, 1 `LEASE_NOT_HELD`). The last good session,
   fence 21 of 2026-10-01T08:21:20Z, came from **leg S**: ONE operator run of the same scripted wrapper, under Andrew's
   standing word of 2026-09-23 item 3 and a window packet with both halves (`HOP7B/OUTCOME_20261001.md`: signed in in
   10 s, no challenge). The first CAPTCHA came about 22 hours later, at 2026-10-02T06:26:18Z.

## Options

| | What | Cost | Unknown |
|---|---|---|---|
| **C** | ONE more leg S, the scripted wrapper as on 2026-10-01, inside a window packet. Taken with the queue 0/0 and no non-terminal job (batch 130's condition). It answers no CAPTCHA: if one appears, the run ends `CHALLENGE_CAPTCHA_UNSUPPORTED` and nothing changes | one window packet; one vendor sign-in under the standing word | whether the CAPTCHA persists or was a one-off risk score; a second refused attempt may raise that score |
| **A** | An ATTENDED sign-in on the host: a virtual display (Xvnc from `tigervnc-server`) and the wrapper run headed in a new attended mode that WAITS at a CAPTCHA (bounded, for example 10 minutes) instead of refusing. Andrew reaches the window from his laptop through a Systems Manager port forward and a VNC viewer, and answers the CAPTCHA himself. The library publishes the session as it always does: fenced, `capture_origin` EC2 (true), the resident's own IP | a library change (attended mode) and its test; one package install on the host (ledgered); a packet with both halves; on Andrew's laptop, the Session Manager plugin and a VNC viewer | Andrew's tooling; whether the vendor asks more than a CAPTCHA (a one-time code) |
| **B** | Andrew signs in on his laptop's browser, and the cookies are published from there | a contract change (`capture_origin` not EC2) and a new publication path | whether the vendor ties the session to the laptop's IP; NOT recommended |

## Recommendation

**C now, and A built in parallel.** C costs one sign-in and settles whether the CAPTCHA persists. A is the only path that
lets a person answer one with the session staying true to its contract. If C passes, A remains the fallback for the next
CAPTCHA. If C meets the CAPTCHA, A is the path, and it is ready sooner for having been started.
