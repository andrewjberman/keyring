# LGIC_NAMING: CVO adjudication

Pre-issuance intake by `3.0.0_SA_CVO`. The rows are from L4 and L5, and no round has been issued (dep_stage DECOMP),
so this is NOT an L8 compile and no judgment criterion is graded here. Each row below was read against the artifact
that closes it before it was dispositioned.

```json
[
  {
    "id": "LGIC_NAMING-C-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T12:05:00Z",
    "one_line": "PRE-ISSUANCE INTAKE: nine rows CLOSED by a ruling or a fix, each read against the artifact that closes it -- the notifier's inbox file (S1, S2), the MDPF_CANON s.3 notice (S4), the stamp's pin (S5), three schema rulings (S6-S8), the stamp's hash-bound status (S9) and legacy membership as data (S10).",
    "class": "OBSERVATION",
    "spec_asserts": "Each row names what would close it: a notifier that writes the inbox file (S1), the s.3 replacement notice (S4), a pin of the recorded bytes (S5), an L10 addendum ruling each schema form (S6, S7, S8, S10), and a status that reads the halves the way LIMB 6 does (S9).",
    "world_is": "S1, S2: today's five [L4-R REVIEW] deliveries to this seat (96552, 96558, 96561, 96564, 96567) arrived as inbox files under their broker Msg-IDs, and none needed a hand relay. S4: docs/architecture/MDPF_CANON_PRD.md @3514843a12 is a notice that reads 's.3's layout is REPLACED'. S5: prd-stamp.py content_pin normalises CRLF to LF before hashing (:83-86, fix b09ed6c736), and status still accepts the pre-S5 raw pin. S6, S7, S8: ruled by 1.0.0_SA_CTO's adjudication @7bd4ef6f27, and landed in NAMING_SCHEMA v1.3 as key.partition's entity form, key.table_case bounded to NEW leaves, key.legacy_served_path and key.code; v1.4 @e04b802fe9 carries them. S9: prd-stamp status, run by path at v1.4, prints both L4-R halves 'SIGNED -- current', read through prd_signoff_lib (fix 6792cc90bc). S10: ruled @e04b802fe9. Membership is data: key.legacy_served_paths names its home, its producer (cell LN-g-1) and its claim ('absent until LN-g-1 lands it'), and grade() RAISES until the list lands.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/3.0.0_SA_CVO/read/ -- five [L4-R REVIEW] files dated 20260914 (untracked carriers, no commit vintage)",
        "docs/architecture/MDPF_CANON_PRD.md@3514843a12",
        ".tools/prd-stamp.py@6792cc90bc :83-92; fixes b09ed6c736 and 6792cc90bc",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_LGIC_NAMING_20260914T103xZ_S6_S7_S8_ENTITY_PARTITION_CODE_TIER_LEGACY_SERVED_PATHS.md@7bd4ef6f27",
        "org/standards/NAMING_SCHEMA.json@e04b802fe9 key.partition, key.table_case, key.legacy_served_path, key.legacy_served_paths, key.code, changelog v1.3 and v1.4"
      ]
    },
    "adjudicates": [
      "LGIC_NAMING-S1",
      "LGIC_NAMING-S2",
      "LGIC_NAMING-S4",
      "LGIC_NAMING-S5",
      "LGIC_NAMING-S6",
      "LGIC_NAMING-S7",
      "LGIC_NAMING-S8",
      "LGIC_NAMING-S9",
      "LGIC_NAMING-S10"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is closed in the artifact it names, as read here. S1's mechanism was remedied by S2 and is exercised in this seat's own inbox. S4's act was taken at MDPF_CANON's L4. S5 and S9 are fixed in prd-stamp. S6, S7, S8 and S10 were ruled by 1.0.0_SA_CTO and landed in NAMING_SCHEMA v1.3 and v1.4. S10's list is owed by cell LN-g-1, and the schema makes grade() refuse rather than guess until it lands. The four ARMED rows (S1, S6, S7, S8) stand INERT from this row.",
    "hazard_standing": "INERT"
  },
  {
    "id": "LGIC_NAMING-C-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T12:05:00Z",
    "one_line": "PRE-ISSUANCE INTAKE, GRADUATED to 1.0.0_SA_CTO: S3 -- the spine's L6 queue rule puts dependent cells in one worker's queue, but an exercise whose validity IS the workers' independence (blind graders, namers who never confer) needs different workers on dependent cells. This seat reads the project's resolution as sound; the spine names no such exception.",
    "class": "OBSERVATION",
    "spec_asserts": "Spine L6: dependent cells ride ONE worker's queue, and the fan-out is derived from the decomposition's dependency chains.",
    "world_is": "LGIC_NAMING_DECOMP.md v1 section 5 keeps the dependency edges but serialises them by spawning a dependent cell's worker only after its input's branch is merged, and supports N up to 8 over M = 5 chains, giving 'blindness' as the reason (row S3). The resolution is sound for this project: one worker carrying N2 into its own grading would void the exercise it grades. But the rule it departs from names no exception, so the next project with blind exercises meets the same conflict, and a reader of the spine alone would call this decomposition non-conformant.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md row LGIC_NAMING-S3",
        "org/missions/D14/LGIC/LGIC_NAMING/decompositions/ (decomposition v1, section 5, per row S3)",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md (L6 queue rule)"
      ]
    },
    "adjudicates": [
      "LGIC_NAMING-S3"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  }
]
```
