# LGIC_BLANKFIX -- remediations

<sweep_watermark>2026-10-07T16:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-07 ~16:2xZ. Graduated at this compile (ADJUDICATION_v1.md): 5 rows, all INERT, none closed.
S4 carries the judgment criterion BE8-AC3 (NOT MET). W2-S4 and W2-S2 are calls owned by 1.0.0_SA_CTO.

```json
[
  {
    "id": "LGIC_BLANKFIX-S4",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "18 of the thread's 140 lines cannot be acted on from the line alone, so FWD-1's ACCEPT is not met although the run prints hole=0: 8 NOT-ASKED lines print a different name beside 'not asked' and give no reason; 6 CARDED lines are a kind of line FWD-1 does not admit and carry no correct name; 2 REFUSED lines state a problem in misleading words and no act; 2 FIX lines give two EC2 instances the same target name.",
    "evidence": [
      "live run by 3.0.0_SA_CVO 2026-10-07 16:1xZ: python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only, rc 0, last line 'ROOTCHECK ok=True ... items=140 right=9 fix=113 not_asked=9 pattern=1 carded=6 refused=2 hole=0'; 0 lines differ from the saved trace @7145fcd3eb",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md@7145fcd3eb rows S4, W2-S5, W1-S3",
      "adjudication row LGIC_BLANKFIX-C-S1"
    ],
    "remedy": "P1. Each of the four groups ends as one of FWD-1's three kinds of line or as FWD-8's pattern line: a NOT-ASKED line says why and says whether the printed name is a rename; a carded key prints its whole correct name or says plainly that none is owed; a refused key says what was measured (a Cottonwood-named file in this firm's bucket) and what the reader does; two resources never share a target. Done when a seat that built none of it reads a live run of the root and acts on 140 of 140.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W7-S1",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The folder map holds one root. 119 repository names are unassigned, 51 of them in folders that two or more Terraform roots claim, because the scope of 11 roots (and the system of two, the source of the investor-reporting roots other than ycharts) is not decided anywhere the repository can be read for it.",
    "evidence": [
      "infra/logic/registry/root_map.json at HEAD: 1 entry (this seat's read)",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md@7145fcd3eb rows W7-S1, W1-S1, W7-S2, W1-S2",
      "adjudication row LGIC_BLANKFIX-C-S2"
    ],
    "remedy": "P1 for FWD-7. The registry's owner decides scope, system and source for the 11 roots and says which root owns each contested folder, the shared investor-reporting parent included; the map is then rebuilt and the unassigned count read again (a scratch map with the eleven owners assigned 40 of the 51).",
    "owner": "4.0.0_SA_CRO",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-W3-S2",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two match keys cannot tell two things apart: a root-map exception is keyed (name, type), so two same-named resources of one root with different owning roles take one answer; a legacy_addresses row matches a key by path with no bucket, so a key in one firm's bucket can match another firm's legacy row.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md@7145fcd3eb rows W3-S1, W3-S2",
      "adjudication row LGIC_BLANKFIX-C-S2"
    ],
    "remedy": "P2. The registry's owner rules whether an exception may carry its owning role or declaration line, and whether a legacy row is bucket-scoped; the reader then matches on that key. ROUND_ANALYSIS round 1 E3 already says a match is on (bucket, key).",
    "owner": "4.0.0_SA_CRO",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-W2-S4",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-BF-e-8 rule 1 fills an inline policy's system from its role and does not say which wins when the root map already carries a ruled exception for that name. decide() lets the exception win, so three lines kept their ruled families; had the role won they would print advi- and contradict three rulings.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md@7145fcd3eb row W2-S4",
      "adjudication row LGIC_BLANKFIX-C-S3"
    ],
    "remedy": "P2, a call. 1.0.0_SA_CTO rules which wins, a ruled exception or the owning role, and the rule is written where the next cell reads it. Done when the ruling is on file and the root check's three lines agree with it.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-W2-S2",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADING_RULE.md still records pandas-pyarrow-layer as a library layer that takes a {system}, against the fourth verdict; lib/tests/test_opal_naming.py overrides that one worked case at load time and says why. The file's owner project, LGIC_NAMING, is closed.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md@7145fcd3eb row W2-S2",
      "adjudication row LGIC_BLANKFIX-C-S3"
    ],
    "remedy": "P2, a call. 1.0.0_SA_CTO names who corrects the worked case and its V-2 wording in GRADING_RULE.md; the test's load-time override is then removed. Done when the file and the test agree with no override.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
    "closed": false
  }
]
```
