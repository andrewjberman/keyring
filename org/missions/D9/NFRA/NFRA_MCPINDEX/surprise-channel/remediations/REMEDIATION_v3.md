# NFRA_MCPINDEX -- surprise channel, REMEDIATION v3 -- THE ROUND-3 SLUG

Author: 3.0.0_SA_CVO~O. Round: v3. Fabric: site-z. Recorded: 2026-09-29T03:45:00Z. **Reader:** `1.0.0_SA_CTO~O`.

6 rows, all OPEN: 4 graduated from round-3 investigation rows and 2 raised at L9. Carried from REMEDIATION_v2 and not
re-graded here: Z-S29/Z-S31 stay OPEN on rotation, but this seat's scan now reads 0 live fingerprints across 43,706
tracked text files at HEAD (6 in round 2), so their value-out-of-tracked-files half is met (Z-C-S30).

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-W8-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Four BD Playwright daily legs (allocation, realized, transaction, unrealized) read opal/bd/credentials and attempt the MFA-broken portal login every weekday, failing 21 of 21; they are the live readers that keep the grant on bd-exporter-ec2-role.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W8-S3",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S52",
      "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/MEASURE_BATCH_ROUND3.md (a)"
    ],
    "remedy": "OPEN: retire or port the four legs off the portal login on the MX-s-12 pattern; then re-run MX-i-4 unchanged. Measure the BD lockout exposure before or with the cut.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~MI",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPINDEX-Z-W11-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The deployed EC2 transaction merge (43,492 B, not the 59,077 B repo file) skips the bd_assets_dim cusip join on every file-processing run and wrote 0-row partitions; the dim's currency does not reach silver transactions.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W11-S2",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S51",
      "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/MEASURE_BATCH_ROUND3.md (b)"
    ],
    "remedy": "OPEN: a DS-lane silver cell after the transaction leg is ported (Z-W8-S3); deploy the repo merge or fix the deployed one, and measure the join on a run with rows.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W10-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "4 of 27 routing questions still miss: Q22 has no catalog vocabulary to select a candidate; Q09, Q13 and Q25 are precision misses where one common word selects a whole channel.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W10-S1"
    ],
    "remedy": "OPEN: catalog index vocabulary for Q22; a NOT_CATALOGUED precision rule for weak channel-keyword-only matches, graded on recall as well.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W13-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "validate_catalog_v02.py makes live S3 reads, which a No-AWS cell cannot run, and 1 of its 36 channel rows reports family_mismatch_or_error, unidentified.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W13-S2"
    ],
    "remedy": "OPEN: identify the one row on a cell that may read S3, and give the validator an offline mode or name it a WORLD instrument.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S28",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal_discover's next_tool is query_v0 for every servable row, never the purpose-built integration tool that answers the same row.",
    "evidence": [
      "adjudications/ADJUDICATION_v4.md#NFRA_MCPINDEX-Z-C-S28"
    ],
    "remedy": "OPEN: join the route to the tool -- name the purpose-built tool as next_tool where one exists (mp.01 -> mdpf_get_aum_metrics); FWD-1 is graded on this.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S29",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal_discover reports the catalog's certification vintage as latest_value (claim held) where the served object carries a fresher date.",
    "evidence": [
      "adjudications/ADJUDICATION_v4.md#NFRA_MCPINDEX-Z-C-S29"
    ],
    "remedy": "OPEN: either re-read the served object's vintage field at answer time (claim measured) or say beside the held value that the served object may be fresher; a design call.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v3"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
