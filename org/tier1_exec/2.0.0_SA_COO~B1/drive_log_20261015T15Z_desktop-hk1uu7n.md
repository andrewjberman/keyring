# 2.0.0_SA_COO~B1 drive log -- ADVI_FIRMBKTS, 2026-10-15 15:50Z to 18:30Z (substantive ticks)

**archetype:** COORDINATE. Times are UTC. Continues `drive_log_20261015T13Z_desktop-hk1uu7n.md`. Push state of the hashes below: LOCAL on `box/dell1` (not re-read against origin this tick).

## Re-seat after the box restart (15:49Z to 16:00Z)
- Startup: watcher armed (re-armed on each 30-minute expiry), registered as `2.0.0_SA_COO~B1`, session serial file written, owned-paths hook already wired, PATH check 102 of 102 comp-tools resolve bare. Inbox empty.
- `/canonical-drive ADVI_FIRMBKTS` armed at 60m (cron at :17, session-only) on the `LIVE_ARMS.md` row naming `~B1`.
- `0.7.0_AE_CloudOps~FB1` read NOT REGISTERED after the restart while holding `FB-l-5` (pending) and `FB-h-5` (parked). Pre-flight: process scan 0 hits, marker scan 0, windows 0 of 20, only this project's orders on the serial. Spawned it with a pointer hint (inbox and `FB-l-5`); LIVE at the next poll, WAITING on the first-day reads.

## Early evidence on the first catch-up fire (17:27Z)
- Read-only look at `/aws/lambda/inf-portal-publisher`, 16:25Z to 16:45Z on 2026-10-15: 8 events, no next token, one invocation `b86ad0ff`, `READINESS HALT: client_perf=2026-10-15 holdings=2026-10-15 canonical_nna=2026-10-14 served=2026-10-15 reason=not-after-served`, no write line, no second START.
- This is the publisher's own log. Not measured: that the served keys carry no new VersionId. It does not grade `FB-l-5` L4; the 2026-10-16 reads by 18:00Z stay the acceptance.

## Waiting
- Box queue: no open call for this project (every ADVI_FIRMBKTS row reads CLOSED). Free options: none. The wait is recorded with `unblock.py tick --wait-until 2026-10-16T13:30:00Z --owner 0.7.0_AE_CloudOps~FB1` (WAITING, count 0). A first attempt with `--owed-ledger` and a slug that is not an open ledger counted an empty tick (empty=1); the dated form restored the count to 0.
- Open: `FB-l-5` first-day reads 2026-10-16 (13:30Z publishes, 16:30Z halts with zero writes), by 18:00Z; then `MOVE_RECORD.json`, the graders, close, the round-8 packet to `3.0.0_SA_CVO`.

## Compiler Tools
Run: `drive-mode.py`, `open-calls.py mode get` and `list`, `unblock.py tick`, `to-check.py`, `comp-find`, read-only `aws logs filter-log-events`. Worked: the dated-wait form. Failed: `--owed-ledger` with a guessed slug read "ledger-not-open"; a piped `comp-surprise` call was refused by the rail and re-run unpiped. Gap: no instrument reads "served keys unchanged since time T" in one call.
