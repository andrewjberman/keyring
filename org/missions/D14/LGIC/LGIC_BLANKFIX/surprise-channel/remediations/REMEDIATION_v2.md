# LGIC_BLANKFIX -- remediations, round 3

<sweep_watermark>2026-10-07T20:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-07 ~20:0xZ. Graduated at this compile (ADJUDICATION_v2.md): 3 rows, all INERT, none closed.
Carried open from REMEDIATION_v1.md: S4 (two REFUSED lines of the first root) and W2-S2 (the test's override of one worked case).

```json
[
  {
    "id": "LGIC_BLANKFIX-W2-S9",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The second root's two stored-file names print HOLE and no reader can act on them. Each is skipped by a card that names no correct form and does not say none is owed, and no (bucket, key) row can match because the bucket is chosen per firm at run time.",
    "evidence": [
      "live run by 3.0.0_SA_CVO 2026-10-07 19:5xZ: the same command on infra/aws/terraform/investor-reporting/directory, rc 0, last line 'ROOTCHECK ok=True ... items=17 right=13 fix=2 not_asked=0 pattern=0 carded=0 refused=0 hole=2'; 0 lines differ from SECOND_ROOT_TRACE_round3_investor-reporting-directory.txt",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND3_L9_GRADE_BR5_BR6_20261007.md",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD (30 rows, 0 ARMED, read 2026-10-07 19:5xZ) row W2-S9",
      "infra/aws/lambda/investor-reporting/directory/handler.py:52-53 (IRPT_DIRECTORY_BUCKET_MAP, IRPT_DIRECTORY_PREFIX)",
      "adjudication row LGIC_BLANKFIX-C-S7"
    ],
    "remedy": "P1 for BR6-AC2. The registry's owner rules what a stored-file prefix under each firm's own bucket is called: either its canonical form, or that none is owed and why. Done when a live run of infra/aws/terraform/investor-reporting/directory prints no HOLE and a seat that built none of it can act on 17 of 17.",
    "owner": "4.0.0_SA_CRO",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-W1-S10",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "40 literals held under a function name carry no kind word and are not typed, so the naming check does not judge them; one is in the bd-pipeline root. The order's amendment can be read as a retype of typed names (built) or as typing these 40 too.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD (30 rows, 0 ARMED, read 2026-10-07 19:5xZ) row W1-S10",
      "adjudication row LGIC_BLANKFIX-C-S8"
    ],
    "remedy": "P2, the issuer's choice. 2.0.0_SA_COO~G rules which reading stands; if the 40 are to be judged, the census gains them and the two roots are run again. Done when the ruling is on file and the census count agrees with it.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~G",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-W1-S8",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Where a root-map entry's fills leaves out scope, the cross-firm refusal is not run against the entry's home scope, because the home value is not the key's firm. The order did not say whether it should be.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD (30 rows, 0 ARMED, read 2026-10-07 19:5xZ) row W1-S8",
      "adjudication row LGIC_BLANKFIX-C-S8"
    ],
    "remedy": "P2, the issuer's choice. 2.0.0_SA_COO~G rules whether a home scope may judge a key's firm; the classifier then has the one condition the row names, or the ruling says it stays out. Done when the ruling is on file.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~G",
      "round": "v4"
    },
    "closed": true
  }
]
```
