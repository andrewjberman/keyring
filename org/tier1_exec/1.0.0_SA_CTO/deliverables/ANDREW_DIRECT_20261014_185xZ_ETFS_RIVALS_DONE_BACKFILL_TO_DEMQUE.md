# Andrew-direct 2026-10-14 ~18:5xZ (laptop, 1.0.0_SA_CTO terminal) -- ETFS_RIVALS is done; its backfill goes to MDPF_DEMQUE

## VERBATIM

> "ETFS_RIVALS is done now, all it needs is its backfill sorted out in DEMQUE"

Answers the one card at ~18:4xZ (ETFS_RIVALS' home under "dell1 wholly ADVI/MDPF").

## Applied (cluster lead)

- **ETFS_RIVALS cuts no new round.** It is EXECUTING round 30 (workstream 4, the page), issued today by
  `2.0.0_SA_COO~V1`. The orders in flight drain; no worker is stopped mid-cell.
- **Then it closes:**
  - `2.0.0_SA_COO~V1` writes `COMPLETION_REPORT`;
  - `1.0.0_SA_CTO~DELL1` writes `COMPLETION_GRADES` with Andrew's "done" as the standing word;
  - the issuer flips `status` to closed and `dep_stage` to CLOSED, as in the MDPF_HEALGAP precedent.
- **If a FWD outcome cannot grade REALIZED** only because it waits on the backfill, its grade says so. Its remainder becomes
  demand in MDPF_DEMQUE instead of a reason to keep ETFS_RIVALS open.
- **The backfill moves to MDPF_DEMQUE (dell1):** each missing range ETFS_RIVALS needs (fund, date range, field set) is entered
  as a demand row in DEMQUE's queue, with its source cited. DEMQUE sorts and fills it on its own schedule.
- dell1 is otherwise unchanged: wholly ADVI/MDPF plus overflow AMGT
  (`ANDREW_DIRECT_20261014_185xZ_DELL1_WHOLLY_ADVI_MDPF_AMGT.md`).
