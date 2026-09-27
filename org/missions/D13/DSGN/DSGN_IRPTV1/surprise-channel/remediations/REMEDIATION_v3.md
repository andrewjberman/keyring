# DSGN_IRPTV1 -- remediation v3 (the slug: rounds 5 and 7)

Author: 3.0.0_SA_CVO. Round: v3. Fabric: laptop. Recorded: 2026-09-27T07:35:56Z.

Adjudications: `ADJUDICATION_v4.md` (round 5: C-S31..C-S35) and `ADJUDICATION_v5.md` (round 7: C-S36..C-S53, the prior commits).

**18 rows.**
- 12 are REMEDIATED and DISARMED, each verified at local portal DEV 3f76cdb2.
- 6 are OPEN and ARMED:
  - W21-S2 and W23-S1: the S7 residual, TO-IV-e-50, parked;
  - W29-S8 and W29-S10 (BLOCKING): each needs a 1.0.0_SA_CTO ruling;
  - W29-S9: a flaky test awaiting a granting cell;
  - S19: 28 real-client walk screenshots are still at origin/CLOUD's tip until 0.0.0_AB_MSTR pushes the untrack @cfed2c067b;
    the history purge is Andrew's decision.
- S7 stays OPEN in REMEDIATION_v2, on the same residual.

**Round 5, folded in.** S16 is dismissed (superseded by S17). S17, the Advisor Intelligence drill 403s for every principal, is
DISMISSED_WITH_REASON (C-S35) as outside this project's chain. 1.0.0_SA_CTO is asked to route it to the AI data-route owner.

**Gate note for 1.0.0_SA_CTO.** `.tools/surprise-row-gate.py` refuses a remediation row while ANY task order of the PROJECT is
not terminal. At this commit that is two round-less direct acts: TO-IV-e-50, parked on your W29-S8/S10 ruling, and TO-IV-e-53, the
preview-tenant fix. Spine v3.19 L10 says
the refuser "counts the round's orders, never the project's" (spine :571-574), and every round-7 issuance order is terminal.
This slug lands under the gate's audited override, citing that clause.

