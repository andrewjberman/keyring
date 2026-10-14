# NFRA_MCPINDEX ROUND 10 -- L8 COMPILE + plausibility read

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-14 ~00:3xZ, on `2.0.0_SA_COO~MI` msg 33839
(`deliverables/2.0.0_SA_COO~MI/round10/L8_PACKET_ROUND10.md` @037d137715).

**Terminality.** 2 of 2 orders are complete: MX-c-8 and MX-r-11. This seat re-ran round-close-check and it reads
MAY-CLOSE. The round has no judgment criterion. The served gateway is `7eff14b2e6`
(EC2_MANIFEST `deployed_commit`, deployed 2026-10-13T23:49:56Z).

**This seat's own reads (a second instrument, through this session's opalgateway connection on the served host,
~00:2xZ 2026-10-14):**
- `opal_discover("harvested news articles and chatter")`: catalogued, 5 matches, all on `harvest_datasets`, each
  `servable: false` with gap owner NFRA_OPLGTW.
- `opal_discover("security analysis research pack")`: catalogued, 1 match (`harvest_packs`), with the same gap.
- `opal_discover("Schwab account positions")`: catalogued, 8 matches, 3 servable. The control is unchanged.
- `s3://opal-data-portal-v2/platinum/mdpf/global/aggregate-aua-timeseries.json`, read whole:
  - `as_of_first = 2024-11-01`, `as_of_last = 2026-10-12`;
  - `cohort_provenance` holds 495 dated entries, first 2024-11-01, last 2026-10-12.
- Tool definitions for `graph_status` (`integrations/globgrph/integration.py:160`) and `ycharts_freshness`
  (`integrations/ycharts/integration.py:125`): both return health or session status and read no dataset.

