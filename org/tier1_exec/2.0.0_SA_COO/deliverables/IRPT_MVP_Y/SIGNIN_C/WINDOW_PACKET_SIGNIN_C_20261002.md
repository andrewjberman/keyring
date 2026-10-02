# Window packet -- sign-in option C: leg S (ONE scripted operator sign-in on the st12 host), then leg J (ONE job) only if S authenticates

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~09:4xZ.
**Authority:** CTO rulings batch 131 items 1-2 (C now: ONE scripted leg S inside a window packet, the queue 0/0 and no
non-terminal job, a CAPTCHA a clean refusal, no retry, no second leg S inside 24 hours) and batch 130 (the first job runs
after the new session reads back with its higher fence). Vendor authority as batch 131 reads it: leg S is the host's own
sign-in (Andrew's standing word of 2026-09-23 item 3; batch 88 item 3's 24-hour clock has passed since 2026-10-01T08:21Z).
Leg J is one attempt inside his word of 2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`).
**Ledger:** `irpt-signin-c-20261002` (S1, J1, J2, J3). **Runner:** `live_walk/signin_c_run.sh`, which hands to the hop-8
runner's legs S and J with this window's folder, root (`/opt/irpt-resident/cf3ae52aee-st12`), base (`SC_overview_cottonwood`)
and ledger. Its `--plan` at 09:4xZ: running root `cf3ae52aee-st12`, 0 non-terminal jobs, `irpt-generation` 0/0, dead-letter 0/0.

## Leg S -- one sign-in, no probe first

- **What runs:** `live_walk/leg_s_host.sh`, sha256 `c2ec45793fbfbabe632d9450d355aa4ec88beb3f66c80a87bb1d0acbacf14251`. These are
  the same bytes as the 2026-10-01 leg S that signed in, and that the HOP7B CTO half read in full. It runs the wrapper
  `run-ycharts-session.sh` (task `probe`) ONCE in the resident unit's context, bounded to 240 s. It prints a redacted
  receipt and `LEG_S_VERDICT=`.
- **No leg P:** batch 127 says no probe precedes a job, and the session's last reading is the resident's own:
  - EVICTED 06:26:09Z;
  - its refresh refused `CHALLENGE_CAPTCHA_UNSUPPORTED` at 06:26:18Z.

  `signin_c_run.sh` writes that citation, not a reading, as the hop-8 runner's leg-P file (`PROBE_VERDICT=NOT_LIVE:
  EVICTED_0626Z_NOT_PROBED`), so the runner's gate admits leg S.
- **Taken by the library:** its own fenced publication (the `_opal` / `ycharts-session` lease row), which raises the
  fence above 21.
- **NOT taken:** the resident's Python-side provider lease, as on 2026-10-01. Batch 130's condition is met by the solo
  gate instead: with no job and both queues empty, no resident request is in flight, so no st12 rotation write can be
  in flight.

**Branches (ONE sign-in in every branch):**
- **(i) AUTHENTICATED:** `ycharts/session/current` gains one version with a higher fence; the old one becomes AWSPREVIOUS.
  Leg J follows after at least 600 s (the runner refuses sooner).
- **(ii) FAILED** (not a challenge, no receipt, or the 240 s bound): nothing is written. The window ends.
- **(iii) CHALLENGED:** no attempt to answer. Nothing is written. The window ends. Option A becomes the path (batch 131
  item 3).
- In (ii) and (iii): no further host sign-in for 24 hours (batch 131 item 2).

## Leg J -- one job, only on branch (i)

**What runs:** the shape of the hop-7, hop-8 and hop-3 jobs, unchanged:
- principal `svc-irpt-analysis@opalinvest.com`, Cottonwood;
- ONE K4 POST of `aapl-vnq-12.03.csv` (35 bytes, sha256 `bb079cbf..0960ddc`);
- ONE K5 POST (`overview`, no comparison key);
- no retry; a 60-minute deadline.

**Write set:**
- in Cottonwood's partition: the upload, input, composition, request and job rows and objects;
- at the vendor, the calls of one Overview: two symbol resolutions, one holdings upload, one model portfolio, its
  status and settings reads, one report generation, one PDF download;
- on READY: the retained vendor PDF, the extraction evidence and the certified report.

**New on st12:** if the vendor rotates a cookie during the job, `ycharts/session/current` gains a version with the
SAME fence and generation, and the journal carries `IRPT_SESSION_ROTATION kept=1 names=<names>`. This is st12's live
proof when it happens. A job with no rotation proves nothing about st12 either way, and the outcome says so.

## Stops

1. Both halves at HEAD naming this file's blob, before either leg.
2. Before EACH leg, the root gate (`cf3ae52aee-st12`) and the solo gate: no non-terminal job, `irpt-generation` 0/0,
   dead-letter 0/0.
3. Leg S is run ONCE; the runner refuses when its output exists. A CAPTCHA ends the window.
4. Leg J: ONE Opal login, EXACTLY one K4 and one K5, no retry. If the upload does not read NORMALIZED, K5 is not made.
5. If leg J reads EVICTED on a session minutes old, that is the window's main finding. It is reported before anything
   else. The resident's one refresh allowance is then its own sign-in, which would meet whatever the vendor shows. The
   sign-in budget of item 2 above applies after it.
6. At leg J's 60-minute deadline, a job still non-terminal is reported to `1.0.0_SA_CTO` before anything is posted or
   redriven.
7. The output files are read for any cookie value, token or password-shaped string before they are committed (as the
   HOP7B half's item 8).
8. Any deviation not named here stops the window for a new half.

## What is read afterwards

- **S1:** `SIGNIN_C/LEG_S_OUTPUT_20261001.txt` (the runner's file name): the verdict by name, the redacted receipt, and
  the stored session's dates and fence after the sign-in.
- **J1, J2, J3:** the two POSTs; the terminal state with the journal, including `IRPT_SESSION_ROTATION` lines and the
  secret's version list; both queue depths. On branch (ii) or (iii), each closes NOT RUN with S1's verdict.
- **On READY:** the Analysis thread has re-run on st12. `2.0.0_SA_COO~D` may walk it.

## Rollback

None for a vendor call that was made. On branch (i), the prior session stays as AWSPREVIOUS (it reads EVICTED). Opal rows
are append-only records of the attempt.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~09:4xZ, on this packet's bytes at the commit that carries it. Read before signing:
- `signin_c_run.sh` hands to `hop8_run.sh` unchanged. Its one addition is the leg-P stand-in file, which carries a
  citation, never a reading.
- `hop8_run.sh` was read in full: one sign-in, one job, each refusing on a second run, and the 600 s spacing.
- `--plan` passed both gates at 09:4xZ with no vendor call.

## CTO half -- 1.0.0_SA_CTO

(not signed)
