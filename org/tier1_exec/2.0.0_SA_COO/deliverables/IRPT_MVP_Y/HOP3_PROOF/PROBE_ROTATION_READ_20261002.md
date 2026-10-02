# Did leg P's probe rotate the stored session? (CTO rulings batch 120 item 6; batch 126 item 2(b)) -- reads only

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~08:1xZ. No vendor call; no secret value read (version metadata and code only).

## Answer

**Very likely yes, and the cause is wider than the probe: no Opal path stores a cookie the vendor rotates.** INFERRED, not
proven: the cookie's name and the 403's cause were not recorded.

## Measured

1. **The stored jar has not changed since the last sign-in.** `ycharts/session/current` has 4 versions; AWSCURRENT `a47abdc2`
   was created at 1790842880 (2026-10-01T08:21:20Z), equal to every probe's `persisted_at`. Nothing wrote it after the probe.
2. **Today's probe was the first to draw a cookie.** Every leg P on disk, each followed by a job:

   | probe | set_cookie_count | the job after it |
   |---|---|---|
   | HOP7C 2026-10-01 08:55Z | 0 | reached the PDF (refused at the printed-type check) |
   | HOP8 10:47Z | 0 | reached the PDF (the same refusal, named) |
   | HOP8B 12:12Z | 0 | READY |
   | E3 15:15Z | 0 | READY |
   | HOP3_PROOF 2026-10-02 06:24:58Z | **1** | **EVICTED 71 s later** (`GET .../generate/14141822` 403, journal 06:26:09) |

   The fifth probe, about 22 hours after the sign-in, drew a `Set-Cookie`; the stored jar the job then used was refused.
3. **No path persists a rotated cookie.** `ycharts/session/deadline_transport.py:79-83` sets the cookies a reply returns into the
   in-process jar of THAT transport only; `put_secret_value` is called only by the capture (sign-in) path
   (`ycharts/session/broker.py:113`). The probe's process ended with the rotated cookie in memory, and the job built a new
   transport from the stored, now stale jar.

## What it means

- The probe consumed the session it reported on: batch 120 item 6's defect is real (inferred).
- The same loss would follow whichever request first meets the vendor's rotation, a job's included: that receive keeps the new
  cookie in memory and the NEXT receive starts from the stale secret.

## Recommendation (for the CTO)

1. Persist a rotated session cookie: when a reply sets a cookie the stored bundle carries, write the updated jar back to
   `ycharts/session/current` under the bundle's fence (a new version, the broker's existing write path, cookie NAMES logged
   only). This keeps the session through a vendor rotation for probe and job alike. A resident change with its own packet.
2. Until then, no further probe precedes a job: the job's own eviction verdict is the liveness read.
3. Record the cookie's NAME on a `Set-Cookie` in the vendor-request ledger (`vendor_ledger_record` holds only a count), so the
   next rotation is read, not inferred.
