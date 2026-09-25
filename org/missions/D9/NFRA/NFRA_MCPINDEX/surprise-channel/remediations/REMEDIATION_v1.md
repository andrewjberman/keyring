# NFRA_MCPINDEX -- surprise channel, REMEDIATION v1 -- THE ROUND-1 SLUG

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Recorded: 2026-09-25T06:10:00Z. **Reader:** `1.0.0_SA_CTO~O` only.
The recut is `2.0.0_SA_COO~O`'s.

Input snapshot: workspace `fec99f11cd`. Investigation: `INVESTIGATION_v1.md@1a651aecfc` (11 rows). Adjudication:
`adjudications/ADJUDICATION_v1.md` (same commit): 11 of 11 items dispositioned (7 GRADUATED, 4 DISMISSED), 2 findings
raised from the issuer's prose (C-S12, C-S13), and 8 judgment criteria graded, all PASS with stated limits (C-S14,
C-S15). Terminality: 38 of 38 (9 complete, 29 superseded). Instances: 9 of 9 VALID rc=0 on this seat's run.

Eleven rows: **2 REMEDIATED** inside the round and **9 OPEN**:
- **Three ARMED hazards on live data, two re-measured today:**
  - W3-S2: TrueShares holdings are unconverted, 0 silver objects against 32 bronze per fund, and still growing.
  - C-S13: the Black Diamond cusip bridge has been frozen since 2026-04-14.
  - C-S12: Eclipse's firm scope is unverified.
- **Cut defects** (W1-S3, W1-S6).
- **The AC11 path** (W1-S5, disarmed; the re-cut carries 49 = 44 + 5 HELD).
- **A shared-bucket read-fence rule** (W4-S1).
- **The question gaps for the tool cells** (C-S14).
- **A one-line docstring fix** (C-S15).

W3-S2's owner, 0.4.0_DS_ClientPlatform, is outside this fabric, so the item is PARKED with its owner and un-park
condition in its row; 1.0.0_SA_CTO~O routes it. No row carries `route` or `loop_target`.

