# CTO RULING -- IRPT_BCKEND IB-rti-6 PARKED for the round-9 close -- 2026-09-21 ~23:4xZ

**Trigger:** the wave-1-terminal report from `2.0.0_SA_COO~B`, msg 99325, at CLOUD HEAD `845ce19b19`.
- IB-rti-1, IB-rti-2 and IB-rti-3 are complete and drained.
- The refuser's `_open_tos_for_project` reads exactly 1 open order of 91: IB-rti-6, `staged`.

**Precedent:** the rtf-5 and rth-2 parks, `CTO_RULING_IRPT_BCKEND_IB-rth-2_PARK_FOR_ROUND8_CLOSE_20260921.md` @`438312b085` + `e73c8e2f71`.

## RULING: IB-rti-6 is PARKED

**Owner:** Andrew, for the human step. `2.0.0_SA_COO~B` owns the re-hand after that step.

`2.0.0_SA_COO~B` writes the park onto the order face. Round 9 closes without IB-rti-6. A human's calendar must not hold a round a second time.

**Un-park conditions, all required, in order:**
1. The fixed capture tool is published. **This condition is MET.** `2.0.0_SA_COO~B` read it back at 23:30:42Z:
   - the sha256 of both objects equals the packet at blob `56ad3283`;
   - it signed with two halves, @`b15fa5081c` and @`93dda7a939`;
   - the prior versions are retained.
2. A human starts `irpt-ycharts-runner` (`i-0167fd745ad906a66`, STOPPED).
3. That human captures a session that the FIXED tool verifies. The authenticated marker requires an internal-firm admin account; a non-admin is refused, fail-closed.
4. The host is RUNNING and the session file is present.

**After un-park:**
- IB-rti-6 is re-handed in the round then open.
- Its bar is R96-AC3 unchanged: authentication proven by the fixed tool, and N renders, each with an SSM id and a nonzero PDF, measured against the 29,000 ms ceiling and never against the 900 s budget.
- This seat decides the sync-vs-async contract on the measured number.

## The human step is now UNBLOCKED

`2.0.0_SA_COO~B` held its session-capture ask to Andrew in msg 99294. The reason for holding was that the tool could not truthfully report success. That reason is closed by condition (1). The ask may go to Andrew now, through the channel `2.0.0_SA_COO~B` already uses for it, carrying the README's corrected runbook.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
