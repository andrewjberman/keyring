# Cross-adjudication files

One file per ruling on a call a box CTO escalated instead of ruling alone: open-ended, deeply architectural, out of
pattern, or touching another box. The same idea as `../change_management/`, for decisions instead of deploys.

- **Order:** Andrew-direct 2026-10-09 ~00:0xZ,
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`.
- **Tool:** `.tools/xadj.py` (`open`, `list`, `show`, `rule`, `adjudicator`). Design:
  `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md`.
- **Name:** `<UTC stamp>_<XA id>.md`, written by `xadj.py rule` on the adjudicating box only (the laptop CTO; the site Z CTO
  when the laptop measures down). Each file holds the originating CTO's submission verbatim (context, position, why it gave
  pause: ambiguity, out of pattern, other solutions) and the ruling.
- **In flight:** the submission travels as `s3://opal-313476888478-globgrph/fabric/xadj/v1/<XA id>.json` until it is ruled;
  this directory holds only ruled files. Commit each one with `safe-commit.sh`; box-sync carries it to every box.
