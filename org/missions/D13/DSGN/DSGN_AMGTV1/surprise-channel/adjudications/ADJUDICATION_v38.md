# DSGN_AMGTV1 -- round 64 L9 grades (dell1)

<sweep_watermark>2026-10-09T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T12:20:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 2404, org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/ROUND64_CLOSE.md. zzp-1 AC3 MET (zzo-1's re-cut), zzp-2 AC3 MET (closes the zzo-3 carry). With round 63's grades (ADJUDICATION_v37), every order the PROD candidate c6c1eb2a carries is graded: zzo-2, zzo-3, zzp-1, zzp-2 MET; zzo-1 NOT MET and superseded by zzp-1 MET.

```json
[
  {
    "id": "DSGN_AMGTV1-D1-C-S33",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:20:00Z",
    "one_line": "TO-AV-zzp-1 AC3 MET (and the re-cut of round 63's failed zzo-1 now passes): ASML's Investment-thesis window prints the served description text under 'COMPANY DESCRIPTION' ('What started as a failing joint venture between ASM International and Philips ...'), and the Item 5 machine lines sit under a separate 'FROM THE FILING' heading with their cited passages. Cosmetic, for the next pass: the served text itself begins with a literal 'COMPANY DESCRIPTION:' (the heading repeated) and runs some sentences together with no space ('... supply chain.ASML is ...').",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: JUDGMENT criteria are graded at L9 by a seat that did none of the work, never self-graded.",
    "world_is": "TO-AV-zzp-1 AC3 MET (and the re-cut of round 63's failed zzo-1 now passes): ASML's Investment-thesis window prints the served description text under 'COMPANY DESCRIPTION' ('What started as a failing joint venture between ASM International and Philips ...'), and the Item 5 machine lines sit under a separate 'FROM THE FILING' heading with their cited passages. Cosmetic, for the next pass: the served text itself begins with a literal 'COMPANY DESCRIPTION:' (the heading repeated) and runs some sentences together with no space ('... supply chain.ASML is ...').",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T121451Z/shots/008-ASML-Thesis-window.png: 'COMPANY DESCRIPTION' heading, description prose, 'FROM THE FILING' heading over the MACHINE Item 5 lines (PARAGRAPH 31 ...)",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/ROUND64_CLOSE.md real-run table"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  },
  {
    "id": "DSGN_AMGTV1-D1-C-S34",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:20:00Z",
    "one_line": "TO-AV-zzp-2 AC3 MET (and closes round 63's zzo-3 carry): after the figure press the cited passage is focused and in view -- window-press.json records the press on [data-sentence-press], focus on BLOCKQUOTE#thesis-passage-0-0 (data-thesis-passage P0405), focused_in_view true, and shot 009 shows the pressed sentence underlined with its passage directly beneath; after the press on the ASML NA listing, shot 005 is ASML NA's own page (ASML Holding NV, ASML NA, EUR 1593.20, Thesis tab).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: JUDGMENT criteria are graded at L9 by a seat that did none of the work, never self-graded.",
    "world_is": "TO-AV-zzp-2 AC3 MET (and closes round 63's zzo-3 carry): after the figure press the cited passage is focused and in view -- window-press.json records the press on [data-sentence-press], focus on BLOCKQUOTE#thesis-passage-0-0 (data-thesis-passage P0405), focused_in_view true, and shot 009 shows the pressed sentence underlined with its passage directly beneath; after the press on the ASML NA listing, shot 005 is ASML NA's own page (ASML Holding NV, ASML NA, EUR 1593.20, Thesis tab).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read tmp/ui-walk/20261009T121451Z/window-press.json: pressed true, focused BLOCKQUOTE thesis-passage-0-0, focused_in_view true",
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T121451Z/shots/009-ASML-Thesis-window-press-1.png and shots/005-ASML-press-1.png",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/ROUND64_CLOSE.md real-run table"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  }
]
```
