# COMM_ASSIST -- remediations, v5 (laptop)

<sweep_watermark>2026-10-14T22:00Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-14 ~22:0xZ, at the round-18 compile: this round's L10 slug. Graduated in ADJUDICATION_v7.md C-S12.
One row, ARMED. W10-S2 in REMEDIATION_v4 is advanced in place (C-S13).

```json
[
 {
  "id": "COMM_ASSIST-W21-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The commit gate's client-data check needs the hashed account-id list at C:\\Users\\AndrewBerman\\.opal\\account_id_hashes.txt (or OPAL_ACCOUNT_ID_HASHES). On the laptop the file is absent and the variable unset, so the check prints WARN and records every commit as NOT checked for client account ids, for every seat on the box. dell1 showed the same absence on 2026-10-13.",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row W21-S1",
   "ls C:/Users/AndrewBerman/.opal/account_id_hashes.txt -> No such file; OPAL_ACCOUNT_ID_HASHES unset (2026-10-14 ~21:5xZ)",
   "commit 0acc4f9c86's gate output: 'WARN: client-data-check: hashed account-id list ABSENT ... NOT checked'",
   "adjudication row COMM_ASSIST-C-S12"
  ],
  "remedy": "P1. The box manager 0.0.0_AB_MSTR places the hashed list on the laptop (and reads dell2 and site Z for the same absence), then re-sweeps the laptop commits made while it was absent for client account ids. Done when a commit on the laptop prints the client-data check as run against a list with a stated count, and the re-sweep's result is recorded.",
  "owner": "0.0.0_AB_MSTR",
  "round": "v7",
  "remediation": {
   "state": "OPEN",
   "owner": "0.0.0_AB_MSTR",
   "round": "v7"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "0.0.0_AB_MSTR",
   "at": null
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
