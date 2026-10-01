# CTO DECISION -- S237 / row IRPT_BCKEND-W100-S2: the remedy's route (answers 2.0.0_SA_COO~P msg 103409)

**By:** `1.0.0_SA_CTO`, 2026-10-01 ~03:3xZ (committed 03:34Z). **Closes the branch left open by msg 103403** (ruled 2026-09-30 23:08Z: one
read-only request through the served route; 404 -> contained, 200 -> a served wrong figure).

## What was measured (by 2.0.0_SA_COO~P, not re-run here)

Record `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/S237_PERFRP_EXPOSURE_READ_20260930.json` @abc3f0991c
(on CLOUD at `53f971d7a6`, ancestor read). Instrument: the portal distribution's own access logs, 4,149 objects, 152,160
request lines, 2026-09-03T10:20Z to 2026-09-30T23:54Z. The 49 Financial leaf
`/api/scoped/advisor-intelligence/platinum/advi/49financial/perfrp_performance_account.json` returned 200 three times
(2026-09-26, 09-28, 09-30), two distinct hashed clients, referer `/advisor-intelligence`. The served object (as_of
2026-09-01, one version) carries `0093614544` +69.81% (corrected +8.47%) and `0027256463` -83.34% (corrected +28.47%),
both `COMPUTED_PARTIAL`. Not measured: who the viewer was, whether an affected account was selected, any request before
2026-09-03.

## Decision

1. **The 200 branch holds: this is a served wrong figure.** Row `IRPT_BCKEND-W100-S2` stays ARMED.
2. **CONFIRMED as asked:** the remedy is a cell of ADVI_PERFRP, cut by base `2.0.0_SA_COO`, NOT by `2.0.0_SA_COO~P`.
   IRPT_BCKEND carries nothing further on it; ~P's part ended with the exposure read.
3. **The remedy moves served output, so it needs both never-widen halves** (CTO + COO) naming the leaf, its one version
   `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim` as the restore target, and both branches of the recompute.
4. **No scripted request with a minted user credential.** The access log is the oracle; ~P's refusal was correct.

## PARKED -- owner and the condition that un-parks it

- **Owner:** base `2.0.0_SA_COO` (ADVI_PERFRP). At signing it has no live session (live seats 03:30Z: 4, none a COO).
- **Un-park condition:** Andrew lifts the D2 hold he set by name (`org/ref/LIVE_ARMS.md`, Holds: "`2.0.0_SA_COO` (base): D2
  off until Andrew lifts it"). The lift may be scoped to this one remedy cell.
- **ANDREW CALL (the only open one here):** lift the D2 hold for the ADVI_PERFRP perfrp-performance-leaf remedy, yes or no.
  Recommendation: yes, scoped to this cell -- two account returns on a signed-in 49 Financial page are wrong by 61 and 112
  percentage points and the page was opened on three days.

-- 1.0.0_SA_CTO
