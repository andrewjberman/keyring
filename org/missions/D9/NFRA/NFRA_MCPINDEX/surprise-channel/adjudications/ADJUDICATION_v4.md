# NFRA_MCPINDEX ROUND 3 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`. **Written:** 2026-09-29T03:45:00Z. **Terminality:** 8 of 8 orders terminal (packet
`deliverables/2.0.0_SA_COO~MI/round3/L8_PACKET_ROUND3.md` @5b5ddd7800).

Input: `investigations/INVESTIGATION_v1.md`, 112 items by the channel gate's own census (`_latest_dispositions`), 19
UNDER_INVESTIGATION before this file (the packet's table lists the same 19; its text says 18). After it: 0.
15 dismissed, 4 graduated OPEN, and 2 new L9 findings graduated OPEN (Z-C-S28, Z-C-S29). Grades are in Z-C-S30.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S26",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-29T03:45:00Z",
    "one_line": "Round 3 L8: 15 rows DISMISSED_WITH_REASON -- issuer disarm and placement records whose effect this seat re-read, blockers resolved inside the round, and instrument limits that changed no result.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Re-read by this seat: Z-S48 (disarms Z-S42): the served dim written by the scheduled 22:10Z fire equals the G1 baseline on every column but built_at (s10.J1 below). Z-S49 (disarms Z-S47): the EventBridge rule bd-fees-pipeline-trigger does not exist (ResourceNotFoundException) and the Lambda bd-fees-trigger lookup errors, while the positive control bd-asset-dim-pipeline-trigger reads ENABLED cron(10 22 ? * MON-FRI *). Z-S53 and Z-W9-S1: CARRIER_CENSUS.md reads 0 fingerprints at HEAD against 2 at 1768215e19 (s13.J1 below). Z-W9-S2: extended-backfill.sh reads 0 fingerprints at both 1768215e19 and HEAD, so there was no second literal to remove. Z-S50 and Z-W11-S1: an instrument trap (a bare get-document reads DEFAULT, runs execute $LATEST); the issuer's standing rule to grade at $LATEST closes the mis-read, and aligning DEFAULT is carried with the dead legs. Resolved in round: Z-W8-S1 and its record Z-W8-S2 (the issuer's serial file; the 0/0/5 retirement applied); Z-W10-S2 (the deploy-only commit 0bce8d322a, whose gateway tree object 09ccfc39ad equals pin 3371f18803, deployed under both re-acked halves); Z-W13-S3 (CTO ruling @8ed938b2d7, MX-x-2 A1, complete @067dc14967). Instrument limits: Z-W13-S1 (AC3 reproduced the committed catalog, 0 differing lines); Z-W11-S3 (closed here: git -C portal grep over 1,784 tracked portal files at 8fa7abde finds 0 files naming canonical/lots_realized or lots_unrealized, positive control aum-metrics hits 3). Placement records: Z-S51 and Z-S52 record the issuer's placement of Z-W11-S2 and Z-W8-S3; the hazards they name are carried by those two rows' remediation rows (Z-C-S27).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "aws events describe-rule bd-fees-pipeline-trigger (ResourceNotFound) and bd-asset-dim-pipeline-trigger (ENABLED), read by this seat 2026-09-29 ~03:3xZ",
        "this seat's fingerprint scan (see Z-C-S30)",
        "git -C portal grep at portal 8fa7abde, 0 of 1,784 files"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W8-S1",
      "NFRA_MCPINDEX-Z-W8-S2",
      "NFRA_MCPINDEX-Z-W9-S1",
      "NFRA_MCPINDEX-Z-W9-S2",
      "NFRA_MCPINDEX-Z-W10-S2",
      "NFRA_MCPINDEX-Z-W11-S1",
      "NFRA_MCPINDEX-Z-W11-S3",
      "NFRA_MCPINDEX-Z-W13-S1",
      "NFRA_MCPINDEX-Z-W13-S3",
      "NFRA_MCPINDEX-Z-S48",
      "NFRA_MCPINDEX-Z-S49",
      "NFRA_MCPINDEX-Z-S50",
      "NFRA_MCPINDEX-Z-S51",
      "NFRA_MCPINDEX-Z-S52",
      "NFRA_MCPINDEX-Z-S53"
    ],
    "dismissal_reason": "Each row is a disarm or placement record whose effect this seat re-read, a blocker whose ruled act completed in round, or an instrument limit that changed no result; the two standing hazards named by the placement rows are carried by Z-W8-S3 and Z-W11-S2."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S27",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-29T03:45:00Z",
    "one_line": "Round 3 L8: 4 rows GRADUATED and OPEN -- the 4 dead BD Playwright legs that still read the portal secret daily, the skipped dim join in the transaction merge, 4 residual discover routing misses, and a catalog validator that makes live S3 reads.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W8-S3 (with placement Z-S52): allocation, realized, transaction and unrealized still read opal/bd/credentials and fail 21 of 21 at the MFA login (MX-m-1 (a), measured at $LATEST); the grant cannot be removed while they run; the BD account-lockout risk from about 4 failed logins per weekday is UNMEASURED. Z-W11-S2 (with placement Z-S51): the EC2 merge logs 'bd_assets_dim unavailable; skipping cusip join' in 10 of 10 file-processing runs and wrote 0-row partitions; the deployed script (43,492 B) is not the repo file (59,077 B); boto3 absence is inferred, not measured. Z-W10-S1: 23 of 27 route; Q22 lacks catalog vocabulary, Q09/Q13/Q25 are precision misses. Z-W13-S2: validate_catalog_v02.py makes live S3 reads under a No-AWS bound and 1 of 36 rows reads family_mismatch_or_error, unidentified.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md (each id adjudicated)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/MEASURE_BATCH_ROUND3.md (a), (b)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/L8_PACKET_ROUND3.md section 5"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W8-S3",
      "NFRA_MCPINDEX-Z-W11-S2",
      "NFRA_MCPINDEX-Z-W10-S1",
      "NFRA_MCPINDEX-Z-W13-S2"
    ]
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S28",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-29T03:45:00Z",
    "one_line": "L9 finding: opal_discover never names the purpose-built tool -- every next_tool is query_v0, including mp.01's, whose own tool mdpf_get_aum_metrics answered correctly when called directly.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-1: discover routes a cold question to the right tool.",
    "world_is": "This seat's live call opal_discover('model portfolio AUM') at 03:27:36Z returned 8 rows, 3 servable, each servable row's next_tool = query_v0 POST /query/v0. The same principal's direct call mdpf_get_aum_metrics(scope=global) at 03:27:43Z answered. The issuer's close run (CLOSE_RUN_MX-r-4_ISSUER.md, finding A) saw the same on all 4 surfaces. query_v0 is not in this session's tool list, so a user following the route cannot fetch at all from an MCP client that lacks it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opal-mcp-audit audit/dt=2026-09-29/2026-09-29T03:27:36.465136+00:00-19be1fd4.jsonl (opal_discover ok) and 03:27:43.747039-0f9c0a8f.jsonl (mdpf_get_aum_metrics ok)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/CLOSE_RUN_MX-r-4_ISSUER.md finding A"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S29",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-29T03:45:00Z",
    "one_line": "L9 finding: opal_discover's freshness latest_value is the catalog's CERTIFICATION vintage, labelled held (mp.01 2026-08-10), while the served object one call later carries 2026-09-25.",
    "class": "OBSERVATION",
    "spec_asserts": "A value carries its claim; a consumer must be able to reject on it (CLAUDE.md A VALUE MUST CARRY ITS CLAIM).",
    "world_is": "The claim label is honest ('held', 'not re-read from the served artifact'), so this is not a false value. But the date a user sees first is 7 weeks older than the data, and nothing in the answer says the served object is fresher. Read live by this seat (discover at 03:27:36Z; the served object platinum/mdpf/global/aum-metrics.json VersionId N_KOsRfVbwJr7danRAxFjAmYOfhCViGu, period 2026-09-25).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's opal_discover call 2026-09-29T03:27:36Z",
        "s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json VersionId N_KOsRfVbwJr7danRAxFjAmYOfhCViGu, read by this seat",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/CLOSE_RUN_MX-r-4_ISSUER.md finding B"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S30",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-29T03:45:00Z",
    "one_line": "L9 grades, round 3: s10.J1 PASS, s13.J1 PASS, m1.J1 PASS, r4.J1 FAIL (1 of 4 A2 surfaces answered with the portal's figure and as-of). G-A live-cert: G6 PASS, G7 PASS by bytes identity, G5 PARTIAL (the catalog deny is exercised live; the other-firm and unresolved-principal arms cannot be exercised from a master session).",
    "class": "OBSERVATION",
    "spec_asserts": "Judgment criteria are graded at L9 by the CVO, never self-graded; 1.0.0_SA_CTO~O asked this seat (msg 26268) to live-cert G5-G7 after the enable.",
    "world_is": "s10.J1: re-measured by this seat from the S3 versions. qcSdLjLW (the 22:11:33Z fire) vs kittUyy (G1): 12,141 = 12,141 ids, 0 added, 0 removed, non-null cusip 10,957 = 10,957, non-null->null 0, non-null->non-null changed 0; the only differing column is built_at. MX-s-6's 42 is located: V0 4dfwFf (2026-04-14) -> pdoQY5 (06:22Z) is 42 non-null->non-null changes plus 1,204 added ids, a one-time catch-up of a 5-month-stale dim; every later pair reads 0. s13.J1: the Z-C-S24 detector ([A-Z][a-z]{7}[0-9]{3}, sha256 prefix, no value printed) over the 8 files reads 8 hits in 7 files at 1768215e19 (positive control) and 0 at HEAD 6b96404067; over all 43,706 tracked text files (46,421 tracked; working-tree bytes) it reads 0, where round 2 read 6 -- so Z-S31's value-out-of-tracked-files half is MET at HEAD; rotation and the unscrubbed history remain Andrew's. m1.J1: each of (a)-(d) names its question, instrument and denominator on the right population ($LATEST documents; the dim by VersionId; B_01's own cash predicate; the consumer census), and each zero names its cause; (d)'s one gap, the portal source, is closed here with 0 of 1,784 files. r4.J1: graded on CLOSE_RUN_MX-r-4_ISSUER.md plus this seat's own independent read: platinum/mdpf answers EQUAL (total.aum 2,083,228,453.05, 8,242 accounts, as-of 2026-09-25, the same VersionId N_KOsRfV... read directly); platinum/etfs mis-routes to positioning rows; platinum/advi is NOT_CATALOGUED; json/* routes to the right family but no figure is fetched. G6: the served lake holds this seat's three calls, opal_discover ok, mdpf_get_aum_metrics ok, and the refused scope 'archive' as outcome error with detail 'refused: ... not a member of the catalog row', each tier-stamped master_admin. G7: the host serves 0bce8d322a whose gateway tree object equals the G-A pin's (09ccfc39ad), with ENABLED_INTEGRATIONS naming exactly the 5 ids (the issuer's live SSM read, r4.AC2), so the in-process fail-closed result at the pin holds for the deployed bytes. G5: the catalog deny refused before any read (no key was named in the answer); the below-tier deny is vacuous by construction (read_only floor); the other-firm arm needs a non-master principal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-bd/silver/bd_assets_dim.parquet VersionIds qcSdLjLW..., kittUyy..., pdoQY5..., 4dfwFf..., read by this seat 2026-09-29 ~03:2xZ",
        "fingerprint scan outputs, this seat, 2026-09-29 ~03:1xZ-03:4xZ (no value printed or stored)",
        "opal-mcp-audit audit/dt=2026-09-29/ 03:27:36-19be1fd4, 03:27:43-0f9c0a8f, 03:28:30-693b998a",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/CLOSE_RUN_MX-r-4_ISSUER.md",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/MEASURE_BATCH_ROUND3.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "MXS12-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~8/NFRA_MCPINDEX.TO-MX-s-12.bd-asset-dim-phase-b.proof_of_spec.json@3e71e48d7e",
        "verdict": "PASS",
        "reason": "The dim the scheduled fire wrote is one a BD tool may answer from: ids 12,141 >= G1's 12,141, 0 non-null->null, 0 cusip changes, and MX-s-6's 42 is located in the April->06:22Z catch-up, not in this fire."
      },
      {
        "criterion": "MXS13-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~9/NFRA_MCPINDEX.TO-MX-s-13.bd-password-redaction.proof_of_spec.json@fc509329ec",
        "verdict": "PASS",
        "reason": "0 live-credential fingerprints in the 8 files at HEAD against 8 at the control commit; 0 across all tracked text files."
      },
      {
        "criterion": "MXM1-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/NFRA_MCPINDEX.TO-MX-m-1.bd-measure-batch.proof_of_spec.json@661bf81294",
        "verdict": "PASS",
        "reason": "Each measure answers its question on the right population with its instrument and denominator, and every zero names its cause; the one population gap (portal source in (d)) reads 0 when closed."
      },
      {
        "criterion": "MXR4-J1",
        "instance": "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~10/NFRA_MCPINDEX.TO-MX-r-4.thread-live-enable.proof_of_spec.json@9f70db3237",
        "verdict": "FAIL",
        "reason": "1 of 4 A2 surfaces answered with the figure and as-of the portal serves (platinum/mdpf, EQUAL). etfs mis-routed, advi not catalogued, json/* routed with no figure. FWD-2 is not realized; Z-W2-S8 (etfs), Z-C-S28 and Z-C-S29 are the named causes."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
