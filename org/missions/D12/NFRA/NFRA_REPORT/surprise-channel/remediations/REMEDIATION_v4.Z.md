# NFRA_REPORT -- surprise channel, REMEDIATION v4 (site Z) -- ROUND 4 L10 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-09 ~07:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

**Round 4 is terminal** at `4363c202c0` (2.0.0_SA_COO~ZZ): RP-s-12/21/22 complete with proofs OK; RP-s-23/24
SUPERSEDED by Andrew-direct 2026-09-17 ("id have CRO~N just finish the project end to end").
`round-close-check.py --project NFRA_REPORT --round 4` read at this seat: verdict=MAY-CLOSE, orders=5,
judgment=1 graded=1 ungraded=0 self_graded=0, reviewer present.

**Channel at this cut** (`comp-surprise --project NFRA_REPORT --armed --json`, read 07:15Z): 43 investigation
items, 16 adjudication rows, 16 remediation rows; OPEN 0; ARMED 8. All 8 ARMED items were GRADUATED with a
ruling on file and no remediation row recording the disarm. This document records those 8 disarms, plus one
open remediation for Z-S26. After it lands, the ARMED count should read 0.

**Live read at this seat (07:1xZ):** `aws lambda get-function-configuration --function-name
opal-infrastructure-monitor` -> CodeSha256 `iU6tKUas0Q0SjxzoxlP6IYzRWAIRyPsdP8ee38HzpKg=`, LastModified
2026-09-17T14:54:07Z, CodeSize 43125: equal to Z-S25's read and to the CRO~N close record. The round-4 edition
is not served; format_report is.

