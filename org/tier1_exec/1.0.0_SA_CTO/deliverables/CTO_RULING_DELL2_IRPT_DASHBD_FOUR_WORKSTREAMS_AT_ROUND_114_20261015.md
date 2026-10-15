# CTO ruling -- IRPT_DASHBD splits into four workstreams at round 114 (2026-10-15 ~01:1xZ)

From `1.0.0_SA_CTO~DELL2`, on `4.0.0_SA_CRO~DELL2A` msg 7891 and its assessment
`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_DASHBD_PARALLELIZATION_ASSESSMENT_20261014.md` @f82b8424c6, ADDENDUM 1 (Andrew's go, ~01:0xZ:
"Go on"). Frame: P1 Investor Reporting, Nov 15. FWDs are unchanged; no PRD change. Rule 27: ONE issuer per workstream round, with
disjoint write surfaces under different `~lane` instances.

## The workstreams (from round 114; round 113's read finishes under `~D2` as issued)

| workstream | issuer | write surface (disjoint) |
|---|---|---|
| **B-49F + contract** | `2.0.0_SA_COO~D2` (continues) | `org/standards/IRPT_DASHBD_*_CONTRACT.json` (**SOLE writer**), the sample builder, the 49F gold, and the account-return producer repair (round 113's 2026-04-21 read, then its pair) |
| **B-CW Cottonwood** | `2.0.0_SA_COO~C2` (on dell2; its old project ADVI_COTBKF moved to dell1 but the seat did not) | the Cottonwood adapter and gold partition, and its producer schedule within the 6 AM ET fold (S2/S3 for Cottonwood, in step with IRPT_BCKEND `~P2`) |
| **B-IN Inflection** | `2.0.0_SA_COO~I2` (NEW lane). NOT `~B2`, whose ADVI_BILLING moves to dell1 | the Inflection adapter and gold partition, and the account-return derivation and tie-out |
| **F-SHIP** render, tab, export | `2.0.0_SA_COO~F2` (NEW lane) | the portal `render/`, `export/`, `tabs/reporting/` and `dashboard/` folders under `InvestorReporting/`, and the `cand/dell2/*` branches it cuts |

**The overlap rules (the assessment's section 4, adopted as binding):**
1. ONE contract writer, `~D2`. The other lanes propose a member's source by a row or an ask to `~D2`.
2. A firm lane writes only its own partition and adapter. Checkers stay per-issuer, under each lane's own `checks/`.
3. F-SHIP reads the filled document and never builds one.
4. IRPT_BCKEND (`~P2`) keeps holdings and the security nodes. The household TWR is IRPT_DASHBD's.
5. **New for the split:** each lane's round analysis is this seat's. One slug per lane round goes to `3.0.0_SA_CVO~DELL2`. If the CVO's
   queue holds more than two un-graded slugs for an hour, a second CVO lane is seated (the assessment's section 5).

## Limits stated, not solved here

Cottonwood's full history still waits on dell1's ADVI_COTBKF silver. The FWD-21 organic arm is Andrew's own read. The disclosure page waits
on call a252. A client-facing PROD page waits on him.

## Seating

`0.0.0_AB_MSTR~DELL2` seats `~I2` and `~F2` and re-tasks `~C2`. This seat lands the LIVE_ARMS rows (`/canonical-drive` 60m each, DIRECTED
on Andrew's "Go on").

-- 1.0.0_SA_CTO~DELL2
