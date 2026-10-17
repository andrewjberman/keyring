# TCKT_VNEXT: CVO adjudication, round 20 part 3 (the contrast fix and its re-shot)

<sweep_watermark>2026-10-17T09:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-17.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-17T09:30Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_RESHOT.md`, blob 23f2afefdaa0 (msg 10468; verified by `git hash-object`). Criteria read
from their orders: `R20PF-AC4J` in `task-orders/TCKT_VNEXT.TO-R20-PF...md`, and `R20RV2-AC2J` in TV2's `TCKT_VNEXT.TO-R20-RV2...md`.

**What this seat read itself:**
- **The shot.** `r20_reshot/filer_completed__...__dev-539b1ee70ba1.png`, opened as an image. It shows the row `TCK-20261017-da2a1987`,
  `completed`, and under it "Confirmed for 2026-10-23 14:00 ET (R20 run 20261017) by tckt-r20-coord-20261017@opal.invalid on Oct 17,
  2026" in light ink, as legible as the row's own text. No controls panel.
- **The contrast**, measured from the PNG's pixels (PIL, WCAG relative luminance): the outcome band is text rgb(209,212,217) on rgb(25,38,67),
  **10.10:1**; the row's own text on the same image is 10.10:1. The same method read 1.25:1 on this ticket before the fix (v11).
- **The refs.** Portal ls-remote: `origin/DEV` `539b1ee70ba1`, which contains the DEV cherry-pick `6cc2035ac1`. The branches
  `cand/dell2/tckt-outcome-line-contrast` `4ae7278d9508` and `-prodfix` `2a64d2115f7e`.
- **The diffs.** `git -C portal diff 4e1e35bf 4ae7278d`: two files, the one-line class change and the new 150-line contrast test.
  `6cc2035ac1` and `2a64d2115f` are each the same 2 files (+151 -1).

## Grades

**TCKT_VNEXT.TO-R20-RV2 R20RV2-AC2J MET.**
- The filer's own completed ticket shows the confirmed outcome line, readable on the board row at 10.10:1 (4.5:1 is the floor), with no
  control. This is what v11 found missing.

**TCKT_VNEXT.TO-R20-PF R20PF-AC4J MET.**
- The line's class goes from `${INK}` (navy) to `text-white/80`, and it reads at 10.10:1 on the board row, measured above.
- Nothing else in `MeetingRequestParts.tsx` changed, so `MeetingOutcomeControls` keeps its white panel and navy ink. v11's
  `coordinator_controls` shot read it navy on white.
- The other file is the test.
- One limit on the test: its two inputs are measured colours, because the row background does not resolve from `src/index.css` tokens.
  The criterion admits "the stated measured value", so it guards the class against that pair but would not catch a token change.

## FWD-11

**FWD-11: the DEV leg is EXERCISED; NOT REALIZED until the PROD leg is read.** The DONE WHEN is "on DEV, then PROD by 2026-10-24". On DEV,
every act is now shown on artifacts:
- the filing (R18 PART 1 and R20);
- the OPEN ticket routed to the coordinator alone;
- the coordinator's confirm on the board (R18, and R20 `coordinator_controls`);
- the filer reading the outcome on the same ticket after completion: readable at 10.10:1 (this re-shot).

The before-completion state draws the same component with the same class, so this fix covers it too; that state was not re-shot.

Still open:
- The coordinator was a synthetic stand-in for jeanette (the CTO's ruling (b)).
- The PROD promote (row 70b4) and its own PROD read are in flight.
- The "light canvas" clause and row D2-C-S6 (the board's dark theme) are unchanged.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S7",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-17T09:30Z",
    "one_line": "Round 20 part 3 L9: R20RV2-AC2J MET and R20PF-AC4J MET -- the filer's completed ticket reads the confirmed outcome at 10.10:1 (was 1.25:1); FWD-11 DEV leg exercised, PROD leg owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-C-S5"
    ],
    "spec_asserts": "R20RV2-AC2J: the filer's own completed ticket shows the confirmed outcome line readable on the board row, no control. R20PF-AC4J: the line takes a light ink that reads at 4.5:1 or better; the controls panel keeps navy on white; nothing else changed.",
    "world_is": "On DEV 539b1ee70ba1 (contains 6cc2035ac1) the completed ticket TCK-20261017-da2a1987 shows the outcome line at 10.10:1, measured by this seat from the re-shot PNG (control: row text 10.10:1); the portal diff is the one class plus a test file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_RESHOT.md blob 23f2afefdaa0 (msg 10468)",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_reshot/filer_completed__tckt-r20-filer-20261017__TCK-20261017-da2a1987__localhost-5174__dev-539b1ee70ba1.png",
        "git -C portal diff 4e1e35bf 4ae7278d; portal ls-remote DEV 539b1ee70ba1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; the D2-C-S5 defect (1.25:1) is fixed on DEV and read at 10.10:1."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
