# AMGT_RESAPP -- round 100 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-12T05:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T05:25:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 4274,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round100/DRAIN_END_PACKET.md @756b450096 (blob 4105169819, sha256 9f00f66b..., verified).
3 of 3 orders complete, no JUDGMENT criterion. Pins resolved by content (C-S101); bg-3's no-byte-moved claim holds on RA1's compare (C-S102); L9 HOLDS
on this seat's timed live reads (C-S103); /15 moves ROG's C-S64 example out of the period grid (C-S104, noted, AMGT_CORPUS's carrier). 1 row swept since
v120 (watermark 2026-10-12T01:15Z; 1 of 1077 investigation rows after it): dismissed. No BLOCKING or ARMED row is open on this project's carrier.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S101",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T05:25:00Z",
    "one_line": "Deploy pins resolved BY CONTENT. The function is $LATEST only (list-versions-by-function: no published version), so bg-1's own package 7DUlZxhl.. cannot be fetched now; the live package is bg-3's: CodeSha256 42z0tn68TZjuk8awBclnMii0k+FX2Pw2bw7iN9Xitz0= (LastModified 04:18:21Z), its zip sha256 equal to it, 408 members. 151 members map to bg-3's merged pin ba22af15f5 and all 151 are byte-equal to the pin's blobs; lambda_function.py equals the pin's infra entry by blob (70f22815375a); the other 256 are vendored libraries. bg-1's pin 6e8dcaf414 and bg-3's pin differ in packaged code ONLY in lib/research/api/scoped_amgt.py (9b13bf0371d4 -> 9f72b58aa87e, bg-2's one S3 client; plus a test file that is not packaged), so bg-1's /15 content is live through bg-3: dossier.py reads 7b67bf62afdd in the live package, at both pins and at HEAD; monthly_chatter.py 38e9511ccc9c unchanged. Both pins are ancestors of box/dell1 HEAD (merged pins).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Deploy pins resolved BY CONTENT. The function is $LATEST only (list-versions-by-function: no published version), so bg-1's own package 7DUlZxhl.. cannot be fetched now; the live package is bg-3's: CodeSha256 42z0tn68TZjuk8awBclnMii0k+FX2Pw2bw7iN9Xitz0= (LastModified 04:18:21Z), its zip sha256 equal to it, 408 members. 151 members map to bg-3's merged pin ba22af15f5 and all 151 are byte-equal to the pin's blobs; lambda_function.py equals the pin's infra entry by blob (70f22815375a); the other 256 are vendored libraries. bg-1's pin 6e8dcaf414 and bg-3's pin differ in packaged code ONLY in lib/research/api/scoped_amgt.py (9b13bf0371d4 -> 9f72b58aa87e, bg-2's one S3 client; plus a test file that is not packaged), so bg-1's /15 content is live through bg-3: dossier.py reads 7b67bf62afdd in the live package, at both pins and at HEAD; monthly_chatter.py 38e9511ccc9c unchanged. Both pins are ancestors of box/dell1 HEAD (merged pins).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO lambda get-function + package download 2026-10-12T05:0xZ; per-member git blob hash vs git ls-tree -r ba22af15f5: 151 of 151 equal",
        "3.0.0_SA_CVO lambda list-versions-by-function opal-amgt-scoped-api: $LATEST only",
        "git diff --name-only 6e8dcaf414 ba22af15f5 -- lib/ infra/aws/lambda/research/scoped_amgt_api/: scoped_amgt.py and its test"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Deploy pins resolved BY CONTENT. The function is $LATEST only (list-versions-by-function: no published version), so bg-1's own package 7DUlZxhl.. cannot be fetched now; the live package is bg-3's: CodeSha256 42z0tn68TZjuk8awBclnMii0k+FX2Pw2bw7iN9Xitz0= (LastModified 04:18:21Z), its zip sha256 equal to it, 408 members. 151 members map to bg-3's merged pin ba22af15f5 and all 151 are byte-equal to the pin's blobs; lambda_function.py equals the pin's infra entry by blob (70f22815375a); the other 256 are vendored libraries. bg-1's pin 6e8dcaf414 and bg-3's pin differ in packaged code ONLY in lib/research/api/scoped_amgt.py (9b13bf0371d4 -> 9f72b58aa87e, bg-2's one S3 client; plus a test file that is not packaged), so bg-1's /15 content is live through bg-3: dossier.py reads 7b67bf62afdd in the live package, at both pins and at HEAD; monthly_chatter.py 38e9511ccc9c unchanged. Both pins are ancestors of box/dell1 HEAD (merged pins)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S102",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T05:25:00Z",
    "one_line": "bg-3 'no served byte moved': holds on the compare the applier recorded (deliverables/0.7.0_AE_CloudOps~RA1/BG3_POST_APPLY_COMPARE_20261012.json): baseline 528 requests 04:10:04Z-04:15:42Z on 7DUlZxhl.., replay 528 requests 04:19:18Z-04:22:46Z on 42z0tn68.., single reader; status moved 0, missing 0, function errors 0, 37 changed paths all clocks (generated_at 35, read_at 2), non-clock 0, outside the table 0; pool-full warnings 78 before the apply, 0 after, 0 after the quiet period; warm median 0.55 -> 0.39 s, max 28.04 -> 3.38 s. bg-3 writes no S3 object, so a VersionId read does not apply; the evidence is the served responses. This seat's own after-read agrees: the whole-body compare below reads 0 non-clock, non-float paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "bg-3 'no served byte moved': holds on the compare the applier recorded (deliverables/0.7.0_AE_CloudOps~RA1/BG3_POST_APPLY_COMPARE_20261012.json): baseline 528 requests 04:10:04Z-04:15:42Z on 7DUlZxhl.., replay 528 requests 04:19:18Z-04:22:46Z on 42z0tn68.., single reader; status moved 0, missing 0, function errors 0, 37 changed paths all clocks (generated_at 35, read_at 2), non-clock 0, outside the table 0; pool-full warnings 78 before the apply, 0 after, 0 after the quiet period; warm median 0.55 -> 0.39 s, max 28.04 -> 3.38 s. bg-3 writes no S3 object, so a VersionId read does not apply; the evidence is the served responses. This seat's own after-read agrees: the whole-body compare below reads 0 non-clock, non-float paths.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~RA1/BG3_POST_APPLY_COMPARE_20261012.json (replay, diffs 37, pool_full_warnings_by_phase)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "bg-3 'no served byte moved': holds on the compare the applier recorded (deliverables/0.7.0_AE_CloudOps~RA1/BG3_POST_APPLY_COMPARE_20261012.json): baseline 528 requests 04:10:04Z-04:15:42Z on 7DUlZxhl.., replay 528 requests 04:19:18Z-04:22:46Z on 42z0tn68.., single reader; status moved 0, missing 0, function errors 0, 37 changed paths all clocks (generated_at 35, read_at 2), non-clock 0, outside the table 0; pool-full warnings 78 before the apply, 0 after, 0 after the quiet period; warm median 0.55 -> 0.39 s, max 28.04 -> 3.38 s. bg-3 writes no S3 object, so a VersionId read does not apply; the evidence is the served responses. This seat's own after-read agrees: the whole-body compare below reads 0 non-clock, non-float paths."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S103",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T05:25:00Z",
    "one_line": "L9 read of the round-100 packet section 2 (no JUDGMENT criterion), each live read timed because this seat cannot announce itself to the applier. 05:06:07Z: live CodeSha256 42z0tn68... 05:07:43Z-05:12:40Z, one reader at a time: R97 SECTOR SERVE, R95 CLASSIFICATION, R94 NAME, R95 CASING, R92 MINOR-UNIT CENSUS YES; R89 PEERS DEPLOYED YES; R89 DEPLOYED CLOSE YES with P1 amgt-corpus-dossier/15; this seat's census 0 minor-unit rows. 05:12:40Z-05:15:01Z: r100_cold_check.py 4 of 4, R100 COLD REQUEST: YES; r100_pool_peak.py 'overall per-client maximum 20 over 35 reads; reads with a client above its own pool: 0', R100 POOL PEAK (the checkout's handler on the live pool). 05:15:01Z-05:16:55Z: r98_thesis_fullbody_compare.py (default --after local; the live function against the checkout handler, whose packaged files equal the live package): 95 of 95 read, 0 failed, 19 changed paths = 18 float_repr (the checkout's Python 3.14 print; the same 18 the issuer names) + 1 clock, 0 under model.team_sheet, 0 other. A partial day-after read, 04:18:21Z-05:18:29Z (Logs Insights): 3,077 REPORT lines, 11 over 20 s, 0 'Connection pool is full' lines; this hour includes the applier's, the issuer's and this seat's cold reads, so it is not bg-3's close (the 24-hour read is the issuer's). round-close-check --round 100: 3 of 3, judgment 0, MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of the round-100 packet section 2 (no JUDGMENT criterion), each live read timed because this seat cannot announce itself to the applier. 05:06:07Z: live CodeSha256 42z0tn68... 05:07:43Z-05:12:40Z, one reader at a time: R97 SECTOR SERVE, R95 CLASSIFICATION, R94 NAME, R95 CASING, R92 MINOR-UNIT CENSUS YES; R89 PEERS DEPLOYED YES; R89 DEPLOYED CLOSE YES with P1 amgt-corpus-dossier/15; this seat's census 0 minor-unit rows. 05:12:40Z-05:15:01Z: r100_cold_check.py 4 of 4, R100 COLD REQUEST: YES; r100_pool_peak.py 'overall per-client maximum 20 over 35 reads; reads with a client above its own pool: 0', R100 POOL PEAK (the checkout's handler on the live pool). 05:15:01Z-05:16:55Z: r98_thesis_fullbody_compare.py (default --after local; the live function against the checkout handler, whose packaged files equal the live package): 95 of 95 read, 0 failed, 19 changed paths = 18 float_repr (the checkout's Python 3.14 print; the same 18 the issuer names) + 1 clock, 0 under model.team_sheet, 0 other. A partial day-after read, 04:18:21Z-05:18:29Z (Logs Insights): 3,077 REPORT lines, 11 over 20 s, 0 'Connection pool is full' lines; this hour includes the applier's, the issuer's and this seat's cold reads, so it is not bg-3's close (the 24-hour read is the issuer's). round-close-check --round 100: 3 of 3, judgment 0, MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran the deployed censuses, the r89 pair (--want amgt-corpus-dossier/15) and org/tier1_exec/3.0.0_SA_CVO/deliverables/checks/amgt_minor_unit_census.py 05:07:43Z-05:12:40Z",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round100_prep/checks/r100_cold_check.py and r100_pool_peak.py 05:12:40Z-05:15:01Z",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round98_prep/checks/r98_thesis_fullbody_compare.py 05:15:01Z-05:16:55Z (its output, written to a stray ./--help, read and deleted)",
        "3.0.0_SA_CVO Logs Insights /aws/lambda/opal-amgt-scoped-api 04:18:21Z-05:18:29Z",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_RESAPP --round 100: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of the round-100 packet section 2 (no JUDGMENT criterion), each live read timed because this seat cannot announce itself to the applier. 05:06:07Z: live CodeSha256 42z0tn68... 05:07:43Z-05:12:40Z, one reader at a time: R97 SECTOR SERVE, R95 CLASSIFICATION, R94 NAME, R95 CASING, R92 MINOR-UNIT CENSUS YES; R89 PEERS DEPLOYED YES; R89 DEPLOYED CLOSE YES with P1 amgt-corpus-dossier/15; this seat's census 0 minor-unit rows. 05:12:40Z-05:15:01Z: r100_cold_check.py 4 of 4, R100 COLD REQUEST: YES; r100_pool_peak.py 'overall per-client maximum 20 over 35 reads; reads with a client above its own pool: 0', R100 POOL PEAK (the checkout's handler on the live pool). 05:15:01Z-05:16:55Z: r98_thesis_fullbody_compare.py (default --after local; the live function against the checkout handler, whose packaged files equal the live package): 95 of 95 read, 0 failed, 19 changed paths = 18 float_repr (the checkout's Python 3.14 print; the same 18 the issuer names) + 1 clock, 0 under model.team_sheet, 0 other. A partial day-after read, 04:18:21Z-05:18:29Z (Logs Insights): 3,077 REPORT lines, 11 over 20 s, 0 'Connection pool is full' lines; this hour includes the applier's, the issuer's and this seat's cold reads, so it is not bg-3's close (the 24-hour read is the issuer's). round-close-check --round 100: 3 of 3, judgment 0, MAY-CLOSE."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S104",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T05:25:00Z",
    "one_line": "AMGT_CORPUS's ARMED row AMGT_CORPUS-D1-C-S64 (case-block rows rendered under history-year headers) IS touched by /15: one live read of ROG_SW_Equity's model.team_sheet at 05:18:12Z finds the row's own example 660.4543... only at team_sheet.blocks[0].rows[4].cells[2], a separate case block (row_counts BLOCK 10, FIGURE 85), not in the period grid of 2016..2029 where round 99's read on /14 still found it. Measured on one of the 13 names; the 62-row close and its DEV render census are AMGT_CORPUS's (C1's census reads 0 values under a foreign header, per the packet). Noted here; the row stays on AMGT_CORPUS's REMEDIATION_v11 and is not moved by this carrier.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "AMGT_CORPUS's ARMED row AMGT_CORPUS-D1-C-S64 (case-block rows rendered under history-year headers) IS touched by /15: one live read of ROG_SW_Equity's model.team_sheet at 05:18:12Z finds the row's own example 660.4543... only at team_sheet.blocks[0].rows[4].cells[2], a separate case block (row_counts BLOCK 10, FIGURE 85), not in the period grid of 2016..2029 where round 99's read on /14 still found it. Measured on one of the 13 names; the 62-row close and its DEV render census are AMGT_CORPUS's (C1's census reads 0 values under a foreign header, per the packet). Noted here; the row stays on AMGT_CORPUS's REMEDIATION_v11 and is not moved by this carrier.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO lambda invoke GET /security/ROG_SW_Equity/thesis 2026-10-12T05:18:12Z (session scratch rog_teamsheet.py)",
        "adjudication row AMGT_RESAPP-D1-C-S97 (round 99: '660.45' still in the /14 grid)",
        "AMGT_CORPUS ADJUDICATION_v63 row AMGT_CORPUS-D1-C-S64"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "AMGT_CORPUS's ARMED row AMGT_CORPUS-D1-C-S64 (case-block rows rendered under history-year headers) IS touched by /15: one live read of ROG_SW_Equity's model.team_sheet at 05:18:12Z finds the row's own example 660.4543... only at team_sheet.blocks[0].rows[4].cells[2], a separate case block (row_counts BLOCK 10, FIGURE 85), not in the period grid of 2016..2029 where round 99's read on /14 still found it. Measured on one of the 13 names; the 62-row close and its DEV render census are AMGT_CORPUS's (C1's census reads 0 values under a foreign header, per the packet). Noted here; the row stays on AMGT_CORPUS's REMEDIATION_v11 and is not moved by this carrier."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S105",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T05:25:00Z",
    "one_line": "D1-W397-S1 (INERT) dismissed: AC3's expected 'thesis noise' line was a clock-dependent count the issuer fixed from one dry run; bg-2 AMENDMENT 1 rewrote it as absent or any count, and this seat's runs show the clock class varying (1 clock path in its whole-body compare).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W397-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W397-S1 (INERT) dismissed: AC3's expected 'thesis noise' line was a clock-dependent count the issuer fixed from one dry run; bg-2 AMENDMENT 1 rewrote it as absent or any count, and this seat's runs show the clock class varying (1 clock path in its whole-body compare).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W397-S1",
        "bg-2 AMENDMENT 1 @e2693c1630"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W397-S1 (INERT) dismissed: AC3's expected 'thesis noise' line was a clock-dependent count the issuer fixed from one dry run; bg-2 AMENDMENT 1 rewrote it as absent or any count, and this seat's runs show the clock class varying (1 clock path in its whole-body compare)."
  }
]
```
