# Deploy Completion Record
**Date opened:** 2026-09-26T17:48:23.428377+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T181043Z
**Deploy:** S147 experiment (CTO 101385): irpt-performance-adapter memory_size 1536 -> 3008 MB; rollback 1536; gate DELTA=0 on report bytes
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | verify | latency + DELTA=0 | 3 new-window recomputes timed (Duration); one served report byte-compared with the same engine code locally on the same data (DELTA=0), a difference = STOP + revert | 3008 MB (TF @12e1041456, safe-apply 0/1/0, readback 3008, replan 0): 3 recomputes on new windows (acc_bf96..): end 09-21 Duration 26515 ms (init 436), 09-19 23164 ms, 09-18 23067 ms, maxmem 342-367 MB -- vs 1536 MB 29670/26023/25850 ms: ~10% faster, NOT CPU-bound, still > 15 s. DELTA=0: each 3008 series (180/179/179 pts) IDENTICAL to the 1536 recompute RPT-e0a917d2's prefix. Reverted to 1536 (TF @6eace01350, safe-apply 0/1/0, readback 1536, replan 0) -- the gain does not justify 2x memory; the real fix needs phase timings (next S147 card). | CLOSED 20260926T181043Z |
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | memory 1536 -> 3008 -> 1536; code Zs2OK7C5 unchanged throughout; final readback 1536; replan No changes | CLOSED 20260926T181043Z |

## Log

- 20260926T174823Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260926T181043Z LEG M1 closed: 3008 MB (TF @12e1041456, safe-apply 0/1/0, readback 3008, replan 0): 3 recomputes on new windows (acc_bf96..): end 09-21
- 20260926T181043Z LEG irpt-performance-adapter closed: memory 1536 -> 3008 -> 1536; code Zs2OK7C5 unchanged throughout; final readback 1536; replan No changes
- 20260926T181043Z CLOSED -- all 2 legs proven
