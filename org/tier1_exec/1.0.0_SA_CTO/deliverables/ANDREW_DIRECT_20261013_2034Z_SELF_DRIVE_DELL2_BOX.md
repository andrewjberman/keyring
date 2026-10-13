# ANDREW DIRECT -- /self-drive over the whole dell2 box, 60-minute loop (2026-10-13 ~20:3xZ) -- ARMING RECORD

**Word (verbatim, via /keep-driving at the laptop, relayed by `0.0.0_AB_MSTR~DELL2` msg 7215 from laptop MSTR bus fca49af3):**

> "ON, 60m loops for /self-drive, /canonical-drive, /govern for the relevant agents. CTOs on each box should have /self-drive loop on their entire box, i.e. any open-calls that appears on that box they need to adjudicate."

The cloud switch reads ON for scan and empty_tick on all four boxes (20:34:07Z).

## ARM TERMS

| term | value |
|---|---|
| driver | `1.0.0_SA_CTO~DELL2` |
| scope | **the whole dell2 box**: every project placed DELL2 (11 scanned of 52 project.json: ADVI_BILLING, ADVI_COTBKF, DSGN_IRPTV1, IRPT_ANLREQ, IRPT_BCKEND, IRPT_CUSTDY (closed), IRPT_DASHBD, IRPT_YCDGEN, NFRA_OPSWKF, NFRA_TRNSPT, TCKT_VNEXT) plus every row on `org/devices/state/dell2/open_calls.json` |
| register finding | `directives-check` places only D7 (TCKT_VNEXT) on DELL2; the other ten dell2 projects sit under directives whose device reads LAPTOP. The scope follows Andrew's "entire box", not the stale device column. The register fix is routed to `0.0.0_AB_MSTR~DELL2` |
| cadence | 60 minutes |
| call routing | skill Step 1: the driver rules on its own REC; a design fork goes to `4.0.0_SA_CRO~DELL2` for research; a governance fork goes to `3.0.0_SA_CVO`; a needed seat is asked of MSTR |
| priority inside the scope | the pivot direction `XB-20261013T180328Z-d4a5`: O1 and O2 (IRPT_ANLREQ) first, then O3 (IRPT_DASHBD FWD-21); the rest never draws from those |
| cited act list | only acts only Andrew can do, each with its citation (skill Step 1) |
| paired_with | the COOs' own `/canonical-drive` 60m, armed by each COO on the same word (laptop MSTR relay); not a `/drive` |
| stop condition | Andrew's stand-down word, or HELD-AT-STOP per the skill section 4 |

-- 1.0.0_SA_CTO~DELL2
