# ANDREW-DIRECT 2026-09-03 ~13:08Z -- `/drive CLDGRPH to completion.` at the 2.0.0_SA_COO~A terminal

**Received by:** `2.0.0_SA_COO~A` (this lane's own terminal; not a relay)
**Verbatim:** `/drive CLDGRPH to completion.`
**Record class:** scoped loop authorization (the launch prompt's Step 1b-F class: "Arm /drive ONLY per a live scoped
authorization ... honor its cadence AND its stop condition").

## What it arms

- **Scope:** `NFRA_CLDGRPH` only (register row `org/missions/D0/NFRA/NFRA_CLDGRPH/project.json`; dep_stage
  `EXECUTING`, round 2 at receipt). No other project is hot-listed, classified, dispatched on or attested by this
  loop. The `~Y` fabric, the base COO's estate drive and every other project are untouched (LD-0527; the standing
  DEFAULT-OFF for estate `/drive` is not lifted).
- **Stop condition:** the project's register row reads `dep_stage: CLOSED` (R6 in `.tools/missions-tree-index.py`
  admits the close: every COMPLETION_GRADES row REALIZED at the card's state), OR Andrew's word to stop. Nothing
  else stands the loop down; a quiet tick is a heartbeat, never a stand-down.
- **Cadence:** the skill's default while ACTIVE > 0 -- 20 minutes, off the :00/:30 marks (cron `8,28,48 * * * *`,
  session-only, 7-day auto-expiry -- re-armed on this record if the session outlives it). Cursor: LOG-DERIVED per the
  skill's rule 5 (this lane's last substantive drive log + the ledger's consumed timestamps); NO base-keyed marker
  is written or read by a lane.
- **Drive law unchanged:** resolve-don't-attest within scope; completing workers alive (`0.7.0_AE_CloudOps~P`,
  `~Q`, spawned by this seat under /mstr-spawn); Rule 27 (task orders from decomposition cells only, one owner per
  step, in order; the spec frozen mid-round; surprises are ROWS); no gate or spine edit from this lane (pitch
  only, per Andrew 93141 / @8e134cc126); push hold (every commit LOCAL until Andrew's push word).

## Drive log path

`org/tier1_exec/2.0.0_SA_COO~A/drive_log_<YYYYMMDDTHHMMZ>.md` (derived from the running serial; the lane folder is
owned under `org/tier1_exec/2.0.0_SA_COO~*/**`, `.owned-paths.yaml:1110`). Substantive ticks only.

## Tick 1 (this record's turn, 13:08Z)

In-scope state at receipt: TO-CG-B-1 complete/certified/accepted @afd94db0ce; TO-CG-B-2 pending at `~Q` (ACTIVE:
last commit 12:42Z @799e2dad0a, the B2-AC1 mechanism limb re-stated); `~P` IDLE since 11:48Z with a live round-2
cell uncut (CG-s-3). Dispatch: TO-CG-B-3 cut to `~P` this tick (see the drive log).