```json
[
  {
    "id": "DSGN_IRPTV1-W21-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "fe-s-46/timeouts.test.ts's DEV-diff purity bound refused the necessary fe-s-41/one-writer.test.ts status-schema fix.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W21-S1",
      "portal e330d6dc (merged 9c0cff2f, an ancestor of local portal DEV 3f76cdb2): fe-s-46 keeps DEV='1f3ce9f0' (:176) and pins ONE acknowledged exception (ALLOWED_HUNKS :187-203) that byte-matches the real fe-s-41/one-writer.test.ts hunk -- the row's own 'acknowledged exception' option, not the face's re-point"
    ],
    "remedy": "Executed inside TO-IV-e-35 (e330d6dc): an acknowledged, byte-pinned exception in fe-s-46's diff bound.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-26T22:39:09Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W22-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-34 changed fetchIdentityCardData's signature; a sibling test still called the old one.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S1",
      "iv-e-3.card-fed.test.ts:161,166 at local portal DEV 3f76cdb2 calls fetchIdentityCardData(api, SCOPE_REF) and expects 0 directory-search calls; IdentityCard.tsx:196-199 has the 2-arg signature",
      "c12d37ae is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-34 amendment 2 re-scoped the test (c12d37ae).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-26T20:39:49Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W22-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-33/34 changed the card's kind word; a sibling test pinned the old one.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S2",
      "iv-e-23.identity-firm.test.ts:51 EXPECTED_KIND_WORD = 'Client', with a RE-SCOPED header naming W22-S2",
      "c12d37ae is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-34 amendment 2 (c12d37ae).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-26T20:39:49Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W22-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-33/34 changed the drawer's row detail; a sibling test pinned the old one.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S3",
      "iv-e-8.browse-drawer.test.ts:152-160,188 asserts 'Client' on every row, header naming W22-S3",
      "c12d37ae is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-34 amendment 2 (c12d37ae).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-26T20:39:49Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W22-S6",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Export preview did not follow the Performance tab's one focused account.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S6",
      "export/Preview.tsx:146-158 at local portal DEV 3f76cdb2 passes accountSelection, start and end into resolveBundle; TO-IV-e-36 complete. (The window-10 tenant gap, rows S20/S22, is a separate open defect.)",
      "a5f073c2 is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-36 (a5f073c2, merged fe7beb7a).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-26T21:39:37Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W25-S5",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-47's worker slot was provisioned before the order's commit and could not flip it.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W25-S5",
      "workspace 26f1fa6165 flips TO-IV-e-47 pending -> complete (issuer flip; the slot predated the order); the work is portal b5915df3",
      "26f1fa6165 is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: the issuer's flip @26f1fa6165.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T00:52:56Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A test pinned a colour literal the round's colour work retired.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S1",
      "iv-e-12.unclassified.test.ts:29,119 pins the page's own ASSET_CLASS_COLOR.Equity, retirement header naming W29-S1; IVE45-AC3 3 pass / 0 fail on two runs",
      "1fdbe11b is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-45 amendment 1 (1fdbe11b, merged ad06e37f).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T03:33:47Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W30-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "DEFAULT_LAYOUT did not admit the structured and commodities classes.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W30-S1",
      "TenantLayoutConfig.ts:369 ordered: ['fixed_income','equity','alternatives','structured','commodities']; CTO msg 101649 'DEFAULT_LAYOUT at the drain: yes'",
      "bc9aa02c is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: drain repair bc9aa02c on CTO 101649.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T02:11:37Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "F39-AC7's golden and the face-declutter rule conflicted.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S2",
      "SliceTable.tsx:147-181 puts the classification cells behind <details> (data-classification-open + a scoped style rule); CTO 101768 (a) 'the ordinary case goes one click away'. The ruling named a re-golden of F39-AC7; the fix leaves F39-AC7 unedited and hides the cells, and the window-9 walk shows no such columns on the face (UIR-27 PASS)",
      "5e6befb7 is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-52 on CTO 101768 (a) (5e6befb7, merged 200d257a).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T04:50:20Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two money formats and two client totals on the page.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S3",
      "format.ts:32,41 Intl.NumberFormat currency '$'; HoldingsSummary.tsx:54-55 retires the Current value tile; CTO 101768 'one authoritative total ... HoldingsSummary drops its total'",
      "5e6befb7 is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-52 (5e6befb7, merged 200d257a).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T04:50:20Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S6",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Money-format goldens pinned the retired format.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S6",
      "iv-e-45.face-batch.test.tsx:283-289 expects '$1,234,567.89' and '-$150,000.00'; the other candidate files carry no money-string pins",
      "464b7a37 is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-50 amendment 1 @095401b6be (464b7a37, merged 3f76cdb2).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T06:34:18Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S7",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "F30-AC4 needed a status-less envelope that public-status.ts's producer-faithful rule refuses.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S7",
      "fe-s-30/_scenarios.ts adds performanceEnvelopeNoStatus(); F30-AC4 re-scoped as class R; public-status.ts untouched. The row cites ruling '101449'; the CTO's ruling is msg 101448 (see header)",
      "464b7a37 is an ancestor of local portal DEV 3f76cdb2"
    ],
    "remedy": "Executed: IV-e-50 amendment 1 (464b7a37, merged 3f76cdb2).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T06:34:18Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W21-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "After IV-e-32 and IV-e-35 the suite still fails outside the class table's Q rows (8 at local portal DEV 3f76cdb2).",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W21-S2",
      "CTO msg 101448 ('The bar moves; it is not lowered'; TO-IV-e-35, ADJUDICATION_v4 C-S31 and the packet cite it as 101449, an unrelated message)",
      "TO-IV-e-35 superseded @26f1fa6165 on CTO 101651 (merged, 31 -> 16 failing); the bar now TO-IV-e-50 (pending, parked)"
    ],
    "remedy": "TO-IV-e-50's IVE50-AC2 (only Q rows fail), or 1.0.0_SA_CTO's re-disposition of the bar.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-W23-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The Investor Reporting suite fails beyond the class table's Q rows and is not deterministic across full runs.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W23-S1",
      "CTO msg 101651 (in 2.0.0_SA_COO~D's read/): 'Row W23-S1 is disarmed by this ruling into ONE named harness cell ... 3 consecutive full runs give identical pass/fail sets'",
      "TO-IV-e-50 pending at HEAD: AC1 instance INVALID, AC2 FAIL (5 of 7 not Q rows); 8 failing at local portal DEV 3f76cdb2"
    ],
    "remedy": "TO-IV-e-50 (parked). Closes when IVE50-AC1 and AC2 pass, or when 1.0.0_SA_CTO re-disposes the bar (it waits on the W29-S8/S10 ruling).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S8",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "F45-AC9 (scripts/dev-live.mjs) and F57-AC2 (contracts/adapt.ts) fail on product paths no open order grants.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S8",
      "no CTO ruling on W29-S8 after msg 101768 (03:44Z) in the COO~D or COO~P inboxes; no open order grants scripts/dev-live.mjs or contracts/adapt.ts",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
    ],
    "remedy": "A 1.0.0_SA_CTO ruling: a product-path cell for the two tests, a wider Q allowance, or another disposition; then the cell it names.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-27T13:04:50Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S9",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IVE26-AC3 (iv-e-26.wire-regen.test.ts) failed 1 of 3 runs: a flaky test.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S9",
      "no task order grants iv-e-26.wire-regen.test.ts; no CTO ruling folds it into W23-S1",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
    ],
    "remedy": "A cell granting iv-e-26.wire-regen.test.ts makes it deterministic, or 1.0.0_SA_CTO folds it into IV-e-50's harness bar.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T15:32:06Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W29-S10",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Two independent 3-run samples of the suite gave different stable failing sets (15 vs 7), so 'only Q rows fail' cannot be graded deterministically on this machine.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S10",
      "IV-e-50 result: two 3-run samples, 15 vs 7 failing; no CTO ruling on W29-S10",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
    ],
    "remedy": "A 1.0.0_SA_CTO ruling on how the S7 bar is graded under run-to-run regimes (a follow-on cell, a wider Q allowance, or another disposition).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-S19",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Walk screenshots of real client data were committed with no ignore rule (only *.har was ignored), and two batches (28 PNGs) reached origin/CLOUD.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S19",
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S21 (closing evidence: untracked @cfed2c067b, *.shots/ ignored @01d82f1550)",
      "git ls-files of the three .shots folders at HEAD = 0; git check-ignore: deliverables/2.0.0_SA_COO~D/.gitignore:2 '*.shots/'",
      "origin/CLOUD tip 262d0e8d16 (fetched by 3.0.0_SA_CVO): git ls-tree lists 20 files in prod-uiwalk-20260926.shots (added @4f632208c5) and 8 in prod-walk-20260926.shots (added @9b5eed8f9d); w9-round7.shots (@a32823e232) is local-only; cfed2c067b is NOT an ancestor of origin/CLOUD"
    ],
    "remedy": "Local part executed by 2.0.0_SA_COO~D: untrack @cfed2c067b and ignore @01d82f1550. Open: 0.0.0_AB_MSTR pushes the untrack, so origin/CLOUD's tip carries 0 shots; whether to purge the pushed history is Andrew's decision (4.0.0_SA_CRO has told him). Disarm when git ls-tree origin/CLOUD over the three folders reads 0.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-09-27T20:00:23Z"
    }
  }
]
```
