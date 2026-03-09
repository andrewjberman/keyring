# COO Decision Log: ADVI_NNAVAR Production Rebuild Authorization
**Agent:** 2.0.0_SA_COO
**Date:** 2026-03-09
**Re:** ADVI_NNAVAR -- investigation closed, rebuild bundle finalized, Andrew decisions logged

---

## Investigation Status: CLOSED

The ADVI_NNAVAR investigation is complete across five phases. All decisions below
are final and authorized by Andrew (CEO/owner) in COO session 2026-03-09.

---

## Decision 1: Correlation Target -- WITHDRAWN

**Decision:** The r>=0.50 PRD correlation target is withdrawn. Correlation improvement
is not a goal of the production rebuild.

**Rationale:** The -$119M volume gap vs Schwab was explained in Phase 5 as a
definitional split: "Holding market value withdrawn" records 49F client departures to
other Schwab-custodied advisors. 49F correctly counts these as NNA outflows; Schwab
does not (assets stayed on platform). This gap will persist structurally at
~$100-130M/year and is correct behavior by design.

The remaining correlation gap (production r=0.329 vs ceiling r=0.448) is a function
of timing definitions: BD records Transfer In/Out at settlement date; Schwab books
at ACAT initiation (~25-30 days earlier). Andrew's decision: use BD settlement date.
This is defensible (BD-native) and not worth chasing with Schwab TOA data.

**Correlation improvement (cap tuning) is NOT part of the rebuild bundle.**

---

## Decision 2: ACAT Integration -- EXCLUDED

**Decision:** Do not include ACAT integration in the rebuild.

**Rationale:** ACAT was designed to close ~$45.98M of the volume gap by adding ACAT
inflow events to gold NNA. The gap is now confirmed as correct behavior -- not missing
inflows. Including ACAT would artificially inflate gold NNA by ~$46M, producing a
worse result than current production.

---

## Decision 3: JNL/Sweep Canonical Fix -- INCLUDED

**Decision:** Include commits 9bfb289b + b4f2d7a7 in the rebuild.

**Rationale:** These commits exclude the following from NNA computation in scripts
05 and 05b:
- JNL-LONG / JNL-SHORT: internal position journals (assets moving between BD accounts
  within the same custodian, not real custodial transfers)
- TRF BTWN SCH ACCTS: Schwab-to-Schwab internal transfers
- SEP sweeps (TO SEP ACCT MGR): operational sweep movements
- FDIC bank sweeps (TRANSFER FUNDS TO SCHWAB BANK): automatic cash sweep to Schwab Bank

These are not real NNA events. Schwab explicitly excludes all of them from its own NNA
definition. Their presence in production is noise that inflates gross inflows and outflows
without affecting the 49F-correct "Holding market value withdrawn" outflows. Including
this fix moves our NNA definition into alignment with Schwab's on this specific point
and does not disturb the $119M definitional gap.

---

## Decision 4: Cap Settings -- PRODUCTION UNCHANGED

**Decision:** Rebuild using existing production cap settings: AUA threshold 1.0x,
velocity window 90d, velocity threshold 1.0x. No cap parameter changes.

**Rationale:** The investigation confirmed the production cap configuration (aua_t1p00
+ vel_w90_t1p00) produced the -$119M result that was confirmed correct. Both caps
are doing legitimate work:

- AUA cap: removes BD phantom withdrawals. Without it, the gap explodes to -$540M.
  Essential data quality gate.
- Velocity cap: catches burst aberrations the AUA cap misses (cumulative over 90 days
  rather than per-event). At production settings it moved the gap from -$168.6M to
  -$124.7M -- in the direction of the correct answer. This is evidence it is suppressing
  aberrant transactions, not real NNA.

The DS analysis characterized the velocity cap as "over-suppressing real NNA" relative
to the correlation ceiling, but that framing was correlation-driven. From a magnitude
standpoint, the production vel cap helped land the correct result. It stays.

---

## Rebuild Bundle (Final)

| Change | Include | Notes |
|--------|---------|-------|
| JNL/sweep canonical fix (9bfb289b + b4f2d7a7) | YES | Cleaner NNA definition, removes non-NNA noise |
| AUAVAR BKF forward-fill fix (91b1918a) | YES | Already deployed to EC2; activates on rebuild |
| ACAT integration | NO | Would inflate NNA incorrectly |
| Cap tuning (vel/AUA parameter changes) | NO | Production settings produced correct magnitude |
| Settlement date (settle_date column) | NO | Timing not a goal; BD settlement is the correct choice |

Note: The AUAVAR BKF fix (Script 02) is a separate pipeline script already deployed
to EC2. It activates in the same gold rebuild as the NNAVAR changes since both feed
the gold layer. One rebuild covers both.

---

## Post-Rebuild Verification

After the gold rebuild completes, DT should confirm:
1. NNA gap vs Schwab is approximately -$119M (within normal variance band)
2. "Holding market value withdrawn" outflows are still present and correctly counted
3. JNL/sweep rows are absent from the NNA flow computation (check stdout exclusion count)
4. Gold AUA has increased by ~$27-33M (BKF forward-fill, AUAVAR fix)

---

## Authorization

Andrew authorized all decisions above in COO session 2026-03-09.
Rebuild can proceed. DT task order to follow.

---

## Files Produced This Session

| File | Action |
|------|--------|
| This file | COO decision log |
| `org/projects/ADVI_NNAVAR.json` | Status updated to closed, rebuild authorized |
| `org/daily_log/2026-03-09.md` | New daily log with this session entry |
