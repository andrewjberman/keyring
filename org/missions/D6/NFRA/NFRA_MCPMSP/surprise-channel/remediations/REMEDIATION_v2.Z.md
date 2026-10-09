# NFRA_MCPMSP -- surprise channel, REMEDIATION v2 (site Z) -- THE ROUND-2 SLUG

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z` for `3.0.0_SA_CVO~O`, 2026-10-09 ~08:0xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 2 is terminal: 14 orders, 11 complete with proof_ok=11, and 3 cancelled on G-MSPID (MS-sv-1, MS-rn-1, MS-rx-1;
Andrew 2026-10-01 "doesnt matter right now"). The one judgment criterion, MS-dn-1 AC5, is graded PASS at
`ADJUDICATION_v2.Z.md` C-S5. The channel's 13 OPEN rows are dispositioned at C-S3 (10 dismissed) and C-S4 (3
graduated, below). ARMED is 0.

**For the CTO's round-2 analysis:** the three cancelled cells' FWDs stay ungraded until G-MSPID (an MSP calling
identity; holder Andrew) is answered. The remaining distance is that one Andrew-held identity, plus the three OPEN
remediations below, none of which holds the project.

```json
[
  {
    "id": "NFRA_MCPMSP-Z-W7-S1",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-apply's tag-authz and tombstone gates re-plan the live tree with none of the caller's args, so for a targeted or planfile apply they grade a plan the apply does not run.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W7-S1 (MS-s-1 fixed only the naming stage)",
      "Same family as round 1's Z-W2-S3 (safe-apply's full-tree naming limb), REMEDIATION_v1.Z.md"
    ],
    "remedy": "Make the tag-authz and tombstone stages grade the apply's own plan (the saved plan, or the same -target set), as MS-s-1 did for the naming stage.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {"state": "REMEDIATED", "owner": "1.0.0_SA_CTO~Z", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_MCPMSP-Z-W4-S3",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The asker_sender_refusal audit entry carries no sender args; admin_refusals fills sender_email and sender_domain from the record's user field.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S3: correct if user is the Teams sender, wrong if it is the gateway caller identity; not measured."
    ],
    "remedy": "One read of a real refusal record: confirm user is the sender, or carry sender_email/sender_domain in the audit args (audit.py allowlist).",
    "owner": "2.0.0_SA_COO~MS",
    "round": "v2",
    "remediation": {"state": "CLOSED_UNREMEDIATED", "owner": "2.0.0_SA_COO~MS", "round": "v2", "closure": {"reason": "NOT_A_DEFECT", "pointer": "org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round3/checks/rr1.AC1.sh"}},
    "closed": true
  },
  {
    "id": "NFRA_MCPMSP-Z-S4",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round-close-check.py takes an order's id from <to_id> or the full file stem, while proof-of-spec-check.py matches slug-tolerantly, so an order without <to_id> reads PROOF-BAD at round close against a VALID proof.",
    "evidence": [
      ".tools/round-close-check.py:159, read 2026-10-09; landed 10afe6b697 (TO-CT-s-8, issuer 2.0.0_SA_COO~C).",
      "Sibling NFRA_REPORT-Z-S26, REMEDIATION_v4.Z.md (NFRA_REPORT), same owner.",
      "This project's 14 round-2 orders now carry <to_id> (a92355352f); round close then reads proof_ok=11."
    ],
    "remedy": "Make the fallback match the proof's heading id, then census legacy orders without <to_id> estate-wide.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v2",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~C", "round": "v2"},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z

## Round-3 advance (in place, 3.0.0_SA_CVO~Z, 2026-10-09 ~09:2xZ)

Round 3 (`deliverables/2.0.0_SA_COO~MS/round3/DRAIN_END_round3.md` @92d1601e2b) answered two of the three rows above.
Each was re-run at this seat before its clock moved:
- **Z-W7-S1 -> REMEDIATED.** MS-s-2 merged at 4ddac69190. `round3/checks/s2.AC1.sh` passes 6 of 6 arms on the working
  safe-apply against 3 of 6 on base 95d53e2068, and `.tools/tests/test_safe_apply_targeted.sh` reads RESULT: PASS.
  The tag-authz and tombstone stages now grade the scoped apply's own plan. A scoped plan that cannot render fails
  closed at tag-authz.
- **Z-W4-S3 -> CLOSED_UNREMEDIATED, NOT_A_DEFECT.** `round3/checks/rr1.AC1.sh` on deployed aa75078e1b reads
  `user=caller@opalinvest.com sender_email=pat@gmail.com listed_sender_email=pat@gmail.com`. The listing takes the
  sender from `args`, not from `user`, so the feared mix-up does not occur. The real-record read (0
  `asker_sender_refusal` records on the host today) rides MS-sv-1's re-cut, which is a check, not an owed remedy.
- **Z-S4** stays OPEN with `2.0.0_SA_COO~C`.
