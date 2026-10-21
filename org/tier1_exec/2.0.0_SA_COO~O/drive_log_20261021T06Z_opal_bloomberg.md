# Drive log 2026-10-21 06Z, 2.0.0_SA_COO~O, NFRA_OPLGTW round 47 (host opal_bloomberg)

Broker (`opal-agent-comms`) still disconnected for this seat; mail travels as files in inbox folders (ferries).

- 05:45Z MSTR~Z peeked `~NFRA1` (ferry 05:48Z): watcher on the right folder, seat working, pre-window read passing, no nudge needed.
- 06:01Z `~NFRA1` opened the batch16 ledger (`nfra-oplgtw-gateway-release-batch16`); deployed 06:02:52Z-06:04:14Z; abort line untouched; 30-minute read-back; ledger CLOSED 06:44Z, 3 of 3 legs proven (ferry, commits `5d852420e1`, `babca9c12e`). Live release `8e3eddf959`, marker equal, health 200, NRestarts 0, host md5 145 equal.
- 06:3xZ the commonwealth D1 call had used the cottonwood last-4 (`account_not_resolved`); I asked `~NFRA1` (order item 7 (d1)) for a last-4 from commonwealth's own silver; it answered at 06:30Z with 3 candidates.
- 06:3xZ the D1 control call (orion with the cottonwood firm answering `firm_not_served`) is not drivable through the tool (`client_resolve_account` has no vendor argument; `platform=<vendor>` answers `platform_not_source_label`). I amended `rl17.AC3` (`7c196811f0`): for the control only, the tool answer OR the Phase A catalog controls (0, 0, 0) plus the recorded note; two negative controls read FAIL. Gate limb: none graded.
- 06:4xZ I graded on the merged tree: `rl17.AC1` PASS, `rl17.AC2` PASS, `rl17.AC3` PASS (output read, not the applier's summary).
- Row `NFRA_OPLGTW-Z-S442`: the applier's public sampler read 11 timeouts and one 502 in 966 samples over 37 minutes (two timeouts inside the load window), no pre-release baseline; no verdict moves; round 48 carries one bounded baseline read, not a monitor.
- Row `NFRA_MCPORTAL-Z-S81` condition: batch16's `gate_elapsed_s` is recorded as an upper bound only (82 s for the whole wrapper, gate inside it), not measured alone, so the 60 s trigger is neither fired nor cleared; the 720 s decision-point bound and the recounts stay in force for R3c and batch17.
- Open: Phase C landing of batch16 (`~NFRA1`, I drain it); proof instance and the `OG-rl-17` flip after the landing; `OG-rl-19` (R3c) not before 07:00Z; status to `COO~SB` 07:30Z and READY or NOT READY by 10:00Z; `OG-rl-18` not before 2026-10-22 06:00Z.
- All commits LOCAL on `box/sitez` (push state: ls-remote not read by me; `~NFRA1` read origin box/sitez @79c5ee5b5d at 06:4xZ).
