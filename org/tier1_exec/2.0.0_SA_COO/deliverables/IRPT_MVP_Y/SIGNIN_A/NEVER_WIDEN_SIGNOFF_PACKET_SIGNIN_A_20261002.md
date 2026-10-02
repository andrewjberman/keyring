# Never-widen sign-off packet -- sign-in option A: an attended sign-in path (the resident st12 -> st13 at CLOUD c657a5966d, carrying the library's attended hold, and a loopback-only display on the host)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~10:1xZ.
**Authority:** CTO rulings batch 131 items 3 and 4. The ruling's terms:
- a display on the host bound to localhost only, reached over a Systems Manager port forward (no inbound port, no
  public listener, no security-group change);
- a wait mode in the capture library that holds at the CAPTCHA for a person and publishes the session through the
  same fenced path;
- the display torn down after;
- no credential, cookie value or screen capture written to a log or a record;
- answering the CAPTCHA is Andrew's act, at a time he names, with the queue 0/0;
- if C succeeds, A still lands.

The exact-file grant for the test suite: msg 104154. **Ledger:** `irpt-resident-st13-20261002` (U1 proven; I1, D1, V1).
No IAM, Lambda, queue, table, schema or security-group moves. **No vendor call in this act:** the attended sign-in
itself is section 4's procedure, run only at Andrew's time.

## 1. What ships

**The library** (`infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js`; `9511060e..` becomes `857d90b8..`;
commit `8e385c08b2`, merged `c657a5966d`):
- `YC_ATTENDED=1` turns on a hold. It is OFF unless set, and refused before any secret read unless `YC_HEADLESS=0`
  and `DISPLAY` are set (`ATTENDED_REQUIRES_DISPLAY`).
- At a screen carrying the CAPTCHA signature, `holdForPerson` re-reads the screen every 2 s for up to
  `YC_ATTENDED_WAIT_S` (default 600, capped at 900). It clicks, types and captures nothing.
- When the signature is gone, the normal flow resumes: probe, identity, fenced publication.
- A wait that runs out is `CHALLENGE_ATTENDED_TIMEOUT` (`retried=false`).
- Bounds: at most 2 holds and ONE re-fill of the form after a hold. Only the CAPTCHA holds; a one-time code still
  fails at once.
- `record.attended` carries the holds: signature, milliseconds held, polls, the screen it cleared to.

**Test:** arm b2 of `tests/run_offline_suite.js` (`8be0144b71`, under the grant) has 4 cases:
- a person clears the CAPTCHA on poll 2, then one re-fill, then authenticated, with 2 credential submits;
- nobody answers: `CHALLENGE_ATTENDED_TIMEOUT` with 1 submit;
- a one-time code fails at once;
- no display: refused with 0 requests.

Arm b is the control: the same CAPTCHA with attended OFF fails at once. Arms a, b, b2, c, d and e all pass
(`node --require ./tests/netguard.js tests/run_offline_suite.js`, rc 0).

**The package.** Every member is at ONE commit, `c657a5966d`. Gate (`SIGNIN_A/GATE_OUTPUT_ST13_20261002.txt`): G1 244 of
244; G2 242 of 242; G3 99 of 99; G4 agree. G5, against the RUNNING st12 package (`rb_cf3ae52aee-st12.tar.gz`, sha256
`1d1ca782..`): **added 0, removed 0, changed 2** -- `ycharts-host/ycharts_session.js` and the bindings, which pin
the library's sha256 `857d90b8..`. **No resident Python member changes.**

**Artifacts:**
- Tar `irpt-resident-c657a5966d-st13.tar.gz`: sha256 `7c503923adc003a1fb02a8cb88c20bbe471fdb818bf122ee24aee62b0b3c08b9`,
  767,144 bytes, S3 version `0j0S_Qjp4yITyCLs8shW5MFXqjvVX3.L`.
- Install script `SIGNIN_A/resident_host_install_c657a5966d-st13.sh`: sha256
  `f7b9daba9b8c037696d4967c9d9077f0ffb4faeda662997dfcde7dd302a7ee12`, S3 version `79mHrL_O.wRCmmBD2581F98Q6goe2Jow`.
- Both keys read 404 before the upload, and both read back equal by version.
- Against st12's script, with root names normalized, the install script differs only in the tar pin, the library pin
  `WANT_LIBRARY` and the ledger slug. The script moves the host library to the package's pin, as every resident
  install has.

**The display:** `SIGNIN_A/xvnc_install_host.sh` (I1) installs `tigervnc-server-minimal` (or `tigervnc-server` if the
minimal package is absent). It enables no service and leaves nothing listening; it only provides the `Xvnc` binary.
Read at 09:53Z (`SIGNIN_PATH/HOST_HEADED_DEPS_READ_20261002.txt`): the headed Playwright Chromium (`chromium-1228`)
resolves every shared library on the host.

**The run's tools:**
- `live_walk/attended_signin_host.sh`: leg A, run only per section 4.
- `live_walk/host_read.py` gains `HOST_READ_TIMEOUT_S` (60 to 3600; default 600): the command's bound and the wait for
  it.

