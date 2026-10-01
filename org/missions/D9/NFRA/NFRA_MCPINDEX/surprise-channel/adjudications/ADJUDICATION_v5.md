# NFRA_MCPINDEX -- round 5, CVO observations ahead of the L8 compile (site Z)

Author: 3.0.0_SA_CVO~O. Round: 5 (L7 open; this document opens the round-5 adjudication and the L8 compile appends
here). Fabric: site-z. Written: 2026-09-30T20:5xZ.

Z-C-S31 records a live measurement that 1.0.0_SA_CTO~O ruled to the round-5 slug (msg 27366), carried here so that
it is evidence in the slug and not a message.

```json
[
  {
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-30T19:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_MCPINDEX-Z-C-S31",
    "one_line": "After MX-r-6 v3 went live (42c52ed4d9, 18:33:41Z; 6 Schwab/query tools served), the index still cannot route to them: live opal_discover('Schwab positions') returns catalogued:false with no dataset and no tool named. No catalog row exists for any Schwab dataset.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Live call by 3.0.0_SA_CVO~O through the opalgateway MCP at ~19:1xZ, after the v3 read-back (2.0.0_SA_COO~MI msg 27332): opal_discover('Schwab positions') -> {catalog.version 0.3, catalogued false, matches []}. The same call at ~07:2xZ returned the same, before any Schwab tool was live.",
        "The cell that owned the Schwab catalog rows, MX-t-2 (EMIT/catalog_entries/schwab_* + CAT), has been SUPERSEDED since 2026-09-24 and never started; no live round-5 cell holds it (1.0.0_SA_CTO~O msg 27366).",
        "PRD ACCEPT FWD-1: 'a question about a property that is not catalogued says so and names nothing' is true here, but FWD-1's outcome is routing to the right tool, and FWD-3's live exercise now has a served tool with no route to it."
      ]
    },
    "spec_asserts": "FWD-1 / FWD-3: a cold Schwab question is routed by the index to the purpose-built Schwab tool, with freshness and scope.",
    "world_is": "The Schwab tools are served and a grant exists (Alyssa, 19:15:29Z), but discover returns not-catalogued for Schwab subjects, so a cold asker reaches them only by knowing the tool names. Ruled to the round-5 slug as the FWD-1/FWD-3 catalog row (1.0.0_SA_CTO~O msg 27366)."
  }
]
```

-- 3.0.0_SA_CVO~O


## Rounds 4+5 L8 compile + L9 (3.0.0_SA_CVO~O, 2026-10-01T08:20:00Z)

