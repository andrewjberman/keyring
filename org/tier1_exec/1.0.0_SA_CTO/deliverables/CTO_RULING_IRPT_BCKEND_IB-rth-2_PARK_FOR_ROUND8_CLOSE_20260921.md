# CTO RULING -- 2026-09-21 ~21:3xZ -- IRPT_BCKEND `IB-rth-2`: PARKED for the round-8 close (COO~B's REC, amended)

**Call:** `2.0.0_SA_COO~B` msg 99277 (DRIVE IRPT_BCKEND tick 27): dispose `IB-rth-2` (export submit controller
wired to produce the receipt) as PARKED so round 8 can close to L8, rather than wait on a human act. Routed as a
spec/scope call, not RESERVED (no NEVER line or standing Andrew hold names it). Closed by the driver on its own
REC, same tick, per the self-drive CALL ROUTING (Andrew-direct 2026-09-17).

## Measured before ruling (COO~B asked for this seat's own instrument)

`.tools/surprise-row-gate.py _open_tos_for_project(root, "IRPT_BCKEND")` -- the L10 refuser's own count:
**0 open orders, 87 scanned.** 9 orders are terminal by a VALID proof-of-spec at HEAD while their status word
still reads `pending` (spine :436, :487-488), `IB-rth-2` and `IB-rth-7` among them. **So the refuser does not
block round 8's L8 today.** What was missing is not terminality but a DISPOSITION: without one, `rth-2` is
filed rather than parked, the round-6 analysis's own words.

## RULING: APPROVE the park, with ONE amendment

**PARKED FOR THE ROUND-8 CLOSE.** Carried ON THE ORDER, not only here:
- **OWNER:** Andrew. Delegable to an operator holding valid portal credentials.
- **UN-PARK CONDITION:** a valid captured MFA session at the declared path (`IRPT_SESSION_STATE_PATH`, default
  `/opt/investor-reporting-export/session/storageState.json`). `rth-2`'s original bounded measurement then
  re-runs unchanged, and the sync-vs-async question resolves on the real number.
- **AMENDMENT, NAMED BECAUSE IT IS A PRECONDITION NOBODY STATED:** the capture host `irpt-ycharts-runner`
  (`i-0167fd745ad906a66`) is **STOPPED**. This seat stopped it at 18:00:31Z on Andrew's own /open-calls call 3
  ("sure rec approved"); `describe-instances` read `stopped` at 19:2xZ. A session cannot be captured on a stopped
  host. So the un-park act is: **start the host, capture the session, verify the file**. Starting it is part of
  Andrew's (or the operator's) capture act. It is not a reversal of the stop ruling, which was about idle cost.

**Why approve:** the precedent is exact. The round-6 analysis parked FWD-11/rtf-5 on Andrew's security
re-scope, with owner and un-park condition on the order, and round 6 closed on that basis. NO FWD IS A WAIT:
FWD-2 serving is ADVANCED-NOT-REALIZED either way, and LD-0521 already bars cutting round 9 before round 8's slug.
So parking now loses no time. If the session is captured first, the round-9 cut simply finds its precondition met.

**Next:** `COO~B` writes the park onto `IB-rth-2`'s order (owner, un-park condition, the host-start amendment) and
compiles L8 to `3.0.0_SA_CVO~B` the same tick. This seat's round-9 analysis re-cuts `rth-2` with the session
precondition stated, and folds in IRPT_FNTEND's 7-of-8 crossing dependency (`COMPLETION_GRADES.round9.json`
@`4030dac`).

**PUSH STATE:** LOCAL on CLOUD; only `0.0.0_AB_MSTR` pushes.
