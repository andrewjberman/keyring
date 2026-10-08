# ANDREW-DIRECT -- 2026-10-08 ~17:2xZ -- /self-drive 30m at 1.0.0_SA_CTO~DELL2 over every project on the dell2 fabric

**Channel:** the `1.0.0_SA_CTO~DELL2` terminal on dell2, in-session. **Time:** received ~17:26Z, which is ~13:26 ET.

VERBATIM:

> Create a /self-drive loop that covers all the projects on this fabric, 30m interval.

## ARM TERMS

| term | value |
|---|---|
| driver | `1.0.0_SA_CTO~DELL2` |
| scope | every project held by a dell2 COO lane at arm time, 7 in all: IRPT_CUSTDY (`~K2`), ADVI_COTBKF (`~C2`), IRPT_BCKEND (`~P2`, `~Y2`, `~M2`), IRPT_YCDGEN (`~G2`), IRPT_DASHBD (`~D2`), NFRA_TRNSPT (`~T2`), TCKT_VNEXT (`~V2`) |
| why the scope is a project list | the register rows D8 and D9 read `device: LAPTOP` while their COOs sit on dell2 (the tick 1 device note of the 10-07 record). An `all directives` selector would therefore resolve the wrong fabric. "This fabric" is read as the projects whose COO lanes are seated on dell2, from the fabric-check roster at ~17:26Z. |
| cadence | 30m |
| call routing | /self-drive Step 1. The driver rules every open call on its own REC. A DESIGN FORK goes to `4.0.0_SA_CRO~DELL2` for research first. A GOVERNANCE FORK goes to `3.0.0_SA_CVO`. A needed seat that is not live is asked of `0.0.0_AB_MSTR~DELL2`. |
| acts only Andrew can do | as cited in the self-drive logs: his half or second approval on a never-widen half (CLAUDE.md NEVER-1), his login or MFA, a vendor use no word of his names, entitlements beyond his grants (for example the real X-1 filer), and portal PROD landings |
| paired_with | the per-seat `/canonical-drive` the seven COO lanes already run (LIVE_ARMS DELL2 row, CHOSEN). No new COO arm. |
| STOP-CONDITION | all 7 `complete`, HELD-AT-STOP, or his stand-down |
| supersedes | `ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` (60m, 5 projects). Its cron is deleted, and a SUPERSEDED line is appended to it in the same commit. |

`org/ref/LIVE_ARMS.md`: this seat does not write its own row. One line to `1.0.0_SA_CTO` names this record so that the DELL2 row can be
amended from 60m over 5 projects to 30m over 7.
