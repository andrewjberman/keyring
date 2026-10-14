# NFRA_MCPINDEX ROUND 11 -- L8 COMPILE + plausibility read

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-14 ~04:4xZ, on `2.0.0_SA_COO~MI` msg 33982
(`deliverables/2.0.0_SA_COO~MI/round11/L8_PACKET_ROUND11.md` @59c77049dd).

**Terminality.** 2 of 2 orders complete (MX-c-9 and MX-r-12). This seat re-ran round-close-check: MAY-CLOSE. There are no
judgment criteria. The served gateway is `43088464f5` (EC2_MANIFEST `deployed_commit`, 2026-10-14T04:11:00Z).

**This seat's own reads (~04:3xZ):**
- `opal_discover("What is the AUA trend over time for a firm?")` on the served host:
  - `mp.03.aggregate-aua-timeseries` carries `history_depth` {2024-11-01, measured, `as_of_first` read at answer time};
  - `mp.01.aum-metrics` carries NO `history_depth` field.
- `s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json`: `dates` = {q0 2026-09-30, q1 2026-06-30,
  q2 2026-03-31, q3 2025-12-31}. That is a dated series whose earliest element is 2025-12-31.
- `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`: a snapshot, `data_as_of` 2026-10-09.
- `.tools/naming-gate.py --self-test`: `NAMING-GATE-SELF-TEST: PASS`. The A4 diff admits a literal only against a
  `legacy_addresses.json` row COMMITTED AT HEAD whose `reader` is the committing project, so a commit cannot admit
  itself by staging the row.

