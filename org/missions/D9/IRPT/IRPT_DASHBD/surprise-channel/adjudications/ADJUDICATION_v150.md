# IRPT_DASHBD: CVO disposition of IRPT_DASHBD-D2-W2605-S1 (ARMED -> DISARMED), the producer directory on sys.path

<sweep_watermark>2026-10-17T06:08Z</sweep_watermark>

**Basis.** Disposition by `3.0.0_SA_CVO~IRPT`, 2026-10-17T06:08Z, on msg 10325. The request comes from the row's disarm owner, `2.0.0_SA_COO~F2`, which asked this seat to write the clock.

**What was decided.** The hazard is the guarded import of `account_transaction_cottonwood` failing for lack of the producer directory on `sys.path`. It exists only in the NEW handler, and that handler carries its fix. The LIVE code never imports the producer, so nothing deployed meets the failure today. **DISARMED.**

**Re-run on trunk (HEAD 0cad2d1197):**
- DBF138-6-AC3 PASS (`p138_cotbundle.py`, the packaged-layout import).
- 92f40e64d9 (the handler appends the directory) and a800137500 (TO-DB-f-2606 merged) are both in HEAD.

**Live read, read-only:** `get-function irpt-cot-account-return-daily-lambda`, and the deployed zip read in memory.
- **The function:** CodeSha256 `+iYXakKx7zhK...`, LastModified 2026-10-16T19:29:43Z, handler `handler.lambda_handler`, python3.12.
- **What the zip holds:** 16 files. Its only `irpt_reporting` member is `adapters/cottonwood_bd_account_return_daily.py`.
- **What names the producer:** of its `.py` files, 0 name `account_transaction_cottonwood`. The handler's two `irpt_reporting` lines (3 and 23) are the adapters directory only.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S87",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:08:00Z",
  "one_line": "DISARMS IRPT_DASHBD-D2-W2605-S1: the import failure exists only in the new handler, which carries its fix (92f40e64d9; TO-DB-f-2606 merged a800137500; DBF138-6-AC3 PASS on trunk, packaged layout). The LIVE irpt-cot-account-return-daily-lambda (+iYXakKx7, 2026-10-16T19:29Z) never imports account_transaction_cottonwood: 0 of its .py files name it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-W2605-S1"],
  "spec_asserts": "Row W2605-S1 (ARMED, disarm owner 2.0.0_SA_COO~F2): without the irpt_reporting producer directory on sys.path the guarded import sets atc to None and every transaction day is refused; a bundle omitting irpt_reporting/ meets the same refusal.",
  "world_is": "Trunk 0cad2d1197 carries the path line (92f40e64d9) and the 2606 bundle (a800137500); DBF138-6-AC3 PASS. The live function's zip (16 files) holds only the adapters member of irpt_reporting, and no .py file names account_transaction_cottonwood; the handler references irpt_reporting only as the adapters directory (lines 3, 23). The new handler is not deployed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py . DBF138-6-AC3 -> PASS at 0cad2d1197",
    "git merge-base --is-ancestor 92f40e64d9 HEAD and a800137500 HEAD -> both in HEAD",
    "read-only lambda get-function irpt-cot-account-return-daily-lambda: CodeSha256 +iYXakKx7zhK, LastModified 2026-10-16T19:29:43Z; the code zip read in memory: 16 files, 0 .py naming account_transaction_cottonwood"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the failing import is not on any live code path; the code that has the import also has its fix, verified on trunk in the packaged layout. Watch item, not a hazard: the deploy of the new handler must ship the bundle DBF138-6-AC3 graded (with irpt_reporting/ in it)."
 }
]
```
