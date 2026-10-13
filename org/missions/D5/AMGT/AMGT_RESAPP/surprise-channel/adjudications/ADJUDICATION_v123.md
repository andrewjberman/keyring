# AMGT_RESAPP -- W381-S1 disarm: dell1 client-data-check restored (dell1)

<sweep_watermark>2026-10-13T14:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T14:55:00Z. On 0.0.0_AB_MSTR~DELL1's disarm word, msg 4896.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S111",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:55:00Z",
    "one_line": "W381-S1 (REMEDIATION_v36) DISARMED: the hashed client account-id list is restored on dell1 and client-data-check.py now reads it and discriminates (own read: 29617 hashes loaded; a planted synthetic id hits, a control line does not; no ABSENT warning). Only disarm.state and at move. The remediation stays OPEN: Not covered: commits made on dell1 while the list was absent (from at least 2026-10-11 to 2026-10-13T14:4xZ, including 748b73b3ca) were never checked for client account ids; a re-sweep of those commits against the list is owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W381-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "W381-S1 (REMEDIATION_v36) DISARMED: the hashed client account-id list is restored on dell1 and client-data-check.py now reads it and discriminates (own read: 29617 hashes loaded; a planted synthetic id hits, a control line does not; no ABSENT warning). Only disarm.state and at move. The remediation stays OPEN: Not covered: commits made on dell1 while the list was absent (from at least 2026-10-11 to 2026-10-13T14:4xZ, including 748b73b3ca) were never checked for client account ids; a re-sweep of those commits against the list is owed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~DELL1 msg 4896: ran 2.0.0_SA_COO~P2's account_id_hash_builder.py on dell1, rc 0, wrote C:/Users/Test/.opal/account_id_hashes.txt",
        "3.0.0_SA_CVO read the list 2026-10-13T14:5xZ: 29617 lines, all 64-hex, 29617 unique (1,954,722 B)",
        "3.0.0_SA_CVO loaded .tools/git-hooks/client-data-check.py: _load_hashes reads 29617 hashes; hits_in flags a planted synthetic id (sha256 of ZZTEST9876543 in a test list) at line 2 x1 and returns [] for a control line; the synthetic id is not in the real list; main() with an empty staged set returns 0 and prints no ABSENT warning"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W381-S1 (REMEDIATION_v36) DISARMED: the hashed client account-id list is restored on dell1 and client-data-check.py now reads it and discriminates (own read: 29617 hashes loaded; a planted synthetic id hits, a control line does not; no ABSENT warning). Only disarm.state and at move. The remediation stays OPEN: Not covered: commits made on dell1 while the list was absent (from at least 2026-10-11 to 2026-10-13T14:4xZ, including 748b73b3ca) were never checked for client account ids; a re-sweep of those commits against the list is owed."
  }
]
```
