# MDPF_DEMQUE -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_DEMQUE-W<n>-S<k>`; seat rows `MDPF_DEMQUE-S<k>`.

```json
[
  {
    "id": "MDPF_DEMQUE-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-08T23:23:39Z",
    "one_line": "The Andrew ~23:0xZ record that places the Rival Funds Bloomberg price asks in this queue is cited as on CLOUD @0573ceb0c3, but neither the record nor its commit @86d85ab4a5 is readable on dell1 after a fetch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~DELL1 msgs 1232 and 1235: record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md @86d85ab4a5, 'reaches CLOUD via the laptop's integrate (CLOUD 0573ceb0c3)'",
        "2026-10-08T23:23:39Z: git fetch origin CLOUD -> origin/CLOUD = 0573ceb0c3; git cat-file -t 86d85ab4a5 -> 'Not a valid object name'; git ls-tree -r --name-only origin/CLOUD has no path matching 230xZ_SITEZ (positive control: the same ls-tree lists the MDPF_DEMQUE project.json)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "msg 1235: the record is an input to the first MDPF_DEMQUE decomposition and reaches dell1 with the next box-sync at CLOUD 0573ceb0c3.",
    "world_is": "CLOUD is at 0573ceb0c3 on origin and carries neither the record nor @86d85ab4a5. Round 1 is FWD-1 only, so the cut does not depend on it; the round-2 cut (tier 3, Rival Funds on Bloomberg) reads it first. Likely still on a box branch awaiting the laptop's next integrate."
  },
  {
    "id": "MDPF_DEMQUE-D1-W3-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~3",
    "surfaced_at": "2026-10-08T23:37:57Z",
    "one_line": "The order's face names Cottonwood's live bucket and three keys as literals, but the commit-time naming gate (ENFORCE) refuses a new literal of them in data/mdpf, so land_cot.py derives them instead of typing them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit of data/mdpf/scripts/demque/land_cot.py + test_demque_land.py (first attempt, base 6dc65d8cba): 'NAMING REFUSE land_cot.py:22 opal-data-cot -> opal-data-cottonwood' and 'NAMING REFUSE :23/:24 silver/transactions/, silver/historical_prices.parquet -> {source}/{scope}/silver/...' (NEW and OUT-OF-PATTERN as S3Key), naming-gate DENOMINATOR 2 path(s); a second attempt then refused the path component 'cot' -> lookup('cottonwood')",
        "lib/opal_naming.lookup('cottonwood') at 6dc65d8cba: bucket opal-data-cottonwood, but alias opal-data-cot carries planes ['bucket'], routed True, lookup False: the live data sits in the routed legacy bucket, which is what the consumer reads",
        "Landed at 9ca032bff5: BUCKET = the single routed bucket alias from lookup('cottonwood'); the three keys are read out of the consumer's own source (build_canonical_prices_v2.py, tree from lookup pipeline_trees), a miss is a loud SystemExit; both checks still pass (LAND-OK; LSEAM-OK ... join_key=cusip)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's THE CELL text states the bucket, the two Tier-2 keys and the transactions prefix as plain addresses to read and write.",
    "world_is": "The gate refuses a hand-typed form of each (Rule 30, R20), and the legacy layout has no address() form. Derivation from the consumer's source is the workaround used: it ties the lander to what the price build reads, but breaks if the consumer's key expressions are rewritten to non-literal forms. If the lander is migrated to the LGIC layout (R19) the keys change with it. Owner of that call: 2.0.0_SA_COO~Q1 / 1.0.0_SA_CTO."
  },
  {
    "id": "MDPF_DEMQUE-D1-W4-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~4",
    "surfaced_at": "2026-10-08T23:45:30Z",
    "one_line": "The cell premise that Cottonwood's gold run goes through gold_dispatch.sh (silver-prep S_00 only on --chain full) is false: the scheduled opal-cot-gold-run SSM document runs a fixed script list with no S_00 and never calls gold_dispatch.sh.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2026-10-08T23:37Z: aws ssm get-document --name opal-cot-gold-run -> runCommand list A_00..D_04, no S_00, no gold_dispatch.sh; infra/aws/terraform/cot-pipeline/ssm.tf:375-404 (grep S_00 = 0 hits)",
        "144 gold-run logs under s3://opal-data-cot/logs/cot-exporter/gold-run/ synced: 0 lines 'BUILD CANONICAL PRICES', 0 '=== S_00'; positive control: the same logs carry '=== A_00' 125 times",
        "trace: org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md Q1, Q2"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face DQ-t-5: gold_dispatch.sh:1069-1071 runs S_00 only when invoked --chain full, and Q1 asks which gold_dispatch.sh arguments the Cottonwood schedule passes.",
    "world_is": "No Cottonwood schedule passes any gold_dispatch.sh arguments; the only gold_dispatch.sh run ever logged on Cottonwood is a manual partial chain on 2026-06-26. Adding S_00 to hop 6 means editing the opal-cot-gold-run SSM document in Terraform, not choosing a dispatch flag."
  },
  {
    "id": "MDPF_DEMQUE-D1-W4-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~4",
    "surfaced_at": "2026-10-08T23:45:31Z",
    "one_line": "Cottonwood's live nightly run does not read canonical_prices.parquet on any page-feeding path: B_00 builds canonical holdings from BD-reported market value in silver/holdings and returns before load_canonical_prices(), and A_03's canonical_prices read is skipped.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/B_00.canonical_holdings.py:1095-1099 returns after _build_canonical_from_snapshot; load_canonical_prices() is at :1124",
        "s3://opal-data-cot/logs/cot-exporter/gold-run/cot-gold-run-20261008-113337.log: 'Holdings snapshot present (85 date(s)) -- canonical holdings from silver/holdings (BD-reported MV ...)' and A_03 'No unrealized data ... skipping buy injection' (silver/unrealized/unrealized_gain_loss.parquet is 404 live)",
        "portal/src has 0 hits for canonical_prices"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomp hop 6 and the DQ-t-5 cell: a new Yahoo row in silver/historical_prices.parquet reaches a Cottonwood client's page through canonical_prices.parquet.",
    "world_is": "Even with S_00 scheduled and the Tier-2 objects landed, no Cottonwood page value changes: pages are fed from gold/canonical/holdings built from silver/holdings market_value. Hop 6 needs a consumer decision (which holdings are Yahoo-priced), not only a schedule."
  }
]
```
