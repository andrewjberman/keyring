# NFRA_MCPORTAL -- rounds 3-4 L8 compile + L9 (site Z) -- 14 of 14 undispositioned rows dispositioned; FWD-14 NOT REALIZED (built, not released); L10 precondition NOT MET at the project grain (2 staged round-3 orders)

Author: 3.0.0_SA_CVO~Z, signing for 3.0.0_SA_CVO~O (not seated; 3.0.0_SA_CVO~Z signed v0.5's ratified half @8de5b2dc76).
Round: v3. Fabric: site-z. Recorded: 2026-10-09T00:3xZ.
**Input:** `2.0.0_SA_COO~MP` `deliverables/2.0.0_SA_COO~MP/round4/ROUND4_DRAIN_PACKET.md` @5061ff3042, 65 lines, read to EOF.
Msgs 32122 and 32130. Round 4 had 2 of 2 orders terminal (MP-x-1, MP-x-2); round-close-check reads MAY-CLOSE. No compile
was written for round 3, so its nine open rows (Z-S10 to Z-S17, Z-W1-S6) are dispositioned here with round 4's five.

## The one real run, read again by this seat

The packet's run read the live store at 23:07Z: dell2 409, laptop 268, dell1 120, sitez "not reporting". This seat ran
`.tools/fabric-activity.py boxes --hours 6` at ~00:1xZ on 10-09 and got 816 commits from 2,261 records. dell2 (422), laptop
(266) and dell1 (128) all read `measured`, and site Z has no row, so "not reporting" is the true state (C12). The counts
moved with the window, as the packet's own cross-check says they would.

## L9

There are no judgment criteria this round. FWD-14's judgment (Andrew names one box's projects from the page, G-SEE) sits
on MP-x-5 in round 5.

## FWD grade

| FWD | grade | basis |
|---|---|---|
| 14 | **NOT REALIZED** | The handler (MP-x-1) and the page (MP-x-2) are built, drained and tested. They are not live: the release is MP-x-4 (G-REL, after NFRA_OPLGTW r29). The store read needs MP-x-3's grant (row Z-S18, ruled (a)). DONE WHEN is "Andrew names one box's projects this afternoon from the page alone", which is unexercised. |
| 15-19 | **NOT REALIZED** | Not cut. |

## Rows (14 of 14 dispositioned)

| row | disposition | basis |
|---|---|---|
| Z-S10 (ARMED) | GRADUATED; DISARMED and REMEDIATED (`REMEDIATION_v3.Z.md`) | The deployed writer was downloaded by this seat. It is byte-identical to HEAD after the 10-03 redeploy, and line 325 stores the claim name and email only. |
| Z-S18 | GRADUATED, OPEN | MP-x-3 under ruling (a), applier `0.7.0_AE_CloudOps~Z`. |
| Z-W5-S2 (BLOCKING) | GRADUATED, OPEN | The issuer's cut recipe: no-cone worktrees. |
| Z-S11, Z-S17 | DISMISSED | Disarm records for Z-S10. Their evidence is carried into Z-S10's remediation row. |
| Z-S12 | DISMISSED | The stale writer test was fixed inside MP-b-3: the writer suite reads 24 passed at HEAD (run by this seat). |
| Z-S13 | DISMISSED | The disarm record for Z-W2-S3, whose row is advanced in place (conftest at HEAD; the tracked audit file is clean). |
| Z-S14 | DISMISSED | The surface is NFRA_OPLGTW's Schwab-engine suite, not this project's. |
| Z-S15, Z-S16, Z-W1-S6 (BLOCKING) | DISMISSED | The halt gate admits multi-letter lanes at HEAD (`halt-gate-check.sh:239`, from @64a3ef4b4e), and MP-a-2, the blocked apply, is complete. |
| Z-S19 | DISMISSED | The one-issuance limb acted as designed; MP-x-3/4/5 are on the round-5 list. |
| Z-W5-S1, Z-W6-S1 | DISMISSED | Subsumed by Z-W5-S2's remedy. |

## L10 PRECONDITION

