# MDPF_SECCLASS -- round 26, L8 compile (dell1)

<sweep_watermark>2026-10-16T04:12:29Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T04:12:29Z. L8 packet: 2.0.0_SA_COO~M1 msg 6475, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R26_20261016.md @2181ff8c3a. The round has no judgment criterion.
Rows swept by id-set difference: 7 dell1 rows never named, all dispositioned here (C-S28 dismisses 6, C-S29 graduates 1). The watermark moves to now.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S28",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T04:12:29Z",
    "one_line": "ROUND 26 L8: six rows dismissed. W95-S1's premise is corrected here: lib.config and lib.platinum_dest ARE tracked, at data/black_diamond/scripts/gold/lib/, and the D_04 writer's bucket reads opal-data-bd from the tree. The other five are measured facts the round's records already carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W93-S1",
      "MDPF_SECCLASS-D1-W93-S3",
      "MDPF_SECCLASS-D1-W94-S1",
      "MDPF_SECCLASS-D1-W95-S1",
      "MDPF_SECCLASS-D1-W95-S2",
      "MDPF_SECCLASS-D1-W96-S1"
    ],
    "spec_asserts": "Spine L8/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; the round has no judgment criterion (round-close-check judgment=0).",
    "world_is": "W95-S1 CORRECTED: the row says D_04's writer modules 'lib.platinum_dest' and 'lib.config' are 'not tracked at HEAD or present in the main checkout'. The writer imports them at data/black_diamond/scripts/gold/D_04.client_portal_summary.py:83-84, and git ls-files lists data/black_diamond/scripts/gold/lib/config.py, platinum_dest.py and platinum_dest_view.py, so they are tracked. The worker looked at the repo-root lib/, which holds neither. lib/config.py:14 reads S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-bd'), and platinum_dest.destination returns (S3_BUCKET, legacy_key) unless a mapping hits (:60-64). So the write's bucket is readable from the tree and agrees with the readers' opal-data-bd. The round's decision (NO-ORDER-DEPENDENT-READER) is unaffected. W93-S1: the stale chain comment that B_02 reads bd-securities is confirmed false by the gold-tree census; a comment fix for the round-27 build. W93-S3: the census cannot see the handle-reached name-prefix read at E_18:156-171, :214, :218; the disposition record names those lines, so it is not silent on them. W94-S1: the nine-key class row holds on 19 of 2,297 dates, and the repointed reader returns either shape. W95-S2: the issuer's own order defect; census-missed readers are recorded in prose with verdict 'no'. W96-S1: the seed path has no class source for HPI, CUBE, GLPI or PCEF; the packet carries a source for the four as owed at round 27.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:83-84",
        "git ls-files data/black_diamond/scripts/gold/lib/ -> config.py, platinum_dest.py, platinum_dest_view.py among 17",
        "data/black_diamond/scripts/gold/lib/config.py:14; lib/platinum_dest.py:60-64",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R26_20261016.md @2181ff8c3a",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is corrected here, recorded in the round's disposition record, or owed by name at round 27; none leaves a live hazard."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S29",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T04:12:29Z",
    "one_line": "Graduated to REMEDIATION_v16: W93-S2 (ARMED). E_18's canonical write still takes its asset_class from the old list; the measurement of how many bd-only tickers a nightly run writes that way is owed at round 27. Also recorded by this row: REMEDIATION_v15's W92-S4 is MET (the E_25 test passes 4 of 4 on this seat's run).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~M1",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W93-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "W93-S2: E_18 writes the canonical row for a bd-only ticker with a class from the old list. Repointing returns None for every candidate, so the old-list input can only be removed, and such tickers then go unresolved. The packet's 'Not shown' names the count as unmeasured, and the round-27 recut owes 'the measurement that disarms D1-W93-S2'. W92-S4: THIS SEAT RAN python -m pytest data/black_diamond/scripts/gold/tests/test_e25_firm_key_r26.py -> 4 passed; E_25.aua_decomposition_audit.py:142 now reads summary.get('firm', {}).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_SECCLASS-D1-W93-S2",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R26_20261016.md @2181ff8c3a",
        "python -m pytest data/black_diamond/scripts/gold/tests/test_e25_firm_key_r26.py -> 4 passed (3.0.0_SA_CVO, 2026-10-16T04:1xZ)",
        "data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py:142"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v16."
  }
]
```

-- 3.0.0_SA_CVO
