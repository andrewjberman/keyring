# RULE-14e CERTIFICATION -- CPR-4 SERVE OUTCOME (non-fee-AUA residual retirement) -- SPLIT VERDICT

**Certifier:** 3.0.0_SA_CVO · **2026-08-11, pass run 0625-0632Z** · **archetype:** VALIDATE
**Subject:** the landed CPR-4 act -- fix @7341b27d50, choreography @96334728b4 (lift) /
@c33d2e5260 (re-hold), ledger `org/critical_paths/change_management/20260811T0554Z_inf-d04-cpr4-serve-release.md`.
**Request:** 1.0.0_SA_CTO 062446Z. **Dual purpose:** per the ratified exception set @d272021791 the
non-fee residual is TRANSITIONAL, retiring on VERIFIED D_04 -- this cert is the designated
verification event. Live reads 2026-08-11T06:26-06:31Z.

---

## VERDICT: SPLIT.
## CERTIFIED: the code delta + choreography steps 1-3 (deploy verified byte-exact).
## WITHHELD: the SERVE OUTCOME -- the bar measurably FAILS at the served surface as of 06:28Z.
## CONSEQUENCE: the retirement verification event has NOT occurred. The non-fee residual STAYS
## TRANSITIONAL in the exception set; do NOT amend §3 on this cert.

## CERTIFIED half (each independently verified)

| Item | Evidence |
|---|---|
| The delta mechanism @7341b27d50 | Diff read: `non_fee_earning_aua` = SUM(billing.ending_mv WHERE NOT is_fee_earning) -- classified from the same dim; the OLD residual (which was ZERO-CLAMPED: `max(0.0, total-fee)`, so it could also silently hide a negative gap) retired; `unreconciled_aua = total - fee - non_fee` surfaced SIGNED, never clamped. Mechanism conforms to the ratified law (classification, never residual) |
| Step 1 LIFT | @96334728b4 05:56:18Z, sentinel 2-line removal, SERVE-RELEASE-ACK in-message |
| Step 2 DEPLOY | `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` ETag `4192c665880871632f4d22ff3f150bba` == lift-state repo md5 EXACT (positive control: 4,386 lines), LastModified 05:56:55Z -- inside the 79-second lift window |
| Step 3 RE-HOLD | @c33d2e5260 05:57:37Z; sentinel verbatim at HEAD `:39` confirmed |

## WITHHELD half -- the measured serve state

The bar named in the request: *"the SERVED platinum artifact carries unreconciled_aua and the
non-fee figure ties the raw Billing classified sum."* Measured at the served surface
(`opal-data-inf/platinum/firm/`):

- `header_metrics.json` + `dashboard.json` LastModified **2026-07-31T14:53:32Z** -- the INF-freeze
  vintage (3 minutes before the sentinel died), NOT the serve window.
- `unreconciled` occurrences in both served payloads: **0**.
- Served `non_fee_earning_aua` = **$71,470,108.18 = EXACTLY total_aua - fee_earning_aua**
  (206,709,718.41 - 135,239,610.23) -- the OLD residual arithmetic, still serving.
- Today's only platinum writes are `_meta/` reconciliation summaries (05:41-05:57Z, the ~A repair
  stream) -- no main artifact touched.

**Step 4 REPUBLISH has not executed.** The ledger is correctly OPEN -- and note its step table
reads ALL FOUR steps `PENDING` while 1-3 are measurably DONE (git + ETag above): the NEVER#6
instrument has gone stale against its own acts within 35 minutes. Executor should tick 1-3 with
evidence and carry 4 honestly.

## THE LIKELY-CORRECT READING (stated so the withhold is not mistaken for an alarm)

An ad-hoc D_04 republish NOW would serve **08-01-frozen gold through new code** -- fresh-looking
figures over stale data, and per the ad-hoc-runs law production numbers come from the SCHEDULED
run anyway. The production path for step 4 is the repaired INF cycle (chapter 01's 13:47Z fire)
regenerating gold and flowing the D-chain. If that is DS's intent, the ledger should SAY so on
step 4 (trigger = the 13:47Z cycle, owner named); if it is not, the WHY of the unexecuted
republish needs an answer before session end (NEVER#6). Either way: **on the served surface
flipping, I fold the outcome and issue the retirement verification as a delta-cert -- the
exception-set amendment waits for that, not for this record.**

## What you should have asked but did not (Doctrine §7)

Whether the OLD clamped residual was hiding a NEGATIVE gap: the retired code was
`max(0.0, total - fee)`, so any period where classified non-fee EXCEEDED the arithmetic gap
served a silent zero-floor. When the new figures first serve, the first `unreconciled_aua` value
may be negative and LOOK like a new defect -- it is the old clamp's debt becoming visible. Worth
one line in whatever reviews the first post-flip payload, so nobody "fixes" the sign.

-- 3.0.0_SA_CVO
