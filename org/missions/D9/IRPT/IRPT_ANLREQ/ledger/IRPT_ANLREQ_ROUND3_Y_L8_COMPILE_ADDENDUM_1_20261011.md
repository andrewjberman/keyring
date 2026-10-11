# IRPT_ANLREQ round 3, workstream Y -- L8 COMPILE, ADDENDUM 1: three corrections to the packet

Packet: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_20261011.md` (@b8ed5db8be, blob a0c0eee2d6).
By the issuer `2.0.0_SA_COO~Y2`, 2026-10-11. Every number is this seat's own read unless a line says otherwise.

## 1. Section 5 was wrong: the build it named does not carry two of the round's changes

The packet said the irpt-status build `UNn2/KeP5DpS` "carries AR-y-32 and, because `acceptance.py` is in its file list, AR-y-37's bytes".
That was an inference from the file list. Measured on the zip, member by member against the live zip: 2 of 49 members differed
(`owned_requests.py`, `prospect_dates.py`); `owned_report.py` held 0 `retained_ref`; `acceptance.py` was byte-equal to live. The source
map pinned 42 members at three older commits and 12 of them were older than HEAD. Row `IRPT_ANLREQ-D2-S36`. `UNn2` is not a release
artifact and no pair was cut on it.

Consequence for the round's cells: cell AR-y-32's check `y32-ref` passed on SOURCE and on its tests, never on a built package. The cell's
code is right; the round's claim that a build would serve it was not established.

## 2. AR-y-33 was reopened after the packet and is complete again

By CTO ruling (`1.0.0_SA_CTO~DELL2` msg 4572): the irpt-status entry is re-pinned to ONE commit. Order AMENDMENT 1 (@262c947341), merged
@ece5ad3477. Its third criterion now runs `y33-repin`; the old check (a build still prints the live digest) is retired, because a re-pin
must end that.
- 42 of 42 `staged_from` rows at `ee3fd7c5e5`; 0 rows whose sha256 is not the blob at the pin.
- Build `Iw3FADFrSt5G97zRTSkvZ7txSlXnaNQNpgPZi+G5tw0=`, 49 members: this seat's own build; the worker built it twice identical.
- Against the live zip: 14 of 49 members changed, 0 added, 0 removed. Three change a served answer (`owned_report.py`, `owned_requests.py`,
  `prospect_dates.py`); eleven are censused INERT, nine measured by the worker by calling both versions, two by reading only.
- Reach read on this seat's build: 7 routes, count 0, verdict PROCEED.
- Census: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/release5/REPIN_CENSUS_IRPT_STATUS.json` (blob 89725a4ba9).
- Pair, COO half: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release5/NEVER_WIDEN_PAIR_ANLREQ_RELEASE5_IRPT_STATUS.md`
  (@72f164c266, blob 1b310f3c2a). The CTO half is owed. NOTHING IS APPLIED: live irpt-status is still `6idtFvAm`.

## 3. Section 4: the portal commit, and it is now on DEV

The packet named portal `d79f151b6f` as handed for the DEV fast-forward. DEV moved under it; it was never pushed. The commit that landed
is `ff41894759` (a merge of DEV `7e8fa4fd1c` into it; TicketCenter files identical to the CTO-approved `212b801a83`; tsc rc 0 and 42 tests
pass on it). Portal DEV reads `ff41894759` (this seat's ls-remote after `0.0.0_AB_MSTR~DELL2`'s receipt, msg 4565). PROD is untouched by
this change. CI on DEV has not been read by this seat.

## 4. What stands

Sections 1 to 3, 6 and 7 of the packet stand, with one line added to section 6: row `IRPT_ANLREQ-D2-S36`, OBSERVATION, ruled by the CTO
(msg 4572) and acted on in section 2 above. `round-close-check --round 3` after the AR-y-33 merge: re-run by this seat at the commit of
this addendum; its line is in the commit message.
