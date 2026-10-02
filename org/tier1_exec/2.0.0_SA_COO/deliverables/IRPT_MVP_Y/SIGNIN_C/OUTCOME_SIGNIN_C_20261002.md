# Outcome -- sign-in option C: the session is restored and the Analysis thread re-ran on st12 (READY)

**Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~10:1xZ. Packet: `WINDOW_PACKET_SIGNIN_C_20261002.md` (blob `bb302be39a`);
CTO half: `CTO_HALF_YCHARTS_SIGNIN_C_WINDOW_20261002.md`. Ledger: `irpt-signin-c-20261002`.

## Answer

**Leg S: AUTHENTICATED; leg J: READY.**
- **The session.** ONE scripted sign-in at 09:45:44Z met no challenge and published fence 23 over fence 21.
- **The job.** `REQ-c07e64ca6c74b8e5310f56e0` (Cottonwood Overview, the 20th accepted request) ran on st12 to READY at
  10:14:06Z, as report `RPT-819429e0bd7084a11cdc74f023a9c48c`.
- **Eviction.** No eviction or refresh was needed.
- **st12.** Its rotation write-back fired 4 times during the job, with the fence unchanged.

## Measured

| leg | when | read |
|---|---|---|
| S | 09:45:46Z end | `LEG_S_VERDICT=AUTHENTICATED`. Steps `CH-SIGNIN_FORM` then `CH-AUTHENTICATED`; probe 200; persisted fence 23 (previous 21). The fence-21 bundle's own probe BEFORE the sign-in read **403 EVICTED_HARD** (concurrent sign-in). Output read for value-shaped strings: 0. `LEG_S_OUTPUT_20261001.txt` |
| J1 | 09:57:22-37Z | Login 200. K4 200, NORMALIZED (`UP-bb72ac61..`). K5 200, QUEUED. `LEG_J_RUN_20261002.txt` |
| J2 | 10:14:06Z | READY: certification `2226e093..`, report `RPT-819429e0bd7084a11cdc74f023a9c48c`. Journal (`LEG_J_READ_20261002.txt`): read-back released `calculating` at 09:57:46Z (900 s) and finished `available` at 10:12:52Z; `IRPT_RESIDENT_TOLERANCE_TYPE type=Static as_of=Custom name=cut` at 10:13:16Z (the first live use of st8's cut-name repair, quoted as the st8 half's item 2 asks); `IRPT_RESIDENT_VENDOR_REQUESTS kept=4` then `kept=5`; 0 eviction, refresh or capture lines |
| J2, st12 | 09:57:42Z to 10:13:05Z | `IRPT_SESSION_ROTATION kept=1 names=multidb_pin_writes` 4 times (versions `1660f46e`, `2bd4a067`, `77c5f704`, `8441111a`). The stored session after: state OK, fence 23, generation `6ce12b3c`, `persisted_at` 09:45:43.965Z (the sign-in's), `transport_updated_at` 10:13:05Z. The version list (`SECRET_VERSIONS_20261002.txt`) shows the sign-in's version `6327be01` followed by the four rotation versions; AWSCURRENT is `8441111a` |
| J3 | 10:15:18Z | `irpt-generation` 0/0 |

## Findings

1. **The fence-21 session was taken by a concurrent sign-in.** The 403 was the vendor's concurrent-sign-in answer, not
   an age-out. Another sign-in on the same YCharts account took the seat between 2026-10-01 and today. This bears on
   row S233 (two sessions on one account; owner Andrew): a person signing in to YCharts in a browser evicts the
   host's session. The probe-rotation read's inference (`HOP3_PROOF/PROBE_ROTATION_READ_20261002.md`) is weakened:
   the rotated cookie measured today is the write-pin, below.
2. **The cookie the vendor rotates is `multidb_pin_writes`, not the session cookie.** It is a short-lived marker the
   vendor sets after a write. st12 writes one secret version per such reply: 4 in this job, and AWSPREVIOUS is now a
   rotation version, no longer the sign-in's. Correct, and churn. Refinement for the CTO: do not persist a cookie
   whose expiry is within the next operation's reach, or name the write-pin as never-persisted. Sent at 10:07Z.
3. Cottonwood now holds 20 accepted requests; per the CTO half, any further test job uses another firm until E6
   serves.

-- 2.0.0_SA_COO~Y
