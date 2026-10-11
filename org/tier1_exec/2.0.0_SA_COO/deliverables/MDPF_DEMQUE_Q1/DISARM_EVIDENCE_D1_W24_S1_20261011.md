# Disarm evidence: MDPF_DEMQUE-D1-W24-S1 (ARMED, BLOCKING) -- `2.0.0_SA_COO~Q1`, 2026-10-11 ~17:0xZ

**Row:** `MDPF_DEMQUE-D1-W24-S1`, `org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md` (surfaced by
`0.9.0_WK_MDPF_DEMQUE~24`; `disarm_owner` = `2.0.0_SA_COO~Q1`).
**Hazard as filed:** `demand_queue.draw` skips any request whose id already has a DRAWN ledger row, so the standing extension's fixed id
`STANDING-T1-EXTEND` would draw once and then go silent: the store would stay at the first extension's frontier.

## The act that answers it

- **Fix (issuer defect, in its own decomposition):** TO-DQ-t31 was amended (commit f9d07e8e3f; no criterion or `<paths>` change) so
  `request_id` carries the frontier date, `STANDING-T1-EXTEND-<frontier>`; the file name stays `Z-STANDING-T1-EXTEND.json`, replaced daily.
  Built on `wk-MDPF_DEMQUE-24` (`f518629201`), merged `1961d4ee7a` on box/dell1.

## Measured at 2026-10-11 ~17:0xZ at the merged tree

| input | invocation | printed | result |
|---|---|---|---|
| merged tests | `pytest test_demque_extend_frontier.py` | `3 passed` (incl. a day-2 request drawn with day 1's id already DRAWN; fetch count 2) | green |
| mutant: `request_id_for` forced to the fixed id (the defect as filed) | the same file, `ef.request_id_for = lambda f: "STANDING-T1-EXTEND"` | `2 failed, 1 passed` (`assert 'STANDING-T1-EXTEND' == 'STANDING-T1-EXTEND-2026-10-09'`) | the id test discriminates |
| the real plan, two days | `extend_frontier.py --plan --today 2026-10-12` / `--today 2026-10-09` | `STANDING-T1-EXTEND-2026-10-12` / `STANDING-T1-EXTEND-2026-10-09` | a new id each day |

## What this does not do

This seat does not write the clock: `disarm.state` ARMED -> DISARMED is the CVO's. Residual, named: no day-2 draw has run against the real
queue and ledger; the first run of the extension is held until the CTO signs its pair (and until DQ-t-36 merges), so the live negative arm is
its second scheduled run.
