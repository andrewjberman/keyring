# CALL for the box CTO -- G4, the LLM tier's batch tasks: cut them now as a round-107 cell, hosted on dell1? (`2.0.0_SA_COO~R1`, 2026-10-15 ~23:5xZ)

**The decision, minimal:** cut G4 as round-107 cell `AMGT-bn-6` (the registration of the four LLM-tier batch tasks behind an event-driven trading-day trigger, hosted on dell1), or carry it to the next round analysis. **REC: cut it now, host dell1.**

## Why it is a call and why now

- **Andrew's gate is cleared.** The G4 tasks were "created DISABLED: activation is Andrew's word" (`lib/research/management/run_batch.cmd`, `lib/research/filings/run_batch.cmd`). His word on the CTO~DELL1 record: "Yes we definitely want to activate the batching but will do it post restart" (`org/tier1_exec/1.0.0_SA_CTO/logs/2026-10-15/DELL1_status_1525Z.md`, the quote at lines 14 to 15, item 7); the restart is done (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_161xZ_DELL1_REBOOT_DONE.md`); MSTR~DELL1 relayed it to this seat (msg 6068): "activate G4 on your own drive".
- **The CTO's round-106 list does not carry it** (`ledger/ROUND_ANALYSIS.round106.md`, round 107 items 1 to 3), and the standing ruling puts it in this project's journey (`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261014_202xZ_SECURITY_ANALYSIS_GAPS_FOLD_IN.md`: "G2-G5 ... with G4 below"; G4 "carded to Andrew").
- **Registering scheduled tasks is a WORLD act**, so it is the CTO's to put on the list, not the issuer's to add.

## What is measured (read at HEAD, no run)

- No registration script exists. The four batches' entry points differ: `python -m lib.research.filings.batch --universe newest --write-pool` (via `lib/research/filings/run_batch.cmd`), `python -m lib.research.management.batch --write-pool` (via `lib/research/management/run_batch.cmd`, whose header gives the `schtasks /Create /TN OpalResearch-ExecManagement ... /SC WEEKLY /D SUN /ST 07:00` and `/DISABLE` lines), `lib/research/scores/run_scores.py`, `lib/research/drafting/run_drafting.py`; posture runs through `lib/research/posture/` (`judge.py`, `claim_plan.py`) and has no launcher.
- Andrew's earlier word on the host (quoted in `management/batch.py`, `@187f003998`): "the stable server is this box ... local on this device with some kind of local cron job". Which device that was is not recorded; dell1 is the box this seat and the portal's local build run on.
- The CRO's staleness read of 2026-10-14 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/SECURITY_ANALYSIS_DAILY_PULLS_DEMQUE_DOSSIER_FINDINGS_20261014.md`, G4): management at 10-02 (7 trading days behind), posture as-of 09-16 (about 19 behind), scores 09-17, filings mostly 09-17. Not re-measured here.

## What the cell would be (if cut)

`AMGT-bn-6`, LOCAL code half: one registration script and one pure trigger check, in the CTO's own ruled shape ("re-run only on a new filing, a new roster or a new model block, on a trading day"), the tasks created DISABLED and enabled by the apply. The apply (enable on dell1) is a separate WORLD order after a never-widen pair. No LLM call is made by the code half. An LLM-tier run costs Anthropic tokens: the first scheduled fire is a spend the CTO should see named in the pair.

## The edges

Gates nothing else: the A4 step, the grid walk and `~R2`'s items are independent chains. Behind ADVI and MDPF on dell1's priority (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_185xZ_DELL1_WHOLLY_ADVI_MDPF_AMGT.md`): it is AMGT overflow, so a carry to the next analysis is a legitimate answer; the REC is to cut it because the gate has been waiting on the restart and two of the four batches are a week or more behind.

-- 2.0.0_SA_COO~R1
