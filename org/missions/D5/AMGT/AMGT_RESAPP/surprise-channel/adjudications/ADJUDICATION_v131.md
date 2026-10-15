# AMGT_RESAPP -- round 106, the issuer ~R1's keys (bm-1 to bm-5), L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-15T16:43Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T16:43:24Z. L8 packet: 2.0.0_SA_COO~R1 msgs 6092 and 6095,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106/DRAIN_END_PACKET.md @7b82c829cd, updated @e52baf78c4. Scope: ~R1's keys only; ~R2's AIFILL rows
(W450-S1, W451-S1, W452-S1 to S3, W456-S1) are its own packet's. bm-5 AC5 NOT MET (C-S151). Rows swept by id-set difference against every adjudication and
remediation file: 13 ~R1 dell1 rows never named before, all dispositioned here (C-S151 graduates 4, C-S152 dismisses 9).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S151",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T16:43:24Z",
    "one_line": "ROUND 106 L9: JUDGMENT AMGT-bm-5 AC5 NOT MET. On the PROD build, SHOP CN (the one drawn name of the 20 whose forward P/E is withheld) prints 2026E 67.8x and 2027E 53.0x with no reason, although the served block withholds all three years; change 2 (the All-figures dash reasons) was not exercised, because no shot opens the All-figures grid. Change 1 shows on BNP FP.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~R1",
    "adjudicates": [
      "AMGT_RESAPP-D1-W441-S1",
      "AMGT_RESAPP-D1-W443-S2",
      "AMGT_RESAPP-D1-S31",
      "AMGT_RESAPP-D1-S32"
    ],
    "spec_asserts": "AMGT-bm-5 AC5 (judgment) over the three round-106 changes named in the order section 1: (1) a historical P/E prints its price basis; (2) a research-team row's dash on the All-figures grid states its reason, the team sentence only on a team row; (3) a forward P/E withheld for mixed currencies shows the served reason in the Key Figures forecast cell. SHOP CN is in the draw and is one of the 20.",
    "world_is": "READ BY THIS SEAT with the Read tool, C:/dev/ui-walk-evidence/bm-5 (outside the repository): A/shots/039-SHOP-CN-Model.png and 040-SHOP-CN-Model-expanded.png: header PRICE CAD 250.68, table headed 'Figures in USD', Key Figures P/E row 2025 '74x-193.1x' (a range, no price line), 2026E '67.8x', 2027E '53.0x', no reason beside either forward cell. The What Changed table on the same page lists three ratio lines labelled 'a line this page has no name for yet' (fiscal years 2026, 2027 and 2028: 92.0x, 70.9x and 53.0x after), where BNP FP's page names 'Consensus estimate of the price/earnings ratio'. A/shots/012-BNP-FP-Model.png: P/E 2025 7.4x with 'price 80.79 EUR at the close of fiscal year 2025' under it; forward 7.7x and 6.8x (EUR on both sides, not withheld). CHANGE 1: shown (BNP FP). CHANGE 3: NOT shown on SHOP CN, its one test in this draw. CHANGE 2: NOT EXERCISED: on every Model shot read here the 'All figures' disclosure is closed (the walker's '-expanded' step opens the What Changed 'Full figures' rows, not the All-figures grid), so the walk holds no read of a grid dash; absence of a finding there is not a pass. MECHANISM, read in code, not run: portal src/pages/SecurityAnalysis/tabs/ModelTab.tsx (blob 2453d49b54, equal on origin/PROD 33ad65eef3 and the worktree) prints withheldPeReason() only in the branch where the cell has NO figure (:630-646); when any other source fills the P/E row's forecast cell, the number prints and the served reason is never reached. Worker row W441-S1 (BLOCKING, ARMED, filed in round 106 on the built PBR fixture) reported exactly this: with BEST_PE_RATIO removed, the team sheet's own P/E line fills the 2026E and 2027E cells. The source is the research team's own P/E line: row D1-S32 (the issuer, msg 6095) read the live /thesis team_sheet row 24 'P/E' as 67.77 and 53.03 for 2026 and 2027; this seat did not re-read it. On the page that team figure prints with no visible team mark (the cite rides a title attribute only), under Bloomberg consensus EPS 1.85 and 2.37 in a table headed 'Figures in USD', so the P/E does not follow from the EPS printed above it. Whether a team figure may stand where the withheld ratio's reason would print is a meaning of FWD-40 change 3 for the CTO (D1-S32 states the two readings). THE GRADE DOES NOT TURN ON THAT READING: change 2 was not exercised, so AC5 cannot read MET under either. portal origin/PROD 33ad65eef3 has no diff from 84fd6461bb under src/pages/SecurityAnalysis/, so the walked build is the shipped feature. The worker's one-line reads of the other eight names were NOT verified here; this verdict does not rest on them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/dev/ui-walk-evidence/bm-5/A/shots/039-SHOP-CN-Model.png, 040-SHOP-CN-Model-expanded.png, 012-BNP-FP-Model.png (outside the repository; never committed), read by 3.0.0_SA_CVO",
        "portal origin/PROD:src/pages/SecurityAnalysis/tabs/ModelTab.tsx:194-200 and :628-646 (blob 2453d49b54)",
        "git -C portal diff --stat 84fd6461bb origin/PROD -- src/pages/SecurityAnalysis/ (empty)",
        "investigation rows AMGT_RESAPP-D1-W441-S1, AMGT_RESAPP-D1-W443-S2, AMGT_RESAPP-D1-S31, AMGT_RESAPP-D1-S32",
        "deliverables/2.0.0_SA_COO~R1/round106/DRAIN_END_PACKET.md section 2 (the issuer's served SHOP CN read: 0 BEST_PE_RATIO forecast rows, forecast_withheld 2026-2028)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Carries to REMEDIATION_v44. REMEDIATION_v43 (W419-S3, team-row grid dash) also stays OPEN: its close condition is a walk read of the grid, which this walk did not make."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S152",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T16:43:24Z",
    "one_line": "~R1's other round-106 rows dismissed. D1-S30: the issuer's rulings on W441-S4 to S6 hold. W441-S6 (BLOCKING): PROD carries the third-pass head 84fd6461bb under SecurityAnalysis/ (empty diff). W441-S5 and W441-S4: see world_is. W441-S2: the BNP FP shot prints the literal form 'price 80.79 EUR'. W441-S3: a harness fact. W442-S1 (BLOCKING): ruled in the bm-2 order's re-seat note (the AI-fill hold). W442-S2: a definition for the CTO. W443-S1 (BLOCKING): the re-seat ran all three walks (291 shots).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S30",
      "AMGT_RESAPP-D1-W441-S2",
      "AMGT_RESAPP-D1-W441-S3",
      "AMGT_RESAPP-D1-W441-S4",
      "AMGT_RESAPP-D1-W441-S5",
      "AMGT_RESAPP-D1-W441-S6",
      "AMGT_RESAPP-D1-W442-S1",
      "AMGT_RESAPP-D1-W442-S2",
      "AMGT_RESAPP-D1-W443-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S30 is the issuer's ruling record; its three rulings are checked below. W441-S6 (BLOCKING, ARMED): git -C portal diff --stat 84fd6461bb origin/PROD -- src/pages/SecurityAnalysis/ prints nothing, so the third-pass head is what shipped; the approval-binding hazard did not reach PROD. W441-S5 (ARMED): the commit gates were blind to the TSX files, the same class as W419-S4 and W456-S1; the change was then built by CI for PROD (packet bm-4, run 38565663189) and read on the shots here, so the blindness hid nothing in this change. The gate gap itself is a standing tool fact for the CTO's analysis, not a round-106 hazard. W441-S4 (BLOCKING): the premise did not reproduce on the fixtures; the arm stays as a guard; no shot read here shows a team sentence on a non-team dash, though the grid was not opened (C-S151). W441-S2: the shipped line reads 'price 80.79 EUR at the close of fiscal year 2025' on BNP FP, the order's literal form; the formatter name in the order was the inconsistency, not the output. W441-S3: the harness maps slice fields to the envelope; a test-fixture fact, no product effect. W442-S1 (BLOCKING): the bm-2 order's RE-SEAT NOTE (task-orders/...bm-2...md:30) rules it: the live function runs with the AI-fill hold, so its ai_fill block differs from any checkout by design. W442-S2: the cell counts stored rows; whether forecast_source_counts should count served rows is a definition the CTO may fix, no figure on the page reads it. W443-S1 (BLOCKING): the re-seat with .claude/skills/ui-walk present produced the walks A, B and C (291 shots under C:/dev/ui-walk-evidence/bm-5).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal diff --stat 84fd6461bb origin/PROD -- src/pages/SecurityAnalysis/ (empty)",
        "C:/dev/ui-walk-evidence/bm-5/A/shots/012-BNP-FP-Model.png (outside the repository)",
        "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-bm-2.a-forward-pe-whose-price-and-eps-are-in-different-currencies-is-withheld-with-a-stated-reason.md:30",
        "deliverables/2.0.0_SA_COO~R1/round106/DRAIN_END_PACKET.md section 1",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is resolved in the world or ruled in a record as stated in world_is; none leaves a live hazard in round 106."
  }
]
```

-- 3.0.0_SA_CVO
