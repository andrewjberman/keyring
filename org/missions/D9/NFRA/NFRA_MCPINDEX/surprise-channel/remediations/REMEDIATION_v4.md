# NFRA_MCPINDEX -- surprise channel, REMEDIATION v4 -- THE ROUND-5 SLUG (rounds 4+5)

Author: 3.0.0_SA_CVO~O. Round: v4. Fabric: site-z. Recorded: 2026-10-01T08:20:00Z. **Reader:** `1.0.0_SA_CTO~O`.

12 rows, all OPEN, graduated at L8 (adjudications/ADJUDICATION_v5.md Z-C-S33). Grades: Z-C-S34. Order of reading: row 1 gates FWD-1 and FWD-4 and must land before r6.J1's cold run. MX-t-12 reads `pending` at HEAD (row 2), so the round is not fully terminal; it is carried here by the issuer's Z-S67. Carried from REMEDIATION_v3, not re-graded as a set: Z-W8-S3 is the subject of MX-s-14 (complete; Z-S69), not re-read here; Z-C-S28 is MEASURED MET for one row (this seat's live discover 'ETF positioning' names etfs_get_positioning) and UNMET for BD and Schwab (row 1).

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-W21-S22",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "opal_discover never reads the catalog's silver_datasets section (app/refs/DATA_CATALOG.yaml:1359; in the gateway tree only tests/test_blackdiamond.py:186 and the blackdiamond integration's CATALOG_REF constant name it), so the blackdiamond_fees row is unreachable; and no Schwab dataset has a catalog row at all. Re-read live by this seat 2026-10-01 ~08:1xZ on catalog 0.4: 'what fees did Black Diamond charge' and 'Schwab positions' both catalogued=false, 0 matches; control 'ETF positioning' routes to etfs_get_positioning. MX-t-13's catalog AC graded the row's PRESENCE in a section no reader consumes, which is how an unreachable row shipped green.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S22",
      "adjudications/ADJUDICATION_v5.md#NFRA_MCPINDEX-Z-C-S31",
      "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/R7_J1_PRINCIPAL_SESSION_20261001.md"
    ],
    "remedy": "OPEN: make discover read the section the row lives in (or move the row), add Schwab catalog rows, and grade reachability: one live discover per new row naming its tool. FWD-1 and FWD-4 route clauses fail until this lands; it must land BEFORE r6.J1's cold run, which otherwise fails on its Schwab position question by construction.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-Z-W20-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "MX-t-12 (advi portal tool) is HELD: the naming limb refuses the new platinum/advi/49financial/ literals (Andrew's R20 named etfs and BD fees only), and the objects are a frozen twin unchanged since 2026-08-21 (publisher disabled), so no tool over them meets FWD-2 parity. The order reads <status>pending at HEAD: it is not terminal.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W20-S3",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W20-S4",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W20-S5",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S67"
    ],
    "remedy": "OPEN: the CTO rules MX-t-12 superseded or cancelled (with its pointer) or re-scopes it onto the advisor page's live source; any new literal needs an R20 entry Andrew acknowledges.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W21-S19",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The CLOUD copy of the opal-gateway terraform root does not render under safe-apply: three data-source secrets of other seats' unapplied files are absent live and two Lambda source dirs are absent from a sparse worktree, so the comp-tagauthz gate cannot run on it; MX-r-7 applied from a pruned scratch copy with the gate running.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S19"
    ],
    "remedy": "OPEN: make the root plannable as committed (apply or gate the other seats' files), so train acts #2 and #3 do not each need a pruned copy.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W21-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MX-r-7 shipped A5 option B: the BD reader ExternalId is rendered into the host .env at deploy time; the six-resource targeted plan (Plan 6) applied.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S12",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S13",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S17"
    ],
    "remedy": "OPEN: option A, a runtime secret read of the ExternalId (the Schwab pattern of Z-W19-S12), retires the .env copy.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S69",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BD realized, transaction and allocation silver have two merge paths: the Playwright documents' merge step and the S3-triggered Lambda bd-silver-merge (the writer of record, ~5 min after each input lands).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S69"
    ],
    "remedy": "OPEN: retire one path or record why both stay, with the writer count for each table.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W21-S15",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gateway test suite is red on CLOUD before any cell: 11 failures plus 35 StreamableHTTP errors at a73e9cf57e (Z-W21-S6), with known pins (test_ogz1_ac05/ac08, test_ogz2_ac06/ac08, ETFS_RIVALS test_rivalfunds_view). One failure is a contradiction between two shipped criteria: MX-d-5 asserts 'ETF holdings and fund flows' is NOT catalogued and MX-t-10's row now catalogues it. Every cell's 'fails with and without' line is graded against a moving red baseline.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S15",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W14-S6",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W15-S4",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S4",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W20-S2",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S6",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S17"
    ],
    "remedy": "OPEN: one hygiene cell at the drain that brings the suite to green or names each remaining red test with its owner; rule the MX-d-5 vs MX-t-10 assertion.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W19-S13",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NFRA_OPLGTW_CONTRACT.json exists in three copies: org/standards (now lists dim_transaction), the gateway's deploy/ byte copy cut from an OLDER base, and the mcportal grant-writer Lambda's bundled copy. A rolled-back deploy left the deploy/ copy on the host (a tar extract never deletes).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S13",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S16",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S9"
    ],
    "remedy": "OPEN: one source with build-time copies checked equal at release, or a release check that fails when a copy differs from org/standards.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W21-S23",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-ec2-deploy.sh's own manifest rewrite (jq | tr) re-encodes non-ASCII EC2_MANIFEST.json lines as cp1252 mojibake in its commit (twice: e159e023f0, da1f54bfda); its halt gate exits 3 in a deploy-only tree that has no session serial file.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S23",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S21",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S21"
    ],
    "remedy": "OPEN: place with the wrapper's owner; fix the manifest rewrite's encoding and resolve the halt-gate serial from the session, not the tree.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S57",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The issuer's channel resolver found incoming rows by a regex on '{\"id\":' as the first key, so a drain read 0 incoming rows when a worker wrote id after other keys, and safe-merge exited 0 (drain 789d4bb967).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-S57"
    ],
    "remedy": "OPEN: parse the JSON blocks rather than match a key order, or record the fix commit; a silent 0-row drain reads identically to a clean one.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W21-S7",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "emit_catalog_v02.py cannot run in a worker's sparse worktree (needs portal/src/api from the empty submodule dir and the census outside the cone) and, without them, rewrites census_ref on rows it does not own; channel keywords have no authored home beyond the EXTRA_CHANNEL_KEYWORDS map MX-d-5 added.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W21-S7",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W15-S1",
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W14-S4"
    ],
    "remedy": "OPEN: give the emitter its inputs as declared arguments and refuse (not rewrite) when the census is absent.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W15-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The platinum/etfs catalog row is AUTHORED in the emitter (a channel block and one artifact row), not certified, and it now serves live (discover routes 'ETF positioning' to etfs_get_positioning).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W15-S3"
    ],
    "remedy": "OPEN: decide whether an authored row needs certification before serving; if yes, certify this one.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W19-S22",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The v3 NEVER-2 sentinel path was outside MX-r-6's <paths> (only the v2 slug's file is named), yet the commits that opened and closed it were admitted.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_MCPINDEX-Z-W19-S22"
    ],
    "remedy": "OPEN: place: either .open_deploys/ is deliberately exempt from the owned-paths check (record it) or the validator has a gap.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v4"
    },
    "closed": false
  }
]
```
