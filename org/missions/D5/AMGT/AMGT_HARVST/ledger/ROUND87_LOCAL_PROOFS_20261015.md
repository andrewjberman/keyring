# AMGT_HARVST round 87 -- the local proof per publisher on dell1 (addendum 3, step 1), measured by `2.0.0_SA_COO~W1`, 2026-10-15

**The rule (CTO addendum 3, step 1):** dell1 proves the publisher locally: one job ends `complete_candidates` with more than 0 accepted, with no upload. All jobs below were `python -m lib.opal_data_harvest run --tickers <T> --publishers <P> --max-jobs 1` from the main tree (the `run` command does not upload; `upload-harvest` was never run). The run records are under `.runtime/opal-data-harvest/runs/` on dell1 (gitignored); the copies committed are named in the right column.

| publisher | job (run record id) | ticker | status | accepted | how the session was obtained | committed copy |
|---|---|---|---|---|---|---|
| `wsj` | `20261015T161540Z-wsj-6e37d73e87` | BA | complete_candidates | 5 | scripts signed in; in-profile renew (`verification.renew`) | `ROUND86_FIRST_DELL1_READ_20261015.md` |
| `wsj` | `20261015T185613Z-wsj-6ee9e9f722` | BA | complete_candidates | 5 | stored token, expired profile, renewed in-profile by the worker (HVST-ca-1 AC3) | `deliverables/2.0.0_SA_COO_W1/round86/ca1_ac3_wsj_job_20261015T185613Z.json` |
| `wsj` | `20261015T194605Z-wsj-b45b24e31e` | COST | complete_candidates | 5 | profile already signed in; window minimised (HVST-cb-5 AC3) | `deliverables/2.0.0_SA_COO_W1/round87/cb5_ac3_wsj_job_20261015T194605Z.json` |
| `barrons` | `20261015T161808Z-barrons-cf237cfae1` | BA | complete_candidates | 5 | scripts signed in; in-profile renew | `ROUND86_FIRST_DELL1_READ_20261015.md` |
| `bbg` | `20261015T200625Z-bbg-557a6d83a4` | BA | complete_candidates | 5 | stored token `secrets:bloomberg/session` (2026-09-11); a Press and Hold 403 was met and solved (minimise call disabled for this run) | this file |
| `bbg` | `20261015T200945Z-bbg-a0af4c26a7` | COST | complete_candidates | 5 | the same stored token; no challenge met; window minimised | this file |
| `sa` | `20261015T201625Z-sa-a47056846d` | BA | complete_candidates | 5 | the profile `browser-profiles/sa` signed in BY ANDREW in a visible Chrome at 20:1xZ (no script can sign `sa` in: `verification.ACCOUNT_CHECKS` has no `sa`, and the Kimi-VL authenticator writes a bundle the tab never reads) | this file |

## What this establishes and what it does not

- **Establishes:** each of `wsj`, `barrons`, `sa` and `bbg` can complete a job on dell1 with more than 0 accepted. That is addendum 3's step 1 for all four. FT is Andrew's to provide.
- **Does NOT establish:** durability. How long the `sa` profile session lasts is unread; `sa` has no in-profile sign-in, so when it expires a person must sign in again (a candidate cell for a later round: an in-profile sign-in for `sa`). `bbg` ran on a Secrets session captured 2026-09-11 and met one Press and Hold in its first attempt: a first attempt (minimised, 19:50Z) died `TargetClosedError`, the next (minimise off) solved it, a third (minimised) met no challenge. A challenge repair in a minimised window is unmeasured; three samples cannot separate the window from chance.
- **Two failed attempts, for the record:** `20261015T192933Z-bbg-b857376c83` (`bot_check`, ChallengeFailed, before the minimise cell) and `20261015T195002Z-bbg-eb428d01cd` (`error`, `TargetClosedError`); each started a publisher cooldown that this seat honoured and did not clear.
- Nothing was uploaded. The jobs wrote local files under `.runtime/opal-data-harvest/` only.

-- 2.0.0_SA_COO~W1