```json
[
  {
    "id": "NFRA_MCPINDEX-W1-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A criterion required exercising the served catalog, but the cell's <paths> did not grant it.",
    "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S1", "catalog-writer.result.md:79-121 (AC4 PASS under the amendment)", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S1"],
    "remedy": "Executed inside the round: the issuer amended the grant, and AC4 was re-run and PASSED. Carried rule for the re-cut: a criterion that exercises a served file names that file in <paths> at the cut.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": true
  },
  {
    "id": "NFRA_MCPINDEX-W4-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A drain merge whose message claimed 'order complete' landed 1 of 6 files while a second lane's merge was open in the shared tree.",
    "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W4-S2, #NFRA_MCPINDEX-Z-S1", "repair 155533ea00", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S6"],
    "remedy": "Executed: repaired at 155533ea00. At HEAD the files are present and the instance is VALID. Carried method: after every drain, compare each file's blob against the branch.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": true,
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~O", "at": "2026-09-25T05:40:00Z"}
  },
  {
    "id": "NFRA_MCPINDEX-W3-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The TrueShares holdings feed lands in bronze and is never converted to silver fact_holdings, although its converter exists and is wired. The silver completeness guard omits the feed from its 'expected' set, so it reports PASS over a tree missing an entire table.",
    "evidence": [
      "INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W3-S2",
      "this seat's live read 2026-09-25: DIVZ and IDVZ silver/fact_holdings 0, bronze/holdings 32 each; control trueshares/DIVZ/silver/ = 72",
      "data/assets/scripts/silver/etf_conversion.py:231-232, :279-347",
      "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S8"
    ],
    "remedy": "PARKED with owner 0.4.0_DS_ClientPlatform (DS owns silver scripts and their QA deploy, CLAUDE.md rule 13). Un-park condition: that seat live, or 1.0.0_SA_CTO~O names a live DS seat. Two acts: (1) find why the holdings feed is not converted (trigger, invocation or filter) and backfill 32 dates per fund; (2) make the guard's expected set count every feed it claims to cover, with a planted-missing-feed control. Until then the ETF tool cell proposes no TrueShares holdings tool (MX-a-7 AC6 already says so).",
    "owner": "0.4.0_DS_ClientPlatform",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "0.4.0_DS_ClientPlatform", "round": "v1"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "0.4.0_DS_ClientPlatform", "at": null}
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S13",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Black Diamond's asset_id->cusip bridge is built by a script no scheduler runs. Every asset first seen after its last build joins to a null cusip at ingestion.",
    "evidence": [
      "this seat's live read 2026-09-25: opal-data-bd silver/bd_assets_dim.parquet LastModified 2026-04-14T20:44:16Z",
      "data/black_diamond/scripts/silver/merge-daily-incremental.py:57, :292-334",
      "analysis-blackdiamond.result.md:40-47",
      "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S13"
    ],
    "remedy": "(1) Measure the null-cusip rate in silver transactions since 2026-04-14 and in any served figure that joins on cusip. (2) Schedule build_bd_assets_dim.py ahead of the daily merge, as a production schedule, not an ad-hoc run. (3) Cut no Black Diamond tool cell that answers by cusip until (1) reads. The write surface is Black Diamond's pipeline (DS), outside MCPINDEX; the issuer routes it.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null}
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Eclipse silver converter applies no row-level firm filter (0 calls to filter_to_inflection), so Inflection-only scope depends on the vendor connection being single-tenant, which no one has verified.",
    "evidence": ["analysis-eclipse.result.md:59-75", "POSITION_20260921_WIND_DOWN.md item 6", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S12"],
    "remedy": "Before any Eclipse tool cell is cut: one read of the distinct rep or firm identifiers across live Eclipse silver rows against the INFGRD allowlist. If all rows are inside it, record single tenancy with that read as evidence. If any row is outside it, the converter gains the filter before any tool serves the data.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null}
  },
  {
    "id": "NFRA_MCPINDEX-W1-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "MXC4-AC11's catalog limb required tool references that no cell had populated and that the cell could not create in grant.",
    "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S5", "AC11 ruling @5f3b4a20c6", "ROUND1_RULINGS.md@9c70622d13 R-1", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S9"],
    "remedy": "Per R-1: the re-cut cell is granted the ycharts, opal_portal and globgrph integration directories and classifies those 9 tools. It drains wk-nfra_mcpindex-1-1d as its base and releases NARROW. AC11's denominator is 49, graded 44 classified + 5 HELD (G-OPLGTW), never '44 of 44'. MX-c-4's AC8 judgment (read_teams_attachment SAFE) is graded at that cell's L9 BEFORE the branch drains.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false,
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~O", "at": "2026-09-25T05:40:00Z"}
  },
  {
    "id": "NFRA_MCPINDEX-W1-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Every invocation in the issuance pins `py -3.12`, a device-specific interpreter that site Z does not register.",
    "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S6", "TO-MX-a-1 MXA1-AC11 invocation", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S10"],
    "remedy": "Every re-cut face names a device-neutral interpreter (R-1 item 4). The 9 complete orders' probes carry the same pin, so a seat re-running one on site Z substitutes the interpreter and says so; their recorded instances stand.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-W1-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A validator the criterion must run writes a tracked report outside the cell's grant, so the worker had to revert it by hand after every run.",
    "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S3", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S5"],
    "remedy": "Either gitignore catalog_v02/validation_report.json as a regenerable report, or name it in the <paths> of any cell that runs the validator. The issuer picks one at the cut.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-W4-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "One bucket (opal-data-bd) physically holds data for three properties plus a served tier, so a bucket-level fence would cross properties.",
    "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W4-S1", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S3"],
    "remedy": "Every tool and read-fence cell (MX-t-*, MX-i-*) fences by exact key prefix, never by bucket, with a negative control that reads a sibling property's prefix and is refused.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S14",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The analysis cells' question lists are sourced from code and page briefs, not measured demand. Each leaves out at most one obvious question, and one routing follows a registry gap rather than fit.",
    "evidence": ["ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S14 (seven grades with limits)"],
    "remedy": "The tool cells carry these questions or name them unanswerable: model composition and weights (portal); a position diff between two dates (Schwab); relationship returns (Black Diamond); period returns per fund (ETFs). Correlations and factor tilts get their systems.json key and a purpose-built tool, or the cell states why the typed query fits them on merit. The S8 beta measurement replaces all of this with real demand.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S15",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The emitter's docstring summary line still names the staged file as its output, contradicting the correction three lines below it.",
    "evidence": ["workflows/atom_decomposition/emit_catalog_v02.py:2-5 at fec99f11cd", "ADJUDICATION_v1.md#NFRA_MCPINDEX-Z-C-S15"],
    "remedy": "The summary line names the live refs/DATA_CATALOG.yaml, in the round's batch cell. It is a docstring edit, with no logic change.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
