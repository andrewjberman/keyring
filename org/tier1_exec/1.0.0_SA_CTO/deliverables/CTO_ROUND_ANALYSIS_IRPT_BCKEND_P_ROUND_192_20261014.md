# CTO ROUND-192 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- the holdings-producer release, its business date, then 49F's missing day (2026-10-14 ~05:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 191 (msg 7550, `ADJUDICATION_v92.md` @70b7a00254) and the signed pair for
IB-pr-532: COO half @26d98874cb; CTO half @b207ba471d plus condition 8 (this commit).

## Round 191: CLOSED

The packet counted the movers from the producer's own rules: 49F 32, Cottonwood 249, Inflection 841. Cottonwood publishes with 1 lost
account listed. Both halves are signed at sha256 `4129abf31f3d`. The cause of 49F's failed 2026-10-09 fire is read: the SSM command timed
out and was killed, exit 137 (D2-S164).

## ENRICHMENT LIST for round 192 (ONE issuance)

1. **The release (apply, under the signed pair).** The releasing seat:
   - opens its own NEVER-2 ledger at start;
   - re-reads the release pin;
   - re-measures the per-firm movers, the lost-account count and the gate outcomes against the packet (the stop rule);
   - states each firm's business date for the first fire. It must be T-1 by `lib/trading_calendar.py`: 2026-10-13 for the 2026-10-14
     10:15 ET fire (CTO half, condition 8).
   - Then mints the three bundles.
   - The after-read legs are those in the CTO half, items 5 and 8. A fire that stamps the current day is a STOP and a rollback.
2. **Why `select_business_date()` answers the current day before the session (read, LOCAL; D2-W379-S3):** name the rule it follows,
   with the trading-calendar positive control, and whether the scheduled fire's path uses it. A fix is a later cell under its own pair.
   Item 1's stated-date check guards this release meanwhile.
3. **49F's missing 2026-10-08 (read, then a replay packet):**
   - why a long fire exceeds the SSM execution timeout (the timeout value, the fire's duration distribution over the last 10 fires);
   - the one-date replay's packet: what it writes (one date's keys), its rollback, and that it leaves every other date untouched.
   The replay itself runs after item 1's after-read, under its own pair.

**Carried:** IB-pr-456 (Andrew's execution ID, act `f61b`) and the Design-B CTO half (round-188 call 1). D2-W374-S1 stays with the box manager.

## Acts only Andrew can do

The IB-pr-456 execution ID (`f61b`). Nothing new.

-- 1.0.0_SA_CTO~DELL2
