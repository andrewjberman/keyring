# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v4 (site Z) -- THE ROUND-4 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-09 ~08:2xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 4 is terminal: 3 of 3 orders complete with VALID proofs, drained at bcb0d718fc (u-1, FWD-1), aebcf9cb69 (u-3,
FWD-3) and 6037269ded (u-2, FWD-8). The three AC4 judgment criteria are graded PASS at `ADJUDICATION_v1.md` C-S19,
C-S20 and C-S21. The 9 OPEN rows are dispositioned at C-S17 (7 dismissed) and C-S18 (2 graduated, below).

**For the CTO's round-4 analysis.** FWD-1, FWD-3 and FWD-8 have their EXERCISED bars met and graded. FWD-4 stays
blocked on the seating ask for the twelve unowned roles (completion report), not on work. Four rows across three
projects now name the same instrument, round-close-check.py: NFRA_REPORT-Z-S26, NFRA_MCPMSP-Z-S4, and Z-S17 and Z-S18
here. All four are routed to `2.0.0_SA_COO~C`, the issuer of TO-CT-s-8, which landed the fallback at 10afe6b697. Z-S17
is the sharpest of them: a judgment criterion reads GRADED off any old CVO row that mentions its bare id.

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-S17",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "round-close-check.py grade_criterion matches the bare criterion id against json.dumps of every CVO-authored row in the project, with no scope to the order, the round or the row's date; it also printed MAY-CLOSE while one order of the round was not complete.",
    "evidence": [
      "Reproduced 2026-10-09 08:2xZ: --round 4 read TO-IAM-u-1/u-2/u-3 AC4 GRADED off Z-C-S8 (a 2026-09-10 round-2 row) before any round-4 grade existed.",
      ".tools/round-close-check.py:242-265."
    ],
    "remedy": "Scope a grade to the order: require the row to name the order id (or the order's to_id) beside the criterion id, and count an order that is not terminal against MAY-CLOSE.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~C", "round": "v4"},
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~C", "at": null},
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S18",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "safe-commit's close-gate grades a dep_stage -> ROUND_CLOSE flip over every order of the project, not the closing round, and the file-stem id fallback reads 18 historical VALID proofs PROOF-BAD.",
    "evidence": [
      "Close-gate line at b756665567: orders=21 proof_ok=3 proof_bad=18, verdict REFUSED (WARN mode, admitted).",
      "Same fallback as NFRA_REPORT-Z-S26 and NFRA_MCPMSP-Z-S4 (round-close-check.py:159, 10afe6b697)."
    ],
    "remedy": "Before the close-gate moves to ENFORCE: scope it to the closing round and make the id fallback match the proof's heading id. Do not edit closed orders to fit the gate.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~C", "round": "v4"},
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~C", "at": null},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
