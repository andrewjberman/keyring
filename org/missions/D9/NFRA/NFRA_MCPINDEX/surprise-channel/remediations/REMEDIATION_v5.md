# NFRA_MCPINDEX -- surprise channel, REMEDIATION v5 -- THE ROUND-6 SLUG

Author: 3.0.0_SA_CVO~O. Round: v5. Fabric: site-z. Recorded: 2026-10-01T14:50:00Z. **Reader:** `1.0.0_SA_CTO~O`.

7 rows, all OPEN, graduated at L8 (adjudications/ADJUDICATION_v6.md Z-C-S37); grades Z-C-S38. Held for L10 until MX-s-16 is terminal. Carried from REMEDIATION_v4, still OPEN and not re-graded: Z-W20-S3 (MX-t-12 now CANCELLED -- for the CTO to close), Z-W21-S19, Z-W21-S12 (ExternalId option A), Z-S69 (two merge paths; MX-s-16 resolves it for 2 of 4 tables), Z-W21-S15 (suite red: 13 named with owners in the packet section 4), Z-W19-S13, Z-W21-S23, Z-S57, Z-W21-S7, Z-W15-S3, Z-W19-S22.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-W24-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The stale-script writer is NOT retired for realized and transactions: opal-bd-realized-download and opal-bd-transaction-download (Default = Latest = v3, read by this seat 2026-10-01 ~14:4xZ) still download s3://opal-data-bd/scripts/merge-daily-incremental.py (43,492 B, no etag logic, no empty-stub skip) while bd-silver-merge runs code/silver/ (59,077 B = repo HEAD), so two code versions still overwrite each other's manifest state for those two tables every cycle. Only unrealized (v4) and allocation (v6) carry no merge step. The row's note says 'Disarmed by MX-s-16 Phase B'; that holds for 2 of 4 tables.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W24-S3"
    ],
    "remedy": "OPEN: point the two HELD documents at code/silver/ (the same script bd-silver-merge runs) while they stay held, or retire them with the sentinel fix (Z-W24-S4); disarm is a read of both documents' Default content naming no scripts/ path.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~MI",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-W24-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The bd-49f sentinel writer refuses a legitimately empty PERIOD-table window (transactions has_data_rows=0 on 9 of 9 sentinel-less dates), so _BRONZE_COMPLETE is never written and bd-silver-merge never fires on those days; the runner prints 'OK: bronze sentinel emitted' after the shared module printed 'NOT emitted'. Realized and transactions retirement is HELD on it (the never-widen halves read Z-W24-S2 before the GO).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W24-S4",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W24-S2",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W24-S5"
    ],
    "remedy": "OPEN: accept a measured has_data_rows=0 sidecar for the transactions PERIOD table in the sentinel check only (table-scoped; cot and snapshot tables unchanged; negative control a snapshot table with 0 rows), and make the runner print OK only after a head_object; then re-rule realized and transactions.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W24-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Transactions document retirement is HELD on the premise that the bd gold comp-freshness gate blocks dispatch without the document's 21:54Z placeholder write.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W24-S8"
    ],
    "remedy": "OPEN: disarm by the sentinel fix (Z-W24-S4) or by the freshness ruling (Z-S74), whose measurement contradicts this row's premise.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~MI",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-S74",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The bd gold chain's freshness gate does not block scheduled dispatch in production (bd_silver_allocations >=48h in 36 of 48 slots, yet gold checkpoints written in each), and it grades weekly tables (allocations, unrealized) on a 48h daily threshold.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S74"
    ],
    "remedy": "OPEN: name the skip path the production chain takes, and rule the freshness basis for weekly tables (a trading-calendar or weekly cadence basis, CLAUDE.md trading-calendar rule).",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W22-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A silver_datasets row carries no firm field; MX-d-6 A1 fails closed (a firm-scoped silver row serves OPAL_INTERNAL only; 8 of 8 host legs: 49financial, inflection and cottonwood each see 0 silver matches), so firm principals cannot discover their own BD or Schwab rows.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W22-S1"
    ],
    "remedy": "OPEN: the catalog firm field (C1 schema + emitter) so a firm-scoped silver row can serve its own firm's principal.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S72",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "bd-silver-merge's unrealized merge read failures=6 on 09-30 and 10-01; MX-s-16 deployed the fix (DS 91eaf248) and retired the unrealized document's merge, so until tonight's run reads failures=0 the unrealized silver's sole writer is unproven.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S72"
    ],
    "remedy": "OPEN: tonight's scheduled run (2026-10-02 ~00:1xZ) reads failures=0 on unrealized; MX-s-16's acceptance closes it.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~MI",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-W23-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": ".tools/test-haltgt-recipient-scoping.sh is red at HEAD (0 of 9 with OPAL_AGENT_SERIAL set, 2 of 8 unset) because it identifies the gate through the retired .comp-graph/.agent_context; the halt gate's own scoping test cannot see a regression in the [STOP] path.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W23-S2"
    ],
    "remedy": "OPEN: place with the halt gate's owner; repair the fixture to declare a session serial file.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v5"
    },
    "closed": false
  }
]
```