```json
[
  {
    "id": "NFRA_REPORT-Z-S24",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-4 edition flattened every section to (state, delta) and dropped the old report's content; Andrew read it and could not use it.",
    "evidence": [
      "Z-S25 (2.0.0_SA_COO~ZZ, 2026-10-09T05:30Z) disarms it with a live read; this seat repeated the read at 07:1xZ and it matches: CodeSha256 iU6tKUas0Q0SjxzoxlP6IYzRWAIRyPsdP8ee38HzpKg=, LastModified 2026-09-17T14:54:07Z.",
      "The served body is format_report, restored by 4.0.0_SA_CRO~N (67168eba8c, 013f755c74) on Andrew's word of 2026-09-17; change record 20260917T1420Z CLOSED.",
      "The disarm condition Z-S24 named had two arms: a content-carrying edition read by Andrew, OR Andrew's word on the shape. The second arm fired: Andrew replaced the edition."
    ],
    "remedy": "Remedied by revert on Andrew's word, not by the round-4 edition. The edition code (edition.py, edition_rows.py) is unwired. Whether FWD-13/FWD-15 are retired or re-specified is the CTO's L2/L4 call in the round-4 analysis.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~ZZ", "at": "2026-10-09T05:30:00Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-C-S16",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "This seat's graduation of Z-S24: FWD-15 FAILED on its own EXERCISED bar because the named reader could not use the edition.",
    "evidence": [
      "Same disarm as Z-S24 above: the edition is no longer served (live read 07:1xZ), and Andrew's word of 2026-09-17 replaced it.",
      "Its notes said NFRA_REPORT could not reach L10 while two orders read open and this row was ARMED. Both orders are now SUPERSEDED (4363c202c0) and the hazard is gone."
    ],
    "remedy": "As Z-S24. FWD-15 stays FAILED as graded; the CTO rules whether it is retired with the edition or carried.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~ZZ", "at": "2026-10-09T05:30:00Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S19",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Eight of eleven REALIZED grades sat on DONE WHEN = EXERCISED bars the graded artifact could not meet.",
    "evidence": [
      "1.0.0_SA_CTO~Z upheld it without amendment and re-graded the eight REALIZED -> APPLIED at b75e35f36e (2026-09-10T14:21Z).",
      "C-S14 declared the disarm and deferred recording it to this round's slug, because the plane admits one remediation row per id."
    ],
    "remedy": "The re-grade, written into both artifacts in place by the CTO.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "1.0.0_SA_CTO~Z", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "1.0.0_SA_CTO~Z", "at": "2026-09-10T14:21:27Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-C-S14",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "This seat's graduation of Z-S19.",
    "evidence": [
      "Discharged by the same CTO re-grade, b75e35f36e. The row itself named this slug as the place the disarm is recorded."
    ],
    "remedy": "As Z-S19.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "1.0.0_SA_CTO~Z", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "1.0.0_SA_CTO~Z", "at": "2026-09-10T14:21:27Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-W1-S7",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-RP-s-21 AC2/AC4 called compute_verdict on rows that never carry 'delta', so no correct port could pass them.",
    "evidence": [
      "Issuer ruling Z-S20 (2.0.0_SA_COO~ZZ, 2026-09-10T15:20Z) upheld it, recut AC2/AC4 to attach delta as a caller must, and placed the delta-attach loop in RP-s-23.",
      "RP-s-21 is complete with proof_ok (round-close-check, read at this seat 07:1xZ)."
    ],
    "remedy": "Criteria recut by the issuer (Z-S20); the order then completed against the recut.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~ZZ", "at": "2026-09-10T15:20:00Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-W3-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Round-4 orders carried the issuer as a markdown line, not the <issued_by> tag halt-gate-check.sh reads, so safe-apply could not admit the worker.",
    "evidence": [
      "Issuer ruling Z-S21 (2.0.0_SA_COO~ZZ, 2026-09-10T16:40Z) upheld it as the issuer's format defect, ratified the worker's in-paths tag, and fixed RP-s-24 before its worker hit the gate.",
      "halt-gate-check.sh still reads the <issued_by> tag only (halt_gate_worker_issuer, :185); the estate convention is the tag, so the gate is correct as designed.",
      "No NFRA_REPORT order is open (round 4 terminal), so no worker of this project can meet the gap again."
    ],
    "remedy": "Issuer format corrected for the round; the tag is the estate convention. Nothing owed in the gate.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~ZZ", "at": "2026-09-10T16:40:00Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-W3-S2",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RP-s-23 AC3's bare ROW_FACTS substring search could not tell a docstring citation from an embedded fact list.",
    "evidence": [
      "Issuer ruling Z-S23 (2026-09-10T17:10Z) reclassified AC3 as a judgment criterion for L9 rather than recut it a third time.",
      "RP-s-23 is SUPERSEDED at 4363c202c0 by Andrew's word of 2026-09-17; the edition it deployed is no longer served (live read 07:1xZ). No L9 judgment is owed on it."
    ],
    "remedy": "None applied: the criterion was never recut and its order was superseded. Closed because no order or served artifact remains for it to grade.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "CLOSED_UNREMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4", "closure": {"reason": "NOT_A_DEFECT", "pointer": "NFRA_REPORT-Z-S23 (issuer ruling: AC3 amended to a judgment criterion) + 4363c202c0 (RP-s-23 SUPERSEDED on Andrew's word of 2026-09-17)"}},
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~ZZ", "at": "2026-10-09T05:30:00Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-W3-S3",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A live message claiming issuer authority reached a worker, which rule 27 says cannot be messaged; its technical prediction was false.",
    "evidence": [
      "Issuer row Z-S23 (2026-09-10T17:10Z, commit f94c40f032) confirmed authorship through the file carrier: the message was 2.0.0_SA_COO~ZZ's, not an injection.",
      "The same row ran the recut and measured FACT_TABLE_CARRIERS=2, confirming the worker's refusal."
    ],
    "remedy": "Authorship confirmed on the file carrier; the worker's refusal stands as correct. No order was changed by the message.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~ZZ", "at": "2026-09-10T17:10:00Z"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S26",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round-close-check.py takes a TO id from the file stem when <to_id> is absent, while proofs carry the heading id, so legacy orders read PROOF-BAD.",
    "evidence": [
      "Read at this seat: .tools/round-close-check.py:159 -- \"id\": tag(text, \"to_id\") or the file stem; landed by 10afe6b697 (0.9.0_WK_NFRA_CTLPLN~18, TO-CT-s-8, issued by 2.0.0_SA_COO~C).",
      "For this project the issuer added <to_id> to RP-s-12/21/22 (4363c202c0); round-close-check then read proof_ok=3, MAY-CLOSE (re-run at this seat 07:1xZ).",
      "Other projects' legacy orders without <to_id> are not censused; the row says so."
    ],
    "remedy": "OPEN with the NFRA_CTLPLN issuer: make the fallback match the heading id (or the proof's to_id), then census legacy orders on other projects.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~C", "round": "v4"},
    "closed": false
  },
  {
    "id": "NFRA_REPORT-Z-S17",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The issuer's withdrawal of Z-S16's conclusion: a 9AM weekday report already fires (infrastructure-monitor-daily).",
    "evidence": [
      "REMEDIATION_v3.Z.md records Z-S16 as a withdrawn claim, DISARMED 2026-09-10T11:57Z; this row is the withdrawal itself."
    ],
    "remedy": "None owed: the row corrects a claim and asserts no defect.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "CLOSED_UNREMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4", "closure": {"reason": "NOT_A_DEFECT", "pointer": "NFRA_REPORT-Z-S16 row in REMEDIATION_v3.Z.md (withdrawn claim)"}},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S18",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S10's disarm condition was met on the artifact when RP-s-20 landed, but the record had not moved.",
    "evidence": [
      "Z-S10 was disarmed in place on its row in REMEDIATION_v1.Z.md (REMEDIATION_v3.Z.md header); ATTRIBUTION.md renders opal-gateway as Gateway and opal-globgrph as Graph per the row."
    ],
    "remedy": "The record was advanced in place on Z-S10's row.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S20",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer ruling on Z-W1-S7: AC2/AC4 recut so the caller attaches delta.",
    "evidence": [
      "RP-s-21 completed against the recut criteria; proof_ok (round-close-check re-run at this seat 07:1xZ)."
    ],
    "remedy": "Criteria recut by the issuer; the order completed.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S21",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer ruling on Z-W3-S1: the markdown issuer line is the issuer's format defect; the <issued_by> tag is the convention.",
    "evidence": [
      "The worker's in-paths tag was ratified and RP-s-24 was fixed before its worker reached the gate; halt-gate-check.sh reads the tag (:185)."
    ],
    "remedy": "Issuer format corrected for the round.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4"},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S22",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The issuer's prediction that RP-s-23 AC3 would fail on citation prose, not an embedded fact list.",
    "evidence": [
      "Z-S23 reclassified AC3 as a judgment criterion; RP-s-23 is SUPERSEDED at 4363c202c0 and its edition is not served (live read 07:1xZ)."
    ],
    "remedy": "None applied; the criterion's order is superseded.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "CLOSED_UNREMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4", "closure": {"reason": "NOT_A_DEFECT", "pointer": "NFRA_REPORT-Z-S23 (AC3 amended to judgment) + 4363c202c0 (RP-s-23 SUPERSEDED)"}},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-S23",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer ruling on Z-W3-S3: authorship confirmed, the worker's refusal correct, AC3 reclassified to judgment.",
    "evidence": [
      "Committed at f94c40f032 on the file carrier. RP-s-23 then SUPERSEDED at 4363c202c0, so no L9 grade of AC3 is owed."
    ],
    "remedy": "None owed beyond the ruling itself.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v4",
    "remediation": {"state": "CLOSED_UNREMEDIATED", "owner": "2.0.0_SA_COO~ZZ", "round": "v4", "closure": {"reason": "NOT_A_DEFECT", "pointer": "f94c40f032 (the ruling) + 4363c202c0 (RP-s-23 SUPERSEDED)"}},
    "closed": true
  },
  {
    "id": "NFRA_REPORT-Z-W2-S7",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RP-s-22's AC4 fixture discriminated only 3 of 10 mapped sections; graduated by this seat at C-S15.",
    "evidence": [
      "The edition the fixture tested is unwired and not served (live read 07:1xZ); no fixture repair was made.",
      "If the CTO re-specifies FWD-13/FWD-15 against the served report, a section-level discrimination bar is owed there."
    ],
    "remedy": "Owed only if the edition's bars are re-specified; carried to the CTO's round-4 analysis.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO~Z", "round": "v4", "closure": {"reason": "CARRIED_BY", "pointer": "org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/remediations/REMEDIATION_v4.Z.md"}},
    "closed": true
  }
]
```

## For the CTO (round-4 analysis)

Every round-4 order is terminal, and once this lands every ARMED row is dispositioned. The open question is the
spec. FWD-13 (structure) and FWD-15 (nothing a reader relies on disappears) were bars on the edition, and
Andrew replaced the edition on 2026-09-17. Retire them, re-specify them against format_report, or close the
project on its current served body. Z-S26's checker fix is the NFRA_CTLPLN issuer's and does not hold this
project.
