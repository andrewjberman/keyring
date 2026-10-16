# NFRA_CTLPLN: CVO L8/L9 at the round-26 close -- FWD-15 re-graded (2026-10-16)

<sweep_watermark>2026-10-16T04:45Z</sweep_watermark>

L8/L9 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109597 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND26.md`
@1d136f5200). Round 26's one cell `CT-ap-1` is the act ADJUDICATION_v29 C-S81 named; it ran on dell1 as crossbox call
`XB-20261016T042748Z-779c`, so no laptop order exists. The round minted no row.

**Result: FWD-15 REALIZED (C-S86). Tally: 8 REALIZED (1, 3, 5, 15, 16, 17, 24, 28), 16 ADVANCED, 0 GATED, 1 PARKED (9),
3 MOVED (13, 20, 26); denominator 28 (C-S87).** The dell1 scratch delete is no longer held by any grade.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S86",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:45Z",
  "one_line": "FWD-15 graded REALIZED: the lane 1.0.0_SA_CTO~DELL1 ran its work on dell1 with tabulate imported from the delivered SCRATCH_TARGET install, and this seat reproduced its committed table byte for byte from the committed receipts with the committed script.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 FWD-15 DONE WHEN: one real package taken the whole way for one Dell lane, and the lane's work then runs. C-S81's one open act: a dell1 lane imports tabulate only from SCRATCH_TARGET, renders one table, and commits the output and tabulate.__file__.",
  "world_is": "origin/box/dell1 e5f033b15c (author 1.0.0_SA_CTO~DELL1), folder NFRA_CTLPLN_TABULATE_LANE_READ_DELL1_20261016/, 3 files: output_run2_as_printed.txt reads tabulate.__file__ = C:\\dev\\_intake_tabulate_20261016\\SCRATCH_TARGET\\tabulate\\__init__.py, __version__ 0.9.0, sys.path[1] = SCRATCH_TARGET ahead of the interpreter's own entries, and a 2-row table (install rc 0, prove rc 0, received_sha256[:12] 024ca478df22, the laptop wheel's prefix). Run 1 (rc blank, a script read error) is kept as printed. This seat ran the committed render_receipts_table.py, with only its receipts path re-pointed, over the two receipts committed at c25860a18b: the 4 table lines are IDENTICAL to dell1's output, so the table is a real render of the real receipts, not hand-typed. With C-S81 (checked, Taildropped, installed from the file alone with --no-index, pip logs hashed equal to their receipts), the one package went the whole way and the lane's work ran. Not read: the python -s flag and the start folder (dell1's note only; the committed __file__ and sys.path settle the import source without them); whether dell1's own interpreter already had tabulate (immaterial: the import came from SCRATCH_TARGET).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show e5f033b15c:org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_CTLPLN_TABULATE_LANE_READ_DELL1_20261016/ (3 files), on origin/box/dell1",
    "the committed script re-run over git show c25860a18b:.../receipts/*.json, 2026-10-16T04:4xZ: diff against output_run2_as_printed.txt table lines -> identical",
    "adjudications/ADJUDICATION_v29.md C-S81"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "NFRA_CTLPLN-C-S87",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T04:45Z",
  "one_line": "FWD delta after round 26: 7 -> 8 REALIZED (FWD-15), 17 -> 16 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED; denominator 28.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "C-S86. Unchanged and not re-read this round: FWD-14 (Andrew's sitting, c9a4 and b87f), FWD-18, FWD-19 and FWD-11 as C-S80 left them.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this record's C-S86",
    "adjudications/ADJUDICATION_v29.md C-S85 (the table entering the round)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard."
 }
]
```
