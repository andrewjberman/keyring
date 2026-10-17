# TCKT_VNEXT: CVO adjudication, round 20 part 2 (the rendered read, R20RV-AC1J)

<sweep_watermark>2026-10-17T08:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-17.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-17T08:55Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_RENDER.md`, blob a3e2acc53423 (msg 10430; verified by `git hash-object`). Shots:
`org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/*.png` (six). The criterion is read from the order
`0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-R20-RV...md` line 53.

**What this seat read itself:**
- **The shots.** `filer_completed`, `coordinator_controls`, `bystander_no_control` and `meeting_form`, opened as images.
- **The contrast**, measured from `filer_completed`'s pixels (PIL; WCAG relative luminance):
  - the outcome-line band: background rgb(25,38,67), strongest text pixel rgb(23,51,114), **1.25:1**;
  - control on the same image, the row text "Meeting Request" on the same board: **10.10:1**. The instrument sees legible text where it
    exists, so 1.25:1 is the line, not the method.

## Grade

**TCKT_VNEXT.TO-R20-RV R20RV-AC1J NOT MET.**

The three clauses against the shots:
1. **"The filer's own ticket shows the meeting outcome line after the confirm and still after completion": NOT MET in the rendered page.**
   - The line "Confirmed for 2026-10-23 14:00 ET ... on Oct 17, 2026" is drawn on `filer_confirmed` and on `filer_completed` (status
     `completed`, no controls), so the R20-pt-1 behaviour holds.
   - But it is drawn at 1.25:1, navy ink on the dark navy board row. In the image it reads as a faint band, and a filer cannot read it.
   - "Shows" is graded as a person would see it, and the purpose of FWD-11's ACCEPT is "the filer reads confirmed or rescheduled on the
     ticket".
2. **"A viewer outside `routing.primary` sees no control": MET.** `bystander_no_control` has the row and the line and no controls panel.
   `coordinator_controls` has the white panel with the two "Confirm this time" buttons and the three optional fields, readable navy on
   white.
3. **"The meeting form renders readable on the light canvas": the form is readable; the canvas is not light.**
   - The Meeting Request form is a white panel with navy labels, readable.
   - The page around it (the New Ticket header and the board) is the dark theme, not the portal's light canvas. The clause's premise does
     not hold on this page. I do not grade the board's theme in this round; see row D2-C-S6.

One clause fails on the page as shipped on DEV `38d4f9473284`, and it is the one that decides FWD-11, so the criterion is NOT MET. This
also corrects this seat's `R20PT-AC4J MET` (ADJUDICATION_v9) in what it can claim. That grade was on the diff and ten tests that assert
words and never colour, and it stated "not rendered". It stands as a grade of the build, not of what a person sees.

**FWD-11 stays NOT REALIZED.** The re-shot of `filer_completed` after `R20-pt-5` (the CTO's ruling msg 10423: one-class fix plus a token
contrast test of at least 4.5:1) is the read that can flip it. The re-shot is graded on the image and a pixel measurement, as here.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S5",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-17T08:55Z",
    "one_line": "Round 20 part 2 L9: R20RV-AC1J NOT MET -- the filer's outcome line renders at 1.25:1 (navy on the dark board row), so the filer cannot read it; bystander clause MET; FWD-11 NOT REALIZED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-S59"
    ],
    "spec_asserts": "R20RV-AC1J: the filer's own ticket shows the meeting outcome line after the confirm and still after completion; a viewer outside routing.primary sees no control; the meeting form renders readable on the light canvas.",
    "world_is": "On DEV 38d4f9473284 the line is drawn after the confirm and after completion but at 1.25:1 (bg rgb(25,38,67), text rgb(23,51,114), measured by this seat from filer_completed; control text on the same image 10.10:1). The bystander shot has no controls; the coordinator shot has them. The form is a readable white panel on the dark theme.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_RENDER.md blob a3e2acc53423 (msg 10430)",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/filer_completed__tckt-r20-filer-20261017__TCK-20261017-da2a1987__localhost-5174.png",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/bystander_no_control__tckt-r20-view-20261017__TCK-20261017-da2a1987__localhost-5174.png",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/coordinator_controls__tckt-r20-coord-20261017__TCK-20261017-da2a1987__localhost-5174.png",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/meeting_form__tckt-r20-filer-20261017__no-ticket__localhost-5174.png"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; D2-S59's remedy is R20-pt-5 (CTO msg 10423), and its re-shot is the read that can flip FWD-11."
  },
  {
    "id": "TCKT_VNEXT-D2-C-S6",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-17T08:55Z",
    "one_line": "The Ticket Center board and its New Ticket panel render on a dark navy theme; the order's 'light canvas' clause and the portal colour law assume a light canvas.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Portal colour law (.claude/skills/frontend-dev): the light #F4F6FA canvas, white hairline panels, navy ink, one band per page; R20RV-AC1J reads 'the meeting form renders readable on the light canvas'.",
    "world_is": "In all six R20 shots the board rows and the New Ticket area are dark navy (row bg rgb(25,38,67)); only the meeting form and the coordinator controls are white panels. Any panel-ink component mounted directly on the board inherits the 1.25:1 class of defect (D2-S59 is the first instance).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/meeting_form__tckt-r20-filer-20261017__no-ticket__localhost-5174.png",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/filer_completed__tckt-r20-filer-20261017__TCK-20261017-da2a1987__localhost-5174.png"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Outside round 20's cells; recorded for the CTO's round-20 analysis (whether the board's theme is in scope, and that a contrast test belongs beside any component mounted on the board)."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
