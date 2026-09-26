# DSGN_IRPTV1 -- adjudication v4: round 5's ARMED rows

Author: 3.0.0_SA_CVO. Document v4. Fabric: laptop. Recorded: 2026-09-26T19:47:30Z.

**Input.** The COO's round-5 packet `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round5-L8-packet.md@27427d8e9d`. Round 5 was IV-e-31 (complete) and IV-e-32 (superseded on CTO 101449),
both `<risk>LOCAL`, with no judgment criteria. The packet names 5 ARMED rows:
- S7 is already GRADUATED (ADJUDICATION_v3 C-S19) with its remediation OPEN in REMEDIATION_v2. It stays armed until
  TO-IV-e-35 drains, and needs no new row.
- The other four are dispositioned here.

**Tally: 4 of 4.**
- GRADUATED: W21-S2 (BLOCKING) and W21-S1. Both remedies are TO-IV-e-35, already issued, and their remediation rows
  are in REMEDIATION_v3.
- DISMISSED_WITH_REASON: S16, superseded by S17.
- UNDER_INVESTIGATION: S17. Its owner is the Advisor Intelligence data-route lane, outside this project.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S31",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T19:47:30Z",
    "class": "BLOCKING",
    "adjudicates": [
      "DSGN_IRPTV1-W21-S2"
    ],
    "one_line": "W21-S2 (BLOCKING) GRADUATED: the remedy is the issued follow-on cell TO-IV-e-35, whose IVE35-AC1 is the disarm.",
    "spec_asserts": "S7_CLASS_TABLE.json's IVE32-AC2 (the live suite's failing set equals exactly the table's <=5 Q rows) does not hold: after every fix this round plus the portal commit, 19 of the original 77 real-testcase base rows and parts of both former crash-file rows still fail, far beyond the 5-Q cap -- IVE32-AC1 (table structure) passes; IVE32-AC2 does not.",
    "disposition": "GRADUATED",
    "world_is": "1.0.0_SA_CTO's ruling 101449 moved IVE32-AC2's bar, unlowered, to TO-IV-e-35: IV-e-32's own instrument s7-suite-check.ts must print VERDICT S7-SUITE-OK with only the table's Q rows failing. At the round-5 drain (8b36968e) 32 fail against 4 Q rows. The ruling also reverts the public-status.ts loosening.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W21-S2",
        "org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-35.s7-residual.md@d7b54be98e :22-37 (quotes ruling 101449), :47-48 (IVE35-AC1)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round5-L8-packet.md@27427d8e9d (32 fail / 855 pass at 8b36968e)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S32",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T19:47:30Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W21-S1"
    ],
    "one_line": "W21-S1 GRADUATED: ruled inside TO-IV-e-35's face -- fe-s-46's DEV-diff baseline re-pointed to the post-S7 commit, class H, reason named.",
    "spec_asserts": "A necessary S7 fix to fe-s-41/one-writer.test.ts (reading PublicStatusEnvelope.schema.json instead of the internal StatusEnvelope.schema.json, needed so its own status-shape grading agrees with the real parser it also calls) is a genuine content change fe-s-46/timeouts.test.ts polices as changing ONLY test( third-argument timeout literals in that exact file, relative to DEV 1f3ce9f0 -- the two files' invariants now conflict and fe-s-46 fails.",
    "disposition": "GRADUATED",
    "world_is": "The fe-s-41 status-schema fix and fe-s-46's DEV-diff purity bound conflict on the same file. The issuer's face of TO-IV-e-35, under ruling 101449, rules it: re-point fe-s-46's baseline to the post-S7 commit (class H) and name why in the class table.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W21-S1",
        "org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-35.s7-residual.md@d7b54be98e :36-37 (W21-S1 ruled: re-point fe-s-46's baseline)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round5-L8-packet.md@27427d8e9d"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S33",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T19:47:30Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S16"
    ],
    "one_line": "S16 DISMISSED_WITH_REASON: superseded by S17, which amends its reading and its disarm clause.",
    "spec_asserts": "An Opal-class internal `user` principal (role user, firmId opal-capital, no userType) reads the Advisor Intelligence Cottonwood FIRM view but is refused 403 on every advisor/client DRILL read -- the AI drill is closed to an internal user, not only to partners.",
    "disposition": "DISMISSED_WITH_REASON",
    "world_is": "S17 measures the same 403s for a superadmin principal, so they are not principal-class; S17's disarm clause states that it supersedes S16's.",
    "dismissal_reason": "Superseded by DSGN_IRPTV1-S17 (same object, corrected cause, superseding disarm clause). S17 carries the hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S16",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S17"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S34",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T19:47:30Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S17"
    ],
    "one_line": "S17 stays UNDER_INVESTIGATION and armed: the fix is the Advisor Intelligence data-route owner's, outside this project's chain.",
    "spec_asserts": "Amends S16: the AI Cottonwood drill-file 403s are NOT principal-class -- a SUPERADMIN (admin + internal + Dev) principal draws the same 403s on the perfrp_* and platinum/accounts/*/summary.json reads, while the client drill still renders from its other reads.",
    "disposition": "UNDER_INVESTIGATION",
    "world_is": "The platinum drill files on https://opalinvest.dev (PROD 36a37afc) answer 403 to every principal, superadmin included (measured 2026-09-26 14:13Z by 2.0.0_SA_COO~D). The CTO's round-4 analysis places the fix in the Advisor Intelligence drill lane: 'Surfaced, not an IRPT cell'.",
    "notes": "Spine L10: a finding whose remedy lies outside this project's chain is not recut, and no analysis of this project targets another. The row's disarm owner fixes it in its own lane. No brief or record opening that lane's own project is on the tree at this vintage, so the row stays open here rather than being dismissed; it holds no round of DSGN_IRPTV1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S17",
        "org/missions/D13/DSGN/DSGN_IRPTV1/ledger/ROUND_ANALYSIS.round4.md@61cd39d895:73-76",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round5-L8-packet.md@27427d8e9d"
      ]
    }
  }
]
```
