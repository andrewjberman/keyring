# LGIC_BLANKFIX -- remediations, round 8

<sweep_watermark>2026-10-09T04:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-09 ~04:1xZ. Graduated at this compile (ADJUDICATION_v7.md): 8 rows, INERT, not closed. The
project moves to dell1 for round 9; owners are the seats that must act, and 1.0.0_SA_CTO's round-8 analysis carries them there.
Clocks advanced: W1-S15 REMEDIATED (CLAUDE.md:197 now reads "the commit-time naming gate REFUSES names today", LAW EDIT
c55a7b39cd, matching org/mcp/naming-gate.enforce); W4-S3 REMEDIATED (irpt-intake-poll now prints NOT-ASKED with its expression's
reason, not 'no cadence row'). Still OPEN: S10 (9 entries held), S11, W2-S2.

```json
[
  {
    "id": "LGIC_BLANKFIX-W1-S19",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The placement step exits 1 on a refusal, but .tools/safe-commit.sh and .tools/safe-apply.sh act on that exit only while the older switch naming-gate.enforce (or its env) is on, so the new switch alone blocks nothing.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W1-S19",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P1, before the switch goes on. The CTO rules whether the callers honour naming-place.enforce on its own. Done when, with only the new switch present, a placement refusal aborts the commit and the apply.",
    "owner": "1.0.0_SA_CTO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W1-S21",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The build has no override (the design's arm H), so with the switch on a NEW name owed a registry row refuses until 4.0.0_SA_CRO writes the row.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W1-S21",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P1, before the switch goes on. Build arm H (an R20 register id the gate can look up; a made-up id still refuses) or rule that none is wanted. Done when that decision is recorded and, if built, arm H holds.",
    "owner": "1.0.0_SA_CTO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W1-S22",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The placement step runs on every commit touching infra/aws .tf even with the switch absent: about 13-15 s against about 2 s, capped at 8 roots, for a refusal that is off.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W1-S22",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P1. Gate the step on the switch, or measure and accept the cost by ruling. Done when a .tf commit with the switch absent costs what it did before the step, or the ruling names the accepted cost.",
    "owner": "1.0.0_SA_CTO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W4-S7",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "47 mapped-root names (45 news-pipeline, 2 portal) are skipped by cards written when news and portal were unresolved; the registry has since resolved both, so the cards print HOLE for names grade() can place.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W4-S7",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P1. The registry's lane writes the drafted name rulings or retires the stale cards. Done when the 47 lines print FIX or RIGHT.",
    "owner": "4.0.0_SA_CRO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W4-S8",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The platinum grammar reads one table level then entity partitions, so served portal keys with a sub-folder raise K4a, and the drafted rulings fold the folder into the table word, which would rename the portal's request paths.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W4-S8",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P2. The registry's owner rules the grammar (admit a sub-folder, or move these keys to gold). Done when the ruling is recorded and the keys' drafted canonicals follow it.",
    "owner": "4.0.0_SA_CRO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W4-S6",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The all command prints UNCOUNTED lines only for mapped roots, so an unmapped root's by-reason uncounted count needs a second read.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W4-S6",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P2. Print unmapped roots' UNCOUNTED lines, or a by-reason count, in the all output. Done when the round's uncounted delta is read from one all run.",
    "owner": "1.0.0_SA_CTO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-W5-S2",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "infra/logic/10_ONBOARDING_CHECKLIST.md STEP 13 still types 'takes about 15 seconds', the kind of figure round 8 removed from the README.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row W5-S2",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P2. Remove the typed timing from STEP 13. Done when the checklist carries no typed run time.",
    "owner": "4.0.0_SA_CRO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-S12",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ROOTCHECK-TEST case 5 and exercise_fwd6_arms.py arm F read a live HOLE in the intake root that the CRO's round-8 registry write closed before the merge, so both criteria read false on the trunk.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 row S12",
      "adjudication row LGIC_BLANKFIX-C-S20"
    ],
    "remedy": "P1. Plant the HOLE in the overlay text, as arm D does, instead of reading one off the estate. Done when both scripts print ok=True on the trunk and stay true when the registry closes holes.",
    "owner": "1.0.0_SA_CTO",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v9"
    },
    "closed": false
  }
]
```
