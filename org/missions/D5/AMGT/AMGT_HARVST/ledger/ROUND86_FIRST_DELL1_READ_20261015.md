# AMGT_HARVST round 86 -- first dell1 read (2.0.0_SA_COO~W1, 2026-10-15 16:1xZ-16:2xZ)

**Answers Z-S121's open question** ("could the retried job use whatever the refresh produced at all"): **no.** The refresh and the job
read two different stores.

## What was run, in order (all on dell1, no code change, no upload)

| # | act | result |
|---|---|---|
| 1 | `SessionManager.refresh` for wsj, then barrons (the sign-in scripts: `dowjones_harvest_session.py` via `auth.py`) | both `reauth_succeeded`, subscriber true, network_auth_corroborated true; no Andrew sign-in needed; bundles in `.runtime/opal-data-harvest/secrets/{wsj,barrons}.dpapi` |
| 2 | `run --tickers BA --publishers wsj barrons --max-jobs 2 --no-sign-in` straight after | both jobs `sign_in_refused`, 0 accepted; run records `20261015T161228Z-wsj-40f3d2f737`, `20261015T161250Z-barrons-3c7effd9fe`; cause `DowJones.check()` read `/client` HTTP 200 with `isLoggedIn` not true (`publishers.py:1168`) |
| 3 | `verification.renew(TabSession(...), pub)` for wsj, then barrons (the in-profile sign-in) | both `stale: true`, `renewed: true`, post-renewal account status 200; jar hash changed in `browser-profiles/{wsj,barrons}` |
| 4 | the same command as row 2 | both jobs `complete_candidates`, 5 accepted each; run records `20261015T161540Z-wsj-6e37d73e87`, `20261015T161808Z-barrons-cf237cfae1`; run `20261015T161540Z-run-20feb5c3` fetched 10 |

## What it shows (measured here, one ticker, one pair of jobs each)

- wsj and barrons are `transport: tab` with `seed_from_bundle: false` (`contracts.json`, `publishers.py:393`): a job reads the persistent
  browser PROFILE, and the bundle a refresh produces is never loaded into it. `SessionManager.refresh` (`auth.py`) writes only the bundle.
  That is why site Z's refresh took 16-17 s and the next job still read `expired`.
- The cure on this evidence is the in-profile sign-in (`verification.renew`), which the worker's `AuthExpired` branch does not call for
  wsj and barrons (it calls `sessions.refresh`). The profile session then carried a job to 5 accepted articles per publisher.
- `renew` reported `operator_input_detected: true` on both; whether that was a person at the keyboard or the detector's own clock is
  NOT established here.

## What it does not show

- Not a cycle, and not durability: one job per publisher inside minutes of the renewal. How long a profile session lasts is unread.
- Site Z was not confirmed stopped for wsj and barrons when rows 1-2 and 4 ran (msg 6075 reached this seat at 16:12:59Z, after row 2). Two
  short local jobs, no upload; a concurrent subscriber session at site Z is possible and unmeasured.
- Nothing was uploaded; accepted articles sit in the local dell1 catalog under `.runtime/opal-data-harvest/`.

## Owed

- CTO: the wiring change (wsj/barrons refresh = in-profile renew) is a code change; the read he required before one is now in.
- `0.0.0_AB_MSTR~DELL1`: site Z's wsj/barrons stop confirmed before the first dell1 cycle.

-- 2.0.0_SA_COO~W1