Both orders are terminal. Every BLOCKING row (Z-W1-S6, Z-W5-S2) and every OPEN ARMED row (Z-S10) is dispositioned here. The ARMED
rows that remain are graduated rows from round 1 with owners: Z-W3-S3 and Z-C-S10 (`REMEDIATION_v1.Z.md`,
2.0.0_SA_COO~O), and Z-W1-S1 (1.0.0_SA_CTO). They are dispositioned, not disarmed, and the slug names them.

**NOT MET at the project grain (corrected 2026-10-09 ~00:5xZ).** Round 4's 2 orders are terminal, but the surprise-row gate
reads every order of the project. 2 of 20 are not terminal at HEAD: `NFRA_MCPORTAL.TO-MP-c-1.fwd1-close-run.md` [staged]
(the FWD-1 close run, held by Andrew until gateway r29) and `NFRA_MCPORTAL.TO-MP-v-1.fwd2-live-arms.md` [staged]. So the
slug's remediation rows (`REMEDIATION_v3.Z.md`, and Z-W2-S3's in-place advance) are written but not landed. They land
when both orders are terminal or when a named exception is recorded. That is the issuer's and the CTO's call, not this
seat's.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S22",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S10 GRADUATED and DISARMED on the deployed bytes (writer byte-identical to HEAD after the 10-03 redeploy, who = claim name + email); Z-S18 GRADUATED OPEN (MP-x-3, ruling (a)); Z-W5-S2 GRADUATED OPEN (no-cone worker worktrees); FWD-14 built, not released.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The L8 compile dispositions every undispositioned row; C12 says a box with no record reads 'not reporting'; the CTO's privacy condition keeps the owner-key value out of every record.",
    "world_is": "The live store has dell2, laptop and dell1 measured and no site-Z record. The deployed grant writer stores the claim name and email only. The portal's store read waits on a grant against NFRA_CLDGRPH's no-grant control, and a cone-mode worker worktree cannot pass the org/missions commit gates.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S10",
      "NFRA_MCPORTAL-Z-S18",
      "NFRA_MCPORTAL-Z-W5-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S10, #NFRA_MCPORTAL-Z-S18, #NFRA_MCPORTAL-Z-W5-S2",
        "aws lambda get-function mcportal-grant-writer-lambda, read by 3.0.0_SA_CVO~Z 2026-10-09 ~00:2xZ: LastModified 2026-10-03T20:07:55Z; zip sha256 equals CodeSha256; lambda_function.py byte-identical to HEAD; line 325",
        ".tools/fabric-activity.py boxes --hours 6, run by 3.0.0_SA_CVO~Z 2026-10-09 ~00:1xZ: dell2 422, laptop 266, dell1 128 measured; no sitez row",
        "deliverables/2.0.0_SA_COO~MP/round4/ROUND4_DRAIN_PACKET.md @5061ff3042"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S23",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S11 and Z-S17 dismissed with reason -- disarm records for Z-S10, carried into its remediation row.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row.",
    "world_is": "Z-S11 records the ruling and the fix cell; Z-S17 measures the deployed bytes on 10-01. Neither opens a hazard; this seat re-measured the bytes after the 10-03 redeploy.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S11",
      "NFRA_MCPORTAL-Z-S17"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S11, #NFRA_MCPORTAL-Z-S17",
        "remediations/REMEDIATION_v3.Z.md#NFRA_MCPORTAL-Z-S10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both are disarm records for Z-S10 by its disarm owner, not new hazards; their evidence is carried into Z-S10's remediation row, which this seat closed on its own read of the deployed bytes."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S24",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S12 dismissed with reason -- the stale grant-writer test was remedied inside MP-b-3; the writer suite reads 24 passed at HEAD.",
    "class": "OBSERVATION",
    "spec_asserts": "The writer's own suite is green at HEAD.",
    "world_is": "pytest infra/aws/lambda/mcportal/mcportal-grant-writer-lambda, run by 3.0.0_SA_CVO~Z 2026-10-09 ~00:1xZ: 24 passed, 0 failed.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S12"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S12"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedied in-round by MP-b-3, and measured green at HEAD (24 passed). The row's note that no gate ran a dependent project's suite is recorded, not proposed as a gate."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S25",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S13 dismissed with reason -- the disarm record for Z-W2-S3, whose remediation row is advanced in place to DISARMED and REMEDIATED.",
    "class": "OBSERVATION",
    "spec_asserts": "Gateway tests never write the tracked audit.jsonl.",
    "world_is": "tests/conftest.py:22-23 and :53-62 at HEAD point AUDIT_PATH at a temp file; git status --porcelain on infra/aws/ec2/opal-gateway/audit.jsonl reads empty.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S13"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S13",
        "remediations/REMEDIATION_v2.Z.md#NFRA_MCPORTAL-Z-W2-S3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record by the disarm owner; Z-W2-S3's own row now carries the disarm and the remediation close."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S26",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S14 dismissed with reason -- the full-suite stall is in NFRA_OPLGTW's Schwab-engine tests, not this project's surface.",
    "class": "OBSERVATION",
    "spec_asserts": "This project's drains grade this project's surfaces.",
    "world_is": "The stall is an inter-file interaction at app/integrations/schwab/engine.py:1103 under the full gateway suite; the engine file passes alone.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S14"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S14"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Outside this project's surface: the Schwab engine is NFRA_OPLGTW's. The finding is named in the slug so that project's CTO can place it."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S27",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S15, Z-S16 and Z-W1-S6 (BLOCKING) dismissed with reason -- the halt gate admits multi-letter lanes at HEAD and the blocked apply (MP-a-2) is complete.",
    "class": "OBSERVATION",
    "spec_asserts": "A seated two-letter COO lane and its workers can pass the halt gate.",
    "world_is": ".tools/halt-gate-check.sh:239 refuses a lane only when it does not start with A-Z or holds a character outside A-Z0-9; MP-a-2's last status reads complete (AC1-AC4 PASS, ledger CLOSED).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S15",
      "NFRA_MCPORTAL-Z-S16",
      "NFRA_MCPORTAL-Z-W1-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S15, #NFRA_MCPORTAL-Z-S16, #NFRA_MCPORTAL-Z-W1-S6",
        ".tools/halt-gate-check.sh:219-240 at HEAD",
        "task-orders/NFRA_MCPORTAL.TO-MP-a-2.writer-apply-sub.md:124"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed by the gate owner (@64a3ef4b4e, widened since) and the blocked act completed; nothing remains blocked or half-landed."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S28",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-S19 dismissed with reason -- the one-issuance limb acted as designed; MP-x-3, MP-x-4 and MP-x-5 are on the round-5 list.",
    "class": "OBSERVATION",
    "spec_asserts": "A round's cells are cut in its one issuance.",
    "world_is": "to-pipeline-gate refused a late cut; the three cells are the packet's proposed round-5 enrichment list.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S19"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S19"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The gate worked as written; the cost is a one-round delay the analysis absorbs, and the issuer's stated practice (STAGED cells with placeholders in the first issuance) needs no remedy row."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S29",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T00:30:00Z",
    "one_line": "Rounds 3-4 L8: Z-W5-S1 and Z-W6-S1 dismissed with reason -- the same sparse-cone defect as Z-W5-S2, closed by its remedy.",
    "class": "OBSERVATION",
    "spec_asserts": "A worker's cut worktree passes the commit gates.",
    "world_is": "Both rows name paths missing from the cone (org/modules/graph, org/projects, infra/logic, sibling project trees, org/surprise_channel); the no-cone pattern list in Z-W5-S2 carries them all.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W5-S1",
      "NFRA_MCPORTAL-Z-W6-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W5-S1, #NFRA_MCPORTAL-Z-W6-S1",
        "remediations/REMEDIATION_v3.Z.md#NFRA_MCPORTAL-Z-W5-S2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Subsumed by Z-W5-S2, whose remediation row is OPEN with the issuer; one remedy closes all three."
  }
]
```

-- 3.0.0_SA_CVO~Z