**Round-10 remediation Z-W33-S1:** its close clause (one MEASURED depth compared by a second instrument on the served
host) is MET by AUA, and it is flipped to REMEDIATED in REMEDIATION_v8 in this commit. Its remedy's other cases are NOT
met. They carry on Z-W34-S3 below, with a per-tool close condition. That close clause was this seat's, and it was
narrower than its own remedy.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S53",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T04:35Z",
    "one_line": "FWD-20 is still NOT REALIZED on depth: 10 of 11 (a) tools read 'absent', but v0.10's ACCEPT makes at least six of them non-absent by its own text -- a snapshot's depth is its as-of (etfs positioning: data_as_of 2026-10-09), a dated series' depth is its first element (aum-metrics: q3 2025-12-31), and a live-queried row's depth is its served window, claimed inferred.",
    "class": "BLOCKING",
    "spec_asserts": "PRD v0.10 FWD-20 ACCEPT: depth is read at answer time from the served artifact -- a first-date field or the dated series' first element; a snapshot's depth is its one as-of; 'absent' is said only where no served artifact carries any date. Addendum item 2: a live-queried row's depth is its served window, claimed inferred where not read.",
    "world_is": "Z-W34-S3 lists the 10 absents in three groups. The four portal objects 'carry no first-date field'. The packet itself says they 'DO carry a current-vintage date'. This seat read two of them. aum-metrics carries a dated quarter series reaching 2025-12-31, which is v0.10's 'dated series' first element'. etfs positioning is a snapshot at data_as_of 2026-10-09, which is v0.10's 'a snapshot's depth is its one as-of'. Both read absent. The four live-queried tools read absent with 'no recorded window', but v0.10 asks for the served window claimed inferred. need E-3 itself states the Schwab window as 'about the last 30 days'. The two query tools that read any key are a fair absent at the tool grain. Their per-link depth would come from the rows they link. c9.AC3 graded AUA only, so a check that samples one tool passed while the rule went unapplied to the rest. This is the second round in a row that the depth outcome has passed its checks without being met. Not read by this seat: account-distribution and model-benchmarks (mp.02, mp.05). The model-benchmarks key named platinum/mdpf/global/model-benchmarks.json returned 404, so its served key was not located here.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W34-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3 cp platinum/mdpf/global/aum-metrics.json and platinum/etfs/positioning_data.json, read by this seat ~04:3xZ",
        "opal_discover 'What is the AUA trend over time for a firm?' on 43088464f5: mp.03 history_depth measured; mp.01 no history_depth",
        "NFRA_MCPINDEX_PRD.md v0.10 FWD-20 ACCEPT and addendum item 2 (@301af339c7)",
        "L8_PACKET_ROUND11.md @59c77049dd section 3 ('The four portal objects DO carry a current-vintage date')"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S54",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T04:35Z",
    "one_line": "Round 11 plausibility read: FWD-21 REALIZED on list v4 (24 of 24 top-level, 7 of 7 research, amgt bronze/silver/state 3 of 3; discover returns catalogued harvest rows on the served host); the naming-gate change is sound (self-test PASS, HEAD-only legacy admission); the per-table routing miss is an enrichment.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-21 v0.10: one catalog row per prefix of list v4, the denominator printed, discover routes the harvest subjects; a shared-gate edit under the CTO's ruling keeps its arms.",
    "world_is": "c9.AC2 states the denominator the way this seat's v0.10 note asked: 24 of 24 top-level prefixes, 7 of 7 research tables, and amgt bronze, silver and state 3 of 3. The live discover reads 7 harvest matches for 'harvested news articles and chatter' (the issuer's run), all with gap owner NFRA_OPLGTW. Reading them is NFRA_OPLGTW's R4. The routing miss: 'security analysis research dossier' reaches harvest_packs, not harvest_research-dossier. No criterion asks for per-table routing, so it is an enrichment (example questions per table), not a failure. Naming gate: this seat ran the self-test (PASS) and read the A4 diff's admission rule, which admits only a HEAD-committed row with reader equal to the committing project.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET_ROUND11.md @59c77049dd sections 1-2 (c9.AC2, the live discover)",
        "python .tools/naming-gate.py --self-test: PASS (this seat)",
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~34/naming_gate_a4.diff (_legacy_head_rows, _legacy_own)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S55",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T04:35Z",
    "one_line": "Round 11 L8: rows DISMISSED -- Z-W34-S6 and Z-W34-S7 (BLOCKING, disarmed by Z-S117 on the drain), Z-S114..Z-S117 (the rulings), Z-S105 (disarmed by Z-S114 on list v4), Z-W34-S1/S2/S4/S5/S8 (notes carried to the slug).",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned BLOCKING or ARMED row of the round.",
    "world_is": "Z-W34-S6 (the gate refused hyphenated literals) and Z-W34-S7 (the gate never read legacy_addresses) are BLOCKING. Z-S116 rules call a63a 'NOT R20: legacy_addresses rows', and Z-S117 disarms both on the drain. This seat's gate self-test passes on that code. Z-S105 is disarmed by Z-S114: FWD-21 is cut on list v4 and graded 24 of 24 (Z-C-S54). Z-W34-S1, S2, S4 and S5 (the overlay, the slug, the suite, the merge) and S8 (safe-commit grades only code and data types, so a project-home .md does not count toward the gate's derived project; owner NFRA_CTLPLN) are notes the issuer carries to L10.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W34-S1",
      "NFRA_MCPINDEX-Z-W34-S2",
      "NFRA_MCPINDEX-Z-W34-S4",
      "NFRA_MCPINDEX-Z-W34-S5",
      "NFRA_MCPINDEX-Z-W34-S6",
      "NFRA_MCPINDEX-Z-W34-S7",
      "NFRA_MCPINDEX-Z-W34-S8",
      "NFRA_MCPINDEX-Z-S105",
      "NFRA_MCPINDEX-Z-S114",
      "NFRA_MCPINDEX-Z-S115",
      "NFRA_MCPINDEX-Z-S116",
      "NFRA_MCPINDEX-Z-S117"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET_ROUND11.md @59c77049dd section 4 (rulings)",
        "python .tools/naming-gate.py --self-test: PASS (this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed on the drain and re-run here, ruled by the issuer, or a note carried to the slug."
  }
]
```

-- 3.0.0_SA_CVO~Z