## 2. Blast radius, by branch

| path | BEFORE (st12) | AFTER (st13 + I1) |
|---|---|---|
| the resident's own capture (its one refresh) | headless; a CAPTCHA fails `CHALLENGE_CAPTCHA_UNSUPPORTED` | unchanged: `YC_ATTENDED` is unset in the unit's environment, so the hold is unreachable (arm b) |
| an operator's scripted leg S | as above | unchanged |
| leg A, the attended run (section 4) | no path | `Xvnc :1` on 127.0.0.1:5901 only for at most 840 s, as the resident's user; a headed browser on that display; a CAPTCHA holds up to 600 s for the person; ONE re-fill at most; fenced publication as leg S; the display killed after, with the port read empty |
| every other resident path (jobs, resolves, status) | -- | unchanged: no resident Python member changes (G5) |
| the host's packages | no VNC | one package and its dependencies installed; no service enabled; nothing listening outside a leg-A run |

**Who can see the display:** only a holder of an AWS identity that can open a Systems Manager session on
`i-0167fd745ad906a66`, the same set that can already run commands there as root. `-SecurityTypes None` adds no one to
that set, because the port is loopback-only (`-localhost`) and the script refuses to run if it binds anywhere else.
There is no inbound rule, no public listener and no security-group change.

**What is never written:** a screen capture (neither the library nor Xvnc records one); a cookie value or credential
(the receipt is leg S's redacted walk).

## 3. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. **I1, at any time** (no restart): `xvnc_install_host.sh` through Systems Manager. Read back: `Xvnc` present; 0
   enabled VNC units; 0 listeners on 5900-5910; the resident unchanged.
3. **D1, only after window C's leg J job is terminal**, and on the solo gate: no non-terminal job, `irpt-generation`
   0/0, the provider lease holder empty.
   - one `head-object` of the script key, printing `79mHrL_O..`;
   - the script fetched BY KEY on the host, its sha256 checked against `f7b9daba..`;
   - run through Systems Manager (`SIGNIN_A/install_fetch_and_run.sh`).
4. **V1:**
   - running root `c657a5966d-st13`;
   - host library `857d90b81960d69a..` (`YC_ATTENDED` and `holdForPerson` present);
   - resident Python digests unchanged: `operation_lease.py` `2519834356b2d7a4`, `transport.py` `d8cdbf3907a7d149`,
     `resident_worker.py` `93e50f0f148960ed`;
   - unit active and polling; queue 0/0; nothing listening on 5901.
5. The ledger closes at V1.

## 4. The attended sign-in (leg A), when it is needed -- Andrew's act, at a time he names

It is needed when a scripted sign-in (the resident's refresh or a leg S) ends `CHALLENGE_CAPTCHA_UNSUPPORTED`. Each run
is ONE vendor sign-in under Andrew's standing word of 2026-09-23 item 3, logged in this ledger family, and taken
with the queue 0/0 and no non-terminal job (batch 130). Batch 131 item 2's budget applies: no more than one host
sign-in in 24 hours after a challenged one, unless Andrew is at the display.

1. The operator runs `HOST_READ_TIMEOUT_S=1080 python live_walk/host_read.py live_walk/attended_signin_host.sh "..."`. It
   refuses before any vendor call if:
   - `Xvnc` is absent;
   - the library has no attended mode;
   - 5901 is already in use;
   - the display binds anywhere but loopback.
2. **Andrew, on his laptop** (both tools are installed there, read 2026-10-02: `C:\Program Files\Amazon\SessionManagerPlugin`,
   `C:\Program Files\TigerVNC`):
   `aws ssm start-session --target i-0167fd745ad906a66 --document-name AWS-StartPortForwardingSession --parameters "portNumber=5901,localPortNumber=5901" --region us-east-1`,
   then the TigerVNC viewer on `localhost:5901`. He sees the browser sign in by itself. If a CAPTCHA shows, he
   answers it; the library continues on its own and publishes. If none shows, the run completes with nothing for
   him to do.
3. The output is read for value-shaped strings before it is committed. `LEG_A_VERDICT=` names the outcome.

## 5. Rollback, per key

- **I1:** `dnf history undo <the transaction I1 prints>`; nothing else depends on the package.
- **D1:** root `cf3ae52aee-st12` and the library `9511060e..` stay on the host, and the script's rollback branch
  restores both.
- **Leg A:** none for a sign-in that was made; the prior session stays as AWSPREVIOUS.

## 6. Not claimed

- That a CAPTCHA answered through the display leads to a session: no real CAPTCHA has been met through it. The replay
  proves the hold, the resume and the bounds, not the vendor's CAPTCHA.
- That the vendor will not ask for a one-time code: that is still not handled, and fails explicitly.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~10:1xZ, on this packet's bytes at the commit that carries it. The write set is:
- one package (and its dependencies) on one host;
- one new resident root, the host library and the cutover receipt with its backup, and the unit's ExecStart;
- at a leg-A run only, a loopback display for at most 840 s and one fenced session version.

The blast radius is section 2, every capture path. The rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
