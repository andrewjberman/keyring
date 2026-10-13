# MDPF_DEMQUE W35-S3 disarm -- HELD (3.0.0_SA_CVO, dell1, 2026-10-13 ~14:5xZ)

HELD by 3.0.0_SA_CVO: surprise-row-gate refuses a new remediation row while 6 MDPF_DEMQUE investigation items are undispositioned (D1-S12, D1-W24-S1, D1-W27-S2, D1-W28-S1, D1-W29-S1, Z-S5). OWNER: 3.0.0_SA_CVO. UN-PARKS ON: the next MDPF_DEMQUE L8 compile that dispositions those items; THEN land the two blocks below as ADJUDICATION_v{next} and REMEDIATION_v{next} (ids and file numbers re-checked at that time).

The disarm itself is measured (own read, msg 4896): the hash list holds 29617 hashes; client-data-check.py flags a planted synthetic id and passes a control line; no ABSENT warning. Same hazard recorded DISARMED in AMGT_RESAPP REMEDIATION_v36 W381-S1.

## Adjudication block (was ADJUDICATION_v9)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S27",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:55:00Z",
    "one_line": "W35-S3 (ARMED, disarm owner 0.0.0_AB_MSTR) graduated to REMEDIATION_v8 with its disarm clock DISARMED: the hashed client account-id list is restored on dell1 and client-data-check.py reads it and discriminates (own read: 29617 hashes; a planted synthetic id hits, a control line does not; no ABSENT warning). Work is owed: Not covered: commits made on dell1 while the list was absent (from at least 2026-10-11 to 2026-10-13T14:4xZ, including 748b73b3ca) were never checked for client account ids; a re-sweep of those commits against the list is owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W35-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "W35-S3 (ARMED, disarm owner 0.0.0_AB_MSTR) graduated to REMEDIATION_v8 with its disarm clock DISARMED: the hashed client account-id list is restored on dell1 and client-data-check.py reads it and discriminates (own read: 29617 hashes; a planted synthetic id hits, a control line does not; no ABSENT warning). Work is owed: Not covered: commits made on dell1 while the list was absent (from at least 2026-10-11 to 2026-10-13T14:4xZ, including 748b73b3ca) were never checked for client account ids; a re-sweep of those commits against the list is owed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~DELL1 msg 4896: ran 2.0.0_SA_COO~P2's account_id_hash_builder.py on dell1, rc 0, wrote C:/Users/Test/.opal/account_id_hashes.txt",
        "3.0.0_SA_CVO read the list 2026-10-13T14:5xZ: 29617 lines, all 64-hex, 29617 unique (1,954,722 B)",
        "3.0.0_SA_CVO loaded .tools/git-hooks/client-data-check.py: _load_hashes reads 29617 hashes; hits_in flags a planted synthetic id (sha256 of ZZTEST9876543 in a test list) at line 2 x1 and returns [] for a control line; the synthetic id is not in the real list; main() with an empty staged set returns 0 and prints no ABSENT warning"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v8.md."
  }
]
```

## Remediation block (was REMEDIATION_v8)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W35-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On dell1 the hashed client account-id list was absent, so .tools/git-hooks/client-data-check.py WARNed and passed: no dell1 commit was checked for client account ids. The list was restored 2026-10-13T14:4xZ (29617 hashes); the gate now reads it.",
    "evidence": [
      "0.0.0_AB_MSTR~DELL1 msg 4896: ran 2.0.0_SA_COO~P2's account_id_hash_builder.py on dell1, rc 0, wrote C:/Users/Test/.opal/account_id_hashes.txt",
      "3.0.0_SA_CVO read the list 2026-10-13T14:5xZ: 29617 lines, all 64-hex, 29617 unique (1,954,722 B)",
      "3.0.0_SA_CVO loaded .tools/git-hooks/client-data-check.py: _load_hashes reads 29617 hashes; hits_in flags a planted synthetic id (sha256 of ZZTEST9876543 in a test list) at line 2 x1 and returns [] for a control line; the synthetic id is not in the real list; main() with an empty staged set returns 0 and prints no ABSENT warning",
      "investigation row MDPF_DEMQUE-D1-W35-S3 @b956c6307e",
      "adjudication row MDPF_DEMQUE-D1-C-S27"
    ],
    "remedy": "Re-sweep every commit made on dell1 while the list was absent (including 748b73b3ca) against the list. Close when: the sweep reports, per commit, 0 hits or each hit redacted under its own pair, with the commit denominator printed.",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-13T14:55:00Z"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
