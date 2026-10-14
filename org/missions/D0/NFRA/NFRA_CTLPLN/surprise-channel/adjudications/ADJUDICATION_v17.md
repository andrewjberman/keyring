# NFRA_CTLPLN: CVO dispositions on ARMED rows, pass 2 (2026-10-14)

<sweep_watermark>2026-10-14T03:30Z</sweep_watermark>

By `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109059. State advances made in place on rows in
`remediations/REMEDIATION_v1.md` (W6-S17, W14-S2) and `REMEDIATION_v4.md` (W73-S2); the evidence is this row's.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S47",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T03:30Z",
  "one_line": "Pass 2 of the issuer's ARMED rows (23 read): W6-S17, W73-S2 and W14-S2 REMEDIATED and DISARMED, each on its own done-when run here; W12-S1, W8-S7, Z-S3, S9103 stay OPEN with no landed remedy; S1 was already closed (laptop only); the other 15 already carry this seat's dismissals.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A graduated ARMED row is REMEDIATED and DISARMED only when its remedy's own done-when is shown.",
  "world_is": "W6-S17: org/devices/intake/test_intake_check.py reads INTAKE-CHECK-TEST cases=57/57 ok=True, including case_check_6_extra_module_in_wheel_fails (a wheel adding a module the installed RECORD never listed fails check 6). W73-S2: .tools/thread-trace.py --selftest reads 12/12, including 'order committed only on origin/CLOUD (HEAD lacks it) is found'. W14-S2: its done-when is a recorded ruling plus a simulation reading the ruled answer for both Dells; Andrew's rec (b) (ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md) put both Dell users in AdministratorAccessOpalCapital, and simulate-principal-policy reads ssm:CreateDocument, UpdateDocument and UpdateDocumentDefaultVersion allowed for cloudops-dell1-agent-user and cloudops-dell2-agent-user. The row's Deny remedy was not applied; the ruling chose the other branch, and Dell document writes are now by design.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/ARMED_ROWS_PASS2_20261014.md @06d4e964a3",
    "timeout 120 python org/devices/intake/test_intake_check.py -> cases=57/57 ok=True (2026-10-14 ~03:2xZ)",
    "timeout 120 python .tools/thread-trace.py --selftest -> cases=12/12 ok=True",
    "aws iam simulate-principal-policy, both Dell users, three ssm document actions: allowed (2026-10-14 ~03:2xZ)",
    "org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of state advances on graduated rows, each on its own done-when; no new defect."
 }
]
```

-- 3.0.0_SA_CVO~L
