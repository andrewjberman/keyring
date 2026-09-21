# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 12 (2026-09-21 ~21:3xZ)  state: ARMED

Driver `1.0.0_SA_CTO`; carrier @`c9ccd9f4e3`; cadence 30m (cron `46e545b7`). Previous log: tick 11 @`e3fdcb516d`.

## Calls closed this window (driver's own REC, per CALL ROUTING)

**IRPT_BCKEND IB-rth-2 -- PARKED for the round-8 close** (`2.0.0_SA_COO~B` 99277, REC approved with one
amendment). Ruling @`438312b085`. Measured on the L10 refuser's own function
(`surprise-row-gate._open_tos_for_project`): 0 open of 87 scanned, 9 terminal by a VALID proof while their
status word reads pending (rth-2 and rth-7 among them). So round 8 was never blocked on terminality, only on a
disposition. On the order:
- OWNER: Andrew (delegable)
- UN-PARK: a valid MFA session at `IRPT_SESSION_STATE_PATH`
- AMENDMENT: the capture host `irpt-ycharts-runner` is STOPPED (this seat, 18:00Z, on Andrew's call 3), so the
  un-park act is start + capture + verify. MSTR's ask to Andrew now names the start explicitly.

Precedent: the round-6 rtf-5 park. COO~B compiles L8 to `3.0.0_SA_CVO~B`.

**IRPT_FNTEND round 10 -- no veto** on `2.0.0_SA_COO~F`'s two design choices (99263): fix-in-cell with mandatory
BEFORE/AFTER captures, and the canvas `<expect>` anchored on `CANVAS: ` followed by `rgb(244, 246, 250)` (ui-smoke
prints that literal on every run, so an unanchored match would pass on the retired silver ground).

## Scope state

`IRPT_FNTEND`: 3 active TOs, round 10 = FWD-12's closing pass (FE-s-61..64, @`fcf38f866b`); 7 other outcomes wait
on IRPT_BCKEND. `IRPT_BCKEND`: 9 active TOs by to-check's status word, 0 open by the refuser's proof count; round 8
closing to L8. **REACHABLE: 2 of 2. COMPLETION TEST: NOT DONE** -- 0 of 2 complete. **OPEN CALLS IN SCOPE: 0.**

## Out of scope, taken because it was the critical path for a whole fabric, recorded for continuity

`lib/opal_naming.py` (this seat's lane), after SITEZ went into a fabric-wide commit stoppage:
- `8a4cb70499` -- a row whose system differs from the tokens overrides them; validate refuses only an agreeing
  row. It amends this seat's ruling 97177. Validate 0 on CLOUD and a SITEZ stand-in; the pre-edit control
  reproduces SITEZ's red. The census over 1,431 names shows 0 changes on CLOUD and exactly the 4 F01 secrets on
  SITEZ. Also unblocked the CRO's `portal`/`website` keys (18 rows -> portal, 7 publishers keep advi/news; the
  pre-edit control refuses exactly those 7). On origin; SITEZ merged it byte-identical (`7bf71e8dfa`).
- `86b238a9af` -- validate refuses a repeated scope key (SITEZ's two `harvest` rows had silently routed AMGT
  harvest data to the vetoed bucket). LOCAL, held until SITEZ takes the CRO's dedup `10bace8916` first.
- Queued: lib/tests worked cases graded without the registry layer (CRO 99283). 5 known stale-fixture failures,
  none caused by these edits.

Push state: LOCAL on CLOUD; `origin/CLOUD` `9e76e05d11` (MSTR); only `0.0.0_AB_MSTR` pushes.

## Compiler Tools

`to-check --project` x2; `check_inbox`; `ack_messages`; `surprise-row-gate._open_tos_for_project`;
`opal_naming validate` / `grade` with a pre-edit control; the 1,431-name before/after census harness.
