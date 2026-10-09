# CTO RULING -- IRPT_BCKEND workstream M: unblock UB-20261009T052107Z-32d8 folded

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~05:5xZ | **COO:** `2.0.0_SA_COO~M2` | **CRO approach:** `4.0.0_SA_CRO~DELL2`, 05:31:08Z
(`python .tools/unblock.py show --id UB-20261009T052107Z-32d8`).

## Ruling: the CRO's three acts are ADOPTED, with these conditions

1. **Act 1, the S392 dry-run pre-read: GO.**
   - Run with `--dry-run --local-out <scratch>` and no `--upload`.
   - **Before the run, print the write set.** The pre-read file names the instrument that shows zero S3 puts, for example the script's
     own dry-run branch at file:line, and lists the local files written.
   - A run that writes any S3 key, served or QA, is outside this ruling. It becomes a BLOCKING row and goes no further.
   - The scheduled 14:15Z fire stays the acceptance. The pre-read is not production evidence.
2. **Act 2, the D1-S8 trace: GO.** It is read-only and touches no line of `holdings_snapshot.py`. It lands as an evidence file plus one row
   on MDPF_SECCLASS's channel, addressed to dell1 `~M1`. It is cross-box evidence, not a cell.
3. **Act 3, the Holdings-tab walk: GO, bounded to one walk.** It runs on the local dev build at port 5174. The frontend brief goes to IRPT_FNTEND's
   owner as a gap list, with no cell cut by ~M2.

## The re-seat

After act 3, `~M2` is RELEASED from IRPT_BCKEND's open work. It keeps only the two event obligations, which its existing crons already arm:
- the S392 10:43 ET read;
- the COO half when dell1 ships e56.

This seat does NOT assign `~M2` to a project. IRPT_ANLREQ already runs a driver and three workstreams, and the consolidated performance
project (IRPT_DASHBD) has its own seats. A new seating follows `org/missions/SEQUENCE.yaml` and the box's COO capacity, and it is
`0.0.0_AB_MSTR~DELL2`'s act.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 1 (2026-10-09 ~05:5xZ): superseded by Andrew's close of the ~M Holdings workstream

Source: Andrew-direct at `4.0.0_SA_CRO~DELL2`'s terminal, VERBATIM: "Not close BCKEND, just the "Holdings" tab work which is what ~M was on, and I
dont see any work remaining on the Holdings tab of IRPT". Recorded in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261009_IRPT_BCKEND_CAN_IT_CLOSE.md` @0eefcda6b4.

- **The ~M Holdings workstream CLOSES now.** IRPT_BCKEND stays open. Acts 1 to 3 above are STRUCK and not run.
- **S392:** today's 14:15Z fire is read once for NO-WORSE by `2.0.0_SA_COO~P2`, against AMENDMENT 2.1. If it is NO-WORSE, S392 RETIRES. A regression
  becomes a BLOCKING row.
- **The e56 never-widen COO half,** due when dell1 `~M1` ships, moves to `~P2`.
- **~M2's two event crons are disarmed** once `~P2` acks the hand-over. `~M2` is released, and its seating is MSTR's.

-- 1.0.0_SA_CTO~DELL2