Input: `investigations/INVESTIGATION_v1.md`, 94 UNDER_INVESTIGATION by the channel gate's own census (`_latest_dispositions`) before this block, plus Z-C-S31 above. The packet counts 60 for round 5; the other 34 are round 4's (W14-W17, S54-S60), never compiled. After this block: 0. Packet: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/L8_PACKET_ROUND5.md@81887e8ae8`.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S32",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-01T08:20:00Z",
    "one_line": "Rounds 4+5 L8: 82 rows DISMISSED_WITH_REASON -- issuer rulings and disarms whose effect was re-read, release records under audited precedent, instrument limits that changed no result, and 17 companions carried by their lead slug row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Issuer ruling and disarm rows whose effect this seat re-read or that the round's own record shows done: Z-S54..S56, S58..S60, S62..S66, S70 (rulings), S71 disarms S68 (plan A ran: ~RV restored 4ce7946426, IAM rollback 0/1/0; the stale-base guard shipped in 42c52ed4d9 and guarded OG-t-2 and MX-r-7), S69 resolves S61. Rows they disarm or rule: Z-W14-S5 (egress declared, Z-S58), Z-W15-S2 (INDEX_TOOLS, Z-S55, landed with Z-W15-S6), Z-W15-S5 and S6 (R20 X11 entries admit the etfs literals), Z-W16-S1 (Z-S54), Z-W17-S1/S2/S4 (lapse with A1, Z-S60), Z-W17-S5 and S7 (Z-S56), Z-W19-S2 (contract lists dim_transaction: 3 hits in org/standards/NFRA_OPLGTW_CONTRACT.json, read here), Z-W19-S7/S8 (Z-S66), Z-W21-S1/S3 (Z-S62; writer named in Z-W21-S16), Z-W21-S9/S10 (R20 entries @0d71a22887). Release records under audited precedent: Z-W14-S7..S12, Z-W19-S10/S11/S14/S19, Z-W21-S14 (overrides on never-merged rel-/dep- branches; deploy-only trees drop other projects' unreleased files, none ships). Records and instrument limits that changed no result: Z-W14-S1/S2/S3 (S3 subsumed by OPEN Z-W10-S1, whose remedy grades recall), Z-W17-S3 (the port that would write beside TRANSACTIONS_DAILY_ was dropped), Z-W17-S6, Z-W19-S1, S3, S5, S6, S12, S15, S18, Z-W20-S1, Z-W21-S2, S4 (graded under a8.J1), S5 (grade('opal/mcp/opal-gateway-blackdiamond-reader-external-id','SECRET') reads CONFORMANT, run here), S8, S11, S16, S18 (an ExternalId is a confused-deputy guard, not a credential; it sits in the policy document as a Condition literal), S20. Z-W19-S20 (r6.AC1 pins the v2 slug): the AC's object was wrong, not the world -- this seat read the v3 entry 20260930T1815Z_nfra-mcpindex-r5-schwab-enable-v3_deploy_completion.md CLOSED at HEAD with no v3 sentinel.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/L8_PACKET_ROUND5.md@81887e8ae8",
        "git ls-tree HEAD org/critical_paths/change_management/ and .open_deploys/, read by this seat 2026-10-01 ~08:1xZ",
        "lib/opal_naming.py grade(), run by this seat 2026-10-01 ~08:1xZ"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S54",
      "NFRA_MCPINDEX-Z-S55",
      "NFRA_MCPINDEX-Z-S56",
      "NFRA_MCPINDEX-Z-S58",
      "NFRA_MCPINDEX-Z-S59",
      "NFRA_MCPINDEX-Z-S60",
      "NFRA_MCPINDEX-Z-S61",
      "NFRA_MCPINDEX-Z-S62",
      "NFRA_MCPINDEX-Z-S63",
      "NFRA_MCPINDEX-Z-S64",
      "NFRA_MCPINDEX-Z-S65",
      "NFRA_MCPINDEX-Z-S66",
      "NFRA_MCPINDEX-Z-S67",
      "NFRA_MCPINDEX-Z-S68",
      "NFRA_MCPINDEX-Z-S70",
      "NFRA_MCPINDEX-Z-S71",
      "NFRA_MCPINDEX-Z-W14-S1",
      "NFRA_MCPINDEX-Z-W14-S10",
      "NFRA_MCPINDEX-Z-W14-S11",
      "NFRA_MCPINDEX-Z-W14-S12",
      "NFRA_MCPINDEX-Z-W14-S2",
      "NFRA_MCPINDEX-Z-W14-S3",
      "NFRA_MCPINDEX-Z-W14-S4",
      "NFRA_MCPINDEX-Z-W14-S5",
      "NFRA_MCPINDEX-Z-W14-S6",
      "NFRA_MCPINDEX-Z-W14-S7",
      "NFRA_MCPINDEX-Z-W14-S8",
      "NFRA_MCPINDEX-Z-W14-S9",
      "NFRA_MCPINDEX-Z-W15-S1",
      "NFRA_MCPINDEX-Z-W15-S2",
      "NFRA_MCPINDEX-Z-W15-S4",
      "NFRA_MCPINDEX-Z-W15-S5",
      "NFRA_MCPINDEX-Z-W15-S6",
      "NFRA_MCPINDEX-Z-W16-S1",
      "NFRA_MCPINDEX-Z-W17-S1",
      "NFRA_MCPINDEX-Z-W17-S2",
      "NFRA_MCPINDEX-Z-W17-S3",
      "NFRA_MCPINDEX-Z-W17-S4",
      "NFRA_MCPINDEX-Z-W17-S5",
      "NFRA_MCPINDEX-Z-W17-S6",
      "NFRA_MCPINDEX-Z-W17-S7",
      "NFRA_MCPINDEX-Z-W19-S1",
      "NFRA_MCPINDEX-Z-W19-S10",
      "NFRA_MCPINDEX-Z-W19-S11",
      "NFRA_MCPINDEX-Z-W19-S12",
      "NFRA_MCPINDEX-Z-W19-S14",
      "NFRA_MCPINDEX-Z-W19-S15",
      "NFRA_MCPINDEX-Z-W19-S16",
      "NFRA_MCPINDEX-Z-W19-S17",
      "NFRA_MCPINDEX-Z-W19-S18",
      "NFRA_MCPINDEX-Z-W19-S19",
      "NFRA_MCPINDEX-Z-W19-S2",
      "NFRA_MCPINDEX-Z-W19-S20",
      "NFRA_MCPINDEX-Z-W19-S21",
      "NFRA_MCPINDEX-Z-W19-S3",
      "NFRA_MCPINDEX-Z-W19-S4",
      "NFRA_MCPINDEX-Z-W19-S5",
      "NFRA_MCPINDEX-Z-W19-S6",
      "NFRA_MCPINDEX-Z-W19-S7",
      "NFRA_MCPINDEX-Z-W19-S8",
      "NFRA_MCPINDEX-Z-W19-S9",
      "NFRA_MCPINDEX-Z-W20-S1",
      "NFRA_MCPINDEX-Z-W20-S2",
      "NFRA_MCPINDEX-Z-W20-S4",
      "NFRA_MCPINDEX-Z-W20-S5",
      "NFRA_MCPINDEX-Z-W21-S1",
      "NFRA_MCPINDEX-Z-W21-S10",
      "NFRA_MCPINDEX-Z-W21-S11",
      "NFRA_MCPINDEX-Z-W21-S13",
      "NFRA_MCPINDEX-Z-W21-S14",
      "NFRA_MCPINDEX-Z-W21-S16",
      "NFRA_MCPINDEX-Z-W21-S17",
      "NFRA_MCPINDEX-Z-W21-S18",
      "NFRA_MCPINDEX-Z-W21-S2",
      "NFRA_MCPINDEX-Z-W21-S20",
      "NFRA_MCPINDEX-Z-W21-S21",
      "NFRA_MCPINDEX-Z-W21-S3",
      "NFRA_MCPINDEX-Z-W21-S4",
      "NFRA_MCPINDEX-Z-W21-S5",
      "NFRA_MCPINDEX-Z-W21-S6",
      "NFRA_MCPINDEX-Z-W21-S8",
      "NFRA_MCPINDEX-Z-W21-S9"
    ],
    "dismissal_reason": "Each row is a ruling or disarm whose effect is read, a release record under the audited rel-/dep- precedent, a limit that changed no result, or a COMPANION whose hazard is carried by its lead row in REMEDIATION_v4 (companion -> lead: Z-S67 -> Z-W20-S3; Z-W14-S4 -> Z-W21-S7; Z-W14-S6 -> Z-W21-S15; Z-W15-S1 -> Z-W21-S7; Z-W15-S4 -> Z-W21-S15; Z-W19-S16 -> Z-W19-S13; Z-W19-S17 -> Z-W21-S15; Z-W19-S21 -> Z-W21-S23; Z-W19-S4 -> Z-W21-S15; Z-W19-S9 -> Z-W19-S13; Z-W20-S2 -> Z-W21-S15; Z-W20-S4 -> Z-W20-S3; Z-W20-S5 -> Z-W20-S3; Z-W21-S13 -> Z-W21-S12; Z-W21-S17 -> Z-W21-S12; Z-W21-S21 -> Z-W21-S23; Z-W21-S6 -> Z-W21-S15)."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S33",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-01T08:20:00Z",
    "one_line": "Rounds 4+5 L8: 13 rows GRADUATED as 12 OPEN slug rows (REMEDIATION_v4), led by discover never reading silver_datasets (BD + Schwab unroutable), MX-t-12 non-terminal, and the un-plannable gateway TF root.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "See remediations/REMEDIATION_v4.md: one row per lead id, companions listed in its evidence.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "remediations/REMEDIATION_v4.md",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/L8_PACKET_ROUND5.md@81887e8ae8"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S57",
      "NFRA_MCPINDEX-Z-S69",
      "NFRA_MCPINDEX-Z-W15-S3",
      "NFRA_MCPINDEX-Z-W19-S13",
      "NFRA_MCPINDEX-Z-W19-S22",
      "NFRA_MCPINDEX-Z-W20-S3",
      "NFRA_MCPINDEX-Z-W21-S12",
      "NFRA_MCPINDEX-Z-W21-S15",
      "NFRA_MCPINDEX-Z-W21-S19",
      "NFRA_MCPINDEX-Z-W21-S22",
      "NFRA_MCPINDEX-Z-W21-S23",
      "NFRA_MCPINDEX-Z-W21-S7",
      "NFRA_MCPINDEX-Z-C-S31"
    ]
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S34",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-01T08:20:00Z",
    "one_line": "L9 grades, round 5: a8.J1 PASS with limits; r7.J1 FAIL (route clause UNMET, re-measured live; VersionId figure check not done); r6.J1 NOT_EVALUATED (the cold run has not run, and would fail its Schwab clause until Z-W21-S22 lands).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded.",
    "world_is": "Graded below against each criterion's text and the order's amendments.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/analysis-blackdiamond.r5.result.md",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/R7_J1_PRINCIPAL_SESSION_20261001.md",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/L8_PACKET_ROUND5.md@81887e8ae8",
        "this seat's live opal_discover calls 2026-10-01 ~08:1xZ (catalog 0.4): BD fees and Schwab positions catalogued=false; ETF positioning -> etfs_get_positioning"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "MXA8-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/NFRA_MCPINDEX.TO-MX-a-8.analysis-blackdiamond-r5.proof_of_spec.json@4be9c0bb0a",
        "verdict": "PASS",
        "reason": "A builder holding only the record can cut the first tool: ONE question class (fees by account/relationship for a date range), ONE tool (blackdiamond_list_fees; the bd_ prefix is C3-invalid and the substitution is ruled by Z-S62), an exact fence down to the IAM shape (GetObject on opal-data-bd/silver/fees/*, ListBucket conditioned on that prefix), a scope rule (scope=49financial argument, z08 account-id assertion fail-closed), and read times on every live fact (listing 08:50Z, per-object 08:5xZ-09:05Z, legend MEASURED/CODE/INFERRED). Empirical check: MX-t-13 was cut from it and its in-process call succeeded. Limits: the z08 scan covers the newest partitions, not full history (the record says so); the rule 'refused when the principal's firm is not 49financial' left Opal-internal undecided and the builder resolved it from PRD 10.8 (Z-W21-S4); the fees writer was unattributed at read time (named later, Z-W21-S16)."
      },
      {
        "criterion": "MXR7-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/NFRA_MCPINDEX.TO-MX-r-7.bd-release.proof_of_spec.json@9d1fff079d",
        "verdict": "FAIL",
        "reason": "Clause 'the route discover gave names that tool' is UNMET: issuer's ask and this seat's independent re-read both return catalogued=false for the BD fees question (cause: Z-W21-S22). Clause 'figure and as-of equal the source object read by VersionId' was not performed by anyone; the only call is the worker's in-process one (as_of 2026-09-29, rows_matched 22853, 632 duplicate transaction_ids before de-duplication), not a principal-session answer. Met: the analysis record, the tool list (58 -> 60, +blackdiamond_list_fees, +etfs_get_positioning). Re-grade after Z-W21-S22 lands, from a session whose tool list postdates 07:13Z."
      },
      {
        "criterion": "MXR6-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~19/NFRA_MCPINDEX.TO-MX-r-6.schwab-enable-release.proof_of_spec.json@1cdbe5df21",
        "verdict": "NOT_EVALUATED",
        "reason": "No material: the cold run needs Alyssa (A6, Andrew 'agreed' @29bc46d827) and has not run. Two notes for the run. (1) It fails by construction until Z-W21-S22 lands: live discover says 'Schwab positions' is not catalogued, and J1 requires discover to name the next tool. Run it after the repair, not before. (2) The criterion comment still carries A2's text ('No grant is widened in round 5'; the transaction question PASSES as a refusal); A5 supersedes it (the transaction question is ANSWERED) and the grant was written with dim_transaction (@c9be59c0c7). This seat grades against A5. The wait is essential (a person is the instrument by Andrew's word) and is carried in the slug."
      }
    ]
  }
]
```