**Out of round, not dispositioned here:** Z-S101 (BLOCKING, ARMED) and Z-S102 (OBSERVATION, ARMED). Both are MX-s-19's,
surfaced by `0.7.0_AE_CloudOps~MI` at 04:45Z on 10-13, and their disarm owner is `2.0.0_SA_COO~MI`. They belong to
MX-s-19's read on 2026-10-19/20, not to this round. Z-S102 is a served-silver hazard: a BD transactions partition was
re-written at 1.3% of its bytes. It stays ARMED with its owner.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S48",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T00:15Z",
    "one_line": "Round 10 plausibility read: FWD-21 REALIZED (three discover reads re-run live by this seat); FWD-20's partition REALIZED (67 of 67, a=11 b=44 c=12, classified from definitions on this seat's sample).",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-21 DONE WHEN: opal_discover for the two harvest subjects returns catalogued datasets, not catalogued: false, and the Schwab control still returns its datasets. FWD-20 DONE WHEN: N served tools partitioned into (a)/(b)/(c) summing to N.",
    "world_is": "FWD-21: this seat's three discover calls on the served host read catalogued 5, catalogued 1 and catalogued 8 (3 servable), and before the round both subjects read catalogued: false (issuer's base read). That is REALIZED as DONE WHEN states it: the route. The read itself is direction Z5, NFRA_OPLGTW's. FWD-20 partition: the issuer's live r11.AC2 reads N=67, a=11, b=44, c=12, with 67 of 67 definitions located in the deployed tree. members.yaml says the classification is by definition, and this seat's sample agrees. The 12 (c) reasons each name a send, write, upload, ticket or probe. graph_status and ycharts_freshness, the two Z-W33-S2 calls that a name alone would misplace, are status probes by their definitions, so they are (c). whoami, opal_discover and opal_describe as (b) is defensible: they read data that no catalog row describes. The partition is REALIZED. FWD-20 as a whole is not; see Z-C-S49.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "mcp opalgateway opal_discover x3, this seat, ~00:2xZ 2026-10-14, served host 7eff14b2e6",
        "workflows/atom_decomposition/tool_index/members.yaml: the 12 member: c entries and their reasons",
        "infra/aws/ec2/opal-gateway/app/integrations/globgrph/integration.py:160; app/integrations/ycharts/integration.py:125",
        "deliverables/2.0.0_SA_COO~MI/round10/L8_PACKET_ROUND10.md @037d137715 (r11.AC2)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S49",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T00:15Z",
    "one_line": "FWD-20 is NOT REALIZED on depth: history_depth reads 'absent' on 11 of 11 (a) tools, but at least one served artifact carries its earliest date as a body field (aggregate-aua-timeseries.json as_of_first = 2024-11-01), so 'absent' is a wrong claim, produced by the order's bound 4 forbidding body reads.",
    "class": "BLOCKING",
    "spec_asserts": "FWD-20 DONE WHEN: each (a) tool carries its index's history depth (earliest served date); ACCEPT: depth carries a claim (measured / inferred / absent), and freshness is read at answer time (FWD-13's rule).",
    "world_is": "members.yaml gives mdpf_get_aggregate_aua (row mp.03.aggregate-aua-timeseries) history_depth claim absent, with the reason 'how far back its data goes is inside the body, and a key listing reads no content'. This seat read that served object: it carries as_of_first = 2024-11-01 at top level, beside as_of_last, the field the catalog already reads from the same object for freshness at answer time. The value exists in the served artifact, so 'absent' asserts a non-existence that is false. The correct claim is measured, by the same body read freshness uses. Z-W33-S1 names the cause: the order's bound 4 forbade reading the body. Its conclusion, that depth 'needs the producer to publish it', is wrong for this object, which already publishes it. The PROOF's second-instrument depth comparison (r11.AC3, 'depth absent CONFIRMED' on etfs_get_positioning) compared absent to absent and could not catch this. Not read by this seat: the other four portal-object tools (mp.01, mp.02, mp.05, etfs.01). A snapshot object's depth is its one as-of date, a measured value, not absent. The Schwab and Black Diamond live-queried rows serve a bounded window (need E-3: about 30 days), and that window is at least INFERRED. So 'absent' on all 11 is a property of the instrument, not of the data.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W33-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3 cp s3://opal-data-portal-v2/platinum/mdpf/global/aggregate-aua-timeseries.json, read whole by this seat: as_of_first 2024-11-01, as_of_last 2026-10-12",
        "opal_describe mp.03.aggregate-aua-timeseries: freshness field as_of_last, claim measured, read from the served object at answer time",
        "workflows/atom_decomposition/tool_index/members.yaml mdpf_get_aggregate_aua history_depth (claim absent, reason quoted)",
        "investigation row Z-W33-S1 (bound 4 forbids reading the body)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S50",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T00:15Z",
    "one_line": "Round 10 L8: 11 rows DISMISSED -- Z-W33-S2 (sound on sample), Z-W33-S3/S4 (ARMED, ruled INERT by Z-S106/S107), Z-W33-S5/S6 (notes), Z-S105 (drained as cut; the widening is round 11 by CTO ruling), Z-S108/S109/S111 (deploy recipe, folded into OPEN Z-S92), Z-S110 (BLOCKING, disarmed on v2 by Z-S113), Z-S112 (the ruling).",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned BLOCKING or ARMED row of the round.",
    "world_is": "Z-W33-S2: the classification calls hold on this seat's sample (Z-C-S48). Z-W33-S3: the entity collision is ruled INERT by Z-S106, since no app reader keys entity over the whole file. A durable link key is carried. Z-W33-S4: the stale suite baseline is ruled INERT by Z-S107 and read beside the verdict under clause 2. A re-baseline is carried. Z-W33-S5 (the naming gate refuses typed platinum prefixes, which is the gate doing its job) and Z-W33-S6 (plane 2 stale at PHASE A) are notes. Z-S105: Andrew's call 8 post-dates the issuance at 0fa3174d89. The round is frozen and drained on list v3, and CTO msg 33748 places v0.10 and the 13 added prefixes at round 11. Z-S108, Z-S111 and Z-S109: the gateway deploy cone lacked infra/logic/registry, a recurrence on all three MCPINDEX releases. This is the class of Z-S92, still OPEN with owner 2.0.0_SA_COO~O, so it folds there rather than into a new row. Z-S110 (BLOCKING): definitions read 65 of 67 on v1. Z-S112 rules fix-forward, and Z-S113 disarms it on v2 at 67 of 67. The manifest's deployed_commit reads 7eff14b2e6, and this seat's discover calls ran against it.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W33-S2",
      "NFRA_MCPINDEX-Z-W33-S3",
      "NFRA_MCPINDEX-Z-W33-S4",
      "NFRA_MCPINDEX-Z-W33-S5",
      "NFRA_MCPINDEX-Z-W33-S6",
      "NFRA_MCPINDEX-Z-S105",
      "NFRA_MCPINDEX-Z-S108",
      "NFRA_MCPINDEX-Z-S109",
      "NFRA_MCPINDEX-Z-S110",
      "NFRA_MCPINDEX-Z-S111",
      "NFRA_MCPINDEX-Z-S112"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows Z-W33-S2..S6, Z-S105, Z-S108..Z-S113",
        "infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway.deployed_commit 7eff14b2e6 (2026-10-13T23:49:56Z)",
        "1.0.0_SA_CTO~Z msg 33748 (v0.10 at the round-10 analysis; round 11 cuts the added prefixes)",
        "REMEDIATION_v6.md row Z-S92 (OPEN)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled by the issuer and sound, folded into an OPEN row of the same class, or placed by a CTO ruling."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S51",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T00:20Z",
    "one_line": "Z-S82 (BLOCKING, from round 6, never dispositioned) is DISMISSED: the act it guarded, MX-s-17's repoint of the transaction document to the code/silver script, is cancelled, and MX-s-19 retires that document's merge step instead, so the boto3-less instance never runs the script.",
    "class": "OBSERVATION",
    "spec_asserts": "The slug dispositions every BLOCKING or ARMED investigation item under the project.",
    "world_is": "Z-S82 (0.7.0_AE_CloudOps~MI, 2026-10-06) measured that i-00c7568bc510f7423 has no boto3. A repoint would therefore have turned the transaction merge into a silent exit-0 no-op, so MX-s-17 published nothing. The hazard was conditional on that repoint. MX-s-17's last status tag reads cancelled. MX-s-19 (pending, the CTO's ruling) retires both documents' merge step under never-widen halves, leaving bd-silver-merge as the one writer. The boto3-less instance is never pointed at code/silver, so the row's failure mode has no path. Not re-measured by this seat: whether the instance still lacks boto3, which no planned act needs. MX-s-19's own rows (Z-S101, Z-S102, ARMED) carry what bears on that retirement.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S82"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row Z-S82, read whole",
        "task-orders/NFRA_MCPINDEX.TO-MX-s-17.bd-doc-repoint-code-silver.md: last status cancelled",
        "task-orders/NFRA_MCPINDEX.TO-MX-s-19.bd-doc-merge-retire.md:1, :21 (retire, not repoint)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The guarded act is cancelled and superseded by a retirement; the failure mode has no path."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S52",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T00:20Z",
    "one_line": "Correction of this seat's round-9 Z-C-S47: its text DISMISSES Z-S96 (the fix landed and was re-run), but the row lists Z-S96 under a GRADUATED disposition together with Z-S97, so the machine reads Z-S96 as graduated with no remediation row. Z-S96 is DISMISSED here.",
    "class": "OBSERVATION",
    "spec_asserts": "One adjudication row carries one disposition for every item it names.",
    "world_is": "ADJUDICATION_v8.md Z-C-S47 one_line: 'Z-S96 DISMISSED (its fix landed and was re-run); Z-S97 GRADUATES'. Its adjudicates list is [Z-S96, Z-S97] with disposition GRADUATED. REMEDIATION_v7 carries Z-S97 only. The surprise-row gate reads Z-S96 as GRADUATED with no remediation row (refusal on this slug, 2026-10-14 ~00:2xZ). Z-S96 ruled the remedy for the bd-served-vintage-alarm.tf plan (can() guard). Z-C-S47's text records that the fix landed and was re-run in round 9. Defect class (this seat's): two dispositions under one row; split them.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S96"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudications/ADJUDICATION_v8.md row Z-C-S47 (one_line and adjudicates)",
        "remediations/REMEDIATION_v7.md (Z-S97 only)",
        "investigation row Z-S96"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Its fix landed and was re-run in round 9 (Z-C-S47's own text); this row splits the disposition it shared with Z-S97."
  }
]
```

-- 3.0.0_SA_CVO~Z
